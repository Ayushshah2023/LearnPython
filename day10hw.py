Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========== RESTART: C:\Users\Pranav\Desktop\PYTHON\Bitcoin_price.py ==========
Enter the Currency Code"USD"
Enter the value"500"
 https://blockchain.info/ticker?currency ="USD"&value="500"
<Response [200]> {
  "USD" : {"15m" : 10407.48, "last" : 10407.48, "buy" : 10407.48, "sell" : 10407.48, "symbol" : "$"},
  "AUD" : {"15m" : 15197.84, "last" : 15197.84, "buy" : 15197.84, "sell" : 15197.84, "symbol" : "$"},
  "BRL" : {"15m" : 42274.15, "last" : 42274.15, "buy" : 42274.15, "sell" : 42274.15, "symbol" : "R$"},
  "CAD" : {"15m" : 13708.22, "last" : 13708.22, "buy" : 13708.22, "sell" : 13708.22, "symbol" : "$"},
  "CHF" : {"15m" : 10277.91, "last" : 10277.91, "buy" : 10277.91, "sell" : 10277.91, "symbol" : "CHF"},
  "CLP" : {"15m" : 7406934.35, "last" : 7406934.35, "buy" : 7406934.35, "sell" : 7406934.35, "symbol" : "$"},
  "CNY" : {"15m" : 74056.52, "last" : 74056.52, "buy" : 74056.52, "sell" : 74056.52, "symbol" : "¥"},
  "DKK" : {"15m" : 70429.52, "last" : 70429.52, "buy" : 70429.52, "sell" : 70429.52, "symbol" : "kr"},
  "EUR" : {"15m" : 9438.14, "last" : 9438.14, "buy" : 9438.14, "sell" : 9438.14, "symbol" : "€"},
  "GBP" : {"15m" : 8472.0, "last" : 8472.0, "buy" : 8472.0, "sell" : 8472.0, "symbol" : "£"},
  "HKD" : {"15m" : 81593.1, "last" : 81593.1, "buy" : 81593.1, "sell" : 81593.1, "symbol" : "$"},
  "INR" : {"15m" : 745997.95, "last" : 745997.95, "buy" : 745997.95, "sell" : 745997.95, "symbol" : "₹"},
  "ISK" : {"15m" : 1314566.98, "last" : 1314566.98, "buy" : 1314566.98, "sell" : 1314566.98, "symbol" : "kr"},
  "JPY" : {"15m" : 1113255.32, "last" : 1113255.32, "buy" : 1113255.32, "sell" : 1113255.32, "symbol" : "¥"},
  "KRW" : {"15m" : 1.241378506E7, "last" : 1.241378506E7, "buy" : 1.241378506E7, "sell" : 1.241378506E7, "symbol" : "₩"},
  "NZD" : {"15m" : 16195.08, "last" : 16195.08, "buy" : 16195.08, "sell" : 16195.08, "symbol" : "$"},
  "PLN" : {"15m" : 40936.27, "last" : 40936.27, "buy" : 40936.27, "sell" : 40936.27, "symbol" : "zł"},
  "RUB" : {"15m" : 684682.26, "last" : 684682.26, "buy" : 684682.26, "sell" : 684682.26, "symbol" : "RUB"},
  "SEK" : {"15m" : 100402.03, "last" : 100402.03, "buy" : 100402.03, "sell" : 100402.03, "symbol" : "kr"},
  "SGD" : {"15m" : 14377.94, "last" : 14377.94, "buy" : 14377.94, "sell" : 14377.94, "symbol" : "$"},
  "THB" : {"15m" : 316325.03, "last" : 316325.03, "buy" : 316325.03, "sell" : 316325.03, "symbol" : "฿"},
  "TWD" : {"15m" : 324659.14, "last" : 324659.14, "buy" : 324659.14, "sell" : 324659.14, "symbol" : "NT$"}
} <class 'str'>
{'USD': {'15m': 10407.48, 'last': 10407.48, 'buy': 10407.48, 'sell': 10407.48, 'symbol': '$'}, 'AUD': {'15m': 15197.84, 'last': 15197.84, 'buy': 15197.84, 'sell': 15197.84, 'symbol': '$'}, 'BRL': {'15m': 42274.15, 'last': 42274.15, 'buy': 42274.15, 'sell': 42274.15, 'symbol': 'R$'}, 'CAD': {'15m': 13708.22, 'last': 13708.22, 'buy': 13708.22, 'sell': 13708.22, 'symbol': '$'}, 'CHF': {'15m': 10277.91, 'last': 10277.91, 'buy': 10277.91, 'sell': 10277.91, 'symbol': 'CHF'}, 'CLP': {'15m': 7406934.35, 'last': 7406934.35, 'buy': 7406934.35, 'sell': 7406934.35, 'symbol': '$'}, 'CNY': {'15m': 74056.52, 'last': 74056.52, 'buy': 74056.52, 'sell': 74056.52, 'symbol': '¥'}, 'DKK': {'15m': 70429.52, 'last': 70429.52, 'buy': 70429.52, 'sell': 70429.52, 'symbol': 'kr'}, 'EUR': {'15m': 9438.14, 'last': 9438.14, 'buy': 9438.14, 'sell': 9438.14, 'symbol': '€'}, 'GBP': {'15m': 8472.0, 'last': 8472.0, 'buy': 8472.0, 'sell': 8472.0, 'symbol': '£'}, 'HKD': {'15m': 81593.1, 'last': 81593.1, 'buy': 81593.1, 'sell': 81593.1, 'symbol': '$'}, 'INR': {'15m': 745997.95, 'last': 745997.95, 'buy': 745997.95, 'sell': 745997.95, 'symbol': '₹'}, 'ISK': {'15m': 1314566.98, 'last': 1314566.98, 'buy': 1314566.98, 'sell': 1314566.98, 'symbol': 'kr'}, 'JPY': {'15m': 1113255.32, 'last': 1113255.32, 'buy': 1113255.32, 'sell': 1113255.32, 'symbol': '¥'}, 'KRW': {'15m': 12413785.06, 'last': 12413785.06, 'buy': 12413785.06, 'sell': 12413785.06, 'symbol': '₩'}, 'NZD': {'15m': 16195.08, 'last': 16195.08, 'buy': 16195.08, 'sell': 16195.08, 'symbol': '$'}, 'PLN': {'15m': 40936.27, 'last': 40936.27, 'buy': 40936.27, 'sell': 40936.27, 'symbol': 'zł'}, 'RUB': {'15m': 684682.26, 'last': 684682.26, 'buy': 684682.26, 'sell': 684682.26, 'symbol': 'RUB'}, 'SEK': {'15m': 100402.03, 'last': 100402.03, 'buy': 100402.03, 'sell': 100402.03, 'symbol': 'kr'}, 'SGD': {'15m': 14377.94, 'last': 14377.94, 'buy': 14377.94, 'sell': 14377.94, 'symbol': '$'}, 'THB': {'15m': 316325.03, 'last': 316325.03, 'buy': 316325.03, 'sell': 316325.03, 'symbol': '฿'}, 'TWD': {'15m': 324659.14, 'last': 324659.14, 'buy': 324659.14, 'sell': 324659.14, 'symbol': 'NT$'}} <class 'dict'>
The value in USD is : $  10407.48
THe value in INR is : http://data.fixer.io/api/convert?access_key=83d32efcf69d48899d6e82006d86489d&from=USD&to=INR&amount=$  10407.48
>>> 
========== RESTART: C:\Users\Pranav\Desktop\PYTHON\Bitcoin_price.py ==========
Enter the Currency Code"USD"
Enter the value"500"
 https://blockchain.info/ticker?currency ="USD"&value="500"
The value in USD is : $  10411.05
THe value in INR is : http://data.fixer.io/api/convert?access_key=83d32efcf69d48899d6e82006d86489d&from=USD&to=INR&amount=$  10411.05
>>> 
========== RESTART: C:\Users\Pranav\Desktop\PYTHON\Bitcoin_price.py ==========
Enter the Currency Code"USD"
Enter the value"500"
 https://blockchain.info/ticker?currency ="USD"&value="500"
The value in USD is : $  10410.61
THe value in INR is : http://data.fixer.io/api/convert?access_key=83d32efcf69d48899d6e82006d86489d&from=USD&to=INR&amount=$  10410.61
>>> 
========== RESTART: C:\Users\Pranav\Desktop\PYTHON\Bitcoin_price.py ==========
Enter the Currency Code"USD"
Enter the value"500"
 https://blockchain.info/ticker?currency ="USD"&value="500"
The value in USD is : $  10437.77
Traceback (most recent call last):
  File "C:\Users\Pranav\Desktop\PYTHON\Bitcoin_price.py", line 19, in <module>
    BitCoin_price(input("Enter the Currency Code"),input("Enter the value"))
  File "C:\Users\Pranav\Desktop\PYTHON\Bitcoin_price.py", line 17, in BitCoin_price
    inr_value=j_resp["rates"]["INR"]*usd_value
KeyError: 'rates'
>>> 
========== RESTART: C:\Users\Pranav\Desktop\PYTHON\Bitcoin_price.py ==========
Enter the Currency Code"USD"
Enter the value"500"
 https://blockchain.info/ticker?currency ="USD"&value="500"
The value in USD is : $  10433.1
{'success': False, 'error': {'code': 105, 'type': 'function_access_restricted', 'info': 'Access Restricted - Your current Subscription Plan does not support this API Function.'}}
Traceback (most recent call last):
  File "C:\Users\Pranav\Desktop\PYTHON\Bitcoin_price.py", line 20, in <module>
    BitCoin_price(input("Enter the Currency Code"),input("Enter the value"))
  File "C:\Users\Pranav\Desktop\PYTHON\Bitcoin_price.py", line 18, in BitCoin_price
    inr_value=j_resp["rates"]["INR"]*usd_value
KeyError: 'rates'
>>> 
========== RESTART: C:\Users\Pranav\Desktop\PYTHON\Bitcoin_price.py ==========
Enter the Currency Code"USD"
Enter the value"500"
 https://blockchain.info/ticker?currency ="USD"&value="500"
The value in USD is : $  10434.82
Traceback (most recent call last):
  File "C:\Users\Pranav\Desktop\PYTHON\Bitcoin_price.py", line 20, in <module>
    BitCoin_price(input("Enter the Currency Code"),input("Enter the value"))
  File "C:\Users\Pranav\Desktop\PYTHON\Bitcoin_price.py", line 18, in BitCoin_price
    inr_value=j_resp["rates"]["INR"]*usd_value
KeyError: 'rates'
>>> 
========== RESTART: C:\Users\Pranav\Desktop\PYTHON\Bitcoin_price.py ==========
Enter the Currency Code"USD"
Enter the value"500"
 https://blockchain.info/ticker?currency ="USD"&value="500"
The value in USD is : $  10455.51
Traceback (most recent call last):
  File "C:\Users\Pranav\Desktop\PYTHON\Bitcoin_price.py", line 20, in <module>
    BitCoin_price(input("Enter the Currency Code"),input("Enter the value"))
  File "C:\Users\Pranav\Desktop\PYTHON\Bitcoin_price.py", line 18, in BitCoin_price
    inr_value=j_resp["rates"]["1"]["INR"]*usd_value
KeyError: 'rates'
>>> 
========== RESTART: C:\Users\Pranav\Desktop\PYTHON\Bitcoin_price.py ==========
Enter the Currency Code"USD"
Enter the value"500"
 https://blockchain.info/ticker?currency ="USD"&value="500"
The value in USD is : $  10453.0
Traceback (most recent call last):
  File "C:\Users\Pranav\Desktop\PYTHON\Bitcoin_price.py", line 21, in <module>
    BitCoin_price(input("Enter the Currency Code"),input("Enter the value"))
  File "C:\Users\Pranav\Desktop\PYTHON\Bitcoin_price.py", line 19, in BitCoin_price
    inr_value=71.73*usd_value
TypeError: can't multiply sequence by non-int of type 'float'
>>> 
========== RESTART: C:\Users\Pranav\Desktop\PYTHON\Bitcoin_price.py ==========
Enter the Currency Code"USD"
Enter the value"500"
 https://blockchain.info/ticker?currency ="USD"&value="500"
The value in USD is : $  10462.96
THe value in INR is : 750508.1208
>>> 
