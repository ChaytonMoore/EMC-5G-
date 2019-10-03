#Programme that generates example data for a neural network
#Under CC:BY-NC
import random

GenNum = int(input("How many pieces of data need to be generated."))
Data = []# The place where the generated data will be stored in 2d arrays
for i in range(0, GenNum):
    Cores = random.randint(1, 5)
    Ram = random.randint(1, 5)
    Priority = random.randint(1, 100)
    Time = random.randint(1, 30)
    combined = [Cores,Ram,Priority,Time]
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
        count = 0
        for i in Data:
            w = i[0],i[1],i[2],i[3]
            w = str(w)
            if count == 0:
                print("Replacing")
                w = w.replace("(","")
            elif count == len(Data)-1:
                w = w.replace(")","")

            count += 1
            print(w)
            file.write(w)
        file.close()
    if inp == "kill":
        print("Killing programme")
        break
        exit()
