import pickle
import pandas as pd
import numpy as np
import sklearn
import catboost

model = pickle.load(open('model_cbr.pkl', 'rb'))