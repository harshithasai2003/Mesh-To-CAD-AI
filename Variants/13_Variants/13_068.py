import FreeCAD as App
import FreeCAD
import PartDesign
# import PartDesignGui
import Sketcher
import Part
import Mesh

# Create a new document dynamically
doc = App.newDocument()

# --- Create Body ---
body = doc.addObject('PartDesign::Body', 'Body')
body.AllowCompound = True

# --- BASE SKETCH (cylinder profile, on XZ_Plane) ---
sketch = body.newObject('Sketcher::SketchObject', 'Sketch')
sketch.AttachmentSupport = (doc.getObject('Origin'), ['XZ_Plane'])
sketch.MapMode = 'FlatFace'

sketch.addGeometry(Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 25.0), False)
sketch.addConstraint(Sketcher.Constraint('Coincident', 0, 3, -1, 1))
sketch.addConstraint(Sketcher.Constraint('Diameter', 0, 65))

doc.recompute()

# --- FIRST PAD (symmetric cylinder, Midplane=1 so total length = CYL_LEN) ---
pad = body.newObject('PartDesign::Pad', 'Pad')
pad.Profile = sketch
pad.Length = 49
pad.Midplane = 1
pad.Type = 0
pad.AlongSketchNormal = 1

doc.recompute()

# --- GROOVE SKETCH (circle at cylinder surface on XY_Plane) ---
# The circle centre is at (CYL_DIA/2, 0) so the groove sits at the outer surface.
# Revolving 360° around V_Axis (Y) cuts a trough around the cylinder equator.
sketch2 = body.newObject('Sketcher::SketchObject', 'Sketch001')
sketch2.AttachmentSupport = (doc.getObject('Origin'), ['XY_Plane'])
sketch2.MapMode = 'FlatFace'

sketch2.addGeometry(Part.Circle(App.Vector(32.5, 0, 0), App.Vector(0, 0, 1), 3.0), False)
sketch2.addConstraint(Sketcher.Constraint('DistanceX', -1, 1, 0, 3, 32.5))
sketch2.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 0, 3, 0.0))
sketch2.addConstraint(Sketcher.Constraint('Radius', 0, 4.97))

doc.recompute()

# --- GROOVE CUT (360-degree revolve around cylinder axis) ---
groove = body.newObject('PartDesign::Groove', 'Groove')
groove.Profile = sketch2
groove.Angle = 360.0
groove.ReferenceAxis = (sketch2, ['V_Axis'])
groove.Type = 0

body.Tip = groove

sketch.Visibility = False
sketch2.Visibility = False

doc.recompute(None, True, True)
doc.saveAs(r"C:/Users/harsh/OneDrive/Desktop/SCIENTIFIC COMPUTING/THIRD SEMESTER/MODELLING SEMINAR B/Variants/13_Variants/13_068.FCStd")

__objs__ = []
__objs__.append(FreeCAD.getDocument(doc.Name).getObject("Body"))
if hasattr(Mesh, "exportOptions"):
    options = Mesh.exportOptions(r"C:/Users/harsh/OneDrive/Desktop/SCIENTIFIC COMPUTING/THIRD SEMESTER/MODELLING SEMINAR B/Variants/13_Variants/13_068.stl")
    Mesh.export(__objs__, r"C:/Users/harsh/OneDrive/Desktop/SCIENTIFIC COMPUTING/THIRD SEMESTER/MODELLING SEMINAR B/Variants/13_Variants/13_068.stl", options)
else:
    Mesh.export(__objs__, r"C:/Users/harsh/OneDrive/Desktop/SCIENTIFIC COMPUTING/THIRD SEMESTER/MODELLING SEMINAR B/Variants/13_Variants/13_068.stl")
del __objs__

App.closeDocument(doc.Name)