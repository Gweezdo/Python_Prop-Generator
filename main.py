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

            no_of_jacks = input("Do you want a Megashor Jack on one end or both ends of the prop? Enter '1' for one end or '2' for both ends: ")
            if no_of_jacks == '1':
                lower_limit = 410
                upper_limit = 620
                prop["jacks"] = 1
            else:
                lower_limit = 820
                upper_limit = 1240
                prop["jacks"] = 2

            
            height = int(height)
            for i in member_list:

                res = height%i
                # print("res= " + str(res))
                # print("height= " + str(height))
                # print("i= " + str(i))

                count = 0
                while(height/i > 1):
                    if((height - i) > lower_limit or res > lower_limit):

                        count += 1
                        # print("count =" + str(count))
                        height -= i
                    else:
                        break


                prop[str(i)] = count
                # height -= i*coun 
        else:
            flag = True  
    print(prop)    
    
propGenerator()
