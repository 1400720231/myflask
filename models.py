from exts import db
from datetime import datetime
class User(db.Model):
	# 表名字
	__tablename__ = "user"
	#　字段　id 整型　主键　自增长|django 中默认id为主键且自增长
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	telephone = db.Column(db.String(11), nullable=False)
	username = db.Column(db.String(50), nullable=False)
	password = db.Column(db.String(100), nullable=False)


class Question(db.Model):
	# 表名字
	__tablename__ = "question"
	#　字段　id 整型　主键　自增长|django 中默认id为主键且自增长
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String(100),nullable=False)
	content = db.Column(db.Text,nullable=False)
	# now()获取服务器第一次运行的时间 now：每次创建实例的时候的时间
	create_time = db.Column(db.DateTime,default=datetime.now)
	# 外键
	author_id = db.Column(db.Integer,db.ForeignKey("user.id"))
	#　相当于django的related_name="questions", author表示实例对象,
	author = db.relationship('User', backref=db.backref("questions"))
