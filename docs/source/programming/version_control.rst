Version Control
===============

What is Version Control and Why Do We Use It?
---------------------------------------------

Version control is a system that helps track changes made to files, documents, or code over time. It records each modification, allowing you to revisit or revert to previous versions of a file when needed. This is especially important in collaborative projects where multiple people might be working on the same files. Version control ensures that everyone’s changes are tracked, reduces the risk of losing work, and helps resolve conflicts when multiple people edit the same parts of a project.

Using version control is crucial in software development, research, and any project that involves multiple people or iterative work. It allows developers to work on different parts of a project simultaneously without interfering with each other’s work. Version control also makes it easier to experiment with new features or fixes, as you can create a branch of your project, make changes, and later merge them into the main project when they’re ready. In case something goes wrong, version control allows you to easily roll back to a stable state, preventing potential data loss or mistakes.

Git and Its Role in Version Control
-----------------------------------

Git is one of the most popular version control systems used today. It was created by Linus Torvalds in 2005 to manage the development of the Linux kernel and has since become the go-to tool for version control in software development. Git allows users to track changes in their code, collaborate with others, and manage different versions of a project in an efficient and flexible way.

What makes Git unique is its distributed nature, meaning every developer has a complete copy of the project’s history on their local machine. This makes working offline possible and speeds up operations like checking out versions or branching. Git uses "commits" to record changes, and each commit includes a snapshot of the changes made along with a message explaining the update. It also supports branching and merging, allowing developers to create separate branches for new features or bug fixes, and then merge those changes back into the main project. Git is widely used in open-source and professional development projects, often with hosting services like GitHub, GitLab, or Bitbucket to facilitate collaboration and code sharing.

We use git on our team.

Getting Started with Git
-------------------------

To begin with, as a general tutorial watch this video `Git Tutorial For Beginners <https://www.youtube.com/watch?v=8JJ101D3knE&t=2148s>`_.

Git workflow
------------

Our team does not have a specific git workflow, but we generally try to make branches based on the name of a feature.
For example, if you are assigned to work on getting the elevator running, you might make a branch called `elevator` and work on that branch. 
Once you are done, you can merge it back into the main branch, then delete your `elevator` branch. If after the elevator has basic functionality you want to increase its speed, 
you might make a branch called `elevator-speed` and work on that.

Also for better communication, software tasks are documented as git issues. If you are working on a current issue, make a comment underneath it.
When you are done and have merged your branch, close the issue, and delete your branch.

All merges into master are done through Github Pull Requests. PRs should be reviewed but atleast one other member before they are merged.
Furthermore, merges into master shbould be tested on a robot or in sim in its own branch before making a PR. In your PR please provide steps for how
someone can verify correct behavior. 

If there are tests that can be written for your code, please write them and run them before making a PR.

If you are working on a feature that is not yet ready to be merged into master, you can make a draft PR. This will allow you to get feedback on your code without it being merged.

If there are merge conflicts when you try to merge your branch into master, you will need to resolve them before your PR can be merged.
Let a veteran member or lead help you with this as they can be tricky to resolve, and it is important to not lose any work.

.. note::
    Add a section on how to resolve merge conflicts.
    
.. note::
    Add a workflow diagram.

Git Cheat sheet
---------------

Here is a handy cheat sheet for git commands :download:`Git Cheat Sheet </_static/pdfs/git-cheat-sheet.pdf>`.

.. note::
    The cheat sheet is a quick reference guide for common git commands. It includes commands for creating repositories, adding files, committing changes, branching, merging, and more. Keep it handy as you start using git for your projects.


