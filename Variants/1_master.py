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
geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 0.000000, 0.000000),App.Vector(0.000000, 80.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,__H__))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',0))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 0, 1, -1, 1))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 80.000000, 0.000000),App.Vector(12.000000, 80.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,__W_SHELF__))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Horizontal',1))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 1, 1, 0, 2))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
geoList = []
geoList.append(Part.LineSegment(App.Vector(12.000000, 80.000000, 0.000000),App.Vector(12.000000, 12.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',2,__H_INNER__))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',2))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 2, 1, 1, 2))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
geoList = []
geoList.append(Part.LineSegment(App.Vector(12.000000, 12.000000, 0.000000),App.Vector(80.000000, 12.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',3,__H_INNER__))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Horizontal',3))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 3, 1, 2, 2))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
geoList = []
geoList.append(Part.LineSegment(App.Vector(80.000000, 12.000000, 0.000000),App.Vector(80.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,__W_SHELF__))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',4))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 4, 1, 3, 2))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
geoList = []
geoList.append(Part.LineSegment(App.Vector(80.000000, 0.000000, 0.000000),App.Vector(0.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList
constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 5, 1, 4, 2))
constraintList.append(Sketcher.Constraint('Coincident', 5, 2, 0, 1))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

App.ActiveDocument.recompute()
App.getDocument('Unnamed').recompute()


App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad')
App.getDocument('Unnamed').getObject('Pad').Profile = (App.getDocument('Unnamed').getObject('Sketch'), ['',])
App.getDocument('Unnamed').getObject('Pad').Length = __PAD_W__
App.getDocument('Unnamed').getObject('Pad').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pad').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pad').Direction = (0, -1, 0)
App.ActiveDocument.recompute()
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
App.getDocument('Unnamed').recompute()
App.ActiveDocument.recompute()

App.getDocument('Unnamed').getObject('Sketch').Visibility = False


App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Fillet','Fillet')
App.getDocument('Unnamed').getObject('Fillet').Base = (App.getDocument('Unnamed').getObject('Pad'),['Edge16','Edge7','Edge6','Edge15',])
App.getDocument('Unnamed').getObject('Pad').Visibility = False
App.ActiveDocument.recompute()

App.getDocument('Unnamed').getObject('Fillet').Radius = __FILLET_R__
App.getDocument('Unnamed').getObject('Fillet').Base = (App.getDocument('Unnamed').getObject('Pad'),["Edge16","Edge7","Edge6","Edge15",])
App.getDocument('Unnamed').getObject('Fillet').Radius = __FILLET_R__
App.getDocument('Unnamed').recompute()
App.getDocument('Unnamed').getObject('Pad').Visibility = False


App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch001')
App.getDocument('Unnamed').getObject('Sketch001').AttachmentSupport = (App.getDocument('Unnamed').getObject('Fillet'),['Face8',])
App.getDocument('Unnamed').getObject('Sketch001').MapMode = 'FlatFace'
App.ActiveDocument.recompute()



ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
geoList = []
geoList.append(Part.Circle(App.Vector(26.182484, 68.096939, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 5.000000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',0,__HOLE_DIA1__))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
geoList = []
geoList.append(Part.Circle(App.Vector(-26.271509, 66.409828, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 5.000000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',1,__HOLE_DIA1__))


App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',0,3,-1,68.096939))
App.getDocument('Unnamed').getObject('Sketch001').setDatum(2,App.Units.Quantity('__HOLE_Y1__ mm'))

App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',0,3,-2,26.182484))
App.getDocument('Unnamed').getObject('Sketch001').setDatum(3,App.Units.Quantity('__HOLE_X1__ mm'))

App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',1,3,-2,26.271509))
App.getDocument('Unnamed').getObject('Sketch001').setDatum(4,App.Units.Quantity('__HOLE_X1__ mm'))

App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',1,3,-1,66.409828))
App.getDocument('Unnamed').getObject('Sketch001').setDatum(5,App.Units.Quantity('__HOLE_Y1__ mm'))

App.ActiveDocument.recompute()
App.getDocument('Unnamed').recompute()


App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pocket','Pocket')
App.getDocument('Unnamed').getObject('Pocket').Profile = (App.getDocument('Unnamed').getObject('Sketch001'), ['',])
App.getDocument('Unnamed').getObject('Pocket').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pocket').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pocket').Direction = (-1, 0, 0)
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pocket').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch001'), ['N_Axis'])
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
App.ActiveDocument.recompute()

App.getDocument('Unnamed').getObject('Fillet').Visibility = False
App.getDocument('Unnamed').getObject('Sketch001').Visibility = False


App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch002')
App.getDocument('Unnamed').getObject('Sketch002').AttachmentSupport = (App.getDocument('Unnamed').getObject('Pocket'),['Face12',])
App.getDocument('Unnamed').getObject('Sketch002').MapMode = 'FlatFace'
App.ActiveDocument.recompute()



ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')
geoList = []
geoList.append(Part.Circle(App.Vector(64.162048, 25.404104, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 5.000000))
App.getDocument('Unnamed').getObject('Sketch002').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Diameter',0,__HOLE_DIA2__))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')
geoList = []
geoList.append(Part.Circle(App.Vector(64.536713, -27.423435, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 5.000000))
App.getDocument('Unnamed').getObject('Sketch002').addGeometry(geoList,False)
del geoList
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Diameter',1,__HOLE_DIA2__))


App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',0,3,-1,25.404104))
App.getDocument('Unnamed').getObject('Sketch002').setDatum(2,App.Units.Quantity('__HOLE_Y3__ mm'))

App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',1,3,-1,27.423435))
App.getDocument('Unnamed').getObject('Sketch002').setDatum(3,App.Units.Quantity('__HOLE_Y3__ mm'))

App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',1,3,-2,64.536713))
App.getDocument('Unnamed').getObject('Sketch002').setDatum(4,App.Units.Quantity('__HOLE_X3__ mm'))

App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',0,3,-2,64.162048))
App.getDocument('Unnamed').getObject('Sketch002').setDatum(5,App.Units.Quantity('__HOLE_X3__ mm'))

App.ActiveDocument.recompute()
App.getDocument('Unnamed').recompute()


App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pocket','Pocket001')
App.getDocument('Unnamed').getObject('Pocket001').Profile = (App.getDocument('Unnamed').getObject('Sketch002'), ['',])
App.getDocument('Unnamed').getObject('Pocket001').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pocket001').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pocket001').Direction = (0, 0, -1)
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pocket001').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch002'), ['N_Axis'])
App.getDocument('Unnamed').getObject('Pocket001').AlongSketchNormal = 1
App.getDocument('Unnamed').getObject('Pocket001').SideType = 0
App.getDocument('Unnamed').getObject('Pocket001').Type = 1
App.getDocument('Unnamed').getObject('Pocket001').Type2 = 0
App.getDocument('Unnamed').getObject('Pocket001').UpToFace = None
App.getDocument('Unnamed').getObject('Pocket001').UpToFace2 = None
App.getDocument('Unnamed').getObject('Pocket001').Reversed = 0
App.getDocument('Unnamed').getObject('Pocket001').Offset = 0
App.getDocument('Unnamed').getObject('Pocket001').Offset2 = 0
App.getDocument('Unnamed').recompute()
App.ActiveDocument.recompute()

App.getDocument('Unnamed').getObject('Pocket').Visibility = False
App.getDocument('Unnamed').getObject('Sketch002').Visibility = False

App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Fillet','Fillet001')
App.getDocument('Unnamed').getObject('Fillet001').Base = (App.getDocument('Unnamed').getObject('Pocket001'),['Edge33',])
App.getDocument('Unnamed').getObject('Pocket001').Visibility = False
App.ActiveDocument.recompute()

App.getDocument('Unnamed').getObject('Fillet001').Radius = __FILLET2_R__
App.getDocument('Unnamed').getObject('Fillet001').Base = (App.getDocument('Unnamed').getObject('Pocket001'),["Edge33",])
App.getDocument('Unnamed').getObject('Fillet001').Radius = __FILLET2_R__
App.getDocument('Unnamed').recompute()
App.getDocument('Unnamed').getObject('Pocket001').Visibility = False


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