def analyze_text(text):
    text = text.lower()
    text = ''.join(c for c in text if c.isalnum() or c.isspace())
    words = text.split()
    num_words = len(words)
    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    word_lengths = [len(word) for word in words]
    average_length = sum(word_lengths) / num_words
    statistics = "Text Analysis:\n"
    statistics += f"Number of words: {num_words}\n"
    statistics += "Word frequency:\n"
    for word, frequency in word_frequency.items():
        statistics += f"   {word}: {frequency}\n"
    statistics += f"Average word length: {average_length:.2f}"
    print(statistics)

text = input("Enter the text: ")
analyze_text(text)

input("Press Enter to exit...")

