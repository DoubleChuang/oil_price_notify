# -*- coding: utf-8 -*-
import re

import requests
from lxml import etree
from decouple import config
import schedule


LINE_NOTIFY_TOKEN = config('LINE_NOTIFY_TOKEN', cast=str,  default='') 
LINE_NOTIFY_URL = config('LINE_NOTIFY_URL', cast=str,  default="https://notify-api.line.me/api/notify")
ALERT_PRICE = config('ALERT_PRICE', cast=int,  default=0)

def get_xpath(html, xpath):
    value = html.xpath(xpath)

    if not value:
        print("找不到匹配的值")

    return parser_price(value)

def parser_price(data):
    for item in data:
        # 使用正則表達式模式匹配數字
        match = re.search(r'\d+(\.\d+)?', item)

        if match:
            # 提取匹配的數字部分
            number = match.group()
            return float(number)

def send_line_notify(message, token):
    url = LINE_NOTIFY_URL
    headers = {
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "message": message
    }
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        print(f"Line Notify通知已發送: {message}")
    else:
        print("無法發送Line Notify通知")

def main():
    response = requests.get("https://gas.goodlife.tw/")
    if response.status_code == 200:
        # 使用lxml解析HTML
        html = etree.HTML(response.content)

        # 使用XPath查找特定元素
        value = get_xpath(html, '//*[@id="rate"]/ul/li[8]/text()')
        message = f"布蘭特原油價格: {value}，注意通膨"
        if value > ALERT_PRICE: send_line_notify(message, LINE_NOTIFY_TOKEN)

        value = get_xpath(html, '//*[@id="rate"]/ul/li[9]/text()')
        message = f"杜拜原油價格: {value}，注意通膨"
        if value > ALERT_PRICE: send_line_notify(message, LINE_NOTIFY_TOKEN)

        value = get_xpath(html, '//*[@id="rate"]/ul/li[10]/text()')
        message = f"西德州原油價格: {value}，注意通膨"
        if value > ALERT_PRICE: send_line_notify(message, LINE_NOTIFY_TOKEN)
    else:
        print("無法發送請求")
    

if __name__ == '__main__':
  main()