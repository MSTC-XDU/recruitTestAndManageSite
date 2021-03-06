# -*- coding: utf-8 -*-
import os

import leancloud
from cloud import engine

APP_ID = os.environ['LC_APP_ID']
MASTER_KEY = os.environ['LC_APP_MASTER_KEY']

leancloud.init(APP_ID, master_key=MASTER_KEY)

application = engine
