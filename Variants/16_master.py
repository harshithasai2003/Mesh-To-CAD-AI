import FreeCAD
import FreeCAD as App
import Part
import PartDesign
# import PartDesignGui
import Sketcher
import Mesh

# Gui.runCommand('Std_DlgMacroRecord',0)
### Begin command Std_New
App.newDocument()
# App.setActiveDocument("Unnamed")
# App.ActiveDocument=App.getDocument("Unnamed")
# Gui.ActiveDocument=Gui.getDocument("Unnamed")
# Gui.activeDocument().activeView().viewDefaultOrientation()
### End command Std_New
### Begin command PartDesign_CompSketches
App.getDocument('Unnamed').addObject('PartDesign::Body','Body')
App.getDocument('Unnamed').getObject('Body').AllowCompound = True
# Gui.getDocument('Unnamed').ActiveView.setActiveObject('pdbody',App.getDocument('Unnamed').getObject('Body'),'')
### End command PartDesign_CompSketches
# Gui.Selection.addSelection('Unnamed','Body','Origin.XY_Plane.',13.9835,15.8392,0)
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch')
App.getDocument('Unnamed').getObject('Sketch').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XY_Plane'])
App.getDocument('Unnamed').getObject('Sketch').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
# Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Sketch.')
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CreateOblong',0)
# Gui.runCommand('Sketcher_CompCreateRectangles',2)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(-19.281986, 14.324642, 0.000000),App.Vector(-19.281986, -57.675358, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(-5.281986, -71.675358, 0.000000),App.Vector(66.718014, -71.675358, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(80.718014, -57.675358, 0.000000),App.Vector(80.718014, 14.324642, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(66.718014, 28.324642, 0.000000),App.Vector(-5.281986, 28.324642, 0.000000)))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(-5.281986, 14.324642, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 14.000000), 1.570796, 3.141593))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(-5.281986, -57.675358, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 14.000000), 3.141593, 4.712389))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(66.718014, -57.675358, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 14.000000), 4.712389, 6.283185))
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(66.718014, 14.324642, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 14.000000), 0.000000, 1.570796))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constrGeoList = []
constrGeoList.append(Part.Point(App.Vector(-19.281986, 28.324642, 0.000000)))
constrGeoList.append(Part.Point(App.Vector(80.718014, -71.675358, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(constrGeoList,True)
del constrGeoList

constraintList = []
constraintList.append(Sketcher.Constraint('Tangent', 0, 1, 4, 2))
constraintList.append(Sketcher.Constraint('Tangent', 0, 2, 5, 1))
constraintList.append(Sketcher.Constraint('Tangent', 1, 1, 5, 2))
constraintList.append(Sketcher.Constraint('Tangent', 1, 2, 6, 1))
constraintList.append(Sketcher.Constraint('Tangent', 2, 1, 6, 2))
constraintList.append(Sketcher.Constraint('Tangent', 2, 2, 7, 1))
constraintList.append(Sketcher.Constraint('Tangent', 3, 1, 7, 2))
constraintList.append(Sketcher.Constraint('Tangent', 3, 2, 4, 1))
constraintList.append(Sketcher.Constraint('Vertical', 0))
constraintList.append(Sketcher.Constraint('Vertical', 2))
constraintList.append(Sketcher.Constraint('Horizontal', 1))
constraintList.append(Sketcher.Constraint('Horizontal', 3))
constraintList.append(Sketcher.Constraint('Equal', 4, 5))
constraintList.append(Sketcher.Constraint('Equal', 5, 6))
constraintList.append(Sketcher.Constraint('Equal', 6, 7))
constraintList.append(Sketcher.Constraint('PointOnObject', 8, 1, 0))
constraintList.append(Sketcher.Constraint('PointOnObject', 8, 1, 3))
constraintList.append(Sketcher.Constraint('PointOnObject', 9, 1, 1))
constraintList.append(Sketcher.Constraint('PointOnObject', 9, 1, 2))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,1,2,2,__RECT_SIZE__)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,1,3,2,__RECT_SIZE__)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Radius',5,__CORNER_RADIUS__)) 
constraintList = []
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',33.2365,28.3246,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.H_Axis',40.0582,0,0.002,False)
### Begin command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',-1,1,3,28.324642)) 
### End command Sketcher_CompDimensionTools
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').setDatum(22,App.Units.Quantity('__HALF_SIZE__ mm'))
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge1',-19.2729,-15.4518,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.V_Axis',0,-16.7511,0.002,False)
### Begin command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',-2,1,0,19.272928)) 
### End command Sketcher_CompDimensionTools
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').setDatum(23,App.Units.Quantity('__HALF_SIZE__ mm'))
# Gui.runCommand('Sketcher_CompCreateConic',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(-36.000000, 36.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 4.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',10,__BOLT_HOLE_DIA__)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 10, 3, 4, 3))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(36.000000, 36.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 4.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',11,__BOLT_HOLE_DIA__)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 11, 3, 7, 3))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(36.000000, -36.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 4.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',12,__BOLT_HOLE_DIA__)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 12, 3, 6, 3))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(-36.000000, -36.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 4.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',13,__BOLT_HOLE_DIA__)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 13, 3, 5, 3))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(0.000000, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 30.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',14,__CENTER_HOLE_DIA__)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 14, 3, -1, 1))


App.ActiveDocument.recompute()
App.getDocument('Unnamed').recompute()
### Begin command PartDesign_Pad
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad')
App.getDocument('Unnamed').getObject('Pad').Profile = (App.getDocument('Unnamed').getObject('Sketch'), ['',])
App.getDocument('Unnamed').getObject('Pad').Length = 10
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pad').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'),['N_Axis'])
App.getDocument('Unnamed').getObject('Sketch').Visibility = False
App.ActiveDocument.recompute()
### End command PartDesign_Pad
App.getDocument('Unnamed').getObject('Pad').Length = __PAD_HEIGHT__
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
App.getDocument('Unnamed').purgeTouched()
App.getDocument('Unnamed').recompute()
App.getDocument('Unnamed').getObject('Sketch').Visibility = False
### Begin command PartDesign_NewSketch
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch001')
App.getDocument('Unnamed').getObject('Sketch001').AttachmentSupport = (App.getDocument('Unnamed').getObject('Pad'),['Face15',])
App.getDocument('Unnamed').getObject('Sketch001').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
### End command PartDesign_NewSketch
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(-35.584373, 35.579830, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 5.000000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',0,__BOLT_SPOTFACE_DIA__)) 
constraintList = []
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(35.718258, 35.742249, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 5.000000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',1,__BOLT_SPOTFACE_DIA__)) 
constraintList = []
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(36.043098, -36.210068, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 5.000000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',2,__BOLT_SPOTFACE_DIA__)) 
constraintList = []
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(-35.746799, -36.534908, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 5.000000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',3,__BOLT_SPOTFACE_DIA__)) 
constraintList = []
### Begin command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',0,3,-1,35.579830)) 
### End command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch001').setDatum(4,App.Units.Quantity('__BOLT_POS__ mm'))
### Begin command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',0,3,-2,35.584373)) 
### End command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch001').setDatum(5,App.Units.Quantity('__BOLT_POS__ mm'))
### Begin command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',1,3,-2,35.718258)) 
### End command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch001').setDatum(6,App.Units.Quantity('__BOLT_POS__ mm'))
### Begin command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',1,3,-1,35.742249)) 
### End command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch001').setDatum(7,App.Units.Quantity('__BOLT_POS__ mm'))
### Begin command Sketcher_CompHorVer
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Horizontal',2,3,3,3))
### End command Sketcher_CompHorVer
### Begin command Sketcher_CompDimensionTools

App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('DistanceY',3,3,-1,1,36.210068)) 
App.getDocument('Unnamed').getObject('Sketch001').setDatum(9,App.Units.Quantity('__BOLT_POS__ mm'))
### Begin command Sketcher_ConstrainVertical
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Vertical',3,3,0,3))
### End command Sketcher_ConstrainVertical
### Begin command Sketcher_ConstrainVertical
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Vertical',2,3,1,3))


lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(0.000000, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 32.500000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',4,__CENTER_SPOTFACE_DIA__)) 
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Coincident', 4, 3, -1, 1))


### End command Sketcher_ConstrainVertical
App.ActiveDocument.recompute()
App.getDocument('Unnamed').recompute()
### Begin command PartDesign_Pocket
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pocket','Pocket')
App.getDocument('Unnamed').getObject('Pocket').Profile = (App.getDocument('Unnamed').getObject('Sketch001'), ['',])
App.getDocument('Unnamed').getObject('Pocket').Length = 1
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pocket').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch001'),['N_Axis'])
App.getDocument('Unnamed').getObject('Sketch001').Visibility = False
App.ActiveDocument.recompute()
### End command PartDesign_Pocket
App.getDocument('Unnamed').getObject('Pocket').Length = __SPOTFACE_DEPTH__
App.getDocument('Unnamed').getObject('Pocket').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pocket').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pocket').Direction = (0, 0, -1)
App.getDocument('Unnamed').getObject('Pocket').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch001'), ['N_Axis'])
App.getDocument('Unnamed').getObject('Pocket').AlongSketchNormal = 1
App.getDocument('Unnamed').getObject('Pocket').SideType = 0
App.getDocument('Unnamed').getObject('Pocket').Type = 0
App.getDocument('Unnamed').getObject('Pocket').Type2 = 0
App.getDocument('Unnamed').getObject('Pocket').UpToFace = None
App.getDocument('Unnamed').getObject('Pocket').UpToFace2 = None
App.getDocument('Unnamed').getObject('Pocket').Reversed = 0
App.getDocument('Unnamed').getObject('Pocket').Offset = 0
App.getDocument('Unnamed').getObject('Pocket').Offset2 = 0
App.getDocument('Unnamed').purgeTouched()
App.getDocument('Unnamed').recompute()
App.getDocument('Unnamed').getObject('Pad').Visibility = False
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