Before working on this branch, include your previous work from steps 1 and 2 (which have been merged to the main branch) in your branch:

```bash
git checkout main
git pull
git checkout 3/use_prefect
git rebase main
```

The goal of this PR is to:

- [ ] Use the prefect library to adapt the code developed in the PR2 to use `flow` and `task` objects

Files to be modified: the `src/modelling` folder

- [ ] Don't forget to update the `requirements.in` file with the new dependencies (and compile it to generate the `requirements.txt` file)
- [ ] Don't forget to update the `README.md` file with the new steps to reproduce to run the code
- [ ] You should among other add instructions to run the prefect UI and visualize the flow runs

___

*TODO: delete this markdown file before merging the pull request*
