from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        text_input = request.form.get('text_input')
        message = f"You entered: {text_input}"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)