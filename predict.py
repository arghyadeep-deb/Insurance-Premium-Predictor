import pickle
import pandas as pd

#importing the model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

MODEL_VERSION = "1.0.0"

class_labels = model.classes_.tolist()

def predict_output(user_input: dict):
    df = pd.DataFrame([user_input])
    
    #predict the class
    prediction = model.predict(df)[0]
    
    #get probabilities for each class
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)
    
    #create mapping: {class_name: probability}
    class_probs = dict(zip(class_labels, map(lambda x: round(x, 4), probabilities)))
    
    return{
        "predicted_class": prediction,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs,
        "model_version": MODEL_VERSION
    }