#imports
import random
from datetime import datetime


#START ENV setup#
#set up environment
l1 = [0,1,0]
l2 = [0,0,0]
l3 = ["a",0,0]
env = [l1,l2,l3]

dif_cache = []

def log(string):
    log_file = open("training_log.txt","a")
    log_file.write(str(string))
    log_file.write("\n")

print("Environment")
for i in env:
    print(i)
######END ENV setup ########
#creates the agent class
class Agent(): # this is for the reinforcement learning
    reward = 0
difference = 0

nodes = []#creates an array that will contain all the different nodes

class node():#the node class
    layer = 0 #which layer it is in
    outputs=[] #The other nodes which it will output to
    bra_str = 0.5 # the strength of all of the outputs(uniform currently)
    tempnum = 0#the temp num when ran
    def __init__(self, layer): # sets the layer upon input # runs on start up
        self.layer = layer
    def output_set(self, outputs):# sets the outputs that it iwll have 
        self.outputs = outputs

#nn test
node0 = node(0)#sets layers
node1 = node(1)
node2 = node(2)
nodes.append(node0)#adds them to the node lst
nodes.append(node1)
nodes.append(node2)



for each in nodes:#This code sets up the outputs for each of the nodes. # Currently it is basicwith each node conectting to all on the next layer.
    #print(each.layer)
    if each.layer == 0:
        each.outputs = []
        for i in nodes:
            if i.layer == 1:
                #print(i.layer,"layer")
                each.outputs.append(i)
                #print(each.outputs,"outputs")
                
    if each.layer == 1:
        each.outputs = []
        for l in nodes:
            if l.layer == 2:
                #print(each.outputs,"before")
                #print(l.layer,"layer")
                #print(l,"the layer")
                each.outputs.append(l)
                #print(each.outputs,"outputs")


aim = int(input("What number should the AI aim to get"))#What number does the user want the ai to get to.
start = 1 # This is the number which the nodes will start at
#node output setup



#start of client
while True: #client input and output loop console
  inp = input("Input a command")
  if inp == "read log":
      print("The programe will now read all the different log files from the archieve.")
      nn1 = open("logs.nn1","r")
      log_data = nn1.read()
      print(log_data)
      log_lst = log_data.split("#")
      
      
  if inp == "save_log":
      dateTimeObj = datetime.now()
      print("The log will now be added to a collection of logs called logs.nn1 and logs.txt")
      title = input("What do you want the log to be called.")
      log = open("training_log.txt","r")
      log_data = log.read()
      log.close()
      nn1 = open("logs.nn1","a")
      wdata = ("|",title,"|<",dateTimeObj,">")
      nn1.write(str(wdata))
      nn1.write(str(log_data))
      nn1.close()
      log_txt = open("logs.txt","a")
      wdata = title,"at",dateTimeObj
      log_txt.write(str(wdata))
      log_txt.write(str(log_data))
      log_txt.write("\n")
      log_txt.close()
  if inp == "aim_s":#resets the aim for the ai.
      aim = int(input("What number should the AI aim to get"))
  if inp == "run1":#Runs the ai a single time does not allow for training.
      print("Running a single time")
      end = 0#lets while loop happen
      node_idx = 0#the current idx of the 
      temp_node = nodes[node_idx] # sets the temp node to the node at the index.
      temp_node.temp_num = start # set the first node to 1
      for i in range(0, len(nodes)-1):    #test#while end == 0:#while loop for the setting of nodes
          print(i)
          temp_node = nodes[node_idx]
          for j in temp_node.outputs:
              j.temp_num = temp_node.temp_num * temp_node.bra_str # sets the temp number based on the input number and branch strength
              print(j)
          print("inb")
          node_idx += 1
          temp_node = nodes[node_idx]
          if temp_node.layer == 2:#temp only goes up to the third(idx 2) layer
              end = 1 #end the while loop
              print("Finished")
      print(nodes[len(nodes)-1].temp_num)
  if inp == "train": # code for training the ai
      run_times = 0
      t_times = int(input("How many times do you want to train the ai for?"))#times to train
      log_file = open("training_log.txt","w")#create a file for the 
      log_file.close()
      for atp in range(0, t_times): # this is the same code as above but without the print statements #
          run_times += 1
          end = 0#lets while loop happen
          node_idx = 0#the current idx of the 
          temp_node = nodes[node_idx] # sets the temp node to the node at the index.
          temp_node.temp_num = start # set the first node to 1
          for i in range(0, len(nodes)-1):    #test#while end == 0:#while loop for the setting of nodes
              temp_node = nodes[node_idx]
              for j in temp_node.outputs:
                  j.temp_num = temp_node.temp_num * temp_node.bra_str # sets the temp number based on the input number and branch strength
              node_idx += 1
              temp_node = nodes[node_idx]
              if temp_node.layer == 2:#temp only goes up to the third(idx 2) layer
                  end = 1 #end the while loop
          end_value = nodes[len(nodes)-1].temp_num
          difference = abs(end_value - aim)
          log(difference) #writes the results to a log for later refernce
          dif_cache.append(difference)
          if run_times != 1:
              print("placement")
      log("#") #And end point for the individual log piece.
               
           
            
    

      
      

    
    
