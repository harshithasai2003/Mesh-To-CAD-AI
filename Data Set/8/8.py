# Macro Begin: C:\Users\pawar\AppData\Roaming\FreeCAD\v1-1\Macro\8.1.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
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
# Gui.Selection.addSelection('Unnamed','Body','Origin.XZ_Plane.',19.6338,-2.2894e-06,19.2049)
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch')
App.getDocument('Unnamed').getObject('Sketch').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XZ_Plane'])
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
# Gui.runCommand('Sketcher_ToggleConstruction',0)
# Gui.runCommand('Sketcher_ToggleConstruction',0)
# Gui.runCommand('Sketcher_CreateLine',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 0.000000, 0.000000),App.Vector(0.000000, 60.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,60.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',0)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 0, 1, -1, 1))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 0.000000, 0.000000),App.Vector(60.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,60.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Horizontal',1)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 1, 1, 0, 1))


# Gui.runCommand('Sketcher_ToggleConstruction',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

constrGeoList = []
constrGeoList.append(Part.LineSegment(App.Vector(60.000000, 0.000000, 0.000000),App.Vector(60.000000, 20.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(constrGeoList,True)
del constrGeoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',2,20.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',2)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 2, 1, 1, 2))


# Gui.runCommand('Sketcher_ToggleConstruction',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(60.000000, 20.000000, 0.000000),App.Vector(20.000000, 20.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',3,40.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Horizontal',3)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 3, 1, 2, 2))


### Begin command Std_ViewRight
# Gui.activeDocument().activeView().viewRight()
### End command Std_ViewRight
# Gui.runCommand('Std_ViewGroup',3)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.')
App.ActiveDocument.recompute()
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.')
# ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
# tv = ActiveSketch.ViewObject.TempoVis
# if tv:
#   tv.restore()
# ActiveSketch.ViewObject.TempoVis = None
# del(tv)
# del(ActiveSketch)
# 
# Gui.Selection.clearSelection()
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
App.getDocument('Unnamed').getObject('Sketch').setVisibility([0,1,2,3,4,5,6,7,8,9,10,11], True)
# ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')
# if ActiveSketch.ViewObject.RestoreCamera:
#   ActiveSketch.ViewObject.TempoVis.saveCamera()
#   if ActiveSketch.ViewObject.ForceOrtho:
#     ActiveSketch.ViewObject.Document.ActiveView.setCameraType('Orthographic')
# 
# Gui.runCommand('Sketcher_CreateLine',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(20.000000, 20.000000, 0.000000),App.Vector(20.000000, 60.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,40.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',4)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 4, 1, 3, 2))


# Gui.runCommand('Sketcher_ToggleConstruction',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

constrGeoList = []
constrGeoList.append(Part.LineSegment(App.Vector(20.000000, 60.000000, 0.000000),App.Vector(0.000000, 60.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(constrGeoList,True)
del constrGeoList

constraintList = []
constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 5, 1, 4, 2))
constraintList.append(Sketcher.Constraint('Coincident', 5, 2, 0, 2))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

# Gui.runCommand('Sketcher_ToggleConstruction',0)
# Gui.runCommand('Sketcher_CompCreateArc',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(10.000000, 60.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 10.000000), 0.000000, 3.141593))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(60.000000, 7.569876, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 12.430124), 4.712389, 7.853982))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
constraintList.append(Sketcher.Constraint('PointOnObject', 7, 3, 2))
constraintList.append(Sketcher.Constraint('Coincident', 7, 2, 2, 2))
constraintList.append(Sketcher.Constraint('Coincident', 7, 1, 1, 2))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge7',12.4869,-0.00800831,69.6858,False)
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch').delGeometries([6])
# Gui.runCommand('Sketcher_CompCreateArc',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(11.013359, 60.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 11.013359), 0.000000, 3.141593))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
constraintList.append(Sketcher.Constraint('PointOnObject', 7, 3, 5))
constraintList.append(Sketcher.Constraint('Coincident', 7, 2, 0, 2))
constraintList.append(Sketcher.Constraint('Coincident', 7, 1, 4, 2))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

# Gui.runCommand('Sketcher_CompCreateConic',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(10.000000, 60.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 5.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',8,10.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 8, 3, 7, 3))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(60.000000, 10.000000, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 5.000000))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Diameter',9,10.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 9, 3, 6, 3))


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
App.getDocument('Unnamed').purgeTouched()
App.getDocument('Unnamed').recompute()
# Gui.getDocument('Unnamed').resetEdit()
App.getDocument('Unnamed').getObject('Sketch').Visibility = False
# Macro End: C:\Users\pawar\AppData\Roaming\FreeCAD\v1-1\Macro\8.1.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
