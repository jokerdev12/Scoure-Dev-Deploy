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

---

### Miễn trừ trách nhiệm — Mục đích phi thương mại / Ứng dụng miễn phí

Dự án này được cung cấp như một bản demo / công cụ tiện ích miễn phí để mọi người có thể tự tạo avatar, banner, icon, sticker, emoji, logo, background theo ý thích. Người phát triển/người duy trì cung cấp mã nguồn dưới dạng scaffold để học tập và sử dụng cá nhân; đây không phải là một sản phẩm thương mại hoặc dịch vụ trả phí do chúng tôi vận hành.

- Mã nguồn và ví dụ trong repo chỉ nhằm mục đích tham khảo và thử nghiệm; bạn cần tự kiểm thử, tinh chỉnh và đánh giá trước khi đưa vào bất kỳ môi trường sản xuất hoặc thương mại nào.
- Vui lòng kiểm tra các điều khoản cấp phép (license) của mô hình và checkpoint bạn sử dụng (ví dụ: FLUX.1, SDXL, hoặc các checkpoint/tài nguyên từ Hugging Face và bên thứ ba). Một số mô hình có giới hạn sử dụng thương mại.
- Không lưu trữ hoặc công khai bí mật (API keys, khóa riêng, thông tin người dùng) trong kho mã nguồn công khai.
- Người duy trì không chịu trách nhiệm pháp lý, chi phí hoặc khiếu nại phát sinh từ việc sử dụng, triển khai hoặc chỉnh sửa mã nguồn này.

Nếu bạn muốn, mình có thể:
- Điều chỉnh ngôn ngữ miễn trừ để chính thức hơn (hợp đồng pháp lý ngắn),
- Thêm phần hướng dẫn kiểm tra license cho từng mô hình (FLUX.1 / SDXL),
- Hoặc commit đoạn này vào README bằng một PR riêng nếu bạn muốn thay đổi cách trình bày.
