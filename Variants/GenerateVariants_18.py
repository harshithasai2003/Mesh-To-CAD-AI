import os
import random
import subprocess
import csv

# EDIT THESE TWO PATHS FOR YOUR MACHINE
FREECADCMD = r"C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe"

MASTER = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\18_master.py"

OUTPUT = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\18_Variants"

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

    base_size = random.randint(60, 200)         # base square edge length
    base_height = random.randint(5, 30)          # tier 1 (square) height
    diamond_height = random.randint(5, 30)       # tier 2 (diamond) height
    top_height = random.randint(5, 30)           # tier 3 (small square) height

    fcstd = os.path.join(OUTPUT, f"18_{generated + 1:03d}.FCStd")
    stl = os.path.join(OUTPUT, f"18_{generated + 1:03d}.stl")
    pyfile = os.path.join(OUTPUT, f"18_{generated + 1:03d}.py")

    script = master
    script = script.replace("__BASE_SIZE__", str(base_size))
    script = script.replace("__BASE_HEIGHT__", str(base_height))
    script = script.replace("__DIAMOND_HEIGHT__", str(diamond_height))
    script = script.replace("__TOP_HEIGHT__", str(top_height))
    script = script.replace("FCSTD_FILE", 'r"%s"' % fcstd.replace("\\", "/"))
    script = script.replace("STL_FILE", 'r"%s"' % stl.replace("\\", "/"))

    with open(pyfile, "w", encoding="utf-8") as f:
        f.write(script)

    log_path = os.path.join(OUTPUT, "variant_log_18.csv")
    log_exists = os.path.exists(log_path)
    with open(log_path, "a", newline="") as logf:
        writer = csv.writer(logf)
        if not log_exists:
            writer.writerow([
                "variant", "base_size", "base_height", "diamond_height", "top_height",
            ])
        writer.writerow([
            generated + 1, base_size, base_height, diamond_height, top_height,
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
            f"(BaseSize={base_size}, BaseH={base_height}, "
            f"DiamondH={diamond_height}, TopH={top_height})"
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