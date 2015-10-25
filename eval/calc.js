/**
 * node calc.js <type> result.xml etalon.xml
 * type - ttk, bank
 */

function getTwit(children) {
    var result = {
        twitid: undefined,
        values: {}
    };
    for (var j = 0; j < children.length; j++) {
        var child = children[j];
        if (child.name() == 'column') {
            var object = child.attr('name').value();
            if (object == 'twitid') {
                result.twitid = child.text();
            }
            if (objects.indexOf(object) != -1) {
                var objectResult = child.text();
                if (objectResult != 'NULL') {
                    result.values[object] = parseInt(objectResult);
                }
            }
        }
    }
    return result;
}

function countDiff(resultTwits, etalonTwit) {
    var resultTwit = resultTwits[etalonTwit.twitid];
    if (resultTwit.twitid == etalonTwit.twitid) {
        for(var object in resultTwit.values) {
            var etalonValue = etalonTwit.values[object]
                , resultValue = resultTwit.values[object];

            if (etalonValue == resultValue) {
                if (etalonValue > 0) {
                    calculations['positive'].tp++;
                    /*    calculations['negative'].tn++; */
                } else if( etalonValue < 0) {
                    calculations['negative'].tp++;
                    /*    calculations['positive'].tn++; */
                }
            }

            if (etalonValue !== resultValue) {
                if (etalonValue <= 0) {
                    if (resultValue==1) {
                        calculations['positive'].fp++;
                    }
                }

                if (etalonValue >=0 ) {
                    if (resultValue==-1) {
                        calculations['negative'].fp++;
                    }
                }

                if (etalonValue > 0) {
                    calculations['positive'].fn++;
                } else if( etalonValue < 0) {
                    calculations['negative'].fn++;
                }

            }

            if (etalonValue !==1) {
                if (resultValue !==1) {
                    calculations['positive'].tn++;
                }
            }

            if (etalonValue !==-1) {
                if (resultValue !==-1) {
                    calculations['negative'].tn++;
                }
            }

        }

    }
}

var libxmljs = require('libxmljs')
    , fsExtra = require('fs-extra')
    , config = require('config')
    //, result = libxmljs.parseXml(fsExtra.readFileSync(config.get('twit-calc')['result-xml']))
    , result = libxmljs.parseXml(fsExtra.readFileSync(process.argv[3]))
    , etalon = libxmljs.parseXml(fsExtra.readFileSync(process.argv[4]))
    , objects = config.get(process.argv[2])
    , calculations = {
        'negative' : {
            tp : 0,
            tn : 0,
            fp : 0,
            fn : 0
        },
        'positive' : {
            tp: 0,
            tn : 0,
            fp : 0,
            fn : 0
        }
    };


var resultTwits = result.find('//pma_xml_export/database/table');
var etalonTwits = etalon.find('//pma_xml_export/database/table');
var resultTwitsHash = {};

for(var i = 0; i < resultTwits.length; i++) {
    var twitXml = resultTwits[i]
        , children = twitXml.childNodes()
        , twit = getTwit(children);
    resultTwitsHash[twit.twitid] = twit;
}

for(var i = 0; i < etalonTwits.length; i++) {
    var twit = etalonTwits[i]
        , children = twit.childNodes();
    countDiff(resultTwitsHash, getTwit(children));
}
var precision = {
    'positive' : calculations['positive'].tp / (calculations['positive'].tp + calculations['positive'].fp),
    'negative' : calculations['negative'].tp / (calculations['negative'].tp + calculations['negative'].fp)
};

var recall = {
    'positive' : calculations['positive'].tp / (calculations['positive'].tp + calculations['positive'].fn),
    'negative' : calculations['negative'].tp / (calculations['negative'].tp + calculations['negative'].fn)
};

var F = {
    'positive' : 2 * ((precision['positive'] * recall['positive']) / ((precision['positive'] + recall['positive']))),
    'negative' : 2 * ((precision['negative'] * recall['negative']) / ((precision['negative'] + recall['negative']))),
};

var F_R = (F['positive'] + F['negative']) / 2;

console.log('Counts    - ', 'positive', calculations['positive'], 'negative', calculations['negative']);
console.log('Precision - ', precision);
console.log('Recall    - ', recall);
console.log('F         - ', F);
console.log('F_R       - ', F_R);