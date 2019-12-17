#Chesterfield's genetic code
#Chesterfield was helped named by Aziz
import random
import datetime
import matplotlib.pyplot as plt
import math                    
                 
global end_out
global TotalWaitTime #This variable is the total time that is waited by requests, perhaps waited by importance.

global RAM_Usage# These two variables are the total usuage of the RAM and CPU
global CPU_Usage

global step #The current time step the neural network is on.
step = 0
RAM_Usage = []
CPU_Usage = []

for i in range(0, 32): #This will fill up the values for the usage lists
    RAM_Usage.append(0)
    CPU_Usage.append(0)

    

Datalist = [] # Sets up the value of Datalist as empty so the data can be called.

#####SET UP FOR THE CPU AND RAM START######
class Partition():#This class contains the data for the partition of either cpu or RAM
    variant = ""#Either CPU or RAM
    Owner_Id = ""#This is the identifier of which object is the owner.
    usage = False#Whether or not in use, other values should be empty except for variant if this is false


CPUs = [] # These are empty lists for the differet pieces of RAM and CPU
RAM = [] # There now needs to be 32 units of both RAM and CPU
for i in range(0, 32):
    tmp_p_c = Partition()
    tmp_p_c.variant  = "CPU" #This is the code for creating CPUs
    CPUs.append(tmp_p_c)

for i in range(0, 32):
    tmp_p_c = Partition()
    tmp_p_c.variant = "RAM"
    RAM.append(tmp_p_c)

#NOTE: The usage variable is all that is used by the neural network.

#####SET UP FOR THE CPU AND RAM END#######


    

#create node class
class Node():
    outputs = []
    weights = []
    layer = 0
    temp_value = 0
    temp_nums = []

class request():#This class contains the data from the list of needed items
    #Imported data
    priority = 0#1-100 for weighting of rewards
    CPUsReq = 0#number of CPUs required
    RAMReq = 0#number of RAM slots required
    exp_wait = 0#will be made so this is the time that it takes to process.
    
    #Changeable data
    actual_wait = 0
    
    def __init__(self, priority,CPUsReq,RAMReq,exp_wait): #an init function
        self.priority = priority
        self.CPUsReq = CPUsReq
        self.RAMReq = RAMReq
        self.exp_wait = exp_wait


def mean(array):
    total = 0
    for i in array:
        total += i
    try:
        total = total / len(array)
    except:
        print("Error:The list supplied is of length 0")
    
    return total


requests = []
Queue = [] # Very important variable, this is used for the current queue data 


def ImportData(): #This function will populate the requests when called. Takes times to do
    #Read statis is weather to read the file again or just use the d(don't know what this is meant to say)
    print("Will now load request data from file.")
    while True:
        rq_f_n = input("What file do you want to open, include extension.")
        try:
            rq_file = open(rq_f_n,"r")
            break
        except:
            print("Sorry, that file can't be found.")
    rq_data = rq_file.read() # reads the data from the file
    rq_data.replace("(","")  # All of this code cleans the data and readies it for use. 
    rq_data.replace(")","")
    rq_data = rq_data.split(")(")
    outputdata = []
    for entry in rq_data:
        entry = entry.split(",")
        outputdata.append(entry) 
    
    classD = [] #creates an empty list for the use of adding different.
    for i in outputdata: #for every obj in a list
        classD.append(request(i[2],i[0],i[1],i[3]))# Setting up the class for each request.
    return classD#returns the class list to the main programme.
        
def refresh_line(DataList,Queue):#Adds more data to the queue from the file data
    
    for i in range(0,(10 - len(Queue))):
        try: #Sometimes it won't work. I don't care if this is bad practise or not.
            requests.append(DataList[0]) # Adds data to the requests list, Queue in normal code.
            del DataList[0] # Takes the data from the DataList
        except:#If the list isn't the correct length.
            print("There is insufficient data for this, just pray it works.")
            break
    return DataList, requests #This outputs the data from the function
        
        
        
def linsearch(array,find):
    idx = 0
    for i in array:
        if i == find:
            break
    idx += 1
    return idx

def FindImp(result,network,reward,out_node):#Finds the impact of a node on a given neural network result
            #Result = what the network get
            #network = the network itself
            #reward = the value gotten how good it performed should be some value(maybe pos and neg)
            
            
            #What I need to do first is determine each nodes impact on the result
            for i in network:
                for w in i.weights: 
                    #now i need to trace it forwards and determine the impact of each node
                    TargetNode = i#current trace node
                    impact = 1 # what impact the node in particular has on the output
                    while TargetNode not in out_node:#while the target that the trace is on isn't the last one
                        TargetNode.weights[0]
                        
#If you are reading this message, get the hell out of the files                        
#Yeah because I never read my comments it must be an intruder.
                
    
#The input nodes will need to be 5 for each of the different requests that are waiting.
#There will also needs to be a node for each of the different          
    

#NOTE: I am assuming that there will be 32 RAM units and 32 CPU cores.

#Create the node classes
                    ##This is the new code for the neural network##
layer0Objs = [] #Input layer should be 50 for the queue and 24 for RAM and CPU
layer1Objs = []#Roughly a hundred for this layer
layer2Objs = []#Roughly a hundred for this layer
layer3Objs = []#There needs to be 24 outputs nodes
#layer4Objs = [] 
#layer5Objs = []
in_layers = [layer3Objs,layer2Objs,layer1Objs,layer0Objs]

#generate nodes and place them in the correct layers
objs = [Node() for i in range(478)] # 50(Queue) + 64(CPU and RAM) + 300 + 64 :  is the total number of nodes
# There are now 150 nodes in each layer

for i in range(0, 114):
    objs[i].layer = 0
    layer0Objs.append(objs[i])
for i in range(114, 264):
    objs[i].layer = 1
    layer1Objs.append(objs[i])
for i in range(264, 414):
    objs[i].layer = 2
    layer2Objs.append(objs[i])
for i in range(414, 478):
    objs[i].layer = 3
    layer3Objs.append(objs[i])


    #   Note the layers should be first around 50 and then 100 100 then to the number needed.
#set up inputs and outputs
    
for i in range(0, len(layer0Objs)): 
    layer0Objs[i].ouputs = layer1Objs

for i in range(0, len(layer1Objs)): 
    layer1Objs[i].outputs = layer2Objs
    layer1Objs[i].inputs = layer0Objs

for i in range(0, len(layer2Objs)): 
    layer2Objs[i].output = layer3Objs
    layer2Objs[i].inputs = layer1Objs

for i in range(0, len(layer3Objs)):
    layer3Objs[i].inputs = layer2Objs


#The hidden layers are layers 1-2 with 0 the input and 3 the output.
#It used to be there were 6 layers but now there are fewer but more nodes all together

        
for i in range(0, len(objs)): #Gives the nodes their weight values.
    for j in range(0, len(objs[i].outputs)):
        objs[i].weights.append(random.random())


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
    
    
#def undateReqs(Queue):#This code will update the values in the neural network.
    
        


def backprop(neurons,outputs,reward,Lreward):#This is the code that will perfect the neural network
    #Each node needs to have a responsability tied to it.
    reward = Lreward / reward # If the current reward is better will be a value above one if not below.
    layer2Objs = []
    for i in neurons:
        if i.layer == 2:
            layer2Objs.append(i)
    
    #So now I will need to determine the effect each node has on the answer.
    layer2Impacts = []
    layer1Impacts = []
    layer0Impacts = []
    for i in neurons:
        if i.layer == 2:
            layer2Impacts.append(mean(i.weights))

    idx = 0    
    for i in neurons:
        if i.layer == 1:
            tmp_lst = []
            for j in i.outputs:
                tmp_lst.append(layer2Impacts[idx]*i.weights[idx])
            idx += 1
            layer1Impacts.append(mean(tmp_lst))
     
    idx = 0
    for i in neurons:
        if i.layer == 0:
            tmp_lst = []
            for j in i.outputs:
                tmp_lst.append(layer1Impacts[idx]*i.weights[idx])
            idx += 1
            layer0Impacts.append(mean(tmp_lst)) 
            
    #It has now be found what every single node has in terms of impact on the network
    #It now needs to go and edit the weights based on the rewards.
    for i in range(0,len(neurons)):
        if neurons[i].layer == 0:
            for j in range(0, len(neurons[i].weights)):
                editable = (neurons[i].weights[j])*layer0Impacts[i]
                leftover = neurons[i].weights[j]-editable
                editable = editable * reward
                neurons[i].weights[j] = leftover + editable
                
        if neurons[i].layer == 1:
            for j in range(0, len(neurons[i].weights)):
                editable = (neurons[i].weights[j])*layer1Impacts[i]
                leftover = neurons[i].weights[j]-editable
                editable = editable * reward
                neurons[i].weights[j] = leftover + editable
        
        if neurons[i].layer == 2:
            for j in range(0, len(neurons[i].weights)):
                editable = (neurons[i].weights[j])*layer2Impacts[i]
                leftover = neurons[i].weights[j]-editable
                editable = editable * reward
                neurons[i].weights[j] = leftover + editable
                
    #This code should edit the weights of the nodes to a fair degree with the various factors
    
    return neurons
            
            
            
                
        
def run(inp, Datalist):
    # Will now need to load data from the list.
    Queue = []
    
    #in_node.temp_value = inp # This code performs the function of transmiting the data
    #old data entry code ^^^^^^
    
    #The code below loads the requests from the Datalist
    #print(Datalist)
    if Datalist == []: #If the Datalist is empty it will call a function that will open data
        Datalist = ImportData()
    Datalist,Queue = refresh_line(Datalist,Queue)
    
    for i in range(0, len(objs)): #This code cleans the nodes.
        objs[i].temp_value = 0
        objs[i].temp_nums = []
    
    ######## ENTER DATA START ##########
    #print(len(Queue),"This is the Queue data.") # I think this should work
    for i in range(0, 10): # For every single part of the input layer in the first 50
        #This first half of the code gets data for the queue elements
        layer0Objs[i*5].temp_value = Queue[i].priority #This sets the different inputs
        layer0Objs[1+i*5].temp_value = Queue[i].CPUsReq#as inputs for the neural network
        layer0Objs[2+i*5].temp_value = Queue[i].RAMReq
        layer0Objs[3+i*5].temp_value = Queue[i].exp_wait
        layer0Objs[4+i*5].temp_value = Queue[i].actual_wait
    
    #There was code here but it is likely not needed.
        
    ########### ENTER DATA END ##############
    

    #for i in layer0Objs:   # This code is the old code for the stuff above.
        #temp_idx = 0
        #for j in i.outputs:
            #j.temp_value = float(i.temp_value) * i.weights[temp_idx] #The problem is that the temp_values need to be set for the next row or 0 is the result of multiplying 0 and the weight.
           # temp_idx += 1
    for i in range(0, len(layer0Objs)): # I think this new and improved code that should work, works.
        #print(layer0Objs[i].temp_value,"temp value")
        layer0Objs[i].outputs = [] #Cleans the outputs for layer 0
        for n in layer1Objs:#This code should create the outputs things which are needed.
            layer0Objs[i].outputs.append(n) 
        
        
        for j in range(0, len(layer0Objs[i].outputs)):#6/11/19 this code right now isn't running
            layer0Objs[i].outputs[j].temp_nums.append(float(layer0Objs[i].temp_value) * layer0Objs[i].weights[j])
        #The last to lines which I've editted should mean it works.
            
    #print(1/1+(math.e**))
   # print("Test thing")
    #print(math.sqrt(1/(1+(math.e**((0-35)/100)))))
    
    

    for i in range(0, len(layer1Objs)):
        #The code here should get the data from the last layer.
        for n in layer1Objs[i].temp_nums:#So we have created a number from all the other nodes nums sum.
            layer1Objs[i].temp_value += n  #This code won't be running as there is nothing here.      
       # print("before",layer1Objs[i].temp_value)
        #sigmoid equation
        layer1Objs[i].temp_value = math.sqrt(layer1Objs[i].temp_value)
        layer1Objs[i].temp_value = math.sqrt(layer1Objs[i].temp_value)
        #print("val",layer1Objs[i].temp_value)
        curve = 1/(1+(math.e**((0-(layer1Objs[i].temp_value/5)**2))))#Sigmoid graph point calculation
        #print("2 data-",curve)
        #print(curve)
        #print("This is second value",curve)
        #square root
        #root = math.sqrt(curve)
        
        layer1Objs[i].temp_value = curve#This sets the value for the node to be that of the eq
       # print(layer1Objs[i].temp_value,"temp value")
       
        
        layer1Objs[i].temp_nums = []
        temp_idx = 0
        for j in range(0, len(layer1Objs[i].outputs)):
            layer1Objs[i].outputs[j].temp_nums.append(layer1Objs[i].temp_value*layer1Objs[i].weights[temp_idx])
            temp_idx += 1
    
    #someeee = input("c1")
    
    
    #This code should check that actual values are transfered.
    #This code is to see why it is only outputing root 0.5
    #Chesterfield has XY chromosomes hence he is male.
    
        
    for i in range(0, len(layer2Objs)):
        for n in layer2Objs[i].temp_nums:
            layer2Objs[i].temp_value += n
            
        layer2Objs[i].temp_nums = []
        temp_idx = 0
        layer2Objs[i].temp_value = math.sqrt(layer2Objs[i].temp_value)
        layer2Objs[i].temp_value = math.sqrt(layer2Objs[i].temp_value)
        curve = 1/(1+(math.e**(0-layer2Objs[i].temp_value/2)))#Sigmoid graph point calculation
        #square root
        #root = math.sqrt(curve)
        #print("root",root)
        
        layer2Objs[i].temp_value = curve#This sets the value for the node to be that of the eq
        layer2Objs[i].outputs = []
        for j in layer3Objs:
            layer2Objs[i].outputs.append(j)
        for j in range(0, len(layer2Objs[i].outputs)):
            layer2Objs[i].outputs[j].temp_nums.append(layer2Objs[i].temp_value*layer2Objs[i].weights[temp_idx])
            temp_idx += 1
    
    
    for i in range(0, len(layer3Objs)):
        for n in layer3Objs[i].temp_nums:
            layer3Objs[i].temp_value = layer3Objs[i].temp_value + n 
        
        layer3Objs[i].temp_value = math.sqrt(layer3Objs[i].temp_value)
        layer3Objs[i].temp_value = math.sqrt(layer3Objs[i].temp_value)
        
        curve = 1/(1+(math.e**(0-layer3Objs[i].temp_value/2)))#Sigmoid graph point calculation
        #square root     #Since there is now only 4 layers layer 3 is the last
        #root = math.sqrt(curve)
        
        layer3Objs[i].temp_value = curve#This sets the value for the node to be that of the eq    
        temp_idx = 0
        #for j in i.outputs:
            #j.temp_nums.append(i.temp_value*i.weights[temp_idx])
            #temp_idx += 1
        
   
    
   
    #Now all nodes that have data in temp_nums will have it added.
        
   # for i in objs:
      #  for j in i.temp_nums:
           # i.temp_value += (j)
    #print(out_node)
    #print(out_node.temp_value,"last")
    #end_out = out_node.temp_value # might be a problem with setting the value of the output to something else
   
    end_out = []
    for i in layer3Objs: # This code is meant to create a list that is returned
        end_out.append(i.temp_value) #So the end out value is just the layer3 temp values
    
    return end_out,Datalist #Returns the data from run to the main programme

    
while True:
    co = input("What do you want to know /do?")
    if co == "help":
        print("train: Trains the algorithm.")
        print("kill: Kills the current code for resets.")
    
    if co == "train":
        diff_cache = []
        print("Training algorithm")
        train_times = int(input("How many times do you want the algorithm to train for."))
        datetime_object = datetime.datetime.now()
        step = 0 #Set the step to start at 0, the first time step.
        runtimes = 0
        for i in range(0, train_times):
            #This is the code that will get data from a file and read it as the RAM + CPU
            nodeinp = open("out.nnca","r")
            nodedata = nodeinp.read()
            widx = 50
            for i in range(0, 64): #Not yet finished
                layer0Objs[i].temp_value = nodedata[i]
                widx += 1
                
                
            
            end_out,Datalist = run(inp, Datalist)#runs the network once
           # dif = abs(end_out - Desired)#finds the difference # This code doesn't work for the need for a many output network

            #it needs to be able to save the current layout of the weights
            in_layers = [layer3Objs,layer2Objs,layer1Objs,layer0Objs]
            diff_cache.append(0) # Should contain a difference but since the code is very different it can't be fixed.
            print(end_out,"Actual output")
            #Back prop start#
           
            #Start of new code for advanced back propogation
            paths = []
            temp_path = []
            paths_weights = []
            temp_path_weights = []
            #Currently paths are only a single node deep and are so very basic
            #Now the paths have been created to be trained 
            #What will now happen is the impact that each path has will be determined and then the impact of each node and each weight.
    
            n_c_idx = 0#The node choose index
            for o in layer3Objs:#For every single output node  #Changed to layer3 (might not work)
                temp_c_node = o#Sets the value to the first thing.
                while temp_c_node not in layer0Objs:#While the node it has gone back to isn't an input node. 
                     if type(temp_c_node.inputs) != list:
                         #print(type(temp_c_node.inputs))
                         tvar = [] 
                         tvar.append(temp_c_node.inputs)
                         temp_c_node.inputs = tvar
                         
                     temp_path.append(temp_c_node) #Appends the current node to the path
                     temp_c_node.inputs = list(temp_c_node.inputs)
                     temp_path_weights.append(temp_c_node.inputs[n_c_idx].weights[linsearch(temp_c_node.inputs[n_c_idx].outputs,temp_c_node)])
                     
                     #Explaination for the previous line
                     #It appends the weight that is needed to the temp_path_weights variable.
                     #It searches for the particular node in the input nodes outputs then feeds that index for the other part to use
                     #to get the weight of the node.
                     temp_c_node = temp_c_node.inputs[n_c_idx]#sets the temp node to the next value
                #The while loop has now finished. And the temp vars will be put into other vars and then emptied
                paths.append(temp_path)
                paths_weights.append(temp_path_weights)
                #Now empty the temp vars
                temp_path = []
                temp_paths_weights = []
                
                     
                n_c_idx += 1
            
                #This should be where data is sent of to the processor
                idx = 0
                dataW = []
                for j in end_out: #These are the values of the layer 3 objs temp values
                 
                    if j > 0.5:#This is when a new slot entry needs to be created
                        dataW.append([])
                        if idx > 31:#if over 31 it is a ram piece else it is a cpu
                            dataW[len(dataW)-1].append("r")
                            dataW[len(dataW)-1].append(Datalist[0].exp_wait)
                            #dataW[len(dataW)-1].append(i)
                        else:
                           # print(len(Datalist))
                            dataW[len(dataW)-1].append("c")#type of thing
                            dataW[len(dataW)-1].append(Datalist[0].exp_wait)#time to process
                           # dataW[len(dataW)-1].append(i) #refnum
                                
                    idx += 1
                
                
                
                
        tmp_idx = 0      
        for i in layer3Objs: # This code will round the code to the nearest whole number
            if i.temp_value < 5:
                layer3Objs[tmp_idx].temp_value = 0
            else:
                layer3Objs[tmp_idx].temp_value = 1
            tmp_idx += 1
        
                
        #Now I need to make the code that writes to the classes
        for i in range(0, 32):#Turning it to a boolean may not be a good idea.
            CPUs[i].usage = bool(layer3Objs[i].temp_value)
            
        tmp_idx = 0
        for i in range(32, 64):
            RAM[tmp_idx].usage = bool(layer3Objs[i].temp_value)
            tmp_idx += 1
        
            
        print("This is the end of thing.")
            
            
        #print("Diffcache",diff_cache)    
        datetime_object2 = datetime.datetime.now()
        print("Time taken was",datetime_object2 - datetime_object)#outputs time taken
        save_q = input("Do you want to save the difference output as a .nng file.y/n")
        if save_q == "y":#This will save the output of the training in an external file.
            file = open("difference_cache.nng","w")
            file.write(str(diff_cache))
            file.close()
        
        if runtimes == 0:
            rewardm1 = datetime_object2 - datetime_object
        step += 1 #This adds one to the step, a programme counter.
        reward0 = datetime_object2- datetime_object
        obj = backprop(objs,0,reward0,rewardm1)
        rewardm1 = reward0
        runtimes += 1
        if runtimes == 0:
            for objectEntity in range(0, len(objs)):
                for weightEntity in range(0, len(objectEntity)):
                    objs[objectEntity].weights[weightEntity] = random.random
                    
            
    
        
            
    if co == "kill":
        break
        exit()
    if co == "run1":
        print("Running once.")
        end_out = run(inp, Datalist)
        print("Final value of output node was",end_out)
        print("The difference between the desired and actual num was", abs(Desired- end_out))
        
    if co == "load":
        f_open = input("which file do you want to open, do not include extension.")
        f_open = f_open + ".5GD"
        file = open(f_open,"r")
        LD = file.read()
        LD = LD.split(")(")
        print(LD)
    
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
    
    if co == "load requests": # Function near start, for populating the Datalist.
        #Will now run a function
        DataList = ImportData()
    
    if co == "view cache": # used for viewing a set of data.
        for i in DataList:#For everything in the data list
            print("For object",i," these are the stats for it.")
            print(i.priority,"The objects priority.")
            print(i.RAMReq,"The requirements for RAM")
            print(i.CPUsReq,"The requirements for CPU")
            print(i.exp_wait,"The time it expects to wait.")
    
    if co == "backprop view":
        print("This dry runs the code for backpropagation")
        for i in range(0, len(objs)):
            for j in range(0, len(objs[i].weights)):
                objs[i].weights[j] = random.random()
        for i in range(0, len(layer0Objs)):
            layer0Objs[i].outputs = layer1Objs
        obj = backprop(objs,0,1,1)
