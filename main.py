import numpy as np

# Create the grades array
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])

# 1. Calculate mean, median, standard deviation
mean_grade = np.mean(grades)
median_grade = np.median(grades)
std_dev = np.std(grades)

# 2. Find maximum and minimum
max_grade = np.max(grades)
min_grade = np.min(grades)

# 3. Sort the grades in ascending order
sorted_grades = np.sort(grades)

# 4. Find the index of the highest grade
index_of_max = np.argmax(grades)

# 5. Count number of students who scored above 90
count_above_90 = np.sum(grades > 90)

# 6. Calculate percentage of students who scored above 90
percentage_above_90 = (count_above_90 / len(grades)) * 100

# 7. Calculate percentage of students who scored below 75
count_below_75 = np.sum(grades < 75)
percentage_below_75 = (count_below_75 / len(grades)) * 100

# 8. Extract grades above 90 into "high_performers"
high_performers = grades[grades > 90]

# 9. Create "passing_grades" array (grades above 75)
passing_grades = grades[grades > 75]

# Print all results
print("Grades array:", grades)
print("\nStatistics:")
print(f"Mean: {mean_grade}")
print(f"Median: {median_grade}")
print(f"Standard Deviation: {std_dev}")

print("\nMax grade:", max_grade)
print("Min grade:", min_grade)

print("\nSorted grades:", sorted_grades)
print("Index of highest grade:", index_of_max)

print("\nNumber of students who scored above 90:", count_above_90)
print(f"Percentage of students who scored above 90: {percentage_above_90:.2f}%")
print(f"Percentage of students who scored below 75: {percentage_below_75:.2f}%")

print("\nHigh performers (grades above 90):", high_performers)
print("Passing grades (grades above 75):", passing_grades)