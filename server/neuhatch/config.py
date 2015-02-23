import os

def get_default_config():
    c = Config()
    c.environ_set()
    return c

class Config:
    def __init__(self):
        self.consumer_key = None
        self.consumer_secret = None
        self.access_token = None
        self.access_token_secret = None
        self.app_secret = None
        self.database_uri = None
        self.database_user = None
        self.database_password = None
        self.hostname = "http://localhost:8000/"
    def environ_set(self):
        self.set_with_warning("CONSUMER_KEY")
        self.set_with_warning("CONSUMER_SECRET")
        self.set_with_warning("ACCESS_TOKEN")
        self.set_with_warning("ACCESS_TOKEN_SECRET")
        self.set_with_warning('APP_SECRET')
        self.set_with_warning('HATCH_DB_USER')
        self.set_with_warning('HATCH_DB_PASSWORD')
        self.set_with_warning('HATCH_DB_NAME')
        self.database_uri = os.getenv('DATABASE_URI',
            'postgres://{usr}:{pw}@db/{db}'.format(
                usr=self.hatch_db_user, pw=self.hatch_db_password,
                db=self.hatch_db_name))
#            'postgres://docker:docker@{}/neuhatch'.format(
#                os.getenv('DB_1_PORT_5432_TCP_ADDR')))

    def set_with_warning(self, var):
        val = os.environ.get(var)
        setattr(self, var.lower(), val)
        if getattr(self, var.lower()) is None:
            print "Warning %s is None" % var


