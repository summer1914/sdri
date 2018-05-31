from wtforms import Form, StringField, IntegerField, ValidationError, FloatField
from wtforms.validators import Email, InputRequired, Length, EqualTo
import cache
from models import User
from flask import g


class BaseForms(Form):
    def get_error(self):
        message = self.errors.popitem()[1][0]
        return message


class LoginForm(BaseForms):
    email = StringField(validators=[Email(message='请输入正确的邮箱格式'), InputRequired(message='请输入邮箱！')])
    password = StringField(validators=[Length(6, 20, message='请输入正确格式的密码')])
    remember = IntegerField()


class ResetpwdForm(BaseForms):
    oldpwd = StringField(validators=[Length(6, 20, message='请输入正确格式的旧密码')])
    newpwd = StringField(validators=[Length(6, 20, message='请输入正确格式的新密码')])
    newpwd2 = StringField(validators=[EqualTo("newpwd", message='确认密码必须和新密码保持一致')])


class ResetEmailForm(BaseForms):
    email = StringField(validators=[Email(message='请输入正确格式的邮箱！')])
    captcha = StringField(validators=[Length(min=6, max=6, message='请输入正常长度的验证码！')])

    def validate_captcha(self, field):
        # 表单提交的验证码
        captcha = field.data
        # 表单提交的email
        email = self.email.data
        # 缓存email
        captcha_cache = cache.get(email)

        if not captcha_cache and captcha.lower() != captcha_cache.lower():
            raise ValidationError('邮箱验证码错误！')

    def validate_email(self, field):
        email = field.data
        user = g.user
        if user.email == email:
            raise ValidationError('不能修改为相同的邮箱！')


class RegisterForm(BaseForms):
    username = StringField(validators=[Length(1, 20, message='请输入正确的账号格式'), InputRequired(message='请输入用户名')])
    email = StringField(validators=[Email(message='请输入正确的邮箱格式'), InputRequired(message='请输入邮箱')])
    password = StringField(validators=[Length(6, 20, message='请输入正确格式的密码')])
    password2 = StringField(validators=[EqualTo("password", message='确认密码必须和新密码保持一致')])
    school = StringField()
    district = StringField()
    member = IntegerField()

    def validate_member(self, field):
        if field.data == None:
            raise ValidationError('请确定用户权限！')

    def validate_email(self, field):

        if User.query.filter(User.email == field.data).first():
            raise ValidationError('该邮箱已被注册请另外选择邮箱！')


class DataAddForm(BaseForms):
    schoolName = StringField(validators=[Length(1, 20, message='请输入正确的学校格式')])
    year = IntegerField()
    province = StringField(validators=[Length(1, 20, message='请输入正确省份')])
    city = StringField(validators=[Length(1, 20, message='请输入正确的城市')])
    county = StringField(validators=[Length(1, 20, message='请输入正确的区县')])
    sumStu = IntegerField()
    schoolPut = FloatField()
    studentAvg = FloatField()
    computerSum = IntegerField()
    multiClass = IntegerField()
    classSum = IntegerField()
    broadband = FloatField()
    effectPrepare = FloatField()
    pertinencePrepare = FloatField()
    optimizeTeach = FloatField()
    turnoverTeach = FloatField()
    manageCourse = FloatField()
    communicateCourse = FloatField()


class DataEditForm(DataAddForm):
    pass
