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
geoList.append(Part.LineSegment(App.Vector(0.000000, 0.000000, 0.000000),App.Vector(__W__, 0.000000, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(__W__, 0.000000, 0.000000),App.Vector(__W__, __H__, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(__W__, __H__, 0.000000),App.Vector(__CUTOUT_X_RIGHT__, __H__, 0.000000)))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(__CUTOUT_CX__, __H__, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), __CUTOUT_R__), 3.141593, 6.283185))
geoList.append(Part.LineSegment(App.Vector(__CUTOUT_X_LEFT__, __H__, 0.000000),App.Vector(0.000000, __H__, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(0.000000, __H__, 0.000000),App.Vector(0.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 0, 2, 1, 1))
constraintList.append(Sketcher.Constraint('Coincident', 1, 2, 2, 1))
constraintList.append(Sketcher.Constraint('Coincident', 2, 2, 3, 2))
constraintList.append(Sketcher.Constraint('Coincident', 3, 1, 4, 1))
constraintList.append(Sketcher.Constraint('Coincident', 4, 2, 5, 1))
constraintList.append(Sketcher.Constraint('Coincident', 5, 2, 0, 1))
constraintList.append(Sketcher.Constraint('Horizontal', 0))
constraintList.append(Sketcher.Constraint('Vertical', 1))
constraintList.append(Sketcher.Constraint('Horizontal', 2))
constraintList.append(Sketcher.Constraint('Horizontal', 4))
constraintList.append(Sketcher.Constraint('Vertical', 5))
constraintList.append(Sketcher.Constraint('Coincident', 0, 1, -1, 1))
constraintList.append(Sketcher.Constraint('Distance', 0, __W__))
constraintList.append(Sketcher.Constraint('Distance', 1, __H__))
constraintList.append(Sketcher.Constraint('DistanceX', -1, 1, 3, 3, __CUTOUT_CX__))
constraintList.append(Sketcher.Constraint('DistanceY', -1, 1, 3, 3, __H__))
constraintList.append(Sketcher.Constraint('Radius', 3, __CUTOUT_R__))

App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList
App.ActiveDocument.recompute()

### Begin command PartDesign_Pad (Base)
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad')
App.getDocument('Unnamed').getObject('Pad').Profile = (App.getDocument('Unnamed').getObject('Sketch'), ['',])
App.getDocument('Unnamed').getObject('Pad').Length = __BASE_THICK__
App.getDocument('Unnamed').getObject('Pad').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pad').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pad').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'), ['N_Axis'])
App.getDocument('Unnamed').getObject('Pad').AlongSketchNormal = 1
App.getDocument('Unnamed').getObject('Pad').Type = 0
App.getDocument('Unnamed').getObject('Pad').Reversed = 1

App.getDocument('Unnamed').getObject('Body').Tip = App.getDocument('Unnamed').getObject('Pad')
App.getDocument('Unnamed').recompute()
App.ActiveDocument.recompute()
### End command PartDesign_Pad

App.getDocument('Unnamed').getObject('Sketch').Visibility = False

### Begin command PartDesign_NewSketch
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch001')
App.getDocument('Unnamed').getObject('Sketch001').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XY_Plane'])
App.getDocument('Unnamed').getObject('Sketch001').AttachmentOffset = App.Placement(App.Vector(0.0, 0.0, __H__), App.Rotation(0.0, 0.0, 0.0))
App.getDocument('Unnamed').getObject('Sketch001').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
### End command PartDesign_NewSketch

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(__PIN_X_LEFT__, __PIN_Y__, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), __PIN_R__))
geoList.append(Part.Circle(App.Vector(__PIN_X_RIGHT__, __PIN_Y__, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), __PIN_R__))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList.append(Sketcher.Constraint('Radius', 0, __PIN_R__))
constraintList.append(Sketcher.Constraint('DistanceX', -1, 1, 0, 3, __PIN_X_LEFT__))
constraintList.append(Sketcher.Constraint('DistanceY', -1, 1, 0, 3, __PIN_Y__))
constraintList.append(Sketcher.Constraint('Radius', 1, __PIN_R__))
constraintList.append(Sketcher.Constraint('DistanceX', -1, 1, 1, 3, __PIN_X_RIGHT__))
constraintList.append(Sketcher.Constraint('DistanceY', -1, 1, 1, 3, __PIN_Y__))

App.getDocument('Unnamed').getObject('Sketch001').addConstraint(constraintList)
del constraintList
App.ActiveDocument.recompute()

### Begin command PartDesign_Pad (Pins)
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad001')
App.getDocument('Unnamed').getObject('Pad001').Profile = (App.getDocument('Unnamed').getObject('Sketch001'), ['',])
App.getDocument('Unnamed').getObject('Pad001').Length = __PIN_HEIGHT__
App.getDocument('Unnamed').getObject('Pad001').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pad001').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pad001').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch001'), ['N_Axis'])
App.getDocument('Unnamed').getObject('Pad001').AlongSketchNormal = 1
App.getDocument('Unnamed').getObject('Pad001').Type = 0
App.getDocument('Unnamed').getObject('Pad001').Reversed = 0

App.getDocument('Unnamed').getObject('Body').Tip = App.getDocument('Unnamed').getObject('Pad001')
App.getDocument('Unnamed').recompute()
App.ActiveDocument.recompute()
### End command PartDesign_Pad

App.getDocument('Unnamed').getObject('Sketch001').Visibility = False

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