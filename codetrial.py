## OF course this can be done in minimal lines using built in functionality
## Below is an example of this:
##l=input().split(',')
##
##a=[]
##
##while l:a+=[l.pop(l.index(min(l)))]
##
##reversed_strings=[x[::-1] for x in a]
##
##alph_strings=[]
##
##
##print(','.join(a))
##
##print(','.join(reversed_strings))


class Node:
    
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

    def set_data(self, dataval):
        self.dataval = dataval
	
    def get_data(self):
        return self.dataval
    
    def set_next(self, nextval):
        self.nextval = nextval
	
    def get_next(self):
        return self.nextval

class SLinkedList:
    
    def __init__(self):
        self.headval = None

    # Print the linked list
    def listprint(self):
        
        printval = self.headval

        count = 1
        words = ''
        while printval is not None:
            
            if count == 10:
                words += printval.dataval

            else:
                words += (printval.dataval + ',')
                
            printval = printval.nextval
            count += 1
        print(words)

    # Function to add newnode at end of list 
    def AtEnd(self, newdata):
        
        NewNode = Node(newdata)
        if self.headval is None:
            
            self.headval = NewNode
            return
        
        last = self.headval
        
        while(last.nextval):
            
            last = last.nextval
            
        last.nextval=NewNode


    def SortList(self):
        sorted = False
        
        while not sorted:
            sorted = True
            
            prev = self.headval
            current = self.headval.get_next()
            while current is not None:
                if prev.get_data() > current.get_data():
                    sorted = False
                    temp = prev.get_data()
                    prev.set_data(current.get_data())
                    current.set_data(temp)
                prev = current
                current = current.get_next()
                
        self.listprint()

    def ReverseSortList(self):
        
        wordval = self.headval
        while wordval is not None:
            item = wordval.dataval
            newItem = item[::-1]
            wordval.set_data(newItem)
            wordval = wordval.nextval
        self.listprint()
        

inputString = input("Please input a New String with 10 Words Seperated by Commas:\n")


list = SLinkedList()

wordCount = 0
startChar = 0

while wordCount < 10:
    word = ''
    charCount = 0
    for char in inputString[startChar:]:
        if char == ',':
            charCount += 1
            startChar += charCount
            break 
        else:
            word += char
            charCount += 1
    wordCount += 1
    if wordCount == 1:
        list.headval = Node(word)
    else:
        list.AtEnd(word)

      
##list.listprint()   
list.SortList()

list.ReverseSortList()












       
##    # Function to add node in between 
##    def Inbetween(self,middle_node,newdata):
##        
##        if middle_node is None:
##            
##            print("The mentioned node is absent")
##            
##            return
##
##        NewNode = Node(newdata)
##        
##        NewNode.nextval = middle_node.nextval
##        
##        middle_node.nextval = NewNode

##    # Function to add node At the beginning           
##    def AtBegining(self,newdata):
##        
##        NewNode = Node(newdata)
##
##        # Update the new nodes next val to existing node
##        NewNode.nextval = self.headval
##        self.headval = NewNode

    
    

##list.headval = Node("Mon")
##e2 = Node("Tue")
##e3 = Node("Wed")
##
##list.headval.nextval = e2
##e2.nextval = e3
##
##list.AtBegining("Sun")
##
##list.listprint()



