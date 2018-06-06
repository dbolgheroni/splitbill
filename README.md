*spbill* is a command-line utility to split bills between a group.  It takes a csv file as input describing the bills and outputs a resume on who must receive and who must pay money.

The input should be in csv format like this:

    who,what,cost,between

An input example, a file called `bills.csv`:
  
    alice,beer,90,alice,bob,carol,dan
    bob,food,120,alice,bob,carol
    carol,gas,240,alice,bob
    erin,water,60,alice,bob,carol

Not paying attention to the correct format should halt the utility.

The first line says Alice paid a 90 dollars bill for beer, to be splitten between herself and her friends Bob, Carol and Dan.  The second line says Bob paid a 120 dollars bill for food, to be splitten between himself, Bob and Carol.  The third line says Carol paid a 60 dollars bill for gas, to be splitten between Alice and Bob, but not herself.  The fourth line says Erin paid a 60 dollars bill for water, to Alice, Bob and Carol, not herself.

Note that Dan appears on the first line, but he didn't pay anything at all.  Erin paid something, but didn't split anything else with the others.

Running *spbill* should give the following output:

    $ spbill bills.csv
    alice    -112.50
    bob      -82.50
    carol    157.50
    dan      -22.50
    erin     60.00
    $

At the end of the event, Alice is owing 112.50 dollars, Bob is owing 82.50 dollars and Dan is owing 22.50.  Carol and Erin paid most of the expenses, and each one should receive 157.50 dollars and 60.00 dollars, respectively.  It's up to you to decide who pays who.

Output to csv is also supported with `-o` flag.
