import os
import random
import subprocess
import csv

FREECADCMD = r"C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe"
MASTER = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\6_master.py"

OUTPUT = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\6_Variants"

NUM_VARIANTS = 100
TIMEOUT_SEC = 60
MAX_TOTAL_ATTEMPTS = 150

os.makedirs(OUTPUT, exist_ok=True)


def unhide(path):
    if os.name == "nt":
        subprocess.run(["attrib", "-h", "-s", path], shell=True)


with open(MASTER, "r", encoding="utf-8") as f:
    master = f.read()

generated = 0
attempt = 0

while generated < NUM_VARIANTS and attempt < MAX_TOTAL_ATTEMPTS:
    attempt += 1
    print(f"Generating Variant {generated + 1} (Attempt {attempt})", flush=True)

    W = random.randint(80, 150)
    H = random.randint(35, 70)
    BASE_THICK = random.randint(15, 35)

    CUTOUT_CX = round(W / 2, 2)
    max_r = (W / 2) - 15
    CUTOUT_R = round(random.uniform(10, max(11, min(max_r, 30))), 2)
    CUTOUT_X_LEFT = round(CUTOUT_CX - CUTOUT_R, 2)
    CUTOUT_X_RIGHT = round(CUTOUT_CX + CUTOUT_R, 2)

    PIN_R = round(random.uniform(3, 6), 2)
    PIN_X_LEFT = round(W * 0.15, 2)
    PIN_X_RIGHT = round(W * 0.85, 2)
    PIN_Y = round(BASE_THICK / 2, 2)
    PIN_HEIGHT = random.randint(20, 40)

    fcstd = os.path.join(OUTPUT, f"6_{generated + 1:03d}.FCStd")
    stl = os.path.join(OUTPUT, f"6_{generated + 1:03d}.stl")
    pyfile = os.path.join(OUTPUT, f"6_{generated + 1:03d}.py")

    script = master
    script = script.replace("__W__", str(W))
    script = script.replace("__H__", str(H))
    script = script.replace("__CUTOUT_CX__", str(CUTOUT_CX))
    script = script.replace("__CUTOUT_R__", str(CUTOUT_R))
    script = script.replace("__CUTOUT_X_LEFT__", str(CUTOUT_X_LEFT))
    script = script.replace("__CUTOUT_X_RIGHT__", str(CUTOUT_X_RIGHT))
    script = script.replace("__BASE_THICK__", str(BASE_THICK))
    script = script.replace("__PIN_R__", str(PIN_R))
    script = script.replace("__PIN_X_LEFT__", str(PIN_X_LEFT))
    script = script.replace("__PIN_X_RIGHT__", str(PIN_X_RIGHT))
    script = script.replace("__PIN_Y__", str(PIN_Y))
    script = script.replace("__PIN_HEIGHT__", str(PIN_HEIGHT))
    script = script.replace("FCSTD_FILE", 'r"%s"' % fcstd.replace("\\", "/"))
    script = script.replace("STL_FILE", 'r"%s"' % stl.replace("\\", "/"))

    with open(pyfile, "w", encoding="utf-8") as f:
        f.write(script)

    log_path = os.path.join(OUTPUT, "variant_log.csv")
    log_exists = os.path.exists(log_path)
    with open(log_path, "a", newline="") as logf:
        writer = csv.writer(logf)
        if not log_exists:
            writer.writerow([
                "variant", "W", "H", "CUTOUT_CX", "CUTOUT_R", "BASE_THICK",
                "PIN_R", "PIN_X_LEFT", "PIN_X_RIGHT", "PIN_Y", "PIN_HEIGHT"
            ])
        writer.writerow([
            generated + 1, W, H, CUTOUT_CX, CUTOUT_R, BASE_THICK,
            PIN_R, PIN_X_LEFT, PIN_X_RIGHT, PIN_Y, PIN_HEIGHT
        ])

    try:
        result = subprocess.run(
            [FREECADCMD, pyfile],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SEC,
        )
    except subprocess.TimeoutExpired:
        print(f"\u2717 TIMED OUT after {TIMEOUT_SEC}s — skipping.\n")
        continue

    if result.returncode == 0 and os.path.exists(fcstd) and os.path.exists(stl):
        unhide(fcstd)
        unhide(stl)
        unhide(pyfile)
        print(f"\u2713 Variant {generated + 1} created (W={W}, H={H}, CUTOUT_R={CUTOUT_R})")
        generated += 1
    else:
        print(f"\u2717 Failed (return code {result.returncode})")
        if result.stdout:
            print("---- stdout ----\n", result.stdout)
        if result.stderr:
            print("---- stderr ----\n", result.stderr)
        print("Trying another random combination...\n")

if generated < NUM_VARIANTS:
    print(f"Stopped after {attempt} attempts — {generated}/{NUM_VARIANTS} succeeded.")
else:
    print("Finished generating all variants.")
    