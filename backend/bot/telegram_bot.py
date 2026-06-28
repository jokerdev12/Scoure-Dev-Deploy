# Telegram Bot for Joker Smile AI

This module contains the Telegram bot that integrates with the project's core AI engine (AIGeneratorEngine). The bot is implemented with aiogram (async) and is intended to run alongside the FastAPI backend, reusing the same AI core.

Features
- /start — welcome message
- /generate <prompt> — generate an image (default: sticker style, "Joker")
- Credit-check skeleton (placeholders): supports free credits, VIP, and payment flow hooks
- Watermark & downscale option for free users (upload-preserve for paid users)
- Upload-to-storage hook and web editor link support

Important: This file is a scaffold and requires you to implement/plug-in the following in your project:
- core.ai_engine.AIGeneratorEngine and its async method generate_design
- database functions for user/credit management (see placeholders)
- upload_to_storage function (S3/GCS/etc.)
- payment checkout endpoint to create payment links


```python
# backend/bot/telegram_bot.py
import os
import asyncio
import logging
import base64
from io import BytesIO
from typing import Optional
from aiogram import Bot, Dispatcher
from aiogram.types import InputFile, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

from core.ai_engine import AIGeneratorEngine

# Placeholder imports - implement these in your backend
# from core.db import get_or_create_user, decrement_credits, is_vip_user
# from core.storage import upload_bytes_and_get_url

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Environment
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BASE_WEB_URL = os.getenv("BASE_WEB_URL", "https://your-web-editor.example.com")

if not TELEGRAM_BOT_TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN is required in environment")

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# Re-use the project's core AI engine
ai_engine = AIGeneratorEngine()

# --- Helper placeholders (replace with real implementation) ---
async def get_or_create_user(telegram_id: int) -> dict:
    """Return a simple user dict. Replace with DB logic (async).
    Expected keys: id, telegram_id, credits (int), is_vip (bool)
    """
    # TODO: Replace with real DB call
    return {"id": telegram_id, "telegram_id": telegram_id, "credits": 3, "is_vip": False}

async def decrement_credits(user_id: int, amount: int = 1) -> None:
    """Atomically decrement credits in DB. Placeholder."""
    # TODO: implement DB decrement
    logger.info("decrement_credits: user=%s amount=%s", user_id, amount)

async def upload_bytes_and_get_url(data: bytes, key: str) -> str:
    """Upload bytes to storage (S3/GCS) and return a public or presigned URL. Placeholder."""
    # TODO: implement storage upload
    return f"{BASE_WEB_URL}/assets/{key}"

# ------------------------------------------------------------

@dp.message(Command("start"))
async def send_welcome(message):
    welcome_text = (
        "🃏 Chào mừng đến với Joker Smile AI Designer!\n\n"
        "Gửi lệnh /generate <mô tả> để tạo logo, sticker hoặc avatar phong cách Joker.\n"
        "Ví dụ: /generate một logo e-sports hình chú hề cười mỉm, neon xanh tím.\n\n"
        "Lưu ý: Mỗi tài khoản có lượt miễn phí. Tham khảo /help để biết chi tiết về hệ thống credit."
    )
    await message.reply(welcome_text)

@dp.message(Command("help"))
async def send_help(message):
    help_text = (
        "Hướng dẫn nhanh:\n"
        "- /generate <mô tả>: tạo ảnh từ mô tả.\n"
        "- Mỗi lần tạo sẽ tiêu 1 credit (trừ khi bạn là VIP).\n"
        "- Hết credit? Bot sẽ gửi link nạp tiền.\n"
        "Liên hệ admin để hỗ trợ thêm."
    )
    await message.reply(help_text)

@dp.message(Command("generate"))
async def generate_design(message):
    prompt = (message.text or "").replace("/generate", "").strip()
    if not prompt:
        await message.reply("Bạn quên nhập mô tả rồi! Ví dụ: /generate logo phong cách Dark Knight")
        return

    processing_msg = await message.reply("⏳ Đang gọi AI để tạo tác phẩm cho bạn. Vui lòng chờ...")

    try:
        user = await get_or_create_user(message.from_user.id)

        # Credit / VIP check
        if not user.get("is_vip") and user.get("credits", 0) <= 0:
            # Build payment link (implement payment flow in your backend)
            payment_link = f"{BASE_WEB_URL}/purchase?user={user['telegram_id']}"
            kb = InlineKeyboardMarkup().add(InlineKeyboardButton("Nạp credit / Mua gói VIP", url=payment_link))
            await processing_msg.edit_text("Bạn đã hết lượt miễn phí. Nạp thêm để tiếp tục.", reply_markup=kb)
            return

        # consume credit if not VIP
        if not user.get("is_vip"):
            await decrement_credits(user["id"], 1)

        # Call AI core
        result = await ai_engine.generate_design(
            prompt=prompt,
            design_type="sticker",
            style="Joker",
            # You may want additional kwargs like size, seed, guidance_scale...
        )

        # Support different return forms from ai_engine
        image_b64: Optional[str] = result.get("image_base64")
        image_url: Optional[str] = result.get("image_url")
        web_url: Optional[str] = result.get("web_url")

        sent = False
        if image_b64:
            data = base64.b64decode(image_b64)
            bio = BytesIO(data)
            bio.name = "joker_design.png"
            await bot.send_photo(chat_id=message.chat.id, photo=InputFile(bio), caption=f"🎨 Tác phẩm của bạn: {prompt}")
            sent = True
        elif image_url:
            # Let Telegram fetch photo by URL
            await bot.send_photo(chat_id=message.chat.id, photo=image_url, caption=f"🎨 Tác phẩm của bạn: {prompt}")
            sent = True
        else:
            # If AI returns raw bytes or needs upload
            image_bytes = result.get("image_bytes")
            if image_bytes:
                key = f"telegram-{message.from_user.id}-{int(asyncio.time.time())}.png"
                url = await upload_bytes_and_get_url(image_bytes, key)
                await bot.send_photo(chat_id=message.chat.id, photo=url, caption=f"🎨 Tác phẩm của bạn: {prompt}")
                sent = True

        # Optionally send web editor link
        if not sent and web_url:
            kb = InlineKeyboardMarkup().add(InlineKeyboardButton("🔧 Tùy chỉnh trên web", url=web_url))
            await processing_msg.edit_text("Tác phẩm sẵn sàng. Mở link dưới đây để chỉnh sửa:", reply_markup=kb)
            return

        # If already sent a photo, optionally send link to open in editor
        if web_url:
            kb = InlineKeyboardMarkup().add(InlineKeyboardButton("🔧 Mở trong web editor", url=web_url))
            await bot.send_message(chat_id=message.chat.id, text="Bạn muốn chỉnh sửa thêm? Mở link dưới đây:", reply_markup=kb)

        await bot.delete_message(chat_id=message.chat.id, message_id=processing_msg.message_id)

    except Exception as e:
        logger.exception("Error in generate_design: %s", e)
        try:
            await processing_msg.edit_text(f"❌ Có lỗi xảy ra: {e}")
        except Exception:
            pass


async def main():
    logger.info("Khởi động Joker Smile Telegram Bot...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
```
