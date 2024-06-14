from flask import Flask, render_template, jsonify, request
import pickle

app = Flask(__name__)

# Load the model
with open('percentage.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        hours = float(request.form['hours'])
        prediction = loaded_model.predict([[hours]])[0]
        return render_template('index.html', prediction=prediction)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)