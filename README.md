# Joker Smile — project README

Joker Smile is a research / demo repository for an AI-powered image generator that supports both a web 3D editor and a Telegram bot interface (JokerSlime persona).

Repository layout (high level)

joker-smile-3d/
├── frontend/                 # Web 3D editor (React/Three.js)
└── backend/                  # Backend services (FastAPI, AI core, bot)
    ├── api/                  # FastAPI routes for web editor & payment webhooks
    ├── core/                 # Core AI logic (ai_engine.py), config, utilities
    ├── bot/                  # Telegram Bot (aiogram)
    │   ├── telegram_bot.py   # Bot implementation
    │   └── persona.md        # Persona & monetization notes
    ├── main.py               # Entrypoint for backend services
    └── requirements.txt      # Backend dependencies

What I added
- backend/bot/telegram_bot.py (scaffold bot implementation with credit/payment hooks)
- backend/bot/persona.md (persona + monetization notes, professional)
- backend/requirements.txt (backend deps)
- backend/.env.example (environment example)
- Updated top-level README with architecture overview and run hints

Next steps (recommended)
1. Implement/plug DB layer (users, credits, images, transactions).
2. Implement storage (S3) upload and configure credentials.
3. Implement payment checkout + webhook (Stripe or regional provider like Momo).
4. Harden ai_engine to return a consistent object (image_url / image_base64 / image_bytes + web_url + asset_id).
5. Add unit tests, CI checks (lint, security scans), and Dockerfiles for production deployment.

Run the bot locally (development)
1. Copy backend/.env.example -> backend/.env and fill values.
2. Install deps: pip install -r backend/requirements.txt
3. Run:
   python backend/bot/telegram_bot.py

Notes
- This commit is scaffold-level. Do not expose secrets.
- If you want, I can also scaffold DB migrations (Alembic), Dockerfile + docker-compose for local development, and a Stripe payment mock for testing.

