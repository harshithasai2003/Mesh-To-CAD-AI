import FreeCAD
import PartDesign
import Sketcher
import Part
import Mesh

### Begin command Std_New
App.newDocument()
### End command Std_New

### Begin command PartDesign_CompSketches
App.getDocument('Unnamed').addObject('PartDesign::Body','Body')
App.getDocument('Unnamed').getObject('Body').AllowCompound = True

App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch')
App.getDocument('Unnamed').getObject('Sketch').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XY_Plane'])
App.getDocument('Unnamed').getObject('Sketch').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
### End command PartDesign_CompSketches


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(0.000000, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 3.000000), 0.000000, 3.141593))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Radius',0,3.000000))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Angle',0,3.141593))
constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 0, 3, -1, 1))
constraintList.append(Sketcher.Constraint('PointOnObject', 0, 2, -1))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(3.000000, -0.000001, 0.000000),App.Vector(5.000000, 0.000001, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,2.000000))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Angle',-1,1,0.000001))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident',1,1,0,1))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(5.000000, 0.000001, 0.000000),App.Vector(5.000000, -2.999999, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',2,3.000000))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',2))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 2, 1, 1, 2))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(5.000000, -2.999999, 0.000000),App.Vector(4.000000, -2.999999, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',3,1.000000))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Horizontal',3))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 3, 1, 2, 2))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(2.015612, -3.101318, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 1.986973), 3.192606, 6.334199))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Angle',4,3.141593))
constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 4, 2, 3, 2))
constraintList.append(Sketcher.Constraint('PointOnObject', 4, 1, -2))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Horizontal',4,1,3,2))
App.getDocument('Unnamed').getObject('Sketch').delConstraint(15)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Radius',4,2.000000))
App.getDocument('Unnamed').getObject('Sketch').setDatum(16,App.Units.Quantity('3.000000 mm'))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(-2.000000, -2.999999, 0.000000),App.Vector(-4.000000, -2.999999, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',5,2.000000))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Horizontal',5))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 5, 1, 4, 1))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(-4.000000, -2.999999, 0.000000),App.Vector(-4.000000, 0.000001, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',6,3.000000))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',6))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 6, 1, 5, 2))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(-4.000000, 0.000001, 0.000000),App.Vector(-3.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 7, 1, 6, 2))
constraintList.append(Sketcher.Constraint('Coincident', 7, 2, 0, 2))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

# --- Post-profile holes — safe to parametrize, referenced only by their own Diameter constraint ---
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(0.000000, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 0.500000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',8,__HOLE1_DIA__))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 8, 3, 0, 3))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(1.000000, -3.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 0.500000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',9,__HOLE2_DIA__))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 9, 3, 4, 3))

App.ActiveDocument.recompute()
App.getDocument('Unnamed').recompute()

### Begin command PartDesign_Pad
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad')
App.getDocument('Unnamed').getObject('Pad').Profile = (App.getDocument('Unnamed').getObject('Sketch'), ['',])
App.getDocument('Unnamed').getObject('Pad').Length = __PAD_LEN__
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
App.getDocument('Unnamed').recompute()
App.ActiveDocument.recompute()
### End command PartDesign_Pad
App.getDocument('Unnamed').getObject('Sketch').Visibility = False

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