FROM python

RUN apt-get update && pip install --upgrade pip \
    && pip install gunicorn==19.8.1 Flask==1.0.2 WTForms==2.1 Flask-Mail==0.9.1 Flask-SQLAlchemy==2.3.2 Flask-Migrate==2.1.1 Flask-Script==2.0.6 DateTime==4.2 Werkzeug==0.14.1 python3-memcached==1.51 PyMySQL==0.8.1 Flask-Session==0.3.1

COPY . /app

WORKDIR /app
