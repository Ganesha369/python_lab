# Sample Data: A list of student dictionaries
students = [
    {"name": "Alice", "scores": [85, 92, 88]},
    {"name": "Bob", "scores": [70, 65, 72]},
    {"name": "Charlie", "scores": [95, 100, 98]},
    {"name": "Diana", "scores": [50, 60, 55]}
]

def get_letter_grade(average):
    """Returns a letter grade based on the average score."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def generate_report(student_list):
    print("--- STUDENT PERFORMANCE REPORT ---")
    print(f"{'Name':<10} | {'Average':<8} | {'Grade':<5}")
    print("-" * 30)

    for student in student_list:
        name = student["name"]
        scores = student["scores"]
        
        # Calculate average using built-in functions sum() and len()
        avg_score = sum(scores) / len(scores)
        grade = get_letter_grade(avg_score)
        
        # Print formatted row
        print(f"{name:<10} | {avg_score:>8.2f} | {grade:<5}")

# Execute the project
if __name__ == "__main__":
    generate_report(students)