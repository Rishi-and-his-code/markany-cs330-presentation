#!/usr/bin/env python3
"""Extract high-res MarkAny SRS diagrams from CS330_SRS_Group_7.pdf into assets/diagrams/."""
from __future__ import annotations

import io
from pathlib import Path

import pymupdf as fitz
from PIL import Image
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "CS330_SRS_Group_7.pdf"
OUT = ROOT / "assets" / "diagrams"

TARGETS = [
    (11, "fig_2_1_architecture.png", "architecture"),
    (29, "fig_b1_use_case.png", "usecase"),
    (31, "fig_b2_dfd_level0.png", "native"),
    (32, "fig_b3_dfd_level1.png", "native"),
    (33, "fig_b4_seq_live.png", "native"),
    (34, "fig_b5_seq_liveness.png", "native"),
    (35, "fig_b6_act_session.png", "native"),
    (36, "fig_b7_act_liveness.png", "native"),
    (37, "fig_b8_erd.png", "native"),
]


def trim_whitespace(img: Image.Image, thresh: int = 248, pad: int = 10) -> Image.Image:
    g = np.array(img.convert("L"))
    ink = g < thresh
    rows = np.where(ink.mean(axis=1) > 0.002)[0]
    cols = np.where(ink.mean(axis=0) > 0.002)[0]
    if len(rows) == 0 or len(cols) == 0:
        return img
    return img.crop(
        (
            max(0, int(cols[0]) - pad),
            max(0, int(rows[0]) - pad),
            min(img.width, int(cols[-1]) + pad),
            min(img.height, int(rows[-1]) + pad),
        )
    )


def crop_dark_diagram(img: Image.Image, pad: int = 6) -> Image.Image:
    arr = np.array(img)
    dark = arr.mean(axis=2) < 90
    row_dark = dark.mean(axis=1)
    col_dark = dark.mean(axis=0)
    rows = np.where(row_dark > 0.02)[0]
    cols = np.where(col_dark > 0.02)[0]
    if len(rows) == 0 or len(cols) == 0:
        return trim_whitespace(img)
    bands = []
    start = prev = int(rows[0])
    for r in rows[1:]:
        r = int(r)
        if r - prev > 20:
            bands.append((start, prev))
            start = r
        prev = r
    bands.append((start, prev))
    best = max(bands, key=lambda b: b[1] - b[0])
    return img.crop(
        (
            max(0, int(cols[0]) - pad),
            max(0, best[0] - pad),
            min(img.width, int(cols[-1]) + pad),
            min(img.height, best[1] + pad),
        )
    )


def largest_native(doc: fitz.Document, page: fitz.Page):
    best = None
    best_area = 0
    for info in page.get_images(full=True):
        xref = info[0]
        try:
            meta = doc.extract_image(xref)
        except Exception:
            continue
        area = meta["width"] * meta["height"]
        if area < 50_000:
            continue
        if area > best_area:
            best_area = area
            best = (xref, meta)
    return best


def extract_native(doc: fitz.Document, page: fitz.Page) -> Image.Image:
    pair = largest_native(doc, page)
    if not pair:
        raise RuntimeError("No embedded image on page")
    _, meta = pair
    return Image.open(io.BytesIO(meta["image"])).convert("RGB")


def extract_page_clip(page: fitz.Page, dpi: int = 300) -> Image.Image:
    info = page.get_images(full=True)[0]
    rect = page.get_image_rects(info[0])[0]
    rect = fitz.Rect(rect) & page.rect
    mat = fitz.Matrix(dpi / 72.0, dpi / 72.0)
    pix = page.get_pixmap(matrix=mat, clip=rect, alpha=False)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF)
    print(f"PDF pages: {doc.page_count}")
    for page_idx, fname, mode in TARGETS:
        page = doc[page_idx]
        if mode == "architecture":
            img = crop_dark_diagram(extract_page_clip(page, 300))
        elif mode == "usecase":
            img = trim_whitespace(extract_page_clip(page, 300))
        else:
            img = trim_whitespace(extract_native(doc, page))
        out = OUT / fname
        img.save(out, "PNG", optimize=True)
        blank = img.convert("L").getextrema()[0] == img.convert("L").getextrema()[1]
        print(
            f"{fname}: {img.size[0]}x{img.size[1]} "
            f"aspect={img.size[0]/img.size[1]:.3f} "
            f"bytes={out.stat().st_size} blank={blank} mode={mode}"
        )


if __name__ == "__main__":
    main()
