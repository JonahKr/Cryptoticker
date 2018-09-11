# Cryptoticker
This is the Code for a crypto ticker. V 2.1
Information source: https://coinmarketcap.com/api/
Library:
https://github.com/hzeller/rpi-rgb-led-matrix

---

In the [Config file](https://github.com/JonahKr/Cryptoticker/blob/master/config.json) you need to set the cryptocurrencies you want to be displayed:

!!! Watch out to set the symbols and not the name !!!  
*example* :
```json
{
"cryptocurrencies":["BTC","ETH","DASH"]
}
```
You cn find a list of all possible Cryptocurrencies [here](https://api.coinmarketcap.com/v2/listings/)

---
You have to set the fiat currency/currencies the *Cryptocurrencies* should be displayed in, in the [Config file](https://github.com/JonahKr/Cryptoticker/blob/master/config.json) aswell.

[Valid fiat currencies:](https://coinmarketcap.com/api/#endpoint_ticker_specific_cryptocurrency)

 *AUD, BRL, CAD, CHF, CLP, CNY, CZK, DKK, EUR, GBP, HKD, HUF, IDR, ILS, INR, JPY, KRW, MXN, MYR, NOK, NZD, PHP, PKR, PLN, RUB, SEK, SGD, THB, TRY, TWD, ZAR*

It is also possible to display the price in one of five cryptocurrencies:
*BTC, ETH, XRP, LTC, and BCH*

!!! Watch out to set the symbols and not the name !!!  
*example* :
```json
{
"cryptocurrencies":["BTC","ETH","DASH"],
"fiatcurrencies":["USD","EUR","BTC"]
}
```
---
Depending on which, how many *RGB-Pannel/s* and which modules you use, you have to adapt the [startup.sh](https://github.com/JonahKr/Cryptoticker/blob/master/startup.sh) file to your needs.
You can find a detailed tutorial [here](https://github.com/hzeller/rpi-rgb-led-matrix).

Last but not least you start the Ticker out of your projectfolder:
`chmod +x startup.sh` - give the script permission to Execute

`sudo ./startup.h`
🎉 Have fun 🎉
