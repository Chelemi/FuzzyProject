inputs = {
    'days_worn': 2,
    'days_left_out': 3,
    'activity': 4,
    'stress': 2,
    'temperature': 3,
    'hours': 4
}

weights = {
    'days_worn': 1,
    'days_left_out': 1,
    'activity': 2,
    'stress': 1,
    'temperature': 1,
    'hours': 1
}

total_score = weights['days_worn'] * inputs['days_worn'] + weights['days_left_out'] * inputs['days_left_out'] + weights['activity'] * inputs['activity'] + weights['stress'] * inputs['stress'] + weights['temperature'] * inputs['temperature'] + weights['hours'] * inputs['hours']

if total_score <= 10:
    cleanliness = "Clean"
elif total_score <= 20:
    cleanliness = "Somewhat dirty"
elif total_score <= 25:
    cleanliness = "Dirty"
else:
    cleanliness = "Very dirty"

print("Cleanliness classification:", cleanliness)