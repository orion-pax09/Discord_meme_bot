# Discord_meme_bot

A simple Discord bot built with Python and `discord_bot.py` that fetches random memes from [meme-api.com](https://meme-api.com) and posts them straight into your server

---

## ✨ Features

- 👋 `$hello` greeting command
- 🎭 Category-based meme command (`$meme <category>`)
- 📢 Responds with a meme when mentioned
- 📋 Lists available meme categories for invalid commands
- 📂 Supports categories like:
  - programming
  - gaming
  - wholesome
  - anime
  - football
  - college
  - gym
  - cats
  - dogs
  - dark
  - pakistan
  - history
  - science
  - marvel
  - starwars
  - cars
  - and more...
- 🔐 Secure token management with `.env`
- ☁️ Deployed on Railway
- 🔞 Automatically skips NSFW-flagged memes
- 🔐 Keeps your bot token safe using environment variables (`.env`)

---

## 🛠️ Technologies

- Python 3.13
- [discord.py](https://discordpy.readthedocs.io/)
- [requests](https://docs.python-requests.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📦 Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/discord-meme-bot.git
cd discord-meme-bot
```

**2. Install dependencies**

```bash
py -m pip install -r requirements.txt
```

**3. Set up your bot token**

Copy the example env file and fill in your real token:

```bash
cp .env.example .env
```

Then open `.env` and replace the placeholder:

```env
DISCORD_TOKEN=your_discord_bot_token_here
```

> Get your token from the (https://discord.com/developers/applications) under your application's **Bot** section. Make sure **Message Content Intent** is enabled there too, or the bot won't be able to read message text.

**4. Run the bot**

```bash
py discord_bot.py
```

If everything's set up correctly, your terminal should print:

```
Logged on as YourBotName#1234
```

---

## 💬 Commands

`$hello` :- Greets the user who sent it 

---

`@your bot name` :- Sends a random meme as an embed 


---

## 📁 Project Structure

```
discord-meme-bot/
│
├── discord_bot.py      # Main bot code
├── requirements.txt    # Python dependencies
├── .env                # Your actual secrets (never committed)
├── .gitignore           # Keeps .env and junk files out of git
└── README.md            # You're reading it
```

---

## 🔐 Security Note

**Never commit your `.env` file or bot token to GitHub.** This project's `.gitignore` already excludes `.env` by default — leave it that way. If a token is ever accidentally exposed, reset it immediately from the Developer Portal.

---

## 👤 Author

Muhammad Hamza Khan
