from flask import Flask, render_template, request, redirect, url_for,session
from exts import db
from models import User
from decorators import login_required

# 引入配置文件
import config
app = Flask(__name__)
# 加载配置文件内容
app.config.from_object(config)
# 这句话的作用和他是一样的：db = SQLAlchemy(app), 因为我们为了防止循环引用分开了db,app所以用init_app()的方式
# 完成db = SQLAlchemy(app)的功能
db.init_app(app)




@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login/", methods=["GET","POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")
	else:
		telephone = request.form.get("telephone")
		password = request.form.get("password")
		user = User.query.filter(User.telephone ==telephone, User.password == password).first()
		# 如果登录成功
		if user:
			print(user.username)
			session["user_id"] = user.id
			# 31天内不需要重新登录
			# session.permanent = True
			return redirect(url_for("index"))

		else:
			return "手机号码或者密码错误，请确认后再登录"



@app.route("/register/",methods=["GET", "POST"])
def register():
	if request.method == "GET":
		return render_template("register.html")
	else:
		telephone = request.form.get("telephone")
		username = request.form.get("username")
		password1 = request.form.get("password1")
		password2 = request.form.get("password2")

		# 验证手机号码是否被注册了
		user = User.query.filter(User.telephone == telephone).first()
		if user:
			return "手机号码已经被注册，请更换手机号码"
		elif password2 != password1:
			return "两次密码不一致，请重新输入"
		else:
			user = User(telephone=telephone, username=username, password = password1)
			db.session.add(user)
			db.session.commit()
			return redirect(url_for("login"))


@app.route("/question/", methods=["GET","POST"])
@login_required
def question():
	if request.method == "GET":
		return render_template("question.html")
	else:
		pass


"""
钩子函数，插入上下文，实现了在所有的html中都可以使用变量user,来达到当用户登录就显示用户名，不登录就显示注册的效果，
django中已经封装好的这个方法，在所有的html中直接可以用user或者request.user变量对象，不用像这里一样手动封装一样user
"""
@app.context_processor
def my_context_processtor():
	user_id = session.get("user_id")
	if user_id:
		user = User.query.filter(User.id==user_id).first()
		if user:
			return {"user":user}
	return {"user":""}

if __name__ == "__main__":
    app.run()