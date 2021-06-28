FROM python:latest

WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt

RUN cd ext && python setup.py build_ext --inplace

ENTRYPOINT ["python"]
CMD ["app.py"]