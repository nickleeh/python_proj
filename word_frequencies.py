from collections import Counter


def read_words(file_name):
    with open(file_name) as f:
        words = f.read().lower().split()
    return words


def top_n_words(counter, n):
    top_n = counter.most_common(n)
    print("Top %d words are:" % n)
    print("-" * 20)
    for w, c in top_n:
        # print("%10s: %-10s" % (w, c))
        print("{word:>10s}: {counts:<10d}".format(word=w, counts=c))


def word_appears(counter, w):
    print(
        "The word '{word:s}' appears {time:d} times.".
        format(word=w, time=counter[w]))


if __name__ == '__main__':

    def main(file_name):
        words = read_words(file_name)
        counter = Counter(words)
        top_n_words(counter, 15)
        print("-" * 20)
        print("Total words: %d" % len(words))
        word_appears(counter, "history")

    main('c:/Users/Nick/Downloads/sample_file.txt')
