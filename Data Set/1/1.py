# Macro Begin: C:\Users\pawar\AppData\Roaming\FreeCAD\v1-1\Macro\1.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
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
# Gui.Selection.addSelection('Unnamed','Body','Origin.XZ_Plane.',16.6475,-1.98937e-06,16.688)
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch')
App.getDocument('Unnamed').getObject('Sketch').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XZ_Plane'])
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
# Gui.runCommand('Sketcher_CompLine',1)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 0.000000, 0.000000),App.Vector(0.000000, 80.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,80.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',0)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 0, 1, -1, 1))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(0.000000, 80.000000, 0.000000),App.Vector(12.000000, 80.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,12.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Horizontal',1)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 1, 1, 0, 2))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(12.000000, 80.000000, 0.000000),App.Vector(12.000000, 12.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',2,68.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',2)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 2, 1, 1, 2))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(12.000000, 12.000000, 0.000000),App.Vector(80.000000, 12.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',3,68.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Horizontal',3)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 3, 1, 2, 2))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(80.000000, 12.000000, 0.000000),App.Vector(80.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',4,12.000000)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Vertical',4)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 4, 1, 3, 2))


ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.LineSegment(App.Vector(80.000000, 0.000000, 0.000000),App.Vector(0.000000, 0.000000, 0.000000)))
App.getDocument('Unnamed').getObject('Sketch').addGeometry(geoList,False)
del geoList

constraintList = []
constraintList = []
constraintList.append(Sketcher.Constraint('Coincident', 5, 1, 4, 2))
constraintList.append(Sketcher.Constraint('Coincident', 5, 2, 0, 1))
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
App.getDocument('Unnamed').getObject('Pad').Length = 80.000000
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
# App.getDocument('Unnamed').getObject('Pad').Length = 80.000000
# App.getDocument('Unnamed').getObject('Pad').TaperAngle = 0.000000
# App.getDocument('Unnamed').getObject('Pad').UseCustomVector = 0
# App.getDocument('Unnamed').getObject('Pad').Direction = (0, -1, 0)
# App.getDocument('Unnamed').getObject('Pad').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'), ['N_Axis'])
# App.getDocument('Unnamed').getObject('Pad').AlongSketchNormal = 1
# App.getDocument('Unnamed').getObject('Pad').SideType = 2
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
# Gui.Selection.addSelection('Unnamed','Body','Pad.Edge16',80,-40,6.73039)
# Gui.Selection.addSelection('Unnamed','Body','Pad.Edge7',8.09762,-40,80)
# Gui.Selection.addSelection('Unnamed','Body','Pad.Edge6',7.30439,40,80)
# Gui.Selection.addSelection('Unnamed','Body','Pad.Edge15',80,40,5.98166)
### Begin command PartDesign_Fillet
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Fillet','Fillet')
App.getDocument('Unnamed').getObject('Fillet').Base = (App.getDocument('Unnamed').getObject('Pad'),['Edge16','Edge7','Edge6','Edge15',])
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Pad').Visibility = False
App.ActiveDocument.recompute()
# App.getDocument('Unnamed').getObject('Fillet').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Fillet').ViewObject.ShapeAppearance)
# App.getDocument('Unnamed').getObject('Fillet').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Fillet').ViewObject.LineColor)
# App.getDocument('Unnamed').getObject('Fillet').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Fillet').ViewObject.PointColor)
# App.getDocument('Unnamed').getObject('Fillet').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Fillet').ViewObject.Transparency)
# App.getDocument('Unnamed').getObject('Fillet').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Pad').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Fillet').ViewObject.DisplayMode)
# Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Fillet.')
# Gui.Selection.clearSelection()
### End command PartDesign_Fillet
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Fillet').Radius = 20.000000
App.getDocument('Unnamed').getObject('Fillet').Base = (App.getDocument('Unnamed').getObject('Pad'),["Edge16","Edge7","Edge6","Edge15",])
App.getDocument('Unnamed').getObject('Fillet').Radius = 20.000000
#App.getDocument('Unnamed').purgeTouched()
App.getDocument('Unnamed').recompute()
App.getDocument('Unnamed').getObject('Pad').Visibility = False
# Gui.getDocument('Unnamed').resetEdit()
# Gui.Selection.addSelection('Unnamed','Body','Fillet.Face8',12,3.81708,36.8677)
### Begin command PartDesign_NewSketch
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch001')
App.getDocument('Unnamed').getObject('Sketch001').AttachmentSupport = (App.getDocument('Unnamed').getObject('Fillet'),['Face8',])
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
geoList.append(Part.Circle(App.Vector(26.182484, 68.096939, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 5.000000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',0,10.000000)) 
constraintList = []
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch001')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(-26.271509, 66.409828, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 5.000000))
App.getDocument('Unnamed').getObject('Sketch001').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Diameter',1,10.000000)) 
constraintList = []
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex1',12.014,26.1825,68.0969,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.H_Axis',12.002,49.6487,0,False)
### Begin command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',0,3,-1,68.096939)) 
### End command Sketcher_CompDimensionTools
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch001').setDatum(2,App.Units.Quantity('60.000000 mm'))
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.V_Axis',12.002,0,58.1276,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex1',12.014,26.1825,60,False)
### Begin command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',0,3,-2,26.182484)) 
### End command Sketcher_CompDimensionTools
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch001').setDatum(3,App.Units.Quantity('20.000000 mm'))
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.V_Axis',12.002,0,88.0356,False)
# Gui.Selection.removeSelection('Unnamed','Body','Sketch001.V_Axis')
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.V_Axis',12.002,0,87.1153,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex2',12.014,-26.2715,66.4098,False)
### Begin command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',1,3,-2,26.271509)) 
### End command Sketcher_CompDimensionTools
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch001').setDatum(4,App.Units.Quantity('20.000000 mm'))
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.Vertex2',12.014,-20,66.4098,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch001.H_Axis',12.002,-54.339,0,False)
### Begin command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch001').addConstraint(Sketcher.Constraint('Distance',1,3,-1,66.409828)) 
### End command Sketcher_CompDimensionTools
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch001').setDatum(5,App.Units.Quantity('60.000000 mm'))
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
# App.getDocument('Unnamed').purgeTouched()
App.getDocument('Unnamed').recompute()
App.ActiveDocument.recompute()
# App.getDocument('Unnamed').getObject('Pocket').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Fillet').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Pocket').ViewObject.ShapeAppearance)
# App.getDocument('Unnamed').getObject('Pocket').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Fillet').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Pocket').ViewObject.LineColor)
# App.getDocument('Unnamed').getObject('Pocket').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Fillet').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Pocket').ViewObject.PointColor)
# App.getDocument('Unnamed').getObject('Pocket').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Fillet').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Pocket').ViewObject.Transparency)
# App.getDocument('Unnamed').getObject('Pocket').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Fillet').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Pocket').ViewObject.DisplayMode)
# Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Pocket.')
# Gui.Selection.clearSelection()
### End command PartDesign_Pocket
# Gui.Selection.clearSelection()
# App.getDocument('Unnamed').getObject('Pocket').TaperAngle = 0.000000
# App.getDocument('Unnamed').getObject('Pocket').UseCustomVector = 0
# App.getDocument('Unnamed').getObject('Pocket').Direction = (-1, 0, 0)
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
App.getDocument('Unnamed').getObject('Fillet').Visibility = False
# Gui.getDocument('Unnamed').resetEdit()
App.getDocument('Unnamed').getObject('Sketch001').Visibility = False
# Gui.Selection.addSelection('Unnamed','Body','Pocket.Face12',60.9968,3.35075,12)
### Begin command PartDesign_NewSketch
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch002')
App.getDocument('Unnamed').getObject('Sketch002').AttachmentSupport = (App.getDocument('Unnamed').getObject('Pocket'),['Face12',])
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
# Gui.runCommand('Sketcher_CompCreateConic',0)
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(64.162048, 25.404104, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 5.000000))
App.getDocument('Unnamed').getObject('Sketch002').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Diameter',0,10.000000)) 
constraintList = []
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch002')

lastGeoId = len(ActiveSketch.Geometry)

geoList = []
geoList.append(Part.Circle(App.Vector(64.536713, -27.423435, 0.000000), App.Vector(0.000000, 0.000000, 1.000000), 5.000000))
App.getDocument('Unnamed').getObject('Sketch002').addGeometry(geoList,False)
del geoList

constraintList = []
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Diameter',1,10.000000)) 
constraintList = []
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Vertex1',64.162,25.4041,12.014,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.H_Axis',67.0969,2.66454e-15,12.002,False)
### Begin command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',0,3,-1,25.404104)) 
### End command Sketcher_CompDimensionTools
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch002').setDatum(2,App.Units.Quantity('20.000000 mm'))
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Vertex2',64.5367,-27.4234,12.014,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.H_Axis',72.3838,2.66454e-15,12.002,False)
### Begin command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',1,3,-1,27.423435)) 
### End command Sketcher_CompDimensionTools
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch002').setDatum(3,App.Units.Quantity('20.000000 mm'))
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Vertex2',64.5367,-20,12.014,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.V_Axis',0,-45.1824,12.002,False)
### Begin command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',1,3,-2,64.536713)) 
### End command Sketcher_CompDimensionTools
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch002').setDatum(4,App.Units.Quantity('60.000000 mm'))
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.Vertex1',64.162,20,12.014,False)
# Gui.Selection.addSelection('Unnamed','Body','Sketch002.V_Axis',0,47.9214,12.002,False)
### Begin command Sketcher_CompDimensionTools
App.getDocument('Unnamed').getObject('Sketch002').addConstraint(Sketcher.Constraint('Distance',0,3,-2,64.162048)) 
### End command Sketcher_CompDimensionTools
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Sketch002').setDatum(5,App.Units.Quantity('60.000000 mm'))
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
### Begin command PartDesign_Pocket
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pocket','Pocket001')
App.getDocument('Unnamed').getObject('Pocket001').Profile = (App.getDocument('Unnamed').getObject('Sketch002'), ['',])
App.getDocument('Unnamed').getObject('Pocket001').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pocket001').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pocket001').Direction = (0, 0, -1)
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pocket001').TaperAngle = 0.000000
App.getDocument('Unnamed').getObject('Pocket001').UseCustomVector = 0
App.getDocument('Unnamed').getObject('Pocket001').Direction = (0, 0, -1)
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
# App.getDocument('Unnamed').purgeTouched()
App.getDocument('Unnamed').recompute()
App.ActiveDocument.recompute()
# App.getDocument('Unnamed').getObject('Pocket001').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Pocket').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Pocket001').ViewObject.ShapeAppearance)
# App.getDocument('Unnamed').getObject('Pocket001').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Pocket').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Pocket001').ViewObject.LineColor)
# App.getDocument('Unnamed').getObject('Pocket001').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Pocket').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Pocket001').ViewObject.PointColor)
# App.getDocument('Unnamed').getObject('Pocket001').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Pocket').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Pocket001').ViewObject.Transparency)
# App.getDocument('Unnamed').getObject('Pocket001').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Pocket').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Pocket001').ViewObject.DisplayMode)
# Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Pocket001.')
# Gui.Selection.clearSelection()
### End command PartDesign_Pocket
# Gui.Selection.clearSelection()
# App.getDocument('Unnamed').getObject('Pocket001').TaperAngle = 0.000000
# App.getDocument('Unnamed').getObject('Pocket001').UseCustomVector = 0
# App.getDocument('Unnamed').getObject('Pocket001').Direction = (0, 0, -1)
# App.getDocument('Unnamed').getObject('Pocket001').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch002'), ['N_Axis'])
# App.getDocument('Unnamed').getObject('Pocket001').AlongSketchNormal = 1
# App.getDocument('Unnamed').getObject('Pocket001').SideType = 0
# App.getDocument('Unnamed').getObject('Pocket001').Type = 1
# App.getDocument('Unnamed').getObject('Pocket001').Type2 = 0
# App.getDocument('Unnamed').getObject('Pocket001').UpToFace = None
# App.getDocument('Unnamed').getObject('Pocket001').UpToFace2 = None
# App.getDocument('Unnamed').getObject('Pocket001').Reversed = 0
# App.getDocument('Unnamed').getObject('Pocket001').Offset = 0
# App.getDocument('Unnamed').getObject('Pocket001').Offset2 = 0
# App.getDocument('Unnamed').purgeTouched()
# App.getDocument('Unnamed').recompute()
App.getDocument('Unnamed').getObject('Pocket').Visibility = False
# Gui.getDocument('Unnamed').resetEdit()
App.getDocument('Unnamed').getObject('Sketch002').Visibility = False
### Begin command Std_ViewIsometric
# Gui.activeDocument().activeView().viewIsometric()
### End command Std_ViewIsometric
# Gui.runCommand('Std_ViewGroup',0)
# Gui.Selection.addSelection('Unnamed','Body','Pocket001.Edge33',12,-9.95378,12)
### Begin command PartDesign_Fillet
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Fillet','Fillet001')
App.getDocument('Unnamed').getObject('Fillet001').Base = (App.getDocument('Unnamed').getObject('Pocket001'),['Edge33',])
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Pocket001').Visibility = False
App.ActiveDocument.recompute()
# App.getDocument('Unnamed').getObject('Fillet001').ViewObject.ShapeAppearance=getattr(App.getDocument('Unnamed').getObject('Pocket001').getLinkedObject(True).ViewObject,'ShapeAppearance',App.getDocument('Unnamed').getObject('Fillet001').ViewObject.ShapeAppearance)
# App.getDocument('Unnamed').getObject('Fillet001').ViewObject.LineColor=getattr(App.getDocument('Unnamed').getObject('Pocket001').getLinkedObject(True).ViewObject,'LineColor',App.getDocument('Unnamed').getObject('Fillet001').ViewObject.LineColor)
# App.getDocument('Unnamed').getObject('Fillet001').ViewObject.PointColor=getattr(App.getDocument('Unnamed').getObject('Pocket001').getLinkedObject(True).ViewObject,'PointColor',App.getDocument('Unnamed').getObject('Fillet001').ViewObject.PointColor)
# App.getDocument('Unnamed').getObject('Fillet001').ViewObject.Transparency=getattr(App.getDocument('Unnamed').getObject('Pocket001').getLinkedObject(True).ViewObject,'Transparency',App.getDocument('Unnamed').getObject('Fillet001').ViewObject.Transparency)
# App.getDocument('Unnamed').getObject('Fillet001').ViewObject.DisplayMode=getattr(App.getDocument('Unnamed').getObject('Pocket001').getLinkedObject(True).ViewObject,'DisplayMode',App.getDocument('Unnamed').getObject('Fillet001').ViewObject.DisplayMode)
# Gui.getDocument('Unnamed').setEdit(App.getDocument('Unnamed').getObject('Body'), 0, 'Fillet001.')
# Gui.Selection.clearSelection()
### End command PartDesign_Fillet
# Gui.Selection.clearSelection()
App.getDocument('Unnamed').getObject('Fillet001').Radius = 2.000000
App.getDocument('Unnamed').getObject('Fillet001').Base = (App.getDocument('Unnamed').getObject('Pocket001'),["Edge33",])
App.getDocument('Unnamed').getObject('Fillet001').Radius = 2.000000
#App.getDocument('Unnamed').purgeTouched()
App.getDocument('Unnamed').recompute()
App.getDocument('Unnamed').getObject('Pocket001').Visibility = False
# Gui.getDocument('Unnamed').resetEdit()
# Macro End: C:\Users\pawar\AppData\Roaming\FreeCAD\v1-1\Macro\1.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
