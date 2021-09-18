FROM python:3.9-buster

# RUN apt-get update
#  && apt-get -yq install gcc && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*
# RUN apt-get install tesseract-ocr
# RUN sudo apt install libtesseract-dev

RUN mkdir /app
RUN mkdir -p /usr/share/tesseract-ocr/tessdata/
WORKDIR /app
ADD . /app/
ADD eng.traineddata /usr/share/tesseract-ocr/tessdata/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/app/src/run.py"]