# openfile = open("./story.txt","r")
def readfile (filename):
    # reading the files
    with open("./story.txt","r") as openfile:
        read_file = openfile.read()
        print(read_file)
        print("this file is true")

def countwords():
    text = readfile("./story.txt")
    print(text)
    split_text = text.split()
    print(split_text)
    counts-dict()

    for word in split_text
        if word in counts:
            counts[word] +=1
        else: 
            counts[word] =1
    return {"as": 10, "would": 20}
countwords()  