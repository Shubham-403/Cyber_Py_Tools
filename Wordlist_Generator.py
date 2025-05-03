import itertools

# Input keywords
keywords = ["john", "doe", "admin"]

# Common suffixes/prefixes
numbers = ["", "123", "2024", "!", "@", "#", "1", "12", "1234"]
specials = ["!", "@", "#", "$", "_", "-", "."]

# Result set to avoid duplicates
results = set()

# Generate simple combos
for i in range(1, len(keywords) + 1):
    for combo in itertools.permutations(keywords, i):
        word = ''.join(combo)
        results.add(word)
        # Add suffixes/prefixes
        for n in numbers:
            results.add(word + n)
            results.add(n + word)
        for s in specials:
            results.add(word + s)
            results.add(s + word)

# Optional: add leetspeak variants
def leetspeak(word):
    return word.replace('a', '@').replace('o', '0').replace('e', '3').replace('i', '1')

for word in list(results):
    results.add(leetspeak(word.lower()))

# Save to file
with open("wordlist.txt", "w") as f:
    for word in sorted(results):
        f.write(word + "\n")

print(f"[+] Wordlist generated with {len(results)} entries.")
