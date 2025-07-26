FROM python:3.14.0rc1
ADD server.py /server.py
CMD python server.py
