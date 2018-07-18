import flask
import os
import requests
import json
import pandas as pd

APP_HOST = os.getenviron.get("APP_HOST", "0.0.0.0")
APP_PORT = int(os.getenviron.get("APP_PORT", 80))

from flask import Flask, request, abort, render_template

app = Flask(__name__)
url_tmpl = "https://s.2.taobao.com/list/waterfall/waterfall.htm?wp={pagenumber}&callback={format}&stype=1&st_trust=1&q={keywords}&ist=1"


@app.route('/')
def index():
    return 'Hello, this is Rui'

@app.route('/')
def get_lowest_price():
    keywords = request.args.get('keywords')
    url = url_tmpl.format(pagenumber=1, format="jsonnp", keywords=keywords)
    res = requests.get(url)
    return res.text


