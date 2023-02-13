FROM python:3.10
WORKDIR /app
RUN mkdir /app && chmod 777 /app
COPY . /app/
RUN pip install -r requirements.txt
CMD ["bash", "start.sh"]
