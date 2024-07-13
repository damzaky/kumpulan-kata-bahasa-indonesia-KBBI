# Read the contents of the text file
with open('list_1.0.0.txt', 'r') as file:
    lines = file.readlines()

# Strip newline characters and check for the presence of '?'
words_with_question_mark = [line.strip() for line in lines if '?' in line]

# Write the resulting list to a new file
with open('fix/raw_fix.txt', 'w') as output_file:
    for word in words_with_question_mark:
        output_file.write(word + '\n')