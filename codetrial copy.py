
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

    def getCount(self): 
        temp = self.headval 
        count = 0
        while (temp): 
            count += 1
            temp = temp.nextval
        return count 


    # Print the linked list
    def listprint(self):
        
        printval = self.headval

        count = 1
        words = ''
        while printval is not None:
            
            if count == self.getCount():
                words += printval.dataval

            else:
                words += (printval.dataval + ',')
                
            printval = printval.nextval
            count += 1
        print(words)

    # Function to add newnode at end of list 
    def Add(self, newdata):
        
        NewNode = Node(newdata)
        if self.headval is None:
            
            self.headval = NewNode
            return
        
        last = self.headval
        
        while(last.nextval):
            
            last = last.nextval
            
        last.nextval=NewNode

        return

    def make_list(self,input):

        word = ''
        firstWord = 0

        for i in input:

            if i != ',':
                word += i
            else:
                if firstWord == 0:
                    self.headval = Node(word)
                    firstWord = 1
                    word=''
                else:
                    self.Add(word)
                    word =''

        self.Add(word)
        return self



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

    def AlphaSortList(self):
        wordval = self.headval
        while wordval is not None:
            item = wordval.dataval

            itemLen = 0 
            for char in item:
                itemLen += 1

            x = itemLen

            li = []

            for i in range (0,x):
                li.append(item[i])

            for i in range(0,x):
                for j in range(0,x):
                    if li[i]<li[j]:
                        temp = li[i]
                        li[i]=li[j]
                        li[j]=temp
            newItem=""
            for i in range(0,x):
                newItem = newItem+li[i]
            wordval.set_data(newItem)
            wordval = wordval.nextval
        self.listprint()
        

inputString = input()

list = SLinkedList()

list.make_list(inputString)
      
list.SortList()

list.ReverseSortList()

list.AlphaSortList()






