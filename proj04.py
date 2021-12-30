###########################################################################################################
#
# CSE 231
# Project 4
#
# Algorithm
#
#   for function get_ch()
#       Ask for input , if the input is empty exit the function
#       Write a while loop if the length != 1, 
#           Aeep asking for input until the length of the input is 1
#       Return the string of length  of 1
#   
#   for function find_state(state,ch)
#       Initialize state as int
#       Initialize ch as string
#       Set initial value of i = 1
#       Create for loop iterating through the string letter
#               Create if - else statements based on the value of state
#                   If state = 1,then the characters of the string has to be h 
#                       if ch[i] = "h" update the value of state and go back to the start of the loop
#                       else assign state to value 5 and break from loop
#                   Keep continuing the if else statements as directed by the project
#                   keep updating the value of state and go back to the start of the loop
#                   And break the for loop if state = 5
#       return the value of state
#
#   for function main()
#       Print function banner and appropriate text directed by the the project
#       Create a string called letter
#       Create a while loop which exits if the input from the user is empty
#          Call function get_ch() and add every character to string letter
#       Call function find_state with parameters (1, letter)
#       Return state from find_state
#       Print letter
#       Print if user is laughing or not depending on the return value for function find_state
########################################################################################################



def print_banner():
    BANNER = '''                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$$o          "$$""$$$$$$""""           o$$$
               $$$$o                                o$$$"
                "$$$$o      o$$$$$$o"$$$$o        o$$$$
                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
                     ""$$$$$oooo  "$$$o$$$$$$$$$"""
                        ""$$$$$$$oo $$$$$$$$$$
                                """"$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$"
                                      "$$$""  '''
    print(BANNER)

def get_ch():
    
    ch = input("Enter a character or press the Return key to finish: ")
    
    if ch == "":
        return ch
    
    if ch != "":
        while len(ch) != 1:
            print("Invalid input, please try again.")
            ch = input("Enter a character or press the Return key to finish: ")
        return ch
                

def find_state(state,ch):
    
    state = int(state)
    ch = str(ch)
    
    i = int(state)
    for i, c in enumerate(ch):
            
        if state == 1:
            if ch[i] == "h":
                state = 2
                continue
            else:
                state = 5
                break
        if state == 2:
            if ch[i] == "a" or ch[i] == "o":
                state = 3
                continue
            else:
                state = 5
                break
        if state == 3:
            if ch[i] == "h":
                state = 2
                continue
            elif ch[i] == "!":
                state = 4
                continue
            else:
                state = 5
                break
        if state == 4:
            if ch[i].isalpha():
                state = 5
                break
            else:
                state = 4
                break
                  
    return state
            

def main():

    print_banner()
    print("I can recognize if you are laughing or not.")
    print("Please enter one character at a time.")
    
    l = get_ch()
    letter = ""
        
    while l!= "":
        letter += l
        l = get_ch()
        
         
    n = find_state(1, letter)
        
    print()
    print("You entered", letter)
    if n == 4:
        return "You are laughing."
    else:
        return "You are not laughing."
            

if __name__ == "__main__":
    print(main())
    
    
    
    
    
    