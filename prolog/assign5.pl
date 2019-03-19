% frome, over, to : describe moves
moves(0,1,3).
moves(0,2,5).
moves(1,3,6).
moves(1,4,8).
moves(2,4,7).
moves(2,5,9).
moves(3,6,10).
moves(3,7,12).
moves(4,7,11).
moves(4,8,13).
moves(5,8,12).
moves(5,9,14).
moves(3,4,5).
moves(6,7,8).
moves(7,8,9).
moves(10,11,12).
moves(11,12,13).
moves(12,13,14).

% generator for moves and their opposites
step(From,Over,To):-
    moves(From,Over,To);moves(To,Over,From).

% build cells
init(I,Board):-
    findall(J,(between(0,14,J),J=\=I),Board).

% performs, if possible, a move
% given the current occupancy of the cells  
move(moves(From,Over,To),Board1,[To|Board3]):-
    select(From,Board1,Board2),
    select(Over,Board2,Board3),
    step(From,Over,To),
    not(member(To,Board1)).
   
% all possible solutions given a cell configuration
solve([_],[]).
solve(Board1,[M|Moves]):-
    move(M,Board1,Board2),
    solve(Board2,Moves).
  
% replay a sequence of moves, showing the state of cells
replay([_],[]).
replay(Board1,[M|Moves]):-  
    move(M,Board1,Board2),
    !,
    show(Board2),
    replay(Board2,Moves).

% show the result by printing out successive states  
set(I,Board,X):-
    member(I,Board)->X=x ; X='.'.
  
show(Board):-
    Lines = [[4,0,0], [3,1,2], [2,3,5], [1,6,9], [0,10,14]],
    member(Line, Lines),
    [T, A, B] = Line,
    nl,
    tab(T),
    between(A,B,I),
    set(I,Board,X),
    write(X),
    write(' '),
    fail.

show(_):- nl.

% visualize a solution for each first 5 positions
% others look the same after 120 degrees rotation
go:-
    between(0, 4, I),
    init(I,Board),
    once(solve(Board,Moves)),
    J is (I + 1),
    write('=== '),
    write(J),
    write(' ==='),
    nl,
    show(Board),
    nl,
    replay(Board,Moves),
    nl,
    maplist(writeln, Moves).
