# 🎬 YouTube Livestream Redirector

A lightweight Flask-based service that redirects users to the best available stream URL for a given YouTube channel, video, or playlist — with smart caching and livestream prioritization.

## 🚀 Features

- 🔗 Accepts any YouTube URL (channel, video, playlist, or livestream)
- ⚡ Redirects to the best streamable URL using `yt_dlp`
- 🧠 Caches stream URLs for 6 hours using custom name-based keys
- 🛡️ Graceful error handling and minimal logging
- 🐘 Runs with Gunicorn for production-grade performance
- 🐳 Docker + Portainer compatible

## 📦 Usage

Here’s a variety of YouTube link formats you can use with your redirector service. These cover channels, live
streams, videos, playlists, and short URLs so you can test all the edge cases.  

These are all valid inputs for your /stream endpoint. Just pair them with a custom name by adding &name=any_name_you_give like:
http://localhost:6095//stream?url=https://www.youtube.com/@MrBeast/live&name=beast  

📺 Standard Video Links

•  https://www.youtube.com/watch?v=dQw4w9WgXcQ  
•  https://youtu.be/dQw4w9WgXcQ  
•  https://www.youtube.com/watch?v=UX38PTCabzM  

🔴 Livestream Links

•  https://www.youtube.com/@kizilcikserbetidizi/live  
•  https://www.youtube.com/@Sozcutelevizyonu/live  
•  https://www.youtube.com/channel/UC4R8DWoMoI7CAwX8_LjQHig/live (generic channel livestream)  

📃 Playlist Links

•  https://www.youtube.com/playlist?list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI  
•  https://www.youtube.com/watch?v=peFZbP64dsU&list=PLGup6kBfcU7Le5laEaCLgTKtlDcxMqGxZ  

👤 Channel Links

•  https://www.youtube.com/@MrBeast  
•  https://www.youtube.com/user/PewDiePie  
•  https://www.youtube.com/channel/UCX6OQ3DkcsbYNE6H8uQQuVA  


### Example

https://localhost:6095/stream?url=https://www.youtube.com/@kizilcikserbetidizi/live&name=kizilcik  
https://localhost:6095/stream?url=https://www.youtube.com/watch?v=UX38PTCabzM&name=owr

📜 License

MIT License — feel free to fork, modify, and deploy.

💬 Credits

Built by [A] with ❤️ and a dash of Python. Powered by Flask, Gunicorn, and yt_dlp.
