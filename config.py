import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5833627856:AAFp3yWfj2ExBSAY7ko_0y-hIJe0AZ1655w")
    API_ID = int(os.environ.get("API_ID", 977080))
    API_HASH = os.environ.get("API_HASH", "0c20c4265501492a1513f91755acd42b")
    DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://abcd:abcd@cluster0.qirokuf.mongodb.net/?retryWrites=true&w=majority")
