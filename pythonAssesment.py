import re
from collections import Counter


def read_article(file_path):
    """
    Reads the contents of a text file and returns it as a string.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return ""



# Count a partcular Word


def count_specific_word(text, search_word):
    if text == "" or search_word == "":
        return 0

    text = text.lower()
    search_word = search_word.lower()

    words = text.split()
    count = 0

    for word in words:  # FOR LOOP REQUIRED
        # remove punctuation manually
        clean_word = word.strip(".,!?;:\"'()")

        if clean_word == search_word:  # IF STATEMENT REQUIRED
            count += 1

    return count

# Find the most common word in the text

def identify_most_common_word(text):
    if text == "":
        return None

    words = text.lower().split()
    word_counts = {}

    for word in words:  # FOR LOOP
        clean_word = word.strip(".,!?;:\"'()")

        if clean_word in word_counts:
            word_counts[clean_word] += 1
        else:
            word_counts[clean_word] = 1

    most_common_word = None
    highest_count = 0

    for word in word_counts:
        if word_counts[word] > highest_count:
            highest_count = word_counts[word]
            most_common_word = word

    return most_common_word


# count the average word length in the text


def calculate_average_word_length(text):
    if text == "":
        return 0

    words = text.split()
    total_length = 0
    total_words = 0

    for word in words:  # FOR LOOP
        clean_word = word.strip(".,!?;:\"'()")

        if clean_word != "":
            total_length += len(clean_word)
            total_words += 1

    if total_words == 0:
        return 0
    else:
        return total_length / total_words



# calculate the number o paragraghs


def count_paragraphs(text):
    if text == "":
        return 1

    paragraphs = text.split("\n\n")
    count = 0

    for paragraph in paragraphs:
        if paragraph.strip() != "":
            count += 1

    return count


# calculate the number o sentenses


def count_sentences(text):
    if text == "":
        return 1

    count = 0
    i = 0

    while i < len(text):  # WHILE LOOP REQUIRED
        if text[i] == "." or text[i] == "!" or text[i] == "?":
            count += 1
        i += 1

    return count


# Main function to execute the analysis


def main():
    file = open("news_article.txt", "r")
    article = file.read()
    file.close()

    print("Text Analysis Results")

    word = input("Enter a word to search: ")

    print("Specific Word Count:", count_specific_word(article, word))
    print("Most Common Word:", identify_most_common_word(article))
    print("Average Word Length:", calculate_average_word_length(article))
    print("Number of Paragraphs:", count_paragraphs(article))
    print("Number of Sentences:", count_sentences(article))


if __name__ == "__main__":
    main()