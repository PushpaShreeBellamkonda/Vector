class person:
    def __init__(self,name,age,place,gen):
        self.name=name
        self.age=age
        self.place=place
        self.gender=gen
    def display(self):
        print(self.name,self.age,self.place,self.gender)
p1=person("pushpa",22,"hyd","F")
p2=person("amar",28,"pnagar","M")
p3=person("nithin",26,"phill","M")
p1.display()
p2.display()
p3.display()