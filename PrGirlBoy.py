def check_word(word):
    letters = set(word.lower())
    if len(letters) % 2 == 0:
        return "This is a girl"
    else:
        return "This is a boy"

# Example usage
word = input("Enter a word: ")
result = check_word(word)
print(result)
