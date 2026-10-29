# eval/

`eval/v<n>.md` is the scoring report of version `n`, written by the scoring session (stage 5). It opens with the summary,
the only part the coordinating session reads; the per-case outputs come after it. The shape, with an example:

```markdown
# Eval v1

## Summary

- n: 20
- met: 18
- not met: 2
- ruled real: 3
- ruled false: 1
- thresholds: met at least 17 of n, and no output that does what the assistant must never do
- score: 90% (n=20)
- verdict: pass

## Cases
```

- `n`: the test cases scored; `met` plus `not met` is `n`.
- `ruled real` and `ruled false`: outputs outside the key that a domain expert ruled on; a real one counts in `met`, a false
  one in `not met`.
- `thresholds`: the spec's thresholds, as frozen at its approval; `verdict`: `pass` when they hold, else `fail`.
- Any other item may follow, one line `- key: value`, the key in lower-case ASCII words with no space before its colon; a
  percentage carries its own `n=` on the same line, a threshold's too: one `n=` per percentage (`met at least 85% (n=20)`),
  never `n=0`.
- Nothing else inside the summary: no heading, fence, quote, HTML tag or control character; at most 60 lines and 4,096 bytes.

Under `## Cases`: one `###` section per case: the case, the output, met or not, and for an output outside the key the
expert's ruling (who, when, real or false).
