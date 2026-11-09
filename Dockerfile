FROM python:3.11-slim
WORKDIR /app
COPY analyser.py ./
COPY tests/ ./tests/
COPY sample_data/ ./sample_data/
COPY entrypoint.sh ./
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
