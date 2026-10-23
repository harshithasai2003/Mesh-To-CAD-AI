import os
import random
import subprocess
import csv
import math

# EDIT THESE TWO PATHS FOR YOUR MACHINE
FREECADCMD = r"C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe"

MASTER = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\9_master.py"
OUTPUT = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\9_Variants"

NUM_VARIANTS = 100


def unhide(path):
    if os.name == "nt":
        subprocess.run(["attrib", "-h", "-s", path], shell=True)


with open(MASTER, "r", encoding="utf-8") as f:
    master = f.read()

generated = 0
attempt = 0

while generated < NUM_VARIANTS:
    attempt += 1
    print(f"Generating Variant {generated + 1} (Attempt {attempt})")

   
    base_width = random.randint(60, 150)          # bottom edge of the profile
    side_height = random.randint(80, 200)         # height of both side walls
    pad_height = random.randint(10, 40)            # plate thickness

    
    min_radius = base_width // 2 + 15
    arc_radius = random.randint(min_radius, min_radius + 135)

   
    pocket_dia = random.randint(int(base_width * 0.7), int(base_width * 1.5))

    dome_center_x = base_width / 2.0
    dome_center_y = side_height + math.sqrt(arc_radius ** 2 - (base_width / 2.0) ** 2)

    pocket_pos_x = round(dome_center_x, 3)
    pocket_pos_y = round(dome_center_y, 3)

    fcstd = os.path.join(OUTPUT, f"9_{generated + 1:03d}.FCStd")
    stl = os.path.join(OUTPUT, f"9_{generated + 1:03d}.stl")
    pyfile = os.path.join(OUTPUT, f"9_{generated + 1:03d}.py")

    script = master
    script = script.replace("__BASE_WIDTH__", str(base_width))
    script = script.replace("__SIDE_HEIGHT__", str(side_height))
    script = script.replace("__ARC_RADIUS__", str(arc_radius))
    script = script.replace("__PAD_HEIGHT__", str(pad_height))
    script = script.replace("__POCKET_DIA__", str(pocket_dia))
    script = script.replace("__POCKET_POS_X__", str(pocket_pos_x))
    script = script.replace("__POCKET_POS_Y__", str(pocket_pos_y))
    script = script.replace("FCSTD_FILE", 'r"%s"' % fcstd.replace("\\", "/"))
    script = script.replace("STL_FILE", 'r"%s"' % stl.replace("\\", "/"))

    with open(pyfile, "w", encoding="utf-8") as f:
        f.write(script)

    # CSV logging
    log_path = os.path.join(OUTPUT, "variant_log_9.csv")
    log_exists = os.path.exists(log_path)
    with open(log_path, "a", newline="") as logf:
        writer = csv.writer(logf)
        if not log_exists:
            writer.writerow([
                "variant", "base_width", "side_height", "arc_radius",
                "pad_height", "pocket_dia", "pocket_pos_x", "pocket_pos_y",
            ])
        writer.writerow([
            generated + 1, base_width, side_height, arc_radius,
            pad_height, pocket_dia, pocket_pos_x, pocket_pos_y,
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
            f"(Width={base_width}, SideHeight={side_height}, ArcRadius={arc_radius}, "
            f"PadHeight={pad_height}, PocketDia={pocket_dia})"
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