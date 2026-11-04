"""Download, verify, and unpack the immutable PDU supplement (standard library only)."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import tarfile
import urllib.request


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True, help='New output directory')
    args = parser.parse_args()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=False)
    manifest = json.loads(Path(__file__).with_name('downloads.json').read_text())
    archives = []
    for item in manifest['archives']:
        dest = out / item['file']
        print('Downloading', dest.name, flush=True)
        request = urllib.request.Request(item['url'], headers={'User-Agent': 'AxionLimitBench-reproduce/0.1.2'})
        with urllib.request.urlopen(request, timeout=120) as src, dest.open('wb') as dst:
            shutil.copyfileobj(src, dst)
        digest = hashlib.sha256(dest.read_bytes()).hexdigest()
        if digest != item['sha256'] or dest.stat().st_size != item['bytes']:
            raise ValueError(f'Integrity check failed: {dest.name}')
        archives.append(dest)
    for archive in archives:
        with tarfile.open(archive, 'r:gz') as tf:
            members = tf.getmembers()
            for member in members:
                target = (out / member.name).resolve()
                if not member.isfile() or not target.is_relative_to(out) or target.exists():
                    raise ValueError(f'Unsafe or duplicate archive member: {member.name}')
            for member in members:
                target = out / member.name
                target.parent.mkdir(parents=True, exist_ok=True)
                with tf.extractfile(member) as src, target.open('xb') as dst:
                    shutil.copyfileobj(src, dst)
    package = out / 'pdu-revision-2026-11-04'
    for line in (package / 'MANIFEST.sha256').read_text().splitlines():
        expected, name = line.split('  ', 1)
        target = (package / name).resolve()
        if not target.is_relative_to(package) or hashlib.sha256(target.read_bytes()).hexdigest() != expected:
            raise ValueError(f'Package checksum failed: {name}')
    print('Verified package:', package)
    print('Follow README.md to reproduce the saved analyses without model calls.')


if __name__ == '__main__':
    main()
