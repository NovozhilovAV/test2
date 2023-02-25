#
# t.student@1004-9 MINGW64 ~
# $ cd Documents
#
# t.student@1004-9 MINGW64 ~/Documents
# $ cd visual studio 2022
# bash: cd: too many arguments
#
# t.student@1004-9 MINGW64 ~/Documents
# $ ls
# '3ds Max 2021'/   ROBLOX/                desktop.ini        'Моя музыка'@
#  Adobe/           SavedGames/            Ира.rbxl           'мои рисунки'@
#  Default.rdp     'Visual Studio 2022'/  'Мои видеозаписи'@
#
# t.student@1004-9 MINGW64 ~/Documents
# $ cd Visual\ Studio\ 2022/
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022
# $ ls
# 'Code Snippets'/   Novozhilov/   Templates/   __pycache__/   py1.py   py1_test.py
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022
# $ cd Novozhilov/
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ ls
# Git1.py
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git add .
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git status
# On branch master
#
# No commits yet
#
# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#         new file:   Git1.py
#
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git commit -m 'First commit'
# [master (root-commit) 9c42ce5] First commit
#  Committer: Test Student <t.student@itstep.local>
# Your name and email address were configured automatically based
# on your username and hostname. Please check that they are accurate.
# You can suppress this message by setting them explicitly:
#
#     git config --global user.name "Your Name"
#     git config --global user.email you@example.com
#
# After doing this, you may fix the identity used for this commit with:
#
#     git commit --amend --reset-author
#
#  1 file changed, 3 insertions(+)
#  create mode 100644 Git1.py
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git config --global user.name 'NovozhilovAV'
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git config --global user.email 'tema.reida87@mail.ru'
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git commit -m 'First commit'
# On branch master
# nothing to commit, working tree clean
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git status
# On branch master
# nothing to commit, working tree clean
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git push origin master
# Enumerating objects: 3, done.
# Counting objects: 100% (3/3), done.
# Writing objects: 100% (3/3), 245 bytes | 245.00 KiB/s, done.
# Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
# To https://github.com/NovozhilovAV/test.git
#  * [new branch]      master -> master
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git add .
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git status
# On branch master
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
#         new file:   git2Test.py
#
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git add git2Test.py
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git status
# On branch master
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
#         new file:   git2Test.py
#
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git commit -m 'Two commit for git2'
# [master a181b66] Two commit for git2
#  1 file changed, 3 insertions(+)
#  create mode 100644 git2Test.py
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git push origin master
# Enumerating objects: 4, done.
# Counting objects: 100% (4/4), done.
# Delta compression using up to 4 threads
# Compressing objects: 100% (2/2), done.
# Writing objects: 100% (3/3), 326 bytes | 326.00 KiB/s, done.
# Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
# To https://github.com/NovozhilovAV/test.git
#    9c42ce5..a181b66  master -> master
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git add git3Test.py
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git commit -m 'Загружаем еще один фаил'
# [master e1e9d8e] Загружаем еще один фаил
#  1 file changed, 3 insertions(+)
#  create mode 100644 git3Test.py
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git push origin master
# Enumerating objects: 4, done.
# Counting objects: 100% (4/4), done.
# Delta compression using up to 4 threads
# Compressing objects: 100% (2/2), done.
# Writing objects: 100% (3/3), 366 bytes | 366.00 KiB/s, done.
# Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
# To https://github.com/NovozhilovAV/test.git
#    2344f03..e1e9d8e  master -> master
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git add .
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git status
# On branch master
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
#         renamed:    git3Test.py -> git2Test.py
#
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git commit -m 'Rename file git3Test to git2Test'
# [master 742ebf0] Rename file git3Test to git2Test
#  1 file changed, 0 insertions(+), 0 deletions(-)
#  rename git3Test.py => git2Test.py (100%)
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git push origin master
# Enumerating objects: 3, done.
# Counting objects: 100% (3/3), done.
# Delta compression using up to 4 threads
# Compressing objects: 100% (2/2), done.
# Writing objects: 100% (2/2), 288 bytes | 288.00 KiB/s, done.
# Total 2 (delta 0), reused 0 (delta 0), pack-reused 0
# To https://github.com/NovozhilovAV/test.git
#    e1e9d8e..742ebf0  master -> master
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git mv git2Test.py git23Test.py
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git status
# On branch master
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
#         renamed:    git2Test.py -> git23Test.py
#
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git commit -m 'Rename file for MV'
# [master 37b1ffc] Rename file for MV
#  1 file changed, 0 insertions(+), 0 deletions(-)
#  rename git2Test.py => git23Test.py (100%)
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git push origin master
# Enumerating objects: 3, done.
# Counting objects: 100% (3/3), done.
# Delta compression using up to 4 threads
# Compressing objects: 100% (2/2), done.
# Writing objects: 100% (2/2), 278 bytes | 278.00 KiB/s, done.
# Total 2 (delta 0), reused 0 (delta 0), pack-reused 0
# To https://github.com/NovozhilovAV/test.git
#    742ebf0..37b1ffc  master -> master
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ ^C
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git log
# commit 834d739780da559e04090fb558283135730ce86d (HEAD -> master, origin/master)
# Author: NovozhilovAV <tema.reida87@mail.ru>
# Date:   Thu Feb 16 21:40:22 2023 +0300
#
#     Add new folder to tree file
#
# commit 37b1ffc30ff7e305f191f9a4dcba6df70c9ae4fb
# Author: NovozhilovAV <tema.reida87@mail.ru>
# Date:   Thu Feb 16 21:32:25 2023 +0300
#
#     Rename file for MV
#
# commit 742ebf0c805b1758810e3d5e82b10593db8e5102
# Author: NovozhilovAV <tema.reida87@mail.ru>
# Date:   Thu Feb 16 21:28:13 2023 +0300
#
#     Rename file git3Test to git2Test
#
# commit e1e9d8e5b6ce0a7a10ea61169143cb16ae04a799
# Author: NovozhilovAV <tema.reida87@mail.ru>
# Date:   Thu Feb 16 21:19:12 2023 +0300
#
#     Загружаем еще один фаил
#
# commit 2344f033582d0f96e1ba184c4ac7a2cdf8b5b85b
# Author: NovozhilovAV <tema.reida87@mail.ru>
# Date:   Thu Feb 16 21:14:11 2023 +0300
#
#     Удаляем фаил
#
# commit a181b66f931357eaf8f5b9db014a38c908d02928
# Author: NovozhilovAV <tema.reida87@mail.ru>
# Date:   Thu Feb 16 20:59:52 2023 +0300
#
#     Two commit for git2
#
# commit 9c42ce5f9d6fc2790fec22474c62b1bc383dae20
# Author: Test Student <t.student@itstep.local>
# Date:   Thu Feb 16 20:10:39 2023 +0300
#
#     First commit
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git log --online
# fatal: unrecognized argument: --online
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git log --oneline
# 834d739 (HEAD -> master, origin/master) Add new folder to tree file
# 37b1ffc Rename file for MV
# 742ebf0 Rename file git3Test to git2Test
# e1e9d8e Загружаем еще один фаил
# 2344f03 Удаляем фаил
# a181b66 Two commit for git2
# 9c42ce5 First commit
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $ git log master --oneline
# 834d739 (HEAD -> master, origin/master) Add new folder to tree file
# 37b1ffc Rename file for MV
# 742ebf0 Rename file git3Test to git2Test
# e1e9d8e Загружаем еще один фаил
# 2344f03 Удаляем фаил
# a181b66 Two commit for git2
# 9c42ce5 First commit
#
# t.student@1004-9 MINGW64 ~/Documents/Visual Studio 2022/Novozhilov (master)
# $
