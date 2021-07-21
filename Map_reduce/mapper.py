

    def word_count(data):

        counts = dict()
        words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

word_count(data)