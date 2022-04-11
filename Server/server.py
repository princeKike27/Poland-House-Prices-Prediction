# import modules
from flask import Flask, request, jsonify
import utilities

'''FLASK
Light web framework that allows you to build web applications
'''

app = Flask(__name__)


'''*****************************************************************************'''
'''ENDPOINTS & ROUTINES
HTTP >> request-response protocol to communicate between a client and a server
GET >> request data from a specified source
POST >> data sent to the server to create/ update a resource
'''
# expose http endpoint >> server route /function name
@app.route('/hello')
def hello():
    return 'Hi :)'


# Post request to predicted_price
@app.route('/predict_house_price', methods=['POST'])
def predict_house_price():
    # request to webpage to get variables from the form
    city = request.form['city']
    floor = int(request.form['floor'])
    rooms = int(request.form['rooms'])
    sq = float(request.form['sq'])
    year = int(request.form['year'])

    # call predict_price function from utilities to get predicted price
    response = jsonify({
        'predict_price': utilities.predict_price(city, floor, rooms, sq, year)
    })

    # allow response to be shared with requesting code
    # * requesting code from any origin can access the resource
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__ == "__main__":
    print('Starting Python Flask Server for Poland House Prices Prediction...', '\n')
    utilities.load_saved_artifacts()
    app.run()
