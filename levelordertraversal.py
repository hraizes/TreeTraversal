def levelorder(tree): 
    keys = Queue() #create Queue to process nodes
    keys.enqueue(tree) #enqueue root node
    while not keys.isEmpty(): #while queue is not empty
        print(keys.items[-1].getRootVal(), end = '') #display data of front node
        node = keys.dequeue() #remove front node from Queue
        if node.getLeftChild() != None: 
            keys.enqueue(node.getLeftChild()) #add left child to rear
        if node.getRightChild() != None:
            keys.enqueue(node.getRightChild()) #add right child to rear
