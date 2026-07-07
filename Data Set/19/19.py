# Macro Begin: C:\Users\pawar\AppData\Roaming\FreeCAD\v1-1\Macro\19.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
import FreeCAD
import PartDesign
import PartDesignGui
import Sketcher

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
# Gui.Selection.addSelection('Unnamed','Body','Origin.XY_Plane.',18.5432,19.3064,0)
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch')
App.getDocument('Unnamed').getObject('Sketch').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XY_Plane'])
App.getDocument('Unnamed').getObject('Sketch').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
# Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Sketch.')
# ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
# tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
# ActiveSketch.ViewObject.TempoVis = tv
# if ActiveSketch.ViewObject.EditingWorkbench:
#   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
# if ActiveSketch.ViewObject.HideDependent:
#   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Body'), 'Sketch.'))
# if ActiveSketch.ViewObject.ShowSupport:
#   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not (ref[0].isDerivedFrom("App::Plane") or ref[0].isDerivedFrom("App::LocalCoordinateSystem"))])
# if ActiveSketch.ViewObject.ShowLinks:
#   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
# tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
# tv.hide(ActiveSketch)
# del(tv)
# del(ActiveSketch)
# 
# ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
# if ActiveSketch.ViewObject.RestoreCamera:
#   ActiveSketch.ViewObject.TempoVis.saveCamera()
#   if ActiveSketch.ViewObject.ForceOrtho:
#     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
# 
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompCreateConic',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(0.000000, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 40.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',0,80.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 0, 3, -1, 1))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(129.894440, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 20.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',1,40.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('PointOnObject', 1, 3, -1))


# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex2',129.894,0,0.014,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.V_Axis',0,19.0507,0.002,False)
### Begin command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,3,-2,129.894440)) 
### End command Sketcher_CompDimensionTools
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').setDatum(4,App.Units.Quantity('120.000000 mm'))
# Gui.runCommand('Sketcher_CompCreateRectangles',0)
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

# Gui.Selection.addSelection('Unnamed','Body','Sketch.Vertex8',104.669,13.7686,0.014,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge2',105.5,13.7658,0.008,False)
### Begin command Sketcher_ConstrainCoincidentUnified
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('PointOnObject',4,2,1))
### End command Sketcher_ConstrainCoincidentUnified
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge6',86.1337,12.8556,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',84.4813,-12.8556,0.008,False)
### Begin command Sketcher_ConstrainEqual
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',5,3))
### End command Sketcher_ConstrainEqual
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompCurveEdition',0)
App.getDocument('Unnamed').getObject('Sketch').trim(4,App.Vector(104.678968,-3.751062,0))
App.getDocument('Unnamed').getObject('Sketch').trim(1,App.Vector(100.397891,-3.969549,0))
App.getDocument('Unnamed').getObject('Sketch').trim(0,App.Vector(39.806045,-3.934304,0))
App.getDocument('Unnamed').getObject('Sketch').trim(2,App.Vector(0.000000,-5.167353,0))
App.getDocument('Unnamed').getObject('Sketch').trim(2,App.Vector(17.915720,-12.855582,0))
App.getDocument('Unnamed').getObject('Sketch').trim(3,App.Vector(21.928537,12.855582,0))
# Gui.Selection.addSelection('Unnamed','Body','Sketch.H_Axis',55.6834,0,0.002,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',56.3916,12.8556,0.008,False)
### Begin command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',3,1,-1,12.855582)) 
### End command Sketcher_CompDimensionTools
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').setDatum(11,App.Units.Quantity('15.000000 mm'))
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',85.6616,15,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge3',86.8418,-12.8556,0.008,False)
### Begin command Sketcher_ConstrainEqual
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',3,2))
### End command Sketcher_ConstrainEqual
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompCreateConic',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(0.000000, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 20.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',4,40.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 4, 3, 0, 3))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(120.000000, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 10.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',5,20.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 5, 3, 1, 3))


# Gui.getDocument('Unnamed').resetEdit()
App.ActiveDocument.recompute()
# ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
# tv = ActiveSketch.ViewObject.TempoVis
# if tv:
#   tv.restore()
# ActiveSketch.ViewObject.TempoVis = None
# del(tv)
# del(ActiveSketch)
# 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.')
App.getDocument('Unnamed').recompute()
### Begin command PartDesign_Pad
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad')
App.getDocument('Unnamed').getObject('Pad').Profile = (App.getDocument('Unnamed').getObject('Sketch'), ['',])
App.getDocument('Unnamed').getObject('Pad').Length = 10
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pad').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'),['N_Axis'])
App.getDocument('Unnamed').getObject('Sketch').Visibility = False
App.ActiveDocument.recompute()
# App.getDocument('Unnamed').getObject('Pad').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Pad').ViewObject.ShapeAppearance)
# App.getDocument('Unnamed').getObject('Pad').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Pad').ViewObject.LineColor)
# App.getDocument('Unnamed').getObject('Pad').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Pad').ViewObject.PointColor)
# App.getDocument('Unnamed').getObject('Pad').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Pad').ViewObject.Transparency)
# App.getDocument('Unnamed').getObject('Pad').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Pad').ViewObject.DisplayMode)
# Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Pad.')
# Gui.Selection.clearSelection()
### End command PartDesign_Pad
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Pad').Length = 10.000000
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
# Gui.getDocument('Unnamed').resetEdit()
App.getDocument('Unnamed').getObject('Sketch').Visibility = False
# Macro End: C:\Users\pawar\AppData\Roaming\FreeCAD\v1-1\Macro\19.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
