
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# end class node

class List:
    def __init__(self):
        self.head = None
    
    # to get length of linkedlist
    def get_length(self):
        if self.head == None:
            return 0

        else:
            len = 1
            itr = self.head
            while(itr.next != None):
                itr = itr.next
                len = len + 1
               
            return len

    # for printing linked list
    def print_list(self):
        if self.head == None:
            print('')

        else:
            itr = self.head
            print(itr.data, end='')
            while(itr.next != None):
                itr = itr.next
                print(', ' + str(itr.data),end='')
               
# end class List
# singly connected simple linked list


# fucntion to create list from given array input
def create_list(arr):
    if len(arr) < 0:
        return None
        
    elif len(arr) == 0:
        return List() # return emtpy list
        
    else:    
        list = List()
        for i in range(0, len(arr)):
            if i == 0:
                list.head = Node(arr[i])

            else:
                itr = list.head
                while (itr.next != None):
                    itr = itr.next
                itr.next = Node(arr[i]) # add nodes from array to linked list

        return list

# function to remove nth node from the end of the given list           
def remove_node(list, n):

    if list.get_length() == 1:
        list.head = None # emtpy list if only 1 element
        
    else:    
        position = list.get_length() - n
        itr = list.head
        for i in range (position - 1):
            itr = itr.next
        itr.next = itr.next.next

    return list


# Driver code
if __name__ == "__main__":
    
    arr = [1, 2, 3, 4, 5]
    print('Original linked list: ', end='')
    list1 = create_list(arr) # create linked list from array input
    list1.print_list()

    print('\nNew linked list: ', end='')
    list1 = remove_node(list1,2) # call remove_node function to remove nth node from the end of list list
    list1.print_list()
