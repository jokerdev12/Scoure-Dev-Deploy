# Joker Smile — project README

Joker Smile là một dự án mã nguồn mở, demo và công cụ tiện ích để tạo avatar, banner, icon, sticker, emoji, logo và background bằng AI. Mục tiêu: cung cấp một scaffold dễ self-host, khuyến khích học hỏi và cộng tác từ cộng đồng.

Repository layout (high level)

joker-smile-3d/
├── frontend/                 # Web 3D editor (React/Three.js)
└── backend/                  # Backend services (FastAPI, AI core, bot)
    ├── api/                  # FastAPI routes for web editor & payment webhooks
    ├── core/                 # Core AI logic (ai_engine.py), config, utilities
    ├── bot/                  # Telegram Bot (aiogram)
    │   ├── telegram_bot.py   # Bot implementation
    │   └── persona.md        # Persona & notes
    ├── main.py               # Entrypoint for backend services
    └── requirements.txt      # Backend dependencies

Quick summary
- Dự án này là mã nguồn mở, cấp phép permissive (MIT). Bạn có thể fork, sửa đổi, sử dụng và phân phối lại mã nguồn theo điều khoản MIT — xem file LICENSE.
- Lưu ý: các mô hình AI (ví dụ: FLUX.1, SDXL) và các checkpoint/weights có license riêng. Không commit checkpoints/weights vào repo. Kiểm tra kỹ model card trước khi sử dụng cho mục đích thương mại.

Run the bot locally (development)
1. Copy `backend/.env.example` -> `backend/.env` và điền giá trị cần thiết.
2. Cài đặt phụ thuộc: `pip install -r backend/requirements.txt`
3. Chạy bot:
   ```bash
   python backend/bot/telegram_bot.py
   ```

Notes & best practices
- Không commit bí mật (API keys, credentials) vào kho công khai. Sử dụng `.env` và `.gitignore`.
- Không commit model weights/checkpoints hoặc file lớn — thay bằng hướng dẫn tải từ nguồn chính thức.
- Kiểm tra license của từng model/mội nguồn dữ liệu trước khi sử dụng trong môi trường sản xuất hoặc thương mại.

Models & licenses
- Thông tin license cho từng model không nằm trong phạm vi của LICENSE này. Vui lòng xem `models-licenses.md` để biết hướng dẫn kiểm tra và liên kết tới model card chính thức.

Contributing
- Mọi đóng góp đều được hoan nghênh: mở issue, gửi PR cho feature, docs, prompt templates, UI presets.
- Trước khi gửi PR lớn, hãy mở issue để thảo luận thiết kế.
- Không thêm weights, secrets hoặc tài nguyên có license không phù hợp vào PR.
- Xem `CONTRIBUTING.md` để biết hướng dẫn chi tiết.

Authorship & ownership
- Tác giả/gốc: JokerVN404 (github: jokerdev12). Bạn được phép sử dụng và phát triển tiếp dự án theo điều khoản MIT. Attribution ngắn gọn "based on Joker Smile by JokerVN404" được hoan nghênh nhưng không bắt buộc.

License
- Mã nguồn chính của dự án này được cấp phép theo MIT. Xem file `LICENSE`.

Contact
- Website / liên hệ: https://bothelper.vn
