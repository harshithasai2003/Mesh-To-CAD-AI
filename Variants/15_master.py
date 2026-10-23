import FreeCAD
import FreeCAD as App
import Part
import PartDesign
# import PartDesignGui
import Sketcher
import Mesh

# Gui.runCommand('Std_DlgMacroRecord',0)
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
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(0.000000, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 25.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',0,__OUTER_DIA__)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 0, 3, -1, 1))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(0.000000, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 10.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',1,__CENTER_HOLE_DIA__)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 1, 3, 0, 3))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(0.000000, 19.037214, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 5.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',2,__BOLT_HOLE_DIA__)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('PointOnObject', 2, 3, -2))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(17.925743, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 5.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',3,__BOLT_HOLE_DIA__)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('PointOnObject', 3, 3, -1))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(0.000000, -17.703526, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 5.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',4,__BOLT_HOLE_DIA__)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('PointOnObject', 4, 3, -2))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(-16.889074, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 5.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',5,__BOLT_HOLE_DIA__)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('PointOnObject', 5, 3, -1))


App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',2,3,-1,19.037214)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(12,App.Units.Quantity('__BOLT_PITCH_RADIUS__ mm'))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',3,3,-2,17.925743)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(13,App.Units.Quantity('__BOLT_PITCH_RADIUS__ mm'))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,3,-1,17.703526)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(14,App.Units.Quantity('__BOLT_PITCH_RADIUS__ mm'))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',5,3,-2,16.889074)) 
App.getDocument('Unnamed').getObject('Sketch').setDatum(15,App.Units.Quantity('__BOLT_PITCH_RADIUS__ mm'))
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
App.getDocument('Unnamed').getObject('Pad').Length = __PAD_HEIGHT__
App.getDocument('Unnamed').getObject('Pad').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pad').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pad').Direction = (0, 0, 1)
App.getDocument('Unnamed').getObject('Pad').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'), ['N_Axis'])
App.getDocument('Unnamed').getObject('Pad').AlongSketchNormal = 1
App.getDocument('Unnamed').getObject('Pad').SideType = 0
App.getDocument('Unnamed').getObject('Pad').Type = 0
App.getDocument('Unnamed').getObject('Pad').Type2 = 0
App.getDocument('Unnamed').getObject('Pad').UpToFace = None
App.getDocument('Unnamed').getObject('Pad').UpToFace2 = None
App.getDocument('Unnamed').getObject('Pad').Reversed = 0
App.getDocument('Unnamed').getObject('Pad').Offset = 0
App.getDocument('Unnamed').getObject('Pad').Offset2 = 0
App.getDocument('Unnamed').purgeTouched()
App.getDocument('Unnamed').recompute()
App.getDocument('Unnamed').getObject('Sketch').Visibility = False

App.getDocument('Unnamed').recompute(None, True, True)
App.getDocument("Unnamed").saveAs(FCSTD_FILE)

__objs__ = []
__objs__.append(FreeCAD.getDocument("Unnamed").getObject("Body"))
if hasattr(Mesh, "exportOptions"):
    options = Mesh.exportOptions(STL_FILE)
    Mesh.export(__objs__, STL_FILE, options)
else:
    Mesh.export(__objs__, STL_FILE)
del __objs__

App.closeDocument(App.getDocument("Unnamed").Name)