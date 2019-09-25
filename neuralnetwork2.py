#Under CC:BY-NC
#Neural network code
import numpy as np
import random
import datetime
import matplotlib.pyplot as plt


global end_out
#create node class
class Node():
    outputs = []
    inputs = []
    weights = []
    layer = 0
    temp_value = 0
    temp_nums = []

def linsearch(array,find):
    idx = 0
    for i in array:
        if i == find:
            break
    idx += 1
    return idx
            
    
    
    

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
    in_node.temp_value = 1 #This is only temp code for testing temp_value can be different

    for i in layer0Objs:
        temp_idx = 0
        for j in i.outputs:
            j.temp_value = i.temp_value * i.weights[temp_idx] #The problem is that the temp_values need to be set for the next row or 0 is the result of multiplying 0 and the weight.
            temp_idx += 1
            

    for i in layer1Objs:
        for n in i.temp_nums:#So we have created a number from all the other nodes nums sum.
            i.temp_value += n
        #sigmoid equation
        curve = 1/(1+)
        #square root
        root = sqrt(i.temp_value)
        
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
        diff_cache = []
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
            diff_cache.append(dif)
            print(end_out,"Actual output")
            #Back prop start#
           # for l in in_layers: #For every single layer in the network
                #for j in l: #For every single node in the layer
                    #for n in 
          #  for o in range(0, len(objs)-1):
          #       for j in range(0, len(objs[o].weights)-1):
             #        if objs[o].weights[j] > Desired/len(objs):
                #         objs[o].weights[j] = objs[o].weights[j] * 0.999
           
            #Start of new code for advanced back propogation
            paths = []
            temp_path = []
            paths_weights = []
            temp_path_weights = []
            
            #for o in layer5Objs:#For every output node
            #    for j in o.inputs:#For each of the input nodes of the out nodes
               #     temp_inn = linsearch(j.outputs,o)#find the index of the weight/output which the other node is linked to.
               #     temp_path.append([j,temp_inn])#0 = the input/weight index and #1 is the node which it applies to.
                #    paths.append(temp_path)#adds the temp path to the main paths list
                 #   temp_path = []#empties the temp path
            #Currently paths are only a single node deep and are so very basic
            #Now the paths have been created to be trained 
            #What will now happen is the impact that each path has will be determined and then the impact of each node and each weight.
    
            n_c_idx = 0#The node choose index
            for o in layer5Objs:#For every single output node
                temp_c_node = o#Sets the value to the first thing.
                while temp_c_node not in layer0Objs:#While the node it has gone back to isn't an input node. 
                     if type(temp_c_node.inputs) != list:
                         print(type(temp_c_node.inputs))
                         tvar = [] 
                         tvar.append(temp_c_node.inputs)
                         temp_c_node.inputs = tvar
                         print("forcing list")
                     temp_path.append(temp_c_node) #Appends the current node to the path
                     temp_c_node.inputs = list(temp_c_node.inputs)
                     print("Done once.")
                     
                     print(temp_c_node.inputs)
                     #if temp_c_node.layer == 1:#I think this is only temporary until I have many different input nodes 
                     temp_path_weights.append(temp_c_node.inputs[n_c_idx].weights[linsearch(temp_c_node.inputs[n_c_idx].outputs,temp_c_node)])
                     
                     #else:
                         #temp_path_weights.append(temp_c_node.inputs[n_c_idx].weights[linsearch(temp_c_node.inputs[n_c_idx].outputs,temp_c_node)])#Gets the index for the place which the temp node is in the previouses nodes ouputs
                     #Explaination for the previous line
                     #It appends the weight that is needed to the temp_path_weights variable.
                     #It searches for the particular node in the input nodes outputs then feeds that index for the other part to use
                     #to get the weight of the node.
                     temp_c_node = temp_c_node.inputs[n_c_idx]#sets the temp node to the next value
                #The while loop has now finished. And the temp vars will be put into other vars and then emptied
                print("The end of a while loop run.")
                paths.append(temp_path)
                paths_weights.append(temp_path_weights)
                #Now empty the temp vars
                temp_path = []
                temp_paths_weights = []
                
                     
                n_c_idx += 1
            
            print(paths)
            
            for path in paths:
                print(path[0][0])
                node = path[0][0]#This is confusing but neededs
                weight = node.weights[path[0][1]]
                print(weight)#The weights are what is important
               # if weight #I Think I 'll simulate the event of a weight getting a 
                
                
            
            
            
        datetime_object2 = datetime.datetime.now()
        print("Time taken was",datetime_object2 - datetime_object)#outputs time taken
        save_q = input("Do you want to save the difference output as a .nng file.y/n")
        if save_q == "y":#This will save the output of the training in an external file.
            file = open("difference_cache.nng","w")
            file.write(str(diff_cache))
            file.close()

            
        
            
    if co == "kill":
        break
        exit()
    if co == "run1":
        print("Running once.")
        end_out = run(inp)
        print("Final value of output node was",end_out)
        print("The difference between the desired and actual num was", abs(Desired- end_out))
    if co == "draw":
        print("Will now draw a graph of the previous difference data.")
        file = open("difference_cache.nng","r")
        fdata = file.read()
        fdata = fdata.replace("[", "")
        fdata = fdata.replace("]", "")
        data2 = fdata.split(",")
        
        x = []
        for i in range(0, len(data2)):
            x.append(i)
        # corresponding y axis values 
        for i in range(0, len(data2)):
            data2[i] = float(data2[i])
        # plotting the points  
        plt.plot(x, data2) 
          
        # naming the x axis 
        plt.xlabel('iteration') 
        # naming the y axis 
        plt.ylabel('Distance from desired') 
          
        # giving a title to my graph 
        plt.title('Difference graph.') 
          
        # function to show the plot 
        plt.show() 