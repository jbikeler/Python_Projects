class MyObj():
    def __init__(self):
        self._protectedVar = 0
        self.__privateVar = 1

    def getPrivate(self):
        return self.__privateVar
    
    def changePrivate(self, newVar):
        self.__privateVar = newVar
        return self.__privateVar
    

if __name__ == '__main__':
    myTestObj = MyObj()
    print('Protected var is {}.\nPrivate var is {}.\nPrivate is {} after it is changed with a class function.'.format(myTestObj._protectedVar, myTestObj.getPrivate(), myTestObj.changePrivate(5)))
    