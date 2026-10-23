import FreeCAD
import FreeCAD as App
import Part
import PartDesign
import Sketcher
import Mesh

### Begin command Std_New
App.newDocument()
### End command Std_New

App.getDocument('Unnamed').addObject('PartDesign::Body','Body')
App.getDocument('Unnamed').getObject('Body').AllowCompound = True

App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject','Sketch')
App.getDocument('Unnamed').getObject('Sketch').AttachmentSupport = (App.getDocument('Unnamed').getObject('Origin'),['XZ_Plane'])
App.getDocument('Unnamed').getObject('Sketch').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
ActiveSketch = App.getDocument('Unnamed').getObject('Sketch')


_D0, _D1, _D2, _D3, _D4 = __D0__, __D1__, __D2__, __D3__, __D4__
_HOLE_DIA = __HOLE_DIA__
_PAD_THICKNESS = __PAD_THICKNESS__

left_width = _D1 - _D3

P0 = App.Vector(0, 0, 0)
P1 = App.Vector(0, _D0, 0)
P2 = App.Vector(left_width, _D0, 0)
P3 = App.Vector(left_width, _D2, 0)
P4 = App.Vector(_D1, _D2, 0)
P5 = App.Vector(_D1, 0, 0)

C1 = App.Vector(left_width / 2.0, _D0, 0)
C2 = App.Vector(_D1, _D2 / 2.0, 0)

# 0: Left vertical edge (P0 to P1)
ActiveSketch.addGeometry([Part.LineSegment(P0, P1)], False)
# 1: Top Arc Semicircle (Starts at P2 (angle 0), ends at P1 (angle PI))
ActiveSketch.addGeometry([Part.ArcOfCircle(Part.Circle(C1, App.Vector(0,0,1), left_width/2.0), 0.0, 3.141593)], False)
# 2: Inner vertical edge (P2 to P3)
ActiveSketch.addGeometry([Part.LineSegment(P2, P3)], False)
# 3: Inner horizontal notch (P3 to P4)
ActiveSketch.addGeometry([Part.LineSegment(P3, P4)], False)
# 4: Right Arc Semicircle (Starts at P5 (angle -PI/2), ends at P4 (angle PI/2))
ActiveSketch.addGeometry([Part.ArcOfCircle(Part.Circle(C2, App.Vector(0,0,1), _D2/2.0), -1.570796, 1.570796)], False)
# 5: Bottom horizontal edge (P5 to P0)
ActiveSketch.addGeometry([Part.LineSegment(P5, P0)], False)

# 6: Top Hole
ActiveSketch.addGeometry([Part.Circle(C1, App.Vector(0,0,1), _HOLE_DIA/2.0)], False)
# 7: Right Hole
ActiveSketch.addGeometry([Part.Circle(C2, App.Vector(0,0,1), _HOLE_DIA/2.0)], False)


# --- CONSTRAINTS ---

# Link the outer loop end-to-end
ActiveSketch.addConstraint(Sketcher.Constraint('Coincident', 0, 2, 1, 2))
ActiveSketch.addConstraint(Sketcher.Constraint('Coincident', 1, 1, 2, 1))
ActiveSketch.addConstraint(Sketcher.Constraint('Coincident', 2, 2, 3, 1))
ActiveSketch.addConstraint(Sketcher.Constraint('Coincident', 3, 2, 4, 2))
ActiveSketch.addConstraint(Sketcher.Constraint('Coincident', 4, 1, 5, 1))
ActiveSketch.addConstraint(Sketcher.Constraint('Coincident', 5, 2, 0, 1))

# Anchor bottom-left to origin
ActiveSketch.addConstraint(Sketcher.Constraint('Coincident', 0, 1, -1, 1))

# Geometric Alignments (forces perfect 90-degree inner/outer corners)
ActiveSketch.addConstraint(Sketcher.Constraint('Vertical', 0))
ActiveSketch.addConstraint(Sketcher.Constraint('Vertical', 2))
ActiveSketch.addConstraint(Sketcher.Constraint('Horizontal', 3))
ActiveSketch.addConstraint(Sketcher.Constraint('Horizontal', 5))

# Cap Semicircle rules (forces arcs to align perfectly with flat edges)
ActiveSketch.addConstraint(Sketcher.Constraint('Horizontal', 1, 1, 1, 2))
ActiveSketch.addConstraint(Sketcher.Constraint('Horizontal', 1, 3, 1, 1))
ActiveSketch.addConstraint(Sketcher.Constraint('Vertical', 4, 1, 4, 2))
ActiveSketch.addConstraint(Sketcher.Constraint('Vertical', 4, 3, 4, 1))

# Dimensional Constraints 
ActiveSketch.addConstraint(Sketcher.Constraint('Distance', 0, _D0))
ActiveSketch.addConstraint(Sketcher.Constraint('Distance', 5, _D1))
ActiveSketch.addConstraint(Sketcher.Constraint('Distance', 3, _D3))
ActiveSketch.addConstraint(Sketcher.Constraint('Radius', 4, _D2 / 2.0))
# D4 derived constraint skipped to prevent redundancy solver crash: __D4__

# Lock Holes to Cap Centers
ActiveSketch.addConstraint(Sketcher.Constraint('Coincident', 6, 3, 1, 3))
ActiveSketch.addConstraint(Sketcher.Constraint('Diameter', 6, _HOLE_DIA))

ActiveSketch.addConstraint(Sketcher.Constraint('Coincident', 7, 3, 4, 3))
ActiveSketch.addConstraint(Sketcher.Constraint('Diameter', 7, _HOLE_DIA))


App.ActiveDocument.recompute()
App.getDocument('Unnamed').recompute()

### Begin command PartDesign_Pad
App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad')
App.getDocument('Unnamed').getObject('Pad').Profile = (App.getDocument('Unnamed').getObject('Sketch'), ['',])
App.getDocument('Unnamed').getObject('Pad').Length = _PAD_THICKNESS
App.ActiveDocument.recompute()
App.getDocument('Unnamed').getObject('Pad').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'),['N_Axis'])
App.getDocument('Unnamed').getObject('Sketch').Visibility = False
App.ActiveDocument.recompute()
### End command PartDesign_Pad

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
App.getDocument('Unnamed').recompute()

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