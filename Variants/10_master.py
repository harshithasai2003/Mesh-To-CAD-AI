# Macro Begin: C:\Users\pawar\AppData\Roaming\FreeCAD\v1-1\Macro\10.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
import FreeCAD
import FreeCAD as App
import Part
import PartDesign
# import PartDesignGui
import Sketcher
import Mesh
import ProfileLib.RegularPolygon

### Begin command Std_New
App.newDocument()
### End command Std_New
### Begin command PartDesign_CompSketches
App.getDocument('Unnamed').addObject('PartDesign::Body','Body')
App.getDocument('Unnamed').getObject('Body').AllowCompound = True
### End command PartDesign_CompSketches
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch')
App.getDocument('Unnamed').getObject('Sketch').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XY_Plane'])
App.getDocument('Unnamed').getObject('Sketch').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

ProfileLib.RegularPolygon.makeRegularPolygon(App.getDocument('Unnamed').getObject('Sketch'),6,App.Vector(0.000000,0.000000,0),App.Vector(__HEX_R__,0.000000,0),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Radius',6,__HEX_R__)) 
constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 6, 3, -1, 1))
constraintList.append(Sketcher.Constraint('PointOnObject', 5, 2, -1))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

App.ActiveDocument.recompute()
App.getDocument('Unnamed').recompute()
### Begin command PartDesign_Pad
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad')
App.getDocument('Unnamed').getObject('Pad').Profile = (App.getDocument('Unnamed').getObject('Sketch'), ['',])
App.getDocument('Unnamed').getObject('Pad').Length = 10
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pad').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'),['N_Axis'])
App.getDocument('Unnamed').getObject('Sketch').Visibility = False
App.ActiveDocument.recompute()
### End command PartDesign_Pad
App.getDocument('Unnamed').getObject('Pad').Length = __PAD_H__
App.getDocument('Unnamed').getObject('Pad').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pad').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pad').Direction = (0, 0, 1)
App.getDocument('Unnamed').getObject('Pad').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'), ['N_Axis'])
App.getDocument('Unnamed').getObject('Pad').AlongSketchNormal = 1
App.getDocument('Unnamed').getObject('Pad').SideType = 2
App.getDocument('Unnamed').getObject('Pad').Type = 0
App.getDocument('Unnamed').getObject('Pad').Type2 = 0
App.getDocument('Unnamed').getObject('Pad').UpToFace = None
App.getDocument('Unnamed').getObject('Pad').UpToFace2 = None
App.getDocument('Unnamed').getObject('Pad').Reversed = 0
App.getDocument('Unnamed').getObject('Pad').Offset = 0
App.getDocument('Unnamed').getObject('Pad').Offset2 = 0
App.getDocument('Unnamed').recompute()
App.getDocument('Unnamed').getObject('Sketch').Visibility = False
### Begin command PartDesign_NewSketch
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch001')
App.getDocument('Unnamed').getObject('Sketch001').AttachmentSupport = (App.getDocument('Unnamed').getObject('Pad'),['Face8',])
App.getDocument('Unnamed').getObject('Sketch001').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
### End command PartDesign_NewSketch
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(0.000000, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 15.000000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',0,__HOLE_DIA__)) 
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Coincident', 0, 3, -1, 1))

App.ActiveDocument.recompute()
App.getDocument('Unnamed').recompute()
### Begin command PartDesign_Pocket
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pocket','Pocket')
App.getDocument('Unnamed').getObject('Pocket').Profile = (App.getDocument('Unnamed').getObject('Sketch001'), ['',])
App.getDocument('Unnamed').getObject('Pocket').Length = 5
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pocket').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch001'),['N_Axis'])
App.getDocument('Unnamed').getObject('Sketch001').Visibility = False
App.ActiveDocument.recompute()
### End command PartDesign_Pocket
App.getDocument('Unnamed').getObject('Pocket').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pocket').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pocket').Direction = (0, 0, -1)
App.getDocument('Unnamed').getObject('Pocket').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch001'), ['N_Axis'])
App.getDocument('Unnamed').getObject('Pocket').AlongSketchNormal = 1
App.getDocument('Unnamed').getObject('Pocket').SideType = 0
App.getDocument('Unnamed').getObject('Pocket').Type = 1
App.getDocument('Unnamed').getObject('Pocket').Type2 = 0
App.getDocument('Unnamed').getObject('Pocket').UpToFace = None
App.getDocument('Unnamed').getObject('Pocket').UpToFace2 = None
App.getDocument('Unnamed').getObject('Pocket').Reversed = 0
App.getDocument('Unnamed').getObject('Pocket').Offset = 0
App.getDocument('Unnamed').getObject('Pocket').Offset2 = 0
App.getDocument('Unnamed').recompute()
App.getDocument('Unnamed').getObject('Pad').Visibility = False
App.getDocument('Unnamed').getObject('Sketch001').Visibility = False
### Begin command PartDesign_Chamfer
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Chamfer','Chamfer')
App.getDocument('Unnamed').getObject('Chamfer').Base = (App.getDocument('Unnamed').getObject('Pocket'),['Face5',])
App.getDocument('Unnamed').getObject('Pocket').Visibility = False
App.ActiveDocument.recompute()
### End command PartDesign_Chamfer
App.getDocument('Unnamed').getObject('Chamfer').Size = 1.000000
App.getDocument('Unnamed').getObject('Chamfer').Base = (App.getDocument('Unnamed').getObject('Pocket'),["Face5",])
App.getDocument('Unnamed').getObject('Chamfer').Size = 1.000000
App.getDocument('Unnamed').recompute()
App.getDocument('Unnamed').getObject('Pocket').Visibility = False
### Begin command PartDesign_Chamfer
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Chamfer','Chamfer001')
App.getDocument('Unnamed').getObject('Chamfer001').Base = (App.getDocument('Unnamed').getObject('Chamfer'),['Face4',])
App.getDocument('Unnamed').getObject('Chamfer').Visibility = False
App.ActiveDocument.recompute()
### End command PartDesign_Chamfer
App.getDocument('Unnamed').getObject('Chamfer001').Size = 1.000000
App.getDocument('Unnamed').getObject('Chamfer001').Base = (App.getDocument('Unnamed').getObject('Chamfer'),["Face4",])
App.getDocument('Unnamed').getObject('Chamfer001').Size = 1.000000
App.getDocument('Unnamed').recompute()
App.getDocument('Unnamed').getObject('Chamfer').Visibility = False

### Begin command Std_Save
App.getDocument('Unnamed').recompute(None, True, True)
App.getDocument("Unnamed").saveAs(FCSTD_FILE)
### End command Std_Save
### Begin command Std_Export
__objs__ = []
__objs__.append(FreeCAD.getDocument("Unnamed").getObject("Body"))
if hasattr(Mesh, "exportOptions"):
    options = Mesh.exportOptions(STL_FILE)
    Mesh.export(__objs__, STL_FILE, options)
else:
    Mesh.export(__objs__, STL_FILE)
del __objs__
### End command Std_Export


App.closeDocument(App.getDocument("Unnamed").Name)
# Macro End: C:\Users\pawar\AppData\Roaming\FreeCAD\v1-1\Macro\10.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++