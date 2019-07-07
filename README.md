# Sentiment Analysis API

Deploy sentiment analysis model as an API

# Requirements

- flask_restful
- flask
- pandas
- numpy
- sklearn

# Usage

`curl -X GET http://127.0.0.1:5000/api/v1/predict/ -d query='Not able to open the app in my phone some trust issue is coming'`

output:

`{
    "prediction": "Negative",
    "confidence": 0.111
}
`
