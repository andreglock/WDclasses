# BDL 8 - Even MORE git stuff!- `git init` - initializes the current working folder as a git repository
- Init should just be run one time per repository
- `git` commands can be run in subfolders
- Git _only_ tracks files, not directories
- The commit message of the first commit to a repo often is "Initial import", "Initial commit" or something similar
- You can create a repository in GitHub before OR after creating your local project
- To add an existing local git repository (new project for example) to a newly created GH repository, you need to add the GH repository as a _remote_
    - `git remote add origin https://github.com/usernamehere/projectnamehere.git`
- You can see the manual for git commands too! `man git branch`

# BDL The final countdown- Pull Request Review / Code Review example
- New Project Example starting from GitHub
- `git branch` - show a listing of all the branches
- `git branch -v` - show a list of all the branches (verbose, show more information)
- `git commit -m "Improve README"` - create a new commit and give it a commit message at the same time!
- `git log` - Shows the commit history of a repository
- `git diff` - Show the differences between two states in git
    - For example, show the modifications you have done without committing
- `git checkout` - Can do many different things
    - `git checkout [Branchname]` - This one switches the currently active branch
    - `git checkout -b [Branchname]` - This one creates a new branch called "Branchname"
    - `git checkout -- [path_to_file]` - This one reverts the changes you have made to a file
- `git rm` - Remove a file from git
- Conflicts
    - Conflicts happen when a file is modified at the same time in two different places and those changes are merged
    - For example, Kai edits REAMDE.md in GitHub and Joel edits README.md in the local repository and tries to merge the changes
    - What needs to happen is we need to Resolve the Conflict
    - When a conflict happens, you need to:
        1. manually fix the conflicted files
        2. stage (git add) the fixed conflicted files
        3. make a new commit
        4. remember to use git status to help you along