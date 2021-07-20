Everytime that you start a project, you have to pull to avoid merge conflicts
those happne when two changes are made to the same space or area hat conflict with changes already saved in git
to push, go to the git area or the tree, and push the + to the files you want to add to git, then they are in staged changes, and then you have to commit them and push the check mark to add them to git. Then you tap the ... and push the files
``` bash
#add files before we commited them as mnay as you want
git add <file1> <file2>
```
write notes on git init and .git
everychange is saved in .git so if yu ever make a change it's saved there
``` bash
#Gives you your status with the git cloud and your computer, what needs to be updated and what happened
git status
```

``` bash
#this allows you to write a message, basically what happned in that commit
git commit -m ""
```

```bash
#this pushes your current commit to the cloud and the control
git push origin master
```
