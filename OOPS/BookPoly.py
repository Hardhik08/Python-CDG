class AddPages:
    def Book1(self,pages1):
        self.pages1 = pages1
    def Book2(self,pages2):
        self.pages2 = pages2
    def Book3(self,pages3):
        self.pages3 = pages3
    def __add__(self,others):
        a = self.pages1+others.pages2
        b = a+others.pages3
        return b


addpages = AddPages()
addpages.Book1("Har")
addpages.Book2("dhi")
addpages.Book3("k")
print(addpages.__add__(addpages))


 
