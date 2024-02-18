from flask import Flask, render_template

app = Flask(__name__)

hotel_ratings = [
    {'ID': 1,'name': 'MapleTree', 'rating': 4},
    {'ID': 2,'name': 'Regents', 'rating': 5},
    {'ID': 3,'name': 'DropInn', 'rating': 3},
]

@app.route('/hotels/')
def display_hotels():
  return render_template('template.html', hotel_ratings=hotel_ratings)

@app.route('/')
def home():
  message = 'Go To The Hotel List'
  return render_template('home.html', msg=message)

if __name__ == '__main__':
  app.run(debug=True)