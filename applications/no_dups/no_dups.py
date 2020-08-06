def no_dups(s):
    # Your code here
    cache = {}
    string=[]

    for words in s.split():
        if words not in cache:
            cache[words] = 1
            string.append(words)

    print(cache)
    return " ".join(string)










if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))