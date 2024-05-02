class BoundedStack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.items = []

    def push(self, items):
        if len(self.items) < self.capacity:
            self.items.append(items)
            return True
        else:
            print("Stack is full, cannot push more items.")
            return False
    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            print("Stack is empty, cannot pop.")
            return None

    def peek(self):
        if self.stack:
            return self.items[-1]
        else:
            print("Stack is empty, cannot peek.")
            return None

    def is_empty(self):
        """
        Check if the flask is empty.

        Returns:
        - bool: True if the flask is empty, False otherwise.
        """        
        return len(self.items) == 0

    def is_full(self):
        """
        Check if the flask is full.

        Returns:
        - bool: True if the flask is full, False otherwise.
        """        
        if len(self.items) == self.capacity :
            return True
        return False

    def is_sealed(self):
        """
        Check if the flask is sealed.

        Returns:
        - bool: True if the flask is sealed, False otherwise.
        """        
        if len(self.items) == 3:
            top_chemical = self.items[-1]
            below_top = self.items[-2]
            second_below_top = self.items[-3]
            if top_chemical == below_top == second_below_top:
                return True
        return False

    def __str__(self):
        return "|".join(self.items)
