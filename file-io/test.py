import os


def writeData():
    data = "Hello world!"
    with open('text.txt', 'a') as f:
        f.write(data)
        f.close()


def openFile():
    with open('text.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()

if __name__ == "__main__":
    writeData()
    openFile()
