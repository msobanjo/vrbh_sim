


# Robot Simulation

[![Join the chat at https://gitter.im/geo7/vrbh_sim](https://badges.gitter.im/geo7/vrbh_sim.svg)](https://gitter.im/geo7/vrbh_sim?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-generate-toc again -->
**Table of Contents**

- [Robot Simulation](#robot-simulation)
- [Code](#code)
- [Git](#git)
    - [Using Git](#using-git)
        - [A possible workflow](#a-possible-workflow)
    - [Edit files online in GitHub](#edit-files-online-in-github)
    - [Issues](#issues)
        - [DON'T CREATE MASSIVE ISSUES](#dont-create-massive-issues)
    - [Local code is useless](#local-code-is-useless)
    - [Make sure you're up to date!](#make-sure-youre-up-to-date)
    - [Keeping in sync with the master](#keeping-in-sync-with-the-master)
        - [2](#2)
        - [3](#3)
        - [4](#4)
    - [Intro to a merge conflict](#intro-to-a-merge-conflict)
- [Documentation](#documentation)
- [PyCharm](#pycharm)
    - [View TODOs in files](#view-todos-in-files)

<!-- markdown-toc end -->



# Code

4 `SPACES` (not tabs) for indentation


Make sure that code is well commented and clean. If you have no idea what
consitutes that then you can google for something along the lines of `how to
write clean code` and there will be a guide. What's currently in the `develop`
branch shouldn't be too far off either.

Basically don't try sending a pull request full of spaghetti.

```python
def something(n):
   """
   What input of n is
   what the output of something() is
   An example use case for the function
   """
   pass
```
For example 

```python
def square(n):
    """
    Takes input of an int(), returns int() which is n**3
    
    square(3) = 9
    """
    return n*n
```

This will make writing tests easier

# Git

There's a reason I put so much stress on Git in the first week.

## Using Git

You should be familiar with how to use Git at this point.

From the first weeks notes the following should have been 

* Read through the Intro to GitHub sheet on Moodle
* Go through the following videos
  [video one](https://www.youtube.com/watch?v=0fKg7e37bQE&list=PLoYCgNOIyGAB_8_iq1cL8MVeun7cB6eNc&index=14),
  [video two](https://www.youtube.com/watch?v=oFYyTZwMyAg&list=PLoYCgNOIyGAB_8_iq1cL8MVeun7cB6eNc&index=15).
  
If you have a problem you should 

* Google it 
* Search Stackoverflow
* Make a post on [Reddit](https://www.reddit.com/r/git/) or
  [Stackoverflow](http://stackoverflow.com/search?q=how+to+create+a+branch)
* Message me with all the info, **don't just say 'why won't x work'**, send
  commands that you entered etc.
  
If you're careful there shouldn't be much of an issue.

### A possible workflow

* create an issue addressing something
* state that you're going to address the issue
* fork the repo to your branch
* clone the repo to your local machine
* `git checkout develop` to make sure you're building off the develop branch (in some cases there might be a different branch to work from, it more than likely won't be the master though)
* Create a new branch off the develop branch `git branch <what-im-going-to-do`
* implement changes
* create a sensible commit message
* push the new branch up to your remote repository
* create a pull request based on the *develop* branch (unless there was another one that was meant to have been worked on) of the main repo (on my page)
* Wait for response / message me about it. 

That's a rough outline, if there's anything in there that you're not sure about
then you should go over the material again or google it. Make sure that when
you're going over material you're actually practicing on a repository as the
only way for this to sink in is to actually mess about with things. 

Learning to use it from PyCharm will also make your life easier, though you
should be also aware of what commands are being used.

## Edit files online in GitHub

You can edit files online in the webapp if it's just a quick change or addition
(to documentation or such ) this can be handy. It will offer to create a branch
automatically for you at the time.

Don't try programming here.

## Issues

You should be checking out the issues regularly and contributing to them. If
there's anything that you want to implement then you should create an issue that
addresses it so that others know what you're doing. You should also state that
you're working on it as well. It's quite alright to create an issue that you're
not working on immediately, just if there's something that you feel should be
considered by others or whatever that's a valid reason for an issue. They have
different labels that I can apply so that we can see what needs to be done
quickly. These are important.

### DON'T CREATE MASSIVE ISSUES

No one likes massive issues and it's just asking for something to go wrong.
Create small issues where the gist of what's being done can be summed up in the
heading. Something like `Create interface` would be *way* too vague for example,
as this is probably going to have a hundred smaller jobs in it. At the same time
creating one such as `type print(n) to see value of n in my code` would be
useless for hopefully obvious reasons. A better approach might be to `Implement
button to set <x> value`. 

## Local code is useless

If you have work on your computer locally for project purposes it might as well
not exist (up to a point). If no one can see it / understand it / use it then
what's the point? 

Using Github properly will enable people to work on more things faster as
everyone should be implementing small parts of the program. 

Trying to work on too much at once is going to cause problems because the
project might have moved on or in a different direction in the time you've been
working in isolation.

## Make sure you're up to date!

Don't think that you can fork the repo and that's it. You might find that your
repo is behind the master repository and if you try and make changes on that you
might bring up a load of merge conflicts. 

Keeping the code up to date is important

## Keeping in sync with the master

So far the 'easy' way to keep in sync with the main repository has been to nuke
your local one and to re-fork mine. While this approach *does* work it's perhaps
a little heavy handed, and any ease is overshadowed by tedium. This should
provide a way to keep up to date with the main repository without having to go
through that.

1. Create a fork of the repository to your GitHub
2. Add an `upstream` remote
3. fetch upstream
4. merge upstream branch to yours

**2. Add an `upstream` remote**

From the terminal 

```bash
# view the remotes that you currently have (there will be two)
git remote -v
# add the url of my branch as an 'upstream' branch
git remote add upstream <url of upstream branch>
# Now view the remotes, there'll be 4, two of which are 'upstream'
git remote -v
```

**3. fetch upstream**

This will grab everything from the upstream repo

```bash
# view the local branches
git branch -a
# fetch upstream content
git fetch upstream
# now view branches - there will be a load that also have upstream
# remotes/upstream/<--name-->
git branch -a
```

**4. merge upstream branch to yours**

Now the upstream branches are local - but you still need to get their content in
with yours. This is done using the `merge` command. I'm not going to go into
merge conflicts here, hopefully you don't have any, keeping up to date regularly
will help to prevent them.

Make sure that you're in the branch that you want to merge into, so if you want
to merge `upstream/item-one` content into your branch `origin/test-item` you
would do the following

```bash
# check you're in the correct branch 
git branch
# merge in the content of the remotes branch
git merge upstream/item-one
```

Hopefully this will go smoothly !

## Intro to a merge conflict

So just so there's an idea of what a conflict is here - it's basically when two
people edit the same file with different (and conflicting) information.

Original File - 
```python
v = "print"
print(v)
```

Person A 

```python
v = "stop"
print(v * 2)
```

Person B

```python
v = "start"
print(v * 2)
```

Both want to commit this code - but the same content has changed and Git can't
tell which version is most important. When this happens it flags it as a merge
conflict and leaves you to decide which is the version that you want.

Here I've created the above files in a git repository and I'm merging the
`person-a` branch into my `master`

```bash
$ git branch -a
* master
  person-a
  person-b

$ git merge person-a 
Updating f7c0e95..df6750a
Fast-forward
 file | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)
$ 
```

All good, however I'll now try and merge `person-b` in the master -

```bash
~/git-demo
$ git merge person-b
Auto-merging file
CONFLICT (content): Merge conflict in file
Automatic merge failed; fix conflicts and then commit the result.
```

Ah, `CONFLICT`, because the files contain different content *at the same places*
and Git can't tell which content is more important, so it hands the choice over
to the user.

Now if we look at the file contents -

```text
<<<<<<< HEAD
v = "stop"
print(v * 2)
=======
v = "start"
print(v * 5)
>>>>>>> person-b
```

We can see that our `HEAD` (the commit that git is currently pointing to) has
the contents of `person-a` that we merged in without trouble, but we also have
the contents of `person-b` underneath the equals `=======` signs.

Now it's a case of manually editing to see which is needed, perhaps the goal was
to print `stop` 5 times (a mix of both), in which case I would edit as follows -

```text
v = "stop"
print(v * 5)
```


```bash
# get status - currently there's a conflict BUT I have just fixed this

$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")

Unmerged paths:
  (use "git add <file>..." to mark resolution)

	both modified:   file

# I can add the file with the changes that I've made (which is the same file -
I've just edited that file and saved it)

$ git add file
$ git commit -m 'fixed conflict'
[master d6bd293] fixed conflict

# The conflict is now resolved

$ git status
On branch master
nothing to commit, working directory clean
```


You shouldn't have to do this (and neither should I), but it's good to have an
idea of what it means. 

Also I'll point out that this was for **2 LINES** of code - if there are 30
lines+ you can see how something of this nature can be a nightmare to ammend.


# Documentation

I'm trying to document things in here so that others can see what's going on and
what's been implemented. If you work on something it might take you a while to
figure something out and writing out some info for others will enable them to
learn from that as well as you and should make the project easier to understand
overall. Of course the code itself should be pretty readable but for somethings
it can help to have a bit more of a verbose / prose explanation for things.

Please contribute to this.

# PyCharm

If you find something particularly useful it might benefit all to update the
information here.

## View TODOs in files

`view > tool windows > TODO` or `Alt f6`. 

This will show you the `TODOs` that are currently in files in the bottom of the screen and you can nav around them, quite useful.
