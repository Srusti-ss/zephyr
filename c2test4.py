def remove_duplicates(items):
    visited = set()
    unique_items = []

    for value in items:
        if value not in visited:
            visited.add(value)
            unique_items.append(value)

    return unique_items[:]


def longest_words(words_list, count):
    count = min(count, len(words_list))
    sorted_words = sorted(words_list, key=len, reverse=True)
    return sorted_words[:count]


def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def display(label, value):
    print(f"{label:<25}: {value}")


word_list = [
    "the", "cat", "sat", "on", "the", "mat", "the",
    "cat", "chased", "a", "sat", "butterfly", "on",
    "a", "phenomenal", "afternoon", "cat"
]

print_section("ORIGINAL WORD LIST")

display("Words", word_list)
display("Total Words", len(word_list))
display("First Word", word_list[0])
display("Last Word", word_list[-1])
display("Sample Slice", word_list[1:4])

print_section("REMOVE DUPLICATES")

unique_words = remove_duplicates(word_list)

display("Original Count", len(word_list))
display("Unique Count", len(unique_words))
display("Unique Words", unique_words)

print("\nProcessing Preview:")
seen_words = set()
current_list = []

for word in word_list[:8]:
    if word not in seen_words:
        seen_words.add(word)
        current_list.append(word)
        action = "Added"
    else:
        action = "Skipped"

    print(f"{word:<12} -> {action:<8} {current_list}")

print_section("TOP K LONGEST WORDS")

k = 5
top_words = longest_words(unique_words, k)

ranked_words = sorted(unique_words, key=len, reverse=True)

for position, word in enumerate(ranked_words, start=1):
    mark = "<-- Top 5" if position <= k else ""
    print(f"{position:<3} {word:<15} Length = {len(word)} {mark}")

print("\nTop 5 Longest Words:")
print(top_words)

print_section("COMBINED FUNCTION DEMO")

result = longest_words(remove_duplicates(word_list), 3)

print("After Removing Duplicates:")
print(remove_duplicates(word_list))

print("\nTop 3 Longest Words:")
print(result)

print("\nFirst 2 From Result:")
print(result[:2])

print_section("SUMMARY")

operations = [
    ("Set", "Tracks visited words"),
    ("List", "Stores final result"),
    ("Loop", "Traverses each item"),
    ("Membership Check", "Checks duplicates"),
    ("Append", "Adds unique values"),
    ("Length", "Counts elements"),
    ("Sorting", "Arranges by length"),
    ("Slicing", "Selects required elements"),
    ("Indexing", "Accesses a position"),
]

print(f"{'Operation':<20} Purpose")
print("-" * 45)

for operation, purpose in operations:
    print(f"{operation:<20} {purpose}")

print("\nConclusion:")
print("The program first removes duplicate words while")
print("keeping their original order. It then finds the")
print("longest words and returns the required top results.")