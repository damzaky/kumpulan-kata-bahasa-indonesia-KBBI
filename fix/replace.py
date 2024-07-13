# Read the contents of the text file
with open('fix/list_words.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

with open('fix/final_fix.txt', 'r', encoding='utf-8') as file:
    fixed_words = [line.strip() for line in file]

fixed_words_iter = iter(fixed_words)
count = 0

for line in lines:
    if '?' in line:
        line = next(fixed_words_iter)
        count += 1

print(count)