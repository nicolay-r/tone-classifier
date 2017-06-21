import io
from os.path import join
import os
import json


_curr_dir = os.path.dirname(os.path.abspath(__file__))

_data_config = join(_curr_dir, 'data.conf')
with io.open(_data_config, "r") as f:
    _data = json.load(f, encoding='utf-8')

# Task dependent score fields
DATA_TCC_FIELDS = _data['tcc']
DATA_BANK_FIELDS = _data['bank']

# Data folder and subfolders
DATA_ROOT = join(_curr_dir, _data['data_root_filepath'])
LEXICONS_ROOT = join(DATA_ROOT, _data['lexicons_folder'])
EMBEDINGS_ROOT = join(DATA_ROOT, _data['embeddings_folder'])
NETWORK_MODELS_ROOT = \
    join(DATA_ROOT, _data['network_models_folder'])

# Word embedding configuration files
TWITTER_MESSAGE_PARSER_FILENAME = _data['message_config_name']
FEATURES_FILENAME = _data['features_config_name']
W2V_FILENAME = _data['w2v_config_name']


TWITTER_MESSAGE_PARSER_CONFIG = join(
    EMBEDINGS_ROOT, TWITTER_MESSAGE_PARSER_FILENAME)

FEATURES_CONFIG = join(EMBEDINGS_ROOT, FEATURES_FILENAME)
W2V_CONFIG = join(EMBEDINGS_ROOT, W2V_FILENAME)
