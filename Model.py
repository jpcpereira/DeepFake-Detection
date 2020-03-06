import numpy as np
import tensorflow 
#import cv2 
import os,sys
import matplotlib.pyplot as plt

import tensorflow
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
import cv2

def classify_video(video_dir, CNN_model, LSTMmodel):
    x = []
    for image_fol in os.listdir(video_dir):
        image = plt.imread(video_dir + image_fol)
        image = cv2.resize(image , (224,224))
        x.append(image)

    x = np.array(x)

    print("input shape", x.shape)
    # Extract frame features using CNN
    x_features = CNN_model.predict(x)
    x_features = x_features.reshape(x_features.shape[0],
                     x_features.shape[1] * x_features.shape[2] * x_features.shape[3])

    print("x_features shape", x_features.shape)

    x_features = np.expand_dims(x_features, axis=0)

    # Feed to RNN
    prediction = LSTMmodel.predict(x_features)

    print("Classification result: ", np.argmax(prediction))
    return prediction


video_dir = "C:\\Users\\Administrator\\Desktop\\hackathon\\"
CNN_model = tensorflow.keras.models.load_model('CNN_model.h5')
LSTM_model = tensorflow.keras.models.load_model("LSTM_model.h5")
classify_video(video_dir, CNN_model, LSTM_model)