# Rules of this repo

Rule files that the `vibemaestro-sdlc` plugin delivers next to its own rules. This directory is listed in `rules.dirs` of
`.vibemaestro/sdlc.json`; the plugin reads it on every edit and every shell command.

A rule is `<name>.instructions.md`: a short frontmatter, then the text of the reminder.

- `applyTo: "<glob>,<glob>"`: reminded when a file that matches is edited.
- `applyWhen: "<regex>"`: reminded when a shell command that matches is about to run.
- `description:` one line shown in the rule catalogue. `level: block` makes a command rule stop the command.
- `status:` anything but `active` (the default) means the rule is not delivered, which is how `example.instructions.md` stays quiet.

A file with the same name as a plugin rule replaces it; `rules.disable` in the config turns a plugin rule off. Keep a rule short and
state the order, not the history: a reminder that is long gets skimmed.
