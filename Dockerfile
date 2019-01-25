FROM python:3
ADD requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt
RUN mkdir /starter-project
ADD . /starter-project/
WORKDIR /starter-project/src/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

