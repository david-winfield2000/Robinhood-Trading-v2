from dataclasses import dataclass
import time
from datetime import datetime
import robin_stocks.robinhood as r

# Log into robinhood
login = r.login("david.winfield2000@gmail.com",
                "Knightro@123")

stock = "ASLN"
shares = 0

high = 0
low = 0
current = 0

# def setup():
#     with open('setup.txt') as f:
#         lines = f.readlines()
#         stock = lines[1].strip()
#         shares = lines[3].strip()
#         f.close()




# while True:
#     # high increases -> raise sell point


#     # price dips to sell point -> sell all

def setup():
    try:
        r.order_sell_stop_loss(stock, 0.82)
    except Exception as e:
        print(e)

    global current, high, low

    current = float(r.get_latest_price(stock)[0])

    high = float(current)

    low = float(high) * 0.85

    print(current, high, low)

setup()

while True:
    current = float(r.get_latest_price(stock)[0])

    print(datetime.now(), ": ", current)

    # high increases -> raise sell point


    # price dips to sell point -> sell all

    time.sleep(1)