# Macro Begin: C:\Users\pawar\AppData\Roaming\FreeCAD\v1-1\Macro\20.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
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
# Gui.Selection.addSelection('Unnamed','Body','Origin.XY_Plane.',14.8211,13.164,0)
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
# Gui.runCommand('Sketcher_CompCreateRectangles',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 0.000000, 0.000000),App.Vector(84.000000, 0.000000, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(84.000000, 0.000000, 0.000000),App.Vector(84.000000, 40.000000, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(84.000000, 40.000000, 0.000000),App.Vector(0.000000, 40.000000, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(0.000000, 40.000000, 0.000000),App.Vector(0.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 0, 2, 1, 1))
constraintList.append(Sketcher.Constraint('Coincident', 1, 2, 2, 1))
constraintList.append(Sketcher.Constraint('Coincident', 2, 2, 3, 1))
constraintList.append(Sketcher.Constraint('Coincident', 3, 2, 0, 1))
constraintList.append(Sketcher.Constraint('Horizontal', 0))
constraintList.append(Sketcher.Constraint('Horizontal', 2))
constraintList.append(Sketcher.Constraint('Vertical', 1))
constraintList.append(Sketcher.Constraint('Vertical', 3))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,1,3,2,84.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,1,2,2,40.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 0, 1, -1, 1))

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(84.000000, 20.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 20.000000), 4.712389, 7.853982))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []

# Gui.Selection.addSelection('Unnamed','Body','Pad.Sketch.Vertex10',83.4944,43.1404,0.014,False)
# Gui.Selection.addSelection('Unnamed','Body','Pad.Sketch.Vertex4',84,40,0.014,False)
### Begin command Sketcher_ConstrainCoincidentUnified
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident',4,2,1,2))
### End command Sketcher_ConstrainCoincidentUnified
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Pad.Sketch.Vertex11',87.6726,18.3967,0.014,False)
# Gui.Selection.addSelection('Unnamed','Body','Pad.Sketch.Vertex4',84,40,0.014,False)
### Begin command Sketcher_ConstrainVertical
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',4,3,1,2))
### End command Sketcher_ConstrainVertical
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Pad.Sketch.Vertex9',85.951,-3.44921,0.014,False)
# Gui.Selection.addSelection('Unnamed','Body','Pad.Sketch.Vertex2',84,0,0.014,False)
### Begin command Sketcher_ConstrainCoincidentUnified
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident',4,1,0,2))
### End command Sketcher_ConstrainCoincidentUnified
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompCurveEdition',0)
App.getDocument('Unnamed').getObject('Sketch').trim(1,App.Vector(84.000000,9.092041,0))
# Gui.Selection.addSelection('Unnamed','Body','Pad.Sketch.Edge1',57.7976,0,0.008,False)
# Gui.Selection.addSelection('Unnamed','Body','Pad.Sketch.Edge2',60.098,40,0.008,False)
### Begin command Sketcher_ConstrainEqual
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Equal',0,1))
### End command Sketcher_ConstrainEqual
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompCreateConic',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(84.000000, 20.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 8.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',4,16.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 4, 3, 3, 3))

#App.getDocument('Unnamed').getObject('Sketch').delConstraint(10)
## Gui.runCommand('Sketcher_CompDimensionTools',0)
#App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Angle',3,3.141593))
## Gui.Selection.addSelection('Unnamed','Body','Pad.Sketch.Edge4',97.5338,34.7254,0,False)
#App.getDocument('Unnamed').getObject('Sketch').setDatum(13,App.Units.Quantity('180.000000 deg'))

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
App.getDocument('Unnamed').getObject('Pad').Length = 16.000000
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
App.getDocument('Unnamed').recompute()
App.ActiveDocument.recompute()
# App.getDocument('Unnamed').getObject('Pad').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Pad').ViewObject.ShapeAppearance)
# App.getDocument('Unnamed').getObject('Pad').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Pad').ViewObject.LineColor)
# App.getDocument('Unnamed').getObject('Pad').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Pad').ViewObject.PointColor)
# App.getDocument('Unnamed').getObject('Pad').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Pad').ViewObject.Transparency)
# App.getDocument('Unnamed').getObject('Pad').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Body').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Pad').ViewObject.DisplayMode)
# Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Pad.')
# Gui.Selection.clearSelection()
### End command PartDesign_Pad
## Gui.Selection.clearSelection()
#App.getDocument('Unnamed').getObject('Pad').Length = 16.000000
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
# Gui.Selection.addSelection('Unnamed','Body','Pad.')
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Pad.Face1',42.9018,0,5.92931)
### Begin command Part_DatumPoint

# import Show
# from Show.Containers import isAContainer
# _tv_DatumPoint = Show.TempoVis(App.ActiveDocument, tag= 'PartGui::TaskAttacher')
# tvObj = App.getDocument('Unnamed').getObject('DatumPoint')
# dep_features = _tv_DatumPoint.get_all_dependent(App.getDocument('Unnamed').getObject('DatumPoint'), '')
# dep_features = [o for o in dep_features if not isAContainer(o)]
# if tvObj.isDerivedFrom('PartDesign::CoordinateSystem'):
# 	visible_features = [feat for feat in tvObj.InList if feat.isDerivedFrom('PartDesign::FeaturePrimitive')]
# 	dep_features = [feat for feat in dep_features if feat not in visible_features]
# 	del(visible_features)
# _tv_DatumPoint.hide(dep_features)
# del(dep_features)
# if not tvObj.isDerivedFrom('PartDesign::CoordinateSystem'):
# 		if len(tvObj.AttachmentSupport) > 0:
# 			_tv_DatumPoint.show([lnk[0] for lnk in tvObj.AttachmentSupport])
# del(tvObj)
### End command Part_DatumPoint
# Gui.runCommand('Part_Datums',3)
App.ActiveDocument.recompute()
# _tv_DatumPoint.restore()
# del(_tv_DatumPoint)
### Begin command Part_DatumPlane
obj = App.activeDocument().addObject('Part::DatumPlane','DatumPlane')
App.ActiveDocument.getObject('Body').addObject(obj)

#obj.ViewObject.doubleClicked()
# import Show
# from Show.Containers import isAContainer
# _tv_DatumPlane = Show.TempoVis(App.ActiveDocument, tag= 'PartGui::TaskAttacher')
# tvObj = App.getDocument('Unnamed').getObject('DatumPlane')
# dep_features = _tv_DatumPlane.get_all_dependent(App.getDocument('Unnamed').getObject('DatumPlane'), '')
# dep_features = [o for o in dep_features if not isAContainer(o)]
# if tvObj.isDerivedFrom('PartDesign::CoordinateSystem'):
# 	visible_features = [feat for feat in tvObj.InList if feat.isDerivedFrom('PartDesign::FeaturePrimitive')]
# 	dep_features = [feat for feat in dep_features if feat not in visible_features]
# 	del(visible_features)
# _tv_DatumPlane.hide(dep_features)
# del(dep_features)
# if not tvObj.isDerivedFrom('PartDesign::CoordinateSystem'):
# 		if len(tvObj.AttachmentSupport) > 0:
# 			_tv_DatumPlane.show([lnk[0] for lnk in tvObj.AttachmentSupport])
# del(tvObj)
### End command Part_DatumPlane
# Gui.runCommand('Part_Datums',1)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Origin.Y_Axis.',0.664206,24.6763,1.55024)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Origin.XZ_Plane.',10.5044,-1.08318e-06,9.08641)
App.getDocument('Unnamed').getObject('DatumPlane').AttachmentOffset = App.Placement(App.Vector(0.0000000000, 0.0000000000, -40.0000000000),  App.Rotation(0.0000000000, 0.0000000000, 0.0000000000))
App.getDocument('Unnamed').getObject('DatumPlane').MapReversed = False
App.getDocument('Unnamed').getObject('DatumPlane').AttachmentSupport = [(App.getDocument('Unnamed').getObject('Origin'),'XZ_Plane.')]
App.getDocument('Unnamed').getObject('DatumPlane').MapPathParameter = 0.000000
App.getDocument('Unnamed').getObject('DatumPlane').MapMode = 'FlatFace'
App.getDocument('Unnamed').getObject('DatumPlane').recompute()
# _tv_DatumPlane.restore()
# del(_tv_DatumPlane)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','DatumPlane.')
### Begin command PartDesign_CompSketches
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch001')
App.getDocument('Unnamed').getObject('Sketch001').AttachmentSupport = (App.getDocument('Unnamed').getObject('DatumPlane'),[])
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
### End command PartDesign_CompSketches
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompCreateRectangles',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 30.748625, 0.000000),App.Vector(50.000000, 30.748625, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(50.000000, 30.748625, 0.000000),App.Vector(50.000000, 52.748625, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(50.000000, 52.748625, 0.000000),App.Vector(0.000000, 52.748625, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(0.000000, 52.748625, 0.000000),App.Vector(0.000000, 30.748625, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 0, 2, 1, 1))
constraintList.append(Sketcher.Constraint('Coincident', 1, 2, 2, 1))
constraintList.append(Sketcher.Constraint('Coincident', 2, 2, 3, 1))
constraintList.append(Sketcher.Constraint('Coincident', 3, 2, 0, 1))
constraintList.append(Sketcher.Constraint('Horizontal', 0))
constraintList.append(Sketcher.Constraint('Horizontal', 2))
constraintList.append(Sketcher.Constraint('Vertical', 1))
constraintList.append(Sketcher.Constraint('Vertical', 3))
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(constraintList)
del constraintList

App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',1,1,3,2,50.000000)) 
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',0,1,2,2,22.000000)) 
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('PointOnObject', 0, 1, -2))


# Gui.Selection.addSelection('Unnamed','Body','Pad001.Sketch001.Edge1',40.5613,39.992,30.7486,False)
# Gui.Selection.addSelection('Unnamed','Body','Pad001.Sketch001.H_Axis',75.5451,39.998,-2.38427e-10,False)
### Begin command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',-1,1,0,30.748625)) 
### End command Sketcher_CompDimensionTools
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch001').setDatum(11,App.Units.Quantity('16.000000 mm'))
# Gui.runCommand('Sketcher_CompCreateArc',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(25.000000, 38.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 25.000000), 0.000000, 3.141593))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []

# Gui.Selection.addSelection('Unnamed','Body','Pad001.Sketch001.Vertex10',-1.40076,39.986,37.8661,False)
# Gui.Selection.addSelection('Unnamed','Body','Pad001.Sketch001.Vertex6',0,39.986,38,False)
### Begin command Sketcher_ConstrainCoincidentUnified
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Coincident',4,2,2,2))
### End command Sketcher_ConstrainCoincidentUnified
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Pad001.Sketch001.Vertex6',0,39.986,38,False)
# Gui.Selection.addSelection('Unnamed','Body','Pad001.Sketch001.Vertex11',25.6358,39.986,40.5969,False)
### Begin command Sketcher_ConstrainHorizontal
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Horizontal',2,2,4,3))
### End command Sketcher_ConstrainHorizontal
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Pad001.Sketch001.Vertex9',51.4025,39.986,40.4888,False)
# Gui.Selection.addSelection('Unnamed','Body','Pad001.Sketch001.Vertex4',50,39.986,38,False)
### Begin command Sketcher_ConstrainCoincidentUnified
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Coincident',4,1,1,2))
### End command Sketcher_ConstrainCoincidentUnified
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompCurveEdition',0)
App.getDocument('Unnamed').getObject('Sketch001').trim(2,App.Vector(32.395424,38.000000,0))
# Gui.runCommand('Std_Undo',0)
# Gui.Selection.addSelection('Unnamed','Body','Pad001.Sketch001.Vertex4',50,39.986,38,False)
# Gui.Selection.addSelection('Unnamed','Body','Pad001.Sketch001.Vertex5',0,39.986,38,False)
# Gui.Selection.addSelection('Unnamed','Body','Pad001.Sketch001.Edge3',0,39.992,29.8235,False)
# Gui.Selection.addSelection('Unnamed','Body','Pad001.Sketch001.Edge2',50,39.992,29.7087,False)
# Gui.runCommand('Sketcher_ConstrainEqual',0)
# Gui.runCommand('Sketcher_CompDimensionTools',0)
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Angle',3,3.141593))
# Gui.Selection.addSelection('Unnamed','Body','Pad001.Sketch001.Edge4',25,63,0,False)
App.getDocument('Unnamed').getObject('Sketch001').setDatum(12,App.Units.Quantity('180.000000 deg'))
# Gui.Selection.clearSelection()
#App.getDocument('Unnamed').getObject('Sketch001').setDatum(13,App.Units.Quantity('180.000000 deg'))

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
### Begin command PartDesign_Pad
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad001')
App.getDocument('Unnamed').getObject('Pad001').Profile = (App.getDocument('Unnamed').getObject('Sketch001'), ['',])
App.getDocument('Unnamed').getObject('Pad001').Length = 12.000000
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
App.getDocument('Unnamed').purgeTouched()
App.getDocument('Unnamed').recompute()
App.ActiveDocument.recompute()
# App.getDocument('Unnamed').getObject('Pad001').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Pad001').ViewObject.ShapeAppearance)
# App.getDocument('Unnamed').getObject('Pad001').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Pad001').ViewObject.LineColor)
# App.getDocument('Unnamed').getObject('Pad001').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Pad001').ViewObject.PointColor)
# App.getDocument('Unnamed').getObject('Pad001').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Pad001').ViewObject.Transparency)
# App.getDocument('Unnamed').getObject('Pad001').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Pad001').ViewObject.DisplayMode)
# Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Pad001.')
# Gui.Selection.clearSelection()
### End command PartDesign_Pad
# Gui.Selection.clearSelection()
#App.getDocument('Unnamed').getObject('Pad001').Length = 12.000000
#App.getDocument('Unnamed').getObject('Pad001').TaperAngle = 0.000000
#App.getDocument('Unnamed').getObject('Pad001').UseCustomVector = 0
#App.getDocument('Unnamed').getObject('Pad001').Direction = (0, -1, 0)
#App.getDocument('Unnamed').getObject('Pad001').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch001'), ['N_Axis'])
#App.getDocument('Unnamed').getObject('Pad001').AlongSketchNormal = 1
#App.getDocument('Unnamed').getObject('Pad001').SideType = 0
#App.getDocument('Unnamed').getObject('Pad001').Type = 0
#App.getDocument('Unnamed').getObject('Pad001').Type2 = 0
#App.getDocument('Unnamed').getObject('Pad001').UpToFace = None
#App.getDocument('Unnamed').getObject('Pad001').UpToFace2 = None
#App.getDocument('Unnamed').getObject('Pad001').Reversed = 0
#App.getDocument('Unnamed').getObject('Pad001').Offset = 0
#App.getDocument('Unnamed').getObject('Pad001').Offset2 = 0
#App.getDocument('Unnamed').purgeTouched()
#App.getDocument('Unnamed').recompute()
#App.getDocument('Unnamed').getObject('Pad').Visibility = False
# Gui.getDocument('Unnamed').resetEdit()
App.getDocument('Unnamed').getObject('Sketch001').Visibility = False
# Gui.runCommand('PartDesign_CompSketches',0)
# Gui.Selection.addSelection('Unnamed','Body','Origin.XZ_Plane.',18.8323,-2.49355e-06,20.9174)
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch002')
App.getDocument('Unnamed').getObject('Sketch002').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XZ_Plane'])
App.getDocument('Unnamed').getObject('Sketch002').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
# Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Sketch002.')
# ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')
# tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
# ActiveSketch.ViewObject.TempoVis = tv
# if ActiveSketch.ViewObject.EditingWorkbench:
#   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
# if ActiveSketch.ViewObject.HideDependent:
#   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Body'), 'Sketch002.'))
# if ActiveSketch.ViewObject.ShowSupport:
#   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not (ref[0].isDerivedFrom("App::Plane") or ref[0].isDerivedFrom("App::LocalCoordinateSystem"))])
# if ActiveSketch.ViewObject.ShowLinks:
#   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
# tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
# tv.hide(ActiveSketch)
# del(tv)
# del(ActiveSketch)
# 
# ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')
# if ActiveSketch.ViewObject.RestoreCamera:
#   ActiveSketch.ViewObject.TempoVis.saveCamera()
#   if ActiveSketch.ViewObject.ForceOrtho:
#     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
# 
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompCreateRectangles',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 15.795054, 0.000000),App.Vector(50.000000, 15.795054, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(50.000000, 15.795054, 0.000000),App.Vector(50.000000, 37.795054, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(50.000000, 37.795054, 0.000000),App.Vector(0.000000, 37.795054, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(0.000000, 37.795054, 0.000000),App.Vector(0.000000, 15.795054, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch002').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 0, 2, 1, 1))
constraintList.append(Sketcher.Constraint('Coincident', 1, 2, 2, 1))
constraintList.append(Sketcher.Constraint('Coincident', 2, 2, 3, 1))
constraintList.append(Sketcher.Constraint('Coincident', 3, 2, 0, 1))
constraintList.append(Sketcher.Constraint('Horizontal', 0))
constraintList.append(Sketcher.Constraint('Horizontal', 2))
constraintList.append(Sketcher.Constraint('Vertical', 1))
constraintList.append(Sketcher.Constraint('Vertical', 3))
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(constraintList)
del constraintList

App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',1,1,3,2,50.000000)) 
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',0,1,2,2,22.000000)) 
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('PointOnObject', 0, 1, -2))


# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Edge3',16.3996,-0.00800451,37.7951,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.H_Axis',-14.9137,-0.002,-2.38419e-10,False)
### Begin command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',-1,1,2,37.795054)) 
### End command Sketcher_CompDimensionTools
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch002').setDatum(11,App.Units.Quantity('38.000000 mm'))
# Gui.runCommand('Sketcher_CompCreateArc',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(25.000000, 38.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 25.000000), 0.000000, 3.141593))
App.getDocument('Unnamed').getObject('Sketch002').addGeometry(geoList,False)
del geoList

constraintList = []
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Edge5',47.5064,-0.00800583,48.8688,False)
# Gui.runCommand('Sketcher_SelectConstraints',0)
# Gui.Selection.clearSelection()

# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Vertex9',51.675,-0.0140046,38.4243,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Vertex4',50,-0.0140045,38,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Vertex10',-1.67837,-0.0140045,37.9996,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Vertex6',0,-0.0140045,38,False)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Vertex4',50,-0.0140045,38,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Vertex9',51.675,-0.0140046,38.4243,False)
### Begin command Sketcher_ConstrainCoincidentUnified
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Coincident',1,2,4,1))
### End command Sketcher_ConstrainCoincidentUnified
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Vertex6',0,-0.0140045,38,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Vertex10',-1.67837,-0.0140045,37.9996,False)
### Begin command Sketcher_ConstrainCoincidentUnified
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Coincident',2,2,4,2))
### End command Sketcher_ConstrainCoincidentUnified
# Gui.Selection.clearSelection()

# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Edge3',25.6718,-0.00800453,38,False)
# Gui.runCommand('Sketcher_ConstrainCoincidentUnified',0)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Vertex11',25,-0.0140048,39.9737,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Edge3',25.6044,-0.00800453,38,False)
### Begin command Sketcher_ConstrainCoincidentUnified
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('PointOnObject',4,3,2))
### End command Sketcher_ConstrainCoincidentUnified
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompCurveEdition',0)
App.getDocument('Unnamed').getObject('Sketch002').trim(2,App.Vector(38.538658,38.000000,0))
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Vertex9',25,-0.0140045,38,False)
# Gui.getDocument('Unnamed').resetEdit()
App.ActiveDocument.recompute()
# ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')
# tv = ActiveSketch.ViewObject.TempoVis
# if tv:
#   tv.restore()
# ActiveSketch.ViewObject.TempoVis = None
# del(tv)
# del(ActiveSketch)
# 
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.')
App.getDocument('Unnamed').recompute()
# Gui.Selection.clearSelection()
# ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')
# tv = Show.TempoVis(App.ActiveDocument, tag= ActiveSketch.ViewObject.TypeId)
# ActiveSketch.ViewObject.TempoVis = tv
# if ActiveSketch.ViewObject.EditingWorkbench:
#   tv.activateWorkbench(ActiveSketch.ViewObject.EditingWorkbench)
# if ActiveSketch.ViewObject.HideDependent:
#   tv.hide(tv.get_all_dependent(App.getDocument('Unnamed').getObject('Body'), 'Sketch002.'))
# if ActiveSketch.ViewObject.ShowSupport:
#   tv.show([ref[0] for ref in ActiveSketch.AttachmentSupport if not (ref[0].isDerivedFrom("App::Plane") or ref[0].isDerivedFrom("App::LocalCoordinateSystem"))])
# if ActiveSketch.ViewObject.ShowLinks:
#   tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
# tv.sketchClipPlane(ActiveSketch, ActiveSketch.ViewObject.SectionView)
# tv.hide(ActiveSketch)
# del(tv)
# del(ActiveSketch)
# 
App.getDocument('Unnamed').getObject('Sketch002').setVisibility([0,1,2,3,4,5,6,7,8,9], True)
# ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')
# if ActiveSketch.ViewObject.RestoreCamera:
#   ActiveSketch.ViewObject.TempoVis.saveCamera()
#   if ActiveSketch.ViewObject.ForceOrtho:
#     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
# 

# Gui.runCommand('Std_Undo',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Edge3',0,-0.00800326,27.3452,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Edge2',50,-0.00800274,22.9974,False)
### Begin command Sketcher_ConstrainEqual
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Equal',2,1))
### End command Sketcher_ConstrainEqual
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Edge1',43.506,-0.00800191,16,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.H_Axis',84.8854,-0.002,-2.38419e-10,False)
### Begin command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',-1,1,0,16.000000)) 
### End command Sketcher_CompDimensionTools
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch002').setDatum(11,App.Units.Quantity('16.000000 mm'))
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Angle',3,3.141593))
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Edge4',25,63,0,False)
App.getDocument('Unnamed').getObject('Sketch002').setDatum(12,App.Units.Quantity('180.000000 deg'))
# Gui.Selection.clearSelection()
# Gui.getDocument('Unnamed').resetEdit()
App.ActiveDocument.recompute()
# ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')
# tv = ActiveSketch.ViewObject.TempoVis
# if tv:
#   tv.restore()
# ActiveSketch.ViewObject.TempoVis = None
# del(tv)
# del(ActiveSketch)
# 
### Begin command PartDesign_Pad
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad002')
App.getDocument('Unnamed').getObject('Pad002').Profile = (App.getDocument('Unnamed').getObject('Sketch002'), ['',])
App.getDocument('Unnamed').getObject('Pad002').Length = 12.000000
App.getDocument('Unnamed').getObject('Pad002').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pad002').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pad002').Direction = (0, -1, 0)
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

# --- THE FIX: Tell the Body that Pad002 is the final active shape ---
App.getDocument('Unnamed').getObject('Body').Tip = App.getDocument('Unnamed').getObject('Pad002')

# Now recompute everything at the very end
App.getDocument('Unnamed').purgeTouched()
App.ActiveDocument.recompute()
# App.getDocument('Unnamed').getObject('Pad002').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Pad001').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Pad002').ViewObject.ShapeAppearance)
# App.getDocument('Unnamed').getObject('Pad002').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Pad001').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Pad002').ViewObject.LineColor)
# App.getDocument('Unnamed').getObject('Pad002').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Pad001').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Pad002').ViewObject.PointColor)
# App.getDocument('Unnamed').getObject('Pad002').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Pad001').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Pad002').ViewObject.Transparency)
# App.getDocument('Unnamed').getObject('Pad002').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Pad001').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Pad002').ViewObject.DisplayMode)
# Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Pad002.')
# Gui.Selection.clearSelection()
### End command PartDesign_Pad
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Pad002.')
# Gui.ActiveDocument.setEdit(App.getDocument('Unnamed').getObject('Pad002'), 0)
# Gui.Selection.clearSelection()
#App.getDocument('Unnamed').getObject('Pad002').Length = 12.000000
#App.getDocument('Unnamed').getObject('Pad002').TaperAngle = 0.000000
#App.getDocument('Unnamed').getObject('Pad002').UseCustomVector = 0
#App.getDocument('Unnamed').getObject('Pad002').Direction = (0, -1, 0)
#App.getDocument('Unnamed').getObject('Pad002').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch002'), ['N_Axis'])
#App.getDocument('Unnamed').getObject('Pad002').AlongSketchNormal = 1
#App.getDocument('Unnamed').getObject('Pad002').SideType = 0
#App.getDocument('Unnamed').getObject('Pad002').Type = 0
#App.getDocument('Unnamed').getObject('Pad002').Type2 = 0
#App.getDocument('Unnamed').getObject('Pad002').UpToFace = None
#App.getDocument('Unnamed').getObject('Pad002').UpToFace2 = None
#App.getDocument('Unnamed').getObject('Pad002').Reversed = 1
#App.getDocument('Unnamed').getObject('Pad002').Offset = 0
#App.getDocument('Unnamed').getObject('Pad002').Offset2 = 0
#App.getDocument('Unnamed').purgeTouched()
#App.getDocument('Unnamed').recompute()
App.getDocument('Unnamed').getObject('Pad001').Visibility = False
# Gui.getDocument('Unnamed').resetEdit()
App.getDocument('Unnamed').getObject('Sketch002').Visibility = False
App.getDocument('Unnamed').getObject('DatumPlane').Visibility = False
# Macro End: C:\Users\pawar\AppData\Roaming\FreeCAD\v1-1\Macro\20.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
