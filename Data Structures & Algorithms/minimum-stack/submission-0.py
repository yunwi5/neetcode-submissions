class MinStack:

    def __init__(self):
        self.__elements = []
        self.__minElements = []

    def push(self, val: int) -> None:
        self.__elements.append(val)
        if self.__minElements:
            newMin = min(self.__minElements[-1], val)
            self.__minElements.append(newMin)
        else:
            self.__minElements = [val]
        

    def pop(self) -> None:
        if not self.__elements:
            return

        self.__elements.pop()
        self.__minElements.pop()
        

    def top(self) -> int:
        if not self.__elements:
            return None
        
        return self.__elements[-1]
        

    def getMin(self) -> int:
        if not self.__minElements:
            return None

        return self.__minElements[-1]
        
