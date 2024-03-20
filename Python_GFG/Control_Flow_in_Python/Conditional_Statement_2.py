# # Create a list of sets
# data = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}, {4, 5, 6}, {5, 6, 7}] * 40

# # Initialize an empty set to store results
# result_set = set()

# # Iterate through the list of sets
# for s in data:

#     # Check if the set contains the number 3
#     if 3 in s:
#         result_set.add(f"Set {s} contains 3")

#     # Check if the set is a subset of {4, 5, 6}
#     if s.issubset({4, 5, 6}):
#         result_set.add(f"Set {s} is a subset of {4, 5, 6}")

#     # Check if the set has more than 3 elements
#     if len(s) > 3:
#         result_set.add(f"Set {s} has more than 3 elements")

# # Print the results
# for r in result_set:
#     print(r)

# # '''''''''''''''''''''''''''''''''
# # Create three sets
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# set3 = {5, 6, 7, 8, 9}

# # Using set comprehensions and conditional statements
# even_squared = {x ** 2 for x in set1 if x % 2 == 0}
# print("Squares of even numbers in set1:", even_squared)

# # Check for set intersection and apply a function to the result
# intersection = set1 & set2
# if intersection:
#     multiplied_intersection = {x * 2 for x in intersection}
#     print("Intersection of set1 and set2, doubled:", multiplied_intersection)
# else:
#     print("There is no intersection between set1 and set2")

# # Check if all elements in set1 satisfy a condition
# all_greater_than_zero = all(x > 0 for x in set1)
# print("Are all elements in set1 greater than zero?", all_greater_than_zero)

# # Check if any element in set2 satisfies a condition
# any_greater_than_ten = any(x > 10 for x in set2)
# print("Is there any element in set2 greater than ten?", any_greater_than_ten)

# # Using set operations and conditional statements to create a new set
# if set1 & set3:
#     new_set = {x + 10 for x in set1 - set3}
# else:
#     new_set = set1 | set3
# print("New set based on conditional operations:", new_set)

# # Check if sets are disjoint and symmetric differences
# is_disjoint = set1.isdisjoint(set2)
# symmetric_difference = set1.symmetric_difference(set2)
# print("Are set1 and set2 disjoint?", is_disjoint)
# print("Symmetric difference between set1 and set2:", symmetric_difference)

# # Complex conditional statements with sets
# if set1.issubset(set2) and len(set2) > 3:
#     result_set = set1.union(set3)
# elif len(set1) > len(set2):
#     result_set = set1.intersection(set2)
# else:
#     result_set = set1.symmetric_difference(set3)
# print("Result set based on complex conditions:", result_set)


# # ''''''''''''''''''''''''
# # Define some sets
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# set3 = {5, 6, 7, 8, 9}

# # Function to find the common elements among multiple sets
# def find_common_elements(*sets):
#     common_elements = set.intersection(*sets)
#     return common_elements

# common_set = find_common_elements(set1, set2, set3)
# print("Common elements among set1, set2, and set3:", common_set)

# # Function to find the union of multiple sets
# def find_union(*sets):
#     union_set = set.union(*sets)
#     return union_set

# union_set = find_union(set1, set2, set3)
# print("Union of set1, set2, and set3:", union_set)

# # Use list comprehensions to create sets
# evens_set = {x for x in range(10) if x % 2 == 0}
# odds_set = {x for x in range(10) if x % 2 != 0}

# print("Set of even numbers from 0 to 9:", evens_set)
# print("Set of odd numbers from 0 to 9:", odds_set)

# # Advanced conditional statement with sets
# def advanced_set_condition(set1, set2):
#     if len(set1) > len(set2):
#         return "Set1 has more elements than Set2"
#     elif len(set1) < len(set2):
#         return "Set2 has more elements than Set1"
#     else:
#         return "Set1 and Set2 have the same number of elements"

# print(advanced_set_condition(set1, set2))

# # Check if a set is a proper subset or superset of another
# def is_proper_subset_superset(set1, set2):
#     if set1 != set2 and set1.issubset(set2):
#         return "Set1 is a proper subset of Set2"
#     elif set1 != set2 and set1.issuperset(set2):
#         return "Set1 is a proper superset of Set2"
#     else:
#         return "Set1 and Set2 are not proper subsets/supersets of each other"

# print(is_proper_subset_superset({1, 2}, {1, 2, 3}))


# # ''''''''''''''''''''''''''''
# # Define sets
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# set3 = {5, 6, 7, 8, 9}

# # Set comprehension: Create a set of squares for even numbers in a range
# even_squares = {x**2 for x in range(10) if x % 2 == 0}

# # Conditional set creation: Create a set based on a condition
# conditional_set = {x for x in set1 if x % 2 == 0}

# # Advanced set operations
# union_set = set1.union(set2, set3)
# intersection_set = set1 & set2 & set3
# difference_set = set1.difference(set2).difference(set3)

# # Check if sets satisfy complex conditions
# if all(x > 0 for x in union_set) and any(x % 2 == 0 for x in intersection_set):
#     print("All elements in the union set are positive, and there's at least one even number in the intersection set.")
# else:
#     print("The conditions were not met.")

# # Advanced conditionals based on set properties
# if len(set1) > len(set2) and not set1.isdisjoint(set2):
#     print("Set1 is larger than Set2 and has at least one common element with Set2.")
# else:
#     print("Set1 is not larger than Set2 or has no common elements with Set2.")

# # More advanced set operations
# symmetric_difference_set = set1.symmetric_difference(set2)

# # Display results
# print("Even squares:", even_squares)
# print("Conditional set:", conditional_set)
# print("Union of all sets:", union_set)
# print("Intersection of all sets:", intersection_set)
# print("Difference between set1, set2, and set3:", difference_set)
# print("Symmetric difference between set1 and set2:", symmetric_difference_set)

# '''''''''''''''''''''''''''''''Conditional Statements with custom objects'''''''''''''''''''''''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

# Create a list of custom objects (Person instances)
people = [
    Person("Alice", 25),
    Person("Bob", 30),
    Person("Charlie", 22),
    Person("David", 35),
]

# Filter people based on age using list comprehension
young_people = [person for person in people if person.age < 30]
middle_aged_people = [person for person in people if 30 <= person.age < 40]
older_people = [person for person in people if person.age >= 40]

# Print the filtered lists
print("Young people:")
for person in young_people:
    print(person)

print("\nMiddle-aged people:")
for person in middle_aged_people:
    print(person)

print("\nOlder people:")
for person in older_people:
    print(person)

# Conditional statements based on custom object attributes
if any(person.age < 25 for person in people):
    print("\nThere are people under 25 years old.")
else:
    print("\nEveryone is 25 or older.")

# Find the oldest person using max and a custom key function
oldest_person = max(people, key=lambda x: x.age)
print(f"\nThe oldest person is: {oldest_person}")

# Sort people by age
sorted_people = sorted(people, key=lambda x: x.age)

print("\nPeople sorted by age:")
for person in sorted_people:
    print(person)

# ''''''''''''''''''''''''''
# Define a custom class representing a Contestant
class Contestant:
    def __init__(self, name, score):
        self.name = name
        self.score = score

# Create instances of the Contestant class
contestant1 = Contestant("Alice", 250)
contestant2 = Contestant("Bob", 300)
contestant3 = Contestant("Charlie", 200)
contestant4 = Contestant("David", 350)

# Store contestants in a list
contestants = [contestant1, contestant2, contestant3, contestant4]

# Sort contestants by score in descending order
contestants.sort(key=lambda x: x.score, reverse=True)

# Find the highest-scoring contestant
highest_score = contestants[0].score

# Determine the winner and runner-up
winner = []
runner_up = []

for contestant in contestants:
    if contestant.score == highest_score:
        winner.append(contestant.name)
    else:
        runner_up.append(contestant.name)

# Display the results
print("Contest results:")
for contestant in contestants:
    print(f"{contestant.name}: {contestant.score} points")

if len(winner) == 1:
    print(f"The winner is {winner[0]} with {highest_score} points.")
else:
    print(f"It's a tie! Winners: {', '.join(winner)} with {highest_score} points each.")

if runner_up:
    print(f"Runner-up(s): {', '.join(runner_up)}")
else:
    print("No runner-up in this contest.")
