import os
import random
import subprocess
import csv

# EDIT THESE TWO PATHS 
FREECADCMD = r"C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe"

MASTER = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\16_master.py"

OUTPUT = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\16_Variants"

NUM_VARIANTS = 100


def unhide(path):
    """Clear Windows Hidden/System attributes that sometimes get set on
    files saved into OneDrive-synced folders or by antivirus scans."""
    if os.name == "nt":
        subprocess.run(["attrib", "-h", "-s", path], shell=True)


with open(MASTER, "r", encoding="utf-8") as f:
    master = f.read()

generated = 0
attempt = 0

while generated < NUM_VARIANTS:
    attempt += 1
    print(f"Generating Variant {generated + 1} (Attempt {attempt})")

    
    rect_size = random.randint(80, 200)             # square plate, edge length
    half_size = rect_size / 2.0                      # derived: centering offset

    
    max_corner = half_size * 0.35
    corner_radius = round(random.uniform(8, max(9, max_corner)), 2)

   
    bolt_pos = round(half_size - corner_radius, 3)

 
    max_bolt_dia = max(3.0, min(bolt_pos, corner_radius) * 0.9)
    bolt_hole_dia = round(random.uniform(3.0, max_bolt_dia), 2)

    
    max_spotface = min(bolt_pos * 0.9, corner_radius * 1.8)
    bolt_spotface_dia = round(min(max_spotface, bolt_hole_dia * random.uniform(1.2, 1.5)), 2)
    if bolt_spotface_dia <= bolt_hole_dia:
        continue  # couldn't fit a valid spot-face here, redraw

  
    diag_clearance = bolt_pos * 1.41421356
    max_center_dia = max(15.0, min(rect_size * 0.5, diag_clearance * 1.2))
    center_hole_dia = round(random.uniform(15.0, max_center_dia), 2)

    center_spotface_dia = round(center_hole_dia * random.uniform(1.05, 1.15), 2)

    pad_height = random.randint(5, 30)               # plate thickness
 
    spotface_depth = round(random.uniform(0.5, pad_height * 0.3), 2)

    fcstd = os.path.join(OUTPUT, f"16_{generated + 1:03d}.FCStd")
    stl = os.path.join(OUTPUT, f"16_{generated + 1:03d}.stl")
    pyfile = os.path.join(OUTPUT, f"16_{generated + 1:03d}.py")

    script = master
    script = script.replace("__RECT_SIZE__", str(rect_size))
    script = script.replace("__HALF_SIZE__", str(half_size))
    script = script.replace("__CORNER_RADIUS__", str(corner_radius))
    script = script.replace("__BOLT_POS__", str(bolt_pos))
    script = script.replace("__BOLT_HOLE_DIA__", str(bolt_hole_dia))
    script = script.replace("__BOLT_SPOTFACE_DIA__", str(bolt_spotface_dia))
    script = script.replace("__CENTER_HOLE_DIA__", str(center_hole_dia))
    script = script.replace("__CENTER_SPOTFACE_DIA__", str(center_spotface_dia))
    script = script.replace("__PAD_HEIGHT__", str(pad_height))
    script = script.replace("__SPOTFACE_DEPTH__", str(spotface_depth))
    script = script.replace("FCSTD_FILE", 'r"%s"' % fcstd.replace("\\", "/"))
    script = script.replace("STL_FILE", 'r"%s"' % stl.replace("\\", "/"))

    with open(pyfile, "w", encoding="utf-8") as f:
        f.write(script)

    log_path = os.path.join(OUTPUT, "variant_log_16.csv")
    log_exists = os.path.exists(log_path)
    with open(log_path, "a", newline="") as logf:
        writer = csv.writer(logf)
        if not log_exists:
            writer.writerow([
                "variant", "rect_size", "corner_radius", "bolt_pos",
                "bolt_hole_dia", "bolt_spotface_dia", "center_hole_dia",
                "center_spotface_dia", "pad_height", "spotface_depth",
            ])
        writer.writerow([
            generated + 1, rect_size, corner_radius, bolt_pos,
            bolt_hole_dia, bolt_spotface_dia, center_hole_dia,
            center_spotface_dia, pad_height, spotface_depth,
        ])

    result = subprocess.run(
        [FREECADCMD, pyfile],
        capture_output=True,
        text=True,
    )

    if result.returncode == 0 and os.path.exists(fcstd) and os.path.exists(stl):
        unhide(fcstd)
        unhide(stl)
        unhide(pyfile)
        print(
            f"\u2713 Variant {generated + 1} created "
            f"(Size={rect_size}, CornerR={corner_radius}, BoltPos={bolt_pos}, "
            f"BoltHole={bolt_hole_dia}, CenterHole={center_hole_dia}, "
            f"PadH={pad_height})"
        )
        generated += 1
    else:
        print(f"\u2717 Failed (return code {result.returncode})")
        if result.stdout:
            print("---- stdout ----")
            print(result.stdout)
        if result.stderr:
            print("---- stderr ----")
            print(result.stderr)
        print("Trying another random combination...\n")

print("Finished generating all variants.")