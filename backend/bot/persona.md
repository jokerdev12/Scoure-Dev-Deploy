# Joker Smile Bot — Persona & Monetization Notes

This document contains the JokerSlime persona (voice used by the bot) and recommended monetization strategies. The tone below is intentionally vivid for branding; keep persona use limited to user-facing messages or marketing pages only.

## Persona (JokerSlime)
JokerSlime is a playful, cheeky, and theatrical persona used to make interactions more entertaining. Use it sparingly in short user-facing messages, marketing banners, or help messages. Avoid using the persona in system logs, error traces, or legal/privacy text.

Example lines:
- "🃏 JokerSlime chào bạn! Muốn một nụ cười bí ẩn không? Gõ /generate <mô tả>" 
- "Năng lượng nụ cười của bạn đã cạn — nạp thêm để tiếp tục cuộc vui!"

## Monetization strategies (recommended, professional)
1. Credit System
   - Provide 3–5 free credits to new users per day.
   - Each /generate consumes 1 credit for non-VIP users.
   - Credits are stored in the database and atomically decremented.

2. VIP / Subscription
   - Offer monthly/yearly VIP tiers that remove credit usage or provide higher-quality outputs and priority processing.
   - Automate group/channel membership for VIP access (optional).

3. Watermarking & Resolution tiers
   - Free outputs are lower resolution and include a visible watermark.
   - Paid outputs remove watermark and may provide higher-resolution assets suitable for commercial use.

4. Self-hosted GPU (cost control)
   - For production-scale usage, deploy inference models on a dedicated GPU server to control per-image cost.
   - Consider hybrid: on-prem GPU for VIP users + third-party API for overflow.

## Security & Compliance
- Do not store payment secrets or tokens in the repository.
- Respect model licensing: ensure models used (Stable Diffusion variants, checkpoints) allow the intended use.
- Provide a privacy policy explaining image retention, sharing, and deletion policy.

## Where to store this
Keep this document as a reference for product/marketing teams and developer implementers. The persona text can be kept verbatim in this file; use processed/safer variants in production code where tone needs to be toned down.
