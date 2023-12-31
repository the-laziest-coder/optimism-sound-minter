RPCs = {
    'Optimism':  'https://rpc.ankr.com/optimism',
}

###############################################################################################################

# Время ожидания между выполнением разных акков рандомное в указанном диапазоне
NEXT_ADDRESS_MIN_WAIT_TIME = 0  # В минутах
NEXT_ADDRESS_MAX_WAIT_TIME = 0.1  # В минутах

# Максимальное кол-во попыток сделать запрос/транзакцию если они фейлятся
MAX_TRIES = 3

###############################################################################################################

# Множитель газа
GAS_PRICE_MULT = 1.2

###############################################################################################################

# Токен и chat id бота в тг. Можно оставить пустым.
TELEGRAM_BOT_TOKEN = ''
TELEGRAM_CHAT_ID = 0
# При True, скрипт только выдает ваш chat id для отправки сообщений в боте.
GET_TELEGRAM_CHAT_ID = False

###############################################################################################################

# Адрес NFT для минта
# Минтить можно не все нфт
# Перед тем как запускать скрипт, надо попробовать заминтить через сайт (достаточно инициировать транзу)
# и убедиться что адрес контракта, с которым будет взаимодействие, следующий:
# 0x403471CbcAB399896004bc0AF2b4674D4Ab3b53B
NFT_ADDRESS = '0xA3dFfe601E086D0854C94487FD481312C374151e'
# Этот параметр можно посмотреть в любой транзакции минта указанной NFT
MINT_INDEX = 0
