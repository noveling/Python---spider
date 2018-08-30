#__author__="noveling"
import os

def loadstr(word="None",filename="default"):
    if not os.path.exists("./content"):
        os.mkdir("./content")
    f=open("./content/"+filename+".txt","a")
    f.write(word)
    f.close()

if __name__ == "__main__":
    loadstr()
