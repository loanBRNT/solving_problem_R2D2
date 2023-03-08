set V := { 0..5 };
set E := { <i,j> in V*V with i < j };
set P [ ] := powerset(V);
set K := indexset(P);

param px [V] := read "../../Data/pb-etape5/tsp6.txt" as "1n" comment "#";
param py [V] := read "../../Data/pb-etape5/tsp6.txt" as "2n" comment "#";

defnumb dist(a,b) := sqrt((px[a]-px[b])^2 + (py[a]-py[b])^2) ;

var x[E] binary ;

minimize cost : sum <i,j> in E : dist(i,j) * x[i,j] ;

subto two_connected : forall <v> in V do
(sum <v,j> in E : x [v,j] ) + ( sum<i,v> in E : x [i,v] ) == 2;

subto no_subtour :
forall <k> in K with card(P[k]) > 2 and card(P[k]) < card(V) - 2 do
sum <i,j> in E with <i> in P[k] and <j> in P[k] : x [i,j]
<= card(P[k]) - 1;