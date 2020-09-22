import math

#height takes a float value in mm
def propGenerator():

        
    flag = True
    while(flag):
        flag = False
        height = input("Please enter a integer value in mm: ")


        if height.isdigit():
            print("is digit")
            if int(height) > 18000:
                print("Prop height greater than 18m is not allowed")
                flag = True
                continue

            member_list = [5400, 2700, 1800, 900, 450, 270, 90]
            prop = {
                "5400": '',
                "2700": '',
                "1800": '',
                "900": '',
                "450": '',
                "270": '',
                "90": '',
                "jacks": ''
            }

            no_of_jacks = input("Do you want a Megashor Jack on one end or both ends of the prop? /nEnter '1' for one end or '2' for both ends: ")
            if no_of_jacks == '1':
                lower_limit = 410
                upper_limit = 620
            else:
                lower_limit = 820
                upper_limit = 1240

            
            height = int(height)
            for i in member_list:

                res = height%i
                print("res= " + str(res))
                print("height= " + str(height))
                print("i= " + str(i))

                
                if (height/i >= 2):
                    if res > upper_limit:
                        temp = math.floor(height/i)
                        prop[str(i)] = temp
                        height = res
                        print(i)
                    if lower_limit < res and res < upper_limit:
                        pass
                elif height/i >= 1 and height/i < 2 and res > upper_limit:
                    prop[str(i)] = 1
                    height -= i
                    print(i)
                elif height/i < 1 and res > lower_limit and res < upper_limit:
                    prop["jacks"] = no_of_jacks
                    print(i)
                    
        else:
            flag = True  
    print(prop)    
    
propGenerator()

