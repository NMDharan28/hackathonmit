from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import joblib
from sklearn.impute import SimpleImputer

# Load the trained models
solar_model = joblib.load('trained_model.pkl')  # Load your trained solar energy model here
wind_model = joblib.load('wind_model.pkl')    # Load your trained wind energy model here

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/solar',methods=['GET'])
def solarpredict():
    return render_template('solar.html')

@app.route('/wind',methods=['GET'])
def windpredict():
    return render_template('wind.html')

@app.route('/solar/predict', methods=['POST'])
def predict1():
    cloud_coverage = float(request.form['cloud_coverage'])
    visibility = float(request.form['visibility'])
    temperature = float(request.form['temperature'])
    dew_point = float(request.form['dew_point'])
    relative_humidity = float(request.form['relative_humidity'])
    wind_speed = float(request.form['wind_speed'])
    station_pressure = float(request.form['station_pressure'])
    prediction=solarresult(cloud_coverage,visibility,temperature, dew_point, relative_humidity, wind_speed, station_pressure)
    return render_template('solar_result.html',prediction= prediction)

@app.route('/wind/predict', methods=['POST'])
def predict2():
    pressure = float(request.form['pressure'])
    wind_direction = float(request.form['wind_direction'])
    wind_speed = float(request.form['wind_speed'])
    prediction = windresult(pressure, wind_direction, wind_speed)
    return render_template('wind_result.html',prediction=prediction)




#@app.route('/predict', methods=['POST'])
#def predict():
 #   energy_type = request.form['energy_type']
  #  if energy_type == 'solar':
#   return redirect(url_for('predict_solar'))
 #   elif energy_type == 'wind':
  #      return redirect(url_for('predict_wind')


#@app.route('/predict/solar/result', methods=['POST'])
#def predict_solar_result():
    # Get input data from the form
    # Assume similar input fields as in the previous code for solar prediction
    # ...

    # Make prediction using the solar model
    # ...

    #cloud_coverage = float(request.form['cloud_coverage'])
    #visibility = float(request.form['visibility'])
    #temperature = float(request.form['temperature'])
    #dew_point = float(request.form['dew_point'])
    #relative_humidity = float(request.form['relative_humidity'])
    #wind_speed = float(request.form['wind_speed'])
    #station_pressure = float(request.form['station_pressure'])
    
    # Impute missing values
    #imputer = SimpleImputer(strategy='mean')
    #X_input = [[cloud_coverage, visibility, temperature, dew_point, relative_humidity, wind_speed, station_pressure]]
    #X_input_imputed = imputer.fit_transform(X_input)

    # Make prediction
    #prediction = solar_model.predict(X_input_imputed)[0]

    #return render_template('solar_result.html', prediction=prediction)
def solarresult(cloud_coverage,visibility,temperature, dew_point, relative_humidity, wind_speed, station_pressure):
    imputer = SimpleImputer(strategy='mean')
    X_input = [[cloud_coverage, visibility, temperature, dew_point, relative_humidity, wind_speed, station_pressure]]
    X_input_imputed = imputer.fit_transform(X_input)

    # Make prediction
    prediction = solar_model.predict(X_input_imputed)[0]
    return prediction


#@app.route('/predict/wind/result', methods=['POST'])
#def predict_wind_result():
    # Get input data from the form
    # Assume similar input fields as in the previous code for wind prediction
    # ...

    # Make prediction using the wind model
    # ...
 #   if request.method == 'POST':
  #      # Get the input values from the form
   #     pressure = float(request.form['pressure'])
    #    wind_direction = float(request.form['wind_direction'])
     #   wind_speed = float(request.form['wind_speed'])

        # Make a prediction using the trained model
      #  prediction = wind_model.predict([[pressure, wind_direction, wind_speed]])
        #print(request.form)


    #return render_template('wind_result.html', prediction=prediction)
def windresult(pressure,wind_direction,wind_speed):
    prediction = wind_model.predict([[pressure, wind_direction, wind_speed]])
    return prediction


    

if __name__ == '__main__':
    app.run(debug=True)
