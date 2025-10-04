FROM python:3.14.0rc3
ADD server.py /server.py
CMD python server.py
