# Learning OpenAI - Coffee Chat (MVP)

Project ini adalah FastAPI app sederhana untuk tugas course:
- menampilkan form input topik kopi
- mengirim input ke model LLM
- menampilkan hasil jawaban di halaman yang sama

## Tech Stack
- Python
- FastAPI
- Jinja2 (template HTML)
- OpenAI SDK (via OpenRouter API)
- Markdown (render response ke HTML)

## Fitur Saat Ini
- `GET /coffee/` untuk menampilkan halaman chat/form.
- `POST /coffee/` untuk menerima `topic`, kirim ke model, lalu render hasil.
- Prompt sistem difokuskan ke domain kopi (resep/knowledge/out-of-scope guardrail).
- UI sederhana dengan Tailwind CDN.

## Struktur Singkat
```text
app/
  main.py
  modules/coffee/
    router.py
    prompt.py
  utils/openai.py
templates/
  index.html
```

## Setup
1. Install dependency:
```bash
uv sync
```

2. Siapkan environment variable:
```bash
OPENROUTER_API_KEY=your_key_here
```

## Menjalankan Project
```bash
make dev
```

App akan jalan di `http://127.0.0.1:8000` (default uvicorn).

## Endpoint
- `GET /coffee/`
  - Return halaman HTML (`templates/index.html`)
- `POST /coffee/`
  - Form field: `topic`
  - Proses: kirim prompt ke model
  - Return: halaman HTML dengan `user_input` dan `result`


