from collections import Counter

movie_data = [
    ["amit", "interstellar"],
    ["vikas", "dhurandar"],
    ["amit", "mafia"],
    ["priya", "pie"],
    ["vikas", "mafia"]
]

# unique names done
unique_name = []
for name, movie in movie_data:
    if name not in unique_name:
        unique_name.append(name)
print(unique_name)

# count unique movies
unique_movies = []
for name, movie in movie_data:
    if movie not in unique_movies:
        unique_movies.append(movie)
print(len(unique_movies))

# movies occurence
movie_count = {}
for name, movie in movie_data:
    if movie not in movie_count:
        movie_count[movie] = 1 
    else:
        movie_count[movie] += 1

# expected output is
"""
expected op is 
dhurandar 1
interstellar 1
mafia 1
pie 2 
"""
for movie, count in movie_count.items():
    print(f"{movie} {count}")


movies_only = [movie for name, movie in movie_data]

# Count them automatically
counts = Counter(movies_only)

print(counts)


election_data = [
    # [Precinct, Position, Name, Points]
    [1, "Mayor",      "Amit",  500],
    [1, "Counsellor", "Priya", 200],
    [1, "Counsellor", "Rohan", 150],

    [2, "Mayor",      "Amit",  450],
    [2, "Counsellor", "Rohan", 300],

    [3, "Mayor",      "Priya", 600],
    [3, "Counsellor", "Amit",  120],

    [4, "Mayor",      "Rohan", 400],
    [4, "Counsellor", "Priya", 250],
    [4, "Counsellor", "Amit",  100]
]

amit_score = 0
for precinct, position, name, points in election_data:
    if name == "Amit":
        print(f"Amit got {points} points in precinct {precinct}")
        amit_score += points
print(amit_score)

mayor_scores = {}
consellor_scores = {}

for precinct, position, name, points in election_data:
    if position == "Mayor":
        if name not in mayor_scores:
            mayor_scores[name] = 0
        mayor_scores[name] += points
    elif position == "Counsellor":
        if name not in consellor_scores:
            consellor_scores[name] = 0
        consellor_scores[name] += points

winner_mayor = max(mayor_scores.items(), key=lambda x:x[1])
winner_counsellor = max(consellor_scores.items(), key=lambda x: x[0])
print(mayor_scores)
print("Final Results")
print(f"Winning Mayor: {winner_mayor[0]} with {winner_mayor[1]} total Points")
print(f"Winning Counsellor: {winner_counsellor[0]} with {winner_counsellor[1]} total points")


# mastering lambda 
nums = [1, 2, 3, 4]

# Return x squared for every x in the list
squared = list(map(lambda x: x**2, nums))

print(squared) # Output: [1, 4, 9, 16]

cube = list(map(lambda x: x**3, nums))
print(cube)

odd = list(filter(lambda x: x % 2 != 0, nums))
# filter is like a bodygaurd this lets you only pass the items which are true and false 
print(f"{odd} is/are even")

even = list(filter(lambda x: x % 2 == 0, nums))
print(f"{even} is/are even")


def two_sum(l1, target):
    left, right = 0 , len(l1) - 1

    while left < right:
        curr = l1[left] + l1[right]
        if curr == target:
            return left, right
        elif curr < target:
            left += 1
        else:
            right -= 1
    return []

l1 = 10,20,30,40
target = 50


print(two_sum(l1, target))
