#!/usr/bin/env python3
"""Parent-vs-child overlap guard for P2.7.4b assemblers [HAND].

Rule (latch / layout-notes): parent metal must not run through a child cell.
Gap stubs may touch a child face (pin pad inset) but must not penetrate the
bbox interior beyond FACE_ALLOW. Call check() before writing GDS.
"""
from __future__ import annotations


# Pin pad half-width in pin_face.HALF is 0.25; allow a little margin for
# via landings that land on the face [HAND].
FACE_ALLOW = 0.55  # µm


def _overlap(a, b):
    x0 = max(a.left, b.left)
    y0 = max(a.bottom, b.bottom)
    x1 = min(a.right, b.right)
    y1 = min(a.top, b.top)
    if x1 <= x0 or y1 <= y0:
        return None
    return (x0, y0, x1, y1)


def penetration_depth(shape_bb, child_bb):
    """How far shape_bb reaches into child_bb past the nearest face (µm)."""
    ov = _overlap(shape_bb, child_bb)
    if ov is None:
        return 0.0
    x0, y0, x1, y1 = ov
    # Depth from each face of the child into the overlap
    from_w = x1 - child_bb.left
    from_e = child_bb.right - x0
    from_s = y1 - child_bb.bottom
    from_n = child_bb.top - y0
    # The stub is "face-only" if the overlap is a strip along one face whose
    # inward depth is the minimum of the four; that depth is the penetration.
    return min(from_w, from_e, from_s, from_n)


class ParentChildGuard:
    """Track child instance bboxes; refuse parent shapes that invade them."""

    def __init__(self, face_allow=FACE_ALLOW):
        self.face_allow = float(face_allow)
        self.children = []  # (name, bbox dtype)
        self.parent_boxes = []  # (tag, bbox)
        self.parent_insts = []  # (tag, bbox)

    def add_child(self, name, bb):
        self.children.append((name, bb))

    def add_parent_box(self, tag, bb, allow_face=True):
        limit = self.face_allow if allow_face else 0.01
        for cname, cbb in self.children:
            d = penetration_depth(bb, cbb)
            if d > limit:
                raise RuntimeError(
                    f"parent shape '{tag}' overlaps child '{cname}' "
                    f"by {d:.3f} µm (> {limit:.3f}); "
                    f"shape={bb} child={cbb}")
        self.parent_boxes.append((tag, bb))

    def add_parent_inst(self, tag, bb, allow_face=False):
        """PCells / vias placed by the parent — no intrusion into children."""
        self.add_parent_box(tag, bb, allow_face=allow_face)
        self.parent_insts.append((tag, bb))

    def check_top_shapes(self, top_cell, layers, tag_prefix="top"):
        """Scan shapes already on top (e.g. after pin helpers) [TOOL]."""
        for layer, lname in layers:
            for s in top_cell.shapes(layer).each():
                if not s.is_box():
                    continue
                bb = s.bbox().to_dtype(top_cell.layout().dbu)
                self.add_parent_box(f"{tag_prefix}:{lname}", bb, allow_face=True)

    def summary(self):
        return (
            f"children={len(self.children)} "
            f"parent_boxes={len(self.parent_boxes)} "
            f"parent_insts={len(self.parent_insts)} "
            f"face_allow={self.face_allow}"
        )
