import os
import random
import subprocess
import csv

# EDIT THESE TWO PATHS
FREECADCMD = r"C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe"

MASTER = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\4_master.py"

OUTPUT = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\4_Variants"

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

    
    outerMajor = random.randint(80, 150)
    outerMinor = random.randint(int(outerMajor * 0.35), int(outerMajor * 0.7))

   
    innerMajor = random.randint(int(outerMajor * 0.4), int(outerMajor * 0.65))
    innerMinor = random.randint(int(outerMinor * 0.35), int(outerMinor * 0.65))

    padHeight = random.randint(60, 150)

  
    wallThickness = outerMajor - innerMajor
    maxHoleDia = max(8, min(30, wallThickness - 5))
    holeDia = random.randint(8, maxHoleDia)

  
    hole1X = -(outerMajor - holeDia)
    hole2X = (outerMajor - holeDia)

    fcstd = os.path.join(OUTPUT, f"4_{generated + 1:03d}.FCStd")
    stl = os.path.join(OUTPUT, f"4_{generated + 1:03d}.stl")
    pyfile = os.path.join(OUTPUT, f"4_{generated + 1:03d}.py")

    script = master
    script = script.replace("__OUTER_MAJOR__", str(outerMajor))
    script = script.replace("__OUTER_MINOR__", str(outerMinor))
    script = script.replace("__INNER_MAJOR__", str(innerMajor))
    script = script.replace("__INNER_MINOR__", str(innerMinor))
    script = script.replace("__PAD_HEIGHT__", str(padHeight))
    script = script.replace("__HOLE_DIA__", str(holeDia))
    script = script.replace("__HOLE1_X__", str(hole1X))
    script = script.replace("__HOLE2_X__", str(hole2X))
    script = script.replace("FCSTD_FILE", 'r"%s"' % fcstd.replace("\\", "/"))
    script = script.replace("STL_FILE", 'r"%s"' % stl.replace("\\", "/"))

    with open(pyfile, "w", encoding="utf-8") as f:
        f.write(script)

    # CSV logging
    log_path = os.path.join(OUTPUT, "variant_log_4.csv")
    log_exists = os.path.exists(log_path)
    with open(log_path, "a", newline="") as logf:
        writer = csv.writer(logf)
        if not log_exists:
            writer.writerow(
                ["variant", "outerMajor", "outerMinor", "innerMajor",
                 "innerMinor", "padHeight", "holeDia"]
            )
        writer.writerow(
            [generated + 1, outerMajor, outerMinor, innerMajor,
             innerMinor, padHeight, holeDia]
        )

   
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
            f"(OuterMajor={outerMajor}, OuterMinor={outerMinor}, "
            f"InnerMajor={innerMajor}, InnerMinor={innerMinor}, "
            f"PadHeight={padHeight}, HoleDia={holeDia})"
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