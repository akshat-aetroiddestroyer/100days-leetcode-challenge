'''object oriented approach(classes and objects)
class-> blueprint contains attribute and methods
object-> instance of the class
static method-> it is a decorator(alag se dikhane k liye decorator use krte h) agar kisi bhi method k upr @staticmethod use kiya to neeche wali function ko koi self ki need nhi h run hone k liye 
'''
# class Factory:
#     a=12  #attribute

#     def hello(self): #method
#         print('hello')
#     print('how r u')
# print(Factory().a)
# Factory().hello()
# class Factory:
#     a=12  #attribute

#     def hello(self): #method
#         print('hello')
# obj=Factory()  #obj  becomes an object who can access anything inside the class till now
# obj2=Factory() 
# print(obj.a)
# obj2.hello()
# obj2.hello()
# '''constructor-
#                 by using constructor jaise hi class ka object bnega constructor run hoga constructor sbse pehele run hota h class mai
# # # class Factory:
#     def __init__(self,material,zips,pockets):
                # print('this is constructor')
#         self.material=material
#         self.zips=zips
#         self.pockets=pockets

# reebok=Factory('leather',3,2)
# class vehicle:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#     def show(self):
#         print(self.name,self.color)
#     @staticmethod
#     def lol():
#         print('this is lol method')
# car1=vehicle('bmw','black')
# car1.lol()
# car1=vehicle('bmw','black')
# car1.show()
'''there are two type of attribute
    1. class attribute-- jo class create hone k just baad bnate h class k andr
    2. instance attribute-- jo attribute method k baad bnate h method k andar'''
# class student:
#     school='dps'
#     @classmethod  #jo sirf class k andr kaam krega
#     def show(cls,newschool):
#         cls.school=newschool
# obj=student
# obj.show('KV')
'''inheritance--> jab ek class dusri class ke sare attribute aur metod ko access kar pae
    1. single level
    2. multi level
    3. hierarchial
    4. multiple
    5. hybrid'''
#single level
# class vehicle:
#     def __init__(self,name):  #dunder method
#         self.name=name
#     def show(self):
#         print('this is vehicle class show method')
# class electricCar(vehicle):
#     def __init__(self, name , battery):
#         super().__init__(name)    #super() use krne se pehele se constructor k andr k parameter inherit kra skte h
#         self.battery=battery
#     def hello(self):
#         print('this is electricCar class...')
# obj=electricCar('bmw',1200)
# # obj.hello()
# #multi level
# class vehicle:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(f'this is vehicle class {self.name}')
# class electric(vehicle):
#     def __init__(self, name , battery):
#         super().__init__(name)
#         self.battery=battery
#     def display(self):
#         print(f'this is electric class {self.name} , {self.battery}')
# class petrol(electric):
#     def __init__(self, name ,battery, mileage):
#         super().__init__(name,battery)
#         self.mileage=mileage

#     def show2(self):
#         print(self.name , self.battery , self.mileage)
# obj=petrol('bmw',1200,12)
# obj.show2()
# obj.display()


#hierarchial level
# class vehicle:
#     name='vehicle' 

#     def show(self):
#         print('this is vehicle class')

# class electric(vehicle):
#     def display(self):
#         print('this is electric class')
# class petrol(vehicle):
#     def greet(self):
#         print('this is petrol class')
# obj=electric()
# obj.show()
# print(obj.name)
#hierarchial level
# class vehicle:
#     def __init__(self,model,brand):
#         self.model=model
#         self.brand=brand

#     def start(self):
#         print(f'{self.model},{self.brand}')

# class electric(vehicle):
#     def __init__(self, model, brand , battery):
#         super().__init__(model, brand)
#         self.battery=battery
#     def show(self):
#             print(f'{self.model},{self.brand},{self.battery}')
# class petrol(vehicle):
#     def __init__(self, model, brand , ltr):
#           super().__init__(model, brand)
#           self.ltr=ltr
#     def greet(self):
#             super().start() #vehicle class ka func pehle run hoga
#             print(f'{self.model},{self.brand},{self.ltr}')


# obj=petrol('M5' , 'BMW' , 14)
# obj.greet()

#multiple class
# class vehicle:
#     def show(self):
#         print('this is show class')
# class electric:
#     def show2(self):
#         print('this is show2 class')
# class hybrid(vehicle,electric):
#     pass
# obj=hybrid()
# obj.show()
# obj.show2()
#HYBRID   combination of 2 hierarchial or multi
# class A:
#     def show(self):
#         print('i am show function')
# class B(A):
#     def show_2(self):
#         print("i am show_2 fumction")
# class C(A):
#     def show_3(self):
#         print('i am show_3 function')
# class D(B,C):
#     def show_4(self):
#         print('i am show_4 function')

'''incapsulation --> encapsulation means bundling data(attributes) and methods into one unit(class)
       and it also involves controlling access to these attributes using access modifiers '''
'''access modifiers-->
      1. public (accessible anywhere)
      2. protected (_ use by this in front of method and attributes)(accessible in the class and subclasses)
      3. private (__ use by this in front of method and attributes)(accessible only in the class)'''
# class animal:
#     name='lion'

#     def speak(self):
#         print('hello i will roar')

# class human(animal):         ek esa function jo private method ko print krae called '''GETTER METHOD'''
#     def say(self):            ek esa function jo private method k value ko change krde ya set krde call '''SETTER METHOD'''
#         print(f'hello my name is {super().name}')
# obj=human()
# obj.say()
    # def show(self,marks):
    #     self.marks=marks
'''polymorphism'''
# class A:
#     def show(self):
#         print('this is show method A')
# class B(A):
#     def show(self):
#             print('this is show method B')
# obj=B()
# obj.show()
'''DATA ABSTRACTION'''
from abc import ABC, abstractmethod
# class parent(ABC):

#     @abstractmethod       #agar kisi fun k upar @abstractmethod lgaya to child class mai bnana pdega vo fun
#     def show(self):
#         pass

#     def display(self):
#         print('this is display func...')

# class child(parent):
#     def show(self):
#         print('this is child class..')
# obj=child()
# obj.show()
# obj.display()

class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

    def show(self):
        print('this is parent class')
class upi(payment):
    def pay(self,amount):
        self.amount=amount
        print(f'amount is {self.amount}')
class card(payment):
    def pay(self,amount):
        self.amount=amount
        print(f'amount is {self.amount}')
    def details(self):
        print('this is card class')
obj=card()
obj.pay(1000)
obj.details()
