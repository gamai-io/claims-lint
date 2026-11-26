# Security policy — claims-lint

## Reporting

E-mail **renato@gamatrade.ba** with the subject `[claims-lint-security]`. Please include the
version or commit, a minimal reproduction, and what an attacker gains. Do not open a
public issue for something exploitable before it is fixed.

There is no bug bounty and no guaranteed response time. Expect an acknowledgement if the
report is actionable.

## Scope

`claims_lint.py` is a linter: it reads Markdown and prints findings. The obvious
attack surface is a repository that points CI at this file over the network
(`raw.githubusercontent.com` without a pin), so pin the commit if you depend on it.

## What this project does and does not promise

It is open-source software provided as-is. There is no warranty, no service-level
agreement and no claim that it is free of defects. Reports are read on a best-effort
basis; a fix is not guaranteed.
