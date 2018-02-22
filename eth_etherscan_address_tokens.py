#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://etherscan.io/address/"

def output_token_data(tokens):
    for token in tokens.findAll('a'):
        add = token['href'].split('/')
        print(add[2][:42]),

        balance = token.find('br').text.split(' ')
        value = balance[0]
        print(value),
        sym = balance[1]

        if '@' in sym:
            print(sym.split('@')[0])
        else:
            print(sym)


def get_token_data(sess, url):
    soup = BeautifulSoup(sess.get(url).text, 'html.parser')
    return soup.find("ul", { "id": "balancelist" })


def main():
    address = str(raw_input("Please input an address: ").strip())

    url = BASE_URL + address
    resp = requests.get(url)
    sess = requests.Session()

    output_token_data(get_token_data(sess, url))


if __name__ == "__main__":
    main()
