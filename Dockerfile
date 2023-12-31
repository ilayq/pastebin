FROM ubuntu:22.04

COPY main.py .
COPY db.py .
COPY requirements.txt .
COPY index.html .
RUN touch db.sqlite
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]