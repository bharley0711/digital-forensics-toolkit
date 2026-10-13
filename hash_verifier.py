"""
Hash verifier for forensic evidence handling.

Computes the MD5, SHA-1, and SHA-256 hashes of a file in a single pass and,
optionally, compares the SHA-256 against an expected value - the check an
examiner runs when acquiring or re-verifying an evidence image to confirm
it has not changed since collection.

Usage:
    python hash_verifier.py <file>
    python hash_verifier.py <file> --expected-sha256 <hex digest>

Exit code is 0 when no expected hash is given or the hashes match,
and 1 on a mismatch or a file error, so the tool can be scripted.
"""

import argparse
import hashlib
import sys

CHUNK_SIZE = 1024 * 1024  # 1 MiB - evidence images can be huge; never
                           # load a whole file into memory.


def hash_file(path):
    """Return (md5, sha1, sha256) hex digests for the file at path."""
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(CHUNK_SIZE):
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)
    return md5.hexdigest(), sha1.hexdigest(), sha256.hexdigest()


def main():
    parser = argparse.ArgumentParser(
        description="Compute and verify file hashes for evidence handling.")
    parser.add_argument("file", help="path to the file to hash")
    parser.add_argument("--expected-sha256",
                        help="expected SHA-256 hex digest to verify against")
    args = parser.parse_args()

    try:
        md5, sha1, sha256 = hash_file(args.file)
    except OSError as e:
        print(f"Error: cannot read {args.file}: {e}", file=sys.stderr)
        return 1

    print(f"File   : {args.file}")
    print(f"MD5    : {md5}")
    print(f"SHA-1  : {sha1}")
    print(f"SHA-256: {sha256}")

    if args.expected_sha256:
        expected = args.expected_sha256.strip().lower()
        if sha256 == expected:
            print("Verify : MATCH - SHA-256 equals the expected value")
            return 0
        print("Verify : MISMATCH - file does NOT match the expected SHA-256")
        print(f"         expected {expected}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
