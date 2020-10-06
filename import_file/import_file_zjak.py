from Autodesk.Revit.DB import *

file_path = 'G:\Drafting\RMD\3D RMD CAD BLOCKS\Megashor AU_Client\megashor\megashor_900.dwg'
dwg_options = DWGImportOptions()
dwg_view = View()
dwg_element = ElementId(25)
doc.Import(file_path, dwg_options, dwg_view, dwg_element)