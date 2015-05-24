FROM python:3

ADD . /usr/src/app
WORKDIR /usr/src/app

RUN pip install -r requirements.txt
# RUN pip install -e .[develop]
RUN python setup.py develop
CMD ["python", "setup.py", "test"]
