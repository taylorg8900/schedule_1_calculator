# About this program

I made this program because I wanted a really easy way to find combinations of mixers in Schedule 1. I wanted some program that could
find out what the best possible mixer to add was so that I wouldn't have to manually calculate anything on my own. 

This program lets you input a drug and it's effects, and see which mixers will give you the best value for your drug and which
effects they are modifying.

I also included a file called recursion.py, which will recursively find the absolute best mixer value up to a certain depth,
and return which path got you there. This takes exponentially longer the higher the depth is, but it will show you the best possible
value paths in the game.

# How to use this program

This program is meant to be ran in the shell (Command Line Interface), since the display of different modified strains of your drug relies upon
being ran in a shell.

You also need python to run this program.

If you aren't familiar with git or using a Command Line Interface, then the first thing you should do is download 'git bash', which
is just a shell program that comes with git installed. Git is a version control software, which is a fancy way of saying it lets you create 
save points for your program, and download other people's repositories (like this one). Go find a tutorial online for things like
downloading git bash, navigating in the shell, and using git clone to download repositories.

If you want the easiest way of running this program, here are the steps to do so:
1) Download [the latest version of python](https://www.python.org/downloads/)
2) Download [git bash](https://git-scm.com/downloads)
   - While setting up the shell, make sure to select `nano` as the default text editor
   - If you need to follow these directions to download the program, then you definitely do not want to use `vim`, the default text editor for git bash
3) Click on `tags` (to the left of the green `code` button) and download the [latest release](https://github.com/taylorg8900/schedule_1_calculator/tags)
4) Drag and drop the file somewhere on your computer
5) Navigate to where you put the file
   - If you navigate using file explorer, you can right click on the folder and select 'open git bash here'
   - If you want to navigate using the shell, use commands like `cd` and `ls`
      - Here is a website with [common shell commands](https://www.educative.io/blog/bash-shell-command-cheat-sheet) to navigate / open files
      - `cd` and `ls` are probably going to be all you need though!
6) type "python main.py" to run the program

It is ok to not input any effects for your drug! If you want to explore all of the possible mixes that you can have starting with nothing,
just press enter when the program asks you for your current effects.

While running the program if you want to see all possible strains that you can make, just type in a really large number - the program does not
let you go over the amount that you can make with the mixers in the game.

If you want to resize the shell's window, use `ctrl +` or `ctrl -`. The programs display will adjust automagically.


# Examples of output by this program

Here is an example of output when you only want to show 3 possible strains at once:
```commandline
CURRENT STRAIN: []
Current strain
----------------------
| Drug type:    meth |
| Drug mult:    1    |
| Drug value: $ 70   |
|                    |
| Effects (0)  Mult  |
----------------------


STRAIN 1                       STRAIN 2                          STRAIN 3
-----------------------------  --------------------------------  -----------------------------------
| Drug type:    meth        |  | Drug type:    meth           |  | Drug type:    meth              |
| Drug mult:    1.52        |  | Drug mult:    1.46           |  | Drug mult:    1.44              |
| Drug value: $ 106.4       |  | Drug value: $ 102.2          |  | Drug value: $ 100.8             |
|                           |  |                              |  |                                 |
| Added Mixer:  horse semen |  | Added Mixer:  viagra         |  | Added Mixer:  addy              |
| Added effect: long faced  |  | Added effect: tropic thunder |  | Added effect: thought provoking |
| Added mult:   0.52        |  | Added mult:   0.46           |  | Added mult:   0.44              |
|                           |  |                              |  |                                 |
| Modified effects          |  | Modified effects             |  | Modified effects                |
|                           |  |                              |  |                                 |
| Effects (1)  Mult         |  | Effects (1)     Mult         |  | Effects (1)        Mult         |
| long faced  0.52          |  | tropic thunder  0.46         |  | thought provoking  0.44         |
-----------------------------  --------------------------------  -----------------------------------

Enter a strain number to repeat (Q to quit) (press Enter to go back by one strain):
```
Here is an example for a strain with a lot of effects!
```commandline
CURRENT STRAIN: ['athletic', 'calming', 'sneaky'] + horse semen + addy + iodine + motor oil
Current strain + 3 + 3 + 2 + 1
---------------------------
| Drug type:    meth      |
| Drug mult:    3.56      |
| Drug value: $ 249.2     |
|                         |
| Effects (7)        Mult |
| athletic           0.32 |
| balding            0.3  |
| electrifying       0.5  |
| jennerising        0.42 |
| slippery           0.34 |
| sneaky             0.24 |
| thought provoking  0.44 |
---------------------------


STRAIN 1                      STRAIN 2                          STRAIN 3
----------------------------  --------------------------------  ------------------------------------
| Drug type:    meth       |  | Drug type:    meth           |  | Drug type:    meth               |
| Drug mult:    3.76       |  | Drug mult:    3.7            |  | Drug mult:    3.68               |
| Drug value: $ 263.2      |  | Drug value: $ 259.0          |  | Drug value: $ 257.6              |
|                          |  |                              |  |                                  |
| Added Mixer:  banana     |  | Added Mixer:  viagra         |  | Added Mixer:  chili              |
| Added effect: gingeritis |  | Added effect: tropic thunder |  | Added effect: spicy              |
| Added mult:   0.2        |  | Added mult:   0.14           |  | Added mult:   0.12               |
|                          |  |                              |  |                                  |
| Modified effects         |  | Modified effects             |  | Modified effects                 |
|                          |  | athletic -> sneaky           |  | athletic          -> euphoric    |
| Effects (8)        Mult  |  |                              |  | sneaky            -> bright eyed |
| athletic           0.32  |  | Effects (7)        Mult      |  | thought provoking -> focused     |
| balding            0.3   |  | balding            0.3       |  |                                  |
| electrifying       0.5   |  | electrifying       0.5       |  | Effects (8)   Mult               |
| gingeritis         0.2   |  | jennerising        0.42      |  | balding       0.3                |
| jennerising        0.42  |  | slippery           0.34      |  | bright eyed   0.4                |
| slippery           0.34  |  | sneaky             0.24      |  | electrifying  0.5                |
| sneaky             0.24  |  | thought provoking  0.44      |  | euphoric      0.18               |
| thought provoking  0.44  |  | tropic thunder     0.46      |  | focused       0.16               |
----------------------------  --------------------------------  | jennerising   0.42               |
                                                                | slippery      0.34               |
                                                                | spicy         0.38               |
                                                                ------------------------------------

Enter a strain number to repeat (Q to quit) (press Enter to go back by one strain):
```

You can have much more than just 3 strains!
```commandline
CURRENT STRAIN: ['athletic', 'long faced', 'sneaky', 'toxic']
Current strain
-----------------------
| Drug type:    meth  |
| Drug mult:    2.08  |
| Drug value: $ 145.6 |
|                     |
| Effects (4)  Mult   |
| athletic    0.32    |
| long faced  0.52    |
| toxic       0.0     |
| sneaky      0.24    |
-----------------------


STRAIN 1                       STRAIN 2                             STRAIN 3
-----------------------------  -----------------------------------  -----------------------------
| Drug type:    meth        |  | Drug type:    meth              |  | Drug type:    meth        |
| Drug mult:    2.54        |  | Drug mult:    2.5               |  | Drug mult:    2.5         |
| Drug value: $ 177.8       |  | Drug value: $ 175.0             |  | Drug value: $ 175.0       |
|                           |  |                                 |  |                           |
| Added Mixer:  paracetamol |  | Added Mixer:  addy              |  | Added Mixer:  iodine      |
| Added effect: sneaky      |  | Added effect: thought provoking |  | Added effect: jennerising |
| Added mult:   0.46        |  | Added mult:   0.42              |  | Added mult:   0.42        |
|                           |  |                                 |  |                           |
| Modified effects          |  | Modified effects                |  | Modified effects          |
| toxic -> tropic thunder   |  | long faced -> electrifying      |  | toxic -> sneaky           |
|                           |  |                                 |  |                           |
| Effects (4)     Mult      |  | Effects (5)        Mult         |  | Effects (4)  Mult         |
| athletic        0.32      |  | athletic           0.32         |  | athletic     0.32         |
| long faced      0.52      |  | electrifying       0.5          |  | jennerising  0.42         |
| sneaky          0.24      |  | sneaky             0.24         |  | long faced   0.52         |
| tropic thunder  0.46      |  | thought provoking  0.44         |  | sneaky       0.24         |
-----------------------------  | toxic              0.0          |  -----------------------------
                               -----------------------------------

STRAIN 4                       STRAIN 5                     STRAIN 6
-----------------------------  ---------------------------  ---------------------------
| Drug type:    meth        |  | Drug type:    meth      |  | Drug type:    meth      |
| Drug mult:    2.48        |  | Drug mult:    2.48      |  | Drug mult:    2.42      |
| Drug value: $ 173.6       |  | Drug value: $ 173.6     |  | Drug value: $ 169.4     |
|                           |  |                         |  |                         |
| Added Mixer:  battery     |  | Added Mixer:  chili     |  | Added Mixer:  motor oil |
| Added effect: bright eyed |  | Added effect: spicy     |  | Added effect: slippery  |
| Added mult:   0.4         |  | Added mult:   0.4       |  | Added mult:   0.34      |
|                           |  |                         |  |                         |
| Modified effects          |  | Modified effects        |  | Modified effects        |
|                           |  | athletic -> euphoric    |  |                         |
| Effects (5)  Mult         |  | sneaky   -> bright eyed |  | Effects (5)  Mult       |
| athletic     0.32         |  |                         |  | athletic    0.32        |
| bright eyed  0.4          |  | Effects (5)  Mult       |  | long faced  0.52        |
| long faced   0.52         |  | bright eyed  0.4        |  | slippery    0.34        |
| sneaky       0.24         |  | euphoric     0.18       |  | sneaky      0.24        |
| toxic        0.0          |  | long faced   0.52       |  | toxic       0.0         |
-----------------------------  | spicy        0.38       |  ---------------------------
                               | toxic        0.0        |
                               ---------------------------

Enter a strain number to repeat (Q to quit) (press Enter to go back by one strain):

```