import string

def get_anagram(word: str, dictionary: list):
    word_size = len(word) + 1
    possible_anagrams_letters = ["".join(sorted(word + c)) for c in string.ascii_lowercase]
    possible_words = [
        given_word for given_word in dictionary 
        if len(given_word)==word_size and "".join(sorted(given_word)) in possible_anagrams_letters
    ]
    print(possible_words)

if __name__ == '__main__':
    with open('words_alpha.txt') as f:
        words_reference = f.read().splitlines()
    get_anagram('apple', words_reference)