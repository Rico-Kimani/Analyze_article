import re

def count_specific_word(text, search_word):
    if not text or not search_word:
        return 0
    text = text.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'")
    pattern = r'\b' + re.escape(search_word.lower()) + r'\b'
    matches = re.findall(pattern, text.lower())
    count = 0
    for match in matches:
        count += 1
    return count

def identify_most_common_word(text):
    if not text:
        return None
    text = text.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'")
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    most_common = None
    max_count = 0
    for word in word_count:
        if word_count[word] > max_count:
            max_count = word_count[word]
            most_common = word
    return most_common

def calculate_average_word_length(text):
    if not text:
        return 0
    text = text.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'")
    words = re.findall(r'\b\w+\b', text)
    if len(words) == 0:
        return 0
    total_length = 0
    for word in words:
        total_length += len(word)
    return total_length / len(words)

def count_paragraphs(text):
    if text == "":
        return 1
    paragraphs = text.strip().split("\n\n")
    count = 0
    i = 0
    while i < len(paragraphs):
        if paragraphs[i].strip() != "":
            count += 1
        i += 1
    return count if count > 0 else 1

def count_sentences(text):
    if text == "":
        return 1
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]
    return len(sentences) if sentences else 1

if __name__ == "__main__":
    print("=" * 50)
    print("📰 NEWS ARTICLE ANALYZER")
    print("=" * 50)
    print("\nEnter your news article (press Enter twice to complete prompt):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    article = "\n".join(lines)
    if not article.strip():
        print("\n❌ No article entered. Exiting.")
        exit()
    search_word = input("\nEnter the word you want to count: ")
    word_count = count_specific_word(article, search_word)
    common_word = identify_most_common_word(article)
    avg_length = calculate_average_word_length(article)
    para_count = count_paragraphs(article)
    sent_count = count_sentences(article)
    print("\n" + "=" * 50)
    print("📊 ANALYSIS RESULTS")
    print("=" * 50)
    print(f"📝 Specific Word Count: {word_count}")
    print(f"🏆 Most Common Word: '{common_word}'")
    print(f"📏 Average Word Length: {avg_length:.2f}")
    print(f"📄 Paragraph Count: {para_count}")
    print(f"📑 Sentence Count: {sent_count}")
    print("=" * 50)