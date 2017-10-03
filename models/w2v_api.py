#!/usr/bin/python
import utils
import json
import logging
from sys import argv
from os.path import join
import configs

models_file = join(configs.EMBEDINGS_ROOT, configs.W2V_FILENAME)

if len(argv) == 1:
    print "usage: ./{} <model_name> <enabled (0 or 1)>".format(argv[0])
    print "Chages options in {}".format(models_file)
    print "model_name: feature name"
    print "enabled: 0 or 1"
    exit()

model_name = argv[1]
if (argv[2] == "1"):
    enabled = "true"
else:
    enabled = "false"

utils.init_logger()

logging.info("set w2v[{}] = {}".format(model_name, enabled))
with open(models_file, "r") as ff:
    features = json.load(ff)
    features["w2v_models"][model_name]['enabled'] = enabled

logging.info("save: {}".format(models_file))
with open(models_file, "w") as ff:
    json.dump(features, ff, indent=4, sort_keys=True)
