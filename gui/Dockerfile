FROM ubuntu:zbar

WORKDIR /app

# do requirements separately to avoid cache busting
COPY requirements.txt /app 
RUN pip install -r requirements.txt
COPY . /app 


RUN mkdir -p static/uploads
ENTRYPOINT ["python2.7"]
CMD ["app.py"]
