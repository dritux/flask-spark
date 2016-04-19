import logging
import os

class BaseConfiguration(object):

    DEBUG = True

    LOGS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'logs'))
    LOG_TAG = 'FLASKSPARK'
    LOG_LEVEL = logging.DEBUG
    LOG_APP_LEVEL = logging.DEBUG
    LOG_RUNTIME_LEVEL = logging.DEBUG
    LOG_BUSINESS_LEVEL = logging.DEBUG

    SIGNER_KEY = ''
