from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    agent = {"User-Agent":"Mozilla/5.0"}
    url = 'https://www.noon.com/uae-en/electronics-and-mobiles/mobiles-and-accessories/mobiles-20905/'
    # source=requests.get(url, headers=agent).text
    # source = requests.get('https://www.noon.com/uae-en/electronics-and-mobiles/mobiles-and-accessories/mobiles-20905/').text
    # soup = BeautifulSoup(source, 'lxml')
    # name = []
    # for el in soup.find_all("div", {"class": "sc-e3js0d-9"}): 
    #     name.append({
    #         'name': el.find('div').get_text(), 
    #         'price': el.find("div", {"class": "sc-sxpmji-1"}).get_text()
    #     })

    name = [{
            "name": "Apple iPhone 13 Pro iPhone 13 Pro",
            "price": "AED 4969.00"
        },
    {
        "name": "Samsung Galaxy A03 Core Dual SIM Black 2GB RAM 32GB LTE - Middle East Version …",
        "price": "AED 338.00"
    }]
    sharaf_dg = [{
            "name": "Apple iPhone 13 Pro",
            "price": "AED 4969.00"
    },
    {
        "name": "Samsung Galaxy A03 Core Dual SIM Black 2GB RAM 32GB LTE - Middle East Version …",
        "price": "AED 339.00"
    }]

    result = []
    name.extend(sharaf_dg)
    for myDict in name:
        if myDict not in result:
            result.append(myDict)
            demo = myDict

    # result = {x['name']:x for x in name + sharaf_dg}.values()
        # name.append({})
        # head["name"] = el.get_text()
        # fyFmgb
    # price = []
    # for price in soup.find_all("div", {"class": "sc-sxpmji-1"}):
    #     price.append(price.get_text())

    # result = [dict(item, **{'price': }) for item in name]
    # children = head.findChildren("span" , recursive=False)
    # return render_template("index.html", soup=head)
    return jsonify(result)