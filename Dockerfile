FROM python:3.7.5

RUN apt-get update --fix-missing
RUN apt-get install -yq vim htop curl
RUN apt install -y libtesseract-dev libleptonica-dev tesseract-ocr

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000

CMD ["curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
