<!--title={Repository}-->

![Image result for digital repository](https://s23078.pcdn.co/wp-content/uploads/digital-repository-limbo-1.jpg) 

A **repository**, or "repo" for short, is a digital directory or storage space where you can access your project, its files, and all the versions of its files that Git saves. More simply, a repo is like a folder for your project. Your project's repository contains all of your project's files and stores each file's revision history. You can also discuss and manage your project's work within the repository.

You can obtain a Git repository in one of two ways:

1. On your machine, take a local directory that is currently not under version control, and turn it into a Git repository.
2. Clone an existing Git repository from elsewhere.

**Initializing a Repository in an Existing Directory**

If you want to turn a project directory that is currently not under version control, you first need to go to that directory by using the `cd` command on your machine, then run the `git init` command to initialize the directory to a git repo.

Here is the example steps:

```
$ cd /c/user/my_project
$ git init
```

This creates a new subdirectory named `.git` that contains all of your necessary repository files — a Git repository skeleton. At this point, nothing in your project is tracked yet. 

If you want to start version-controlling existing files (as opposed to an empty directory), you should probably begin tracking those files and do an initial commit. You can accomplish that with a few `git add` commands that specify the files you want to track, followed by a `git commit`:

```console
$ git add *.c 
$ git add LICENSE
$ git commit -m 'initial project version'
```

Note that the asterisk (`*`) is a wild card representing any amount of characters, so `git add *.c` tracks all files ending with `.c`. 

We will have other cards to explain these commands. At this point, you have Git repository with tracked files and an initial commit.

**Cloning an Existing Repository**

If you want to get a copy of an existing Git repository - for example, a project that you'd like to continue to - the command you need is `git clone`. Running this command, Git receives a full copy of nearly all data that the server has. Every version of every file for the history of the project is pulled down by default.

You clone a repository with `git clone <url>`. For example, if you want to clone the Git linkable library called `libgit2`, you can do so like this:

```console
$ git clone https://github.com/libgit2/libgit2
```

That creates a directory named `libgit2`, initializes a `.git` directory inside it, pulls down all the data for that repository, and checks out a working copy of the latest version.

If you want to clone the repository into a directory with other name, you can specify the new directory name as an additional argument:

```console
$ git clone https://github.com/libgit2/libgit2 mylibgit
```

That command does the same thing as the previous one, but the target directory is called `mylibgit`.

**Adding Files to a Repo**

You can add a file by using the `touch` command.

After new files are created, Git will notice that changes have been made inside the repo. However, Git won't officially keep track of the file unless you explicitly tell it to.

After creating the new file, you can use the `git status` command to see which files Git know exist.

**Git Status**

The `git status` command will show the working tree status.

It displays paths that have differences between the index file and the current HEAD commit, paths that have differences between the working tree and the index file, and paths in the working tree that are not tracked by Git. The first are what you *would* commit by running `git commit`; the second and third are what you *could* commit by running *git add* before running `git commit`.