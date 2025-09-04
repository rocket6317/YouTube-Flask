from flask import Flask, request, redirect
from cachetools import TTLCache
import yt_dlp
import logging

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

app = Flask(__name__)

# Cache: max 100 entries, TTL = 6 hours
cache = TTLCache(maxsize=100, ttl=21600)

def get_stream_url(youtube_url):
    logging.info(f"Fetching stream URL for: {youtube_url}")
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'forcejson': True,
        'extract_flat': False,
        'format': 'best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)

        # Case 1: Direct livestream
        if info.get('is_live'):
            logging.info("Livestream detected – prioritizing")
            return info.get('url')

        # Case 2: Playlist or channel
        if 'entries' in info and info['entries']:
            for entry in info['entries']:
                if entry.get('is_live'):
                    logging.info(f"Livestream found in entries: {entry.get('title')}")
                    return entry.get('url')

            first_entry = info['entries'][0]
            logging.info(f"No livestream found – using first video: {first_entry.get('title')}")
            return first_entry.get('url')

        raise ValueError("Could not extract stream URL")

@app.route('/stream')
def stream():
    logging.info("Received request to /stream endpoint")
    youtube_url = request.args.get('url')
    custom_name = request.args.get('name')

    if not youtube_url or not custom_name:
        logging.warning("Missing 'url' or 'name' parameter")
        return "Missing url or name parameter", 400

    key = f"name:{custom_name}"
    logging.info(f"Using cache key: {key}")

    if key in cache:
        logging.info("Cache hit – returning cached stream URL")
        stream_url = cache[key]
    else:
        logging.info("Cache miss – fetching new stream URL")
        try:
            stream_url = get_stream_url(youtube_url)
            cache[key] = stream_url
            logging.info("Stream URL fetched and cached")
        except Exception as e:
            logging.error(f"Error fetching stream URL: {str(e)}")
            return f"Error: {str(e)}", 500

    logging.info("Redirecting to stream URL")
    return redirect(stream_url)