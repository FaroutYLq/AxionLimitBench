# PDU revised evaluation and repeatability supplement

This supplement adds pointwise-agreement rates with bootstrap intervals, revised
coverage and joint-success analyses, outcome audits,
figure/table scripts, and the 100-paper Fable 5 agent repeatability study to
AxionLimitBench. The original benchmark scorer and leaderboard remain unchanged.

## Download and reproduce

Run `python download.py --out /path/to/new-directory` from this directory.
It downloads both archives from an immutable Hugging Face revision, verifies
their SHA-256 checksums, and extracts the complete reproduction package.
Python 3.10 or newer is required. No credentials or model access are needed.

Then follow [the package instructions](PACKAGE_README.md) to install dependencies
and run `reproduce.py` from the extracted `pdu-revision-2026-11-04/` directory.
See [release notes](RELEASE_NOTES.md) for scope and validation.

The `source/` directory mirrors the supplement's analysis and figure scripts
for review in GitHub. Run the extracted package, which also contains the frozen
inputs and required directory layout. Full transcripts are distributed as
archives rather than committed to Git history.

## Files

- [pdu-revision-2026-11-04-analysis.tar.gz](https://huggingface.co/datasets/FaroutYLq/AxionLimitBench/resolve/e53872f03aae77735cc1071eef7d63b041972741/supplements/pdu-revision-2026-11-04-v0.1.3/pdu-revision-2026-11-04-analysis.tar.gz) (66,122,410 bytes)
- [pdu-revision-2026-11-04-transcripts.tar.gz](https://huggingface.co/datasets/FaroutYLq/AxionLimitBench/resolve/e53872f03aae77735cc1071eef7d63b041972741/supplements/pdu-revision-2026-11-04-v0.1.3/pdu-revision-2026-11-04-transcripts.tar.gz) (70,664,854 bytes)

Hugging Face revision: `e53872f03aae77735cc1071eef7d63b041972741`. Checksums are in `SHA256SUMS`.
