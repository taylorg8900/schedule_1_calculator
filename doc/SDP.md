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
-type:             str
-mult:             float
-value:            int
-modified_effects: dict[str : str]
-added_mixer:      str
-added_effect:     str
-added_mult:       float
-effects:          dict[str : float]

-value_dict:       dict[str : float]
-mixer_dict:       dict[str : str]
-modify_dict:      dict[dict[str : str]]
---------------------
__init__(type, list): dict[str : float]
-calc_mult():          
-calc_value():    
-create_dicts()     
+add_mixer(str)
-modify_effects(str)
-create_modified_effects_dict(str)

+get_type():                str
+get_effects():             list(str)
+get_mini_representation(): list(str)
+get_representation():      list(str)
```
Thoughts while creating UML
- For calculating the best new strain, would it make sense to create a new drug object and find its mult / value with its methods?
- I want get_representation to be a list of strings instead of one string, so that I can print multiple strains horizontally relative to each other, rather than vertically
- The difference between the first drug and strain 1 in the example up there, is that we are not printing out the attributes we don't need or have default values


Pseudocode for methods
```commandline
__init__(str: type, list: list(str)):
    set up self. variables' default values
        self.type = type
        self.mult = 0
        self.value = 0
        self.effects = {}
        self.added_mixer = ''
        self.added_effect = ''
        self.added_mult = 0
        
    call create_dicts to create every dictionary
    self.effects = {}
    for effect in list
        self.effects[effect] = self.value_dict[effect]
    call calc_mult
    call calc_value

add_mixer(str mixer)
    first get the following
        self.added_mixer
        self.added_effect
        self.added_mult
        call create_modified_effects_dict
    call modify_effects(str)
    
create_modified_effects_dict(str mixer)
    dict = {}
    for effect in self.effects
        if effect can be modified / exists in self.modify_dict[mixer][effect]
            dict[effect] = self.modify_dict[mixer][effect]
        otherwise, do nothing
    self.modified dicts = dict

modify_effects(str mixer)
    remember to add self.added mixer to the dict
    new_effects = {}
    for effect in self.effects
        idea: if effect can be modified as per what is in self.modify_dict, then add the modified version of effect to new_effects
        if effect can't be modified / is not in self.modify_dict[mixer], then just add what is already in self.effects to new_effects
        
        if effect exists in self.modify_dict[mixer]
            new_effects[effect] = self.modify_dict[mixer][effect]
        else
            new_effects[effect] = self.effects[effect]
    add self.added mixer to the dict 
    self.effects = new_effects

calc_mult():
    total = 1
    for each key in self.effects
        total += self.effects[key]
    self.mult = total

calc_value()
    drug_name = self.type.lower().strip()
    if drug_name.startswith('we')
        self.value = self.mult * 35
    repeat for other drugs
    else
        self.value = 0

create_dicts()
    import dict functions from dicts.py and let it rip brother
    


```




# Implementation

# Testing / Debugging

# Deployment

# Maintenance