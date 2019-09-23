
# Python program to check if a string 
# contains any special character 
  
# import required package 
import re 
  
# Function checks if the string 
# contains any special character 
def run(string): 
  
    # Make own character set and pass  
    # this as argument in compile method 
    regex = re.compile('[!]') 
      
    # Pass the string in search  
    # method of regex object.     
    if(regex.search(string) == None): 
        print("String is accepted") 
          
    else: 
        print("String is not accepted.") 
      
  
# Driver Code 
if __name__ == '__main__' : 
      
    # Enter the string 
    string = "Geeks!For!Geeks"
      
    # calling run function  
    run(string) 



'''If the character in the string is an even number then execute the search for Three
Exclimation points IF and only if there are 3 exclimation points found then proceed to search for another
even number. If another even number is found return TRUE, ELSE false.'''   






