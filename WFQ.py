#Input packets as a string, S=Standard, P=Priority, E=Economy
input_packets = ["S Mary", "P Dee", "P Dee", "P Dee", "E Eileen",
"E Mike", "E Joe", "P Dee", "E Vicky", "E George",
"P Dee", "P Joe", "E Sally", "P Joe", "S Pete",
"P Dee", "S Bill", "S Chase", "E Price", "P Dee",
"E Sue"]            #namelist
premium_data = [] #established for later
standard_data = [] #^^
economy_data = []#^^
sorted_queue = []#^^
sorted_names = []#^^
premtimer = 0#^^
stantimer = 0#^^
ecotimer = 0#^^
class Packet:       #packet object
    def __init__(self, type, name):
        self.type = type
        self.name = name
for x in input_packets: #loop to seperate lists
    User = Packet(x[:1],x[2:]) #if its less than the second character, its the type. else, its the name
    if User.type == "P":
        premium_data.append(User.type)
    elif User.type == "S":
        standard_data.append(User.type)
    elif User.type == "E":
        economy_data.append(User.type)

while (len(premium_data) + len(standard_data) + len(economy_data)) != 0: #if the sum of all the data isnt 0 keep going
    while premtimer != 3: #counter
        if len(premium_data) != 0: #if theres more than 0 entries in the premium data list
            sorted_queue.append(premium_data[len(premium_data) - 1]) #add the final entry of the prem list to the sorted list
            premium_data.pop() #get rid of that entry
        premtimer = premtimer + 1 #add to the counter
    while stantimer != 2:
        if len(standard_data) != 0:
            sorted_queue.append(standard_data[len(standard_data) - 1])
            standard_data.pop()
        stantimer = stantimer + 1
    while ecotimer != 1:
        if len(economy_data) != 0:
            sorted_queue.append(economy_data[len(economy_data) - 1])
            economy_data.pop()
        ecotimer = ecotimer + 1
    premtimer = 0 #reset counters
    stantimer = 0
    ecotimer = 0


#establishing name lists
premium_names = []
standard_names = []
economy_names = []

for x in input_packets: #this is all copy - pasted :P --------------------------------------------
    User = Packet(x[:1],x[2:])
    if User.type == "P":
        premium_names.append(User.name)
    elif User.type == "S":
        standard_names.append(User.name)
    elif User.type == "E":
        economy_names.append(User.name)

while (len(premium_names) + len(standard_names) + len(economy_names)) != 0:
    while premtimer != 3:
        if len(premium_names) != 0:
            sorted_names.append(premium_names[len(premium_names) - 1])
            premium_names.pop()
        premtimer = premtimer + 1
    while stantimer != 2:
        if len(standard_names) != 0:
            sorted_names.append(standard_names[len(standard_names) - 1])
            standard_names.pop()
        stantimer = stantimer + 1
    while ecotimer != 1:
        if len(economy_names) != 0:
            sorted_names.append(economy_names[len(economy_names) - 1])
            economy_names.pop()
        ecotimer = ecotimer + 1
    premtimer = 0
    stantimer = 0
    ecotimer = 0
#-----------------------------------------------------------------------------------

print("Names")
print(sorted_names)
print("--------------------")   #to my understanding the order goes 3 prem, 2 stan, 1 eco
print("Packet Types")          #if that's incorrect im sorry, the wordage on this assignment confused me a bit
print(sorted_queue)
#this queue goes first out, if that isnt sufficient with the prompt (im a little unclear how the output
#                                                                         you want is supposed to look)
#i can just flip the list with this
#---------------------------  |
#sorted_names.reverse()     <-|
#sorted_queue.reverse()     <-|
#print(sorted_names)
#print(sorted_queue)
#---------------------------
