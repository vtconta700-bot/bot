# Bot Telegram em Python

## Arquivos
- `bot.py` — código do bot
- `requirements.txt` — dependência do Python

## Rodar localmente

Defina a variável `BOT_TOKEN` com o token recebido do BotFather.

Windows:
```bat
set BOT_TOKEN=SEU_TOKEN
python bot.py
```

Linux/macOS:
```bash
export BOT_TOKEN="SEU_TOKEN"
python bot.py
```

## Render

Use um **Background Worker**.

Build Command:
```bash
pip install -r requirements.txt
```

Start Command:
```bash
python bot.py
```

Crie a variável de ambiente:
`BOT_TOKEN` = seu token do BotFather.

Nunca coloque o token diretamente no código ou publique o token no GitHub.
