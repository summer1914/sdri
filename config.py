import os

SECRET_KEY = os.urandom(24)

DEBUG = True

DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_HOST = 'sdri_db_3306'
DB_PORT = 3306
DB_NAME = 'sdri'

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 发送者邮箱的服务器地址
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = '587'
MAIL_USE_TLS = True
# MAIL_USE_SSL : default False

MAIL_USERNAME = "409322382@qq.com"
MAIL_PASSWORD = "uxveqvagrbesbhgd"
MAIL_DEFAULT_SENDER = "409322382@qq.com"
