from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/leaguestandings')
def premier():
    url = "https://premier-league-standings1.p.rapidapi.com/"

    headers = {
	"X-RapidAPI-Key": "16a307a9bemsh20ca6f2e4755c2ap1a7065jsn62bcdfdbfb4d",
	"X-RapidAPI-Host": "premier-league-standings1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    standing = response.json()
        
    return render_template('premier.html' , data = standing)

@app.route('/player')
def method_name():
    url = "https://premier-league-players1.p.rapidapi.com/players"

    headers = {
        "X-RapidAPI-Key": "16a307a9bemsh20ca6f2e4755c2ap1a7065jsn62bcdfdbfb4d",
        "X-RapidAPI-Host": "premier-league-players1.p.rapidapi.com"
    }
    

    response = requests.get(url, headers=headers)
    player = response.json()

    return render_template('player.html', data = player)

if __name__ == '__main__':
    app.run(debug=True)