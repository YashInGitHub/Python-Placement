class Super:
    
    #public data member (default)
    var1 = None

    #protected data member
    _var2 = None

    #private data memeber
    __var3 = None

    #Constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    #Public member function
    def displayPublicMember(self):
        #Accessing public data member
        print("Public Data Member: ", self.var1)
    
    #Protected member function
    def _displayProtectedMember(self):
        #Accessing protected data member
        print("Protected Data Member: ", self._var2)

    #Private member function
    def __displayPrivateMember(self):
        #Accessing private data member
        print("Private Data Member: ", self.__var3)
    
    #Public member function
    def accessPrivateMembers(self):
        #Accessing private member function
        self.__displayPrivateMember()

class Sub(Super):

    #Constructor
    def __init__(self, var1, var2, var3):
        Super.__init__(self, var1, var2, var3)

    #Public member function
    def accessProtectedMembers(self):
        #Accessing protected member functions of super class
        self._displayProtectedMember()

obj = Sub("Hello", "all", "People")

#Calling public member functions of all class
obj.displayPublicMember()
obj._displayProtectedMember()
obj.__displayPrivateMember()

#Object can access protected member
print("Object is accessing protected member: ", obj._var2)

#Object can not access private member, so it will generate attribute



    