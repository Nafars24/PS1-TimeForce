#!/usr/bin/env python3
"""
patch_biglump.py - apply the Indonesian translation to BIGLUMP.BIN
(Power Rangers: Time Force, PS1).

Usage:
    python patch_biglump.py BIGLUMP.BIN biglump_strings_ID.csv BIGLUMP_ID.BIN [--force]

The input file is never modified. The output has exactly the same size as the
input; only bytes inside the three English string tables (entries 0, 1 and 3)
are changed. Each translation is written at the start of its original slot and
the rest of the slot is zero-filled, so the offset tables stay valid.

The script aborts (and writes nothing) if:
  * the input hash does not match the supported version (override: --force)
  * a CSV row does not match the original English string
  * a translation is longer than the original string
  * newline count, printf placeholders or button glyphs differ from the original
  * a translation contains non-ASCII characters
"""
import csv
import hashlib
import re
import struct
import sys

EXPECTED_SIZE = 28647424
EXPECTED_SHA256 = "add7cdad91e45ed2eef2ea90c86a2d5a6195c12b81c4591f5dbc6e5ad88d4b32"
TOC_ENTRIES = 251
TEXT_ENTRIES = (0, 1, 3)   # identical English string tables
STRING_COUNT = 611
GLYPHS = "{}|~"            # controller button icons
PLACEHOLDER = re.compile(r"%[0-9]*[ds]")


def fail(msg):
    sys.exit("error: " + msg)


def read_toc(data):
    toc = [struct.unpack_from("<II", data, i * 8) for i in range(TOC_ENTRIES)]
    for off, size in toc:
        if off % 0x800 or off + size > len(data):
            fail("unexpected archive layout (bad TOC entry)")
    return toc


def read_table(entry):
    count = struct.unpack_from("<I", entry, 0)[0]
    if count != STRING_COUNT:
        fail("string table has %d entries, expected %d" % (count, STRING_COUNT))
    offs = list(struct.unpack_from("<%dI" % count, entry, 4))
    strings = []
    for o in offs:
        end = entry.index(b"\0", o)
        strings.append(entry[o:end])
    return offs, strings


def load_csv(path):
    rows = {}
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            idx = int(r["idx"])
            rows[idx] = (r["english"].replace("\\n", "\n"),
                         r["indonesia"].replace("\\n", "\n"))
    return rows


def validate(rows, original):
    errors = []
    for idx, (eng, tr) in sorted(rows.items()):
        if not 0 <= idx < STRING_COUNT:
            errors.append("idx %d: out of range" % idx)
            continue
        orig = original[idx].decode("latin-1")
        if eng != orig:
            errors.append("idx %d: 'english' column does not match the game text" % idx)
            continue
        try:
            tr.encode("ascii")
        except UnicodeEncodeError:
            errors.append("idx %d: non-ASCII character in translation" % idx)
            continue
        if len(tr) > len(orig):
            errors.append("idx %d: too long (%d > %d): %r" % (idx, len(tr), len(orig), tr))
        if tr.count("\n") != orig.count("\n"):
            errors.append("idx %d: newline count differs" % idx)
        if PLACEHOLDER.findall(tr) != PLACEHOLDER.findall(orig):
            errors.append("idx %d: printf placeholders differ" % idx)
        for g in GLYPHS:
            if tr.count(g) != orig.count(g):
                errors.append("idx %d: button glyph %r count differs" % (idx, g))
    return errors


def main(argv):
    force = "--force" in argv
    args = [a for a in argv if a != "--force"]
    if len(args) != 3:
        sys.exit(__doc__)
    src, csv_path, dst = args

    data = bytearray(open(src, "rb").read())
    sha = hashlib.sha256(data).hexdigest()
    if len(data) != EXPECTED_SIZE or sha != EXPECTED_SHA256:
        msg = ("input does not match the supported BIGLUMP.BIN\n"
               "  size   : %d (expected %d)\n  sha256 : %s\n  expected: %s"
               % (len(data), EXPECTED_SIZE, sha, EXPECTED_SHA256))
        if not force:
            fail(msg + "\nuse --force to try anyway (untested versions may break)")
        print("warning: " + msg)

    toc = read_toc(data)
    tables = {}
    for k in TEXT_ENTRIES:
        off, size = toc[k]
        tables[k] = read_table(bytes(data[off:off + size]))
    ref_offs, ref_strings = tables[TEXT_ENTRIES[0]]
    for k in TEXT_ENTRIES[1:]:
        if tables[k][0] != ref_offs or tables[k][1] != ref_strings:
            fail("string table copies differ; unsupported version")

    rows = load_csv(csv_path)
    errors = validate(rows, ref_strings)
    if errors:
        print("\n".join(errors[:50]))
        fail("%d problem(s) in %s, nothing written" % (len(errors), csv_path))

    changed = 0
    for idx, (eng, tr) in rows.items():
        if tr == eng:
            continue
        changed += 1
        slot = len(ref_strings[idx]) + 1          # string + null terminator
        new = tr.encode("ascii") + b"\0" * (slot - len(tr))
        for k in TEXT_ENTRIES:
            start = toc[k][0] + ref_offs[idx]
            data[start:start + slot] = new

    assert len(data) == EXPECTED_SIZE or force
    with open(dst, "wb") as f:
        f.write(data)
    print("patched %d strings in %d tables" % (changed, len(TEXT_ENTRIES)))
    print("output : %s (%d bytes)" % (dst, len(data)))
    print("sha256 : %s" % hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main(sys.argv[1:])
