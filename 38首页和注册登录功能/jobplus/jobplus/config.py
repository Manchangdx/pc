class BaseConfig:
    SECRET_KEY = 'shiyanlou'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/jobplus?charset=utf8'

class ProConfig(BaseConfig):
    pass

configs = {
    'dev': DevConfig,
    'pro': ProConfig
}
