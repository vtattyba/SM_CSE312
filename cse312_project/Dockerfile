FROM ubuntu:18.04

RUN apt-get update

ENV HOME /root
WORKDIR /root

RUN apt-get update --fix-missing && apt-get install -y python3-pip && apt-get install -y git
RUN apt-get install -y npm && apt-get install -y python3 && apt-get install -y python3-dev
RUN apt-get install -y python3-distutils
#RUN apt-get install -y postgresql
RUN apt-get install -y python3-psycopg2

COPY . .

# dependancies ?
RUN python3 -m pip install --upgrade Pillow
RUN python3 -m pip install bootstrap4
RUN pip3 install django-bootstrap4
RUN pip3 install django-bootstrap
RUN pip3 install misaka
RUN python3 -m pip install Django
RUN pip3 install psycopg2-binary
RUN pip3 install channels
RUN pip3 install channels-redis

 


EXPOSE 8000
EXPOSE 5432
EXPOSE 6379

#ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
#RUN chmod +x /wait
#
#
# CMD /wait && ["python3", "manage.py", "migrate"] && ["python3", "manage.py", "makemigrations"] && ["python3", "manage.py", "migrate"] &&["python3", "manage.py", "runserver"]


CMD ["python3", "manage.py", "runserver"]