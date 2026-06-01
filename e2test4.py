tokens_a = [["the", "DT"], ["cat", "NN"], ["sat", "VBD"]]
tokens_b = [("the", "DT"), ("cat", "NN"), ("sat", "VBD")]
tokens_c = {"the/DT": 1, "cat/NN": 1, "sat/VBD": 1}

best_choice = (("the", "DT"), ("cat", "NN"), ("sat", "VBD"))


def check_representation(title, data):
    print("\n" + "-" * 50)
    print(title)
    print("-" * 50)
    print("Value :", data)
    print("Type  :", type(data)._name_)

    try:
        data[0] = data[0]
        is_immutable = False
        imm_msg = "can be modified"
    except (TypeError, KeyError):
        is_immutable = True
        imm_msg = "cannot be modified"

    try:
        value_hash = hash(data)
        is_hashable = True
        hash_msg = f"hash value = {value_hash}"
    except TypeError as err:
        is_hashable = False
        hash_msg = str(err)

    notes = {
        "Option A - list of lists": ("Readable but fully mutable", "!"),
        "Option B - list of tuples": ("Pairs are clear and easy to read", "+"),
        "Option C - dictionary": ("Loses sequence information", "-"),
        "Preferred - tuple of tuples": ("Ordered, clear and immutable", "+"),
    }

    text, symbol = notes[title]

    print("\nImmutable :", ("Yes" if is_immutable else "No"), "-", imm_msg)
    print("Hashable  :", ("Yes" if is_hashable else "No"), "-", hash_msg)
    print("Clarity   :", symbol, "-", text)

    print("\nCache Test:")
    if is_hashable:
        sample_cache = {data: "stored"}
        print("  Result ->", sample_cache[data])
    else:
        try:
            sample_cache = {data: "stored"}
        except TypeError as err:
            print("  Cannot be used as key ->", err)


print("=" * 50)
print("ANNOTATED CORPUS REPRESENTATION CHECK")
print("=" * 50)

check_representation("Option A - list of lists", tokens_a)
check_representation("Option B - list of tuples", tokens_b)
check_representation("Option C - dictionary", tokens_c)
check_representation("Preferred - tuple of tuples", best_choice)

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)

print(f"{'Representation':<30} {'Immutable':<12} {'Hashable':<10} {'Clarity'}")
print("-" * 50)

summary_data = [
    ("List of lists", "No", "No", "Average"),
    ("List of tuples", "Partial", "No", "Good"),
    ("Dictionary", "No", "No", "Poor"),
    ("Tuple of tuples", "Yes", "Yes", "Excellent")
]

for item, imm, hsh, clarity in summary_data:
    print(f"{item:<30} {imm:<12} {hsh:<10} {clarity}")

print("\nFinal Conclusion:")
print("Tuple of tuples is the best choice because it preserves")
print("order, keeps word-tag pairs together, is immutable,")
print("and can also be used as a dictionary key when needed.")