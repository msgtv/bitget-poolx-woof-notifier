from bitget.bitget_api import BitgetApi

from config import (
    passphrase,
    api_key,
    secret_key,
    WOOF_COUNT_TO_INFORM,
    CHAT_ID,
    BOT_API,
    POOLX_URL,
)
from woof import get_available_coins
from send_message import send_message


def main():
    client = BitgetApi(
        api_key=api_key,
        api_secret_key=secret_key,
        passphrase=passphrase
    )

    woof_count = get_available_coins(client)

    if woof_count >= WOOF_COUNT_TO_INFORM:
        # send message
        send_message(
            BOT_API,
            chat_id=CHAT_ID,
            msg=f'🤑 На споте %.2f $WOOF.\n\n❤️‍🔥 Пора бы им в PoolX\n\n%s' % (woof_count, POOLX_URL)
        )
    # else:
    #     send_message(
    #         BOT_API,
    #         chat_id=CHAT_ID,
    #         msg=f'Количество $WOOF на споте: %.2f' % woof_count
    #     )


if __name__ == '__main__':
    main()
