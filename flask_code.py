import os
from bstack import BoundedStack
from bqueue import BoundedQueue

os.system("")       # Enables ANSI escape codes in terminal
    
def clear_screen():
    """
    Clears the terminal screen.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def print_location(x, y, text):
    '''
    Prints text at the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
        - text (str): text to print
    Returns: N/A
    '''
    print ("\033[{1};{0}H{2}".format(x, y, text)) 


def move_cursor(x, y):
    '''
    Moves the cursor to the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
    Returns: N/A
    '''
    print("\033[{1};{0}H".format(x, y), end='')



def display_flasks(flasks,s,d):
    """
    Display the flasks with colors and indices for source and destination.

    Parameters:
    - flasks (list): List of Flask objects.
    - s (int): Index of the source flask.
    - d (int): Index of the destination flask.
    """    
    max_capacity = max(flask.capacity for flask in flasks)
    rows = (len(flasks) + 3) // 4
    ANSI = {
        'AA': '\033[41m',  # Red
        'BB': '\033[44m',  # Blue 
        'CC': '\033[42m',  # Green 
        'DD': '\033[48;5;202m',  # Orange 
        'EE': '\033[43m',  # Yellow 
        'FF': '\033[45m'}  # Magenta   
    
    print("\n\n")

    for row in range(rows):
        for level in range(max_capacity, 0, -1):
            for i in range(row * 4, min((row + 1) * 4, len(flasks))):
                if level == max_capacity and flasks[i].is_sealed() and not flasks[i].is_empty():
                    print('+--+ ', end='')
                elif level <= len(flasks[i].items):
                    # Print item with bg color
                    print(f"|{ANSI[flasks[i].items[level - 1]]}{flasks[i].items[level - 1]:^2}\033[0m| ", end="")  
                else:
                    print("|  | ", end="")
                if i % 4 != 3:
                    print("  ", end="")
            print()
        
        # Print horizontal lines
        for i in range(row * 4, min((row + 1) * 4, len(flasks))):
            print("+--+   ", end="")
        print()
        
        # Print flask indices
        for i in range(row * 4, min((row + 1) * 4, len(flasks))):
            if i == s:
                print(f"\033[31m{i + 1:>3}\033[0m   ", end="")
            elif i == d:
                print(f"\033[32m{i + 1:>3}\033[0m   ", end="")
            else:
                print(f"{i + 1:>3}    ", end="")
        print("\n")        

    print("\n\n")


def play(flasks,num_chem):
    """
    Play the magical flask game.

    Parameters:
    - flasks (list): List of Flask objects.
    - num_chem (int): Number of sealed flasks needed to win the game.
    """    
    game_over = False
    source = None
    dest = None
    while not game_over:
        flask_sealed = 0
        source_selected = False
        clear_screen()  # Assuming this function clears the terminal screen
        print_location(0,1,"Magical Flask Game")
        print_location(0,2,"")
        print_location(0,3,"Select source Flask: ")
        print_location(0,4,"Select destination Flask: ")
        move_cursor(0,3)
        display_flasks(flasks,source,dest)
        move_cursor(0,1)        
        
        while not source_selected:
            move_cursor(0,3)
            source_input = input("Select source Flask: ")
            if source_input.upper() == 'EXIT':
                print_location(0,26,"Game Over")      
                game_over = True
                source_selected = True
            elif source_input.isdigit() and 1 <= int(source_input) <= len(flasks):
                source = int(source_input) - 1
                source_flask = flasks[source]
                source_selected = True
                
                if source_flask.is_empty() or source_flask.is_sealed():
                    move_cursor(0,5)            
                    print("\033[K", end='')     
                    print_location(0,5,"Cannot pour from that flask. Try again.")
                    move_cursor(0,3)
                    print("\033[K", end='')           #clears the line
                    print_location(0,3,"Select source Flask: ")
                    
                    source_selected = False
                else:
                    source_selected = True
            else:
                move_cursor(0,5)
                print("\033[K", end='')                    
                print_location(0,5,"Invalid input. Try again.")
                move_cursor(0,3)
                print("\033[K", end='')           #clears the line
                print_location(0,3,"Select source Flask: ")
      
        if not game_over :
    
            finish = False
            exit = False
          # Select destination flask
            dest_selected = False
            while not dest_selected:
                move_cursor(0,4)
                dest_input = input("Select destination Flask: ")
                if dest_input.upper() == 'EXIT':
                    print_location(0,26,"Game Over")
                    game_over = True
                    dest_selected = True
                elif dest_input.isdigit() and 1 <= int(dest_input) <= len(flasks):
                    dest = int(dest_input) - 1
                    dest_flask = flasks[dest]
                    dest_selected = True
        
                    if dest_flask.is_sealed() or dest_flask.is_full():
                        move_cursor(0,5)
                        print("\033[K", end='')                         
                        print_location(0,5,"Cannot pour into that flask. Try again.")
                        move_cursor(0,4)
                        print("\033[K", end='')           #clears the line
                        print_location(0,4,"Select Destination Flask: ")
                        dest_selected = False
                    elif source == dest:
                        move_cursor(0,5)
                        print("\033[K", end='')                             
                        print_location(0,5,"Cannot pour into the same flask. Try again.")
                        move_cursor(0,4)
                        print("\033[K", end='')           #clears the line
                        print_location(0,4,"Select Destination Flask: ")
                        dest_selected = False
                    else:
                        # Move chemical from source to destination flask
                        chemical = source_flask.pop()
                        dest_flask.push(chemical)
                        move_cursor(0,3)
                        display_flasks(flasks,source,dest)
                        move_cursor(0,3)
                        print("\033[K", end='')                                    
                        move_cursor(0,4)
                        print("\033[K", end='')  
                        move_cursor(0,5)
                        print("\033[K", end='')                        
                        dest_selected = True
                        
                        # Check win conditions
                        for flask in flasks:
                            if flask.is_sealed():
                                flask_sealed+=1
                            if flask_sealed == num_chem:
                                finish=True
                          
                            if finish:      
                                print("You win!")
                                game_over = True
                            elif exit:
                                print("Exiting game.")
                                game_over = True
                        
                else:
                    move_cursor(0,5)
                    print("\033[K", end='')                         
                    print_location(0,5,"Invalid input. Try again.")
                    move_cursor(0,4)
                    print("\033[K", end='')           #clears the line
                    print_location(0,4,"Select Destination Flask: ")
   

def main() :
    clear_screen()      #This clears the screen
  
    with open("chemicals2.txt","r") as file :
        item = file.readline().strip()
        num_flask = int(item[0])
        num_chem = int(item[-1])
    
        x1 = file.readlines()
    
        chemicals = []
        for z in x1 :
            chemicals.append(z.strip())
        
            bq = BoundedQueue(4)
            flasks = [BoundedStack(4) for _ in range(int(num_flask))]
            discarded= []
        for items in chemicals :
            if len(items) != 2 :
                deq = int(items[0]) #num of chemicals it dequeues
                enq = int(items[2]) #which flask it enqueues these items to
                for x in range(deq) :
                    chemical = bq.dequeue()
                    if chemical :
                        flasks[enq-1].push(chemical)
                #print(bq)
                #print(f"{bq} (Dequeue {deq} chemicals and add to flask {enq})")
            else :
                if bq.size() < 4 :
                    bq.enqueue(items)
                    #print(bq)

                else :
                    discarded.append(items)
        #print(bq)
    #display_flasks(flasks)
    play(flasks,num_chem)

if __name__ == "__main__":
    main()