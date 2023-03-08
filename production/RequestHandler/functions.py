import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
from keras.models import load_model

def linear_regression(data):
    """Processes prediction calls to linear regression

    Args:
        data (int): value to predict

    Returns:
        bool, ndarray: predicted value
    """
    # locate model artifact 
    with open("./artifacts/linear_model.pkl", "rb") as model_file:
        # load model artifact 
        linear_model = pickle.load(model_file)
    
    # make predictions
    data = linear_model.predict(np.array(data).reshape(1, -1))
    
    # return status and predicted data
    return True, data

def support_vector_machine(data):
    """Processes prediction calls to support vector regression

    Args:
        data (int): value to predict

    Returns:
        bool, ndarray: predicted value
    """
    # locate model artifact 
    with open("./artifacts/support_model.pkl", "rb") as model_file:
        # load model artifact 
        svm_model = pickle.load(model_file)

    # make predictions
    data = svm_model.predict(np.array(data).reshape(1, -1))

    # return status and predicted data
    return True, data

def artificial_neural_network(data):
    """Processes prediction calls to artificial neural network

    Args:
        data (int): value to predict

    Returns:
        bool, ndarray: predicted value
    """
    # locate model artifact 
    ann_model = load_model("./artifacts/ann_model.h5")
    
    # scale the input data and make predictions
    data = ann_model.predict(StandardScaler().fit_transform(np.array(data).reshape(1, -1)))
    
    # return data and predicted data
    return True, data[0]
    