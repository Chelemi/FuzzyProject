from clothes import *

weights = {
    'Days_worn': 1,
    'Days_left_out': 1,
    'Activity': 2,
    'Stress': 1,
    'Temperature': 1,
    'Hours': 1
}

def calculate_score(input):
    total_score = weights['Days_worn'] * input['Days_worn'] + weights['Days_left_out'] * input['Days_left_out'] + weights['Activity'] * input['Activity'] + weights['Stress'] * input['Stress'] + weights['Temperature'] * input['Temperature'] + weights['Hours'] * input['Hours']

    if total_score <= 10:
        cleanliness = "clean"
    elif total_score <= 20:
        cleanliness = "somewhat clean"
    elif total_score <= 30:
        cleanliness = "somewhat dirty"
    else:
        cleanliness = "dirty"

    return total_score, cleanliness

def run_test():
    correct_counter = 0
    for index, row in CLOTHES.iterrows():
        print(f"\nCloth {index+1}:")

        score, cleanliness = calculate_score(row)
        print(f"Output: {score}")
        print(f"Final output: {cleanliness}")

        if cleanliness == row['Output']:
            correct_counter += 1

    return correct_counter, CLOTHES.shape[0]
