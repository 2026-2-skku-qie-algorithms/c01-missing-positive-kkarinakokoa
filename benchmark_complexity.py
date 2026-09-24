"""Measure scaling and write CSV/SVG artifacts using the standard library only.

Run: python benchmark_complexity.py
Input allocation is excluded. Timing and memory are measured separately.
This experiment illustrates scaling; it does not prove an asymptotic bound.
"""

import csv
from pathlib import Path
from statistics import median
from time import perf_counter
import tracemalloc

from smallest_missing_positive import smallest_missing_positive


SIZES = (1_000, 5_000, 10_000, 20_000, 40_000, 60_000, 80_000, 100_000)
REPEATS = 7
CALLS_PER_SAMPLE = 5


def measure_time(values):
    smallest_missing_positive(values)  # Warm up before collecting samples.
    samples = []
    for _ in range(REPEATS):
        start = perf_counter()
        for _ in range(CALLS_PER_SAMPLE):
            result = smallest_missing_positive(values)
        elapsed = (perf_counter() - start) / CALLS_PER_SAMPLE
        assert result == len(values) + 1
        samples.append(elapsed * 1000)
    return median(samples), min(samples), max(samples)


def measure_space(values):
    tracemalloc.start()
    try:
        result = smallest_missing_positive(values)
        _, peak = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()
    assert result == len(values) + 1
    return peak


def collect_measurements():
    rows = []
    for size in SIZES:
        values = list(range(1, size + 1))
        elapsed, low, high = measure_time(values)
        peak = measure_space(values)
        rows.append((size, elapsed, low, high, peak))
        print(f"n={size:>6}: {elapsed:8.3f} ms, peak={peak / 1024:8.1f} KiB")
    return rows


def draw_panel(rows, x_offset, column, divisor, title, unit):
    left, top, width, height = x_offset + 75, 135, 440, 295
    maximum_x = rows[-1][0]
    values = [row[column] / divisor for row in rows]
    scale = values[-1] / maximum_x
    maximum_y = max(values) * 1.2
    if column == 1:
        maximum_y = max(row[3] for row in rows) * 1.2

    def point(size, value):
        return left + width * size / maximum_x, top + height * (1 - value / maximum_y)

    parts = [f'<text x="{left}" y="105" class="title">{title}</text>']
    for tick in range(6):
        fraction = tick / 5
        y = top + height * (1 - fraction)
        x = left + width * fraction
        parts.append(f'<path d="M {left} {y} h {width}" class="grid"/>')
        parts.append(f'<text x="{left - 10}" y="{y + 4}" text-anchor="end">{maximum_y * fraction:.1f}</text>')
        parts.append(f'<text x="{x}" y="{top + height + 25}" text-anchor="middle">{maximum_x * fraction / 1000:.0f}k</text>')
    parts.append(f'<text x="{left}" y="{top - 12}">{unit}</text>')
    parts.append(f'<text x="{left + width / 2}" y="{top + height + 52}" text-anchor="middle">Input length n</text>')
    start = point(0, 0)
    end = point(maximum_x, scale * maximum_x)
    parts.append(f'<line x1="{start[0]}" y1="{start[1]}" x2="{end[0]}" y2="{end[1]}" stroke="#d97706" stroke-width="2" stroke-dasharray="7 5"/>')
    coordinates = [point(row[0], value) for row, value in zip(rows, values)]
    joined = " ".join(f"{x:.2f},{y:.2f}" for x, y in coordinates)
    parts.append(f'<polyline points="{joined}" fill="none" stroke="#2563eb" stroke-width="2.5"/>')
    for row, (x, y) in zip(rows, coordinates):
        if column == 1:
            low_y = point(row[0], row[2])[1]
            high_y = point(row[0], row[3])[1]
            parts.append(f'<line x1="{x}" y1="{low_y}" x2="{x}" y2="{high_y}" stroke="#93c5fd" stroke-width="3"/>')
        parts.append(f'<circle cx="{x}" cy="{y}" r="4" fill="#2563eb"><title>n={row[0]}, value={row[column] / divisor:.3f} {unit}</title></circle>')
    return "\n".join(parts)


def write_graph(rows, path):
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1160" height="640" viewBox="0 0 1160 640">',
        '<rect width="1160" height="640" fill="white"/>',
        '<style>text{font-family:Arial,sans-serif;font-size:13px;fill:#334155}.title{font-size:19px;font-weight:bold}.grid{stroke:#e2e8f0;stroke-width:1}</style>',
        '<text x="35" y="38" class="title">Smallest missing positive: measured scaling</text>',
        '<text x="35" y="65">Input: [1, 2, ..., n]. Input creation excluded. Standard-library measurements.</text>',
        draw_panel(rows, 0, 1, 1, "Execution time", "ms"),
        draw_panel(rows, 575, 4, 1024, "Peak extra Python memory", "KiB"),
        '<text x="75" y="510" fill="#2563eb">Blue: measurements (time whiskers: min to max of 7 batch averages).</text>',
        '<text x="75" y="535">Dashed orange: c * n, scaled to the final measurement; a reference, not a fitted proof.</text>',
        '<text x="75" y="560">Time: median of 7 samples, 5 calls each; tracemalloc disabled during timing.</text>',
        '<text x="75" y="585">Memory: tracemalloc peak during one call; set capacity growth can produce steps.</text>',
        '<text x="75" y="610">Expected O(n) time assumes ordinary integer costs and expected constant-time set operations.</text>',
        '</svg>',
    ]
    path.write_text("\n".join(parts), encoding="utf-8")


def main():
    rows = collect_measurements()
    output_directory = Path(__file__).resolve().parent
    csv_path = output_directory / "complexity_measurements.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(("n", "median_ms", "min_ms", "max_ms", "peak_extra_bytes"))
        writer.writerows(rows)
    graph_path = output_directory / "complexity_graph.svg"
    write_graph(rows, graph_path)
    print(f"Saved {csv_path.name} and {graph_path.name}")


if __name__ == "__main__":
    main()
