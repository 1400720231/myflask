import os
DEBUG = True

# dialect+driver://username:password@host:port/database
# 数据库设置
DIALECT = "mysql"
DRIVER = "mysqlclient"
USERNAME ="panda"
PASSWORD = "250onion"
HOST = "localhost"
PORT = "3306"
DATABASE = "myflask"

# SQLALCHEMY_DATABASE_URI为固定写法
SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format\
						(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

# 改成False运行的时候就不会有警告
SQLALCHEMY_TRACK_MODIFICATIONS  = False


# flask的session加密的密钥串
SECRET_KEY = os.urandom(24)