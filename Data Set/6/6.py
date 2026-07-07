import FreeCAD
import PartDesign
import Sketcher
import Part

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

# --- 1. BASE BLOCK WITH U-CUTOUT ---
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
# 0: Bottom
geoList.append(Part.LineSegment(App.Vector(0.000000, 0.000000, 0.000000),App.Vector(100.000000, 0.000000, 0.000000)))
# 1: Right wall
geoList.append(Part.LineSegment(App.Vector(100.000000, 0.000000, 0.000000),App.Vector(100.000000, 50.000000, 0.000000)))
# 2: Top Right flat
geoList.append(Part.LineSegment(App.Vector(100.000000, 50.000000, 0.000000),App.Vector(70.000000, 50.000000, 0.000000)))
# 3: U-Cutout Arc (Bottom half of circle, from X=30 to X=70)
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(50.000000, 50.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 20.000000), 3.141593, 6.283185))
# 4: Top Left flat
geoList.append(Part.LineSegment(App.Vector(30.000000, 50.000000, 0.000000),App.Vector(0.000000, 50.000000, 0.000000)))
# 5: Left wall
geoList.append(Part.LineSegment(App.Vector(0.000000, 50.000000, 0.000000),App.Vector(0.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
# Close the perimeter exactly
constraintList.append(Sketcher.Constraint('Coincident', 0, 2, 1, 1))
constraintList.append(Sketcher.Constraint('Coincident', 1, 2, 2, 1))
constraintList.append(Sketcher.Constraint('Coincident', 2, 2, 3, 2))
constraintList.append(Sketcher.Constraint('Coincident', 3, 1, 4, 1))
constraintList.append(Sketcher.Constraint('Coincident', 4, 2, 5, 1))
constraintList.append(Sketcher.Constraint('Coincident', 5, 2, 0, 1))

# Keep walls perfectly straight
constraintList.append(Sketcher.Constraint('Horizontal', 0))
constraintList.append(Sketcher.Constraint('Vertical', 1))
constraintList.append(Sketcher.Constraint('Horizontal', 2))
constraintList.append(Sketcher.Constraint('Horizontal', 4))
constraintList.append(Sketcher.Constraint('Vertical', 5))

# Lock to Origin
constraintList.append(Sketcher.Constraint('Coincident', 0, 1, -1, 1))

# Dimensions
constraintList.append(Sketcher.Constraint('Distance', 0, 100.000000)) # Total Width
constraintList.append(Sketcher.Constraint('Distance', 1, 50.000000))  # Total Height
constraintList.append(Sketcher.Constraint('DistanceX', -1, 1, 3, 3, 50.000000)) # Arc Center X
constraintList.append(Sketcher.Constraint('DistanceY', -1, 1, 3, 3, 50.000000)) # Arc Center Y
constraintList.append(Sketcher.Constraint('Radius', 3, 20.000000)) # Arc Radius

App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList
App.ActiveDocument.recompute()

### Begin command PartDesign_Pad (Base)
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad')
App.getDocument('Unnamed').getObject('Pad').Profile = (App.getDocument('Unnamed').getObject('Sketch'), ['',])
App.getDocument('Unnamed').getObject('Pad').Length = 20.000000
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

# --- 2. TOP PINS ---
### Begin command PartDesign_NewSketch
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch001')
App.getDocument('Unnamed').getObject('Sketch001').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XY_Plane'])
# Offset the sketch exactly 50mm UP so it rests perfectly on top of the base block!
App.getDocument('Unnamed').getObject('Sketch001').AttachmentOffset = App.Placement(App.Vector(0.0, 0.0, 50.0), App.Rotation(0.0, 0.0, 0.0))
App.getDocument('Unnamed').getObject('Sketch001').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
### End command PartDesign_NewSketch

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
# Left Pin
geoList.append(Part.Circle(App.Vector(15.000000, 10.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 5.000000))
# Right Pin
geoList.append(Part.Circle(App.Vector(85.000000, 10.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 5.000000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
# Left Pin Constraints
constraintList.append(Sketcher.Constraint('Radius', 0, 5.000000))
constraintList.append(Sketcher.Constraint('DistanceX', -1, 1, 0, 3, 15.000000))
constraintList.append(Sketcher.Constraint('DistanceY', -1, 1, 0, 3, 10.000000))

# Right Pin Constraints
constraintList.append(Sketcher.Constraint('Radius', 1, 5.000000))
constraintList.append(Sketcher.Constraint('DistanceX', -1, 1, 1, 3, 85.000000))
constraintList.append(Sketcher.Constraint('DistanceY', -1, 1, 1, 3, 10.000000))

App.getDocument('Unnamed').getObject('Sketch001').addConstraint(constraintList)
del constraintList
App.ActiveDocument.recompute()

### Begin command PartDesign_Pad (Pins)
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad001')
App.getDocument('Unnamed').getObject('Pad001').Profile = (App.getDocument('Unnamed').getObject('Sketch001'), ['',])
App.getDocument('Unnamed').getObject('Pad001').Length = 30.000000
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