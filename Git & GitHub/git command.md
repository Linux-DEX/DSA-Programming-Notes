# Standard Git Command
## git branch
+ __List all branches__:
```bash
git branch --all
```

+ __List which branches include__ a specific _Git commit in their history_:
```bash
git branch --all --contains <commit_hash>
```

+ __Show the name__ of the _current branch_:
```bash
git branch --show-current
```

+ __Create new branch__ based on the _current commit_:
```bash
git branch <branch_name>
```

+ __Create new branch__  based on _specific commit_:
```bash
git branch <branch_name> <commit_hash>
```

+ __Rename a branch__:
```bash
git branch -m <old_branch_name> <new_branch_name>
```

+ __Delete a local branch__:
```bash
git branch -d <branch_name>
```

+ __Delete a remote branch__:
```bash
git push <remote_name> --delete <remote_branch_name>
```

## git init
+ __Initialize a new local repository__:
```bash
git init
```

+ __Initialize a repository__ with the specified name for the _inital branch_:
```bash
git init --initial-branch=<branch_name>
```

+ __Initialize a repository using SHA256 for object hashes__:
```bash
git init --object-format=sha256
```

+ __Initialize a barebones__ repository, suitable for use a _remote over SSH_:
```bash
git init --bare
```

## git merge
+ __Merge a branch__ into your _current branch_:
```bash
git merge <branch_name>
```

+ __Edit the merge message__:
```bash
git merge --edit <branch_name>
```

+ __Merge a branch and create a merge commit__:
```bash
git merge --no-ff <branch_name>
```

+ __Abort a merge in case of conflicts__:
```bash
git merge --abort
```

+ __Merge using a specific strategy__:
```bash
git merge --strategy <strategy> --strategy-option <strategy_option> <branch_name>
```

## git pull
+ __Download changes from default remote repository and merge it__:
```bash
git pull
```

+ __Download changes from default remote repository and use fast-forward__:
```bash
git pull --rebase
```

+ __Download changes from given remote repository and branch, then merge them in to HEAD__:
```bash
git pull <remote_name> <branch_name>
```

## git stash
+ __Stash current changes, except new (_untracked_) files__:
```bash
git stash push -m <optional_stash_message>
```

+ __Stash current changes, including new (_untracked_) files__:
```bash
git stash -u
```

+ __Interactively select parts of changed files for stashing__:
```bash
git stash -p
```

+ __List all stashes (_shows stash name, related branch and message_)__:
```bash
git stash list
```

+ __Show the changes as a patch between the stash__:
```bash
git stash show -p <stash@{0}>
```

+ __Apply a stash (_default is the latest, named stash@{0}_)__:
```bash
git stash apply <optional_stash_name_or_commit>
```

+ __Drop or apply a stash (_default is stash@(0)_) and remove it from the stash list if applying doesn't cause conflicts__:
```bash
git stash pop <optional_stash_name>
```

+ __Drop all stashes__:
```bash
git stash clear
```

## git reset
+ __Unstage everything__:
```bash
git reset
```

+ __Unstage specific file's__:
```bash
git reset <path_to_file1> <path_to_file2> ...
```

+ __Interactively unstage portions of a file__:
```bash
git reset --patch <path_to_file>
```

+ __Undo the last commit, keeping its changes (_and any further uncommitted changes_) in the filesystem__:
```bash
git reset HEAD~
```

+ __Undo the last two commits, adding their changes to the index, i.e. staged for commit__:
```bash
git reset --soft HEAD~2
```

+ __Discard any uncommitted changes, staged or not (_for only unstaged changes, use git checkout_)__:
```bash
git reset --hard
```

+ __Reset the repository to a given commit, discarding committed, staged and uncommitted changes since then__:
```bash
git reset --hard <commit>
```

## git push
+ __Send local changes in the current branch to its default remote counterpart__:
```bash
git push
```

+ __Send changes from a specific local branch to its remote counterpart__:
```bash
git push <remote_name> <local_branch>
```

+ __Send changes from a specific local branch to its remote counterpart, and set the remote one as the default push/pull target of the local one__:
```bash
git push -u <remote_name> <local_branch>
```

+ __Send changes from a specific local branch to a specific remote branch__:
```bash
git push <remote_name> <local_branch>:<remote_branch>
```

+ __Send changes on all local branches to their counterparts in a given remote repository__:
```bash
git push --all <remote_name>
```

+ __Delete a branch in a remote repository__:
```bash
git push <remote_name> --delete <remote_branch>
```

+ __Remove remote branches that don't have a local counterpart__:
```bash
git push --prune <remote_name>
```

+ __Public tags that aren't yet in the remote repository__:
```bash
git push --tags
```

##  git add
+ __Add a file to the index__:
```bash
git add <path_to_file>
```

+ __Add all files (_tracked and untracked_)__:
```bash
git add -A
```

+ __Add all already tracked files__:
```bash
git add .
```

+ __Only add already tracked files__:
```bash
git add -u
```

+ __Also and ignored files__:
```bash
git add -f
```

+ __Interactively stage parts of files__:
```bash
git add -p
```

+ __Interactively stage parts of a given file__:
```bash
git add -p <path_to_file>
```

+ __Interactively stage a file__:
```bash
git add -i
```

## git clone
+ __Clone an existing repository into a new directory (_the default directory is the repository name_)__:
```bash
git clone <remote_repository_location> <path_to_directory>
```

+ __Clone an existing repository and it's submodules__:
```bash
git clone --recursive <remote_repository_location>
```

+ __Clone only the _.git_ directory of an existing repository__:
```bash
git clone --no-checkout <remote_repository_location>
```

+ __Clone a local repository__:
```bash
git clone --local <path_to_local_repository>
```

+ __Clone quietly__:
```bash
git clone --quiet <remote_repository_location>
```

+ __Clone an existing repository only fetching the 10 most recent commits on the default branch (_useful to save time_)__:
```bash
git clone --depth 10 <remote_repository_location>
```

+  __Clone an existing repository only fetching a specific branch__:
```bash
git clone --branch name --single-branch remote_repository_location
```

+ __Clone an existing repository using a specific SSH command__:
```bash
git clone --config core.sshCommand="ssh -i path/to/private_ssh_key" remote_repository_location
```

## git status
 + __Show changed files which are not yet added for commit__:
 ```bash
git status
```

+ __Give output in [s]hort format__:
```bash
git status --short
```

+ __Show the [b]ranch and tracking info__:
```bash
git status --branch
```

+ __Show output in [s]hort format along with [b]ranch info__:
```bash
git status --short --branch
```

+ __Show the number of entries currently stashed away__:
```bash
git status --show-stash
```

+ __Don't show untracked files in the output__:
```bash
git status --untracked-files=no
```

## git push
+ __Send local changes in the current branch to its default remote counterpart__:
```bash
git push
```

+ __Send changes from a specific local branch to its remote counterpart__:
```bash
git push <remote_name> <local_branch>
```

+ __Send changes from a specific local branch to its remote counterpart, and set the remote one as the default push/pull target of the local one__:
```bash
git push -u <remote_name> <local_branch>
```

+ __Send changes from a specific local branch to a specific remote branch__:
```bash
git push <remote_name> <local_branch>:<remote_branch>
```

+ __Send changes on all local branches to their counterparts in a given remote repository__:
```bash
git push --all <remote_name>
```

+ __Delete a branch in a remote repository__:
```bash
git push <remote_name> --delete <remote_branch>
```

+ __Remove remote branches that don't have a local counterpart__:
```bash
git push --prune <remote_name>
```

+ __Publish tags that aren't yet in the remote repository__:
```bash
git push --tags
```

## git diff
+ __Show unstaged changes__:
```bash
git diff
```

+ __Show all uncommitted changes (_including staged ones_)__:
```bash
git diff HEAD
```

+ __Show only staged (_added, but not yet committed_) changes__:
```bash
git diff --staged
```

+ __Show changes from all commits since a given date/time (a date expression, e.g. "1 week 2 days" or an ISO date)__:
```bash
git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'
```

+ __Show only names of changed files since a given commit__:
```bash
git diff --name-only <commit>
```

+ __Output a summary of file creations, renames and mode changes since a given commit__:
```bash
git diff --summary <commit>
```

+ __Compare a single file between two branches or commits__:
```bash
git diff <branch_1>..<branch_2> [--] <path_to_file>
```

+ __Compare different files from the current branch to other branch__:
```bash
git diff <branch>:<path_to_file2> <path_to_file>
```

## git commit
+ __Commit staged files to the repository with a message__:
```bash
git commit --message "message"
```

+ __Commit staged files with a message read from a file__
```bash
git commit --file <path_to_commit_message_file>
```

+ __Auto stage all modified and deleted files and commit with a message__:
```bash
git commit --all --message "message"
```

+ __Commit staged files and sign them with the specified GPG key (_or the one defined in the configuration file if no argument is specified_)__:
```bash
git commit --gpg-sign key_id --message "message"
```

+ __Update the last commit by adding the currently staged changes, changing the commit's hash__:
```bash
git commit --amend
```

+ __Commit only specific (_already staged_) files__:
```bash
git commit <path_to_file1> <path_to_file2>
```

+ __Create a commit, even if there are no staged files__:
```bash
git commit --message "message" --allow-empty
```

## git clean
+ __Delete untracked files__:
```bash
git clean
```

+ __Interactively delete untracked files__:
```bash
git clean -i
```

+ __Show which files would be deleted without actually deleting them__:
```bash
git clean --dry-run
```

+ __Forcefully delete untracked files__:
```bash
git clean -f
```

+ __Forcefully delete untracked directories__:
```bash
git clean -fd
```

+ __Delete untracked files, including excluded files (files ignored in .gitignore and .git/info/exclude)__:
```bash
git clean -x
```

## git rebase
+ __Rebase the current branch on top of another specified branch__:
```bash
git rebase <new_base_branch>
```

+ __Start an interactive rebase, which allows the commits to be reordered, omitted, combined or modified__:
```bash
git rebase -i <target_base_branch_or_commit_hash>
```

+ __Continue a rebase that was interrupted by a merge failure, after editing conflicting files__:
```bash
git rebase --continue
```

+ __Continue a rebase that was paused due to merge conflicts, by skipping the conflicted commit__:
```bash
git rebase --skip
```

+ __Abort a rebase in progress (_e.g. if it is interrupted by a merge conflict_)__:
```bash
git rebase --abort
```

+ __Move part of the current branch onto a new base, providing the old base to start from__:
```bash
git rebase --onto <new_base> <old_base>
```

+ __Reapply the last 5 commits in-place, stopping to allow them to be reordered, omitted, combined or modified__:
```bash
git rebase -i HEAD~5
```

+ __Auto-resolve any conflicts by favoring the working branch version (_theirs keyword has reversed meaning in this case_)__:
```bash
git rebase -X theirs <branch_name>
```

## git checkout
+ __Create and switch to a new branch__:
```bash
git checkout -b <branch_name>
```

+ __Create and switch to a new branch based on a specific reference (_branch, remote/branch, tag are examples of valid references_)__:
```bash
git checkout -b <branch_name> <reference>
```

+ __Switch to an existing local branch__:
```bash
git checkout <branch_name>
```

+ __Switch to the previously checked out branch__:
```bash
git checkout -
```

+ __Switch to an existing remote branch__:
```bash
git checkout --track <remote_name>/<branch_name>
```

+ __Discard all unstaged changes in the current directory (_see git reset for more undo-like commands_)__:
```bash
git checkout .
```

+ __Discard unstaged changes to a given file__:
```bash
git checkout <path_to_file>
```

+ __Replace a file in the current directory with the version of it committed in a given branch__:
```bash
git checkout <branch_name> -- <path_to_file>
```

## git config
+ __List only local configuration entries (_stored in .git/config in the current repository_)__:
```bash
git config --list --local
```

+ __List only global configuration entries (stored in ~/.gitconfig by default or in $XDG_CONFIG_HOME/git/config if such a file exists)__:
```bash
git config --list --global
```

+ __List only system configuration entries (stored in /etc/gitconfig), and show their file location__:
```bash
git config --list --system --show-origin
```

+ __Get the value of a given configuration entry__:
```bash
git config alias.unstage
```

+ __Set the global value of a given configuration entry__:
```bash
git config --global alias.unstage "reset HEAD --"
```

+ __Revert a global configuration entry to its default value__:
```bash
git config --global --unset alias.unstage
```

+ __Edit the Git configuration for the current repository in the default editor__:
```bash
git config --edit
```

+ __Edit the global Git configuration in the default editor__:
```bash
git config --global --edit
```

## git log
+ __Show the sequence of commits starting from the current one, in reverse chronological order of the Git repository in the current working directory__:
```bash
git log
```

+ __Show the history of a particular file or directory, including differences__:
```bash
git log -p <path/to/file_or_directory>
```

+ __Show an overview of which file(s) changed in each commit__:
```bash
git log --stat
```

+ __Show a graph of commits in the current branch using only the first line of each commit message__:
```bash
git log --oneline --graph
```

+ __Show a graph of all commits, tags and branches in the entire repo__:
```bash
git log --oneline --decorate --all --graph
```

+ __Show only commits whose messages include a given string (_case-insensitively_)__:
```bash
git log -i --grep search_string
```

+ __Show the last N commits from a certain author__:
```bash
git log -n number --author=author
```

+ __Show commits between two dates (yyyy-mm-dd)__:
```bash
git log --before="2017-01-29" --after="2017-01-17"
```

## git show
+ __Show information about the latest commit (hash, message, changes, and other metadata)__:
```bash
git show
```

+ __Show information about a given commit__:
```bash
git show <commit>
```

+ __Show information about the commit associated with a given tag__:
```bash
git show tag
```

+ __Show information about the 3rd commit from the HEAD of a branch__:
```bash
git show branch~3
```

+ __Show a commit's message in a single line, suppressing the diff output__:
```bash
git show --oneline -s <commit>
```

+ __Show only statistics (added/removed characters) about the changed files__:
```bash
git show --stat <commit>
```

+ __Show only the list of added, renamed or deleted files__:
```bash
git show --summary <commit>
```

+ __Show the contents of a file as it was at a given revision (e.g. branch, tag or commit)__:
```bash
git show <revision>:<path_to_file>
```

## get fetch
+ __Fetch the latest changes from the default remote upstream repository (if set)__:
```bash
git fetch
```

+ __Fetch new branches from a specific remote upstream repository__:
```bash
git fetch <remote_name>
```

+ __Fetch the latest changes from all remote upstream repositories__:
```bash
git fetch --all
```

+ __Also fetch tags from the remote upstream repository__:
```bash
git fetch --tags
```

+ __Delete local references to remote branches that have been deleted upstream__:
```bash
git fetch --prune
```

## git tag
+ __List all tags__:
```bash
git tag
```

+ __Create a tag with the given name pointing to the current commit__:
```bash
git tag <tag_name>
```

+ __Create a tag with the given name pointing to a given commit__:
```bash
git tag <tag_name> <commit>
```

+ __Create an annotated tag with the given message__:
```bash
git tag <tag_name> -m <tag_message>
```

+ __Delete the tag with the given name__:
```bash
git tag -d <tag_name>
```

+ __Get updated tags from remote__:
```bash
git fetch --tags
```

+ __Push a tag to remote__:
```bash
git push origin tag <tag_name>
```

+ __List all tags whose ancestors include a given commit__:
```bash
git tag --contains <commit>
```

## git remote
+ __List existing remotes with their names and URLs__:
```bash
git remote -v
```

+ __Show information about a remote__:
```bash
git remote show <remote_name>
```

+ __Add a remote__:
```bash
git remote add <remote_name> <remote_url>
```

+ __Change the URL of a remote (use --add to keep the existing URL)__:
```bash
git remote <set-url> <remote_name> <new_url>
```

+ __Show the URL of a remote__:
```bash
git remote <get-url> <remote_name>
```

+ __Remove a remote__:
```bash
git remote remove <remote_name>
```

+ __Rename a remote__:
```bash
git remote rename <old_name> <new_name>
```














