import numpy as np 
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing import image # type: ignore
import os


class DogCat:
    def __init__(self,filename):
        self.filename = filename
        
    def predictiondogcat(self):
        
        model = load_model(os.path.join("artifacts","training","model.h5"))
        
        imagename = self.filename
        
        test_image = image.load_img(imagename,target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image,axis = 0)   
        result = np.argmax(model.predict(test_image),axis = 1)
        print(result)
        
        
        if result[0] == 1:
            prediction = 'This is a Dog Image'
            return prediction
        
        else:
            prediction = 'This is a Cat Image'
            return prediction