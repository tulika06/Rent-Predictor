import pandas as pd
from flask import Flask, render_template, request
import pickle


#from paramiko import BadHostKeyException

app = Flask(__name__)
data = pd.read_csv('Cleaned_data.csv')
pipe = pickle.load(open("RidgeModel.pkl", 'rb'))

@app.route('/')
def index():
    locations = sorted(data['Locations'].unique())
    #statuses = sorted(data['Status'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    locations = request.form.get('location')
    bhk = request.form.get('bhk')
    bathrooms = request.form.get('bath')
    sqft = request.form.get('total_sqft')
    #status = request.form.get('status')
    print(locations, bhk, bathrooms, sqft)
    input = pd.DataFrame([[locations, bhk, bathrooms, sqft]], columns=['Locations', 'Square feet area', 'Bathrooms', 'BHK'])
    prediction = pipe.predict(input)[0]
    return str(prediction)

if __name__ == "__main__":
    app.run(debug=True,port=5001)
