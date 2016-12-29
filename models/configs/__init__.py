import os

_curr_dir = os.path.dirname(os.path.abspath(__file__))

TWITTER_MESSAGE_PARSER_CONFIG = os.path.join(_curr_dir, 'msg.conf')
FEATURES_CONFIG = os.path.join(_curr_dir, 'features.conf')
MODEL_CONFIG = os.path.join(_curr_dir, 'model.conf')
# TODO connection config
