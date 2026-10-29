# cases/

- `dev/`: the cases the build works on.
- `test-v<n>/`: the test cases of version `n` and their expected results (the key). A separate session makes them after
  the tag `v<n>`, from `inputs/` alone; the domain experts review the key against the inputs before scoring. The age check
  proves the test set is younger than the tag. When version `n + 1` starts, the used test set moves to `dev/`.

The case shape is the one the spec states.
