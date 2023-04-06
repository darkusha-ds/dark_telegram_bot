FROM python:3.10-slim-buster as build

ADD . /opt/bot_dir
WORKDIR /opt/bot_dir/

# RUN echo "Asia/Yekaterinburg" > /etc/timezone
# RUN dpkg-reconfigure -f noninteractive tzdata

# RUN /etc/localtime timedatectl set-timezone "Asia/Yekaterinburg"

# RUN apt update -y
# RUN apt upgrade -y
# RUN apt install python3.10 python3.10-pip -y

# RUN /usr/local/bin/python -m pip install --upgrade pip

# RUN pip3 install -r requirements.txt
RUN pip install -r requirements.txt

RUN chmod +x bot.sh

CMD /bin/sh ./bot.sh