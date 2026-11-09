import cv2
import numpy as np


# ==========================================
# IMAGE PREPROCESSING FUNCTION
# ==========================================

def preprocess_image(image_path):
    """
    Preprocess the uploaded X-ray image
    before sending it to the AI model.

    The trained model expects:
        160 x 160 x 3

    EfficientNetB0 handles its own input
    preprocessing.
    """

    try:

        # ======================================
        # READ IMAGE
        # ======================================

        image = cv2.imread(image_path)

        if image is None:

            raise ValueError(
                "Unable to load image."
            )


        # ======================================
        # CONVERT BGR TO RGB
        # ======================================

        image = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2RGB
        )


        # ======================================
        # RESIZE IMAGE
        # ======================================

        image = cv2.resize(
            image,
            (160, 160)
        )


        # ======================================
        # CONVERT TO FLOAT32
        # ======================================

        image = image.astype(
            "float32"
        )


        # ======================================
        # EXPAND DIMENSIONS
        # ======================================

        image = np.expand_dims(
            image,
            axis=0
        )


        # ======================================
        # RETURN IMAGE
        # ======================================

        return image


    except Exception as e:

        print(
            "Preprocessing Error:",
            e
        )

        return None
