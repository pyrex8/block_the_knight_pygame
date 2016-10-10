#! /usr/bin/env python
""" pyweek 22 entry 'You can't let him in here.""" 

__author__ = "Rex Allison"
__copyright__ = "Copyright 2016, Rex Allison"
__license__ = "MIT"


level = [

# level 1
 '........................................'
,'........................................'
,'....................X...................'
,'....................X...................'
,'....................X...................'
,'....................X...................'

# level 2
,'................................X.......'
,'................................X.......'
,'................X...............X.......'
,'................X...............X.......'
,'................X.......................'
,'................X.......................'

# level 3
,'............................X...........'
,'............................X...........'
,'............X...............X...........'
,'............X...............X...........'
,'............X...........................'
,'............X...........................'

# level 4
,'...XXXXX............XXXXX...............'
,'....XXX..............XXX................'
,'.....X................X.................'
,'.............X.................X........'
,'............XXX...............XXX.......'
,'...........XXXXX.............XXXXX......'

# level 5
,'..XXXXXXX..........XXXXXXX..............'
,'...XXXXX............XXXXX...............'
,'....XXX......X.......XXX.......X........'
,'.....X......XXX.......X.......XXX.......'
,'...........XXXXX.............XXXXX......'
,'..........XXXXXXX...........XXXXXXX.....'

# level 6
,'.XXXXXXXXX........XXXXXXXXX.............'
,'..XXXXXXX....X.....XXXXXXX.....X........'
,'...XXXXX....XXX.....XXXXX.....XXX.......'
,'....XXX....XXXXX.....XXX.....XXXXX......'
,'.....X....XXXXXXX.....X.....XXXXXXX.....'
,'.........XXXXXXXXX.........XXXXXXXXX....'

# level 7
,'.XXXXXXXXX........XXXXXXXXX.............'
,'........................................'
,'........................................'
,'........................................'
,'........................................'
,'.........XXXXXXXXX.........XXXXXXXXX....'

# level 8
,'XXXXXXXXXXX......XXXXXXXXXXX............'
,'........................................'
,'........................................'
,'........................................'
,'........................................'
,'........XXXXXXXXXXX.......XXXXXXXXXXX...'

# level 9
,'......................XXXXXX............'
,'.........XXXXXX.......XXXXXX............'
,'.........XXXXXX.......XXXXXX............'
,'.........XXXXXX.......XXXXXX............'
,'.........XXXXXX.......XXXXXX............'
,'.........XXXXXX.........................'

# level 10
,'XXXXXX....................XXXXXX........'
,'XXXXXX.......XXXXXX.......XXXXXX........'
,'XXXXXX.......XXXXXX.......XXXXXX........'
,'XXXXXX.......XXXXXX.......XXXXXX........'
,'XXXXXX.......XXXXXX.......XXXXXX........'
,'.............XXXXXX.....................'

# level 11
,'........................X...............'
,'........................X...............'
,'................X.......X...............'
,'................X.......X...............'
,'................X.......................'
,'................X.......................'

# level 12
,'......................X.................'
,'......................X.................'
,'.................X....X.................'
,'.................X....X.................'
,'.................X......................'
,'.................X......................'

# level 13
,'..................X.....................'
,'..................X.....................'
,'..........X.......X.......X.............'
,'..........X.......X.......X.............'
,'..........X...............X.............'
,'..........X...............X.............'

# level 14
,'..............X...........X.............'
,'..............X...........X.............'
,'........................................'
,'........................................'
,'..............X...........X.............'
,'..............X...........X.............'

# level 15
,'....................X...................'
,'....................X...................'
,'...........X..................X.........'
,'...........X..................X.........'
,'...........X........X.........X.........'
,'...........X........X.........X.........'

# level 16
,'....................X........X..........'
,'....................X........X..........'
,'...........X............................'
,'...........X............................'
,'...........X........X........X..........'
,'...........X........X........X..........'

# level 17
,'..................X...X.................'
,'......................X.................'
,'..............X.......X.................'
,'..............X...X...X.................'
,'..............X...X.....................'
,'..............X...X.....................'

# level 18
,'....X.............X.....................'
,'....X...................................'
,'....X...................................'
,'..................X.....................'
,'..................X.....................'
,'....X.............X.....................'

# level 19
,'.... .............X................X....'
,'.... ..............................X....'
,'.... ..............................X....'
,'..................X.....................'
,'..................X.....................'
,'.... .............X................X....'

# level 20
,'...................X................X...'
,'..........X........X........X.......X...'
,'..........X........X........X.......X...'
,'..........X........X........X.......X...'
,'..........X........X........X...........'
,'..........X.................X...........'

# level 21
,'.........X.......X.......X.......X......'
,'.........X.......X.......X.......X......'
,'........................................'
,'........................................'
,'.........X.......X.......X.......X......'
,'.........X.......X.......X.......X......'

# level 22
,'...........XX........XX.................'
,'.....................XX.................'
,'........................................'
,'........................................'
,'...........XX...........................'
,'...........XX........XX.................'

# level 23
,'....................X..........X........'
,'........................................'
,'........................................'
,'........................................'
,'........................................'
,'..........X..............X..............'

# level 24
,'.............X.................X........'
,'........................................'
,'........................................'
,'........................................'
,'........................................'
,'.......X........X........X........X.....'

# level 25
,'...................X................X...'
,'..........X.................X...........'
,'........................................'
,'....................................X...'
,'...................X....................'
,'..........X.................X...........'

# level 26
,'...X...................X................'
,'...X...................X................'
,'XXXXXXX.............XXXXXXX.............'
,'..........XXXXXXX.............XXXXXXX...'
,'.............X...................X......'
,'.............X...................X......'

# level 27
,'...X...................X................'
,'...X...................X................'
,'..XXX.......XXX.......XXX.......XXX.....'
,'..XXX.......XXX.......XXX.......XXX.....'
,'.............X...................X......'
,'.............X...................X......'

# level 28
,'...X...................X................'
,'...X...................X................'
,'.XXXXX.....XXXXX.....XXXXX.....XXXXX....'
,'.XXXXX.....XXXXX.....XXXXX.....XXXXX....'
,'.............X...................X......'
,'.............X...................X......'

# level 29
,'XXX..............................X......'
,'X.XXXXX.....X.X.X....X.X.X......X.......'
,'XXX.X.X.....XXXXX....XXXXX.....XXXXXXX..'
,'............XXXXXXXXXXXXXX......X.......'
,'..............XXXX..XXXX.........X......'
,'..............XXXX..XXXX................'

# level 30
,'........................................'
,'............X.X.X....X.X.X..............'
,'............XXXXX....XXXXX..............'
,'............XXXXXXXXXXXXXX..............'
,'..............XXXX..XXXX................'
,'..............XXXX..XXXX................'

       ]

