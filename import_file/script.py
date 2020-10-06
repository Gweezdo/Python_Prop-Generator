import clr
from Autodesk.Revit.DB import DWGImportOptions, ImportPlacement, ElementId, Transaction

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

options = DWGImportOptions()
options.Placement = ImportPlacement.Origin
link = clr.Reference[ElementId]()
t = Transaction(doc)
t.Start('Load Link')
doc.Link(r"G:\Drafting\RMD\3D RMD CAD BLOCKS\Megashor AU_Client\megashor\megashor_5400.dwg", options, uidoc.ActiveView, link)
t.Commit()
