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
App.getDocument('Unnamed').getObject('Sketch').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XZ_Plane'])
App.getDocument('Unnamed').getObject('Sketch').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
### End command PartDesign_CompSketches


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 0.000000, 0.000000),App.Vector(0.000000, 20.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,20.000000))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',0))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 0, 1, -1, 1))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 0.000000, 0.000000),App.Vector(-100.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,100.000000))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Horizontal',1))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 1, 1, 0, 1))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(-99.642036, 13.282415, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 13.287238), 1.543853, 4.685445))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Angle',2,3.141593))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 2, 2, 1, 2))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Radius',2,13.287238))
App.getDocument('Unnamed').getObject('Sketch').setDatum(8,App.Units.Quantity('20.000000 mm'))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(-99.251212, 39.992991, 0.000000),App.Vector(-24.251212, 39.992991, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',3,75.000000))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Horizontal',3))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 3, 1, 2, 1))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(0.000000, 39.929123, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 24.251296), 3.138959, 4.712389))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList
constraintList = []
constraintList.append(Sketcher.Constraint('PointOnObject', 4, 3, -2))
constraintList.append(Sketcher.Constraint('Coincident', 4, 1, 3, 2))
constraintList.append(Sketcher.Constraint('Coincident', 4, 2, 0, 2))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',2,1,1,2))

App.ActiveDocument.recompute()
App.getDocument('Unnamed').recompute()

### Begin command PartDesign_Pad
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad')
App.getDocument('Unnamed').getObject('Pad').Profile = (App.getDocument('Unnamed').getObject('Sketch'), ['',])
App.getDocument('Unnamed').getObject('Pad').Length = __PAD_LEN__
App.getDocument('Unnamed').getObject('Pad').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pad').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pad').Direction = (0, -1, 0)
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
App.getDocument('Unnamed').purgeTouched()
App.getDocument('Unnamed').recompute()
### End command PartDesign_Pad
App.getDocument('Unnamed').getObject('Sketch').Visibility = False


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(-100.000003, 20.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 10.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',5,__HOLE_DIA__))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 5, 3, 2, 3))

App.ActiveDocument.recompute()
App.getDocument('Unnamed').recompute()

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