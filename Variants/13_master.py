import FreeCAD as App
import FreeCAD
import PartDesign
# import PartDesignGui
import Sketcher
import Part
import Mesh

doc = App.newDocument()


body = doc.addObject('PartDesign::Body', 'Body')
body.AllowCompound = True

sketch = body.newObject('Sketcher::SketchObject', 'Sketch')
sketch.AttachmentSupport = (doc.getObject('Origin'), ['XZ_Plane'])
sketch.MapMode = 'FlatFace'

sketch.addGeometry(Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 25.0), False)
sketch.addConstraint(Sketcher.Constraint('Coincident', 0, 3, -1, 1))
sketch.addConstraint(Sketcher.Constraint('Diameter', 0, __CYL_DIA__))

doc.recompute()


pad = body.newObject('PartDesign::Pad', 'Pad')
pad.Profile = sketch
pad.Length = __CYL_LEN__
pad.Midplane = 1
pad.Type = 0
pad.AlongSketchNormal = 1

doc.recompute()


sketch2 = body.newObject('Sketcher::SketchObject', 'Sketch001')
sketch2.AttachmentSupport = (doc.getObject('Origin'), ['XY_Plane'])
sketch2.MapMode = 'FlatFace'

sketch2.addGeometry(Part.Circle(App.Vector(__GROOVE_X__, 0, 0), App.Vector(0, 0, 1), 3.0), False)
sketch2.addConstraint(Sketcher.Constraint('DistanceX', -1, 1, 0, 3, __GROOVE_X__))
sketch2.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 0, 3, 0.0))
sketch2.addConstraint(Sketcher.Constraint('Radius', 0, __GROOVE_R__))

doc.recompute()


groove = body.newObject('PartDesign::Groove', 'Groove')
groove.Profile = sketch2
groove.Angle = 360.0
groove.ReferenceAxis = (sketch2, ['V_Axis'])
groove.Type = 0

body.Tip = groove

sketch.Visibility = False
sketch2.Visibility = False

doc.recompute(None, True, True)
doc.saveAs(FCSTD_FILE)

__objs__ = []
__objs__.append(FreeCAD.getDocument(doc.Name).getObject("Body"))
if hasattr(Mesh, "exportOptions"):
    options = Mesh.exportOptions(STL_FILE)
    Mesh.export(__objs__, STL_FILE, options)
else:
    Mesh.export(__objs__, STL_FILE)
del __objs__

App.closeDocument(doc.Name)