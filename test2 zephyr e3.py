import random
import string
import timeit
from collections import defaultdict

SEED = 42
VOCAB_SIZE = 50000
STREAM_SIZE = 4000000


def make_stream(n, vocab, seed):
    rng = random.Random(seed)

    words = []
    for _ in range(vocab):
        word = "".join(
            rng.choices(string.ascii_lowercase, k=rng.randint(3, 10))
        )
        words.append(word)

    stream = [rng.choice(words) for _ in range(n)]
    return stream


def approach_a(stream):
    counts = {}

    for word in stream:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def approach_b(stream):
    counts = defaultdict(int)

    for word in stream:
        counts[word] += 1

    return counts


def approach_c(stream):
    counts = {}

    for word in stream:
        counts[word] = counts.setdefault(word, 0) + 1

    return counts


def verify_correctness(stream):
    print("=" * 50)
    print("Correctness Check")
    print("=" * 50)

    sample = stream[:10]

    result_a = approach_a(sample)
    result_b = dict(approach_b(sample))
    result_c = approach_c(sample)

    assert result_a == result_b == result_c

    print("Sample Stream:")
    print(sample)
    print()

    print("Approach A:", result_a)
    print("Approach B:", result_b)
    print("Approach C:", result_c)
    print()

    print("All approaches produce the same result.\n")


def ghost_entry_demo():
    print("=" * 50)
    print("Ghost Entry Demo")
    print("=" * 50)

    normal_dict = {"apple": 3}

    _ = "banana" in normal_dict

    print("Plain dict keys:")
    print(list(normal_dict.keys()))
    print()

    default_dict = defaultdict(int)

    default_dict["apple"] += 3

    before = len(default_dict)

    value = default_dict["banana"]

    after = len(default_dict)

    print("defaultdict access:")
    print("Returned value:", value)
    print("Keys before:", before)
    print("Keys after :", after)
    print("banana exists:", "banana" in default_dict)
    print()

    safe_value = default_dict.get("orange", 0)

    print("Safe access using get():")
    print("Returned value:", safe_value)
    print("orange exists:", "orange" in default_dict)
    print()

    setdefault_dict = {"apple": 3}

    temp = setdefault_dict.setdefault("banana", 0)

    print("setdefault access:")
    print("Returned value:", temp)
    print("Keys:", list(setdefault_dict.keys()))
    print()


def benchmark(stream, repeat=3):
    print("=" * 50)
    print("Benchmark")
    print("=" * 50)

    def run_test(fn):
        times = timeit.repeat(lambda: fn(stream), number=1, repeat=repeat)
        return min(times)

    time_a = run_test(approach_a)
    time_b = run_test(approach_b)
    time_c = run_test(approach_c)

    print(f"Approach A: {time_a:.3f}s")
    print(f"Approach B: {time_b:.3f}s")
    print(f"Approach C: {time_c:.3f}s")
    print()


def readability_summary():
    print("=" * 50)
    print("Readability Summary")
    print("=" * 50)

    print("""
Approach A:
Uses a normal dictionary with an explicit condition.
Very easy to understand but slightly longer.

Approach B:
Uses defaultdict(int).
Short, clean and commonly used for counting.

Approach C:
Uses setdefault().
Works correctly but is less readable for counting logic.
""")


def recommendation(stream):
    print("=" * 50)
    print("Recommended Version")
    print("=" * 50)

    counts = defaultdict(int)

    for word in stream:
        counts[word] += 1

    sample_words = list(counts.keys())[:3]
    sample_words.append("__ghost__")

    for word in sample_words:
        print(f"{word:20s} -> {counts.get(word, 0)}")

    final_dict = dict(counts)

    print()
    print("Unique words:", len(final_dict))

    top_words = sorted(
        final_dict.items(),
        key=lambda item: item[1],
        reverse=True
    )[:5]

    print("\nTop 5 words:")

    for index, (word, freq) in enumerate(top_words, start=1):
        print(f"{index}. {word:20s} {freq}")


if __name__ == "__main__":
    print(f"\nGenerating stream with {STREAM_SIZE} tokens...\n")

    stream = make_stream(STREAM_SIZE, VOCAB_SIZE, SEED)

    print("Stream generated.\n")

    verify_correctness(stream)

    ghost_entry_demo()

    benchmark(stream)

    readability_summary()

    recommendation(stream)

    print("\nDone.")