import googlesearch
import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from threading import Thread
import json

app = Flask('')
app.config['JSON_SORT_KEYS'] = False
@app.route('/')	
def home():
	return  "I'm alive"

@app.route('/api/<string:s>', methods=['GET'])
def prayer(s):
  query = str(s + " prayer time site:muslimpro.com")
  data = {}
  mencari = googlesearch.search(query)
  try :
    url = str(mencari[0])
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    city = soup.find("h2", attrs ={"class": "place"})
    dates = soup.find("h2", attrs ={"class": "date"})
    month = soup.find("span", attrs ={"class": "display-month"})
    data["city"] = city.get_text()
    tanggal = dates.get_text().split()
    data["date"] = tanggal[0] + " " + month.get_text()
    data["prayers"] = {}
    waktu = soup.find_all("span", attrs ={"class": "waktu-solat"})
    jam = soup.find_all("span", attrs ={"class": "jam-solat"})
    for x,y in zip(waktu,jam):
      data["prayers"][x.get_text()] = y.get_text()
  except :
    data["Error"] = "Result Not Found"
  return jsonify(data)

def run():
	app.run(host='0.0.0.0',port=7000)

t = Thread(target=run)
t.start()