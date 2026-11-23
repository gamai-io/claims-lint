# claims-lint

A number in a README is a promise. This linter flags measured figures (`%`, `ms`, `pass rate`,
`n=`, `x faster`) that have **no reproducer, date or N** within ±4 lines.

```bash
python3 claims_lint.py README.md            # report only
python3 claims_lint.py README.md --strict   # exit 1 on findings
```

Use it in CI **non-strict at first** (report), then strict once the backlog is clean. It is a
reminder, not a proof: a line can still cite a command that does not work.

CI snippet:

```yaml
- run: |
    curl -fsSL https://raw.githubusercontent.com/gamai-io/claims-lint/main/claims_lint.py -o /tmp/cl.py
    python3 /tmp/cl.py README.md
```

Apache-2.0.
