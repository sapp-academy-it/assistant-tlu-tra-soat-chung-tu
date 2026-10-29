# The spec of an AI Assistant: the skeleton of stage 2

Copy these sections into the spec of this assistant (`kb/specs/`), fill each one, and have the owner approve it before the
build starts. The scoring thresholds freeze at that approval, before any test case exists. Name people by their role.

## The process

The business process the assistant serves, in the customer's own terms: who uses it, what they give it, what they get back,
and which decision stays with a person.

## What the assistant does

Each task, as a sentence a user would recognise, with the documents in `inputs/` it relies on.

## What the assistant must never do

Each limit, as a sentence a reviewer can check against an output (for example: decide in a person's place, invent a rule the
documents do not hold). A test case may target one; an output that breaks one is never met.

## The inputs

Where the customer's documents come from and who sends them; the files in `inputs/` and what each one is.

## The case shape

One case: the input the assistant gets, and its expected result (the key), with the source of that result in `inputs/`.
Where a case lives (`cases/dev/`, `cases/test-v<n>/`) and how a file is named.

## The scoring thresholds

When an output meets its expected result, and the thresholds a version must hold to pass, each with its `n`: a percentage
is written with its own `n` beside it, one `n` per percentage (`met at least 85% (n=20)`), never `n=0`; the scoring report
copies them as written.

## The domain experts

The people who know this business process (the customer's or ours), by role: who signs off the key of each test set against
the inputs, who rules on an output outside the key, and how each sign-off and ruling is recorded.

## Known limits

What the assistant does not cover, for the handover PDF.
