import os
import random
import subprocess
import csv

# EDIT THESE TWO PATHS 
FREECADCMD = r"C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe"

MASTER = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\15_master.py"

OUTPUT = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\15_Variants"

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

    
    outer_dia = random.randint(60, 150)                     # overall flange diameter
    center_hole_dia = round(random.uniform(15, outer_dia * 0.4), 2)   # center bore
    bolt_hole_dia = round(random.uniform(5, outer_dia * 0.15), 2)     # each of the 4 bolt holes
    pad_height = random.randint(5, 30)                       # flange thickness

   
    margin = 2.0
    min_pitch = center_hole_dia / 2.0 + bolt_hole_dia / 2.0 + margin
    max_pitch = outer_dia / 2.0 - bolt_hole_dia / 2.0 - margin
    if max_pitch <= min_pitch:
        continue  
    bolt_pitch_radius = round(random.uniform(min_pitch, max_pitch), 3)

    fcstd = os.path.join(OUTPUT, f"15_{generated + 1:03d}.FCStd")
    stl = os.path.join(OUTPUT, f"15_{generated + 1:03d}.stl")
    pyfile = os.path.join(OUTPUT, f"15_{generated + 1:03d}.py")

    script = master
    script = script.replace("__OUTER_DIA__", str(outer_dia))
    script = script.replace("__CENTER_HOLE_DIA__", str(center_hole_dia))
    script = script.replace("__BOLT_HOLE_DIA__", str(bolt_hole_dia))
    script = script.replace("__BOLT_PITCH_RADIUS__", str(bolt_pitch_radius))
    script = script.replace("__PAD_HEIGHT__", str(pad_height))
    script = script.replace("FCSTD_FILE", 'r"%s"' % fcstd.replace("\\", "/"))
    script = script.replace("STL_FILE", 'r"%s"' % stl.replace("\\", "/"))

    with open(pyfile, "w", encoding="utf-8") as f:
        f.write(script)

    log_path = os.path.join(OUTPUT, "variant_log_15.csv")
    log_exists = os.path.exists(log_path)
    with open(log_path, "a", newline="") as logf:
        writer = csv.writer(logf)
        if not log_exists:
            writer.writerow([
                "variant", "outer_dia", "center_hole_dia", "bolt_hole_dia",
                "bolt_pitch_radius", "pad_height",
            ])
        writer.writerow([
            generated + 1, outer_dia, center_hole_dia, bolt_hole_dia,
            bolt_pitch_radius, pad_height,
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
            f"(OuterDia={outer_dia}, CenterHole={center_hole_dia}, "
            f"BoltHole={bolt_hole_dia}, PitchR={bolt_pitch_radius}, PadH={pad_height})"
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