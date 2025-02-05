class config():
    SECRET_key = '0806fb170ceff1b2c8524d9890dbbaf9'

class developmentConfig(config):
    DEBUG = True
    MYSQL_HOST= 'localhost'
    MYSQL_USER= 'root'
    MYSQL_PASSWORD= '1234567890'
    MYSQL_DB= 'flask_practis_sql'

class ProductionsConfig(config):
    DEBUG = False
    MYSQL_HOST= 'localhost'
    MYSQL_USER= 'root'
    MYSQL_PASSWORD= '1234567890'
    MYSQL_DB= 'flask_practis_sql'

config = {
    'development' : developmentConfig,
    'productions' : ProductionsConfig
}