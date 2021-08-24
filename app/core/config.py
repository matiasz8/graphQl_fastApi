import os
from typing import Dict

from starlette.config import Config

ROOT_DIR = os.getcwd()
_config = Config(os.path.join(ROOT_DIR, '.env'))
APP_VERSION = "0.0.1"
APP_NAME = "GraphQl API"
API_PREFIX = "/api"
