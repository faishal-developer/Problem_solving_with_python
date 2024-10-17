from abc import ABC, abstractmethod

class Document(ABC):
    # static attributes
    hardware="pc"

    @classmethod
    def dummyClassMethod(self):
        return ("class method")

    @staticmethod
    def allHardwareTypes(self):
        return ['pc','mobile','tab']

    @abstractmethod
    def process(self):
        pass

    def type(self):
        return NotImplementedError

class PDFDocument(Document):
    def __init__(self):
        self.__salary=500

    # process must be implemented in child
    def process(self):
        return "Processing PDF document"
    
    def type(self):
        return "pdf"
    
    # getter
    @property
    def salary(self):
        return self.__salary
    
    # setter
    @salary.setter
    def salary(self,value):
        self.__salary=value
    
    
    

pdf = PDFDocument()
pdf.salary=1500
print(pdf.salary)
