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
### End command Std_New
### Begin command PartDesign_CompSketches
App.getDocument('Unnamed').addObject('PartDesign::Body','Body')
App.getDocument('Unnamed').getObject('Body').AllowCompound = True
### End command PartDesign_CompSketches
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch')
App.getDocument('Unnamed').getObject('Sketch').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XY_Plane'])
App.getDocument('Unnamed').getObject('Sketch').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
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

App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',1,1,3,2,__BASE_SIZE__)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Distance',0,1,2,2,__BASE_SIZE__)) 
App.getDocument('Unnamed').getObject('Sketch').addConstraint(Sketcher.Constraint('Coincident', 4, 1, -1, 1))


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
App.getDocument('Unnamed').getObject('Pad').Length = __BASE_HEIGHT__
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
App.getDocument('Unnamed').getObject('Sketch001').AttachmentSupport = (App.getDocument('Unnamed').getObject('Pad'),['Face6',])
App.getDocument('Unnamed').getObject('Sketch001').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
### End command PartDesign_NewSketch
App.getDocument('Unnamed').getObject('Sketch001').addExternal("Sketch","Edge3", True, False)
App.getDocument('Unnamed').getObject('Sketch001').addExternal("Sketch","Edge2", True, False)
App.getDocument('Unnamed').getObject('Sketch001').addExternal("Sketch","Edge1", True, False)
App.getDocument('Unnamed').getObject('Sketch001').addExternal("Sketch","Edge4", True, False)
### Begin command Sketcher_ToggleConstruction
App.getDocument('Unnamed').getObject('Sketch001').toggleConstruction(-6) 
App.getDocument('Unnamed').getObject('Sketch001').toggleConstruction(-5) 
App.getDocument('Unnamed').getObject('Sketch001').toggleConstruction(-4) 
App.getDocument('Unnamed').getObject('Sketch001').toggleConstruction(-3) 
### End command Sketcher_ToggleConstruction
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

App.ActiveDocument.recompute()
App.getDocument('Unnamed').recompute()
### Begin command PartDesign_Pad
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad001')
App.getDocument('Unnamed').getObject('Pad001').Profile = (App.getDocument('Unnamed').getObject('Sketch001'), ['',])
App.getDocument('Unnamed').getObject('Pad001').Length = 10
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pad001').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch001'),['N_Axis'])
App.getDocument('Unnamed').getObject('Sketch001').Visibility = False
App.ActiveDocument.recompute()
### End command PartDesign_Pad
App.getDocument('Unnamed').getObject('Pad001').Length = __DIAMOND_HEIGHT__
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
App.getDocument('Unnamed').getObject('Sketch001').Visibility = False
### Begin command PartDesign_NewSketch
App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch002')
App.getDocument('Unnamed').getObject('Sketch002').AttachmentSupport = (App.getDocument('Unnamed').getObject('Pad001'),['Face14',])
App.getDocument('Unnamed').getObject('Sketch002').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
### End command PartDesign_NewSketch
App.getDocument('Unnamed').getObject('Sketch002').addExternal("Sketch001","Edge1", True, False)
App.getDocument('Unnamed').getObject('Sketch002').addExternal("Sketch001","Edge2", True, False)
App.getDocument('Unnamed').getObject('Sketch002').addExternal("Sketch001","Edge4", True, False)
App.getDocument('Unnamed').getObject('Sketch002').addExternal("Sketch001","Edge3", True, False)
### Begin command Sketcher_ToggleConstruction
App.getDocument('Unnamed').getObject('Sketch002').toggleConstruction(-6) 
App.getDocument('Unnamed').getObject('Sketch002').toggleConstruction(-4) 
App.getDocument('Unnamed').getObject('Sketch002').toggleConstruction(-5) 
App.getDocument('Unnamed').getObject('Sketch002').toggleConstruction(-3) 
### End command Sketcher_ToggleConstruction
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

App.ActiveDocument.recompute()
App.getDocument('Unnamed').recompute()
### Begin command PartDesign_Pad
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad002')
App.getDocument('Unnamed').getObject('Pad002').Profile = (App.getDocument('Unnamed').getObject('Sketch002'), ['',])
App.getDocument('Unnamed').getObject('Pad002').Length = 10
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pad002').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch002'),['N_Axis'])
App.getDocument('Unnamed').getObject('Sketch002').Visibility = False
App.ActiveDocument.recompute()
### End command PartDesign_Pad
App.getDocument('Unnamed').getObject('Pad002').Length = __TOP_HEIGHT__
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
App.getDocument('Unnamed').getObject('Sketch002').Visibility = False

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