import lru_cache as lru

C = lru.LRUCache(5)
C.process_item(1)
C.process_item(2)
C.process_item(3)
C.process_item(4)
C.process_item(5)
C.print_all()
print("-----")
C.process_item(6)
C.process_item(7)
C.print_all()
print("-----")
C.process_item(8)
C.process_item(9)
C.print_all()
print("-----")


