from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main_2.html", message = "Python page", contacts = ['c1','c2','c3','c4'])

@app.route('/calculate', methods=['POST'])
def calculate():
    ans = []
    val_1 = int(request.form['num1'])
    val_2 = int(request.form['num2'])
    x = val_1 + val_2
    ans.append(val_1)
    ans.append(val_2)
    ans.append(x)
    return render_template('main_2.html', answer=ans)

@app.route('/display', methods=['POST'])
def display():

    predict_array = []

    val_1 = int(request.form['model'])
    val_2 = int(request.form['fuel'])
    val_3 = int(request.form['kms'])
    val_4 = int(request.form['city'])

    model_car = val_1
    km = val_3
    fuel = val_2
    city = val_4

    if fuel==1:
        fuel='Diesel'
    elif fuel==2:
        fuel = 'Petrol'
    else:
        fuel = 'Petrol+CNG'

    predict_array.append(val_1)
    predict_array.append(val_2)
    predict_array.append(val_3)
    predict_array.append(val_4)

    model = pickle.load(open('gbr_car.sav','rb'))
    ans = model.predict([predict_array])
    ans = int(ans)

    return render_template('main_2.html', answer=ans, model=model_car, km=km, city=city, fuel=fuel)



if __name__ == "__main__":
    app.run()