from flask import Flask, render_template, request
from exts import db
# 引入配置文件
import config
app = Flask(__name__)
# 加载配置文件内容
app.config.from_object(config)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/login/", methods=["GET","POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")


@app.route("/register/")
def register():
	if request.method == "GET":
		return render_template("register.html")

if __name__ == "__main__":
    app.run()