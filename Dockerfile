FROM continuumio/anaconda3:latest
MAINTAINER Rui Cao "704645806@qq.com"
COPY . /app
WORKDIR . /app
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python"]
CMD ["app.py"]