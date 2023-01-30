#Widgets=75 grams
#Gizmos=112 grams
Widgets=int(input("Enter your number of Widgets: "))
Gizmos=int(input("Enter your number of Gizmos: "))
weight_of_widgets= Widgets*75
weight_of_gizmos= Gizmos*112
totalWeight= weight_of_widgets + weight_of_gizmos
print ("The total weight of the order: ",totalWeight,"grams")