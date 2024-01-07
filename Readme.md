# Stocks WhatsApp (Meta) notifier

![Contributors](https://img.shields.io/github/contributors/jvsadek/Coursera-Machine-Learning?style=plastic)
![Forks](https://img.shields.io/github/forks/jvsadek/Coursera-Machine-Learning)
![Stars](https://img.shields.io/github/stars/jvsadek/Coursera-Machine-Learning)
![Licence](https://img.shields.io/github/license/jvsadek/Coursera-Machine-Learning)
![Issues](https://img.shields.io/github/issues/jvsadek/Coursera-Machine-Learning)

## 
### Description
This is my first Flask app utilizing the [yfinance](https://pypi.org/project/yfinance/) and [heyoo](https://pypi.org/project/heyoo/) Python libraries to get WhatsApp notification when my favourite stock 📈, do a certain move 🕺. 

### This is not financial advice!
![](https://www.termsfeed.com/public/uploads/2023/02/harrington-investments-legal-disclaimer-no-investment-advice-risks-sections.jpg)


### Project motivation

While Twilio is a great sms notifier, I reached their free limit pricing [Twilio ](https://www.twilio.com/en-us/pricing/messaging)  
in no time. Therefore, I utilized the free Meta WhatsApp business api [1,000 conversation per month](https://developers.facebook.com/docs/whatsapp/pricing/). 
### Quick Start

1. Install yfinance using pip:

`$ pip install yfinance --upgrade --no-cache-dir`

2. Install heyoo using pip:

#### For Windows 

`pip install  --upgrade heyoo`

##### For Linux | MAC 

`pip3 install --upgrade heyoo`

3. Setup you Meta for Developers app

Follow the steps as mentioned in heyoo project, to be able to set up your `TOKEN` and `TEST WHATSAPP NUMBER` = `Phone_id`
and update it in `main.py`. 

4. Update your target stocks list in `main.py`

5. Update main.py with the phone number to receive the Whatsapp notification on `Your_phone_number`