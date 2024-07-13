from kbbi import *

# Read terms from the file
try:
    with open('fix/fix.txt', 'r', encoding='utf-8') as file:
        terms = [line.strip() for line in file]
except FileNotFoundError:
    print("The file fix.txt was not found.")
    exit()

results = {}

auth = AutentikasiKBBI("focig57450@mposhop.com", "siganteng")

for term in terms:
    try:
        print(f"Checking term: {term}")  # Debugging statement
        entry = KBBI(term, auth)
        results[term] = "found"
    except TidakDitemukan:
        results[term] = "not found"
    except BatasSehari:
        results[term] = "batas sehari"
    except AkunDibekukan:
        results[term] = "banned"
    except Exception as e:
        results[term] = f"error: {str(e)}"

# Write the results to an output file
try:
    with open('fix/results.txt', 'w', encoding='utf-8') as file:
        for term, status in results.items():
            file.write(f"{term}+{status}\n")
except Exception as e:
    print(f"Error writing to results file: {str(e)}")
    exit()

print("Check completed. Results are saved in 'results.txt'.")
