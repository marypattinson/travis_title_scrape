FROM python:3
RUN mkdir /code
COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt 
COPY myscript.py /code/
CMD ["python","/code/myscript.py"]