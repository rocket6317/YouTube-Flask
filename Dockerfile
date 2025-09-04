FROM python:3.13.0-slim

# Install tzdata for timezone support
RUN apt-get update && apt-get install -y --no-install-recommends tzdata

# Set the timezone (change to your desired timezone)
ENV TZ=Europe/London

# Optional: Set noninteractive mode to avoid tzdata prompts
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

COPY app.py .

RUN pip install flask yt-dlp cachetools gunicorn

EXPOSE 6095

# CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:6095", "app:app"]
CMD ["gunicorn", "--workers", "3", "--threads", "2", "--bind", "0.0.0.0:6095", "app:app"]