# aurum_ai_bot.py
# ——— Aurum AI ———
# بوت تيليجرام تحليلي للذهب (XAU/USD) والبتكوين (BTC/USD)
# أوامر: /start /help /gold /btc /signal
# تحديث آلي كل 5 دقائق عبر JobQueue
# ملاحظة: هذا الهيكل مبدئي. دوال التحليل الحقيقية (T20/Y7) موضوعة كـ placeholders.

import os
from datetime import datetime, timezone
from telegram import Update, BotCommand
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# ——— إعدادات عامة ———
BOT_NAME = "Aurum AI"
REFRESH_MINUTES = 5  # التحديث الدوري كل 5 دقائق

# استخدم متغير البيئة TELEGRAM_BOT_TOKEN
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
if not TOKEN:
    raise RuntimeError("يرجى تعيين متغير البيئة TELEGRAM_BOT_TOKEN قبل التشغيل.")

# ——— Placeholders لدوال التحليل ———
# لاحقًا اربطها ببيانات السوق الفعلية و نماذجك (T20/Y7)

def analyze_gold():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return {
        "symbol": "XAU/USD",
        "time": now,
        "trend": "Neutral to Bullish",
        "entry": "Buy above 2370.5",
        "sl": "2364.0",
        "tp": "2381.0",
        "note": "MVP signal — replace with T20/Y7 output",
    }

def analyze_btc():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return {
        "symbol": "BTC/USD",
        "time": now,
        "trend": "Range-bound",
        "entry": "Buy above 63,200",
        "sl": "62,450",
        "tp": "64,400",
        "note": "MVP signal — replace with T20/Y7 output",
    }

def unified_signal():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return {
        "asset": "XAU/USD",
        "direction": "LONG",
        "entry": "2370.5",
        "sl": "2363.5",
        "tp": "2382.0",
        "confidence": "0.62 (MVP)",
        "time": now,
        "framework": "T20+Y7 (placeholder)",
    }

# ——— Utilities ———
def fmt_signal(d):
    if "symbol" in d:
        return (
            f"\n<b>{d['symbol']}</b> — <i>{d['time']}</i>\n"
            f"اتجاه: <b>{d['trend']}</b>\n"
            f"دخول: <code>{d['entry']}</code>\n"
            f"وقف: <code>{d['sl']}</code>\n"
            f"هدف: <code>{d['tp']}</code>\n"
            f"ملاحظة: {d['note']}"
        )
    return (
        f"\n<b>{d['asset']}</b> — <i>{d['time']}</i>\n"
        f"اتجاه: <b>{d['direction']}</b>\n"
        f"دخول: <code>{d['entry']}</code>\n"
        f"وقف: <code>{d['sl']}</code>\n"
        f"هدف: <code>{d['tp']}</code>\n"
        f"ثقة: <b>{d['confidence']}</b>\n"
        f"إطار: <code>{d['framework']}</code>"
    )

# ——— Handlers ———
async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name or ""
    text = (
        f"مرحبا {name}! أنا <b>{BOT_NAME}</b> 🤖\n\n"
        "الأوامر المتاحة:\n"
        "/gold — تحليل لحظي للذهب\n"
        "/btc — تحليل لحظي للبيتكوين\n"
        "/signal — توصية (دخول/خروج + هدف + وقف)\n"
        "يتم التحديث كل 5 دقائق تلقائيًا."
    )
    await update.message.reply_text(text, parse_mode=ParseMode.HTML)

async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "استخدم /gold أو /btc أو /signal. أضفني لقروبك وفعّلني كمشرف لو حاب التنبيهات الدورية."
    )

async def cmd_gold(update: Update, context: ContextTypes.DEFAULT_TYPE):
    d = analyze_gold()
    await update.message.reply_text(fmt_signal(d), parse_mode=ParseMode.HTML)

async def cmd_btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    d = analyze_btc()
    await update.message.reply_text(fmt_signal(d), parse_mode=ParseMode.HTML)

async def cmd_signal(update: Update, context: Conte_
