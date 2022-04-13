# import modules
import numpy as np
import pickle
from flask import Flask, request, jsonify, render_template, url_for

'''FLASK
Light web framework that allows you to build web applications
'''
# initialize Flask
app = Flask(__name__)

# read and model file in binary >> rb
with open('poland_house_prices_model.pickle', 'rb') as f:
    model = pickle.load(f)

'''*****************************************************************************'''
''' ENDPOINTS & ROUTINES
HTTP >> request-response protocol to connect between a client and a server
GET  >> request data from a specified source
POST >> data sent to the server to create/update a resurce
'''

# expose http endpoint >> @server_route == function name
'''HOME PAGE'''
@app.route('/')
def home():
    # render html page
    return render_template('home.html')

'''PREDICT PRICE'''
@app.route('/predict',methods = ['POST'])
def predict():
    # save values from form
    city_f = request.form.get('city_form')
    floors_f = request.form.get('floors_form')
    rooms_f = request.form.get('rooms_form')
    sq_f = request.form.get('sq_form')
    year_f = request.form.get('year_form')

    # standarize values to be fed into the Model
    city = 1 if city_f == 'Warsaw' else 0
    floors = float(floors_f)
    rooms = float(rooms_f)
    sq = (float(sq_f) - 25.01) / (150 - 25.01)
    year = 1 if int(year_f) >= 1970 else 0

    # save intercept and parameters from model
    b_0 = model['intercept'][0]
    b_1 = model['params'][0]
    b_2 = model['params'][1]
    b_3 = model['params'][2]
    b_4 = model['params'][3]
    b_5 = model['params'][4]

    # calculate predictive price
    predictive_price = b_0 + b_1*city + b_2*floors + b_3*rooms + b_4*sq + b_5*year
    predictive_price *= 100000

    print('\n')
    print(f'City: {city_f}, # Floors: {floors_f}, # Rooms: {rooms_f}, Area m^2: {sq_f}, Year Built: {year_f}')
    print(f'Predicted Price: €{predictive_price:.2f}', '\n')
    
    return render_template('home.html', prediction_text=f'€{predictive_price:.2f}')


if __name__ == '__main__':
    print('*' * 100)
    print('Starting Python Flask Server for Poland House Prices Prediction...', '\n')
    print(f'Model: {model}', '\n')
    app.run(debug=True)
