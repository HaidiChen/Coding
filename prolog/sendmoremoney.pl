go:-
  puzzle(Show,[0,1,2,3,4,5,6,7,8,9],_),
  Show,
  fail
; nl.

/*

    T E X A S +
  N E V A D A
---------------
  A L A S K A


*/

% problem specific code

puzzle(show(T,E,X,A,S,N,V,D,L,K))-->
  add_digits(S,A,A,  0,R1),
  add_digits(A,D,K, R1,R2),
  add_digits(X,A,S, R2,R3),
  add_digits(E,V,A, R3,R4),
  add_digits(T,E,L, R4,R5),
  add_digits(0,N,A, R5,0),
  {T>0,N>0,A>0}.

show(T,E,X,A,S,N,V,D,L,K):-
( write('  '),
  write([T,E,X,A,S]),
  write('+'),nl,
  write('  '),
  write([N,E,V,A,D,A]),
  write('='),nl,
  write([A,L,A,S,K,A]),nl,
  fail
; nl
).

% reusable code

digit(X)-->{integer(X)},!.
digit(X)-->sel(X).

add_digits(C1,C2,Res,R1,R2)-->
   digit(C1),
   digit(C2),
   digit(Res),
   {add_with_carry(C1,C2,R1, Res,R2)}.

add_with_carry(C1,C2,R1, Res,R2):-
    S is (C1+C2)+R1,
    Res is S mod 10,
    R2 is S // 10.

sel(X,[X|Xs],Xs).
sel(X,[Y|Xs],[Y|Ys]):-sel(X,Xs,Ys).

