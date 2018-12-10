from exts import db

class User(db.Model):
	# 表名字
	__tablename__ = "user"
	#　字段　id 整型　主键　自增长|django 中默认id为主键且自增长
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	telephone = db.Column(db.String(11), nullable=False)
	username = db.Column(db.String(50), nullable=False)
	password = db.Column(db.String(100), nullable=False)
