# Requirements analysis

This program needs two files;
1. One that holds information about each effect's value multiplier
2. One that holds information about which effects are modified when a new mixer is introduced to a mix

From the second file, we can use the first file to determine the total mult added to a mix when something is added.
Sometimes this will be very little, or negative, or a lot depending on which effect gets turned into what. For example, 
turning the 'laxative' effect into 'long faced + spicy' with a chili would net you a positive change multiplier of 0.90.

However, this only works if the added effects are not already part of the effects in the drug. We need to create a data
structure which holds all of the information from both the first and second files, and will go through until it finds a 
mix that is the highest possible additional mult for effects which are not present already.

After finding the highest possible additional mult this way, we show the user the results:
- initial mix, value multiplier, and total value (which depends on the drug)
- which effects got removed, and then added
- resulting mix, value multiplier, and total value (which depends on the drug)

# Design

We need a data structure which can hold the following information:
- Some initial effect to be modified
- A mixer that will modify the intial effect
- What the initial effect turns into
- The additional effect that the mixer introduces passively (example: chili will always add spicy)
- the resulting added value mult, which is the following
  - (value of resulting effect + value of mixer's passive added effect) - (original effect)

What if we had a dictionary structured like this?
```python
mixes = {
    chili: {
        'shrinking': 'refreshing',
        'athletic': 'euphoric',
        'munchies': 'toxic',
        'anti gravity': 'tropic thunder',
        'sneaky': 'bright eyed',
        'laxative': 'long faced' },
    addy: {
        'glowing': 'refreshing',
        'foggy': 'energizing',
        'sedating': 'gingeritis',
        'long faced': 'electrifying',
        'explosive': 'euphoric'}
    
}
```
Let me think really fast about how I would go about finding the largest value possible manually...

Steps
1. Set some value 'max' to 0
2. For each effect present, look up the added mult value. 
3. Find the mult value for the effects that *can be added*
   - Out of the modified effect and passively added effect, this could be both, or just one, or neither
4. After going through all of the mixing table things, look at the single effect table and see if that mult can be added on it's own
5. if mult is greater than max, update max

Here are some functions I need for all of this
- Function to take the effect_values file and turn it into a dictionary, so we can find values of each effect quickly
- Function to create the mix / modification effect dictionary of dictionaries
- Function to create a dict from a csv file for mixer's passive effects
- Function to find out if an effect can be added to our drug
- Function to find the mult value for effects that can be added

Here is the structure of the project

1. Find out which drug we are using
2. Find out which effects are present
3. Create the values dictionary
4. Create the mixes dictionary of dictionaries
5. Set some max value to 0
6. For each effect present:
   - Find the mult value for effects that *can be added* against our original effect
   - If the mult value is greater than our max, update max
7. Search another dictionary for singly adding effects, and compare against max
8. Print results in a nice format

# Implementation



# Testing and debugging

# Deployment

# Maintenance