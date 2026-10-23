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
geoList.append(Part.LineSegment(App.Vector(0.000000, 0.000000, 0.000000),App.Vector(84.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,84.000000))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Horizontal',0))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 0, 1, -1, 1))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 0.000000, 0.000000),App.Vector(0.000000, 40.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,40.000000))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',1))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 1, 1, 0, 1))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 40.000000, 0.000000),App.Vector(84.000000, 40.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',2,84.000000))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Horizontal',2))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 2, 1, 1, 2))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(83.959223, 20.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 20.000042), 4.714428, 7.851943))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 3, 2, 2, 2))
constraintList.append(Sketcher.Constraint('Coincident', 3, 1, 0, 2))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Radius',3,20.000042))
App.getDocument('Unnamed').getObject('Sketch').setDatum(11,App.Units.Quantity('20.000000 mm'))

# --- Center hole — the ONLY thing safe to randomize on this sketch ---
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(83.999960, 20.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 8.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',4,__HOLE_DIA__))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 4, 3, 3, 3))

App.ActiveDocument.recompute()
App.getDocument('Unnamed').recompute()

### Begin command PartDesign_Pad
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad')
App.getDocument('Unnamed').getObject('Pad').Profile = (App.getDocument('Unnamed').getObject('Sketch'), ['',])
App.getDocument('Unnamed').getObject('Pad').Length = __PAD_LEN__
App.getDocument('Unnamed').getObject('Pad').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pad').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pad').Direction = (0, 0, 1)
App.ActiveDocument.recompute()
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
### End command PartDesign_Pad
App.getDocument('Unnamed').getObject('Sketch').Visibility = False

### Begin command Part_DatumPlane
obj = App.activeDocument().addObject('Part::DatumPlane','DatumPlane')
App.ActiveDocument.getObject('Body').addObject(obj)
App.getDocument('Unnamed').getObject('DatumPlane').AttachmentOffset = App.Placement(App.Vector(0.0000000000, 0.0000000000, -40.0000000000),  App.Rotation(0.0000000000, 0.0000000000, 0.0000000000))
App.getDocument('Unnamed').getObject('DatumPlane').MapReversed = False
App.getDocument('Unnamed').getObject('DatumPlane').AttachmentSupport = [(App.getDocument('Unnamed').getObject('Origin'),'XZ_Plane.')]
App.getDocument('Unnamed').getObject('DatumPlane').MapPathParameter = 0.000000
App.getDocument('Unnamed').getObject('DatumPlane').MapMode = 'FlatFace'
App.getDocument('Unnamed').getObject('DatumPlane').recompute()
### End command Part_DatumPlane

### Begin command PartDesign_CompSketches (Sketch001)
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch001')
App.getDocument('Unnamed').getObject('Sketch001').AttachmentSupport = (App.getDocument('Unnamed').getObject('DatumPlane'),[])
App.getDocument('Unnamed').getObject('Sketch001').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
### End command PartDesign_CompSketches

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 15.503569, 0.000000),App.Vector(50.000000, 15.503569, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',0,50.000000))
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Horizontal',0))
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('PointOnObject', 0, 1, -2))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(50.000000, 15.503569, 0.000000),App.Vector(50.000000, 37.503569, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',1,22.000000))
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Vertical',1))
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Coincident', 1, 1, 0, 2))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 15.503569, 0.000000),App.Vector(0.000000, 37.503569, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',2,22.000000))
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Vertical',2))
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Coincident', 2, 1, 0, 1))

App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',-1,1,0,15.503569))
App.getDocument('Unnamed').getObject('Sketch001').setDatum(9,App.Units.Quantity('__PAD_LEN__ mm'))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(25.000000, 37.927228, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 25.000106), 0.002911, 3.138682))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 3, 1, 1, 2))
constraintList.append(Sketcher.Constraint('Coincident', 3, 2, 2, 2))
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(constraintList)
del constraintList

App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Radius',3,25.000106))
App.getDocument('Unnamed').getObject('Sketch001').setDatum(12,App.Units.Quantity('25.000000 mm'))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(25.000000, 37.999964, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 6.000000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',4,__BOSS_HOLE_DIA__))
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Coincident', 4, 3, 3, 3))

App.ActiveDocument.recompute()
App.getDocument('Unnamed').recompute()

### Begin command PartDesign_Pad (Pad001)
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad001')
App.getDocument('Unnamed').getObject('Pad001').Profile = (App.getDocument('Unnamed').getObject('Sketch001'), ['',])
App.getDocument('Unnamed').getObject('Pad001').Length = __PAD1_LEN__
App.getDocument('Unnamed').getObject('Pad001').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pad001').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pad001').Direction = (0, -1, 0)
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pad001').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch001'), ['N_Axis'])
App.getDocument('Unnamed').getObject('Pad001').AlongSketchNormal = 1
App.getDocument('Unnamed').getObject('Pad001').SideType = 0
App.getDocument('Unnamed').getObject('Pad001').Type = 0
App.getDocument('Unnamed').getObject('Pad001').Type2 = 0
App.getDocument('Unnamed').getObject('Pad001').UpToFace = None
App.getDocument('Unnamed').getObject('Pad001').UpToFace2 = None
App.getDocument('Unnamed').getObject('Pad001').Reversed = 0
App.getDocument('Unnamed').getObject('Pad001').Offset = 0
App.getDocument('Unnamed').getObject('Pad001').Offset2 = 0
App.getDocument('Unnamed').recompute()
### End command PartDesign_Pad
App.getDocument('Unnamed').getObject('Pad').Visibility = False
App.getDocument('Unnamed').getObject('Sketch001').Visibility = False

### Begin command PartDesign_CompSketches (Sketch002)
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch002')
App.getDocument('Unnamed').getObject('Sketch002').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XZ_Plane'])
App.getDocument('Unnamed').getObject('Sketch002').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
### End command PartDesign_CompSketches

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 15.896892, 0.000000),App.Vector(50.000000, 15.896892, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch002').addGeometry(geoList,False)
del geoList

App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',0,50.000000))
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Horizontal',0))
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('PointOnObject', 0, 1, -2))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(50.000000, 15.896892, 0.000000),App.Vector(50.000000, 37.896892, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch002').addGeometry(geoList,False)
del geoList

App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',1,22.000000))
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Vertical',1))
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Coincident', 1, 1, 0, 2))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 15.896892, 0.000000),App.Vector(0.000000, 37.896892, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch002').addGeometry(geoList,False)
del geoList

App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',2,22.000000))
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Vertical',2))

App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',-1,1,0,15.896892))
App.getDocument('Unnamed').getObject('Sketch002').setDatum(8,App.Units.Quantity('__PAD_LEN__ mm'))
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Coincident',2,1,0,1))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(25.000000, 37.972981, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 25.000015), 0.001081, 3.140512))
App.getDocument('Unnamed').getObject('Sketch002').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 3, 2, 2, 2))
constraintList.append(Sketcher.Constraint('Coincident', 3, 1, 1, 2))
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(constraintList)
del constraintList

App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Radius',3,25.000015))
App.getDocument('Unnamed').getObject('Sketch002').setDatum(12,App.Units.Quantity('25.000000 mm'))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(25.000000, 37.999947, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 6.000000))
App.getDocument('Unnamed').getObject('Sketch002').addGeometry(geoList,False)
del geoList

App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Diameter',4,__BOSS_HOLE_DIA__))
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Coincident', 4, 3, 3, 3))

App.ActiveDocument.recompute()
App.getDocument('Unnamed').recompute()

### Begin command PartDesign_Pad (Pad002)
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad002')
App.getDocument('Unnamed').getObject('Pad002').Profile = (App.getDocument('Unnamed').getObject('Sketch002'), ['',])
App.getDocument('Unnamed').getObject('Pad002').Length = __PAD2_LEN__
App.getDocument('Unnamed').getObject('Pad002').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pad002').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pad002').Direction = (0, -1, 0)
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pad002').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch002'), ['N_Axis'])
App.getDocument('Unnamed').getObject('Pad002').AlongSketchNormal = 1
App.getDocument('Unnamed').getObject('Pad002').SideType = 0
App.getDocument('Unnamed').getObject('Pad002').Type = 0
App.getDocument('Unnamed').getObject('Pad002').Type2 = 0
App.getDocument('Unnamed').getObject('Pad002').UpToFace = None
App.getDocument('Unnamed').getObject('Pad002').UpToFace2 = None
App.getDocument('Unnamed').getObject('Pad002').Reversed = 1
App.getDocument('Unnamed').getObject('Pad002').Offset = 0
App.getDocument('Unnamed').getObject('Pad002').Offset2 = 0
App.getDocument('Unnamed').recompute()
App.ActiveDocument.recompute()
### End command PartDesign_Pad
App.getDocument('Unnamed').getObject('Pad001').Visibility = False
App.getDocument('Unnamed').getObject('Sketch002').Visibility = False
App.getDocument('Unnamed').getObject('DatumPlane').Visibility = False

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