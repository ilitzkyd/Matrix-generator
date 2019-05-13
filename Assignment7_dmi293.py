import random as ran
from string import punctuation

def take_symbol(s):
    return ''.join(c for c in s if c not in punctuation)

def word_char(dictionary, word):
    print("Word count of \"" + word + "\" is:", dictionary[word])

    
stop_words = ["a","am","an", "and","are", "as", "at",
              "be","but", "by", "for", "i", "if", "in", "into",
              "is", "it", "its", "my", "nor", "not", "of", "on",
              "or", "so", "than", "that", "the", "then", "this",
              "to", "too", "will", "with"]

#1
def matrix_count(rows,columns):
    mat = []
    for r in range(0, rows):
        row = []
        for c in range(0, columns):
            val = ran.randint(0,1)
            row.append(val)
        mat.append(row)
    return mat



#2
def square_mat(mat):
    columns = len(mat[0])
    num_rows = len(mat)
    first = []
    for i in range(0,columns):
        inc = 0
        for r in range(0,num_rows):
            if mat[r][i] == 1:
                inc += 1
        if inc%2 == 0:
            first.append(i)
    return first



def count_words(raven):
    valword = dict()
    with open(raven,"r") as f:
        for sent in f.read():
            for word in sent.split(" "):
                final = take_symbol(word)      
                final = final.lower()
                print(word,end="")
                if not word in stop_words:
                    if not final in valword:
                        valword[final] = 0
                    valword[final] += 1
            print()
    return valword
    


def find_max(valword):
    high_word = max(valword.keys(), key=lambda x: wordcount[x])
    high_val = valword[high_word]
    return (high_word,high_count)

def main():
    mat = matrix_count(6,6)
    print(mat)
    print(square_mat(mat))
    

    wordcount = count_words("raven.txt")
    maxtuple = find_max(valword)
    word_char(wordcount, maxtuple[0])
    word_char(valword, "raven")
    word_char(valword, "nevermore")


main()

                
