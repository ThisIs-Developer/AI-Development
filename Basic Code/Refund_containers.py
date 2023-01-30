Less_one_litter = 0.10
More_one_litter = 0.25
less=int(input("How many containers one litre or less: ")) 
more=int(input("How many containers more than one litre: ")) 
refund = less * Less_one_litter + more * More_one_litter
print ("Refund: $%.2f."%refund)