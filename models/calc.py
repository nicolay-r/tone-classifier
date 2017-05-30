#!/usr/bin/python
import pandas as pd
from sys import argv


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


def countDiff(rScores, eTwitID, eTwitScores):
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

if len(argv) < 4:
    print "Usage %s <task_type> <result.csv> <etalon.csv>" % argv[0]
    exit(0)

task = argv[1]
resultFilepath = argv[2]
etalonFilepath = argv[3]

if (task == 'bank'):
    scoreColumns = ['sberbank', 'vtb', 'alfabank', 'gazprom', 'bankmoskvy',
                    'raiffeisen', 'uralsib', 'rshb']
elif (task == 'ttk'):
    scoreColumns = ['beeline', 'mts', 'megafon', 'tele2', 'rostelecom',
                    'komstar', 'skylink']
else:
    raise "Task is not supported"
    exit(0)

calculations = {"positive": {'tp': int(0), 'fp': int(0),
                             'tn': int(0), 'fn': int(0)},
                "negative": {'tp': int(0), 'fp': int(0),
                             'tn': int(0), 'fn': int(0)}}

rdf = pd.read_csv(resultFilepath, sep=',')
edf = pd.read_csv(etalonFilepath, sep=',')

rScores = getScores(rdf, scoreColumns)
eScores = getScores(edf, scoreColumns)

for twitID in eScores.iterkeys():
    countDiff(rScores, twitID, eScores[twitID])

precision = {'positive': float(calculations['positive']['tp']) /
             (calculations['positive']['tp'] + calculations['positive']['fp']),
             'negative': float(calculations['negative']['tp']) /
             (calculations['negative']['tp'] + calculations['negative']['fp'])}

recall = {'positive': float(calculations['positive']['tp']) /
          (calculations['positive']['tp'] + calculations['positive']['fn']),
          'negative': float(calculations['negative']['tp']) /
          (calculations['negative']['tp'] + calculations['negative']['fn'])}

F = {'positive': 2 * ((precision['positive'] * recall['positive']) /
                      ((precision['positive'] + recall['positive']))),
     'negative': 2 * ((precision['negative'] * recall['negative']) /
                      ((precision['negative'] + recall['negative'])))}

Fr = (F['positive'] + F['negative']) / 2

print 'calculations --', calculations
print 'precision --', precision
print 'recall --', recall
print 'F --', F
print 'F_macro ', Fr
