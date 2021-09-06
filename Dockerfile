from python:3

run mkdir /django/
workdir /django
copy requirements.txt /django/requirements.txt
copy manage.py /django/manage.py
copy app /django/app
copy accounts /django/accounts
run pip3 install -r requirements.txt


copy entrypoint.sh /entrypoint.sh
CMD [ "/bin/sh", "/entrypoint.sh" ]

