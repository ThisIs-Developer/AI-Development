# An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos in an order from the user. Then your program
# should compute and display the total weight of the order.

#Widgets=75 grams
#Gizmos=112 grams
Widgets=int(input("Enter your number of Widgets: "))
Gizmos=int(input("Enter your number of Gizmos: "))
weight_of_widgets= Widgets*75
weight_of_gizmos= Gizmos*112
totalWeight= weight_of_widgets + weight_of_gizmos
print ("The total weight of the order: ",totalWeight,"grams")
