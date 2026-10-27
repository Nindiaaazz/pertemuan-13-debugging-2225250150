
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from praktik.praktik_4_debugging import (
    hitung_rata_rata,
    status,
    nilai_tertinggi
)

test_cases = [
    ("T1 Rata-rata 4 nilai",
     hitung_rata_rata([80, 60, 90, 70]), 75.0),

    ("T2 Rata-rata 2 nilai",
     hitung_rata_rata([100, 80]), 90.0),

    ("T3 Status nilai 60",
     status(60), "Lulus"),

    ("T4 Status nilai 59",
     status(59), "Tidak lulus"),

    ("T5 Nilai tertinggi",
     nilai_tertinggi([80, 60, 90, 70]), 90),
]

for nama, aktual, harapan in test_cases:
    hasil = "PASS" if aktual == harapan else "FAIL"
    print(f"{nama}: {hasil} (aktual={aktual}, harapan={harapan})")
