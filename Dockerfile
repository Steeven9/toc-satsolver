FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
WORKDIR /usr/src/app/app
CMD [ "flask", "run", "--host", "0.0.0.0" ]
