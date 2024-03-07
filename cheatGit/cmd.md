- Set your global Git username:

    `git config --global user:name "firstname lastname"`

- Set your global Git user email:

    `git config --global user:email "valid-email"`

---

- Initialize a new Git repository in the current directory:

    `git init`

- Clone a repository into a new directory:

    `git clone [url]`

- Show the working directory status:

    `git status`

- Add a file to the staging area:

    `git add [file]`

- Unstage a file:

    `git reset [file]`

- Revert the file to its last commit state:

    `git checkout -- [file]`

- Show changes between working directory and staging area:

    `git diff`

- Show changes between staging area and the last commit:

    `git diff --staged`

- Commit staged changes with a descriptive message:

    `git commit -m "descriptive message"`

- Add a new remote repository:

    `git remote add [alias] [url]`

- Fetch changes from a remote repositor:

    `git fetch [alias]`

- Merge changes from a remote branch into the current branch:

    `git merge [alias]/[branch]`

- Push local branch changes to a remote repository:

    `git push [alias] [branch]`

- Fetch and merge changes from the remote branch into the current branch:

    `git pull`

***Note: git pull is equivalent to a combination of git fetch and git merge commands.***

- Ignore files and directories:

The following samples should be written to the .gitignore file:
```
logs/
*.notes
pattern*/
```
