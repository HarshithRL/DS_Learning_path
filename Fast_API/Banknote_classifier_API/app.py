# 1. Library imports
import uvicorn
from fastapi import FastAPI
from modeldata import BankNote
import pickle

# 2. Create the app object
bank_note_api = FastAPI()
pickle_in = open(r"C:\Users\HarshithR\conda_poj\BankNote_classifier.pkl","rb")
classifier=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@bank_note_api.get('/')
def index():
    return {'message': 'Welcome to bank Note Prediction'}

@bank_note_api.post('/predict')
def predict_banknote(data:BankNote):
    data = data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    if(prediction[0]>0.5):
        prediction="Fake note"
    else:
        prediction="Its a Bank note"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(bank_note_api, host='127.0.0.1', port=8000)
 #uvicorn app:bank_note_api --reload