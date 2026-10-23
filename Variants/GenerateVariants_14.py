import os
import random
import subprocess
import csv

FREECADCMD = r"C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe"
MASTER = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\14_master.py"
OUTPUT = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\14_Variants"
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

    size  = random.randint(10, 35)            # square full side length
    pad_h = random.randint(3, 15)             # block thickness
    x_offset = round(size * 0.3917, 2)
    y_offset = round(size * 0.3083, 2)
    delta_x  = round(2 * x_offset, 2)        # setDatum(9)
    delta_y  = round(2 * y_offset, 2)        # setDatum(4)

    max_hole_dia = round(size * 0.20, 2)
    if max_hole_dia < 0.5:
        continue
    hole_dia = round(random.uniform(0.3, max_hole_dia), 2)

    fcstd  = os.path.join(OUTPUT, f"14_{generated + 1:03d}.FCStd")
    stl    = os.path.join(OUTPUT, f"14_{generated + 1:03d}.stl")
    pyfile = os.path.join(OUTPUT, f"14_{generated + 1:03d}.py")

    script = master
    script = script.replace("__SIZE__",     str(size))
    script = script.replace("__PAD_H__",    str(pad_h))
    script = script.replace("__HOLE_DIA__", str(hole_dia))
    script = script.replace("__DELTA_Y__",  str(delta_y))
    script = script.replace("__DELTA_X__",  str(delta_x))
    script = script.replace("__X_OFFSET__", str(x_offset))
    script = script.replace("__Y_OFFSET__", str(y_offset))
    script = script.replace("FCSTD_FILE", 'r"%s"' % fcstd.replace("\\", "/"))
    script = script.replace("STL_FILE",   'r"%s"' % stl.replace("\\", "/"))

    with open(pyfile, "w", encoding="utf-8") as f:
        f.write(script)

    log_path = os.path.join(OUTPUT, "variant_log_14.csv")
    log_exists = os.path.exists(log_path)
    with open(log_path, "a", newline="") as logf:
        writer = csv.writer(logf)
        if not log_exists:
            writer.writerow(["variant","size","pad_h","hole_dia",
                             "x_offset","y_offset","delta_x","delta_y"])
        writer.writerow([generated+1, size, pad_h, hole_dia,
                         x_offset, y_offset, delta_x, delta_y])

    result = subprocess.run([FREECADCMD, pyfile], capture_output=True, text=True)

    if result.returncode == 0 and os.path.exists(fcstd) and os.path.exists(stl):
        unhide(fcstd); unhide(stl); unhide(pyfile)
        print(f"\u2713 Variant {generated+1} (Size={size}, PadH={pad_h}, "
              f"HoleDia={hole_dia}, XOff={x_offset}, YOff={y_offset})")
        generated += 1
    else:
        print(f"\u2717 Failed (return code {result.returncode})")
        if result.stdout: print("---- stdout ----\n", result.stdout)
        if result.stderr: print("---- stderr ----\n", result.stderr)
        print("Trying another combination...\n")

print("Finished generating all variants.")