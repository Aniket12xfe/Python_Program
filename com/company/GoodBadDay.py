days = input()
days_input = str(input())


fishman = list(map(int, days_input.split(',')))

max_fish = fishman[0]
min_fish = fishman[0]
happy_count = 0
sad_count = 0

for i in range(1, len(fishman)):
    if fishman[i] > max_fish:
        happy_count += 1
        max_fish = fishman[i]
    elif fishman[i] < min_fish:
        sad_count += 1
        min_fish = fishman[i]

print(happy_count)
print(sad_count)