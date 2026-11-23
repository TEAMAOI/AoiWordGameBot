"""Centralized environment-based configuration for Word Grid & WordSeek Bot."""

import os
from dotenv import load_dotenv

load_dotenv()


def _parse_int(value: str, default: int = 0) -> int:
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return default


def _parse_float(value: str, default: float = 0.0) -> float:
    try:
        return float(str(value).strip())
    except (TypeError, ValueError):
        return default


def _parse_int_list(raw: str) -> list[int]:
    seen: set[int] = set()
    result: list[int] = []
    for item in str(raw or "").split(","):
        item = item.strip()
        if item and item.lstrip("-").isdigit():
            uid = int(item)
            if uid not in seen:
                seen.add(uid)
                result.append(uid)
    return result


# --- Telegram Credentials (Required) ---
API_ID: int = _parse_int(os.getenv("API_ID", "0"), 0)
API_HASH: str = os.getenv("API_HASH", "").strip()
BOT_TOKEN: str = os.getenv("BOT_TOKEN", "").strip()

# --- MongoDB Database (Required) ---
MONGO_URI: str = os.getenv("MONGO_URI", "").strip()
DB_NAME: str = os.getenv("DB_NAME", "WordGridBotDB").strip() or "WordGridBotDB"

# --- Admins & Bot Identity ---
SUDO_USERS: list[int] = _parse_int_list(os.getenv("SUDO_USERS", ""))
BOT_USERNAMES: list[str] = [
    x.strip().lstrip("@")
    for x in os.getenv("BOT_USERNAMES", os.getenv("BOT_USERNAME", "")).split(",")
    if x.strip().lstrip("@")
]

# --- Community Links & Locale ---
SUPPORT_GROUP: str = os.getenv("SUPPORT_GROUP", "https://t.me/Telegram").strip()
UPDATE_CHANNEL: str = os.getenv("UPDATE_CHANNEL", "https://t.me/Telegram").strip()
TIME_ZONE: str = os.getenv("TIME_ZONE", "Asia/Kolkata").strip() or "Asia/Kolkata"

# --- Cooldown & Gameplay Settings (Seconds) ---
CMD_COOLDOWN: float = _parse_float(os.getenv("CMD_COOLDOWN", "2.0"), 2.0)
GAME_START_COOLDOWN: float = _parse_float(os.getenv("GAME_START_COOLDOWN", "2.5"), 2.5)
HINT_COOLDOWN: float = _parse_float(os.getenv("HINT_COOLDOWN", "10.0"), 10.0)
REFRESH_COOLDOWN: float = _parse_float(os.getenv("REFRESH_COOLDOWN", "12.0"), 12.0)
CALLBACK_COOLDOWN: float = _parse_float(os.getenv("CALLBACK_COOLDOWN", "1.0"), 1.0)
GUESS_COOLDOWN: float = _parse_float(os.getenv("GUESS_COOLDOWN", "0.35"), 0.35)
MAX_HINTS_PER_ROUND: int = _parse_int(os.getenv("MAX_HINTS_PER_ROUND", "3"), 3)
WORDSEEK_MAX_GUESSES: int = _parse_int(os.getenv("WORDSEEK_MAX_GUESSES", "30"), 30)
PORT: int = _parse_int(os.getenv("PORT", "0"), 0)
