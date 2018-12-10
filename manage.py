from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from zlktqa import app
from exts import db
# User 模型
from models import User
db.init_app(app)

manager = Manager(app)
# 使用Migrate绑定app和db
migrate = Migrate(app, db)
# 添加迁移脚本的命令带manager中
manager.add_command("db", MigrateCommand)


if __name__ == "__mian__":
    manager.run()


"""
migrate = Migrate(app, db):
    这行命令的作用就是把app中的models和db设置结合起来，因为如果不结合起来的话，
db,create_all()只能使用一次，之后在models添加新的字段db.create_all()将不会生效。
所以要用Migrate(app,db)结合起来，让添加字段后直接可以通过某个命令迁移成功。
manager.add_command("db", MigrateCommand)：
    此命令的意义就是上面让添加字段成功迁移的自定义命令：python manage.py db migrate
其中manage.py是此py的名字， db是manager.add_command("db", MigrateCommand)中的“db”，
migrate则是MigrateCommand中产生的，所以是必填的。

ps：
    如果要顺利完成models的迁移，还需要把model导入到这个py文件中
    第一次先执行：python manage.py db  init 

"""