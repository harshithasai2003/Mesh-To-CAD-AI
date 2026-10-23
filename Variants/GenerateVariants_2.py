import os
import random
import subprocess
import csv

# EDIT THESE TWO PATHS
FREECADCMD = r"C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe"

MASTER = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\2_master.py"

OUTPUT = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants"

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

   
    outer = random.randint(80, 200)
    boss = random.randint(40, outer - 15)     
    hole = random.randint(20, boss - 15)      
    body = random.randint(50, 150)
    bossHeight = random.randint(10, 40)

    fcstd = os.path.join(OUTPUT, f"2_{generated + 1:03d}.FCStd")
    stl = os.path.join(OUTPUT, f"2_{generated + 1:03d}.stl")
    pyfile = os.path.join(OUTPUT, f"2_{generated + 1:03d}.py")

    script = master
    script = script.replace("__OUTER_DIA__", str(outer))
    script = script.replace("__BODY_HEIGHT__", str(body))
    script = script.replace("__BOSS_DIA__", str(boss))
    script = script.replace("__HOLE_DIA__", str(hole))
    script = script.replace("__BOSS_HEIGHT__", str(bossHeight))
    script = script.replace("FCSTD_FILE", 'r"%s"' % fcstd.replace("\\", "/"))
    script = script.replace("STL_FILE", 'r"%s"' % stl.replace("\\", "/"))

    with open(pyfile, "w", encoding="utf-8") as f:
        f.write(script)

   
    log_path = os.path.join(OUTPUT, "variant_log.csv")
    log_exists = os.path.exists(log_path)
    with open(log_path, "a", newline="") as logf:
        writer = csv.writer(logf)
        if not log_exists:
            writer.writerow(["variant", "outer", "body", "boss", "hole", "bossHeight"])
        writer.writerow([generated + 1, outer, body, boss, hole, bossHeight])

    
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
            f"(Outer={outer}, Body={body}, Boss={boss}, "
            f"Hole={hole}, BossHeight={bossHeight})"
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