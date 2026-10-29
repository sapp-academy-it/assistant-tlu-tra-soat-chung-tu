# dist/

The outputs of version `n`, made by the packaging (stage 6) from the tag `v<n>`:

- `<name>-v<n>-skill.zip`: one top-level folder named as the skill; each staff member adds it in their own Claude
  (Customize > Skills, with code execution on);
- `<name>-v<n>-plugin.zip`: the same skill wrapped as a plugin, which the customer's Team or Enterprise admin provisions to
  everyone;
- the handover PDF: what the assistant does and must never do, how to install it each way, this version's score with its
  `n`, its known limits, and that a person stays accountable for each decision.

A zip of a version is written once; building it again gives the same bytes.
