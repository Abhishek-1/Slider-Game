# Slider-Game

15 puzzle is a sliding puzzle game with numbered squares arranged in 4X4 grid with one tile missing.

The puzzle is solved when the numbers are arranged in order.

The actions are defined in terms of direction where empty square can be moved to UP (U), Down(D), Left(L), Right(R)

Input -  The input is given in form of sequence of numbered tiles for initial board configuration, ‘0’ indicating the empty space (see example below)
Output
1. Moves
2. Number of Nodes expanded
3. TIme Taken
4. Memory Used
Example
> 1 0 2 4 5 7 3 8 9 6 11 12 13 10 14 15
Moves: RDLDDRR
Number of Nodes expanded: 2642
TIme Taken: 42ms
Memory Used: 8624kb

Unsolvable puzzle - There can be some puzzle for which the solved state cannot be reached. If the solution doesn’t exist, the message 
“solution cannot be found” is displayed.
