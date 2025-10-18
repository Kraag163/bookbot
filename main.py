from stats import count_book_words, count_characters, list_of_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_name = sys.argv[1]
    content = get_book_text(file_name)
    num_words = count_book_words(content)
    num_chars = count_characters(content)
    dic = list_of_dict(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_name}...")
    print("----------- Word Count ----------")
    print("Found",num_words, "total words\n--------- Character Count -------")
    for x in dic:
        line = f"{x["char"]}: {x["num"]}"
        print(line)
    print("============= END ===============")
    
main()
