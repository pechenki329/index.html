<!DOCTYPE html>
<html>
<head>
    <title>Sticker Race</title>
    <meta charset="utf-8">
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        body {
            text-align: center;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }
        h1 { font-size: 28px; margin-bottom: 30px; }
        .emoji { font-size: 100px; margin: 30px; }
        .stickers { display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; }
        .sticker {
            width: 100px;
            height: 100px;
            cursor: pointer;
            border: 4px solid white;
            border-radius: 15px;
            transition: all 0.3s;
        }
        .sticker:hover { transform: scale(1.1); border-color: gold; }
        .message { font-size: 24px; margin: 20px; min-height: 40px; }
        button {
            background: gold;
            color: #333;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>🎮 Кто быстрее подберет стикер?</h1>
    <div class="emoji" id="emoji">😊</div>
    <div class="stickers" id="stickers"></div>
    <div class="message" id="message"></div>
    <button onclick="newRound()">🎲 Следующий раунд</button>

    <script>
        let tg = Telegram.WebApp;
        tg.expand();

        const stickers = {
            '😊': 'https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f60a.png',
            '😂': 'https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f602.png'
        };

        let currentCorrect = stickers['😊'];

        function newRound() {
            document.getElementById('emoji').textContent = '😊';
            currentCorrect = stickers['😊'];
            document.getElementById('message').innerHTML = '';
            showStickers();
        }

        function showStickers() {
            let html = '';
            html += '<img src="' + stickers['😊'] + '" class="sticker" onclick="check(true)">';
            html += '<img src="' + stickers['😂'] + '" class="sticker" onclick="check(false)">';
            document.getElementById('stickers').innerHTML = html;
        }

        function check(isCorrect) {
            if (isCorrect) {
                document.getElementById('message').innerHTML = '✅ ПРАВИЛЬНО!';
                tg.sendData(JSON.stringify({result: 'win'}));
            } else {
                document.getElementById('message').innerHTML = '❌ НЕПРАВИЛЬНО!';
            }
        }

        newRound();
    </script>
</body>
</html>
