import requests


def send_message(token: str, chat_id: str, msg: str):
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}'
    requests.get(url)
