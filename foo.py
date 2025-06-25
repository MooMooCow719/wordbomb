

trigrams = []

with open('words.txt', 'r', encoding='utf-8') as f:
    reader = f
    for i, row in enumerate(reader):
        trigrams.append(row)

# Optional: save to a .txt file
with open('words.txt', 'w', encoding='utf-8') as out:
    for trigram in trigrams:
        out.write(trigram.strip() + "," + "\n")
