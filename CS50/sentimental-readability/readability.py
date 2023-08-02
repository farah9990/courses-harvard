# TODO

def main():
    text = input("Text : ")
    text += " "
    L = 0
    S = 0
    X = 0
    grade = 0

    # here we compute
    L = count_letters(text) / count_words(text) * 100
    S = count_sentences(text) / count_words(text) * 100
    X = 0.0588 * L - 0.296 * S - 15.8
    grade = round(X)

    if grade > 16:  # to organize print
        print("Grade 16+")
    elif grade < 1:
        print(" Before Grade 1")
    else:
        print("Grade", grade)


# methods
# to count letter
def count_letters(text):
    letter = 0
    k = len(text)
    i = 0
    for i in range(k):
        if (text[i].isalpha()) == True:
            letter += 1
        i += 1
    return letter


# to count words
def count_words(text):
    word = 0
    k = len(text)
    i = 0
    for i in range(k):
        if text[i].isspace() == True or text[i] == "\0":
            word += 1
        i += 1
    return word


# to count sentences
def count_sentences(text):
    sentence = 0
    k = len(text)
    i = 0
    for i in range(k):
        if text[i] == "!" or text[i] == "." or text[i] == "?":
            sentence += 1
    return sentence


main()
