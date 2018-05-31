from flask import Flask, render_template, redirect, url_for, request, session, g, views

import config
from forms import LoginForm, ResetpwdForm, RegisterForm, DataAddForm, ResetEmailForm, DataEditForm
from models import User, Exponent
from decorators import login_required
from exts import db, mail
import restful
from flask_mail import Message
import string, random
import cache
# from flask.ext.session import Session

app = Flask(__name__)
app.config.from_object(config)
# Session(app)
db.init_app(app)
mail.init_app(app)


@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/profile/')
@login_required
def profile():
    return render_template('profile.html')


@app.route('/schooldata/')
@login_required
def schooldata():
    if g.user.user_role.id != 1 and g.user.user_role.id != 2:
        return redirect(url_for('index'))
    else:

        if g.user.user_role.id == 1:
            id = g.user.parent_id
        else:
            id = g.user.id

        context = {
            'datas': Exponent.query.filter(Exponent.add_user_id == id).order_by(Exponent.create_time.desc())
        }

        return render_template('schooldata.html', **context)


@app.route('/schoolrank/')
@login_required
def schoolrank():
    if g.user.user_role.id != 2 and g.user.user_role.id != 3:
        return redirect(url_for('index'))
    else:
        if g.user.user_role.id == 2:
            user = User.query.filter(User.id == g.user.parent_id).first()
            context = {
                'datas': Exponent.query.order_by(Exponent.final_index.desc()).filter(
                    Exponent.schoolCounty == user.district_name).all()
            }
            return render_template('schoolrank.html', **context)

        else:
            user = User.query.filter(User.id == g.user.parent_id).first()
            print(user.district_name)
            context = {
                'datas': Exponent.query.order_by(Exponent.final_index.desc()).all()
            }

            return render_template('schoolrank.html', **context)


@app.route('/schoolsearch/')
@login_required
def schoolsearch():
    if g.user.user_role.id != 3:
        return redirect(url_for('index'))
    else:
        province = request.args.get('province')
        city = request.args.get('city')
        county = request.args.get('county')
        if city and county:
            pass

        return render_template('schoolsearch.html')


@app.route('/schoolreport/')
@login_required
def schoolreport():
    if g.user.user_role.id != 2:
        return redirect(url_for('index'))
    else:
        return render_template('schoolreport.html')


@app.route('/datamanage/')
@login_required
def datamanage():
    if g.user.user_role.id != 2:
        return redirect(url_for('index'))
    else:
        id = g.user.id

        context = {
            'datas': Exponent.query.filter(Exponent.add_user_id == id).order_by(Exponent.create_time.desc())
        }

        return render_template('datamanage.html', **context)


@app.route('/manual/')
@login_required
def manual():
    return render_template('manual.html')


@app.route('/usermanage/')
@login_required
def usermanage():
    if g.user.user_role.id == 1:
        return redirect(url_for('index'))
    else:
        id = g.user.id
        # print(id)
        context = {
            'children': User.query.filter(User.parent_id == id).order_by(User.join_time.desc())
        }

        return render_template('usermanage.html', **context)


@app.route('/usermanage/delete/', methods=['POST'])
@login_required
def duser():
    user_id = request.form.get('user_id')
    # print (user_id)
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return restful.success()


@app.route('/datamanage/delete/', methods=['POST'])
@login_required
def ddata():
    data_id = request.form.get('data_id')
    # print (user_id)
    data = Exponent.query.get(data_id)
    db.session.delete(data)
    db.session.commit()
    return restful.success()


class LoginView(views.MethodView):

    def get(self, message=None):
        return render_template('login.html', message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = User.query.filter_by(email=email).first()
            if user and user.password == password:
                session['user_id'] = user.id

                if remember:
                    session.permanent = True
                    app.permanent_session_lifetime = timedelta(minutes=3600)
                return redirect(url_for('index'))
            else:
                return self.get(message='邮箱或密码错误')
        else:
            message = form.get_error()
            return self.get(message=message)


class ResetPwdView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('resetpwd.html')

    def post(self):
        form = ResetpwdForm(request.form)

        if form.validate():
            oldpwd = form.oldpwd.data
            newpwd = form.newpwd.data
            user = g.user
            if (user.password == oldpwd):
                user.password = newpwd
                db.session.commit()

                return restful.success()
            else:

                return restful.params_error("旧密码错误!")

        else:

            return restful.params_error(form.get_error())


@app.route('/email_captcha/')
def email_captcha():
    # /email_captcha/?email=xxx@qq.com
    email = request.args.get('email')
    if not email:
        return restful.params_error('请传递邮箱参数！')

    source = list(string.ascii_letters)
    source.extend(map(lambda x: str(x), range(0, 10)))
    # source.extend(["0","1","2","3","4","5","6","7","8","9"])
    captcha = "".join(random.sample(source, 6))

    # 给这个邮箱发送邮件
    message = Message('邮箱验证码', recipients=[email], body='您的验证码是：%s' % captcha)
    try:
        mail.send(message)
    except:
        return restful.server_error()
    cache.set(email, captcha)
    return restful.success()


class ResetEmailView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('resetemail.html')

    def post(self):
        form = ResetEmailForm(request.form)
        if form.validate():
            email = form.email.data
            g.cms_user.email = email
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(form.get_error())


class RegisterView(views.MethodView):
    decorators = [login_required]

    def get(self, message=None):
        if g.user.user_role.id == 1:
            return redirect(url_for('index'))
        else:
            return render_template('adduser.html')

    def post(self):
        form = RegisterForm(request.form)
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            member = form.member.data
            school = form.school.data
            district = form.district.data
            print(district)

            if not User.query.filter_by(email=email).first():
                user = User(username=username, email=email, password=password, role_id=member, parent_id=g.user.id,
                            school_name=school, district_name=district)
                db.session.add(user)
                db.session.commit()

                return restful.success()
            else:
                return restful.params_error("该邮箱已被注册！请更换邮箱!")
        else:
            return restful.params_error(form.get_error())


class DataAddView(views.MethodView):
    decorators = [login_required]

    def get(self):
        if g.user.user_role.id != 2:
            return redirect(url_for('index'))
        else:
            return render_template('adddata.html')

    def post(self):
        form = DataAddForm(request.form)
        if form.validate():
            schoolName = form.schoolName.data
            year = form.year.data
            province = form.province.data
            city = form.city.data
            county = form.county.data
            sumStu = form.sumStu.data
            schoolPut = form.schoolPut.data
            studentAvg = form.studentAvg.data
            computerSum = form.computerSum.data
            multiClass = form.multiClass.data
            classSum = form.classSum.data
            broadband = form.broadband.data
            effectPrepare = form.effectPrepare.data
            pertinencePrepare = form.pertinencePrepare.data
            optimizeTeach = form.optimizeTeach.data
            turnoverTeach = form.turnoverTeach.data
            manageCourse = form.manageCourse.data
            communicateCourse = form.communicateCourse.data

            # 投入指数
            if (schoolPut / sumStu) / studentAvg > 1:
                I = 1
            else:
                I = round((schoolPut / sumStu) / studentAvg, 2)

            C1 = round(computerSum / sumStu, 2)
            C2 = round(multiClass / classSum, 2)
            if broadband >= 1000:
                C3 = 1.0
            elif broadband >= 100:
                C3 = 0.5
            elif broadband > 0:
                C3 = 0.2
            else:
                broadband = 0
            # 配置指数
            C = round((C1 * C2 * C3) ** (1. / 3), 2)

            E1 = round(0.67 * effectPrepare + 0.33 * pertinencePrepare, 2)
            E2 = round(0.33 * optimizeTeach + 0.67 * turnoverTeach, 2)
            E3 = round(0.67 * manageCourse + 0.33 * communicateCourse, 2)

            # 效果指数
            E = round((E1 * E2 * E3) ** (1. / 3), 2)

            # 总指数
            final_index = round((I ** 0.25) * (C ** 0.25) * (E ** 0.5), 2)
            # print(final_index)

            add_user_id = g.user.id

            exponent = Exponent(schoolName=schoolName, year=year, schoolProvince=province, schoolCity=city,
                                schoolCounty=county, schoolStu=sumStu, schoolPut=schoolPut, studentAvg=studentAvg,
                                computerSum=computerSum, multiClass=multiClass, classSum=classSum, broadband=broadband,
                                effectPrepare=effectPrepare, pertinencePrepare=pertinencePrepare,
                                optimizeTeach=optimizeTeach, turnoverTeach=turnoverTeach, manageCourse=manageCourse,
                                communicateCourse=communicateCourse, I=I, C1=C1, C2=C2, C3=C3, C=C, E1=E1, E2=E2, E3=E3,
                                E=E, final_index=final_index, add_user_id=add_user_id
                                )
            db.session.add(exponent)
            db.session.commit()
            print(restful.success())
            return restful.success()

        else:
            return restful.params_error(form.get_error())


@app.route('/datamanage/detail/<id>', methods=['GET', 'POST'])
@login_required
def data_detail(id):
    if request.method == 'GET':
        if g.user.user_role.id != 2:
            return redirect(url_for('index'))
        else:
            data = Exponent.query.filter(Exponent.id == id).first()
            return render_template('datadetail.html', data=data)
    else:
        form = DataEditForm(request.form)
        if form.validate():

            exponent = Exponent.query.filter(Exponent.id == id).first()
            exponent.schoolName = form.schoolName.data
            exponent.year = form.year.data

            exponent.schoolProvince = form.province.data
            exponent.schoolCity = form.city.data
            exponent.schoolCounty = form.county.data
            exponent.schoolStu = form.sumStu.data
            exponent.schoolPut = form.schoolPut.data
            exponent.studentAvg = form.studentAvg.data
            exponent.computerSum = form.computerSum.data
            exponent.multiClass = form.multiClass.data
            exponent.classSum = form.classSum.data
            exponent.broadband = form.broadband.data
            exponent.effectPrepare = form.effectPrepare.data
            exponent.pertinencePrepare = form.pertinencePrepare.data
            exponent.optimizeTeach = form.optimizeTeach.data
            exponent.turnoverTeach = form.turnoverTeach.data
            exponent.manageCourse = form.manageCourse.data
            exponent.communicateCourse = form.communicateCourse.data

            # 投入指数
            if (exponent.schoolPut / exponent.schoolStu) / exponent.studentAvg > 1:
                I = 1
            else:
                I = round((exponent.schoolPut / exponent.schoolStu) / exponent.studentAvg, 2)

            C1 = round(exponent.computerSum / exponent.schoolStu, 2)
            C2 = round(exponent.multiClass / exponent.schoolStu, 2)
            if exponent.broadband >= 1000:
                C3 = 1.0
            elif exponent.broadband >= 100:
                C3 = 0.5
            elif exponent.broadband > 0:
                C3 = 0.2
            else:
                exponent.broadband = 0
            # 配置指数
            C = round((C1 * C2 * C3) ** (1. / 3), 2)

            E1 = round(0.67 * exponent.effectPrepare + 0.33 * exponent.pertinencePrepare, 2)
            E2 = round(0.33 * exponent.optimizeTeach + 0.67 * exponent.turnoverTeach, 2)
            E3 = round(0.67 * exponent.manageCourse + 0.33 * exponent.communicateCourse, 2)

            # 效果指数
            E = round((E1 * E2 * E3) ** (1. / 3), 2)

            # 总指数
            final_index = round((I ** 0.25) * (C ** 0.25) * (E ** 0.5), 2)
            # print(final_index)

            exponent.I = I
            exponent.C1 = C1
            exponent.C2 = C2
            exponent.C3 = C3
            exponent.C = C
            exponent.E1 = E1
            exponent.E2 = E2
            exponent.E3 = E3
            exponent.E = E
            exponent.final_index = final_index

            db.session.commit()

            return redirect(url_for('datamanage'))

        else:
            return restful.params_error(form.get_error())


app.add_url_rule('/login/', view_func=LoginView.as_view('login'))

app.add_url_rule('/resetpwd/', view_func=ResetPwdView.as_view('resetpwd'))

app.add_url_rule('/resetemail/', view_func=ResetEmailView.as_view('resetemail'))

app.add_url_rule('/usermanage/add/', view_func=RegisterView.as_view('add_user'))

app.add_url_rule('/datamanage/add/', view_func=DataAddView.as_view('add_data'))


@app.before_request
def before_request():
    if 'user_id' in session:
        user_id = session.get('user_id')
        user = User.query.get(user_id)
        if user:
            g.user = user


@app.route('/logout/')
@login_required
def logout():
    # session.clear()
    del session['user_id']
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
