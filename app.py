from flask import Flask, request, render_template

app = Flask(__name__)

# Fixed number for testing
secret_number = 10

@app.route('/', methods=['GET', 'POST'])
def guess_number():
    message = ""
    if request.method == 'POST':
        try:
            user_guess = int(request.form['guess'])
            if user_guess < secret_number:
                message = "Too low! Try again."
            elif user_guess > secret_number:
                message = "Too high! Try again."
            else:
                message = "Congratulations! You guessed the correct number."
        except ValueError:
            message = "Please enter a valid number."
    
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
