
def get_text(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_all(text: str) -> int:

    return len(text.split())


def count_individual(text: str) -> dict[str, int]:

    output: dict[str, int] = {}
    for char in text:
        lc_char = char.lower()
        if lc_char in output:
            output[lc_char] += 1
        else:
            output[lc_char] = 1

    return output

def main():

    text = get_text("books/frankenstein.txt")
    print(count_all(text))

    print(count_individual(text))

main()
