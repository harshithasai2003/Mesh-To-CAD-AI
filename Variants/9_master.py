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
# Gui.Selection.addSelection('Unnamed','Body','Origin.XY_Plane.',18.5629,15.4938,0)
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
# Gui.runCommand('Sketcher_CreateLine',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 0.000000, 0.000000),App.Vector(100.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,__BASE_WIDTH__)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Horizontal',0)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 0, 1, -1, 1))


# Gui.runCommand('Sketcher_CreateLine',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(100.000000, 0.000000, 0.000000),App.Vector(100.000000, 150.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,__SIDE_HEIGHT__)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',1)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 1, 1, 0, 2))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 0.000000, 0.000000),App.Vector(0.000000, 150.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',2,__SIDE_HEIGHT__)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',2)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 2, 1, 0, 1))


# Gui.runCommand('Sketcher_CompCreateArc',1)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.ArcOfCircle(Part.Circle(App.Vector(50.000000, 236.726873, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 100.107695), 5.235367, 10.472597))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 3, 2, 2, 2))
constraintList.append(Sketcher.Constraint('Coincident', 3, 1, 1, 2))
App.getDocument('Unnamed').getObject('Sketch').addConstraint(constraintList)
del constraintList

# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Radius',3,100.107695)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch.Edge4',-44.5765,269.542,0,False)
App.getDocument('Unnamed').getObject('Sketch').setDatum(11,App.Units.Quantity('__ARC_RADIUS__ mm'))
# Gui.Selection.clearSelection()
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
App.getDocument('Unnamed').getObject('Pad').Length = __PAD_HEIGHT__
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
# App.getDocument('Unnamed').purgeTouched()
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
# Gui.Selection.clearSelection()
# App.getDocument('Unnamed').getObject('Pad').Length = __PAD_HEIGHT__
# App.getDocument('Unnamed').getObject('Pad').TaperAngle = 0.000000
# App.getDocument('Unnamed').getObject('Pad').UseCustomVector = 0
# App.getDocument('Unnamed').getObject('Pad').Direction = (0, 0, 1)
# App.getDocument('Unnamed').getObject('Pad').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'), ['N_Axis'])
# App.getDocument('Unnamed').getObject('Pad').AlongSketchNormal = 1
# App.getDocument('Unnamed').getObject('Pad').SideType = 0
# App.getDocument('Unnamed').getObject('Pad').Type = 0
# App.getDocument('Unnamed').getObject('Pad').Type2 = 0
# App.getDocument('Unnamed').getObject('Pad').UpToFace = None
# App.getDocument('Unnamed').getObject('Pad').UpToFace2 = None
# App.getDocument('Unnamed').getObject('Pad').Reversed = 0
# App.getDocument('Unnamed').getObject('Pad').Offset = 0
# App.getDocument('Unnamed').getObject('Pad').Offset2 = 0
# App.getDocument('Unnamed').purgeTouched()
# App.getDocument('Unnamed').recompute()
# Gui.getDocument('Unnamed').resetEdit()
App.getDocument('Unnamed').getObject('Sketch').Visibility = False
# Gui.Selection.addSelection('Unnamed','Body','Pad.Face6',52.7513,277.657,20)
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
geoList.append(Part.Circle(App.Vector(56.010113, 234.926071, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 69.000731))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
# Gui.runCommand('Sketcher_CompDimensionTools',0)
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',0,138.001462)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Edge1',124.072,246.27,0,False)
App.getDocument('Unnamed').getObject('Sketch001').deleteAllGeometry(True)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(52.762591, 221.304824, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 65.000000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter', 0, __POCKET_DIA__))


App.getDocument('Unnamed').getObject('Sketch001').setGeometryIds([(0,1)])
App.getDocument('Unnamed').getObject('Sketch001').setDatum(0,App.Units.Quantity('__POCKET_DIA__ mm'))
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',0,3,-1,1,227.507618)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex1',52.7626,221.305,0,False)

# Gui.Selection.addSelection('Unnamed','Body','Sketch001.H_Axis',164.342,0,0,False)
App.getDocument('Unnamed').getObject('Sketch001').setDatum(1,App.Units.Quantity('__POCKET_POS_Y__ mm'))
# Gui.Selection.clearSelection()

# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex1',52.7626,236.6,0,False)
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',0,3,-2,52.762591)) 
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.V_Axis',0,235.813,0,False)
App.getDocument('Unnamed').getObject('Sketch001').setDatum(2,App.Units.Quantity('__POCKET_POS_X__ mm'))
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
# App.getDocument('Unnamed').purgeTouched()
App.getDocument('Unnamed').recompute()
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
# App.getDocument('Unnamed').getObject('Pocket').TaperAngle = 0.000000
# App.getDocument('Unnamed').getObject('Pocket').UseCustomVector = 0
# App.getDocument('Unnamed').getObject('Pocket').Direction = (0, 0, -1)
# App.getDocument('Unnamed').getObject('Pocket').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch001'), ['N_Axis'])
# App.getDocument('Unnamed').getObject('Pocket').AlongSketchNormal = 1
# App.getDocument('Unnamed').getObject('Pocket').SideType = 0
# App.getDocument('Unnamed').getObject('Pocket').Type = 1
# App.getDocument('Unnamed').getObject('Pocket').Type2 = 0
# App.getDocument('Unnamed').getObject('Pocket').UpToFace = None
# App.getDocument('Unnamed').getObject('Pocket').UpToFace2 = None
# App.getDocument('Unnamed').getObject('Pocket').Reversed = 0
# App.getDocument('Unnamed').getObject('Pocket').Offset = 0
# App.getDocument('Unnamed').getObject('Pocket').Offset2 = 0
# App.getDocument('Unnamed').purgeTouched()
# App.getDocument('Unnamed').recompute()
App.getDocument('Unnamed').getObject('Pad').Visibility = False
# Gui.getDocument('Unnamed').resetEdit()
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