FROM python

WORKDIR /program

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY  . /program

EXPOSE 5000

CMD ["python3", "./app.py"]