from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def birthday():
    return render_template('birthday.html')

if __name__ == '__main__':
    app.run(debug=True)

