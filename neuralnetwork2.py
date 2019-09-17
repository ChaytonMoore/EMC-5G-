#Under CC:BY-NC
#Neural network code
import numpy as np
import random
import datetime


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
in_layers = [layer5Objs,layer4Objs,layer3Objs,layer2Objs,layer1Objs,layer0Objs]

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
        
Desired = 1 #The wanted end number
inp = 1 # The number inputed into the first node

difference_cache = []

def reward(difference_cache):#This code calculates the reward for the algorithm.
    desired = 1 # Note this is a temp constant that will be replaced later with the real value.
    difference = abs(desired-end_out)
    difference_cache.append(difference)
    #This part of the code essentially draws a graph of all the different values.

def save_weights(in_layers):#Saves the weights, it has increadibly high demands.
    save_data = []
    save_entry = []
    for i in in_layers: # for every layer
        for j in i: # for each of the nodes in each of the layers
            for n in j.weights: # for each of the weights
                save_entry.append(n)
            save_entry2 = [i,j,save_entry]
            save_data.append(save_entry2)
    file = open("tempnodes.nnws","w")
    file.write(str(save_data))
    print("The node weights have been saved.")
    
    
#def backprop():
    
    
    
def run(inp):
    in_node.temp_value = inp # This code performs the function of transmiting the data
    for i in objs:
        i.temp_value = 0
        i.temp_nums = []
    in_node.temp_value = 1#This is only temp code for testing temp_value can be different

    for i in layer0Objs:
        temp_idx = 0
        for j in i.outputs:
            j.temp_value = i.temp_value * i.weights[temp_idx] #The prolem is that the temp_values need to be set for the next row or 0 is the result of multiplying 0 and the weight.
            temp_idx += 1
            

    for i in layer1Objs:
        for n in i.temp_nums:
            i.temp_value += n
        i.temp_nums = []
        temp_idx = 0
        for j in i.outputs:
            j.temp_nums.append(i.temp_value*i.weights[temp_idx])
            temp_idx += 1
        
    for i in layer2Objs:
        for n in i.temp_nums:
            i.temp_value += n
        i.temp_nums = []
        temp_idx = 0
        for j in i.outputs:
            j.temp_nums.append(i.temp_value*i.weights[temp_idx])
            temp_idx += 1
    
    for i in layer3Objs:
        for n in i.temp_nums:
            i.temp_value += n   
        temp_idx = 0
        for j in i.outputs:
            j.temp_nums.append(i.temp_value*i.weights[temp_idx])
            temp_idx += 1
    
    for i in layer4Objs:
        for n in i.temp_nums:
            i.temp_value += n
        temp_idx = 0
        for j in i.outputs:
            j.temp_nums.append(i.temp_value*i.weights[temp_idx])
            temp_idx += 1
    
    for i in layer5Objs:
        for n in i.temp_nums:
            i.temp_value += n

    #Now all nodes that have data in temp_nums will have it added.
        
   # for i in objs:
      #  for j in i.temp_nums:
           # i.temp_value += (j)
    end_out = out_node.temp_value # might be a problem with setting the value of the output to something else
    
    
    
    return end_out

while True:
    co = input("What do you want to know /do?")
    if co == "help":
        print("train: Trains the algorithm")
        print("kill: Kills the current code for resets.")
    if co == "train":
        print("Training algorithm")
        train_times = int(input("How many times do you want the algorithm to train for."))
        datetime_object = datetime.datetime.now()
        for i in range(0, train_times):
            end_out = run(inp)#runs the network once
            dif = abs(end_out-Desired)#finds the difference
            #it needs to be able to save the current layout of the weights
            in_layers = [layer5Objs,layer4Objs,layer3Objs,layer2Objs,layer1Objs,layer0Objs]
            #save_weights(in_layers) Commented because of lag and high storage usage
            
            print(dif)
            print(end_out,"Actual output")
            #Back prop start#
            for l in in_layers: #For every single layer in the network
                for j in l: #For every single node in the layer
                    for n in 
                    
                    
            
            
        datetime_object2 = datetime.datetime.now()
        print("Time taken was",datetime_object2 - datetime_object)

            
        
            
    if co == "kill":
        break
        exit()
    if co == "run1":
        print("Running once.")
        end_out = run(inp)
        print("Final value of output node was",end_out)
        print("The difference between the desired and actual num was", abs(Desired- end_out))