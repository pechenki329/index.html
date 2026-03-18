<!DOCTYPE html>
<html>
<head>
    <title>Sticker Race</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
        .emoji { font-size: 100px; margin: 30px; animation: bounce 1s infinite; }
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }
        .stickers {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
            margin: 30px 0;
        }
        .sticker {
            width: 120px;
            height: 120px;
            cursor: pointer;
            border: 4px solid white;
            border-radius: 20px;
            transition: all 0.3s;
            box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        }
        .sticker:hover {
            transform: scale(1.1);
            border-color: gold;
            box-shadow: 0 15px 30px rgba(0,0,0,0.4);
        }
        .message {
            font-size: 28px;
            margin: 20px;
            padding: 15px;
            border-radius: 15px;
            font-weight: bold;
            min-height: 60px;
        }
        button {
            background: gold;
            color: #333;
            border: none;
            padding: 15px 40px;
            font-size: 20px;
            border-radius: 30px;
            cursor: pointer;
            font-weight: bold;
            margin-top: 20px;
            transition: all 0.3s;
        }
        button:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }
        .score {
            font-size: 24px;
            margin: 20px;
            color: gold;
        }
    </style>
</head>
<body>
    <h1>🎮 Кто быстрее подберет стикер?</h1>
    <div class="emoji" id="emoji">😊</div>
    <div class="stickers" id="stickers"></div>
    <div class="message" id="message">Выбери стикер!</div>
    <div class="score" id="score">Счет: 0</div>
    <button id="nextBtn" onclick="nextRound()">🎲 Следующий раунд</button>

    <script>
        // Инициализация Telegram
        let tg = Telegram.WebApp;
        tg.expand();
        tg.ready();

        // База данных игры
        const gameData = {
            '😊': 'https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f60a.png',
            '😂': 'https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f602.png',
            '😍': 'https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f60d.png',
            '😎': 'https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f60e.png',
            '🥳': 'https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f973.png'
        };

        const emojis = Object.keys(gameData);
        let currentEmoji = '😊';
        let currentCorrectSticker = gameData['😊'];
        let score = 0;
        let gameActive = true;
// Функция показа стикеров
        function showStickers() {
            const stickersDiv = document.getElementById('stickers');
            stickersDiv.innerHTML = '';
            
            // Получаем все стикеры
            const allStickers = Object.values(gameData);
            
            // Перемешиваем и берем 3 случайных
            const shuffled = [...allStickers].sort(() => Math.random() - 0.5);
            const selectedStickers = shuffled.slice(0, 3);
            
            // Если правильного стикера нет в выбранных - добавляем его
            if (!selectedStickers.includes(currentCorrectSticker)) {
                selectedStickers[0] = currentCorrectSticker;
                // Снова перемешиваем
                selectedStickers.sort(() => Math.random() - 0.5);
            }
            
            // Отображаем стикеры
            selectedStickers.forEach(sticker => {
                const img = document.createElement('img');
                img.src = sticker;
                img.className = 'sticker';
                img.onclick = () => checkSticker(sticker);
                stickersDiv.appendChild(img);
            });
        }

        // Функция проверки выбора
        window.checkSticker = function(selectedSticker) {
            if (!gameActive) return;
            
            if (selectedSticker === currentCorrectSticker) {
                // Правильный выбор
                gameActive = false;
                score++;
                document.getElementById('score').textContent = Счет: ${score};
                document.getElementById('message').innerHTML = '✅ ПРАВИЛЬНО! +1 очко';
                document.getElementById('message').style.color = '#4caf50';
                
                // Отправляем результат в Telegram
                tg.sendData(JSON.stringify({
                    result: 'win',
                    score: score,
                    emoji: currentEmoji
                }));
                
                // Подсвечиваем правильный стикер
                highlightCorrect();
            } else {
                // Неправильный выбор
                document.getElementById('message').innerHTML = '❌ НЕПРАВИЛЬНО! Попробуй другой';
                document.getElementById('message').style.color = '#f44336';
                
                // Эффект для неправильного стикера
                event.target.style.transform = 'scale(0.9)';
                event.target.style.opacity = '0.5';
                setTimeout(() => {
                    event.target.style.transform = 'scale(1)';
                    event.target.style.opacity = '1';
                }, 200);
            }
        };

        // Функция подсветки правильного стикера
        function highlightCorrect() {
            const stickers = document.querySelectorAll('.sticker');
            stickers.forEach(sticker => {
                if (sticker.src === currentCorrectSticker) {
                    sticker.style.borderColor = '#4caf50';
                    sticker.style.transform = 'scale(1.1)';
                } else {
                    sticker.style.opacity = '0.3';
                }
            });
        }

        // Запускаем первый раунд
        window.onload = function() {
            nextRound();
        };
    </script>
</body>
</html>
        // Функция нового раунда
        window.nextRound = function() {
            // Выбираем случайный эмодзи
            const randomIndex = Math.floor(Math.random() * emojis.length);
            currentEmoji = emojis[randomIndex];
            currentCorrectSticker = gameData[currentEmoji];
            
            // Обновляем отображение
            document.getElementById('emoji').textContent = currentEmoji;
            document.getElementById('message').innerHTML = 'Выбери стикер!';
            document.getElementById('message').style.color = 'white';
            
            // Показываем стикеры
            showStickers();
            gameActive = true;
        };
        
