def writefile():
    f = open("practice.txt", "w+")
    n = int(input("enter number of lines to enter: "))
    for i in range(n):
        c = str(input("add: "))
        d = c +"\n"
        f.write(d)
    f.close()
def swapjava():
    f = open("practice.txt", "r")
    k  = f.readlines()
    b = []
    w = str(input("enter word to swap : "))
    p = str(input("enter swapped word : "))
    for j in k :
        l = j.split()
        p = ""
        for m in l :
            if m == w:
                m = p
            p+= m
            p+=" "
        b.append(p)
    f.close()
    f = open("practice.txt", "w+")
    for i in (b):
        f.write(i)
        f.write("\n")
    f.close()
def wordsearch() :
    f = open("practice.txt", "r")
    c = f.read()
    v = c.split()
    q = str(input("enter word search: "))
    n = 0
    for i in v :
        if i == q:
            n+= 1
    if n > 0 :
        print( q , "exist and occur" , n, "times")
    else :
        print( q , "does not exist")
    f.close()
def occur_first():
    word = input("enter word to find : ")
    with open("practice.txt" , "r") as f:
        c = f.readlines()
        for i in c :
            if i.find(word) != -1:
                print("word found in",c.index(i)+1 , "line")
                break
        else: 
            print("not found")
occur_first()


# choice1 = str(input("select to write(w) , to swap word(e) , or to search word (s)): "))
# if choice1 == "w" or "W ":
#     writefile()
# elif choice1 == "e" or "E":
#     swapjava()
# elif choice1 == "s" or "S" :
#     wordsearch()
# else :
#     print("Error.......choose a valid option ")
