from flask import Flask, request, redirect
from cachetools import TTLCache
import yt_dlp
import logging
import os

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logging.getLogger().setLevel(logging.INFO)

app = Flask(__name__)

# 🔐 Load secret token from environment variable
SECRET_TOKEN = os.getenv("STREAM_API_TOKEN", "your-secret-token")

# 🧠 In-memory cache: max 100 entries, TTL = 6 hours
cache = TTLCache(maxsize=100, ttl=21600)

def get_m3u8_url(youtube_url):
    logging.info(f"Extracting M3U8 stream from: {youtube_url}")
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'forcejson': True,
        'format': 'best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        formats = info.get('formats', [])

        for f in formats:
            if f.get('protocol') == 'm3u8' and f.get('url'):
                logging.info(f"M3U8 stream found: {f['url']}")
                return f['url']

        raise ValueError("No M3U8 stream found in available formats")

@app.route('/m3u8')
def m3u8():
    youtube_url = request.args.get('url')
    custom_name = request.args.get('name')
    token = request.args.get('token')

    if not youtube_url or not custom_name or not token:
        logging.warning("Missing url, name, or token parameter")
        return "Missing url, name, or token parameter", 400

    if token != SECRET_TOKEN:
        logging.warning(f"Unauthorized access attempt with token: {token}")
        return "Unauthorized", 403

    key = f"name:{custom_name.strip().lower()}"
    logging.info(f"Using cache key: {key}")

    try:
        m3u8_url = cache[key]
        logging.info("Cache hit – returning cached M3U8 URL")
    except KeyError:
        logging.info("Cache miss – extracting new M3U8 URL")
        try:
            m3u8_url = get_m3u8_url(youtube_url)
            cache[key] = m3u8_url
            logging.info("M3U8 URL fetched and cached")
        except Exception as e:
            logging.error(f"Error extracting M3U8: {str(e)}")
            return f"Error: {str(e)}", 500

    logging.info("Redirecting to M3U8 stream")
    return redirect(m3u8_url)
