import FreeCAD as App
import FreeCADGui as Gui
import os
import time

# ============================================================
# SETTINGS
# ============================================================

input_dir = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\ConstructionTreeAnalysis"

output_dir = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\ConstructionTreeAnalysis\Cube_views"

# Name of the single FreeCAD file
filename = "sphere.FCStd"

# ============================================================
# CAMERA ANGLES
# ============================================================

angles = [
    [30,  45,   0],
    [60, 120,  45],
    [90, 200,  90],
    [120, 30, 135],
    [150, 60, 180],
    [180, 150, 225],
    [210, 240, 270],
    [240, 300, 315],
    [270, 330, 360]
]

# ============================================================
# IMAGE SETTINGS
# ============================================================

IMAGE_WIDTH = 640
IMAGE_HEIGHT = 480

# Time to wait for FreeCAD to redraw
REDRAW_DELAY = 0.5

# ============================================================
# CREATE OUTPUT DIRECTORY
# ============================================================

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("")
print("==============================================")
print("FREECAD AUTOMATIC VIEW GENERATION")
print("==============================================")
print("Input folder:")
print(input_dir)
print("")
print("Input file:")
print(filename)
print("")
print("Output folder:")
print(output_dir)
print("")
print("==============================================")

# ============================================================
# FUNCTION: MAKE ALL OBJECTS VISIBLE
# ============================================================

def make_all_objects_visible(doc):

    print("  Making all model objects visible...")

    for obj in doc.Objects:

        try:

            # Make graphical objects visible
            if hasattr(obj, "ViewObject"):

                obj.ViewObject.Visibility = True

        except Exception as error:

            print(
                "  Could not change visibility of {}: {}".format(
                    obj.Name,
                    error
                )
            )

# ============================================================
# FUNCTION: SET CAMERA
# ============================================================

def set_view_orientation(view, e1, e2, e3):

    # Rotation around X axis
    p1 = App.Rotation(
        App.Vector(1, 0, 0),
        e1
    )

    # Rotation around Y axis
    p2 = App.Rotation(
        App.Vector(0, 1, 0),
        e2
    )

    # Rotation around Z axis
    p3 = App.Rotation(
        App.Vector(0, 0, 1),
        e3
    )

    # Combine rotations
    rotation = p3.multiply(p2).multiply(p1)

    # FreeCAD version accepts the Rotation object directly
    view.setCameraOrientation(rotation)

# ============================================================
# FUNCTION: PREPARE VIEW
# ============================================================

def prepare_view(doc, view):

    # Recompute model
    try:
        doc.recompute()
    except:
        pass

    Gui.updateGui()
    time.sleep(0.3)

    # Make every object visible
    make_all_objects_visible(doc)

    Gui.updateGui()
    time.sleep(0.3)

    # Fit entire model
    try:
        view.fitAll()
    except Exception as error:
        print("  Warning: fitAll failed:", error)

    Gui.updateGui()
    time.sleep(0.5)

# ============================================================
# SOURCE FILE
# ============================================================

filepath = os.path.join(
    input_dir,
    filename
)

# ============================================================
# CHECK FILE EXISTS
# ============================================================

if not os.path.isfile(filepath):

    print("")
    print("ERROR - File not found:")
    print("  " + filepath)
    print("")
    raise SystemExit

# ============================================================
# PROCESS SINGLE FILE
# ============================================================

print("")
print("==============================================")
print("Processing: " + filename)
print("==============================================")

doc = None

try:

    # ========================================================
    # OPEN DOCUMENT
    # ========================================================

    print("  Opening CAD file...")

    doc = App.openDocument(filepath)

    if doc is None:

        print("  ERROR: Could not open document.")
        raise SystemExit

    # ========================================================
    # ACTIVATE DOCUMENT
    # ========================================================

    App.setActiveDocument(doc.Name)

    Gui.updateGui()

    time.sleep(0.5)

    # ========================================================
    # GET GUI DOCUMENT
    # ========================================================

    gui_doc = Gui.getDocument(doc.Name)

    if gui_doc is None:

        print("  ERROR: GUI document not available.")

        App.closeDocument(doc.Name)
        doc = None

        raise SystemExit

    # ========================================================
    # GET ACTIVE 3D VIEW
    # ========================================================

    view = gui_doc.activeView()

    if view is None:

        print("  ERROR: 3D view not available.")

        App.closeDocument(doc.Name)
        doc = None

        raise SystemExit

    # ========================================================
    # MAKE ALL OBJECTS VISIBLE
    # ========================================================

    prepare_view(doc, view)

    # ========================================================
    # CREATE OUTPUT FOLDER
    # ========================================================

    # Since there is only one file, save v1-v9
    # directly inside output_dir

    if not os.path.exists(output_dir):

        os.makedirs(output_dir)

    print("  Output folder:")
    print("  " + output_dir)

    # ========================================================
    # GENERATE 9 VIEWS
    # ========================================================

    count = 0

    for i, angle in enumerate(angles):

        view_number = i + 1

        e1 = angle[0]
        e2 = angle[1]
        e3 = angle[2]

        print("")
        print(
            "  Generating view {} / 9".format(
                view_number
            )
        )

        print(
            "  Angles: X={} Y={} Z={}".format(
                e1,
                e2,
                e3
            )
        )

        # ----------------------------------------------------
        # MAKE SURE OBJECTS ARE STILL VISIBLE
        # ----------------------------------------------------

        make_all_objects_visible(doc)

        # ----------------------------------------------------
        # RECOMPUTE
        # ----------------------------------------------------

        try:
            doc.recompute()
        except:
            pass

        Gui.updateGui()

        time.sleep(0.2)

        # ----------------------------------------------------
        # SET CAMERA ORIENTATION
        # ----------------------------------------------------

        set_view_orientation(
            view,
            e1,
            e2,
            e3
        )

        # ----------------------------------------------------
        # UPDATE GUI
        # ----------------------------------------------------

        Gui.updateGui()

        time.sleep(0.3)

        # ----------------------------------------------------
        # FIT MODEL TO VIEW
        #
        # IMPORTANT:
        # Do this AFTER changing the camera orientation.
        # ----------------------------------------------------

        view.fitAll()

        Gui.updateGui()

        time.sleep(0.5)

        # ----------------------------------------------------
        # FIT AGAIN
        #
        # This helps prevent blank/partially visible
        # images after changing camera orientation.
        # ----------------------------------------------------

        view.fitAll()

        Gui.updateGui()

        time.sleep(REDRAW_DELAY)

        # ----------------------------------------------------
        # SAVE IMAGE
        # ----------------------------------------------------

        image_name = "v{}.png".format(
            view_number
        )

        image_path = os.path.join(
            output_dir,
            image_name
        )

        print(
            "  Saving: " + image_name
        )

        view.saveImage(
            image_path,
            IMAGE_WIDTH,
            IMAGE_HEIGHT,
            "Current"
        )

        # ----------------------------------------------------
        # CHECK IMAGE
        # ----------------------------------------------------

        if os.path.isfile(image_path):

            file_size = os.path.getsize(
                image_path
            )

            print(
                "  SUCCESS - {} bytes".format(
                    file_size
                )
            )

            count += 1

        else:

            print(
                "  WARNING - Image was not created!"
            )

    # ========================================================
    # CLOSE DOCUMENT
    # ========================================================

    print("")
    print("  Closing: " + filename)

    App.closeDocument(doc.Name)

    doc = None

    Gui.updateGui()

    time.sleep(0.5)

    print("")
    print(
        "  FINISHED: " + filename
    )

# ============================================================
# ERROR HANDLING
# ============================================================

except Exception as error:

    print("")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("ERROR while processing: " + filename)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("")
    print(str(error))
    print("")

    # Try to close document
    if doc is not None:

        try:

            App.closeDocument(doc.Name)

        except:

            pass

    doc = None

# ============================================================
# COMPLETE
# ============================================================

print("")
print("")
print("==============================================")
print("FILE PROCESSED")
print("==============================================")
print("")
print("Input file:")
print(filepath)
print("")
print("Output directory:")
print(output_dir)
print("")
print("Total views generated: {}".format(count))
print("")
print("Expected images: 9")
print("")
print("Files:")
print("  v1.png")
print("  v2.png")
print("  v3.png")
print("  v4.png")
print("  v5.png")
print("  v6.png")
print("  v7.png")
print("  v8.png")
print("  v9.png")
print("")
print("==============================================")
