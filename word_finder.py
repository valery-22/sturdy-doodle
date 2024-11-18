def frequent_words_finder(text):
    from collections import defaultdict

    text = text.lower()
    word_counts = defaultdict(int)
    word_list = text.split()
    for word in word_list:
        word_counts[word] += 1
    top_three = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:3]
    return top_three