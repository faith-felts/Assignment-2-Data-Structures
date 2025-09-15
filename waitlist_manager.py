## Create a Node class to represent each customer in the waitlist
class Node:
  def __init__(self, name):
    self.name = name
    self.next = None
   


# Create a LinkedList class to manage the waitlist

    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    


class LinkedList:
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def remove(self, name):
        current = self.head
        prev = None
        while current:
            if current.name == name:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"{name} has been removed from the waitlist.")
                return
            prev = current
            current = current.next
        print(f"{name} not found.")

    def print_list(self):
        current = self.head
        if not current:
            print("The waitlist is empty.")
        else:
          while current:
            print(current.name)
            current = current.next


    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            waitlist.add_end(name) 

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            waitlist.remove(name)
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
The waitlist works by utilizing a singly linked list. Each name is stored in a node that holds a pointer to 
the next node. The LinkedList class handles all nodes starting with a head. The head is the first node in the 
linked list and serves as the only entry point. When the list is empty, the head is none. The first node added fills
the head. Subsequent nodes are pointed to from the head and down the chain of nodes. If a node is added to the front of the list, the head is replaced. 
Removing a node requires searching through the list for a name and updating the surrounding pointers to skip over the node 
containing the selected name. 
- When might a real engineer need a custom list like this?
An engineer might utilize a linked list when making a queue for workorders.
It would be an ideal use since the workorder information may change frequently
and needs to easily be added and removed. The linked list would allow 
for insertions and deletions without messing with any other elements 
in the list. 
'''
