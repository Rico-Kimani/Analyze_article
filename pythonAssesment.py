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
    """
    Counts the number of occurrences of search_word in text.
    Case-insensitive.
    Returns an integer.
    """
    if not text or not search_word:
        return 0

    words = re.findall(r'\b\w+\b', text.lower())
    return words.count(search_word.lower())


# Find the most common word in the text

def identify_most_common_word(text):
    """
    Identifies the most common word in text.
    Returns the word as a string.
    Returns None if text is empty.
    """
    if not text.strip():
        return None

    words = re.findall(r'\b\w+\b', text.lower())

    if not words:
        return None

    word_counts = Counter(words)
    most_common = word_counts.most_common(1)

    return most_common[0][0] if most_common else None


# count the average word length in the text


def calculate_average_word_length(text):
    """
    Calculates the average word length.
    Excludes punctuation and special characters.
    Returns a float.
    Returns 0 if text is empty.
    """
    if not text.strip():
        return 0

    words = re.findall(r'\b\w+\b', text)

    if not words:
        return 0

    total_characters = sum(len(word) for word in words)
    return total_characters / len(words)



# calculate the number o paragraghs


def count_paragraphs(text):
    """
    Counts paragraphs based on empty lines.
    Returns an integer.
    Returns 1 if text is empty.
    """
    if not text.strip():
        return 1

    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    return len(paragraphs)


# calculate the number o sentenses


def count_sentences(text):
    """
    Counts sentences based on '.', '!', '?'.
    Returns an integer.
    Returns 1 if text is empty.
    """
    if not text.strip():
        return 1

    sentences = re.findall(r'[.!?]+', text)
    return len(sentences)



# Main function to execute the analysis


def main():
    file_path = "news_article.txt"  
    article_text = read_article(file_path)

    if not article_text:
        print("No article content to analyze.")
        return

    print("\n--- TEXT ANALYSIS RESULTS ---\n")

    # particular word count
    word_to_search = input("Enter a word to search for: ")
    word_count = count_specific_word(article_text, word_to_search)
    print(f"\nThe word '{word_to_search}' appears {word_count} times.")

    # Most Common Word
    most_common = identify_most_common_word(article_text)
    print(f"The most common word is: {most_common}")

    # Average length of words
    average_length = calculate_average_word_length(article_text)
    print(f"Average word length: {average_length:.2f}")

    # Paragraph Count
    paragraph_count = count_paragraphs(article_text)
    print(f"Number of paragraphs: {paragraph_count}")

    # Sentence Count
    sentence_count = count_sentences(article_text)
    print(f"Number of sentences: {sentence_count}")

    print("\n--- END OF ANALYSIS ---\n")


if __name__ == "__main__":
    main()