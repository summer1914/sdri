from exts import db
from datetime import datetime
from werkzeug.security import check_password_hash


class CMSPermission(object):
    # 255的二进制方式表示1111 1111
    ALL_PERMISSION = 0b1111
    # 1.教师权限，查看本校指数,修改个人信息
    TEACHER = 0b0001
    # 2.学校管理者权限，修改个人信息，查看本校指数，学校排名与分析，学校诊断报告，数据录入，注册教师角色
    SCHOOL = 0b0010
    # 3.区域管理者的权限，查看学校排名与分析，学校检索,注册学校管理者角色
    DISTRICT = 0b0100
    # 4.开发者权限，拥有所有权限。
    DEVELOPER = 0b1000


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(200), nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    permission = db.Column(db.Integer, default=CMSPermission.TEACHER)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)
    school_name = db.Column(db.String(100), default=None)
    district_name = db.Column(db.String(100), default=None)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    user_role = db.relationship('Role', backref='role_users')

    parent_id = db.Column(db.Integer, default=None)


class Exponent(db.Model):
    __tablename__ = 'exponent'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 学校
    schoolName = db.Column(db.String(50), nullable=False)
    # 年份
    year = db.Column(db.String(50), nullable=False)
    # 学校地区
    schoolProvince = db.Column(db.String(50))
    schoolCity = db.Column(db.String(50))
    schoolCounty = db.Column(db.String(50))
    # 学校学生总数
    schoolStu = db.Column(db.Integer)
    # 学校年度投入
    schoolPut = db.Column(db.Float)
    # 区县生均经费
    studentAvg = db.Column(db.Float)
    # 计算机配置总数
    computerSum = db.Column(db.Integer)
    # 多媒体教室总数
    multiClass = db.Column(db.Integer)
    # 通用教室与专用教室总数
    classSum = db.Column(db.Integer)
    # 学校网络出口总宽带速度
    broadband = db.Column(db.Float)
    # 区县分配到学校平均值
    # broadbandAvg = db.Column(db.Float)
    # 教师备课教学效果指数值
    effectPrepare = db.Column(db.Float)
    # 教师备课教学针对性指数值
    pertinencePrepare = db.Column(db.Float)
    # 教师教学优化课堂指数值
    optimizeTeach = db.Column(db.Float)
    # 教师教学转变学习方式指数值
    turnoverTeach = db.Column(db.Float)
    # 课程管理指数值
    manageCourse = db.Column(db.Float)
    # 课程交流指数值
    communicateCourse = db.Column(db.Float)
    I = db.Column(db.Float)
    C1 = db.Column(db.Float)
    C2 = db.Column(db.Float)
    C3 = db.Column(db.Float)
    C = db.Column(db.Float)
    E1 = db.Column(db.Float)
    E2 = db.Column(db.Float)
    E3 = db.Column(db.Float)
    E = db.Column(db.Float)

    # 就绪指数
    final_index = db.Column(db.Float)
    create_time = db.Column(db.DateTime, default=datetime.now)
    add_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    add_user = db.relationship('User', backref='exponents')

    __mapper_args__ = {
        "order_by": -create_time
    }
