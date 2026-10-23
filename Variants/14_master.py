# Macro Begin: C:\Users\pawar\AppData\Roaming\FreeCAD\v1-1\Macro\14.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
import FreeCAD
import FreeCAD as App
import Part
import PartDesign
# import PartDesignGui
import Sketcher
import Mesh

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

# Centered square (symmetric about origin)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)
geoList = []
geoList.append(Part.LineSegment(App.Vector(-9.000000, -9.000000, 0.000000),App.Vector(9.000000, -9.000000, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(9.000000, -9.000000, 0.000000),App.Vector(9.000000, 9.000000, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(9.000000, 9.000000, 0.000000),App.Vector(-9.000000, 9.000000, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(-9.000000, 9.000000, 0.000000),App.Vector(-9.000000, -9.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constrGeoList = []
constrGeoList.append(Part.Point(App.Vector(0.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(constrGeoList,True)
del constrGeoList

constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 0, 2, 1, 1))
constraintList.append(Sketcher.Constraint('Coincident', 1, 2, 2, 1))
constraintList.append(Sketcher.Constraint('Coincident', 2, 2, 3, 1))
constraintList.append(Sketcher.Constraint('Coincident', 3, 2, 0, 1))
constraintList.append(Sketcher.Constraint('Horizontal', 0))
constraintList.append(Sketcher.Constraint('Horizontal', 2))
constraintList.append(Sketcher.Constraint('Vertical', 1))
constraintList.append(Sketcher.Constraint('Vertical', 3))
constraintList.append(Sketcher.Constraint('Symmetric', 2, 1, 0, 1, 4, 1))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList


App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,1,3,2,__SIZE__))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,1,2,2,__SIZE__))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 4, 1, -1, 1))

App.ActiveDocument.recompute()
App.getDocument('Unnamed').recompute()
### Begin command PartDesign_Pad
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad')
App.getDocument('Unnamed').getObject('Pad').Profile = (App.getDocument('Unnamed').getObject('Sketch'), ['',])
App.getDocument('Unnamed').getObject('Pad').Length = __PAD_H__
App.getDocument('Unnamed').getObject('Pad').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pad').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pad').Direction = (0, 0, 1)
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pad').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'),['N_Axis'])
App.getDocument('Unnamed').getObject('Pad').AlongSketchNormal = 1
App.getDocument('Unnamed').getObject('Pad').SideType = 0
App.getDocument('Unnamed').getObject('Pad').Type = 0
App.getDocument('Unnamed').getObject('Pad').Type2 = 0
App.getDocument('Unnamed').getObject('Pad').UpToFace = None
App.getDocument('Unnamed').getObject('Pad').UpToFace2 = None
App.getDocument('Unnamed').getObject('Pad').Reversed = 0
App.getDocument('Unnamed').getObject('Pad').Offset = 0
App.getDocument('Unnamed').getObject('Pad').Offset2 = 0
App.ActiveDocument.recompute()
### End command PartDesign_Pad
App.getDocument('Unnamed').getObject('Sketch').Visibility = False

### Begin command PartDesign_NewSketch
# Face6 is the top face (z=PAD_H) of the centered square pad
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch001')
App.getDocument('Unnamed').getObject('Sketch001').AttachmentSupport = (App.getDocument('Unnamed').getObject('Pad'),['Face6',])
App.getDocument('Unnamed').getObject('Sketch001').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
### End command PartDesign_NewSketch

# Four corner circles (positions constrained via setDatum below)
# Initial positions are starting guesses; constraints set the final positions.
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
lastGeoId = len(ActiveSketch.Geometry)
geoList = []
geoList.append(Part.Circle(App.Vector(6.440913, 6.660893, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 0.825000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',0,__HOLE_DIA__))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
lastGeoId = len(ActiveSketch.Geometry)
geoList = []
geoList.append(Part.Circle(App.Vector(6.936379, -6.159151, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 0.825000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',1,__HOLE_DIA__))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
lastGeoId = len(ActiveSketch.Geometry)
geoList = []
geoList.append(Part.Circle(App.Vector(-6.379128, 6.598959, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 0.825000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',2,__HOLE_DIA__))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
lastGeoId = len(ActiveSketch.Geometry)
geoList = []
geoList.append(Part.Circle(App.Vector(-6.317194, -6.530746, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 0.825000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',3,__HOLE_DIA__))

# idx 4: Y distance between circle 1 (lower right) and circle 0 (upper right) = DELTA_Y
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('DistanceY',1,3,0,3,12.820044))
App.getDocument('Unnamed').getObject('Sketch001').setDatum(4,App.Units.Quantity('__DELTA_Y__ mm'))

# Horizontal alignments (top two circles at same Y; bottom two at same Y)
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Horizontal',2,3,0,3))
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Horizontal',1,3,3,3))

# Vertical alignments (left two circles at same X; right two at same X)
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Vertical',2,3,3,3))
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Vertical',1,3,0,3))

# idx 9: X distance between circle 3 (lower left) and circle 1 (lower right) = DELTA_X
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('DistanceX',3,3,1,3,14.100000))
App.getDocument('Unnamed').getObject('Sketch001').setDatum(9,App.Units.Quantity('__DELTA_X__ mm'))

# idx 10: X distance from origin to circle 1 (right column) = X_OFFSET
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('DistanceX',-1,1,1,3,7.219222))
App.getDocument('Unnamed').getObject('Sketch001').setDatum(10,App.Units.Quantity('__X_OFFSET__ mm'))

# idx 11: Y distance from H-axis to circle 2 (upper left) = Y_OFFSET
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',2,3,-1,5.532796))
App.getDocument('Unnamed').getObject('Sketch001').setDatum(11,App.Units.Quantity('__Y_OFFSET__ mm'))

App.ActiveDocument.recompute()
App.getDocument('Unnamed').recompute()
### Begin command PartDesign_Pocket
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pocket','Pocket')
App.getDocument('Unnamed').getObject('Pocket').Profile = (App.getDocument('Unnamed').getObject('Sketch001'), ['',])
App.getDocument('Unnamed').getObject('Pocket').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pocket').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pocket').Direction = (0, 0, -1)
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pocket').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch001'),['N_Axis'])
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
### End command PartDesign_Pocket
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
# Macro End: C:\Users\pawar\AppData\Roaming\FreeCAD\v1-1\Macro\14.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++