# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", '6795023'))
    API_HASH = os.environ.get("API_HASH", '48eb04ae416967495ba9930f87d4f4da')
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '1800034142:AAEyfzZJhELEDfXnuCCbdbFo_Zzm42n7Two')
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL", '-1001273138715'))
    DB_CHANNEL = int(os.environ.get("DB_CHANNEL")) or LOGS_CHANNEL
    MONGODB_URL = os.environ.get("MONGODB_URL", 'mongodb://mongo:wWp1Uq4pxGd0L88A3Owm@containers-us-west-65.railway.app:5653')
    BOT_OWNER = int(os.environ.get("BOT_OWNER", '1851062714'))
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/DKBOTZ"
    TG_MAX_SIZE = 2040108421
    # Gofile.io token
    GOFILE_TOKEN = os.environ.get("GOFILE_TOKEN", 'DKBOTZ')
    # Default chunk size (0.005 MB) Increase if you need faster downloads
    CHUNK_SIZE = 1024 * 6
