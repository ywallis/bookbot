import sys
from utils import count_all, count_individual, report

def get_text(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    title: str = sys.argv[1]
    text = get_text(title)
    print(f"--- Begin report of {title} ---")
    
    print(f"{count_all(text)} words found in the document\n")

    chars = count_individual(text)
    report(chars)

    print("--- End report ---")

main()
