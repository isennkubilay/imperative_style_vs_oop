#Imperative style

# our_list = [1,2,3]
# for item in our_list:
#     print(f'Item {item}')

##OOP Style
 
class PrintList:
    def __init__(self,numberlist):
        self.numberlist = numberlist
    def print_list(self):
        for item in self.numberlist:
            print(f'Item {item}')
A = PrintList([1,2,3])
A.print_list()

'''
Python Objects 
number=4 
list_of_numbers =[1,2,4]
'''

'''
number_array = [[1,2,4],[5,6,7]]
'''

'''
df=pd.DataFrame([[1,2,4],[5,6,7]])

'''
