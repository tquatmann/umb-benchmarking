# Log files for prism_from-prism_check_default on model [egl.10-8](../../models/egl.10-8)

Parsed values: `[3.582, 2.227, 2.234, 3.535, 2.306]`



### Log file: prism_from-prism_check_default_egl.10-8_rep1.log

```
Command(s):
../bin/prism  models/egl.10-8/model.prism models/egl.10-8/property.props
Wallclock time: 479.154 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:18:42 GMT+01:00 2026
Hostname: r23m0140.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/egl.10-8/model.prism models/egl.10-8/property.props

Parsing PRISM model file "models/egl.10-8/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Parsing properties file "models/egl.10-8/property.props"...

1 property:
(1) "unfairA": P=? [ F !"knowA"&"knowB" ]

---------------------------------------------------------------------

Model checking: "unfairA": P=? [ F !"knowA"&"knowB" ]

Building model (engine:symbolic)...

Warning: Guard for command 11 of module "partyA" is never satisfied.

Warning: Guard for command 12 of module "partyA" is never satisfied.

Warning: Guard for command 13 of module "partyA" is never satisfied.

Warning: Guard for command 14 of module "partyA" is never satisfied.

Warning: Guard for command 15 of module "partyA" is never satisfied.

Warning: Guard for command 16 of module "partyA" is never satisfied.

Warning: Guard for command 17 of module "partyA" is never satisfied.

Warning: Guard for command 18 of module "partyA" is never satisfied.

Warning: Guard for command 19 of module "partyA" is never satisfied.

Warning: Guard for command 20 of module "partyA" is never satisfied.

Warning: Guard for command 31 of module "partyA" is never satisfied.

Warning: Guard for command 32 of module "partyA" is never satisfied.

Warning: Guard for command 33 of module "partyA" is never satisfied.

Warning: Guard for command 34 of module "partyA" is never satisfied.

Warning: Guard for command 35 of module "partyA" is never satisfied.

Warning: Guard for command 36 of module "partyA" is never satisfied.

Warning: Guard for command 37 of module "partyA" is never satisfied.

Warning: Guard for command 38 of module "partyA" is never satisfied.

Warning: Guard for command 39 of module "partyA" is never satisfied.

Warning: Guard for command 40 of module "partyA" is never satisfied.

Warning: Guard for command 51 of module "partyA" is never satisfied.

Warning: Guard for command 52 of module "partyA" is never satisfied.

Warning: Guard for command 53 of module "partyA" is never satisfied.

Warning: Guard for command 54 of module "partyA" is never satisfied.

Warning: Guard for command 55 of module "partyA" is never satisfied.

Warning: Guard for command 56 of module "partyA" is never satisfied.

Warning: Guard for command 57 of module "partyA" is never satisfied.

Warning: Guard for command 58 of module "partyA" is never satisfied.

Warning: Guard for command 59 of module "partyA" is never satisfied.

Warning: Guard for command 60 of module "partyA" is never satisfied.

Warning: Guard for command 11 of module "partyB" is never satisfied.

Warning: Guard for command 12 of module "partyB" is never satisfied.

Warning: Guard for command 13 of module "partyB" is never satisfied.

Warning: Guard for command 14 of module "partyB" is never satisfied.

Warning: Guard for command 15 of module "partyB" is never satisfied.

Warning: Guard for command 16 of module "partyB" is never satisfied.

Warning: Guard for command 17 of module "partyB" is never satisfied.

Warning: Guard for command 18 of module "partyB" is never satisfied.

Warning: Guard for command 19 of module "partyB" is never satisfied.

Warning: Guard for command 20 of module "partyB" is never satisfied.

Warning: Guard for command 31 of module "partyB" is never satisfied.

Warning: Guard for command 32 of module "partyB" is never satisfied.

Warning: Guard for command 33 of module "partyB" is never satisfied.

Warning: Guard for command 34 of module "partyB" is never satisfied.

Warning: Guard for command 35 of module "partyB" is never satisfied.

Warning: Guard for command 36 of module "partyB" is never satisfied.

Warning: Guard for command 37 of module "partyB" is never satisfied.

Warning: Guard for command 38 of module "partyB" is never satisfied.

Warning: Guard for command 39 of module "partyB" is never satisfied.

Warning: Guard for command 40 of module "partyB" is never satisfied.

Warning: Guard for command 51 of module "partyB" is never satisfied.

Warning: Guard for command 52 of module "partyB" is never satisfied.

Warning: Guard for command 53 of module "partyB" is never satisfied.

Warning: Guard for command 54 of module "partyB" is never satisfied.

Warning: Guard for command 55 of module "partyB" is never satisfied.

Warning: Guard for command 56 of module "partyB" is never satisfied.

Warning: Guard for command 57 of module "partyB" is never satisfied.

Warning: Guard for command 58 of module "partyB" is never satisfied.

Warning: Guard for command 59 of module "partyB" is never satisfied.

Warning: Guard for command 60 of module "partyB" is never satisfied.

Computing reachable states...

Reachability (BFS): 341 iterations in 3.06 seconds (average 0.008974, setup 0.00)

Time for model construction: 3.582 seconds.

Type:        DTMC
States:      317718526 (1 initial)
Transitions: 318767101

Transition matrix: 120213 nodes (3 terminal), 318767101 minterms, vars: 331r/331c

Prob0: 303 iterations in 6.78 seconds (average 0.022376, setup 0.00)

Prob1: 3 iterations in 0.21 seconds (average 0.070000, setup 0.00)

yes = 75727871, no = 241989120, maybe = 1535

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=331, nodes=9297] [435.8 KB]
Adding explicit sparse matrices... [levels=319, num=21, compact] [524.0 KB]
Creating vector for diagonals... [dist=1, compact] [606.0 MB]
Creating vector for RHS... [dist=2, compact] [606.0 MB]
Allocating iteration vectors... [2 x 2.4 GB]
TOTAL: [5.9 GB]

Starting iterations...
Iteration 4: max relative diff=inf, 5.76 sec so far
Iteration 8: max relative diff=inf, 11.37 sec so far
Iteration 12: max relative diff=inf, 17.00 sec so far
Iteration 16: max relative diff=inf, 22.64 sec so far
Iteration 20: max relative diff=0.000977, 28.27 sec so far

Jacobi: 21 iterations in 465.52 seconds (average 1.413333, setup 435.84)

Value in the initial state: 0.50048828125

Time for model checking: 474.95 seconds.

Result: 0.50048828125 (exact floating point)

---------------------------------------------------------------------

Note: There were 60 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_egl.10-8_rep2.log

```
Command(s):
../bin/prism  models/egl.10-8/model.prism models/egl.10-8/property.props
Wallclock time: 465.089 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:56 GMT+01:00 2026
Hostname: n23m0406.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/egl.10-8/model.prism models/egl.10-8/property.props

Parsing PRISM model file "models/egl.10-8/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Parsing properties file "models/egl.10-8/property.props"...

1 property:
(1) "unfairA": P=? [ F !"knowA"&"knowB" ]

---------------------------------------------------------------------

Model checking: "unfairA": P=? [ F !"knowA"&"knowB" ]

Building model (engine:symbolic)...

Warning: Guard for command 11 of module "partyA" is never satisfied.

Warning: Guard for command 12 of module "partyA" is never satisfied.

Warning: Guard for command 13 of module "partyA" is never satisfied.

Warning: Guard for command 14 of module "partyA" is never satisfied.

Warning: Guard for command 15 of module "partyA" is never satisfied.

Warning: Guard for command 16 of module "partyA" is never satisfied.

Warning: Guard for command 17 of module "partyA" is never satisfied.

Warning: Guard for command 18 of module "partyA" is never satisfied.

Warning: Guard for command 19 of module "partyA" is never satisfied.

Warning: Guard for command 20 of module "partyA" is never satisfied.

Warning: Guard for command 31 of module "partyA" is never satisfied.

Warning: Guard for command 32 of module "partyA" is never satisfied.

Warning: Guard for command 33 of module "partyA" is never satisfied.

Warning: Guard for command 34 of module "partyA" is never satisfied.

Warning: Guard for command 35 of module "partyA" is never satisfied.

Warning: Guard for command 36 of module "partyA" is never satisfied.

Warning: Guard for command 37 of module "partyA" is never satisfied.

Warning: Guard for command 38 of module "partyA" is never satisfied.

Warning: Guard for command 39 of module "partyA" is never satisfied.

Warning: Guard for command 40 of module "partyA" is never satisfied.

Warning: Guard for command 51 of module "partyA" is never satisfied.

Warning: Guard for command 52 of module "partyA" is never satisfied.

Warning: Guard for command 53 of module "partyA" is never satisfied.

Warning: Guard for command 54 of module "partyA" is never satisfied.

Warning: Guard for command 55 of module "partyA" is never satisfied.

Warning: Guard for command 56 of module "partyA" is never satisfied.

Warning: Guard for command 57 of module "partyA" is never satisfied.

Warning: Guard for command 58 of module "partyA" is never satisfied.

Warning: Guard for command 59 of module "partyA" is never satisfied.

Warning: Guard for command 60 of module "partyA" is never satisfied.

Warning: Guard for command 11 of module "partyB" is never satisfied.

Warning: Guard for command 12 of module "partyB" is never satisfied.

Warning: Guard for command 13 of module "partyB" is never satisfied.

Warning: Guard for command 14 of module "partyB" is never satisfied.

Warning: Guard for command 15 of module "partyB" is never satisfied.

Warning: Guard for command 16 of module "partyB" is never satisfied.

Warning: Guard for command 17 of module "partyB" is never satisfied.

Warning: Guard for command 18 of module "partyB" is never satisfied.

Warning: Guard for command 19 of module "partyB" is never satisfied.

Warning: Guard for command 20 of module "partyB" is never satisfied.

Warning: Guard for command 31 of module "partyB" is never satisfied.

Warning: Guard for command 32 of module "partyB" is never satisfied.

Warning: Guard for command 33 of module "partyB" is never satisfied.

Warning: Guard for command 34 of module "partyB" is never satisfied.

Warning: Guard for command 35 of module "partyB" is never satisfied.

Warning: Guard for command 36 of module "partyB" is never satisfied.

Warning: Guard for command 37 of module "partyB" is never satisfied.

Warning: Guard for command 38 of module "partyB" is never satisfied.

Warning: Guard for command 39 of module "partyB" is never satisfied.

Warning: Guard for command 40 of module "partyB" is never satisfied.

Warning: Guard for command 51 of module "partyB" is never satisfied.

Warning: Guard for command 52 of module "partyB" is never satisfied.

Warning: Guard for command 53 of module "partyB" is never satisfied.

Warning: Guard for command 54 of module "partyB" is never satisfied.

Warning: Guard for command 55 of module "partyB" is never satisfied.

Warning: Guard for command 56 of module "partyB" is never satisfied.

Warning: Guard for command 57 of module "partyB" is never satisfied.

Warning: Guard for command 58 of module "partyB" is never satisfied.

Warning: Guard for command 59 of module "partyB" is never satisfied.

Warning: Guard for command 60 of module "partyB" is never satisfied.

Computing reachable states...

Reachability (BFS): 341 iterations in 1.83 seconds (average 0.005367, setup 0.00)

Time for model construction: 2.227 seconds.

Type:        DTMC
States:      317718526 (1 initial)
Transitions: 318767101

Transition matrix: 120213 nodes (3 terminal), 318767101 minterms, vars: 331r/331c

Prob0: 303 iterations in 4.04 seconds (average 0.013333, setup 0.00)

Prob1: 3 iterations in 0.15 seconds (average 0.050000, setup 0.00)

yes = 75727871, no = 241989120, maybe = 1535

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=331, nodes=9297] [435.8 KB]
Adding explicit sparse matrices... [levels=319, num=21, compact] [524.0 KB]
Creating vector for diagonals... [dist=1, compact] [606.0 MB]
Creating vector for RHS... [dist=2, compact] [606.0 MB]
Allocating iteration vectors... [2 x 2.4 GB]
TOTAL: [5.9 GB]

Starting iterations...
Iteration 4: max relative diff=inf, 5.76 sec so far
Iteration 8: max relative diff=inf, 11.37 sec so far
Iteration 12: max relative diff=inf, 16.97 sec so far
Iteration 16: max relative diff=inf, 22.57 sec so far
Iteration 20: max relative diff=0.000977, 28.16 sec so far

Jacobi: 21 iterations in 456.20 seconds (average 1.407619, setup 426.64)

Value in the initial state: 0.50048828125

Time for model checking: 462.171 seconds.

Result: 0.50048828125 (exact floating point)

---------------------------------------------------------------------

Note: There were 60 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_egl.10-8_rep3.log

```
Command(s):
../bin/prism  models/egl.10-8/model.prism models/egl.10-8/property.props
Wallclock time: 479.400 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:05 GMT+01:00 2026
Hostname: r23m0159.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/egl.10-8/model.prism models/egl.10-8/property.props

Parsing PRISM model file "models/egl.10-8/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Parsing properties file "models/egl.10-8/property.props"...

1 property:
(1) "unfairA": P=? [ F !"knowA"&"knowB" ]

---------------------------------------------------------------------

Model checking: "unfairA": P=? [ F !"knowA"&"knowB" ]

Building model (engine:symbolic)...

Warning: Guard for command 11 of module "partyA" is never satisfied.

Warning: Guard for command 12 of module "partyA" is never satisfied.

Warning: Guard for command 13 of module "partyA" is never satisfied.

Warning: Guard for command 14 of module "partyA" is never satisfied.

Warning: Guard for command 15 of module "partyA" is never satisfied.

Warning: Guard for command 16 of module "partyA" is never satisfied.

Warning: Guard for command 17 of module "partyA" is never satisfied.

Warning: Guard for command 18 of module "partyA" is never satisfied.

Warning: Guard for command 19 of module "partyA" is never satisfied.

Warning: Guard for command 20 of module "partyA" is never satisfied.

Warning: Guard for command 31 of module "partyA" is never satisfied.

Warning: Guard for command 32 of module "partyA" is never satisfied.

Warning: Guard for command 33 of module "partyA" is never satisfied.

Warning: Guard for command 34 of module "partyA" is never satisfied.

Warning: Guard for command 35 of module "partyA" is never satisfied.

Warning: Guard for command 36 of module "partyA" is never satisfied.

Warning: Guard for command 37 of module "partyA" is never satisfied.

Warning: Guard for command 38 of module "partyA" is never satisfied.

Warning: Guard for command 39 of module "partyA" is never satisfied.

Warning: Guard for command 40 of module "partyA" is never satisfied.

Warning: Guard for command 51 of module "partyA" is never satisfied.

Warning: Guard for command 52 of module "partyA" is never satisfied.

Warning: Guard for command 53 of module "partyA" is never satisfied.

Warning: Guard for command 54 of module "partyA" is never satisfied.

Warning: Guard for command 55 of module "partyA" is never satisfied.

Warning: Guard for command 56 of module "partyA" is never satisfied.

Warning: Guard for command 57 of module "partyA" is never satisfied.

Warning: Guard for command 58 of module "partyA" is never satisfied.

Warning: Guard for command 59 of module "partyA" is never satisfied.

Warning: Guard for command 60 of module "partyA" is never satisfied.

Warning: Guard for command 11 of module "partyB" is never satisfied.

Warning: Guard for command 12 of module "partyB" is never satisfied.

Warning: Guard for command 13 of module "partyB" is never satisfied.

Warning: Guard for command 14 of module "partyB" is never satisfied.

Warning: Guard for command 15 of module "partyB" is never satisfied.

Warning: Guard for command 16 of module "partyB" is never satisfied.

Warning: Guard for command 17 of module "partyB" is never satisfied.

Warning: Guard for command 18 of module "partyB" is never satisfied.

Warning: Guard for command 19 of module "partyB" is never satisfied.

Warning: Guard for command 20 of module "partyB" is never satisfied.

Warning: Guard for command 31 of module "partyB" is never satisfied.

Warning: Guard for command 32 of module "partyB" is never satisfied.

Warning: Guard for command 33 of module "partyB" is never satisfied.

Warning: Guard for command 34 of module "partyB" is never satisfied.

Warning: Guard for command 35 of module "partyB" is never satisfied.

Warning: Guard for command 36 of module "partyB" is never satisfied.

Warning: Guard for command 37 of module "partyB" is never satisfied.

Warning: Guard for command 38 of module "partyB" is never satisfied.

Warning: Guard for command 39 of module "partyB" is never satisfied.

Warning: Guard for command 40 of module "partyB" is never satisfied.

Warning: Guard for command 51 of module "partyB" is never satisfied.

Warning: Guard for command 52 of module "partyB" is never satisfied.

Warning: Guard for command 53 of module "partyB" is never satisfied.

Warning: Guard for command 54 of module "partyB" is never satisfied.

Warning: Guard for command 55 of module "partyB" is never satisfied.

Warning: Guard for command 56 of module "partyB" is never satisfied.

Warning: Guard for command 57 of module "partyB" is never satisfied.

Warning: Guard for command 58 of module "partyB" is never satisfied.

Warning: Guard for command 59 of module "partyB" is never satisfied.

Warning: Guard for command 60 of module "partyB" is never satisfied.

Computing reachable states...

Reachability (BFS): 341 iterations in 1.82 seconds (average 0.005337, setup 0.00)

Time for model construction: 2.234 seconds.

Type:        DTMC
States:      317718526 (1 initial)
Transitions: 318767101

Transition matrix: 120213 nodes (3 terminal), 318767101 minterms, vars: 331r/331c

Prob0: 303 iterations in 4.28 seconds (average 0.014125, setup 0.00)

Prob1: 3 iterations in 0.16 seconds (average 0.053333, setup 0.00)

yes = 75727871, no = 241989120, maybe = 1535

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=331, nodes=9297] [435.8 KB]
Adding explicit sparse matrices... [levels=319, num=21, compact] [524.0 KB]
Creating vector for diagonals... [dist=1, compact] [606.0 MB]
Creating vector for RHS... [dist=2, compact] [606.0 MB]
Allocating iteration vectors... [2 x 2.4 GB]
TOTAL: [5.9 GB]

Starting iterations...
Iteration 4: max relative diff=inf, 5.46 sec so far
Iteration 8: max relative diff=inf, 10.68 sec so far
Iteration 12: max relative diff=inf, 15.99 sec so far
Iteration 16: max relative diff=inf, 21.19 sec so far
Iteration 20: max relative diff=0.000977, 26.56 sec so far

Jacobi: 21 iterations in 469.48 seconds (average 1.326190, setup 441.63)

Value in the initial state: 0.50048828125

Time for model checking: 475.983 seconds.

Result: 0.50048828125 (exact floating point)

---------------------------------------------------------------------

Note: There were 60 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_egl.10-8_rep4.log

```
Command(s):
../bin/prism  models/egl.10-8/model.prism models/egl.10-8/property.props
Wallclock time: 459.191 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:11:42 GMT+01:00 2026
Hostname: n23m0319.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/egl.10-8/model.prism models/egl.10-8/property.props

Parsing PRISM model file "models/egl.10-8/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Parsing properties file "models/egl.10-8/property.props"...

1 property:
(1) "unfairA": P=? [ F !"knowA"&"knowB" ]

---------------------------------------------------------------------

Model checking: "unfairA": P=? [ F !"knowA"&"knowB" ]

Building model (engine:symbolic)...

Warning: Guard for command 11 of module "partyA" is never satisfied.

Warning: Guard for command 12 of module "partyA" is never satisfied.

Warning: Guard for command 13 of module "partyA" is never satisfied.

Warning: Guard for command 14 of module "partyA" is never satisfied.

Warning: Guard for command 15 of module "partyA" is never satisfied.

Warning: Guard for command 16 of module "partyA" is never satisfied.

Warning: Guard for command 17 of module "partyA" is never satisfied.

Warning: Guard for command 18 of module "partyA" is never satisfied.

Warning: Guard for command 19 of module "partyA" is never satisfied.

Warning: Guard for command 20 of module "partyA" is never satisfied.

Warning: Guard for command 31 of module "partyA" is never satisfied.

Warning: Guard for command 32 of module "partyA" is never satisfied.

Warning: Guard for command 33 of module "partyA" is never satisfied.

Warning: Guard for command 34 of module "partyA" is never satisfied.

Warning: Guard for command 35 of module "partyA" is never satisfied.

Warning: Guard for command 36 of module "partyA" is never satisfied.

Warning: Guard for command 37 of module "partyA" is never satisfied.

Warning: Guard for command 38 of module "partyA" is never satisfied.

Warning: Guard for command 39 of module "partyA" is never satisfied.

Warning: Guard for command 40 of module "partyA" is never satisfied.

Warning: Guard for command 51 of module "partyA" is never satisfied.

Warning: Guard for command 52 of module "partyA" is never satisfied.

Warning: Guard for command 53 of module "partyA" is never satisfied.

Warning: Guard for command 54 of module "partyA" is never satisfied.

Warning: Guard for command 55 of module "partyA" is never satisfied.

Warning: Guard for command 56 of module "partyA" is never satisfied.

Warning: Guard for command 57 of module "partyA" is never satisfied.

Warning: Guard for command 58 of module "partyA" is never satisfied.

Warning: Guard for command 59 of module "partyA" is never satisfied.

Warning: Guard for command 60 of module "partyA" is never satisfied.

Warning: Guard for command 11 of module "partyB" is never satisfied.

Warning: Guard for command 12 of module "partyB" is never satisfied.

Warning: Guard for command 13 of module "partyB" is never satisfied.

Warning: Guard for command 14 of module "partyB" is never satisfied.

Warning: Guard for command 15 of module "partyB" is never satisfied.

Warning: Guard for command 16 of module "partyB" is never satisfied.

Warning: Guard for command 17 of module "partyB" is never satisfied.

Warning: Guard for command 18 of module "partyB" is never satisfied.

Warning: Guard for command 19 of module "partyB" is never satisfied.

Warning: Guard for command 20 of module "partyB" is never satisfied.

Warning: Guard for command 31 of module "partyB" is never satisfied.

Warning: Guard for command 32 of module "partyB" is never satisfied.

Warning: Guard for command 33 of module "partyB" is never satisfied.

Warning: Guard for command 34 of module "partyB" is never satisfied.

Warning: Guard for command 35 of module "partyB" is never satisfied.

Warning: Guard for command 36 of module "partyB" is never satisfied.

Warning: Guard for command 37 of module "partyB" is never satisfied.

Warning: Guard for command 38 of module "partyB" is never satisfied.

Warning: Guard for command 39 of module "partyB" is never satisfied.

Warning: Guard for command 40 of module "partyB" is never satisfied.

Warning: Guard for command 51 of module "partyB" is never satisfied.

Warning: Guard for command 52 of module "partyB" is never satisfied.

Warning: Guard for command 53 of module "partyB" is never satisfied.

Warning: Guard for command 54 of module "partyB" is never satisfied.

Warning: Guard for command 55 of module "partyB" is never satisfied.

Warning: Guard for command 56 of module "partyB" is never satisfied.

Warning: Guard for command 57 of module "partyB" is never satisfied.

Warning: Guard for command 58 of module "partyB" is never satisfied.

Warning: Guard for command 59 of module "partyB" is never satisfied.

Warning: Guard for command 60 of module "partyB" is never satisfied.

Computing reachable states...

Reachability (BFS): 341 iterations in 2.94 seconds (average 0.008622, setup 0.00)

Time for model construction: 3.535 seconds.

Type:        DTMC
States:      317718526 (1 initial)
Transitions: 318767101

Transition matrix: 120213 nodes (3 terminal), 318767101 minterms, vars: 331r/331c

Prob0: 303 iterations in 6.67 seconds (average 0.022013, setup 0.00)

Prob1: 3 iterations in 0.21 seconds (average 0.070000, setup 0.00)

yes = 75727871, no = 241989120, maybe = 1535

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=331, nodes=9297] [435.8 KB]
Adding explicit sparse matrices... [levels=319, num=21, compact] [524.0 KB]
Creating vector for diagonals... [dist=1, compact] [606.0 MB]
Creating vector for RHS... [dist=2, compact] [606.0 MB]
Allocating iteration vectors... [2 x 2.4 GB]
TOTAL: [5.9 GB]

Starting iterations...
Iteration 4: max relative diff=inf, 5.72 sec so far
Iteration 8: max relative diff=inf, 11.32 sec so far
Iteration 12: max relative diff=inf, 16.91 sec so far
Iteration 16: max relative diff=inf, 22.49 sec so far
Iteration 20: max relative diff=0.000977, 28.06 sec so far

Jacobi: 21 iterations in 445.91 seconds (average 1.402381, setup 416.46)

Value in the initial state: 0.50048828125

Time for model checking: 454.992 seconds.

Result: 0.50048828125 (exact floating point)

---------------------------------------------------------------------

Note: There were 60 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_egl.10-8_rep5.log

```
Command(s):
../bin/prism  models/egl.10-8/model.prism models/egl.10-8/property.props
Wallclock time: 448.545 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 02:57:56 GMT+01:00 2026
Hostname: n23m0022.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/egl.10-8/model.prism models/egl.10-8/property.props

Parsing PRISM model file "models/egl.10-8/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Parsing properties file "models/egl.10-8/property.props"...

1 property:
(1) "unfairA": P=? [ F !"knowA"&"knowB" ]

---------------------------------------------------------------------

Model checking: "unfairA": P=? [ F !"knowA"&"knowB" ]

Building model (engine:symbolic)...

Warning: Guard for command 11 of module "partyA" is never satisfied.

Warning: Guard for command 12 of module "partyA" is never satisfied.

Warning: Guard for command 13 of module "partyA" is never satisfied.

Warning: Guard for command 14 of module "partyA" is never satisfied.

Warning: Guard for command 15 of module "partyA" is never satisfied.

Warning: Guard for command 16 of module "partyA" is never satisfied.

Warning: Guard for command 17 of module "partyA" is never satisfied.

Warning: Guard for command 18 of module "partyA" is never satisfied.

Warning: Guard for command 19 of module "partyA" is never satisfied.

Warning: Guard for command 20 of module "partyA" is never satisfied.

Warning: Guard for command 31 of module "partyA" is never satisfied.

Warning: Guard for command 32 of module "partyA" is never satisfied.

Warning: Guard for command 33 of module "partyA" is never satisfied.

Warning: Guard for command 34 of module "partyA" is never satisfied.

Warning: Guard for command 35 of module "partyA" is never satisfied.

Warning: Guard for command 36 of module "partyA" is never satisfied.

Warning: Guard for command 37 of module "partyA" is never satisfied.

Warning: Guard for command 38 of module "partyA" is never satisfied.

Warning: Guard for command 39 of module "partyA" is never satisfied.

Warning: Guard for command 40 of module "partyA" is never satisfied.

Warning: Guard for command 51 of module "partyA" is never satisfied.

Warning: Guard for command 52 of module "partyA" is never satisfied.

Warning: Guard for command 53 of module "partyA" is never satisfied.

Warning: Guard for command 54 of module "partyA" is never satisfied.

Warning: Guard for command 55 of module "partyA" is never satisfied.

Warning: Guard for command 56 of module "partyA" is never satisfied.

Warning: Guard for command 57 of module "partyA" is never satisfied.

Warning: Guard for command 58 of module "partyA" is never satisfied.

Warning: Guard for command 59 of module "partyA" is never satisfied.

Warning: Guard for command 60 of module "partyA" is never satisfied.

Warning: Guard for command 11 of module "partyB" is never satisfied.

Warning: Guard for command 12 of module "partyB" is never satisfied.

Warning: Guard for command 13 of module "partyB" is never satisfied.

Warning: Guard for command 14 of module "partyB" is never satisfied.

Warning: Guard for command 15 of module "partyB" is never satisfied.

Warning: Guard for command 16 of module "partyB" is never satisfied.

Warning: Guard for command 17 of module "partyB" is never satisfied.

Warning: Guard for command 18 of module "partyB" is never satisfied.

Warning: Guard for command 19 of module "partyB" is never satisfied.

Warning: Guard for command 20 of module "partyB" is never satisfied.

Warning: Guard for command 31 of module "partyB" is never satisfied.

Warning: Guard for command 32 of module "partyB" is never satisfied.

Warning: Guard for command 33 of module "partyB" is never satisfied.

Warning: Guard for command 34 of module "partyB" is never satisfied.

Warning: Guard for command 35 of module "partyB" is never satisfied.

Warning: Guard for command 36 of module "partyB" is never satisfied.

Warning: Guard for command 37 of module "partyB" is never satisfied.

Warning: Guard for command 38 of module "partyB" is never satisfied.

Warning: Guard for command 39 of module "partyB" is never satisfied.

Warning: Guard for command 40 of module "partyB" is never satisfied.

Warning: Guard for command 51 of module "partyB" is never satisfied.

Warning: Guard for command 52 of module "partyB" is never satisfied.

Warning: Guard for command 53 of module "partyB" is never satisfied.

Warning: Guard for command 54 of module "partyB" is never satisfied.

Warning: Guard for command 55 of module "partyB" is never satisfied.

Warning: Guard for command 56 of module "partyB" is never satisfied.

Warning: Guard for command 57 of module "partyB" is never satisfied.

Warning: Guard for command 58 of module "partyB" is never satisfied.

Warning: Guard for command 59 of module "partyB" is never satisfied.

Warning: Guard for command 60 of module "partyB" is never satisfied.

Computing reachable states...

Reachability (BFS): 341 iterations in 1.82 seconds (average 0.005337, setup 0.00)

Time for model construction: 2.306 seconds.

Type:        DTMC
States:      317718526 (1 initial)
Transitions: 318767101

Transition matrix: 120213 nodes (3 terminal), 318767101 minterms, vars: 331r/331c

Prob0: 303 iterations in 4.09 seconds (average 0.013498, setup 0.00)

Prob1: 3 iterations in 0.16 seconds (average 0.053333, setup 0.00)

yes = 75727871, no = 241989120, maybe = 1535

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=331, nodes=9297] [435.8 KB]
Adding explicit sparse matrices... [levels=319, num=21, compact] [524.0 KB]
Creating vector for diagonals... [dist=1, compact] [606.0 MB]
Creating vector for RHS... [dist=2, compact] [606.0 MB]
Allocating iteration vectors... [2 x 2.4 GB]
TOTAL: [5.9 GB]

Starting iterations...
Iteration 4: max relative diff=inf, 6.01 sec so far
Iteration 8: max relative diff=inf, 11.91 sec so far
Iteration 12: max relative diff=inf, 17.77 sec so far
Iteration 16: max relative diff=inf, 23.39 sec so far
Iteration 20: max relative diff=0.000977, 28.91 sec so far

Jacobi: 21 iterations in 438.66 seconds (average 1.442857, setup 408.36)

Value in the initial state: 0.50048828125

Time for model checking: 444.298 seconds.

Result: 0.50048828125 (exact floating point)

---------------------------------------------------------------------

Note: There were 60 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

