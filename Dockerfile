FROM python:3.10.14

WORKDIR /app

COPY . /app

RUN apt-get update;apt-get install sudo vim -y

RUN curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

RUN apt-get install nodejs -y

RUN curl -L https://npmjs.org/install.sh | sudo sh

RUN npm -v

RUN npm install; npm run build

RUN pip install -r requirement.txt

EXPOSE 8012

ENTRYPOINT ["python3","manage.py", "runserver","0:8012"]