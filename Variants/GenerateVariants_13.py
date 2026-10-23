import os
import random
import subprocess
import csv

FREECADCMD = r"C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe"
MASTER = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\13_master.py"
OUTPUT = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\13_Variants"
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

    cyl_dia = random.randint(20, 100)         # cylinder outer diameter
    cyl_len = random.randint(10, 60)          # total cylinder length (symmetric pad)

    
    groove_x = cyl_dia / 2.0

    
    max_groove_r = min(cyl_len / 2.0 - 1.0, cyl_dia * 0.4 / 2.0)
    if max_groove_r < 1.0:
        continue
    groove_r = round(random.uniform(1.0, max_groove_r), 2)

    fcstd  = os.path.join(OUTPUT, f"13_{generated + 1:03d}.FCStd")
    stl    = os.path.join(OUTPUT, f"13_{generated + 1:03d}.stl")
    pyfile = os.path.join(OUTPUT, f"13_{generated + 1:03d}.py")

    script = master
    script = script.replace("__CYL_DIA__",  str(cyl_dia))
    script = script.replace("__CYL_LEN__",  str(cyl_len))
    script = script.replace("__GROOVE_X__", str(groove_x))
    script = script.replace("__GROOVE_R__", str(groove_r))
    script = script.replace("FCSTD_FILE", 'r"%s"' % fcstd.replace("\\", "/"))
    script = script.replace("STL_FILE",   'r"%s"' % stl.replace("\\", "/"))

    with open(pyfile, "w", encoding="utf-8") as f:
        f.write(script)

    log_path = os.path.join(OUTPUT, "variant_log_13.csv")
    log_exists = os.path.exists(log_path)
    with open(log_path, "a", newline="") as logf:
        writer = csv.writer(logf)
        if not log_exists:
            writer.writerow(["variant", "cyl_dia", "cyl_len", "groove_x", "groove_r"])
        writer.writerow([generated + 1, cyl_dia, cyl_len, groove_x, groove_r])

    result = subprocess.run([FREECADCMD, pyfile], capture_output=True, text=True)

    if result.returncode == 0 and os.path.exists(fcstd) and os.path.exists(stl):
        unhide(fcstd); unhide(stl); unhide(pyfile)
        print(f"\u2713 Variant {generated + 1} (CylDia={cyl_dia}, CylLen={cyl_len}, "
              f"GrooveX={groove_x}, GrooveR={groove_r})")
        generated += 1
    else:
        print(f"\u2717 Failed (return code {result.returncode})")
        if result.stdout: print("---- stdout ----\n", result.stdout)
        if result.stderr: print("---- stderr ----\n", result.stderr)
        print("Trying another combination...\n")

print("Finished generating all variants.")