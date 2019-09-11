#Programme that generates example data for a neural network
#Under CC:BY-NC
import random

GenNum = int(input("How many pieces of data need to be generated."))
Data = []# The place where the generated data will be stored in 2d arrays
for i in range(0, GenNum):
    Cores = random.randint(1, 5)
    Ram = random.randint(1, 5)
    combined = [Cores,Ram]
    Data.append(combined)

print("The data has been generated.")
while True:
    inp = input("What do you want to do.")
    if inp == "view":
        print("Viewing data.")
        for i in Data:
            print(i)
        print("Data view finish.")
    if inp == "save":
        DName = input("What do you want the file to be called. Note: Don't include file type.")
        DName = DName +".5GD"
        file = open(DName,"w")
        for i in Data:
            w = (i[0],",",i[1],"|")
            file.write(str(w))
        file.close()
    