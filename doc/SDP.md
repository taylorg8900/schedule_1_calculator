# Requirement analysis

What problem does this program aim to solve?

I want an easy way to find out which mixer would give my current drug the most value. Once you have a drug with a lot of effects, it can get
very complicated very quickly since so many things are getting modified at once. It would take way too long to try and calculate everything
by hand or remember which mixers change which effects are present, and nobody has time for that. 

I want to give the program some amount of effects, and have it do the following:
1) Find out which mixer would give the biggest gain in mult
2) Show you the new drug, with it's:
   - Effects
     - Which effects got changed? What did they turn into?
   - Mult
     - What was the previous mult? What is it now?
   - Value
     - This is different for each kind of drug, so we need to input that along with the effects
3) If you want to keep going, repeat the process for the new version of the drug as many times as you want

It might be interesting to have the program show you the top 3 most profitable drugs, instead of just the best one. 
This could be good for seeing if you want one with funny effects, like glowing or bright eyed.

# Design

Here are the functions that we will need:

Dictionary creators
- I am going to store information about the following in different csv files, to be parsed into dictionaries with custom functions:
  1) Each effect, and it's mult value
  2) Each mixer, and it's passive effect
  3) What each effect will turn into when combined with a mixer (for example, `explosive` + `addy` -> `euphoric`)
- adsfdaf

Mult calculator
- This just takes an object which stores a drug's effects, and finds the total mult present
- This could be a method inside of an object? 

Printing functions
- I want a visually appealing way of showing these things:
  1) Which effects were in our original drug
  2) The mult value of our original drug
  3) The value of our original drug
  4) The effects in our new drug
  5) The mult value of our new drug
  6) The value of our new drug
  7) Which effects got modified along the way

What if printing out a drug looked something like this?

```commandline
CURRENT DRUG
--------------------
| Drug type:  weed |
| Drug mult:  2.18 |
| Drug value: $ 76 |
|                  |
| Effects      Mult|
| athletic     .32 |
| calming      .10 |
| focused      .16 |
| shrinking    .60 |
--------------------

NEW STRAIN 1
-----------------------------
| Drug type:    weed        |
| Drug mult:    2.34        |
| Drug value: $ 81.9        |
|                           |
| Added Mixer:  mega bean   |
| Added effect: foggy       |
| Added mult:   0.16        |
|                           |
| Modified effects          |
| athletic  -> laxative     |
| calming   -> glowing      |
| focused   -> disorienting |
| shrinking -> electrifying |
|                           |
| Effects       Mult        |
| disorienting  .00         |
| electrifying  .50         |
| foggy         .36         |
| glowing       .48         |
| laxative      .00         |
-----------------------------

Enter strain number to repeat (0 to quit): 
```

How do I store all of this information?

We need to use an object, since we need some kind of container to hold all of this information 
and will have multiple containers stored in memory.

Class diagram / UML
```commandline
Drug
--------------------
type:             str
mult:             float
value:            int
modified effects: dict[str : str]
added mixer:      str
added effect:     str
added mult:       float
effects:          dict[str : float]

value_dict:       dict[str : float]
mixer_dict:       dict[str : str]
modify_dict:      dict[dict[str : str]]
---------------------
__init__(list): dict[str : float]
get_mult(): float
get_value(): int
modify_effects(str): 
get_modified_effects(str): list
```
\_\_init__(list)
- our constructor, creates the 'effects' attribute

get_mult()
- returns the total mult for the object, uses the value_dict to do this

get_value()
- takes the 'type' attribute and the 'mult' attribute to figure out the drugs value

modify_effects(str):
- modifies the object's 'effects' attribute


# Implementation

# Testing / Debugging

# Deployment

# Maintenance