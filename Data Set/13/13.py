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

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(0.000000, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 25.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 0, 3, -1, 1))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter', 0, 50.000000))

App.ActiveDocument.recompute()

### Begin command PartDesign_Pad
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad')
App.getDocument('Unnamed').getObject('Pad').Profile = (App.getDocument('Unnamed').getObject('Sketch'), ['',])
App.getDocument('Unnamed').getObject('Pad').Length = 10.000000
App.getDocument('Unnamed').getObject('Pad').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pad').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pad').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'), ['N_Axis'])
App.getDocument('Unnamed').getObject('Pad').AlongSketchNormal = 1
App.getDocument('Unnamed').getObject('Pad').Midplane = 1
App.getDocument('Unnamed').getObject('Pad').Type = 0
App.getDocument('Unnamed').getObject('Pad').Type2 = 0
App.getDocument('Unnamed').getObject('Pad').UpToFace = None
App.getDocument('Unnamed').getObject('Pad').UpToFace2 = None
App.getDocument('Unnamed').getObject('Pad').Reversed = 0
App.getDocument('Unnamed').getObject('Pad').Offset = 0
App.getDocument('Unnamed').getObject('Pad').Offset2 = 0

App.getDocument('Unnamed').getObject('Body').Tip = App.getDocument('Unnamed').getObject('Pad')

App.getDocument('Unnamed').recompute()
App.ActiveDocument.recompute()
### End command PartDesign_Pad

App.getDocument('Unnamed').getObject('Sketch').Visibility = False

### Begin command PartDesign_NewSketch
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch001')
App.getDocument('Unnamed').getObject('Sketch001').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XY_Plane'])
App.getDocument('Unnamed').getObject('Sketch001').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
### End command PartDesign_NewSketch

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(25.000000, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 3.000000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('DistanceX', -1, 1, 0, 3, 25.000000))
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 0, 3, 0.000000))
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Radius', 0, 3.000000))

App.ActiveDocument.recompute()

### Begin command PartDesign_Groove
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Groove','Groove')
App.getDocument('Unnamed').getObject('Groove').Profile = (App.getDocument('Unnamed').getObject('Sketch001'), ['',])
App.getDocument('Unnamed').getObject('Groove').Angle = 360.000000
App.getDocument('Unnamed').getObject('Groove').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch001'), ['V_Axis'])
App.getDocument('Unnamed').getObject('Groove').Midplane = 0
App.getDocument('Unnamed').getObject('Groove').Reversed = 0
App.getDocument('Unnamed').getObject('Groove').Type = 0
App.getDocument('Unnamed').getObject('Groove').UpToFace = None

App.getDocument('Unnamed').getObject('Body').Tip = App.getDocument('Unnamed').getObject('Groove')

App.getDocument('Unnamed').recompute()
App.ActiveDocument.recompute()
### End command PartDesign_Groove

App.getDocument('Unnamed').getObject('Sketch001').Visibility = False