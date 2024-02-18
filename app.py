from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hotels/')
def display_hotels():
  return render_template('template.html')

if __name__ == '__main__':
  app.run()