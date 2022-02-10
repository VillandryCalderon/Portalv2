FROM python:3.8.3-alpine3.12
COPY . /Portal
WORKDIR /Portal
RUN pip install asgiref==3.4.1
RUN pip install astroid==2.6.6 
RUN pip installl backports.entry-points-selectable==1.1.0
RUN pip install beautifulsoup4==4.10.0
RUN pip install click==8.0.3
RUN pip install colorama==0.4.4
RUN pip install distlib==0.3.3
RUN pip install dj-database-url==0.5.0
RUN pip install Django==3.2.7
RUN pip install django-bootstrap==0.2.4
RUN pip install django-bootstrap-form==3.4
RUN pip install django-bootstrap4==3.0.1
RUN pip install django-crispy-forms==1.8.1
RUN pip install django-filter==2.4.0
RUN pip install django-forms-bootstrap==2.0.3.post2
RUN pip install django-heroku==0.3.1
RUN pip install django-uuslug==1.2.0
RUN pip install djangorestframework==3.12.4
RUN pip install filelock==3.0.12
RUN pip install Flask==2.0.2
RUN pip install gunicorn==20.1.0
RUN pip install isort==5.9.3
RUN pip install itsdangerous==2.0.1
RUN pip install Jinja2==3.0.2
RUN pip install lazy-object-proxy==1.6.0
RUN pip install MarkupSafe==2.0.1
RUN pip install mccabe==0.6.1
RUN pip install olefile==0.46
RUN pip install Pillow==8.3.2
RUN pip install platformdirs==2.3.0
RUN pip install psycopg2==2.9.1
RUN pip install pylint==2.9.6
RUN pip install PyQRCode==1.2.1
RUN pip install python-slugify==5.0.2
RUN pip install pytz==2019.3
RUN pip install pyzbar==0.1.8
RUN pip install qrcode==7.3.1
RUN pip install six==1.16.0
RUN pip install soupsieve==2.2.1
RUN pip install sqlparse==0.3.1
RUN pip install text-unidecode==1.3
RUN pip install toml==0.10.2
RUN pip install ua-parser==0.10.0
RUN pip install Unidecode==1.3.2
RUN pip install user-agents==2.2.0
RUN pip install virtualenv==20.8.0
RUN pip install Werkzeug==2.0.2
RUN pip install whitenoise==5.0.1
RUN pip install wrapt==1.12.1

EXPOSE 8000

CMD [ "python","manage.py" ]