# 🎬 YouTube Livestream Redirector

A lightweight Flask-based service that extracts a YouTube livestream .m3u8 HLS URL and serves it in a way that IPTV players (like OTT Navigator, TiviMate, VLC) can consume — with smart caching.  

## 🚀 Features

- 🔗 Accepts YouTube livestream URLs 
- ⚡ Redirects to the best streamable URL using `yt_dlp`
- 🧠 Caches stream URLs for 6 hours using custom name-based keys
- 🛡️ Graceful error handling and minimal logging
- 🐘 Runs with Gunicorn for production-grade performance
- 🐳 Docker + Portainer compatible

## 📦 Usage

Here’s a variety of YouTube link formats you can use with your redirector service.

These are all valid inputs for your /stream endpoint. Just pair them with a custom name by adding &name=any_name_you_give like:
http://localhost:6095/stream?url=https://www.youtube.com/@Sozcutelevizyonu/live&name=sozcutv  

🔴 Livestream Links

•  https://www.youtube.com/@Sozcutelevizyonu/live  
•  https://www.youtube.com/watch?v=UX38PTCabzM


### Example

https://localhost:6095/stream?url=https://www.youtube.com/@kizilcikserbetidizi/live&name=kizilcik  
https://localhost:6095/stream?url=https://www.youtube.com/watch?v=UX38PTCabzM&name=tomorrowland

📜 License

MIT License — feel free to fork, modify, and deploy.

💬 Credits

Built by [A] with ❤️ and a dash of Python. Powered by Flask, Gunicorn, and yt_dlp.
