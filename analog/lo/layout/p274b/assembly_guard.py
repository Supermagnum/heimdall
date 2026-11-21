#!/usr/bin/env python3
"""Parent-vs-child + no-parent-M1 guard for P2.7.4b assemblers [HAND].

Rules (VCO island join + latch notes):
- Parent metal must not run through a child cell (face stubs only).
- No parent M1 straps: parent M1 is only short stubs onto a child face pin
  or tiny via/device landings (≤ M1_STUB_MAX). Call check() before writing GDS.
"""
from __future__ import annotations


FACE_ALLOW = 0.55  # µm — pin pad inset + via landing [HAND]
M1_STUB_MAX = 2.50  # µm — longest allowed parent M1 edge [HAND]


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
    from_w = x1 - child_bb.left
    from_e = child_bb.right - x0
    from_s = y1 - child_bb.bottom
    from_n = child_bb.top - y0
    return min(from_w, from_e, from_s, from_n)


def touches_child_face(shape_bb, child_bb, face_allow=FACE_ALLOW):
    """True if shape only kisses a child face (penetration ≤ face_allow)."""
    d = penetration_depth(shape_bb, child_bb)
    return 0.0 < d <= face_allow or (
        _overlap(shape_bb, child_bb) is not None and d <= face_allow)


class ParentChildGuard:
    """Track child bboxes; refuse invasion and long parent M1."""

    def __init__(self, face_allow=FACE_ALLOW, m1_stub_max=M1_STUB_MAX):
        self.face_allow = float(face_allow)
        self.m1_stub_max = float(m1_stub_max)
        self.children = []  # (name, bbox)
        self.parent_boxes = []  # (tag, bbox, layer_name)
        self.parent_insts = []
        self.forbid_parent_m1 = True

    def add_child(self, name, bb):
        self.children.append((name, bb))

    def _check_child_overlap(self, tag, bb, allow_face=True):
        limit = self.face_allow if allow_face else 0.01
        for cname, cbb in self.children:
            d = penetration_depth(bb, cbb)
            if d > limit:
                raise RuntimeError(
                    f"parent shape '{tag}' overlaps child '{cname}' "
                    f"by {d:.3f} µm (> {limit:.3f}); "
                    f"shape={bb} child={cbb}")

    def _check_m1_stub(self, tag, bb):
        """Parent M1 must be a short stub (≤ m1_stub_max on longest edge)."""
        if not self.forbid_parent_m1:
            return
        w = bb.right - bb.left
        h = bb.top - bb.bottom
        longest = max(w, h)
        if longest <= self.m1_stub_max + 1e-9:
            return
        # Long M1 only allowed if it is exclusively a face strip on one child
        # (should not happen — face stubs are short). Fail closed.
        raise RuntimeError(
            f"parent M1 '{tag}' too long ({longest:.3f} µm > "
            f"{self.m1_stub_max:.3f}); no parent M1 straps "
            f"[VCO island rule]. shape={bb}")

    def add_parent_box(self, tag, bb, allow_face=True, layer=""):
        self._check_child_overlap(tag, bb, allow_face=allow_face)
        lname = (layer or "").upper()
        if lname in ("M1", "METAL1", "8/0", "8,0"):
            self._check_m1_stub(tag, bb)
        self.parent_boxes.append((tag, bb, layer))

    def add_parent_inst(self, tag, bb, allow_face=False):
        self.add_parent_box(tag, bb, allow_face=allow_face)
        self.parent_insts.append((tag, bb))

    def check_top_shapes(self, top_cell, layers, tag_prefix="top"):
        """layers: list of (layer_index, name) e.g. (m1, 'M1')."""
        dbu = top_cell.layout().dbu
        for layer, lname in layers:
            for s in top_cell.shapes(layer).each():
                if not s.is_box():
                    continue
                bb = s.bbox().to_dtype(dbu)
                self.add_parent_box(
                    f"{tag_prefix}:{lname}", bb, allow_face=True, layer=lname)

    def summary(self):
        return (
            f"children={len(self.children)} "
            f"parent_boxes={len(self.parent_boxes)} "
            f"parent_insts={len(self.parent_insts)} "
            f"face_allow={self.face_allow} "
            f"m1_stub_max={self.m1_stub_max} "
            f"forbid_parent_m1={self.forbid_parent_m1}"
        )
