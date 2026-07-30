def create_alert(category, confidence):

    # Low confidence detections
    if confidence < 0.50:
        return {
            "alert_level": "LOW",
            "message": f"Low confidence {category} observation recorded"
        }

    # Human intrusion / possible poaching risk
    if category == "human":
        return {
            "alert_level": "CRITICAL",
            "message": "Human detected inside protected area - possible intrusion risk"
        }

    # Vehicle monitoring
    elif category == "vehicle":
        return {
            "alert_level": "HIGH",
            "message": "Vehicle detected in protected area - verify authorization"
        }

    # Large mammals
    elif category == "elephant":
        return {
            "alert_level": "MEDIUM",
            "message": "Elephant detected - monitor movement and human-wildlife interaction risk"
        }

    elif category == "lion":
        return {
            "alert_level": "HIGH",
            "message": "Lion detected near settlement - potential human-wildlife conflict risk"
        }

    elif category == "buffalo":
        return {
            "alert_level": "HIGH",
            "message": "Buffalo detected - monitor for community safety risk"
        }

    elif category == "giraffe":
        return {
            "alert_level": "LOW",
            "message": "Giraffe observation recorded"
        }

    # Generic wildlife observation
    else:
        return {
            "alert_level": "LOW",
            "message": f"{category} wildlife observation recorded"
        }