#!/usr/bin/python
import utils
import json
import logging
from sys import argv
from os.path import join
import configs

features_file = join(configs.EMBEDINGS_ROOT, configs.FEATURES_FILENAME)

if len(argv) == 1:
    print "usage: ./{} <type> <name> <enabled (0 or 1)>".format(argv[0])
    print "Chages options in {}".format(features_file)
    print "type: 'lexicons' or 'clustered_words'"
    print "name: feature name"
    print "enabled: 0 or 1"
    exit()

feature_type = argv[1]
feature_name = argv[2]
if (argv[3] == "1"):
    enabled = "true"
else:
    enabled = "false"

utils.init_logger()

logging.info("set {}[{}] = {}".format(feature_type, feature_name, enabled))
with open(features_file, "r") as ff:
    features = json.load(ff)
    features[feature_type]['$' + feature_name]['enabled'] = enabled

logging.info("save: {}".format(features_file))
with open(features_file, "w") as ff:
    json.dump(features, ff, indent=4, sort_keys=True)
