FROM python:latest
ENV NAME="Skillfactory"
WORKDIR /usr/src/app
COPY ./src/ .
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./plot.py" ]