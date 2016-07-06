FROM australiansynchrotron/epics:centos7-python3.5.2
COPY app /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python3", "./app.py" ]
