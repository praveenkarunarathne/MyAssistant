FROM python:latest

RUN apt update && apt upgrade -y

#Installing Requirements
RUN apt install git curl python3-pip ffmpeg -y

#Updating Pip
RUN pip3 install -U pip

#Copying Requirements
COPY requirements.txt /requirements.txt
RUN cd /
RUN pip3 install -U -r requirements.txt
RUN mkdir /MyAssistant
WORKDIR /MyAssistant
COPY bot.py /bot.py

#Running Radio Player Bot
CMD ["python", "bot.py"]
