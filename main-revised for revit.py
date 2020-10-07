import math
# Imports the necessary modules for the text input dialog box in Revit
from rpw.ui.forms import TextInput

from rpw.ui.forms import Alert

#This module allows python code seamless integration with the .NET Common Language Runtime (CLR)
import clr
from Autodesk.Revit.DB import DWGImportOptions, ImportPlacement, ElementId, Transaction, BaseImportOptions, XYZ, ImportUnit

#Assigns the variable "doc" the active document
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

options = DWGImportOptions()
#options.ReferencePoint = XYZ()
#options.Unit = ImportUnit.Millimeter

#options.Placement = ImportPlacement.Origin
link = clr.Reference[ElementId]()
t = Transaction(doc)



def propGenerator():
        
    flag = True
    while(flag):
        flag = False
        #height takes a int value in mm
        height = TextInput("Prop Generator", description="Please enter a integer value in mm:", default="0")
        
        #Input validation - accepthing only integers
        if height.isdigit():
            #Max prop height according to RMD literature is 18m
            if int(height) > 18000:
                Alert("Prop height greater than 18m is not allowed", title="Prop Generator", header="User Input Error!", exit=False)
                flag = True
                
            member_list = [5400, 2700, 1800, 900, 450, 270, 90]
            prop = [
                ["5400"],
                ["2700"],
                ["1800"],
                ["900"],
                ["450"],
                ["270"],
                ["90"],
                ["jacks", 0]
            ]

            no_of_jacks = TextInput("Prop Generator", description="Megashor Jack on one(1) end or both(2) ends: ", default="1")
            if no_of_jacks.isdigit():
                if no_of_jacks == '1':
                    lower_limit = 410
                    upper_limit = 620
                    prop[7][1] = 1
                else:
                    lower_limit = 820
                    upper_limit = 1240
                    prop[7][1] = 2
            else:
                Alert("Please only enter a integer value for the prop height", title="Prop Generator", header="User Input Error!", exit=False)
                

            height = int(height)
            j = 0

            for i in member_list:

                res = height%i
                count = 0
                
                while((height/i) > 1):
                    if((height - i > lower_limit) or (res > lower_limit)):
                        count += 1
                        height -= i
                    else:
                        break

                prop[j].append(count)
                j+=1 
        else:
            Alert("Please only enter a integer value for the prop height", title="Prop Generator", header="User Input Error!", exit=False)
            flag = True  
    print(prop)
    return prop   

prop_list = propGenerator()

x, y, z = 0.0, 0.0, 0.0
X = x / 304.8
Y = y / 304.8
for i in prop_list:
    for j in range(i[1]):
        Z = z / 304.8
        options.ReferencePoint = XYZ(X, Y, Z)
        if(i[0] == "jacks"):
            z += float((i-1)[0])
            options.ReferencePoint = XYZ(X, Y, Z)
            t.Start('Load Link')
            doc.Link(r"G:\Drafting\RMD\\3D RMD CAD BLOCKS\Megashor AU_Client\megashor\megashor_jack_base_left.dwg", options, uidoc.ActiveView, link)
            t.Commit()
            z += 200
            options.ReferencePoint = XYZ(X, Y, Z)
            t.Start('Load Link')
            doc.Link(r"G:\Drafting\RMD\\3D RMD CAD BLOCKS\Megashor AU_Client\megashor\megashor_jack_screw.dwg", options, uidoc.ActiveView, link)
            t.Commit()
            z += 200
            options.ReferencePoint = XYZ(X, Y, Z)
            t.Start('Load Link')
            doc.Link(r"G:\Drafting\RMD\\3D RMD CAD BLOCKS\Megashor AU_Client\megashor\megashor_jack_base_right.dwg", options, uidoc.ActiveView, link)
            t.Commit()

        else:
            z += float(i[0])
            Z = z / 304.8
            options.ReferencePoint = XYZ(X, Y, Z)
            print("G:\Drafting\RMD\\3D RMD CAD BLOCKS\Megashor AU_Client\megashor\megashor_" + str(i[0]) + ".dwg")
            t.Start('Load Link')
            doc.Link(r"G:\Drafting\RMD\\3D RMD CAD BLOCKS\Megashor AU_Client\megashor\megashor_" + str(i[0]) + ".dwg", options, uidoc.ActiveView, link)
            t.Commit()