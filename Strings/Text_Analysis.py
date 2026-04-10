import string

def analyze_paragraph(paragraph):
    translator = str.maketrans('', '', string.punctuation)
    words = paragraph.translate(translator).lower().split()

    word_count = {}
    longest_word = ""
    for w in words:
        word_count[w] = word_count.get(w, 0) + 1
    most_repeated_word = max(word_count, key=word_count.get)
    for w in words:
        word_count[w] = word_count.get(w, 0) + 1
    longest_word = max(words, key=len) if words else "" 
    paragraph_length = len(paragraph)

    print(f"Word count for each word: {word_count}")
    print(f"Most repeated word: '{most_repeated_word}' (appeared {word_count[most_repeated_word]} times)")
    print(f"Longest word: '{longest_word}' (length {len(longest_word)})")
    print(f"Length of entire paragraph (characters): {paragraph_length}")

if __name__ == "__main__":
    user_paragraph = input("Enter a paragraph or large text:\n")
    analyze_paragraph(user_paragraph)
