# start by pulling the python image
FROM python:3.8-alpine
# copy the requirements file into the image
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY main.py requirements.txt /app/
RUN apk add --update --no-cache python3 && \
    ln -sf python3 /usr/bin/python && \
    python3 -m ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools && \
    pip3 install -r requirements.txt
# copy every content from the local file to the image
# configure the container to run in an executed manner
ENTRYPOINT ["python"]
CMD ["main.py"]
