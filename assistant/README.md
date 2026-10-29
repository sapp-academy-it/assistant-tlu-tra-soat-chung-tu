# assistant/

<!-- assistant-procedure:template-placeholder (the packaging check refuses this file: the build replaces it with the skill) -->

The skill, written in the build (stage 3):

- `SKILL.md`, whose frontmatter `name` and `description` stay within Claude's limits (the packaging check names them);
- `scripts/` and `reference/`, as the skill needs;
- `.claude-plugin/plugin.json`, the plugin manifest that wraps the same files: its `name` is the skill's `name`, and it holds
  metadata only.

Every file in this folder ships in the skill zip and the plugin zip: the build replaces this README with the skill.
The tag `v<n>` on the merged build freezes this folder; the zips are made from the tag, never from a working tree.
