import re
import nltk
from nltk.tag import DefaultTagger, RegexpTagger, UnigramTagger


def build_tagger(train_sentences):
    default = DefaultTagger("NN")

    rules = [
        (r".*ing$", "VBG"),
        (r".*ed$", "VBD"),
        (r".*s$", "NNS"),
        (r"^[0-9]+$", "CD"),
    ]

    regex_tagger = RegexpTagger(rules, backoff=default)

    unigram = UnigramTagger(
        train_sentences,
        backoff=regex_tagger
    )

    return unigram


if __name__ == "__main__":
    nltk.download("brown", quiet=True)
    nltk.download("universal_tagset", quiet=True)

    from nltk.corpus import brown

    train_sentences = brown.tagged_sents(categories="news")

    tagger = build_tagger(train_sentences)

    words = [
        "The",
        "Zorbaxing",
        "robots",
        "built",
        "42",
        "flurbs"
    ]

    tagged_words = tagger.tag(words)

    vocabulary = {
        word.lower()
        for sentence in train_sentences
        for word, tag in sentence
    }

    patterns = [
        r".*ing$",
        r".*ed$",
        r".*s$",
        r"^[0-9]+$"
    ]

    print("Token          Tag   Source")
    print("-" * 45)

    for word, tag in tagged_words:

        if word.lower() in vocabulary:
            source = "UnigramTagger"

        elif any(re.search(pattern, word) for pattern in patterns):
            source = "RegexpTagger"

        else:
            source = "DefaultTagger"

        print(f"{word:<14} {tag:<5} {source}")