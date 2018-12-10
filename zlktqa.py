from flask import Flask, render_template, request, redirect, url_for
from exts import db
from models import User
# 引入配置文件
import config
app = Flask(__name__)
# 加载配置文件内容
app.config.from_object(config)

db.init_app(app)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/login/", methods=["GET","POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")


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


if __name__ == "__main__":
    app.run()