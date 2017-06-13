import io
import os
import json


_curr_dir = os.path.dirname(os.path.abspath(__file__))

_data_config = os.path.join(_curr_dir, 'data.conf')
with io.open(_data_config, "r") as f:
    _data_settings = json.load(f, encoding='utf-8')

# Task dependent score fields
DATA_TCC_FIELDS = _data_settings['tcc']
DATA_BANK_FIELDS = _data_settings['bank']

# Data folder and subfolders
DATA_ROOT = os.path.join(_curr_dir, _data_settings['data_root_filepath'])
LEXICONS_ROOT = os.path.join(DATA_ROOT, _data_settings['lexicons_folder'])
EMBEDINGS_ROOT = os.path.join(DATA_ROOT, _data_settings['embeddings_folder'])

# Word embedding configuration files
TWITTER_MESSAGE_PARSER_CONFIG = os.path.join(EMBEDINGS_ROOT, 'msg.conf')
FEATURES_CONFIG = os.path.join(EMBEDINGS_ROOT, 'features.conf')
MODEL_CONFIG = os.path.join(EMBEDINGS_ROOT, 'model.conf')
