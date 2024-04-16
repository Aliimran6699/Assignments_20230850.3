def calculate_average_scores(**kwargs):
    total_score = 0
    num_subjects = 0

    # Iterate through each subject and its score
    for subject, score in kwargs.items():
        total_score += score
        num_subjects += 1

    # Calculate the average score
    if num_subjects > 0:
        average_score = total_score / num_subjects
        print("Average score:", average_score)
    else:
        print("No scores provided.")


# Passing the scores using **kwargs
calculate_average_scores(IT5014=60, IT7809=80, IT6798=50, IT5048=70)
