no_of_days = 1234

years = no_of_days // 365
print(years)

no_of_days %= 365
weeks = no_of_days // 7
print(weeks)

no_of_days %= 7
print(no_of_days)


s = "I am Aniket Rajendra Chaudhari"

words = s.split()
print(words)
maxLenWord = max(len(word) for word in words)
print(maxLenWord)


