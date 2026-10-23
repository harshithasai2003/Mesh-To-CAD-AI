import os
import random
import subprocess
import csv
import time

FREECADCMD = r"C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe"
MASTER = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\11_master.py"
OUTPUT = r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING\THIRD SEMESTER\MODELLING SEMINAR B\Variants\11_Variants"
NUM_VARIANTS = 100
TIMEOUT_SEC = 45
MAX_TOTAL_ATTEMPTS = 150

os.makedirs(OUTPUT, exist_ok=True)

if not os.path.exists(FREECADCMD):
    raise SystemExit(f"FREECADCMD not found at: {FREECADCMD}")
if not os.path.exists(MASTER):
    raise SystemExit(f"MASTER not found at: {MASTER}")


def unhide(path):
    if os.name == "nt":
        subprocess.run(["attrib", "-h", "-s", path], shell=True)


def kill_process_tree(pid):
    subprocess.run(["taskkill", "/F", "/T", "/PID", str(pid)], capture_output=True)


with open(MASTER, "r", encoding="utf-8") as f:
    master = f.read()

generated = 0
attempt = 0

while generated < NUM_VARIANTS and attempt < MAX_TOTAL_ATTEMPTS:
    attempt += 1
    print(f"Generating Variant {generated + 1} (Attempt {attempt})", flush=True)

    PAD_LEN = random.randint(10, 35)
    HOLE_DIA = round(random.uniform(10, 18), 2)

    fcstd = os.path.join(OUTPUT, f"11_{generated + 1:03d}.FCStd")
    stl = os.path.join(OUTPUT, f"11_{generated + 1:03d}.stl")
    pyfile = os.path.join(OUTPUT, f"11_{generated + 1:03d}.py")

    script = master
    script = script.replace("__PAD_LEN__", str(PAD_LEN))
    script = script.replace("__HOLE_DIA__", str(HOLE_DIA))
    script = script.replace("FCSTD_FILE", 'r"%s"' % fcstd.replace("\\", "/"))
    script = script.replace("STL_FILE", 'r"%s"' % stl.replace("\\", "/"))

    with open(pyfile, "w", encoding="utf-8") as f:
        f.write(script)

    log_path = os.path.join(OUTPUT, "variant_log.csv")
    log_exists = os.path.exists(log_path)
    with open(log_path, "a", newline="") as logf:
        writer = csv.writer(logf)
        if not log_exists:
            writer.writerow(["variant", "PAD_LEN", "HOLE_DIA"])
        writer.writerow([generated + 1, PAD_LEN, HOLE_DIA])

    start = time.time()
    proc = subprocess.Popen(
        [FREECADCMD, pyfile],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )

    try:
        stdout, stderr = proc.communicate(timeout=TIMEOUT_SEC)
        returncode = proc.returncode
    except subprocess.TimeoutExpired:
        print(f"\u2717 TIMED OUT after {TIMEOUT_SEC}s — killing process tree (PID {proc.pid})")
        kill_process_tree(proc.pid)
        time.sleep(1)
        continue

    elapsed = round(time.time() - start, 1)

    if returncode == 0 and os.path.exists(fcstd) and os.path.exists(stl):
        unhide(fcstd)
        unhide(stl)
        unhide(pyfile)
        print(f"\u2713 Variant {generated + 1} created in {elapsed}s")
        generated += 1
    else:
        print(f"\u2717 Failed (return code {returncode}, took {elapsed}s)")
        if stdout:
            print("---- stdout ----\n", stdout)
        if stderr:
            print("---- stderr ----\n", stderr)

if generated < NUM_VARIANTS:
    print(f"Stopped after {attempt} attempts — {generated}/{NUM_VARIANTS} succeeded.")
else:
    print("Finished generating all variants.")