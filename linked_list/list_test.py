import linked_list as LL

L = LL.LinkedList()
L.insert(1)
L.insert(2)
L.insert(3)
L.insert(4)
L.insert(5)
L.print_all()
print("-----")

# delete 2 elements
L.delete()
L.delete()
L.print_all()
print("-----")

# delete to have 1 remaining element
L.delete()
L.delete()
L.print_all()
print("-----")

# delete last element (now empty list)
L.delete()
L.print_all()
print("-----")




