class Pet:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.age = 0

    def setName(self, n):
        self.name = n

    def setType(self, t):
        self.type = t

    def setAge(self, a):
        self.age = a

    def getName(self):
        return self.name
    
    def GetType(self):
        return self.type

    def getAge(self):
        return self.age
    
def main():
    inputName = input("Eneter a pet name: ")
    inputType = input("Enter a pet type: ")
    inputAge = int(input("Enter a pet age: "))

    Animal = Pet()
    Animal.setName(inputName)
    Animal.setType(inputType)
    Animal.setAge(inputAge)

if __name__ == "__main__":
    main()