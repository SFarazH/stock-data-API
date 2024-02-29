from flask import Flask, request, jsonify
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import numpy as np
import os
from sectors import sectors_url

app = Flask(__name__)


def stock_data_to_dict(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')
    
    raw_stock_prices = []
    
    s = soup.select('td.right')
    for element in s:
        raw_stock_prices.append(element.text)
    stock_name = soup.select('td.left')
    values =[]
    ticker =[]
    for i in range(0, len(raw_stock_prices)):
        price = raw_stock_prices[i]
        j = i+1
        if j%5 != 0:
            values.append(price.split()[1])
        else:
            values.append(price.split()[0])
    for element in stock_name:
        ticker.append(element.text)
    stock_float = []
    processed_data = []
    for i in values:
        if i.strip() == '-':
            processed_data.append('0')
        else:
            processed_data.append(i.strip())
    for i in processed_data:
        integer = float(i)
        stock_float.append(integer)
    rows1 = []
    current_row1 = []       
    for entry in stock_float:
        current_row1.append(entry)
        if len(current_row1) == 5:
            rows1.append(current_row1)
            current_row1 = []
    if current_row1:
        rows1.append(current_row1)
    matrix = np.array(rows1)
    
    stock_data = []
    for symbol, row in zip(ticker, matrix):
        stock_data.append({
            'stockName': symbol,
            'return1Y': f'{row[0]} %',
            'return9M': f'{row[1]} %',
            'return6M': f'{row[2]} %',
            'return3M': f'{row[3]} %',
            'stockPrice': row[4]
        })
    
    return stock_data  


@app.route('/getsector/<sector>')
def getsector(sector):
    urls = sectors_url[sector]
    if isinstance(urls, str):  
        data = stock_data_to_dict(urls)
    elif isinstance(urls, list):  
        all_data = []
        for url in urls:
            all_data.extend(stock_data_to_dict(url))
        data = all_data
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)