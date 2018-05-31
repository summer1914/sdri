from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from exts import db
from models import User, Role, CMSPermission

manager = Manager(app)

# 使用migrate绑定app和db
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-e', '--email', dest='email')
@manager.option('-r', '--role_id', dest='role_id')
def create_user(username, password, email, role_id):
    user = User(username=username, password=password, email=email, role_id=role_id)
    db.session.add(user)
    db.session.commit()
    print('cms用户添加成功！')


@manager.command
def create_role():
    # 1.教师权限，查看本校指数,修改个人信息
    teacher = Role(name='教师', desc='教师权限，查看本校指数,修改个人信息。')
    teacher.permission = CMSPermission.TEACHER

    # 2.学校管理者(学校管理者权限，修改个人信息，查看本校指数，学校排名与分析，学校诊断报告，数据录入，注册教师角色)
    school_manager = Role(name='学校管理者', desc='学校管理者权限，修改个人信息，查看本校指数，学校排名与分析，学校诊断报告，数据录入，注册教师角色')
    school_manager.permission = CMSPermission.SCHOOL

    # 3.区域管理员（区域管理者的权限，修改个人信息，查看学校排名与分析，学校检索,注册学校管理者角色）
    district_manager = Role(name='区域管理员', desc='区域管理者的权限，修改个人信息，查看学校排名与分析，学校检索,注册学校管理者角色。')
    district_manager.permission = CMSPermission.DISTRICT

    # 4.开发者
    developer = Role(name='系统开发者', desc='开发人员专用角色，具有所有权限，注册区域管理员账号。')
    developer.permission = CMSPermission.DEVELOPER

    db.session.add_all([teacher, school_manager, district_manager, developer])
    db.session.commit()


@manager.command
def test_permission():
    user = User.query.first()
    if user.is_developer:
        print ('这个用户有访问者的权限！')
    else:
        print('这个用户没有访问者的权限！')


if __name__ == '__main__':
    manager.run()
