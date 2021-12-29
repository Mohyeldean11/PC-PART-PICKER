
"""constants"""
repeat_flag="yes"
budget=0
MOBOprice=0
CPUprice=0
GPUprice=0
RAMprice=0
PSUprice=0
hard_price=0
HDD=0
processor=0
videocard=0
motherboard=0
ram=0
powersupply=0

CPU_list=[]
cpu_choices=[]
GPU_list=[]
gpu_choices=[]
MOBO_list=[]
mobo_choices=[]
RAM_list=[]
ram_choices=[]
PSU_list=[]
psu_choices=[]
HDD_list=[]
HDD_choices=[]
cooling_list=[]
cooling_choices=[]
"""functions"""
def remainder():
    remaining_budget=int((CPUprice+GPUprice+MOBOprice+RAMprice+PSUprice)-PC_parts.total_budget())
    return remaining_budget






"""classes"""
class accessories(object):
    def __init__(self,Name,Price):
        self.Name=Name
        self.Price=Price
    
     
class PC_parts(object):
    def __init__(self,Name,Price,Manufacturer,Rating):
        self.Name=Name
        self.Price=Price
        self.Manufacturer=Manufacturer
        self.Rating=Rating

    def power_summation(self):
        power_output=processor.Power_output + videocard.Powerusage
        return power_output

    def __str__(self):
        return ("THE BEST PART FOR YOUR BUDGET IS '{}' AND ITS PRICE IS {} L.E AND SOLD TO YOU BY '{}'".format(self.Name,self.Price,self.Manufacturer))

    def total_budget():
        Total=processor.Price+videocard.Price+motherboard.Price+ram.Price+powersupply.Price
        return Total

    def final_rating():
        Rate=(processor.Rating+videocard.Rating+motherboard.Rating+ram.Rating+powersupply.Rating)/5
        return ("THE FINAL RATING FOR YOUR BUILD IS ACTUALLY {} OUT OF 10".format(Rate))

    def build_display():
        print("YOUR BUILD IS\n")
        print(processor.Name)
        print("\n")
        print(videocard.Name)
        print("\n")
        print(motherboard.Name)
        print("\n")
        print(ram.Name)
        print("\n")
        print(powersupply.Name)
        print("\n")
        return("HOPE YOU ENJOY YOUR BUILD")
class CPU(PC_parts):
    
    def __init__(self,Name,Price,Manufacture,Rating,Core_num,Frequency,Gen,Power_output):
        super().__init__(Name,Price,Manufacture,Rating)
        self.Core_num=Core_num
        self.Frequency=Frequency
        self.Gen=Gen
        self.Power_output=Power_output

    def choose_CPU(self):

        for key in CPU_list:
            if(key.Price<=CPUprice):
                cpu_choices.append(key)
        try:
            cpu_choices.sort(key=lambda CPU:CPU.Price,reverse=True)

            return(cpu_choices[0])
        except:
            processorflag=0
            return("SORRY,THERE IS INSUFFICIENT MONEY FOR THE PROCESSOR ")
            

            

"""THE PROCESSORS AVAILABLE IN THE APP"""

CPU1=CPU("RYZEN 5 1600",2600,"AMD",6,6,3.2,1,65)
CPU2=CPU("RYZEN 5 2600",3500,"AMD",6.5,6,3.4,2,100)
CPU3=CPU("RYZEN 5 3600",4244,"AMD",7,6,3.6,3,120)
CPU4=CPU("RYZEN 5 5600X",5900,"AMD",7.5,6,3.7,4,142)
CPU5=CPU("Ryzen 7 3700X",5500,"AMD",8.5,8,3.6,3,150)
CPU6=CPU("RYZEN 7 5800X",8400,"AMD",9,8,4.7,4,189)
CPU_list=[CPU1,CPU2,CPU3,CPU4,CPU5,CPU6]


class GPU(PC_parts):
    def __init__(self,Name,Price,Manufacture,Rating,Capacity,Powerusage):
        super().__init__(Name,Price,Manufacture,Rating)
        self.Capacity=Capacity
        self.Powerusage=Powerusage

    def choose_GPU(self):
        for key in GPU_list:
            if(key.Price<=GPUprice):
                gpu_choices.append(key)
        try:     
            gpu_choices.sort(key=lambda GPU:GPU.Price,reverse=True)

            return (gpu_choices[0])
            
        except:

            return("SORRY,THERE IS INSUFFICIENT MONEY FOR THE GRAPHIC CARD")

"""THE GPUS AVAILABLE IN THE APP"""

GPU1=GPU("RTX 2060",7000,"NVIDIA",6,6,160)
GPU2=GPU("RTX 2060 super",8600,"NVIDIA",7,6,170)
GPU3=GPU("RTX 2070",9000,"NVIDIA",7.5,8,175)
GPU4=GPU("RTX 2070 super",12000,"NVIDIA",8,8,190)
GPU5=GPU("RTX 2080",17000,"NVIDIA",8.5,8,215)
GPU6=GPU("RTX 2080 ti",20000,"NVIDIA",9,11,250)
GPU_list=[GPU1,GPU2,GPU3,GPU4,GPU5,GPU6]





class MOBO(PC_parts):
    def __init__(self,Name,Price,Manufacture,Rating,Ram_cap,Gen):
        super().__init__(Name,Price,Manufacture,Rating)
        self.Ram_cap=Ram_cap
        self.Gen=Gen

    def choose_MOBO(self):
        for key in MOBO_list:
            if(key.Price<=MOBOprice):
                if(key.Gen<=processor.Gen):
                    mobo_choices.append(key)

        try:
            if(usage==1):
                mobo_choices.sort(key=lambda MOBO:MOBO.Price,reverse=True)
            elif(usage==2):
                mobo_choices.sort(key=lambda MOBO:MOBO.Ram_cap,reverse=True)
            elif(usage==3):
                mobo_choices.sort(key=lambda MOBO:MOBO.Ram_cap,reverse=True)

            return mobo_choices[0]
            
        except:

            return("SORRY,THERE IS INSUFFICIENT MONEY FOR THE MOTHERBOARD")        

"""THE MOTHERBOARDS AVAILABLE IN THE APP"""

MOBO1=MOBO("B350-F",1200,"MSI",6,64,2)
MOBO2=MOBO("B450 Tomahawk MAX",1400,"MSI",6.5,64,3)
MOBO3=MOBO("B450 AORUS Pro",1500,"Gigabyte",7,64,3)
MOBO4=MOBO("A520 AORUS Elite",2200,"Gigabyte",7.5,128,4)
MOBO5=MOBO("B550M Steel Legend",2500,"ASRock",8,128 ,4)
MOBO6=MOBO("ROG Strix X570",2800,"ASUS",9,128,4)
MOBO_list=[MOBO1,MOBO2,MOBO3,MOBO4,MOBO5,MOBO6]       


class RAM(PC_parts):
    def __init__(self, Name, Price, Manufacturer,Rating,Speed,Size):
        super().__init__(Name, Price, Manufacturer,Rating)
        self.Speed=Speed
        self.Size=Size
    
    def choose_RAM(self):
        for key in RAM_list:
            if(key.Price<=RAMprice):
                if(key.Size<=motherboard.Ram_cap):
                    ram_choices.append(key)
        try:
            if(usage==1):
                ram_choices.sort(key=lambda RAM:RAM.Speed ,reverse=True)
            elif(usage==2):
                ram_choices.sort(key=lambda RAM:RAM.Size ,reverse=True)
            elif(usage==3):
                ram_choices.sort(key=lambda RAM:RAM.Size ,reverse=True)


            return (ram_choices[0])
            
        except:

            return("SORRY,THERE IS INSUFFICIENT MONEY FOR THE RAMS")

"""THE RAMS AVAILABLE IN THE APP"""

RAM1=RAM("Vengeance LPX 1X8 DDR4",700,"Corsair",6,3200,8)
RAM2=RAM("Vengeance LPX 2X8 DDR4",1200,"Corsair",7,3200,16)
RAM3=RAM("Ripjaws 4X16 DDR4 2400 C14 8x16GB",3500,"G.SKILL",8.5,2666,64)
RAM4=RAM("Ripjaws 2X8 DDR4",2000,"Corsair",8.5,3600,16)
RAM5=RAM("Ripjaws 1X8 DDR4",1400,"Corsair",8,3600,8)
RAM6=RAM("BALLISTICKS 2X16 DDR4",2800,"Corsair",9,3200,32)
RAM_list=[RAM1,RAM2,RAM3,RAM4,RAM5,RAM6]


class PSU(PC_parts):
    def __init__(self, Name, Price, Manufacturer,Rating,Power_output,Type):
        super().__init__(Name, Price, Manufacturer,Rating)
        self.Power_output=Power_output
        self.Type=Type

    def choose_PSU(self):
        total_power=PC_parts.power_summation(self)

        for key in PSU_list:
            if(key.Price<=PSUprice):
                if(key.Power_output>=total_power):
                    psu_choices.append(key)
        try:            
            psu_choices.sort(key=lambda PSU:PSU.Price ,reverse=True)
            return(psu_choices[0])
        except:
            return("SORRY,THERE IS INSUFFICIENT MONEY FOR THE POWER SUPPLY")


"""THE PSU AVAILABLE IN THE APP"""
PSU1=PSU("VS400",600,"Corsair",6,400," 80PLUS® White")
PSU2=PSU("PW400",600,"GigaByte",7,400,"80 PLUS")
PSU3=PSU("P550B",850,"GigaByte",8,550,"80 PLUS Bronze")
PSU4=PSU("MWE BRONZE",2000,"CoolerMaster",8,750,"80 PLUS Bronze")
PSU5=PSU("RGPS",1200,"Redragon ",8,600,"80 PLUS Bronze")
PSU6=PSU("Super NOVA",2100,"EVGA",9,850,"80 Plus Gold")

PSU_list=[PSU1,PSU2,PSU3,PSU4,PSU5,PSU6]

class HARD_DRIVES(accessories):
    def __init__(self, Name, Price,Size,Speed):
        super().__init__(Name, Price)
        self.Size=Size
        self.Speed=Speed

    def choose_HDD(self):
        
        for key in HDD_list:
            if(key.Price<=hard_price):
                HDD_choices.append(key)
        try:        
            HDD_choices.sort(key=lambda HARD_DRIVES:HARD_DRIVES.Price ,reverse=True)
            return(HDD_choices[0])
        except:
            return("SORRY NOT ENOUGH MONEY FOR ADDING A HARD DRIVE")


    def __str__(self):
        return("YOU WILL BE ABLE TO ADD A '{}'  WITH A CAPACITY '{}' AS A STORAGE TO YOUR PC".format(self.Name,self.Size))
    

"""THE HARD DRIVES AVAILABLE IN THE APP"""
HDD1=HARD_DRIVES("SEAGATE",340,"500GB",5900)
HDD2=HARD_DRIVES("SAMSUNG",750,"1TB",7200)
HDD3=HARD_DRIVES("SEAGATE",1200,"2TB",7200)
HDD4=HARD_DRIVES("KINGSTONE",2500,"4TB",7200)
HDD5=HARD_DRIVES("INTEL",12000,"20TB",7200)
HDD_list=[HDD1,HDD2,HDD3,HDD4,HDD5]

class COOLING(accessories):
    
    def __init__(self, Name, Price):
        super().__init__(Name, Price)

    def choose_cooling(self):
        
        for key in cooling_list:
            if(key.Price<=cooling_price):
                cooling_choices.append(key)


        try:
            cooling_choices.sort(key=lambda COOLING:COOLING.Price ,reverse=True)
                
            return(cooling_choices[0])
        except:
            return("SORRY NOT ENOUGH MONEY FOR ADDING A COOLING SYSTEM")

    def __str__(self):
        return ("YOU WILL BE ABLE TO SET UP A {} SYSTEM FOR YOUR BUILD".format(self.Name))

"""THE COOLING SYSTEMS IN THE APP"""
COOLING_SYS1=COOLING("AIR COOLING",900)
COOLING_SYS2=COOLING("WATER COOLING",2500)
COOLING_SYS3=COOLING("GLYCERINE COOLING",5000)

cooling_list=[COOLING_SYS1,COOLING_SYS2,COOLING_SYS3]


"""PC PART PICKER"""
while (repeat_flag=="yes" or repeat_flag=="YES"):
    print("'///////////////////// HELLO IN THE PC PART PICKER PROGRAM \\\\\\\\\\\\\\\\\\\\\'")
    print("YOU CAN CHOOSE FROM EITHER THE WIZARD OR BY YOUR OWN")
    print("FOR THE WIZZARD PRESS '1'\nFOR MANUAL ADDING PRESS '2' \n")
    build_way=int(input("ENTER YOUR CHOICE: "))
    if(build_way==1):

        budget=int(input("PLEASE ENTER YOU BUDGET IN NUMBERS :  "))
        usage=int(input("PLEASE ENTER YOUR CHOISE  \n '1' FOR GAMING \n '2' FOR RENDERING \n '3' FOR NORMAL USAGE  \n:  "))

        if(usage==1):

            adding_hard=input("DO YOU WANT TO ADD A HARD DRIVE? ")
            adding_cooler=input("DO YOU WANT TO ADD A COOLING SYSTEM ? ")

            print("YOUR CHOICE IS GAMING PC")
            CPUprice=(budget*0.26)
            GPUprice=(budget*0.41)
            MOBOprice=(budget*0.13)
            RAMprice=(budget*0.12)
            PSUprice=(budget*0.08)


            processor=CPU.choose_CPU(CPUprice)
            print(processor)
            videocard=GPU.choose_GPU(GPUprice)
            print(videocard)
            motherboard=MOBO.choose_MOBO(MOBOprice)
            print(motherboard)
            ram=RAM.choose_RAM(RAMprice)
            print(ram)
            powersupply=PSU.choose_PSU(PSUprice)
            print(powersupply)


            sum=PC_parts.total_budget()
            print("THE WHOLE BUILD WILL COST U {} L.E ".format(sum))
            print(PC_parts.build_display())
            print(PC_parts.final_rating())

            if(adding_hard=="yes" or adding_hard=="YES"):
                hard_price=0.3*remainder()
                hard_price=int(hard_price)
                hard_drive=HARD_DRIVES.choose_HDD(hard_price)
                print(hard_drive)

            if(adding_cooler=="yes" or adding_cooler=="YES"):
                cooling_price=0.5*remainder()
                cooling_price=int(cooling_price)
                cooling_system=COOLING.choose_cooling(cooling_price)
                print(cooling_system)

            repeat_flag=input("DO YOU WANT TO MAKE ANOTHER BUILD ? ")

        elif(usage==2):

            adding_hard=input("DO YOU WANT TO ADD A HARD DRIVE? ")
            adding_cooler=input("DO YOU WANT TO ADD A COOLING SYSTEM ? ")
            

            print("Your choice is RENDERING PC")
            CPUprice=(budget*0.36)
            GPUprice=(budget*0.31)
            RAMprice=(budget*0.17)
            MOBOprice=(budget*0.10)
            PSUprice=(budget*0.06)

            processor=CPU.choose_CPU(CPUprice)
            print(processor)
            videocard=GPU.choose_GPU(GPUprice)
            print(videocard)
            motherboard=MOBO.choose_MOBO(MOBOprice)
            print(motherboard)
            ram=RAM.choose_RAM(RAMprice)
            print(ram)
            powersupply=PSU.choose_PSU(PSUprice)
            print(powersupply)


            sum=PC_parts.total_budget()
            print("THE WHOLE BUILD WILL COST U {} ".format(sum))
            print(PC_parts.build_display())
            print(PC_parts.final_rating())

            if(adding_hard=="yes" or adding_hard=="YES"):
                hard_price=0.3*remainder()
                hard_price=int(hard_price)
                hard_drive=HARD_DRIVES.choose_HDD(hard_price)
                print(hard_drive)

            if(adding_cooler=="yes" or adding_cooler=="YES"):
                cooling_price=0.5*remainder()
                cooling_price=int(cooling_price)
                cooling_system=COOLING.choose_cooling(cooling_price)
                print(cooling_system)
    

            repeat_flag=input("DO YOU WANT TO MAKE ANOTHER BUILD ? ")

        elif(usage==3):
            adding_hard=input("DO YOU WANT TO ADD A HARD DRIVE? ")
            adding_cooler=input("DO YOU WANT TO ADD A COOLING SYSTEM ? ")


            print("Your choice is A NORMAL PC")
            CPUprice=(budget*0.32)
            GPUprice=(budget*0.32)
            RAMprice=(budget*0.17)
            MOBOprice=(budget*0.12)
            PSUprice=(budget*0.07)

            processor=CPU.choose_CPU(CPUprice)
            print(processor)
            videocard=GPU.choose_GPU(GPUprice)
            print(videocard)
            motherboard=MOBO.choose_MOBO(MOBOprice)
            print(motherboard)
            ram=RAM.choose_RAM(RAMprice)
            print(ram)
            powersupply=PSU.choose_PSU(PSUprice)
            print(powersupply)


            sum=PC_parts.total_budget()
            print("THE WHOLE BUILD WILL COST U {} ".format(sum))
            print(PC_parts.build_display())
            print(PC_parts.final_rating())

            if(adding_hard=="yes" or adding_hard=="YES"):
                hard_price=0.3*remainder()
                hard_price=int(hard_price)
                hard_drive=HARD_DRIVES.choose_HDD(hard_price)
                print(hard_drive)

            if(adding_cooler=="yes" or adding_cooler=="YES"):
                cooling_price=0.5*remainder()
                cooling_price=int(cooling_price)
                cooling_system=COOLING.choose_cooling(cooling_price)
                print(cooling_system)


            repeat_flag=input("DO YOU WANT TO MAKE ANOTHER BUILD ? ")
        else:
            print("INVALID CHOICE")
            break

    elif(build_way==2):

    
        print("please enter the usage of the pc\n")
        print("'1' FOR GAMING \n")
        print("'2' FOR RENDERING \n")
        print("'3' FOR NORMAL USE \n")
        usage=int(input("ENTER YOUR CHOICE: "))
        print(usage)
        CPUprice=int(input("PLEASE ENTER THE MONEY FOR THE PROCESSOR: "))
        processor=CPU.choose_CPU(CPUprice)

        if(CPUprice<2600):
            print(processor)
            break
        else:
            print(processor)
            
        GPUprice=int(input("PLEASE ENTER THE MONEY FOR THE GRAPHIC CARD: "))
        videocard=GPU.choose_GPU(GPUprice)

        if(GPUprice<7000):
            print(videocard)
            break
        else:
            print(videocard)


        MOBOprice=int(input("PLEASE ENTER THE MONEY FOR THE MOTHERBOARD: "))
        motherboard=MOBO.choose_MOBO(MOBOprice)

        if(MOBOprice<1200):
            print(motherboard)
            break
        else:
            print(motherboard)

        RAMprice=int(input("PLEASE ENTER THE MONEY FOR THE RAMS : "))
        ram=RAM.choose_RAM(RAMprice)

        if(RAMprice<700):
            print(ram)
            break
        else:
            print(ram)


        PSUprice=int(input("PLEASE ENTER THE MONEY FOR THE POWER SUPPLY: "))
        powersupply=PSU.choose_PSU(PSUprice)

        if(PSUprice<600):
            print(powersupply)
            break
        else:
            print(powersupply)

            
        print("\n")
        print("THE BUILD WILL COST YOU {} L.E".format(PC_parts.total_budget()))
        print(PC_parts.build_display())
        print(PC_parts.final_rating())
        print("\n")
        print("YOU STILL HAVE {} L.E REMAINING".format(remainder()))

        adding_hard=input("DO YOU WANT TO ADD A HARD DRIVE? ")
        if(adding_hard=="yes" or adding_hard=="YES"):
            hard_price=0.3*remainder()
            hard_price=int(hard_price)
            hard_drive=HARD_DRIVES.choose_HDD(hard_price)
            print(hard_drive)

        adding_cooler=input("DO YOU WANT TO ADD A COOLING SYSTEM ? ")
        if(adding_cooler=="yes" or adding_cooler=="YES"):
            cooling_price=0.7*remainder()
            cooling_price=int(cooling_price)
            cooling_system=COOLING.choose_cooling(cooling_price)
            print(cooling_system)

        repeat_flag=input("DO YOU WANT TO MAKE ANOTHER BUILD ? ")
    
    else:
        print("INVALID CHOICE")
        break


