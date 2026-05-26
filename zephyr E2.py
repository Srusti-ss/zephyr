import time
import random
import string

random.seed(42)

# Generate random token
def generate_word(length=6):
    return "".join(random.choices(string.ascii_lowercase, k=length))


# Sizes
block_words_count = 10000
stream_words_count = 5000000
sample_size = 50000


# Create blocklist and token stream
blocked_words = [generate_word() for _ in range(block_words_count)]
incoming_tokens = [generate_word() for _ in range(stream_words_count)]


# Different data structures
blocked_list = blocked_words
blocked_tuple = tuple(blocked_words)
blocked_set = set(blocked_words)


# Benchmark function
def check_speed(structure_name, data_structure, tokens, note=""):
    start_time = time.perf_counter()

    found_count = sum(1 for word in tokens if word in data_structure)

    end_time = time.perf_counter()
    total_time = end_time - start_time

    print(f"{structure_name:<15} | {note:<20} | hits: {found_count:>6} | time: {total_time:.4f}s")

    return total_time


print(f"Blocklist size : {block_words_count:,}")
print(f"Stream size    : {stream_words_count:,}")
print(f"(list/tuple tested on {sample_size:,}-token subset)")
print("-" * 68)


# Run benchmarks
check_speed("list", blocked_list,
            incoming_tokens[:sample_size],
            "O(n) on 50k subset")

check_speed("tuple", blocked_tuple,
            incoming_tokens[:sample_size],
            "O(n) on 50k subset")

set_time = check_speed("set", blocked_set,
                       incoming_tokens,
                       "O(1) on full 5M")


# Estimate list time for full dataset
list_sample_time = check_speed("list (50k)",
                               blocked_list,
                               incoming_tokens[:sample_size])

estimated_time = list_sample_time * (stream_words_count / sample_size)

print(f"  → estimated list time for 5M tokens: ~{estimated_time:.1f}s")
print(f"  → set is approximately {estimated_time / set_time:.0f}x faster")