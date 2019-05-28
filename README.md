# CPT
Plane Game - Nicholas and Tim

**Status:** Under development

## Info

  A pun on *plain* game, Plane Game is a side-scrolling game based off of PyArcade. The objective of the game is to travel the longest distance by avoiding or destroying obstacles. Players are encouraged to beat their previous high scores, which are stored in a non-volatile format, meaning that players can return to their game without losing their hard-faught records. As players progress in the level, the obstacles move faster! **How far can your plane go?** 

## Installation Instructions

### Plane Game requires the following packages:

• **Random**: https://docs.python.org/2/library/random.html

• **PyArcade**: https://pypi.org/project/arcade/ 

Simply download the whole repository and after extracting, put it under a single directory, and run it with your IDE of choice.


# Game Instructions

## Goal
  The ultimate goal is to try to get the highest possible score, employing different tactics and tricks to get the highest score. The user must move their plane to avoid touching any of the obstacles.
  
## Controls
Plane game can be controlled with only two buttons.

• Pressing UPARROW `↑` moves the plane up

• Pressing DOWNARROW `↓` moves the plane down

## Menus
When entering the game, three buttons can be found. From left to right, these three buttons are: leaderboards, play, and shop.
Clicking on any of these buttons leads to their respective menus. 

• **Leaderboards:** The furthest left, this menu will show up to ten of a player's highest scores.

  • A player may also clear their high scores list here.
  
• **Play:** Located in the middle, pressing this button launches Plane Game. After clicking on this button, the user should begin controlling their plane with the keyboard. 
  • A buffer-zone equal to half of `WIDTH` is given to facilitate this transition. 

• **Shop:** Furthest right, pressing this button will bring up the shop where upgrades can be purchased.
  • Player balance will also be shown here
  
## Upgrades
Intended for players who are interested in gaining the highest possible score, upgrades can be purchased with currency collected from playing the game.

> - UPGRADES TBD - 

## Changing Controls
For more experienced coders, controls can be easily changed in `Plain_Game_Beta.py` under the `on_key_press` and `on_key_release` functions



      if game:
    
          global keyup, keydown
        
          if key == arcade.key.DOWN:
        
              keydown = True
            
          if key == arcade.key.UP:
        
              keyup = True
            
`

Changing `arcade.key.DOWN` to another key such as `S` for down can be as simple as `arcade.key.S`

Changing `arade.key.UP` follows the same principle.

• **Example:** 

   > Change up to `W` and down to `S` 
   




      if game:
    
          global keyup, keydown
        
          if key == arcade.key.S:
        
              keydown = True
            
          if key == arcade.key.W:
        
              keyup = True
            
`

• **IMPORTANT** 

You MUST also mirror these to the `on_key_release` function!





      if game:
    
          global keyup, keydown
        
          if key == arcade.key.DOWN:
        
             keydown = False
            
          if key == arcade.key.UP:
        
              keyup = False
            
`



