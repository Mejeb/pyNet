n, m = map(int, input().split())
dictionary = [input().strip() for _ in range(n)]
words = [input().strip() for _ in range(m)]

for word in words:
    if len(word) < 6:
        print("none")
        continue

    prefixes = [word[:i] for i in range(3, len(word))]
    suffixes = [word[i:] for i in range(len(word)-2, -1, -1)]

    possible_pairs = []

    for prefix in prefixes:
        for suffix in suffixes:
            for dictionary_word in dictionary:
                if dictionary_word.startswith(prefix) and dictionary_word.endswith(suffix):
                    possible_pairs.append((dictionary_word, dictionary_word))
                    break

    if not possible_pairs:
        print("none")
    elif len(possible_pairs) > 1:
        print("ambiguous")
    else:
        print(possible_pairs[0][0], possible_pairs[0][1])
