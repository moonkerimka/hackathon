FROM python
COPY app /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]