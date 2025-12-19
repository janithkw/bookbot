import sys
from stats import get_num_words, get_char_count, get_sorted_characters

def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
        
    
    return content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    num_words = get_num_words(book_text)
    char_count = get_char_count(book_text.lower())
    sorted_characters = get_sorted_characters(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_characters:
        char = item["char"]
        if char.isalpha():
            print(f"{char}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()