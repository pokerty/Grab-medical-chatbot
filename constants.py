"""Constants."""

MIN_AGE = 12
MAX_AGE = 130

SEX_NORM = {
    "male": "male",
    "m": "male",
    "man": "male",
    "boy": "male",
    "female": "female",
    "f": "female",
    "woman": "female",
    "girl": "female",
}

ANSWER_NORM = {
    "yes": "present",
    "y": "present",
    "yup": "present",
    "definitely": "present",
    "sure": "present",
    "surely": "present",
    "present": "present",
    "no": "absent",
    "n": "absent",
    "nah": "absent",
    "nope": "absent",
    "absent": "absent",
    "?": "unknown",
    "skip": "unknown",
    "unknown": "unknown",
    "dont know": "unknown",
    "don't know": "unknown",
}