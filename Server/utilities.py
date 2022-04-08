# import modules
import json
import pickle
import numpy as np



'''*****************************************************************************'''
'''ROUTINES'''

# function to load information from artifacts
def load_saved_artifacts():
    print('loading saved artifacts...', '\n')
    global data_columns

    # read columns file
    with open('./Artifacts/columns.json', 'r') as f:
        # save column names to varible
        data_columns = json.load(f)['data_columns']

    # read model file >> read in binary
    with open('./Artifacts/poland_house_prices_model.pickle', 'rb') as f:
        # save pickle file to variable
        model = pickle.load(f)

    print(f'Data Columns: {data_columns}', '\n')
    print(f'Model: {model}', '\n')
    print('loading saved artifacts...done!!!', '\n')

    return data_columns, model


# function to predict a house price
def predict_price(city, floor, rooms, sq, year):
    # standarize features to be fed into the model
    city_st = 1 if city == ' Warsaw' else 0
    year_st = 1 if year >= 1970 else 0
    sq_st = (sq - 25.01) / (150 - 25.01)

    # features np array
    features = np.array([city_st, floor, rooms, sq_st, year_st])

    # call load_saved_artifacts
    data_columns, model = load_saved_artifacts()

    print('********************************************************************************')

    # intercept
    b0 = model['intercept'][0]
    # parameters
    b1, b2, b3, b4, b5 = model['params'][0], model['params'][1], model['params'][2], model['params'][3], model['params'][4]

    # predict price >> b0 + b1*x1 + b2*x2 + b3*x3 + b4*x4 + b5*x5
    predicted_price = b0 + b1*features[0] + b2*features[1] + b3*features[2] + b4*features[3] + b5*features[4]
    predicted_price *= 100000

    print(f'Estimated House Price for City:{city}, Floors:{floor}, Rooms:{rooms}, Sq:{sq}, Year:{year}....')
    return round(predicted_price,2)



'''*****************************************************************************'''
'''MAIN'''

if __name__ == '__main__':
    # load_saved_artifacts()
    # call predict_price function
    print(predict_price('Poznan', 3, 2, 42.39, 1985))
