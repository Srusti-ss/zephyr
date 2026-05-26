import string


# Split sentence into words
def split_words(text):
    return text.split()


# Convert to lowercase and remove punctuation
def clean_words(words):
    cleaned = []

    for word in words:
        word = word.lower()
        word = word.strip(string.punctuation)
        cleaned.append(word)

    return cleaned


# Remove common stopwords
def remove_common_words(words, stop_words):
    final_words = []

    for word in words:
        if word not in stop_words and word != "":
            final_words.append(word)

    return final_words


# Simple stemming
def stem_words(words):
    endings = ["ing", "ed", "ly", "es", "s"]

    output = []

    for word in words:
        new_word = word

        for end in endings:
            if word.endswith(end) and len(word) > len(end) + 2:
                new_word = word[:-len(end)]
                break

        output.append(new_word)

    return output


# Stopword list
stop_words = {
    "a", "an", "the", "is", "are", "was",
    "in", "on", "at", "to", "of", "and",
    "or", "but", "for", "with"
}


# Main function
def main():

    text = "we are from csbs department,studying in 3rd year.running behind marks and to aquire skills and knowledge."

    print("Original Text:")
    print(text)

    print("\nAfter Tokenization:")
    words = split_words(text)
    print(words)

    print("\nAfter Normalization:")
    cleaned_words = clean_words(words)
    print(cleaned_words)

    print("\nAfter Stopword Removal:")
    filtered_words = remove_common_words(cleaned_words, stop_words)
    print(filtered_words)

    print("\nAfter Stemming:")
    stemmed_words = stem_words(filtered_words)
    print(stemmed_words)


# Run program
main()