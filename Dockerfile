FROM python:3.10
WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
COPY . /app
CMD python -m Adarsh
