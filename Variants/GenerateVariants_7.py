import os
import random
import subprocess
import csv

# EDIT THESE TWO PATHS 
FREECADCMD = r"C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe"

MASTER = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\7_master.py"

OUTPUT = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\7_Variants"

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

    size = random.randint(30, 80)              # square side length
    height = random.randint(20, 80)             # pad thickness
    
    filletRadius = random.randint(3, max(4, int(size * 0.3)))
   
    maxHoleDia = max(6, size - 2 * filletRadius - 5)
    holeDia = random.randint(6, maxHoleDia)

    fcstd = os.path.join(OUTPUT, f"7_{generated + 1:03d}.FCStd")
    stl = os.path.join(OUTPUT, f"7_{generated + 1:03d}.stl")
    pyfile = os.path.join(OUTPUT, f"7_{generated + 1:03d}.py")

    script = master
    script = script.replace("__SIZE__", str(size))
    script = script.replace("__HEIGHT__", str(height))
    script = script.replace("__FILLET_RADIUS__", str(filletRadius))
    script = script.replace("__HOLE_DIA__", str(holeDia))
    script = script.replace("FCSTD_FILE", 'r"%s"' % fcstd.replace("\\", "/"))
    script = script.replace("STL_FILE", 'r"%s"' % stl.replace("\\", "/"))

    with open(pyfile, "w", encoding="utf-8") as f:
        f.write(script)

    log_path = os.path.join(OUTPUT, "variant_log_7.csv")
    log_exists = os.path.exists(log_path)
    with open(log_path, "a", newline="") as logf:
        writer = csv.writer(logf)
        if not log_exists:
            writer.writerow(["variant", "size", "height", "filletRadius", "holeDia"])
        writer.writerow([generated + 1, size, height, filletRadius, holeDia])

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
            f"(Size={size}, Height={height}, FilletRadius={filletRadius}, HoleDia={holeDia})"
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