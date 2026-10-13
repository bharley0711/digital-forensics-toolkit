# Digital Forensics Toolkit

Small, dependency-free utilities and templates from my digital forensics
training — the unglamorous parts of evidence handling that have to be right
every time.

> Everything here is generic training material. It contains no data,
> images, or details from any real examination or employer matter.

## Contents

### `hash_verifier.py`

Computes MD5, SHA-1, and SHA-256 hashes of a file in a single streaming
pass (1 MiB chunks, so it handles full disk images without loading them
into memory) and optionally verifies the file against an expected SHA-256 —
the integrity check run at acquisition and at every evidence transfer.

```bash
python hash_verifier.py evidence_image.E01
python hash_verifier.py evidence_image.E01 --expected-sha256 <digest>
```

Example output:

```
File   : sample.txt
MD5    : 61f5b7a732652f873e2500e4ce71a4a7
SHA-1  : d3ff0f8cc6b037953598172a982df809b7a68d1f
SHA-256: 862823e714ed7c278bae14e6869c9b3e21436582a90ae42b72754d4f2b8bb218
Verify : MATCH - SHA-256 equals the expected value
```

The exit code is 0 on a match (or when no expected hash is supplied) and 1
on a mismatch or file error, so the tool can sit inside a larger acquisition
script and fail loudly instead of silently passing bad evidence.

### `chain_of_custody_template.md`

A one-form-per-item chain of custody template: item and collection details,
acquisition hash recording, storage, a running transfer log, and final
disposition. Written the way I was trained to document collections —
contemporaneous, one entry per transfer, hash re-verification noted at each
hand-off.

## Why these two live together

A hash is only as good as the paperwork around it. The verifier produces the
integrity values; the custody form is where they get recorded, who handled
the item, and when. If the two ever disagree, the discrepancy — not the
evidence — becomes the story, which is exactly what both pieces are designed
to prevent.

## Next additions

- A companion script that walks a folder of evidence images and writes the
  results to a verification log (CSV) for the case file.
- Examination notes template (analysis log) to sit alongside the custody
  form.
