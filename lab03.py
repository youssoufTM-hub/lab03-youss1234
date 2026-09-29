# Name: Youssouf Tive Madi
# Date: Sep 28, 2026
# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Replace each `pass` with your code, and use `return` to send the answer
# back (not `print`).


def pig_latin(word):
    # TODO (Part 1): return the Pig Latin form of a single lowercase word.
    #   If it starts with a vowel (a, e, i, o, u): add "way" to the end.
    #   Otherwise: move the first letter to the end and add "ay".
    #Check if the letter is a vowel
    vowels: str = "aeiou"
    pig_word1: str = ""
    #if it is then I return the word and way at the end
    if (word[0].lower() in vowels) :
        pig_word1 = word + "way"
        return pig_word1
    #If not then i make an empty list, then I add to it the second letteer
    else:
        pig_list = [""]
        pig_word2: str

        pig_list.append(word[1])
        #then I add all the remaining letters 
        for i in range (2, len(word) , 1):
            pig_list.append(word[i])
        #After that at the end I put toghether the list so it becomes a string, add the first letter as well as ay and I return it
        pig_word2 = "".join(pig_list) + word[0] + "ay"
        return pig_word2 
        


def word_lengths(sentence):
    # TODO (Part 2): return a list with the length of each word in `sentence`
    #   (words are separated by spaces).
    #I make an empty list
    lengths = []
    #for each word in the sentend I add its length to its index in the list
    for word in sentence.split():
        lengths.append(len(word))
    #I return the length list
    return lengths


def reverse_words(sentence):
    # TODO (Part 3): return `sentence` with the order of its words reversed.
    #   e.g. "hello world" -> "world hello"

    #I make an empty list where I'll store the words
    reverse: str [list] = []

    #i put every word in sentence into the list
    for word in sentence.split():
        reverse.append(word)
    #then I reverse the list
    reverse = reverse[::-1]
    rev_words = ""
    #I put the reverse list in a sting and return it 
    for word in reverse:
        rev_words = rev_words + word + " " 

    return rev_words




def letter_counts(text):
    # TODO (Part 4 - STRETCH, optional): return a dictionary mapping each letter
    #   to how many times it appears in `text`. Ignore case, and ignore anything
    #   that isn't a letter.
    #I make the dictionary 
    letters = {}
    #For every letter in the text I create a spot in the dictionnary for it and set it to 1 count 
    # but if its already there I just increase the count
    for letter in text.lower():
        if letter.isalpha() == True:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
    return letters


def main():
    # Optional scratch space - use this to try your functions with sample values.
    print(pig_latin("banana"))                    # ananabay
    print(word_lengths("the quick brown fox"))    # [3, 5, 5, 3]
    print(reverse_words("the quick brown fox"))   # fox brown quick the
    print(letter_counts("hello"))                 # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    pass


if __name__ == "__main__":
    main()
