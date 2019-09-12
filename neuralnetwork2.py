#Under CC:BY-NC
#Neural network code
import numpy as np
import random


global end_out
#create node class
class Node():
    outputs = []
    inputs = []
    weights = []
    layer = 0
    temp_value = 0
    temp_nums = []
    

#Create the node classes
layer0Objs = []
layer1Objs = []
layer2Objs = []
layer3Objs = []
layer4Objs = []
layer5Objs = []

#generate nodes and place them in the correct layers
objs = [Node() for i in range(100)]
for i in range(0, 24):
    objs[i].layer = 1
    layer1Objs.append(objs[i])
for i in range(25, 50):
    objs[i].layer = 2
    layer2Objs.append(objs[i])
for i in range(51, 75):
    objs[i].layer = 3
    layer3Objs.append(objs[i])
for i in range(76, 99):
    objs[i].layer = 4
    layer4Objs.append(objs[i])
    

#sets up input and output nodes
in_node = Node()
in_node.outputs = layer1Objs
in_node.layer = 0
layer0Objs.append(in_node)

out_node = Node()
out_node.inputs = layer4Objs
out_node.layer = 5
layer5Objs.append(out_node)
objs.append(out_node)


#set up inputs and outputs
for i in layer1Objs:
    i.outputs = layer2Objs
    i.inputs = in_node

for i in layer2Objs:
    i.output = layer3Objs
    i.inputs = layer1Objs

for i in layer3Objs:
    i.outputs = layer4Objs
    i.inputs = layer2Objs

for i in layer4Objs:
    i.inputs = layer3Objs
    i.outputs.append(out_node)
    

#The hidden layers are layers 1-4 with 0 the input and 5 the output.

for i in objs:#Gives the nodes their output weights randomly.
    for j in i.outputs:
        i.weights.append(random.random())


#Now the working of the neural network
        
Desired = 0.5 #The wanted end number
inp = 1 # The number inputed into the first node

difference_cache = []

def reward(difference_cache):#This code calculates the reward for the algorithm.
    desired = 0.5 # Note this is a temp constant that will be replaced later with the real value.
    difference = abs(desired-end_out)
    difference_cache.append(difference)
    #This part of the code essentially draws a graph of all the different values.
    
    
    
    
    
def run(inp):
    in_node.temp_value = inp # This code performs the function of transmiting the data

    for i in layer0Objs:
        temp_idx = 0
        for j in i.outputs:
            j.temp_value = i.temp_value * i.weights[temp_idx] 
            temp_idx += 1

    for i in layer1Objs:
        temp_idx = 0
        for j in i.outputs:
            j.temp_nums.append(i.temp_value*i.weights[temp_idx])
            temp_idx += 1
        
    for i in layer2Objs:
        temp_idx = 0
        for j in i.outputs:
            j.temp_nums.append(i.temp_value*i.weights[temp_idx])
            temp_idx += 1
    
    for i in layer3Objs:
        temp_idx = 0
        for j in i.outputs:
            j.temp_nums.append(i.temp_value*i.weights[temp_idx])
            temp_idx += 1
    
    for i in layer4Objs:
        temp_idx = 0
        for j in i.outputs:
            j.temp_nums.append(i.temp_value*i.weights[temp_idx])
            temp_idx += 1

    #Now all nodes that have data in temp_nums will have it added.
        
    for i in objs:
        for j in i.temp_nums:
            i.temp_value += (j/len(i.temp_nums))
    end_out = out_node.temp_value
    return end_out

#print("The neural network has finished being made. The neural network has ran.")
#print("The final number of",out_node.temp_value)

while True:
    co = input("What do you want to know /do?")
    if co == "help":
        print("train: Trains the algorithm")
    if co == "train":
        print("Training algorithm")
        train_times = int(input("How many times do you want the algorithm to train for."))
        for i in range(0, train_times):
            end_out = run(inp)
        
            
    if co == "kill":
        exit()
    if co == "run1":
        print("Running once.")
        end_out = run(inp)
        print("Final value of output node was",end_out)
        
    
        
        




    
