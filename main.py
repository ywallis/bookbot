
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

def report(input_dict: dict[str, int]):

    # for key, val in input_dict.items():
    #     print(f"The '{key}' character was found {val} times")
    dict_list = [{'char': key, 'count': val} for key, val in input_dict.items() if key.isalpha()]
    
    output_list = sorted(dict_list, reverse=True, key=lambda x: x['count'])

    for item in output_list:
        print(f"The '{item['char']}' character was found {item['count']} times")

    

def main():

    print("--- Begin report of books/frankenstein.txt ---")

    text = get_text("books/frankenstein.txt")
    
    print(f"{count_all(text)} words found in the document\n")

    chars = count_individual(text)
    report(chars)

    print("--- End report ---")

main()
