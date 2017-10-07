#!/usr/bin/python
import pandas as pd
from sys import argv
import configs


def markErrors(errorDf, etalonDf, scoreColumns):
    """
    Adds correct answers for values in scoreColumns
    """
    for twitID in errorDf['twitid']:
        errorRow = errorDf[errorDf['twitid'] == twitID]
        errorRowIndex = errorRow.index[0]
        for columnName in scoreColumns:
            row = etalonDf[etalonDf['twitid'] == twitID]
            rowIndex = row.index[0]
            if row[columnName].isnull()[rowIndex]:
                continue
            errorDf[columnName][errorRowIndex] = \
                '{}({})'.format(errorRow[columnName][errorRowIndex],
                                int(row[columnName][rowIndex]))


def getScores(df, scoreColumns):
    result = {}
    for rowIndex in range(len(df)):
        scores = {}
        twitID = df['twitid'][rowIndex]
        for columnName in scoreColumns:
            val = df[columnName][rowIndex]
            if df[columnName].isnull()[rowIndex]:
                continue
            scores[columnName] = int(val)

        result[twitID] = scores
    return result


def countDiff(rScores, eTwitID, eTwitScores, calculations, errorTwitIDs):
    if (eTwitID in rScores):
        rTwitScores = rScores[eTwitID]
        for key in rTwitScores.iterkeys():

            if key not in eTwitScores:
                continue

            rv = rTwitScores[key]
            ev = eTwitScores[key]
            assert(type(rv) == int)
            assert(type(ev) == int)
            if (ev == rv):
                if (ev > 0):
                    calculations['positive']['tp'] += 1
                elif (ev < 0):
                    calculations['negative']['tp'] += 1
            else:
                errorTwitIDs.add(eTwitID)

            if (ev != rv):
                if (ev <= 0):
                    if (rv == 1):
                        calculations['positive']['fp'] += 1

                if (ev >= 0):
                    if (rv == -1):
                        calculations['negative']['fp'] += 1

                if (ev > 0):
                    calculations['positive']['fn'] += 1
                elif (ev < 0):
                    calculations['negative']['fn'] += 1

            if (ev != 1):
                if (rv != 1):
                    calculations['positive']['tn'] += 1

            if (ev != -1):
                if (rv != -1):
                    calculations['negative']['tn'] += 1


def check(task_type, result_table, etalon_table, error_filepath=None):
    """
    tast_type : str
        'bank' or 'ttk'
    result_table : srt
        path to a csvfile with classifier results
    etalon_table : str
        path to a csv file with etalon results

    returns : dict
        result information
    """
    if (task_type == 'bank'):
        scoreColumns = configs.DATA_BANK_FIELDS
    elif (task_type == 'ttk'):
        scoreColumns = configs.DATA_TCC_FIELDS
    else:
        raise "Task is not supported"
        exit(0)

    errorTwitIDs = set()
    calculations = {"positive": {'tp': int(0), 'fp': int(0),
                                 'tn': int(0), 'fn': int(0)},
                    "negative": {'tp': int(0), 'fp': int(0),
                                 'tn': int(0), 'fn': int(0)}}

    rdf = pd.read_csv(result_table, sep=',')
    edf = pd.read_csv(etalon_table, sep=',')

    rScores = getScores(rdf, scoreColumns)
    eScores = getScores(edf, scoreColumns)

    for twitID in eScores.iterkeys():
        countDiff(rScores, twitID, eScores[twitID], calculations, errorTwitIDs)

    e = 1e-10
    precision = {'positive': float(calculations['positive']['tp']) /
                 (calculations['positive']['tp'] +
                  calculations['positive']['fp'] + e),
                 'negative': float(calculations['negative']['tp']) /
                 (calculations['negative']['tp'] +
                  calculations['negative']['fp'] + e)}

    recall = {'positive': float(calculations['positive']['tp']) /
              (calculations['positive']['tp'] +
               calculations['positive']['fn'] + e),
              'negative': float(calculations['negative']['tp']) /
              (calculations['negative']['tp'] +
               calculations['negative']['fn'] + e)}

    F = {'positive': 2 * ((precision['positive'] * recall['positive']) /
         ((precision['positive'] + recall['positive'] + e))),
         'negative': 2 * ((precision['negative'] * recall['negative']) /
                          ((precision['negative'] + recall['negative'] + e)))}

    Fr_macro = (F['positive'] + F['negative']) / 2

    precision_micro = ((calculations['positive']['tp'] +
                       calculations['negative']['tp']) /
                       (calculations['positive']['tp'] +
                        calculations['negative']['tp'] +
                        calculations['positive']['fp'] +
                        calculations['negative']['fp'] + e))

    recall_micro = ((calculations['positive']['tp'] +
                     calculations['negative']['tp']) /
                    (calculations['positive']['tp'] +
                     calculations['negative']['tp'] +
                     calculations['positive']['fn'] +
                     calculations['negative']['fn'] + e))

    Fr_micro = (2 * (precision_micro * recall_micro) /
                (precision_micro + recall_micro))

    errorDf = rdf[rdf['twitid'].isin(list(errorTwitIDs))]

    if (error_filepath is not None):
        markErrors(errorDf, edf, scoreColumns)
        if (error_filepath is not None):
            errorDf.to_csv(error_filepath)

    return {"error_filepath": error_filepath,
            "calculations": calculations,
            "precision": precision,
            "recall": recall,
            "F": F,
            "F_macro": Fr_macro,
            "F_micro": Fr_micro}


def show(result, filename=None):
    """
    result : dict
        display results
    filename : str
        filepath to output result
    """

    s = 'calculations -- {}\n precision -- {}\nrecall -- {}\nF -- {}\nF_macro -- {}\nF_micro -- {}\n'.format(
        result['calculations'], result['precision'], result['recall'],
        result['F'], result['F_macro'], result['F_micro'])

    if filename is None:
        print s
    else:
        with open(filename, "a+") as out:
            out.write(s)


if __name__ == "__main__":
    if len(argv) < 5:
        print "Usage %s <task_type> <result.csv> <etalon.csv> <errors.csv>" % \
                argv[0]
        exit(0)

    task_type = argv[1]
    resultFilepath = argv[2]
    etalonFilepath = argv[3]
    errorFilepath = argv[4]

    result = check(task_type, resultFilepath, etalonFilepath, errorFilepath)
    show(result)
