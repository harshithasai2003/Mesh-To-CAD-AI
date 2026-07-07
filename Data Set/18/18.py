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
# Gui.Selection.addSelection('Unnamed','Body','Origin.XY_Plane.',17.3106,18.4094,5.71176e-15)
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
# Gui.runCommand('Sketcher_CompCreateRectangles',1)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(-50.000000, -50.000000, 0.000000),App.Vector(50.000000, -50.000000, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(50.000000, -50.000000, 0.000000),App.Vector(50.000000, 50.000000, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(50.000000, 50.000000, 0.000000),App.Vector(-50.000000, 50.000000, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(-50.000000, 50.000000, 0.000000),App.Vector(-50.000000, -50.000000, 0.000000)))
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

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,1,3,2,100.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,1,2,2,100.000000)) 
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
# Gui.Selection.addSelection('Unnamed','Body','Pad.Face6',20.1443,0.318018,10)
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
# Gui.runCommand('Sketcher_CompExternal',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge3',34.7753,50,0)
App.getDocument('Unnamed').getObject('Sketch001').addExternal("Sketch","Edge3", True, False)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge2',50,26.8897,0)
App.getDocument('Unnamed').getObject('Sketch001').addExternal("Sketch","Edge2", True, False)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge1',16.9059,-50,0)
App.getDocument('Unnamed').getObject('Sketch001').addExternal("Sketch","Edge1", True, False)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',-50,-20.4348,0)
App.getDocument('Unnamed').getObject('Sketch001').addExternal("Sketch","Edge4", True, False)
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompExternal',0)
# Gui.Selection.addSelection(App.getDocument('Unnamed').getObject('Body'),['Sketch001.Vertex1','Sketch001.Vertex2','Sketch001.ExternalEdge4','Sketch001.Vertex3','Sketch001.Vertex4','Sketch001.ExternalEdge3','Sketch001.Vertex5','Sketch001.Vertex6','Sketch001.ExternalEdge2','Sketch001.Vertex7','Sketch001.Vertex8','Sketch001.ExternalEdge1','Sketch001.RootPoint'])
### Begin command Sketcher_ToggleConstruction
App.getDocument('Unnamed').getObject('Sketch001').toggleConstruction(-6) 
App.getDocument('Unnamed').getObject('Sketch001').toggleConstruction(-5) 
App.getDocument('Unnamed').getObject('Sketch001').toggleConstruction(-4) 
App.getDocument('Unnamed').getObject('Sketch001').toggleConstruction(-3) 
### End command Sketcher_ToggleConstruction
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CreateLine',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 50.000000, 0.000000),App.Vector(50.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
constraintList.append(Sketcher.Constraint('Symmetric', -3, 1, -3, 2, 0, 1))
constraintList.append(Sketcher.Constraint('Symmetric', -4, 1, -4, 2, 0, 2))
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(constraintList)
del constraintList

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(50.000000, 0.000000, 0.000000),App.Vector(0.000000, -50.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 1, 1, 0, 2))
constraintList.append(Sketcher.Constraint('Symmetric', -5, 1, -5, 2, 1, 2))
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(constraintList)
del constraintList

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, -50.000000, 0.000000),App.Vector(-50.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
constraintList.append(Sketcher.Constraint('Symmetric', -5, 1, -5, 2, 2, 1))
constraintList.append(Sketcher.Constraint('Symmetric', -6, 1, -6, 2, 2, 2))
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(constraintList)
del constraintList

ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(-50.000000, 0.000000, 0.000000),App.Vector(0.000000, 50.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
constraintList.append(Sketcher.Constraint('Symmetric', -6, 1, -6, 2, 3, 1))
constraintList.append(Sketcher.Constraint('Coincident', 3, 2, 0, 1))
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(constraintList)
del constraintList

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
App.getDocument('Unnamed').getObject('Pad001').Length = 10
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pad001').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch001'),['N_Axis'])
App.getDocument('Unnamed').getObject('Sketch001').Visibility = False
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
App.getDocument('Unnamed').getObject('Pad001').Length = 10.000000
App.getDocument('Unnamed').getObject('Pad001').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pad001').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pad001').Direction = (0, 0, 1)
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
App.getDocument('Unnamed').getObject('Pad').Visibility = False
# Gui.getDocument('Unnamed').resetEdit()
App.getDocument('Unnamed').getObject('Sketch001').Visibility = False
# Gui.Selection.addSelection('Unnamed','Body','Pad001.Face14',7.98487,7.23089,20)
### Begin command PartDesign_NewSketch
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch002')
App.getDocument('Unnamed').getObject('Sketch002').AttachmentSupport = (App.getDocument('Unnamed').getObject('Pad001'),['Face14',])
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
### End command PartDesign_NewSketch
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompExternal',0)
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Edge1',25.55,24.45,10)
App.getDocument('Unnamed').getObject('Sketch002').addExternal("Sketch001","Edge1", True, False)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Edge2',33.3946,-16.6054,10)
App.getDocument('Unnamed').getObject('Sketch002').addExternal("Sketch001","Edge2", True, False)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Edge4',-24.3619,25.6381,10)
App.getDocument('Unnamed').getObject('Sketch002').addExternal("Sketch001","Edge4", True, False)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Edge3',-18.068,-31.932,10)
App.getDocument('Unnamed').getObject('Sketch002').addExternal("Sketch001","Edge3", True, False)
# Gui.Selection.clearSelection()
# Gui.Selection.addSelection(App.getDocument('Unnamed').getObject('Body'),['Sketch002.Vertex1','Sketch002.Vertex2','Sketch002.ExternalEdge4','Sketch002.Vertex3','Sketch002.Vertex5','Sketch002.Vertex6','Sketch002.ExternalEdge2','Sketch002.Vertex8','Sketch002.RootPoint'])
# Gui.Selection.addSelection(App.getDocument('Unnamed').getObject('Body'),['Sketch002.Vertex4','Sketch002.ExternalEdge3','Sketch002.Vertex7','Sketch002.ExternalEdge1'])
### Begin command Sketcher_ToggleConstruction
App.getDocument('Unnamed').getObject('Sketch002').toggleConstruction(-6) 
App.getDocument('Unnamed').getObject('Sketch002').toggleConstruction(-4) 
App.getDocument('Unnamed').getObject('Sketch002').toggleConstruction(-5) 
App.getDocument('Unnamed').getObject('Sketch002').toggleConstruction(-3) 
### End command Sketcher_ToggleConstruction
# Gui.Selection.clearSelection()
# Gui.runCommand('Sketcher_CompCreateRectangles',1)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(-25.000000, -25.000000, 0.000000),App.Vector(25.000000, -25.000000, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(25.000000, -25.000000, 0.000000),App.Vector(25.000000, 25.000000, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(25.000000, 25.000000, 0.000000),App.Vector(-25.000000, 25.000000, 0.000000)))
geoList.append(Part.LineSegment(App.Vector(-25.000000, 25.000000, 0.000000),App.Vector(-25.000000, -25.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch002').addGeometry(geoList,False)
del geoList

constrGeoList = []
constrGeoList.append(Part.Point(App.Vector(0.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch002').addGeometry(constrGeoList,True)
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
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(constraintList)
del constraintList

constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 4, 1, -1, 1))
constraintList.append(Sketcher.Constraint('Symmetric', -3, 1, -3, 2, 1, 2))
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(constraintList)
del constraintList

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
### Begin command PartDesign_Pad
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad002')
App.getDocument('Unnamed').getObject('Pad002').Profile = (App.getDocument('Unnamed').getObject('Sketch002'), ['',])
App.getDocument('Unnamed').getObject('Pad002').Length = 10
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pad002').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch002'),['N_Axis'])
App.getDocument('Unnamed').getObject('Sketch002').Visibility = False
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
App.getDocument('Unnamed').getObject('Pad002').Length = 10.000000
App.getDocument('Unnamed').getObject('Pad002').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pad002').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pad002').Direction = (0, 0, 1)
App.getDocument('Unnamed').getObject('Pad002').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch002'), ['N_Axis'])
App.getDocument('Unnamed').getObject('Pad002').AlongSketchNormal = 1
App.getDocument('Unnamed').getObject('Pad002').SideType = 0
App.getDocument('Unnamed').getObject('Pad002').Type = 0
App.getDocument('Unnamed').getObject('Pad002').Type2 = 0
App.getDocument('Unnamed').getObject('Pad002').UpToFace = None
App.getDocument('Unnamed').getObject('Pad002').UpToFace2 = None
App.getDocument('Unnamed').getObject('Pad002').Reversed = 0
App.getDocument('Unnamed').getObject('Pad002').Offset = 0
App.getDocument('Unnamed').getObject('Pad002').Offset2 = 0
App.getDocument('Unnamed').purgeTouched()
App.getDocument('Unnamed').recompute()
App.getDocument('Unnamed').getObject('Pad001').Visibility = False
# Gui.getDocument('Unnamed').resetEdit()
App.getDocument('Unnamed').getObject('Sketch002').Visibility = False
# Macro End: C:\Users\pawar\AppData\Roaming\FreeCAD\v1-1\Macro\19.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
