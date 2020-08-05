class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.head = None

    def find(self, value):
        
        while self.head is not None:
            if self.head.value == value:
                return self.head
            
            self.head = self.head.next

        return None

    def delete(self, value):

        # Special case of deleteing head
        
        if self.head.value == value:
            self.head = self.head.next
            return self.head

        # General case of deleting internal node

        while self.head is not None: 
            if self.head.next.value == value: ## found it
                self.head.next = self.head.next # cut it out
                return self.head # Return delted node
            else:
                self.head = self.head.next
                self.head.next = self.head.next.next 
        
        return None # nothing was found

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def insert_or_overwrite_value(self, value):
        node = self.find(value)

        if node is None:
            #make new node
            self.insert_at_head(node(value))

        else:
            #overwrite old value
            node.value = value
            


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8




class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.size = 0
        self.hash_table = [None] * self.capacity
        
        
        



    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        
        k = self.get_num_slots()
        n = self.size
        return n / k


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass
        


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        
        if self.hash_table[index] is None:
            
            self.hash_table[index] = HashTableEntry(key,value)

        else:
            table = self.hash_table[index]

            while table is not None:
                if table.key == key:
                    table.value = value
                    return

                if table.next == None:
                    table.next = HashTableEntry(key, value)
                    return

                table = table.next





        
                




    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        self.put(key, None)
        self.size -= 1

      


                    
             


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)

        table = self.hash_table[index]
        while table != None:
            if table.key == key:
                return table.value
            table = table.next 

        return None

        

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_table = self.hash_table
        old_capacity = self.capacity

        self.hash_table = [None] * new_capacity
        self.capacity = new_capacity

        for index in range(old_capacity):
            pos = old_table[index]
            while pos != None:
                self.put(pos.key, pos.value)
                pos = pos.next





if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
