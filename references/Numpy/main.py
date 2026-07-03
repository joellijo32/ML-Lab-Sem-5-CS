import numpy as np

# Filtering

ages = np.array([
    [43, 3, 62, 1, 24, 2, 62, 41],
    [39, 12, 64, 14, 100, 61, 7, 53]
])

teenagers = ages[(ages >= 13) & (ages <= 19)] 

print("Teenagers:", teenagers)

adults = ages[(ages >= 18) & (ages <= 65)]

print("Adults:", adults)

seniors = ages[ages >= 65]

print("Seniors:", seniors)

evens = ages[ages %2 == 0]

print("evens:", evens)

odds = ages[ages%2 != 0]

print("odds:", odds)

# Filtering with preserving shape
# where(condition, array, fill_value)

adults = np.where(ages>=18, ages, -1)

print("adults:\n", adults)