from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np

from model import NLPModel
app = Flask(__name__)
api = Api(app)
# create new model object
model = NLPModel()
# load trained classifier
clf_path = 'lib/models/SentimentClassifier.pkl'
with open(clf_path, 'rb') as f:
    model.clf = pickle.load(f)
# load trained vectorizer
vec_path = 'lib/models/TFIDFVectorizer.pkl'
with open(vec_path, 'rb') as f:
    model.vectorizer = pickle.load(f)

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('query')

