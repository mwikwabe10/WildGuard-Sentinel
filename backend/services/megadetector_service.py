from datetime import datetime
from pathlib import Path


def detect_objects(image_path):

    """
    Wildlife detection engine.
    Currently uses simulation mode.
    Replace this function with MegaDetector inference.
    """

    image_name = Path(image_path).name

    # Temporary AI simulation
    detections = [
        {
            "filename": image_name,
            "category": "elephant",
            "confidence": 0.94,
            "latitude": -1.4061,
            "longitude": 35.1439,
            "timestamp": datetime.utcnow().isoformat()
        }
    ]

    return detections