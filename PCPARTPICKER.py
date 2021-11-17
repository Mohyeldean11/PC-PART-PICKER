"""classes"""
from _typeshed import Self
import random
class PC(object):
    def __init__(self,Name,Price,Manufacturer):
        self.Name=Name
        self.Price=Price
        self.Manufacturer=Manufacturer
    def __str__(self):
        return "the part is {} and its price is {} and its manufacturer is {}".format(self.Name,self.Price,self.Manufacturer)
    




class CPU(PC):
    CPU_DIC={}
    def __init__(self,Core_num,Frequency):
        self.Core_num=Core_num
        self.Frequency=Frequency
    
    def choose_CPU(self,Price):
        if self.Price in self.CPU_DIC:
            choice= random.choice(self.CPU_DIC[self.Price])
 
        
        print(choice)
        return choice
     

class GPU(PC):
    GPU_DIC={}
    def __init__(self,CAPACITY,POWERUSAGE):
        self.CAPACITY=CAPACITY
        self.POWERUSAGE=POWERUSAGE
    def choose_GPU(self,Price):
        if self.Price in self.GPU_DIC:
            choice= random.choice(self.GPU_DIC[self.Price])
 
        print(choice)
        return choice


class RAMS(PC):
    RAM_DIC={}
    def __init__(self,size,speed,DDR):
        self.size=size
        self.speed=speed
        self.DDR=DDR

    def choose_RAMS(self,Price):
        if self.Price in self.RAM_DIC:
            choice= random.choice(self.RAM_DIC[self.Price])
 
        print(choice)
        return choice

class MOBO(PC):
    MOBO_DIC={}
    def __init__(self,RAM_CAPACITY,slot_number):
        self.RAM_CAPACITY=RAM_CAPACITY
        self.slot_number=slot_number

    def choose_MOBO(self,Price):
        if self.Price in self.MOBO_DIC:
            choice= random.choice(self.MOBO_DIC[self.Price])
 
        print(choice)
        return choice

    def CPU_COMPAT(self,CPU):
        pass

class PSU(PC):
    PSU_DIC={}
    def __init__(self,POWER_CAPACITY,TYPE):
        self.POWER_CAPACITY=POWER_CAPACITY
        self.TYPE=TYPE

    def choose_PSU(self,Price):
        if self.Price in self.PSU_DIC:
            choice= random.choice(self.PSU_DIC[self.Price])
 
        print(choice)
        return choice


class CASE(PC):
    CASE_DIC={}

    def choose_PSU(self,Price):
        if self.Price in self.CASE_DIC:
            choice= random.choice(self.CASE_DIC[self.Price])
 
        print(choice)
        return choice

budget=0
def GAMINGCHOICE():
    print("Your choice is GAMING PC")
    CPU.Price=(budget*0.25)
    GPU.Price=(budget*0.40)
    RAMS.Price=(budget*0.11)
    MOBO.Price=(budget*0.12)
    PSU.Price=(budget*0.08)
    CASE.Price=(budget*0.04)
        
def RENDERING_Choice():
    print("Your choice is RENDERING PC")
    CPU.Price=(budget*0.35)
    GPU.Price=(budget*0.30)
    RAMS.Price=(budget*0.16)
    MOBO.Price=(budget*0.10)
    PSU.Price=(budget*0.06)
    CASE.Price=(budget*0.03)

def NORMAL_CHOICE():
    print("Your choice is A NORMAL PC")
    CPU.Price=(budget*0.30)
    GPU.Price=(budget*0.30)
    RAMS.Price=(budget*0.15)
    MOBO.Price=(budget*0.10)
    PSU.Price=(budget*0.05)
    CASE.Price=(budget*0.10)



"""PC PART PICKER"""

print("Which option do you want to choose?\n")
print("(1) I want to build it by my own\n (2) I want the magic wizard to build it for me\n")
Choice=input("please enter you choice (1) or (2) :  \n ")
print(Choice)

if(Choice==1):
    budget=input("The budget is : \n")
    print("The usage of the PC will be \n (1)GAMING\n(2)RENDERING AND DESIGN \(2)A NORMAL PC")
    usage=input("your usage will be (1) or (2) or (3) : \n ")
    if(usage==1):
        GAMINGCHOICE()

    elif(usage==2):
        RENDERING_Choice()

    elif(usage==3):
        NORMAL_CHOICE()

    else:
        print("PLEASE CHOOSE A VALID OPTION")
        exit
    


