FROM python:3.10.8-slim-buster

COPY requirements.txt /requirements.txt

RUN cd /RUN pip install -r requirements.txt
WORKDIR /Autofilterwithshortner_bot
COPY . .
CMD ["python3", "bot.py"]
