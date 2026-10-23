import os
import random
import subprocess
import csv

FREECADCMD = r"C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe"
MASTER = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\12_master.py"
OUTPUT = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\12_Variants"
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

    outer_dia = random.randint(40, 120)      # cylinder outer diameter

    
    pad_h = random.randint(15, 50)

    
    groove_outer = random.randint(int(outer_dia * 0.55), int(outer_dia * 0.88))
    groove_inner = random.randint(int(outer_dia * 0.30), groove_outer - 5)

    
    max_depth = max(5, pad_h // 2 - 2)
    groove_depth = random.randint(3, max_depth)

    fcstd = os.path.join(OUTPUT, f"12_{generated + 1:03d}.FCStd")
    stl   = os.path.join(OUTPUT, f"12_{generated + 1:03d}.stl")
    pyfile = os.path.join(OUTPUT, f"12_{generated + 1:03d}.py")

    script = master
    script = script.replace("__OUTER_DIA__",    str(outer_dia))
    script = script.replace("__PAD_H__",        str(pad_h))
    script = script.replace("__GROOVE_OUTER__", str(groove_outer))
    script = script.replace("__GROOVE_INNER__", str(groove_inner))
    script = script.replace("__GROOVE_DEPTH__", str(groove_depth))
    script = script.replace("FCSTD_FILE", 'r"%s"' % fcstd.replace("\\", "/"))
    script = script.replace("STL_FILE",   'r"%s"' % stl.replace("\\", "/"))

    with open(pyfile, "w", encoding="utf-8") as f:
        f.write(script)

    log_path = os.path.join(OUTPUT, "variant_log_12.csv")
    log_exists = os.path.exists(log_path)
    with open(log_path, "a", newline="") as logf:
        writer = csv.writer(logf)
        if not log_exists:
            writer.writerow(["variant","outer_dia","pad_h","groove_outer","groove_inner","groove_depth"])
        writer.writerow([generated+1, outer_dia, pad_h, groove_outer, groove_inner, groove_depth])

    result = subprocess.run([FREECADCMD, pyfile], capture_output=True, text=True)

    if result.returncode == 0 and os.path.exists(fcstd) and os.path.exists(stl):
        unhide(fcstd); unhide(stl); unhide(pyfile)
        print(f"\u2713 Variant {generated+1} (OuterDia={outer_dia}, PadH={pad_h}, "
              f"GrooveOuter={groove_outer}, GrooveInner={groove_inner}, GrooveDepth={groove_depth})")
        generated += 1
    else:
        print(f"\u2717 Failed (return code {result.returncode})")
        if result.stdout: print("---- stdout ----\n", result.stdout)
        if result.stderr: print("---- stderr ----\n", result.stderr)
        print("Trying another combination...\n")

print("Finished generating all variants.")