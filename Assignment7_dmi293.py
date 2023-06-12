import random as ran
from string import punctuation

def take_symbol(s):
    return ''.join(c for c in s if c not in punctuation)

def word_char(dictionary, word):
    print("Word count of \"" + word + "\" is:", dictionary[word])

    
stop_words = ["a", "am", "an", "and", "are", "as", "at",
              "be", "but", "by", "for", "i", "if", "in", "into",
              "is", "it", "its", "my", "nor", "not", "of", "on",
              "or", "so", "than", "that", "the", "then", "this",
              "to", "too", "will", "with"]

# 1. Generate a matrix with random values of 0s and 1s
def matrix_count(rows, columns):
    mat = []
    for r in range(rows):
        row = []
        for c in range(columns):
            val = ran.randint(0, 1)
            row.append(val)
        mat.append(row)
    return mat

# 2. Find the columns in the matrix with an even number of 1s
def square_mat(mat):
    columns = len(mat[0])
    num_rows = len(mat)
    first = []
    for i in range(columns):
        inc = 0
        for r in range(num_rows):
            if mat[r][i] == 1:
                inc += 1
        if inc % 2 == 0:
            first.append(i)
    return first

# Count the occurrences of words in a file
def count_words(filename):
    wordcount = {}
    with open(filename, "r") as f:
        for line in f:
            for word in line.split():
                word = take_symbol(word)
                word = word.lower()
                print(word, end=" ")
                if word not in stop_words:
                    wordcount[word] = wordcount.get(word, 0) + 1
            print()
    return wordcount

# Find the word with the highest count in the dictionary
def find_max(wordcount):
    high_word = max(wordcount, key=wordcount.get)
    high_count = wordcount[high_word]
    return high_word, high_count

def main():
    mat = matrix_count(6, 6)
    print(mat)
    print(square_mat(mat))

    wordcount = count_words("raven.txt")
    maxtuple = find_max(wordcount)
    word_char(wordcount, maxtuple[0])
    word_char(wordcount, "raven")
    word_char(wordcount, "nevermore")

main()
