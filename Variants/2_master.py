
import FreeCAD
import FreeCAD as App
import Part
import PartDesign

import Sketcher
import Mesh


App.newDocument()

App.getDocument('Unnamed').addObject('PartDesign::Body','Body')
App.getDocument('Unnamed').getObject('Body').AllowCompound = True

App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch')
App.getDocument('Unnamed').getObject('Sketch').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XZ_Plane'])
App.getDocument('Unnamed').getObject('Sketch').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(0.000000, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 50.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',0,__OUTER_DIA__)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 0, 3, -1, 1))


App.ActiveDocument.recompute()

App.getDocument('Unnamed').recompute()

App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad')
App.getDocument('Unnamed').getObject('Pad').Profile = (App.getDocument('Unnamed').getObject('Sketch'), ['',])
App.getDocument('Unnamed').getObject('Pad').Length = 10
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pad').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'),['N_Axis'])
App.getDocument('Unnamed').getObject('Sketch').Visibility = False
App.ActiveDocument.recompute()

App.getDocument('Unnamed').getObject('Pad').Length = __BODY_HEIGHT__
App.getDocument('Unnamed').getObject('Pad').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pad').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pad').Direction = (0, -1, 0)
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

App.getDocument('Unnamed').getObject('Sketch').Visibility = False

App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch001')
App.getDocument('Unnamed').getObject('Sketch001').AttachmentSupport = (App.getDocument('Unnamed').getObject('Pad'),['Face3',])
App.getDocument('Unnamed').getObject('Sketch001').MapMode = 'FlatFace'
App.ActiveDocument.recompute()

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(0.000000, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 40.000000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',0,__BOSS_DIA__)) 
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Coincident', 0, 3, -1, 1))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(0.000000, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 25.000000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',1,__HOLE_DIA__)) 
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Coincident', 1, 3, 0, 3))



App.ActiveDocument.recompute()

App.getDocument('Unnamed').recompute()

App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad001')
App.getDocument('Unnamed').getObject('Pad001').Profile = (App.getDocument('Unnamed').getObject('Sketch001'), ['',])
App.getDocument('Unnamed').getObject('Pad001').Length = 10
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pad001').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch001'),['N_Axis'])
App.getDocument('Unnamed').getObject('Sketch001').Visibility = False
App.ActiveDocument.recompute()

App.getDocument('Unnamed').getObject('Pad001').Length = __BOSS_HEIGHT__
App.getDocument('Unnamed').getObject('Pad001').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pad001').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pad001').Direction = (0, -1, 0)
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
App.getDocument('Unnamed').getObject('Pad').Visibility = False

App.getDocument('Unnamed').getObject('Sketch001').Visibility = False

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
