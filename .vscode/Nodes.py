""" 
These are important important information to note about Nodes in Python.
A Node contains data and the data can be of any datatype in python "string, decimals , integer etc"
A node can also have links which can also be referred to as pointers.
A node without a pointer is said to be at the end of its path.

"""
#This is an example of a linked Node
class MyNodes:

    def __init__(self,year,information,linkedNode=None):
        self._year = year
        self._information = information
        self._linkedNode = linkedNode

    def get_year(self):
        return self._year 
    
    def get_information(self):
        return self._information 
    
    def get_linkedNodes(self):
        return self._linkedNode
    
    def set_linkNode(self,link_node):
        self._linkedNode = link_node



firstYear = MyNodes(2017,"I bought a car")
secondYear = MyNodes(2018,"I bought a private Jet")
thirdYear = MyNodes(2019,"I went to paris with fried")


firstYear.set_linkNode(secondYear)
secondYear.set_linkNode(thirdYear)


second_year_data= firstYear.get_linkedNodes().get_information()
third_year_data = secondYear.get_linkedNodes().get_information()


print(second_year_data)  
print(third_year_data)
