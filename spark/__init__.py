import os
from flask import Flask
from itsdangerous import TimestampSigner

app = Flask(__name__)

def get_env():
    local_settings_found = os.path.exists(os.path.join(os.path.dirname(__file__), 'config', 'local.py'))
    return os.environ.get('SPARK_APPLICATION_SETTINGS', 'local'  if local_settings_found else 'base')

def get_conf():
    return 'spark.config.%s.Configuration' % get_env()

app.config.from_object(get_conf())
app.signer = TimestampSigner(app.config['SIGNER_KEY'])

from . import views
from . import api


