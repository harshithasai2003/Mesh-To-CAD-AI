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
geoList.append(Part.Circle(App.Vector(0.000000, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 40.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',0,80.000000))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 0, 3, -1, 1))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(129.894440, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 20.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',1,40.000000))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('PointOnObject', 1, 3, -1))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,3,-2,129.894440))
App.getDocument('Unnamed').getObject('Sketch').setDatum(4,App.Units.Quantity('120.000000 mm'))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 13.768575, 0.000000),App.Vector(0.000000, -12.843344, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(0.000000, -12.843344, 0.000000),App.Vector(104.668708, -12.843344, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(104.668708, -12.843344, 0.000000),App.Vector(104.668708, 13.768575, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(104.668708, 13.768575, 0.000000),App.Vector(0.000000, 13.768575, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 2, 2, 3, 1))
constraintList.append(Sketcher.Constraint('Coincident', 3, 2, 4, 1))
constraintList.append(Sketcher.Constraint('Coincident', 4, 2, 5, 1))
constraintList.append(Sketcher.Constraint('Coincident', 5, 2, 2, 1))
constraintList.append(Sketcher.Constraint('Vertical', 2))
constraintList.append(Sketcher.Constraint('Vertical', 4))
constraintList.append(Sketcher.Constraint('Horizontal', 3))
constraintList.append(Sketcher.Constraint('Horizontal', 5))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

constraintList = []
constraintList.append(Sketcher.Constraint('PointOnObject', 2, 1, -2))
constraintList.append(Sketcher.Constraint('PointOnObject', 3, 2, 1))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('PointOnObject',4,2,1))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',5,3))


App.getDocument('Unnamed').getObject('Sketch').trim(4,App.Vector(104.678968,-3.751062,0))
App.getDocument('Unnamed').getObject('Sketch').trim(1,App.Vector(100.397891,-3.969549,0))
App.getDocument('Unnamed').getObject('Sketch').trim(0,App.Vector(39.806045,-3.934304,0))
App.getDocument('Unnamed').getObject('Sketch').trim(2,App.Vector(0.000000,-5.167353,0))
App.getDocument('Unnamed').getObject('Sketch').trim(2,App.Vector(17.915720,-12.855582,0))
App.getDocument('Unnamed').getObject('Sketch').trim(3,App.Vector(21.928537,12.855582,0))

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',3,1,-1,12.855582))
App.getDocument('Unnamed').getObject('Sketch').setDatum(11,App.Units.Quantity('15.000000 mm'))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',3,2))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(0.000000, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 20.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',4,__HOLE1_DIA__))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 4, 3, 0, 3))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(120.000000, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 10.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',5,__HOLE2_DIA__))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 5, 3, 1, 3))

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