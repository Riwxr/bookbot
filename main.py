import sys

from stats import get_book_text, get_count_perletter, get_num_words, sort_letter_count

if len(sys.argv) != 2:
    sys.exit("Usage: python3 main.py <path_to_book>")


def main():
    path = sys.argv[1]
    book_text = get_book_text(path)
    count_perletter = get_count_perletter(book_text)
    num_words = get_num_words(book_text)
    sorted = sort_letter_count(count_perletter)
    print(
        f"============ BOOKBOT ============\nAnalyzing book found at {path}...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------"
    )
    for i in sorted:
        print(f"{i["letter"]}: {i["nums"]}")
    print("============= END ===============")


main()
