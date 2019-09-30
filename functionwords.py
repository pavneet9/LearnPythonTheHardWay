# Practice Session

# Function to split words
def split_words(words):
    """This function splits words"""
    return words.split(" ")

# function to sort words
def sort_words(words):
    """This function sorts words in a sentence"""
    return sorted(words)

# function to find the first words
def first_words(words):
    return words.pop(0)

# function to find the last word
def last_words(words):
    return words.pop(-1)

def first_and_last_sentence(sentence):
    first = first_words(split_words(sentence))
    last  = last_words(split_words(sentence))
    return first

first = first_and_last_sentence(" This is a sentence")
print first
