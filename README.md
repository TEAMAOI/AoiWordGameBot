# 🎮 Word Grid Arcade + WordSeek Dual Bot


<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</p>

<p align="center">
  <img src="https://files.catbox.moe/jivakh.png" alt="AoiWaifu Bot" width="100%">
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</p>

All-in-one **Telegram Dual Word Game Bot** combining **3D Word Grid Arcade** and **WordSeek (Wordle 4L/5L/6L + Daily Mode)** inside a single **Kurigram/Pyrogram + Motor (Async MongoDB) + Pillow** repository, optimized for 512MB RAM dynos and Python 3.12+.

## 🚀 One-Click Deploy on Aoi Hosting

[![Deploy on Aoi Hosting](https://host-repository.vercel.app/deploy-button.svg)](https://host-repository.vercel.app/deploy?template=https://github.com/TEAMAOI/AoiWordGameBot.git)

> **Note:** After pushing this repo to GitHub, replace `OWNER/REPO` in the button URL above with your actual GitHub `username/repo`.

## ✨ Key Features

- **🧩 Word Grid Arcade (3D Word Search)**: 5,600+ curated English words (`bot/utils/words.json`), 8 neon 3D Pillow themes, per-chat async locks, non-blocking board rendering, and `/game`, `/hint`, `/stopgame`.
- **🟩 WordSeek (Wordle 4, 5 & 6 Letters + Daily Mode)**: 4-letter (`/new4`), 5-letter (`/new`, `/new5`, `/wordseek`), and 6-letter (`/new6`) modes in groups and DMs, Daily WordSeek (`/daily`, `/pausedaily`) with Pillow-rendered dark Wordle boards, definitions/IPA phonetics, 3-player vote-to-end (`/end`), group admin authorization (`/seekauth`), and forum topic controls.
- **🏆 Dual Leaderboards & Profiles**: Combined Word Grid + WordSeek player profiles (`/profile`, `/rank`), interactive leaderboards (`/leaderboard`, `/top`), and detailed WordSeek score history (`/score`).
- **🛡️ Admin Panel**: Built-in `/panel`, `/stats`, `/ban`, `/unban`, `/transfer`, and `/broadcast` restricted to `SUDO_USERS`.

## 🛠️ Manual Setup

1. **Clone the repository** and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. **Configure environment variables**:
   Copy `.env.example` to `.env` and fill in `API_ID`, `API_HASH`, `BOT_TOKEN`, `MONGO_URI`, and `SUDO_USERS`.
3. **Run the bot**:
   ```bash
   python run.py
   ```

## ⚙️ Commands

| Command | Description |
| :--- | :--- |
| `/start` | Open the main Dual Word Game dashboard |
| `/game` | Start a 3D Word Grid Arcade round in a group |
| `/hint` | Reveal a letter hint in Word Grid |
| `/stopgame` | Stop the active Word Grid round |
| `/new` / `/wordseek` | Start a 5-letter WordSeek game (or `/new 4`, `/new 6`) |
| `/new4` / `/new5` / `/new6` | Start a 4, 5, or 6-letter WordSeek game |
| `/end` / `/endseek` | End the current WordSeek game (admin/starter or 3-player vote) |
| `/daily` / `/pausedaily` | Play or pause Daily WordSeek in Private Chat (DM) |
| `/score` / `/myscore` | View WordSeek scores & streaks (`/score [global\|group] [today\|week\|month\|all] [4\|5\|6]`) |
| `/profile` / `/rank` | View combined Word Grid + WordSeek player profile card |
| `/leaderboard` / `/top` | View interactive Dual Leaderboards (Word Grid & WordSeek) |
| `/seekauth` | Authorize group members to end WordSeek games without voting |
| `/setgametopic` / `/unsetgametopic` | Restrict games to specific forum topics |
| `/allowonlylen` | Set allowed WordSeek lengths in a topic (`/allowonlylen 5 4 6`) |
| `/id` | View chat, user, topic, and message IDs |
| `/panel` / `/admin` / `/stats` | Admin dashboard & live system stats (`SUDO_USERS` only) |
| `/ban` / `/unban` / `/transfer` | Global user moderation & score transfer (`SUDO_USERS` only) |
| `/broadcast` | Reply to any message to broadcast to all users & groups (`SUDO_USERS` only) |

---

## 🌐 Community & Support

- **Telegram Channel:** [@aoinetwork](https://t.me/aoinetwork)
- **Support Group:** [@devpointserror](https://t.me/devpointserror)
- 
