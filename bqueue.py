class BoundedQueue:
    # Creates a new empty queue:
    def __init__(self, capacity):
        assert isinstance(capacity, int), ('Error: Type error: %s' % (type(capacity))) # throws an assertion error on not true
        assert capacity >= 0, ('Error: Illegal capacity: %d' % (capacity))
        self.__items = [] # init the  list / queue as empty
        self.__capacity = capacity

    # Adds a new item to the back of the queue, and returns nothing:
    def enqueue(self, item):
        '''
        Enqueue the element to the back of the queue
        :param item: the element to be enqueued
        :return: No returns
        '''

        if len(self.__items) >= self.__capacity:
            raise Exception('Error: Queue is full')
        self.__items.append(item)


    def dequeue(self):
        '''
        Dequeue the element from the front of the queue and return it
        return: The object that was dequeued
        '''

        if len(self.__items) <= 0:
            raise Exception('Error: Queue is empty')
        return self.__items.pop(0)
    
    
    def isEmpty(self):
            return len(self.__items) == 0
    
    def isFull(self):
        return len(self.__items) == self.__capacity

    def size(self):
        return len(self.__items)

    def capacity(self):
        return self.__capacity

    def __str__(self):
        return str(self.__items)
        
