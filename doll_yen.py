import requests
from bs4 import BeautifulSoup

bid = []
ask = []
change = []
open_ = []
high = []
low = []

def get_values():
    load_url = "https://finance.yahoo.co.jp/quote/USDJPY=FX?frm=1mntly&ovrIndctr=sma%2Cmma%2Clma&addIndctr="
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")

    values = soup.find(class_="AUqxmBEI")
    values = values.find_all(class_="_3Pvw_N8d")
    for value in values:
        print(value.text)

if __name__ == "__main__":
    main()