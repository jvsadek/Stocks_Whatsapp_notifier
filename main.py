import os

from flask import Flask, render_template
app = Flask(__name__)

import pandas as pd
import yfinance as yf
from heyoo import WhatsApp
from datetime import datetime

## Heyoo Python wrapper for Whatsapp Business API
token = os.environ.get('TOKEN')
phone_id = os.environ.get('Phone_id')
messenger = WhatsApp(token=token, phone_number_id=phone_id)



Porto = ["ATER", "AMC", "BB", "GME"]

Tech = ['EAF','MMAT', 'PLL', 'ALB', 'SLI','CPNG','RBLX','AVAV','U', 'BBIG', 'ETSY', 'BX', 'ASML', 'PL', 'ANGH', 'NVDA', 'SIMO', 'LMND', 'Y', 'TWLO', 'SHOP', 'BABA',
        'MCHP', 'MRVL', 'INTC', 'TSM', 'MSFT', 'RKT', 'ORCL', 'NFLX', 'TWTR', 'MU', 'SNOW', 'EPAM', 'META', 'AMZN',
        'AAPL', 'ATVI', 'GFS', 'DWAC', 'ATER', 'SPCE', 'ZOM', 'PLTR', 'SNDL', 'CRSR', 'AMD', 'TDC', 'NOK', 'AMC',
        'BB', 'GME', 'DASH','VTNR','WM', 'HON', 'EQNR', 'APPS', 'OXY', 'OII', 'XOM', 'SHEl', 'AES', 'GP', 'CLNE', 'BP',
        'TELL', 'CVX', 'GE', 'GTLS', 'FSLR', 'PLUG', 'JKS', 'CSX', 'MATX', 'ZIM','GTLI', 'GRAB', 'UBER', 'SWVL', 'NIO', 'TSLA',
        'LCID', 'RIVN', 'NKLA', 'HOG', 'BA', 'RTX', 'CHRW', 'LMT', 'JPM', 'BAC', 'DAVE','MARA', 'MOC','DOLE','UAN','DBA', 'EDR', 'DCFC',
        'UUUU', 'DNN', 'CCJ', 'SRUUF', 'HCC', 'WEAT', 'NTR', 'OLN', 'ADM', 'BBBY', 'CLF', 'WISH','FDMT','EPIX', 'LQDA',
        'CRXT', 'PFE', 'BNTX', 'INO', 'VCNX', 'MRNA','SNY', 'NVS', 'GSK', 'CVAC', 'OCGN', 'HIMS', 'CLOV', 'SAVA']

Other_OTC = ['NTDOY', 'TCEHY']


@app.route("/")
def hello_world():

    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print("Current Time =", current_time)
    movers = []

    while current_time != "23:30":
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        print("Current Time =", current_time)

        for _ in Tech:
            globals()[_] = yf.download(tickers=_, period='1d', interval='1m', actions=False)
            globals()[_+"_arr"] = globals()[_]["Adj Close"].values-globals()[_]["Adj Close"].values[::-1, None]
            globals()[_+"arr_pre"] = (globals()[_]["Adj Close"].values-globals()[_]["Adj Close"].values[::-1, None])/globals()[_]["Adj Close"].values[::-1, None]*100
            globals()[_] = pd.DataFrame(globals()[_+"_arr"], columns = globals()[_].index.values[::-1], index=globals()[_].index.values[::-1])
            globals()[_+"_Pre"] = pd.DataFrame(globals()[_+"arr_pre"], columns = globals()[_].index.values[::-1], index=globals()[_].index.values[::-1])

            ## Condition for the stock notification
            condition = (globals()[_+"_Pre"].values > 5).any()
            print(condition)
            if condition and _ not in movers:
                messenger.send_message(
                    message=f"{_} has moved +/- 5%! Time to see",
                    recipient_id="Your_phone_number", )

                movers.append(_)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=True, port=server_port, host='0.0.0.0')