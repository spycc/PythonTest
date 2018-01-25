class Shilei():
    lei_a = 'class var a'
    __lei_b = 'class private var b'

    def __init__(self, id, name, age, school='Default:mohan'):
        self.__id = id
        self.name = name
        self.age = age
        self.school = school
        #print (self.__class__.lei_a)

    def ex_medhot(self):
        print ("shili_medhot")
    
    def __private_medhot(self):
        print ("shilei private medhot")

    def diaoyong(self):
        print ("这是类变量"+self.__lei_b)


    @classmethod
    def __lei_medhot(cls):
        print(cls.__lei_b)
        print ("lei_medhot")

    @staticmethod
    def jing_medhot():
        print ("jing_medhot")

ceshi = Shilei(1,'xiaochong',18)
print (ceshi.age)
print (Shilei.lei_a)
#print (count)
#Shilei.lei_medhot()
#ceshi.lei_medhot()


# Shilei.lei_a = 20
# count2 = ceshi.lei_a
# count3 = Shilei.lei_a
# print(count2)
# print(count3)
