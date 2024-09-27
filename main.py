def main():
    # Define the number of students
    num_students = int(input("Enter the number of students: "))
    
    # Initialize lists for names and scores
    names = []
    scores = []
    
    # Input names and scores
    for _ in range(num_students):
        name = input("Enter student name: ")
        score = float(input(f"Enter score for {name}: "))
        names.append(name)
        scores.append(score)

    # Calculate average score
    average_score = sum(scores) / num_students
    print(f"\nAverage Score: {average_score:.2f}")

    # Determine who passed (assuming passing score is 50)
    passing_score = 50
    print("\nStudents who passed:")
    for name, score in zip(names, scores):
        if score >= passing_score:
            print(f"{name}: {score}")

if __name__ == "__main__":
    main()
