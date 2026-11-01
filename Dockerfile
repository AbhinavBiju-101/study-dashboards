FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=10000

WORKDIR /app

# Install deps first so this layer is cached between code changes.
# (Every dashboard only needs Flask, which the hub already requires.)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run as a non-root user.
RUN useradd --create-home appuser && chown -R appuser /app
USER appuser

EXPOSE 10000

# Render injects $PORT at runtime; shell form so it expands.
CMD gunicorn app:app --bind 0.0.0.0:${PORT} --workers 2 --threads 4 --access-logfile -
