FROM mysql:5.7
FROM python:3.7-slim
ENV MYSQL_ROOT_PASSWORD=root
RUN pip install flask
RUN pip install flask-mysql
RUN mkdir templates
RUN mkdir static
COPY app.py /app.py
COPY templates/*  /templates/
COPY static/*  /static/
RUN chmod -R a+rwx static
RUN chmod -R a+rwx templates
CMD ["python","app.py"]
COPY script.sql /docker-entrypoint-initdb.d/
