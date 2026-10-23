import os
import random
import subprocess
import csv
import time


# ============================================================
# PATHS

FREECADCMD = r"C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe"

MASTER = (
    r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING"
    r"\THIRD SEMESTER\MODELLING SEMINAR B\Variants\1_master.py"
)

OUTPUT = (
    r"C:\Users\harsh\OneDrive\Desktop\SCIENTIFIC COMPUTING"
    r"\THIRD SEMESTER\MODELLING SEMINAR B\Variants\1_Variants"
)

NUM_VARIANTS = 100

MAX_ATTEMPTS = NUM_VARIANTS * 20

FREECAD_TIMEOUT = 120


# ============================================================
# CHECK PATHS
# ============================================================

if not os.path.isfile(FREECADCMD):
    raise FileNotFoundError(
        f"FreeCAD executable not found:\n{FREECADCMD}"
    )

if not os.path.isfile(MASTER):
    raise FileNotFoundError(
        f"Master script not found:\n{MASTER}"
    )

os.makedirs(OUTPUT, exist_ok=True)


# ============================================================
# READ MASTER SCRIPT
# ============================================================

with open(MASTER, "r", encoding="utf-8") as f:
    master = f.read()


# ============================================================
# REQUIRED PLACEHOLDERS
# ============================================================

required_placeholders = [
    "__H__",
    "__W_SHELF__",
    "__H_INNER__",
    "__PAD_W__",
    "__FILLET_R__",
    "__FILLET2_R__",
    "__HOLE_DIA1__",
    "__HOLE_DIA2__",
    "__HOLE_X1__",
    "__HOLE_Y1__",
    "__HOLE_X3__",
    "__HOLE_Y3__",
    "FCSTD_FILE",
    "STL_FILE",
]

missing = [
    p for p in required_placeholders
    if p not in master
]

if missing:
    raise RuntimeError(
        "Missing placeholders in 1_master.py:\n"
        + "\n".join(missing)
    )


# ============================================================
# CSV
# ============================================================

log_path = os.path.join(
    OUTPUT,
    "variant_log.csv"
)

csv_header = [
    "variant",
    "H",
    "W_SHELF",
    "H_INNER",
    "PAD_W",
    "FILLET_R",
    "FILLET2_R",
    "HOLE_DIA1",
    "HOLE_DIA2",
    "HOLE_X1",
    "HOLE_Y1",
    "HOLE_X3",
    "HOLE_Y3",
]


# Start a clean CSV so it always corresponds to this run.
with open(
    log_path,
    "w",
    encoding="utf-8",
    newline=""
) as f:

    writer = csv.writer(f)
    writer.writerow(csv_header)


# ============================================================
# HELPERS
# ============================================================

def unhide(path):

    if os.name == "nt" and os.path.exists(path):

        try:
            subprocess.run(
                ["attrib", "-h", "-s", path],
                shell=True,
                capture_output=True,
                text=True
            )
        except Exception:
            pass


def delete_file(path):

    try:
        if os.path.exists(path):
            os.remove(path)
    except Exception:
        pass


def valid_file(path):

    return (
        os.path.isfile(path)
        and os.path.getsize(path) > 0
    )


def generate_parameters():

    # --------------------------------------------------------
    # MAIN DIMENSIONS
    # --------------------------------------------------------

    H = random.randint(60, 150)

    W_SHELF = random.randint(
        8,
        max(9, H // 5)
    )

    H_INNER = H - W_SHELF

    PAD_W = random.randint(20, 100)


    # --------------------------------------------------------
    # HOLE DIAMETERS
    # --------------------------------------------------------

    max_dia = min(
        5.0,
        W_SHELF * 0.60
    )

    if max_dia < 4.0:
        return None

    HOLE_DIA1 = round(
        random.uniform(
            4.0,
            max_dia
        ),
        2
    )

    HOLE_DIA2 = round(
        random.uniform(
            4.0,
            max_dia
        ),
        2
    )


    # --------------------------------------------------------
    # VERTICAL-ARM HOLE OFFSET
    # --------------------------------------------------------

    margin1 = max(
        HOLE_DIA1 / 2.0 + 3.0,
        5.0
    )

    min_offset1 = margin1

    max_offset1 = (
        PAD_W / 2.0
        - margin1
    )

    if max_offset1 < min_offset1:
        return None

    HOLE_X1 = round(
        random.uniform(
            min_offset1,
            max_offset1
        ),
        2
    )


    # --------------------------------------------------------
    # HORIZONTAL-ARM HOLE OFFSET
    # --------------------------------------------------------

    margin2 = max(
        HOLE_DIA2 / 2.0 + 3.0,
        5.0
    )

    min_offset2 = margin2

    max_offset2 = (
        PAD_W / 2.0
        - margin2
    )

    if max_offset2 < min_offset2:
        return None

    HOLE_Y3 = round(
        random.uniform(
            min_offset2,
            max_offset2
        ),
        2
    )


    # --------------------------------------------------------
    # HOLE POSITION ALONG ARMS
    # --------------------------------------------------------

    HOLE_Y1 = round(
        random.uniform(
            H * 0.55,
            H * 0.90
        ),
        2
    )

    HOLE_X3 = round(
        random.uniform(
            H * 0.55,
            H * 0.90
        ),
        2
    )


    # --------------------------------------------------------
    # FILLET RADII
    # --------------------------------------------------------

    max_fillet1 = min(
        W_SHELF * 0.30,
        PAD_W * 0.20
    )

    max_fillet2 = min(
        W_SHELF * 0.25,
        PAD_W * 0.15
    )

    if max_fillet1 <= 1.0:
        return None

    if max_fillet2 <= 1.0:
        return None

    FILLET_R = round(
        random.uniform(
            1.0,
            max_fillet1
        ),
        2
    )

    FILLET2_R = round(
        random.uniform(
            1.0,
            max_fillet2
        ),
        2
    )


    # --------------------------------------------------------
    # FINAL GEOMETRIC VALIDATION
    # --------------------------------------------------------

    if H_INNER <= 0:
        return None

    if W_SHELF >= H:
        return None

    if HOLE_DIA1 >= W_SHELF:
        return None

    if HOLE_DIA2 >= W_SHELF:
        return None

    if FILLET_R >= W_SHELF / 2.0:
        return None

    if FILLET2_R >= W_SHELF / 2.0:
        return None

    if (
        HOLE_X1
        + HOLE_DIA1 / 2.0
        >= PAD_W / 2.0
    ):
        return None

    if (
        HOLE_Y3
        + HOLE_DIA2 / 2.0
        >= PAD_W / 2.0
    ):
        return None


    return {
        "H": H,
        "W_SHELF": W_SHELF,
        "H_INNER": H_INNER,
        "PAD_W": PAD_W,
        "FILLET_R": FILLET_R,
        "FILLET2_R": FILLET2_R,
        "HOLE_DIA1": HOLE_DIA1,
        "HOLE_DIA2": HOLE_DIA2,
        "HOLE_X1": HOLE_X1,
        "HOLE_Y1": HOLE_Y1,
        "HOLE_X3": HOLE_X3,
        "HOLE_Y3": HOLE_Y3,
    }


def build_script(parameters, fcstd, stl):

    script = master

    replacements = {
        "__H__": parameters["H"],
        "__W_SHELF__": parameters["W_SHELF"],
        "__H_INNER__": parameters["H_INNER"],
        "__PAD_W__": parameters["PAD_W"],
        "__FILLET_R__": parameters["FILLET_R"],
        "__FILLET2_R__": parameters["FILLET2_R"],
        "__HOLE_DIA1__": parameters["HOLE_DIA1"],
        "__HOLE_DIA2__": parameters["HOLE_DIA2"],
        "__HOLE_X1__": parameters["HOLE_X1"],
        "__HOLE_Y1__": parameters["HOLE_Y1"],
        "__HOLE_X3__": parameters["HOLE_X3"],
        "__HOLE_Y3__": parameters["HOLE_Y3"],
    }

    for placeholder, value in replacements.items():

        script = script.replace(
            placeholder,
            str(value)
        )

    script = script.replace(
        "FCSTD_FILE",
        'r"%s"' % fcstd.replace("\\", "/")
    )

    script = script.replace(
        "STL_FILE",
        'r"%s"' % stl.replace("\\", "/")
    )

    return script


def log_success(
    variant,
    parameters
):

    with open(
        log_path,
        "a",
        encoding="utf-8",
        newline=""
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            variant,
            parameters["H"],
            parameters["W_SHELF"],
            parameters["H_INNER"],
            parameters["PAD_W"],
            parameters["FILLET_R"],
            parameters["FILLET2_R"],
            parameters["HOLE_DIA1"],
            parameters["HOLE_DIA2"],
            parameters["HOLE_X1"],
            parameters["HOLE_Y1"],
            parameters["HOLE_X3"],
            parameters["HOLE_Y3"],
        ])


# ============================================================
# MAIN LOOP
# ============================================================

generated = 0
attempt = 0


print("=" * 70)
print("FREECAD VARIANT GENERATOR")
print("=" * 70)
print(
    f"Target variants: {NUM_VARIANTS}"
)
print(
    f"Output: {OUTPUT}"
)
print("=" * 70)


while generated < NUM_VARIANTS:

    attempt += 1

    if attempt > MAX_ATTEMPTS:

        print()
        print(
            f"ERROR: Maximum attempts ({MAX_ATTEMPTS}) reached."
        )

        print(
            f"Only {generated} of "
            f"{NUM_VARIANTS} variants were generated."
        )

        break


    variant = generated + 1

    print()
    print(
        f"Attempt {attempt} | "
        f"Generating Variant {variant}/{NUM_VARIANTS}"
    )


    # --------------------------------------------------------
    # GENERATE PARAMETERS
    # --------------------------------------------------------

    parameters = generate_parameters()

    if parameters is None:

        print(
            "  Skipped invalid parameter combination."
        )

        continue


    # --------------------------------------------------------
    # FILE PATHS
    # --------------------------------------------------------

    fcstd = os.path.join(
        OUTPUT,
        f"1_{variant:03d}.FCStd"
    )

    stl = os.path.join(
        OUTPUT,
        f"1_{variant:03d}.stl"
    )

    pyfile = os.path.join(
        OUTPUT,
        f"1_{variant:03d}.py"
    )


    # --------------------------------------------------------
    # REMOVE PREVIOUS FILES
    # --------------------------------------------------------

    delete_file(fcstd)
    delete_file(stl)
    delete_file(pyfile)


    # --------------------------------------------------------
    # BUILD GENERATED SCRIPT
    # --------------------------------------------------------

    try:

        script = build_script(
            parameters,
            fcstd,
            stl
        )

        with open(
            pyfile,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(script)

    except Exception as exc:

        print(
            f"  Failed to create Python file: {exc}"
        )

        continue


    # --------------------------------------------------------
    # RUN FREECAD
    # --------------------------------------------------------

    try:

        start = time.time()

        result = subprocess.run(
            [
                FREECADCMD,
                pyfile
            ],
            capture_output=True,
            text=True,
            timeout=FREECAD_TIMEOUT
        )

        elapsed = time.time() - start

        print(
            f"  FreeCAD runtime: {elapsed:.1f} s"
        )

        print(
            f"  Return code: {result.returncode}"
        )


    except subprocess.TimeoutExpired:

        print(
            "  FAILED: FreeCAD timeout."
        )

        delete_file(fcstd)
        delete_file(stl)

        continue


    except Exception as exc:

        print(
            f"  FAILED to start FreeCAD: {exc}"
        )

        delete_file(fcstd)
        delete_file(stl)

        continue


    # --------------------------------------------------------
    # FREECAD ERROR
    # --------------------------------------------------------

    if result.returncode != 0:

        print()
        print(
            "  FREECAD FAILED"
        )

        if result.stdout:

            print(
                "----- STDOUT -----"
            )

            print(
                result.stdout
            )

        if result.stderr:

            print(
                "----- STDERR -----"
            )

            print(
                result.stderr
            )

        print(
            "------------------"
        )


        delete_file(fcstd)
        delete_file(stl)

        # Keep the Python file for debugging.

        failed_py = os.path.join(
            OUTPUT,
            f"_FAILED_attempt_{attempt:04d}.py"
        )

        try:

            os.replace(
                pyfile,
                failed_py
            )

        except Exception:
            pass

        continue


    # --------------------------------------------------------
    # VERIFY OUTPUT
    # --------------------------------------------------------

    if not valid_file(fcstd):

        print(
            "  FAILED: FCStd file missing or empty."
        )

        delete_file(fcstd)
        delete_file(stl)

        continue


    if not valid_file(stl):

        print(
            "  FAILED: STL file missing or empty."
        )

        delete_file(fcstd)
        delete_file(stl)

        continue


    # --------------------------------------------------------
    # SUCCESS
    # --------------------------------------------------------

    unhide(fcstd)
    unhide(stl)
    unhide(pyfile)


    # IMPORTANT:
    # Only now increment generated.
    generated += 1


    # Only successful variants are written to CSV.

    log_success(
        generated,
        parameters
    )


    print()
    print(
        f"  SUCCESS: Variant "
        f"{generated}/{NUM_VARIANTS}"
    )

    print(
        f"  H={parameters['H']}"
    )

    print(
        f"  W_SHELF={parameters['W_SHELF']}"
    )

    print(
        f"  H_INNER={parameters['H_INNER']}"
    )

    print(
        f"  PAD_W={parameters['PAD_W']}"
    )

    print(
        f"  FILLET_R={parameters['FILLET_R']}"
    )

    print(
        f"  FILLET2_R={parameters['FILLET2_R']}"
    )

    print(
        f"  HOLE_DIA1={parameters['HOLE_DIA1']}"
    )

    print(
        f"  HOLE_DIA2={parameters['HOLE_DIA2']}"
    )

    print(
        f"  HOLE_X1={parameters['HOLE_X1']}"
    )

    print(
        f"  HOLE_Y1={parameters['HOLE_Y1']}"
    )

    print(
        f"  HOLE_X3={parameters['HOLE_X3']}"
    )

    print(
        f"  HOLE_Y3={parameters['HOLE_Y3']}"
    )


# ============================================================
# FINAL MESSAGE
# ============================================================

print()
print("=" * 70)
print("GENERATION FINISHED")
print("=" * 70)

print(
    f"Generated: {generated}/{NUM_VARIANTS}"
)

print(
    f"Attempts: {attempt}"
)

print(
    f"CSV: {log_path}"
)

print(
    f"Output: {OUTPUT}"
)

print("=" * 70)

if generated == NUM_VARIANTS:

    print(
        "ALL 100 VARIANTS GENERATED SUCCESSFULLY."
    )

else:

    print(
        "WARNING: Not all variants were generated."
    )