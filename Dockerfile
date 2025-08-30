FROM python:3.14.0rc2
ADD server.py /server.py
CMD python server.py
