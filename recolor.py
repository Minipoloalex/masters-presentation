from pathlib import Path
import re

from pypdf import PdfReader, PdfWriter
from pypdf.generic import DecodedStreamObject, NameObject


DIR = "figures/results_new/single-envs/highway"

src = Path(f"{DIR}/main.pdf")
out = Path(f"{DIR}/main_orange.pdf")

# Matplotlib viridis yellow used by PPO in the PDF content stream.
# The regex uses \s+ so it still works if the PDF wraps the RGB values across lines.
yellow_pattern = re.compile(
    rb"0\.993248\s+0\.906157\s+0\.143936"
)

def hex_to_pdf_rgb(hex_color: str) -> bytes:
    """
    Convert '#RRGGBB' or 'RRGGBB' to PDF RGB float bytes.

    Example:
        '#E66100' -> b'0.901961 0.380392 0'
    """
    h = hex_color.strip().lstrip("#")

    if len(h) != 6:
        raise ValueError("Expected '#RRGGBB' or 'RRGGBB'")

    r = int(h[0:2], 16) / 255
    g = int(h[2:4], 16) / 255
    b = int(h[4:6], 16) / 255

    def fmt(x):
        return f"{x:.6f}".rstrip("0").rstrip(".")

    return f"{fmt(r)} {fmt(g)} {fmt(b)}".encode("ascii")

rgb_orange = "#FFA500" # "#E66100"
orange = hex_to_pdf_rgb(rgb_orange)

reader = PdfReader(str(src))
writer = PdfWriter()

total_replacements = 0

for page in reader.pages:
    contents = page.get_contents()
    data = contents.get_data()

    data, n = yellow_pattern.subn(orange, data)
    total_replacements += n

    new_stream = DecodedStreamObject()
    new_stream.set_data(data)

    page[NameObject("/Contents")] = new_stream
    writer.add_page(page)

with out.open("wb") as f:
    writer.write(f)

print(f"Wrote {out}")
print(f"Replacements made: {total_replacements}")
