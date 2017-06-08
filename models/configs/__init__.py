import io
import os
import json


_curr_dir = os.path.dirname(os.path.abspath(__file__))

TWITTER_MESSAGE_PARSER_CONFIG = os.path.join(_curr_dir, 'msg.conf')
FEATURES_CONFIG = os.path.join(_curr_dir, 'features.conf')
MODEL_CONFIG = os.path.join(_curr_dir, 'model.conf')

_connection_config = os.path.join(_curr_dir, 'connection.conf')
with io.open(_connection_config, "r") as f:
    CONNECTION_SETTINGS = json.load(f, encoding='utf-8')

_data_config = os.path.join(_curr_dir, 'data.conf')
with io.open(_data_config, "r") as f:
    _data_settings = json.load(f, encoding='utf-8')

DATA_ROOT = os.path.join(_curr_dir, _data_settings['data_root_filepath'])
LEXICONS_ROOT = os.path.join(DATA_ROOT, _data_settings['lexicons'])
DATA_TCC_FIELDS = _data_settings['tcc']
DATA_BANK_FIELDS = _data_settings['bank']
