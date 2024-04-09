from collections import OrderedDict

#Create an ordered dict
Ordered_Dict=OrderedDict([('b',2),('c',3),('d',4)])

#Item to insert in the beginning
new_item=('a',1)

#Create a new Ordered Dict with new item as first element
new_ordered_dict=OrderedDict([new_item])

#Merge the new ordered dict with the original ordered dict
new_ordered_dict.update(Ordered_Dict)

#print the updated ordered dict
print("Updated OrderedDict: ",new_ordered_dict)