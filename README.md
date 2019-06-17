# Plane Game
ICS 2O1 CPT - Nicholas Poon and Timothy Zheng

## Info

  A pun on *plain* game, Plane Game is a side-scrolling game based off of PyArcade. The objective of the game is to travel the longest distance by avoiding stars and collecting coins for upgrades. Players are encouraged to beat their previous high scores, which are stored in a non-volatile format, meaning that players can return to their game without losing their hard-fought records. As players progress in the level, the obstacles move faster! **How far can your plane go?** 

# Installation Instructions

### Plane Game requires the following package:

• **PyArcade**: https://pypi.org/project/arcade/ 

• **IMPORTANT:** PyArcade version 2.0.9 or later MUST be used! Parameters for loading sprites have changed since this version.


Simply download the whole repository and after extracting, put it under a single directory, and run it with your IDE of choice.


# Game Instructions

## Goal
  The ultimate goal is to try to get the highest possible score, employing different tactics and tricks to get the highest score. The user must move their plane to avoid touching any of the obstacles.
  
## Controls
Plane game can be controlled with only two buttons.

• Pressing UPARROW `↑` moves the plane up.

• Pressing DOWNARROW `↓` moves the plane down.

• Pressing `ESCAPE` while playing the game will result in an immediate ending of the round.

• Pressing `SPACE` while playing the game will pause the game. This can only be done **twice** per round.

## Menus
When entering the game, four buttons can be found. From left to right, these three buttons are: leaderboards, play, instructions, and shop.
Clicking on any of these buttons leads to their respective menus. 

• **Leaderboards:** The furthest left, this menu will show up to ten of a player's highest scores. Players can compete by comparing their highest scores with each other.

  • A player may also clear their high scores list here by clicking on the red reset button.
  
• **Play:** Located in the middle, pressing this button launches Plane Game. After clicking on this button, the user should begin controlling their plane with the keyboard. 
  • A buffer-zone equal to half of `WIDTH` is given to facilitate this transition, giving the player more time to react. 
  
• **Instructions:** Anyone requiring reminders of the game's features of any further clarification on the game's mechanics can navigate to this screen.

• **Shop:** Furthest right, pressing this button will bring up the shop where upgrades can be purchased.
  • Player balance will also be shown here on the top right
  • Player progress (Coins, upgrades) can be reset here as well by clicking on the red reset button.
  
## Currency
In order to gain currency, the player must try to maneuver their airplane to touch coins that are flying by. Be careful though! You won't want to touch a star by accident!

## Upgrades
Intended for players who are interested in gaining the highest possible score, upgrades can be purchased with currency collected from playing the game. To purchase the **elevator upgrade**, click on the store icon. Here, you will be able to purchase the elevator upgrade if you have the specified amount of coins. Players are highly encouraged to purchase upgrades in order to increase the skill cap of the game.

• Upgrades get more expensive and increase the vertical speed of the plane less and less as more upgrades are purchased. More information on the calculations can be found at the bottom of this document.


## Changing Controls
For more experienced coders, controls can be easily changed in `Plane_Game_Beta.py` under the `on_key_press` and `on_key_release` functions.



      if game:
    
          global keyup
        
          if key == arcade.key.DOWN:
        
              keyup = False
            
          if key == arcade.key.UP:
        
              keyup = True
            


Changing `arcade.key.DOWN` to another key such as `S` for down can be as simple as `arcade.key.S`.

Changing `arade.key.UP` follows the same principle.

• **Example:** 

   > Change up to `W` and down to `S` 
   




      if game:
    
          global keyup
        
          if key == arcade.key.S:
        
              keyup = False
            
          if key == arcade.key.W:
        
              keyup = True
            


• **IMPORTANT** 

You MUST also mirror these to the `on_key_release` function!





      if game:
    
          global keyup
        
          if key == arcade.key.S:
        
             keyup = True
            
          if key == arcade.key.W:
        
              keyup = False
            
## Performance Requirements:


• Screen resolution must be at least 1600 x 900 pixels

• To ensure that the game runs at its optimal speed, ensure that your [power option](https://gyazo.com/01f2a91c68cab85950ac2ff14a191591) is set to **high performance** in windows.

• If on a laptop, plugging it in to its AC adapter may also improve performance to match realtime rendering.

## Stats for Nerds

• Graphs on the calculations behind shop pricing and speed upgrades can be found [here](https://www.desmos.com/calculator/xjoczpbfcc)

• The highest plane speed that can be achieved is 17.999999999999986 pixels per frame, and occurs on the 357th upgrade! 
It would come at a cost of 4,667,980,210,673,925,2074,891.5998 coins!

(If you manage to get this point you've truly beaten the game, but probably cheated)



