def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        counter = 0
        for file in file_contents.split():
            counter += 1

        print(counter)
main()
