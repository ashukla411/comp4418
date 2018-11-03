v(1..6).
e(1, 2). e(1, 3). e(1, 4).
e(2, 1). e(2, 4). e(2, 5). e(2, 6).
e(3, 1). e(3, 4). e(3, 5). e(3, 6).
e(4, 1). e(4, 2). e(4, 3). e(4, 5).
e(5, 2). e(5, 3). e(5, 4). e(5, 6).
e(6, 2). e(6, 3). e(6, 5).

%since a clique is a subset of vertices V. C  V
k {c(X) : v(X)} k.
%unary predicate c, unary predicate v and binary predicate e
%x 2 C and y 2 C, if x 6= y, then fx; yg 2 E literal conversion to clingo
:- c(X), c(Y), X!=Y, v(X), v(Y), not  e(X,Y), not e(Y,X).

#show clique_are.