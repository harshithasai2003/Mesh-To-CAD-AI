# Macro Begin: C:\Users\pawar\AppData\Roaming\FreeCAD\v1-1\Macro\14.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
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
# Gui.runCommand('Std_OrthographicCamera',1)
### Begin command PartDesign_CompSketches
App.getDocument('Unnamed').addObject('PartDesign::Body','Body')
App.getDocument('Unnamed').getObject('Body').AllowCompound = True
# Gui.getDocument('Unnamed').ActiveView.setActiveObject('pdbody',App.getDocument('Unnamed').getObject('Body'),'')
### End command PartDesign_CompSketches
# Gui.Selection.addSelection('Unnamed','Body','Origin.XY_Plane.',16.0135,17.7183,-4.7848e-15)
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch')
App.getDocument('Unnamed').getObject('Sketch').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XY_Plane'])
App.getDocument('Unnamed').getObject('Sketch').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
# Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Sketch.')
# import Show
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
# Gui.runCommand('Sketcher_CreateRectangle_Center',0)
# Gui.runCommand('Sketcher_CompCreateRectangles',1)
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

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,1,3,2,18.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,1,2,2,18.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 4, 1, -1, 1))


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
App.getDocument('Unnamed').getObject('Pad').Length = 5.000000
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
App.getDocument('Unnamed').purgeTouched()
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
#App.getDocument('Unnamed').getObject('Pad').Length = 5.000000
#App.getDocument('Unnamed').getObject('Pad').TaperAngle = 0.000000
#App.getDocument('Unnamed').getObject('Pad').UseCustomVector = 0
#App.getDocument('Unnamed').getObject('Pad').Direction = (0, 0, 1)
#App.getDocument('Unnamed').getObject('Pad').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'), ['N_Axis'])
#App.getDocument('Unnamed').getObject('Pad').AlongSketchNormal = 1
#App.getDocument('Unnamed').getObject('Pad').SideType = 0
#App.getDocument('Unnamed').getObject('Pad').Type = 0
#App.getDocument('Unnamed').getObject('Pad').Type2 = 0
#App.getDocument('Unnamed').getObject('Pad').UpToFace = None
#App.getDocument('Unnamed').getObject('Pad').UpToFace2 = None
#App.getDocument('Unnamed').getObject('Pad').Reversed = 0
#App.getDocument('Unnamed').getObject('Pad').Offset = 0
#App.getDocument('Unnamed').getObject('Pad').Offset2 = 0
#App.getDocument('Unnamed').purgeTouched()
#App.getDocument('Unnamed').recompute()
# Gui.getDocument('Unnamed').resetEdit()
App.getDocument('Unnamed').getObject('Sketch').Visibility = False
# Gui.Selection.addSelection('Unnamed','Body','Pad.Face6',4.42499,1.42658,5)
### Begin command PartDesign_NewSketch
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch001')
App.getDocument('Unnamed').getObject('Sketch001').AttachmentSupport = (App.getDocument('Unnamed').getObject('Pad'),['Face6',])
App.getDocument('Unnamed').getObject('Sketch001').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
# Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Sketch001.')
# ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
# tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
# ActiveSketch.ViewObject.TempoVis = tv
# if ActiveSketch.ViewObject.EditingWorkbench:
#   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
# if ActiveSketch.ViewObject.HideDependent:
#   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Body'), 'Sketch001.'))
# if ActiveSketch.ViewObject.ShowSupport:
#   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not (ref[0].isDerivedFrom("App::Plane") or ref[0].isDerivedFrom("App::LocalCoordinateSystem"))])
# if ActiveSketch.ViewObject.ShowLinks:
#   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
# tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
# tv.hide(ActiveSketch)
# del(tv)
# del(ActiveSketch)
# 
# ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
# if ActiveSketch.ViewObject.RestoreCamera:
#   ActiveSketch.ViewObject.TempoVis.saveCamera()
#   if ActiveSketch.ViewObject.ForceOrtho:
#     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
# 
### End command PartDesign_NewSketch
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompCreateConic',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(6.440913, 6.660893, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 0.825000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',0,1.650000)) 
constraintList = []
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(6.936379, -6.159151, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 0.825000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',1,1.650000)) 
constraintList = []
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(-6.379128, 6.598959, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 0.825000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',2,1.650000)) 
constraintList = []
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(-6.317194, -6.530746, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 0.825000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',3,1.650000)) 
constraintList = []
# Gui.runCommand('Sketcher_CompDimensionTools',0) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex1',6.44091,6.66089,0,False)
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('DistanceY',1,3,0,3,12.820044)) 
App.getDocument('Unnamed').getObject('Sketch001').setDatum(4,App.Units.Quantity('11.100000 mm')) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex2',6.93638,-6.15915,0,False)
# Gui.Selection.clearSelection()
#App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',3,3,-1,1,9.086120)) 


# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex4',-6.31719,-6.53075,0,False)
# App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('DistanceX',3,3,-1,1,6.317194)) 
# App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',3,3,-1,1,9.086120)) 
# App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',3,3,2,3,13.129851)) 
# # Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex3',-6.37913,6.59896,0,False)
# App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('DistanceY',3,3,2,3,13.129705)) 
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_ConstrainCoincidentUnified',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex3',-6.37913,6.59896,0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex1',6.44091,5.5328,0)
# App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Coincident', 2, 3, 0, 3))
# Gui.Selection.clearSelection()
# Gui.runCommand('Std_Undo',0)
# Gui.runCommand('Sketcher_CompHorVer',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex3',-6.37913,6.59896,0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex1',6.44091,5.5328,0)
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Horizontal',2,3,0,3))
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex2',6.93638,-5.5672,0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex4',-6.31719,-6.53075,0)
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Horizontal',1,3,3,3))
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompDimensionTools',0)
# Gui.runCommand('Sketcher_CompHorVer',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex3',-6.37913,5.5328,0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex4',-6.31719,-5.5672,0)
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Vertical',2,3,3,3))
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex2',6.93638,-5.5672,0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex1',6.44091,5.5328,0)
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Vertical',1,3,0,3))
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('DistanceX',3,3,1,3,14.100000)) 

App.getDocument('Unnamed').getObject('Sketch001').setDatum(9,App.Units.Quantity('14.100000 mm'))
# Gui.Selection.clearSelection()
 
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('DistanceX',-1,1,1,3,7.219222)) 
App.getDocument('Unnamed').getObject('Sketch001').setDatum(10,App.Units.Quantity('7.050000 mm'))
# Gui.Selection.clearSelection()

# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex3',-7.05,5.5328,0,False)

App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',2,3,-1,5.532796)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.H_Axis',-5.25503,0,0,False)
App.getDocument('Unnamed').getObject('Sketch001').setDatum(11,App.Units.Quantity('5.550000 mm'))
# Gui.Selection.clearSelection()
# Gui.getDocument('Unnamed').resetEdit()
App.ActiveDocument.recompute()
# ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')
# tv = ActiveSketch.ViewObject.TempoVis
# if tv:
#   tv.restore()
# ActiveSketch.ViewObject.TempoVis = None
# del(tv)
# del(ActiveSketch)
# 
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.')
App.getDocument('Unnamed').recompute()
### Begin command PartDesign_Pocket
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pocket','Pocket')
App.getDocument('Unnamed').getObject('Pocket').Profile = (App.getDocument('Unnamed').getObject('Sketch001'), ['',])
App.getDocument('Unnamed').getObject('Pocket').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pocket').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pocket').Direction = (0, 0, -1)
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
App.getDocument('Unnamed').purgeTouched()
App.getDocument('Unnamed').recompute()
# App.getDocument('Unnamed').getObject('Pocket').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Pocket').ViewObject.ShapeAppearance)
# App.getDocument('Unnamed').getObject('Pocket').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Pocket').ViewObject.LineColor)
# App.getDocument('Unnamed').getObject('Pocket').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Pocket').ViewObject.PointColor)
# App.getDocument('Unnamed').getObject('Pocket').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Pocket').ViewObject.Transparency)
# App.getDocument('Unnamed').getObject('Pocket').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Pocket').ViewObject.DisplayMode)
# Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Pocket.')
# Gui.Selection.clearSelection()
### End command PartDesign_Pocket
# Gui.Selection.clearSelection()
#App.getDocument('Unnamed').getObject('Pocket').TaperAngle = 0.000000
#App.getDocument('Unnamed').getObject('Pocket').UseCustomVector = 0
#App.getDocument('Unnamed').getObject('Pocket').Direction = (0, 0, -1)
#App.getDocument('Unnamed').getObject('Pocket').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch001'), ['N_Axis'])
#App.getDocument('Unnamed').getObject('Pocket').AlongSketchNormal = 1
#App.getDocument('Unnamed').getObject('Pocket').SideType = 0
#App.getDocument('Unnamed').getObject('Pocket').Type = 1
#App.getDocument('Unnamed').getObject('Pocket').Type2 = 0
#App.getDocument('Unnamed').getObject('Pocket').UpToFace = None
#App.getDocument('Unnamed').getObject('Pocket').UpToFace2 = None
#App.getDocument('Unnamed').getObject('Pocket').Reversed = 0
#App.getDocument('Unnamed').getObject('Pocket').Offset = 0
#App.getDocument('Unnamed').getObject('Pocket').Offset2 = 0
#App.getDocument('Unnamed').purgeTouched()
#App.getDocument('Unnamed').recompute()
#App.getDocument('Unnamed').getObject('Pad').Visibility = False
# Gui.getDocument('Unnamed').resetEdit()
App.getDocument('Unnamed').getObject('Sketch001').Visibility = False
# Macro End: C:\Users\pawar\AppData\Roaming\FreeCAD\v1-1\Macro\14.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
