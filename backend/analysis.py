from transformers import pipeline



LABELS = [
    "healthy",
    "confident",
    "dominant",
    "cringe",
    "dismissive",
    "toxic"
]

GREEN_LABELS = ["healthy", "confident"]
YELLOW_LABELS = ["dominant", "cringe"]
RED_LABELS = ["dismissive", "toxic"]

STRONG_THRESHOLD = 0.6
MEDIUM_THRESHOLD = 0.3




EXPLANATION_KEYWORDS = {
    "dismissive": [
        "don't waste my time",
        "dont waste my time",
        "serious people only",
        "don't bother",
        "swipe left"
    ],
    "toxic": [
        "hate",
        "weak people",
        "fake",
        "annoying",
        "stupid"
    ],
    "dominant": [
        "i like to lead",
        "alpha",
        "take charge",
        "expect effort"
    ],
    "cringe": [
        "sigma",
        "grind",
        "hustle",
        "gym rat"
    ],
    "confident": [
        "i know what i want",
        "ambitious",
        "focused on my goals"
    ],
    "healthy": [
        "kindness",
        "honesty",
        "communication",
        "meaningful"
    ]
}


classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)


def extract_explanations(bio_text, active_labels):
    bio_lower = bio_text.lower()
    explanations = {}

    for label in active_labels:
        matches = [
            phrase for phrase in EXPLANATION_KEYWORDS.get(label, [])
            if phrase in bio_lower
        ]
        if matches:
            explanations[label] = matches

    return explanations


def analyze_bio(bio_text: str):
    output = classifier(bio_text, LABELS)

    labels = output["labels"]
    scores = output["scores"]
    score_map = dict(zip(labels, scores))

    green_flags = []
    yellow_flags = []
    red_flags = []

    for label, score in score_map.items():
        if label in RED_LABELS and score >= STRONG_THRESHOLD:
            red_flags.append(label)

        elif label in YELLOW_LABELS and score >= MEDIUM_THRESHOLD:
            yellow_flags.append(label)
        
        elif label in RED_LABELS and score >= MEDIUM_THRESHOLD:
            yellow_flags.append(label)


        elif label in GREEN_LABELS and score >= MEDIUM_THRESHOLD:
            green_flags.append(label)

    active_labels = green_flags + yellow_flags + red_flags
    explanations = extract_explanations(bio_text, active_labels)

    note = None
    if not active_labels:
        note = "No strong positive or negative signals detected."

    return {
        "bio": bio_text,
        "green_flags": green_flags,
        "yellow_flags": yellow_flags,
        "red_flags": red_flags,
        "scores": score_map,
        "explanations": explanations,
        "note": note
    }
