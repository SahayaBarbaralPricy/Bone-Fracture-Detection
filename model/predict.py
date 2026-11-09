import os
import numpy as np
from tensorflow.keras.models import load_model

from model.preprocess import preprocess_image


# ==========================================
# PROJECT BASE DIRECTORY
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


# ==========================================
# LOAD AI MODEL
# ==========================================

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "bone_fracture_model.h5"
)


print("\n========================================")
print("LOADING BONE FRACTURE MODEL")
print("========================================")

model = load_model(MODEL_PATH)

print("Bone Fracture Model Loaded Successfully")
print("Model path:", MODEL_PATH)


# ==========================================
# PREDICTION FUNCTION
# ==========================================

def predict_fracture(image_path):
    """
    Predict whether the uploaded X-ray
    contains a fracture or is normal.

    Model class mapping:
        0 = fracture
        1 = normal
    """

    try:

        # ======================================
        # PREPROCESS IMAGE
        # ======================================

        image = preprocess_image(image_path)

        if image is None:

            return "Error", 0


        # ======================================
        # AI PREDICTION
        # ======================================

        prediction = model.predict(
            image,
            verbose=0
        )


        probability = float(
            prediction[0][0]
        )


        # ======================================
        # CLASSIFICATION
        # ======================================
        #
        # The trained model uses:
        #
        # 0 = fracture
        # 1 = normal
        #
        # Sigmoid output represents the probability
        # of class 1 (normal).
        #
        # Therefore:
        #
        # probability >= 0.5 → Normal
        # probability < 0.5  → Fracture
        # ======================================

        if probability >= 0.5:

            result = "Normal"

            confidence = probability * 100

        else:

            result = "Fracture"

            confidence = (1 - probability) * 100


        # ======================================
        # RETURN RESULT
        # ======================================

        return result, confidence


    except Exception as e:

        print(
            "Prediction Error:",
            e
        )

        return "Error", 0
