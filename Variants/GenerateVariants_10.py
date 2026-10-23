import os
import random
import math
import subprocess
import csv

FREECADCMD = r"C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe"
MASTER = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\10_master.py"
OUTPUT = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\10_Variants"
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

    hex_r = random.randint(15, 50)          # circumradius of hexagon

   
    pad_h = random.randint(10, 40)

    inscribed_r = hex_r * math.sqrt(3) / 2.0
    max_hole_dia = max(6, int(inscribed_r * 1.6))  # generous -- hole can overlap flats
    hole_dia = random.randint(6, min(max_hole_dia, int(hex_r * 1.8)))

    fcstd = os.path.join(OUTPUT, f"10_{generated + 1:03d}.FCStd")
    stl   = os.path.join(OUTPUT, f"10_{generated + 1:03d}.stl")
    pyfile = os.path.join(OUTPUT, f"10_{generated + 1:03d}.py")

    script = master
    script = script.replace("__HEX_R__",   str(hex_r))
    script = script.replace("__PAD_H__",   str(pad_h))
    script = script.replace("__HOLE_DIA__", str(hole_dia))
    script = script.replace("FCSTD_FILE", 'r"%s"' % fcstd.replace("\\", "/"))
    script = script.replace("STL_FILE",   'r"%s"' % stl.replace("\\", "/"))

    with open(pyfile, "w", encoding="utf-8") as f:
        f.write(script)

    log_path = os.path.join(OUTPUT, "variant_log_10.csv")
    log_exists = os.path.exists(log_path)
    with open(log_path, "a", newline="") as logf:
        writer = csv.writer(logf)
        if not log_exists:
            writer.writerow(["variant","hex_r","pad_h","hole_dia"])
        writer.writerow([generated+1, hex_r, pad_h, hole_dia])

    result = subprocess.run([FREECADCMD, pyfile], capture_output=True, text=True)

    if result.returncode == 0 and os.path.exists(fcstd) and os.path.exists(stl):
        unhide(fcstd); unhide(stl); unhide(pyfile)
        print(f"\u2713 Variant {generated+1} (HexR={hex_r}, PadH={pad_h}, HoleDia={hole_dia})")
        generated += 1
    else:
        print(f"\u2717 Failed (return code {result.returncode})")
        if result.stdout: print("---- stdout ----\n", result.stdout)
        if result.stderr: print("---- stderr ----\n", result.stderr)
        print("Trying another combination...\n")

print("Finished generating all variants.")