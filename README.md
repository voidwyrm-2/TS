# TS
(help me)

## TurtleSequencer.py
This is a horrifying way to actively draw with python turtle

It uses sequences of instruction in the format of x,y/x,y/x,y

This is a horribly tedious way to draw(but I'm proud of it)

You can find examples of drawings in drawings/presets.txt

(type "file/run [filename]" to run a file)

## TScreator.py
This uses pygame to create a way to more easily draw using TurtleSequencer

~~I'm not giving any instructions for this, right now(me lazy)~~
I stand corrected, here's instructions(I was ~~procraftinating on sleeping~~ bored)
<details>
    <summary>TScreator instructions</summary>
    
    WASD/arrow keys to move
    
    It's currently in pixel mode by default, the switch for it is on line 38
    
    Press enter to place a waypoint(lines are drawn between them in the order that they were place)

    Press O to delete the last placed waypoint

    Press c to remove all placed waypoints

    Press P to convert all waypoint positions to TS instructions

</details>


## linestitcher
Does what the name suggests, it stitches multiple lines into one line

Put what you want stitched into linsti-in.txt, the output will be put in linsti-out.txt

The SEP variable at the top of the file is what is put between each line attached