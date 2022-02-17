from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
from flask import jsonify
import json
import re, cgi

app = Flask(__name__)

@app.route('/')
def hello():
    agent = {"User-Agent":"Mozilla/5.0"}
    noon_url = 'https://www.noon.com/uae-en/electronics-and-mobiles/mobiles-and-accessories/mobiles-20905/'
    sharaf_url = 'https://uae.sharafdg.com/c/mobiles_tablets/mobiles/'
    noon_source = requests.get(noon_url, headers=agent).text
    sharaf_source = requests.get(sharaf_url, headers=agent).text
    # source = requests.get('https://www.noon.com/uae-en/electronics-and-mobiles/mobiles-and-accessories/mobiles-20905/').text
    noon_soup = BeautifulSoup(noon_source, 'lxml')
    sharaf_soup = BeautifulSoup(sharaf_source, 'lxml')
    noon_data = []

    for ns in noon_soup.find_all("div", {"class": "sc-e3js0d-9"}): 
        noon_name = ns.find('div').get_text(), 
        noon_name = ''.join(noon_name)
        noon_old_price = ns.find("span", {"class": "oldPrice"})
        noon_data.append({
            'name': ' '.join(noon_name.split()[:3]),
            'price': ns.find("div", {"class": "sc-sxpmji-1"}).get_text(),
            # 'old_price': noon_old_price
        })
    sharaf_dg = []
    # shd = sh_soup.find_all("div", {"class": "product-container"})
    # shd2 = shd.find_all("div", {"class": "product-container"})
    for sh in sharaf_soup.find_all("div", {"class": "slide"}):
        sh_name = sh.find('h4').get_text()
        sharaf_dg.append({
            'name': ' '.join(sh_name.split()[:3]),
            'price': sh.find("div", {"class": "price"}).get_text()
        }), 
            # 'price': sh.find("div", {"class": "price"}).get_text()
        # })
    # name = [{
    #         "name": "Apple iPhone 13 Pro iPhone 13 Pro",
    #         "price": "AED 4969.00"
    #     },
    # {
    #     "name": "Samsung Galaxy A03 Core Dual SIM Black 2GB RAM 32GB LTE - Middle East Version …",
    #     "price": "AED 338.00"
    # }]
    # sharaf_dg = [{
    #         "name": "Apple iPhone 13 Pro",
    #         "price": "AED 4969.00"
    # },
    # {
    #     "name": "Samsung Galaxy A03 Core Dual SIM Black 2GB RAM 32GB LTE - Middle East Version …",
    #     "price": "AED 339.00"
    # }]
    result = []
    # name.extend(sharaf_dg)
    same = []
    same_two = []
    count = 0
    for myDict in noon_data:
        for myDictTwo in sharaf_dg:
            if (myDict['name'] != myDictTwo['name']):
                if not any(n['name'] == myDict['name'] for n in result):
                    result.append(myDict)
                if not any(s['name'] == myDictTwo['name'] for s in result):
                    result.append(myDictTwo)
                continue
                # count = count+1
                # same.append(myDict)
                # same_two.append(myDictTwo)
                # continue
            # demo = myDict
    # result = {x['name']:x for x in name + sharaf_dg}.values()
        # name.append({})
        # head["name"] = el.get_text()
        # fyFmgb
    # price = []
    # for price in soup.find_all("div", {"class": "sc-sxpmji-1"}):
    #     price.append(price.get_text())
    # result = [dict(item, **{'price': }) for item in name]
    # children = head.findChildren("span" , recursive=False)
    # return render_template("index.html", soup=result)
    with open("scraped.json", "w") as outfile:
        json.dump(result, outfile)
    return jsonify(result)