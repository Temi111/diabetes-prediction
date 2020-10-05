import json
import pickle

#'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']

model = pickle.load(open='./Random_Forest.pkl','rb')



def predict(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }
    params = event['queryStringParameters']

    Pregnancies = float(params['Pregnancies'])
    Glucose = float(params['Glucose'])
    BP = float(params['BP'])
    SkinThickness = float(params['SkinThickness'])
    Insulin = float(params['Insulin'])
    BMI = float(params['BMI'])
    DiabetesPedigreeFunction = float(params['DiabetesPedigreeFunction'])
    Age = float(params['Age'])

    input_data = [['Pregnancies', 'Glucose', 'BP', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age']]

    pred = model.predict(input_data)[0]

    body['prediction'] = pred



    response = {
        "statusCode": 200,
        "body": json.dumps(body)
        "header":{
            'Access-Control-Allow_Origin':'*'
        }
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
