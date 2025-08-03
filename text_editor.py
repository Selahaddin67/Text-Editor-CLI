def read_file(filename="my_text_file.txt"):
    with open(filename, 'r') as file:
        content = file.read()
    return content

def save_file(content, filename="my_text_file.txt"):
    with open(filename, 'w') as file:
        file.write(content)

import string
from collections import Counter

def word_count(text):
    words = text.translate(str.maketrans('', '', string.punctuation)).lower().split()
    word_counts = Counter(words)
    top_five = word_counts.most_common(5)

    print("\nTop 5 Most Common Words:")
    for word, count in top_five:
        print(f"{word.upper()} - {count} times")

    return word_counts

def is_single_word(word):
    return word.strip().count(" ") == 0 and word.strip() != ""

def single_word_count(text):
    word = input(">> Enter a word to count: ").strip()

    while not is_single_word(word):
        print("Please enter a single word (no spaces).")
        word = input(">> Enter a word to count: ").strip()

    words = text.translate(str.maketrans('', '', string.punctuation)).lower().split()
    count = words.count(word.lower())

    print(f"\n{word.upper()} appears {count} time(s) in the text.")

def replace_word(text):
    target = input(">> Enter the word to replace: ").strip()
    replacement = input(">> Enter the replacement word: ").strip()

    if not is_single_word(target) or not is_single_word(replacement):
        print("Both inputs must be single words.")
        return text

    words = text.split()
    replaced_count = 0

    for i in range(len(words)):
        word_clean = words[i].strip(string.punctuation)
        if word_clean.lower() == target.lower():
            punctuation = words[i][len(word_clean):]
            words[i] = replacement + punctuation
            replaced_count += 1

    updated_text = ' '.join(words)
    print(f"\n{replaced_count} word(s) replaced with {replacement.upper()}.")

    save_file(updated_text)
    return updated_text

def add_text(text):
    new_text = input(">> Enter text to add: ").strip()
    if new_text == "":
        print("No text added.")
        return text

    updated_text = text + "\n" + new_text
    save_file(updated_text)
    print("Text added and file updated.")
    return updated_text

def delete_text(text):
    to_delete = input(">> Enter the text to delete (first instance only): ").strip()
    if to_delete == "":
        print("No text entered.")
        return text

    index = text.find(to_delete)
    if index == -1:
        print("Text not found.")
        return text

    updated_text = text.replace(to_delete, "", 1)
    save_file(updated_text)
    print(f"First instance of '{to_delete}' deleted and file updated.")
    return updated_text

def highlight_word(text):
    word = input(">> Enter a word to highlight: ").strip()

    if not is_single_word(word):
        print("Please enter a single word.")
        return

    words = text.split()
    highlight_words = []

    for w in words:
        stripped = w.strip(string.punctuation)
        if stripped.lower() == word.lower():

            prefix = w[:w.find(stripped)]
            suffix = w[w.find(stripped) + len(stripped):]
            w = prefix + "**" + stripped + "**" + suffix
        highlight_words.append(w)

    highlighted_text = ' '.join(highlight_words)
    print("\nHighlighted Text:\n")
    print(highlighted_text)

    save_file(highlighted_text)
    print("Highlighted text saved to file.")
    return highlighted_text

def reverse_text(text):
    reversed_text = text[::-1]

    print(("\nReversed Text:\n"))
    print(reversed_text)
    save_file(reversed_text)
    print("Reversed text saved to file.")
    return reversed_text

if __name__ == "__main__":
    text = read_file()

    while True:
        print("\n======== Edit Menu ========")
        print("1: Top 5 Most Common Words")
        print("2: Single Word Frequency")
        print("3: Replace a Word")
        print("4: Add Text")
        print("5: Delete Text")
        print("6: Highlight Text")
        print("7: Reverse Text")
        print("0: Exit")
        print("===========================")
        choice = input(">> Input: ")

        if choice == '1':
            word_count(text)

        elif choice == '0':
            print("Exiting...")
            break

        elif choice == '2':
            single_word_count(text)

        elif choice == '3':
            text = replace_word(text)

        elif choice == '4':
            text = add_text(text)

        elif choice == '5':
            text = delete_text(text)

        elif choice == '6':
            text = highlight_word(text)

        elif choice == '7':
            text = reverse_text(text)

        else:
            print("Invalid Option.")