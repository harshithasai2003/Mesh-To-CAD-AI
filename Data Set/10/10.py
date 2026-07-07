# Macro Begin: C:\Users\pawar\AppData\Roaming\FreeCAD\v1-1\Macro\10.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
import FreeCAD
import PartDesign
import PartDesignGui
import Sketcher
import ProfileLib.RegularPolygon

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
# Gui.Selection.addSelection('Unnamed','Body','Origin.XY_Plane.',15.1539,13.8724,0)
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
# Gui.runCommand('Sketcher_CompCreateRegularPolygon',3)
ProfileLib.RegularPolygon.makeRegularPolygon(App.getDocument('Unnamed').getObject('Sketch'),6,App.Vector(0.000000,0.000000,0),App.Vector(25.000000,0.000000,0),False)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Radius',6,25.000000)) 
constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 6, 3, -1, 1))
constraintList.append(Sketcher.Constraint('PointOnObject', 5, 2, -1))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

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
App.getDocument('Unnamed').getObject('Pad').Length = 20.000000
App.getDocument('Unnamed').getObject('Pad').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pad').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pad').Direction = (0, 0, 1)
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
App.getDocument('Unnamed').purgeTouched()
App.getDocument('Unnamed').recompute()
# Gui.getDocument('Unnamed').resetEdit()
App.getDocument('Unnamed').getObject('Sketch').Visibility = False
# Gui.Selection.addSelection('Unnamed','Body','Pad.Face8',-1.07293,-0.836249,10)
### Begin command PartDesign_NewSketch
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch001')
App.getDocument('Unnamed').getObject('Sketch001').AttachmentSupport = (App.getDocument('Unnamed').getObject('Pad'),['Face8',])
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
geoList.append(Part.Circle(App.Vector(0.000000, 0.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 15.000000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',0,30.000000)) 
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Coincident', 0, 3, -1, 1))


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
App.getDocument('Unnamed').getObject('Pocket').Length = 5
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pocket').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch001'),['N_Axis'])
App.getDocument('Unnamed').getObject('Sketch001').Visibility = False
App.ActiveDocument.recompute()
# App.getDocument('Unnamed').getObject('Pocket').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Pocket').ViewObject.ShapeAppearance)
# App.getDocument('Unnamed').getObject('Pocket').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Pocket').ViewObject.LineColor)
# App.getDocument('Unnamed').getObject('Pocket').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Pocket').ViewObject.PointColor)
# App.getDocument('Unnamed').getObject('Pocket').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Pocket').ViewObject.Transparency)
# App.getDocument('Unnamed').getObject('Pocket').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Pocket').ViewObject.DisplayMode)
# Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Pocket.')
# Gui.Selection.clearSelection()
### End command PartDesign_Pocket
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Pocket').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pocket').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pocket').Direction = (0, 0, -1)
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
App.getDocument('Unnamed').getObject('Pad').Visibility = False
# Gui.getDocument('Unnamed').resetEdit()
App.getDocument('Unnamed').getObject('Sketch001').Visibility = False
# Gui.Selection.addSelection('Unnamed','Body','Pocket.Face5',18.1332,3.62225,10)
### Begin command PartDesign_Chamfer
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Chamfer','Chamfer')
App.getDocument('Unnamed').getObject('Chamfer').Base = (App.getDocument('Unnamed').getObject('Pocket'),['Face5',])
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Pocket').Visibility = False
App.ActiveDocument.recompute()
# App.getDocument('Unnamed').getObject('Chamfer').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Pocket').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Chamfer').ViewObject.ShapeAppearance)
# App.getDocument('Unnamed').getObject('Chamfer').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Pocket').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Chamfer').ViewObject.LineColor)
# App.getDocument('Unnamed').getObject('Chamfer').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Pocket').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Chamfer').ViewObject.PointColor)
# App.getDocument('Unnamed').getObject('Chamfer').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Pocket').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Chamfer').ViewObject.Transparency)
# App.getDocument('Unnamed').getObject('Chamfer').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Pocket').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Chamfer').ViewObject.DisplayMode)
# Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Chamfer.')
# Gui.Selection.clearSelection()
# Gui.Selection.clearSelection()
### End command PartDesign_Chamfer
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Chamfer').Size = 1.000000
App.getDocument('Unnamed').getObject('Chamfer').Base = (App.getDocument('Unnamed').getObject('Pocket'),["Face5",])
App.getDocument('Unnamed').getObject('Chamfer').Size = 1.000000
App.getDocument('Unnamed').purgeTouched()
App.getDocument('Unnamed').recompute()
App.getDocument('Unnamed').getObject('Pocket').Visibility = False
# Gui.getDocument('Unnamed').resetEdit()
# Gui.Selection.addSelection('Unnamed','Body','Chamfer.Face4',21.5694,3.87347,-10)
### Begin command PartDesign_Chamfer
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Chamfer','Chamfer001')
App.getDocument('Unnamed').getObject('Chamfer001').Base = (App.getDocument('Unnamed').getObject('Chamfer'),['Face4',])
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Chamfer').Visibility = False
App.ActiveDocument.recompute()
# App.getDocument('Unnamed').getObject('Chamfer001').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Chamfer').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Chamfer001').ViewObject.ShapeAppearance)
# App.getDocument('Unnamed').getObject('Chamfer001').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Chamfer').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Chamfer001').ViewObject.LineColor)
# App.getDocument('Unnamed').getObject('Chamfer001').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Chamfer').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Chamfer001').ViewObject.PointColor)
# App.getDocument('Unnamed').getObject('Chamfer001').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Chamfer').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Chamfer001').ViewObject.Transparency)
# App.getDocument('Unnamed').getObject('Chamfer001').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Chamfer').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Chamfer001').ViewObject.DisplayMode)
# Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Chamfer001.')
# Gui.Selection.clearSelection()
# Gui.Selection.clearSelection()
### End command PartDesign_Chamfer
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Chamfer001').Size = 1.000000
App.getDocument('Unnamed').getObject('Chamfer001').Base = (App.getDocument('Unnamed').getObject('Chamfer'),["Face4",])
App.getDocument('Unnamed').getObject('Chamfer001').Size = 1.000000
App.getDocument('Unnamed').purgeTouched()
App.getDocument('Unnamed').recompute()
App.getDocument('Unnamed').getObject('Chamfer').Visibility = False
# Gui.getDocument('Unnamed').resetEdit()
# Macro End: C:\Users\pawar\AppData\Roaming\FreeCAD\v1-1\Macro\10.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
