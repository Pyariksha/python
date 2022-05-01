FROM python:3.9-slim

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY ./app ./
COPY requirements.txt ./

# Install production dependencies.
RUN pip install -r requirements.txt

CMD python3 ikea_tweets_api.py

