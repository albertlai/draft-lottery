# draft-lottery
An easy way to perform a weighted draft lottery like the NBA. Odds are taken from the [Wikipedia page](https://en.wikipedia.org/wiki/NBA_draft_lottery#Process)

To run, simply make a text file that contains the standings of your league's teams in order of the previous year's standings, e.g.:

``standings.txt``  
Awesome First Place Team  
Not So Awesome Second Place  
Third's the Nerd  
Et Cetera  

Then call the script with 
``python lottery.py standings.txt``

If you want to just get the results all at once instead of one at a time, run:
``python lottery.py standings.txt --no_anim``

You'll then see the results!
