from flask import Flask, render_template, request, jsonify, redirect, url_for
# from flask_cors import CORS
from chat1 import receive

app = Flask(__name__)
# CORS(app)

@app.get("/")
def index_get():
    return render_template("index.html")

@app.get("/index.html")
def get_index():
    return render_template("index.html")

@app.get("/clinics.html")
def get_clinics():
    return render_template("clinics.html")

@app.get("/about.html")
def get_about():
    return render_template("about.html")

@app.post("/predict")
def predict():
    # print(age, sex)
    text = request.get_json().get('message')
    if "hello" in text or text=='hi':
        # print(text)
        message1 = {"answer": "Hello! What is your age and gender! :)"}
        return jsonify(message1)
    elif "pain" in text:
        symptom = text
        age, sex = 30, "male"
        response = receive(text, age, sex, symptom)
        message3 = {"answer": response}
        return jsonify(message3)
    elif "ache" in text:
        symptom = text
        age, sex = 30, "male"
        response = receive(text, age, sex, symptom)
        message3 = {"answer": response}
        return jsonify(message3)
    elif "fever" in text:
        symptom = text
        age, sex = 30, "male"
        response = receive(text, age, sex, symptom)
        message3 = {"answer": response}
        return jsonify(message3)
    elif "cold" in text:
        symptom = text
        age, sex = 30, "male"
        response = receive(text, age, sex, symptom)
        message3 = {"answer": response}
        return jsonify(message3)
    else: 
        age, sex, symptom = None, None, None
        response = receive(text, age, sex, symptom)
        if response[0]=="What are your conditions?":
            age, sex = response[1]
            # print(age, sex)
        message2 = {"answer": response[0]}
        # return redirect(url_for('predict2'))
        return jsonify(message2)

# @app.post("/predict2")
# def predict2():
#     text = request.get_json().get('message')
#     response = receive(text)
#     message = {"answer": response}
#     return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
    