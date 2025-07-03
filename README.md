# 🌐 InfoBot

A fullstack web summarizer that takes a user's query, searches the web, scrapes relevant content, summarizes it using **Gemini**, and optionally adds a **Creative Commons image** using [Openverse](https://openverse.org).

---

## ✨ Features

- 🔍 Accepts user questions via chat UI
- 🌐 Scrapes top 3 relevant web results (via SERP API)
- 🧠 Summarizes using Google Gemini API
- 🖼️ Fetches relevant image if helpful (via Openverse)
- ⚡ Built with FastAPI (backend) & Next.js + Tailwind CSS (frontend)

---

## 🛠️ Tech Stack

| Layer     | Technology               |
|-----------|--------------------------|
| Frontend  | Next.js, Tailwind CSS    |
| Backend   | FastAPI, Uvicorn         |
| AI Model  | Gemini API (Google AI)   |
| Web Search| SerpAPI                  |
| Images    | Openverse API            |

---

## 🌐 Live App

🔗 [Visit the app on Vercel](https://info-bot-ten.vercel.app/)  

---

## 📜 License & Usage

- This project uses third-party APIs and publicly available web content.
- Images are retrieved from [Openverse](https://openverse.org/) using filters to ensure they are under valid Creative Commons licenses (e.g., `CC0`, `CC-BY`, `CC-BY-SA`).
- Summarization is powered by the [Google Gemini](https://ai.google.dev/) API.
- Always verify the license of each image before using it for commercial or public distribution.
- This project is intended for **educational**, **personal**, and **demonstration** purposes only.

---

## 🙏 Credits

- [Google AI Studio (Gemini)](https://ai.google.dev/)
- [Openverse](https://openverse.org/)
- [SerpAPI](https://serpapi.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Next.js](https://nextjs.org/)
- [Tailwind CSS](https://tailwindcss.com/)

---

