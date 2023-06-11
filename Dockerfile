FROM python:3.10.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /RUN pip install -r requirements.txt
RUN mkdir /Autofilterwithshortner_bot
WORKDIR /Autofilterwithshortner_bot
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]
