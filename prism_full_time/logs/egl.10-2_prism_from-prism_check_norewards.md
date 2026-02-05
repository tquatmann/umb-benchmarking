# Log files

Tool configuration: prism_from-prism_check_norewards
Benchmark: [egl.10-2](../../models/egl.10-2)
Parsed values: [52.072, 58.438, 47.961, 49.334, 49.626]



### Log file: prism_from-prism_check_norewards_egl.10-2_rep1.log

```
Command(s):
../bin/prism  models/egl.10-2/model.prism models/egl.10-2/property.props
Wallclock time: 52.072 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:46:19 GMT+01:00 2026
Hostname: r23m0045.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/egl.10-2/model.prism models/egl.10-2/property.props

Parsing PRISM model file "models/egl.10-2/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Parsing properties file "models/egl.10-2/property.props"...

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

Reachability (BFS): 101 iterations in 0.08 seconds (average 0.000792, setup 0.00)

Time for model construction: 0.204 seconds.

Type:        DTMC
States:      66060286 (1 initial)
Transitions: 67108861

Transition matrix: 18729 nodes (3 terminal), 67108861 minterms, vars: 169r/169c

Prob0: 63 iterations in 0.20 seconds (average 0.003175, setup 0.00)

Prob1: 3 iterations in 0.02 seconds (average 0.006667, setup 0.00)

yes = 12628991, no = 53429760, maybe = 1535

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=169, nodes=4809] [225.4 KB]
Adding explicit sparse matrices... [levels=159, num=21, compact] [524.0 KB]
Creating vector for diagonals... [dist=1, compact] [126.0 MB]
Creating vector for RHS... [dist=2, compact] [126.0 MB]
Allocating iteration vectors... [2 x 504.0 MB]
TOTAL: [1.2 GB]

Starting iterations...
Iteration 15: max relative diff=inf, 5.23 sec so far

Jacobi: 21 iterations in 50.65 seconds (average 0.345714, setup 43.39)

Value in the initial state: 0.50048828125

Time for model checking: 51.227 seconds.

Result: 0.50048828125 (exact floating point)

---------------------------------------------------------------------

Note: There were 60 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_egl.10-2_rep2.log

```
Command(s):
../bin/prism  models/egl.10-2/model.prism models/egl.10-2/property.props
Wallclock time: 58.438 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:08:50 GMT+01:00 2026
Hostname: r23m0196.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/egl.10-2/model.prism models/egl.10-2/property.props

Parsing PRISM model file "models/egl.10-2/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Parsing properties file "models/egl.10-2/property.props"...

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

Reachability (BFS): 101 iterations in 0.09 seconds (average 0.000891, setup 0.00)

Time for model construction: 0.281 seconds.

Type:        DTMC
States:      66060286 (1 initial)
Transitions: 67108861

Transition matrix: 18729 nodes (3 terminal), 67108861 minterms, vars: 169r/169c

Prob0: 63 iterations in 0.24 seconds (average 0.003810, setup 0.00)

Prob1: 3 iterations in 0.03 seconds (average 0.010000, setup 0.00)

yes = 12628991, no = 53429760, maybe = 1535

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=169, nodes=4809] [225.4 KB]
Adding explicit sparse matrices... [levels=159, num=21, compact] [524.0 KB]
Creating vector for diagonals... [dist=1, compact] [126.0 MB]
Creating vector for RHS... [dist=2, compact] [126.0 MB]
Allocating iteration vectors... [2 x 504.0 MB]
TOTAL: [1.2 GB]

Starting iterations...
Iteration 12: max relative diff=inf, 5.01 sec so far

Jacobi: 21 iterations in 56.80 seconds (average 0.414762, setup 48.09)

Value in the initial state: 0.50048828125

Time for model checking: 57.371 seconds.

Result: 0.50048828125 (exact floating point)

---------------------------------------------------------------------

Note: There were 60 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_egl.10-2_rep3.log

```
Command(s):
../bin/prism  models/egl.10-2/model.prism models/egl.10-2/property.props
Wallclock time: 47.961 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:01 GMT+01:00 2026
Hostname: r23m0100.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/egl.10-2/model.prism models/egl.10-2/property.props

Parsing PRISM model file "models/egl.10-2/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Parsing properties file "models/egl.10-2/property.props"...

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

Reachability (BFS): 101 iterations in 0.08 seconds (average 0.000792, setup 0.00)

Time for model construction: 0.188 seconds.

Type:        DTMC
States:      66060286 (1 initial)
Transitions: 67108861

Transition matrix: 18729 nodes (3 terminal), 67108861 minterms, vars: 169r/169c

Prob0: 63 iterations in 0.17 seconds (average 0.002698, setup 0.00)

Prob1: 3 iterations in 0.01 seconds (average 0.003333, setup 0.00)

yes = 12628991, no = 53429760, maybe = 1535

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=169, nodes=4809] [225.4 KB]
Adding explicit sparse matrices... [levels=159, num=21, compact] [524.0 KB]
Creating vector for diagonals... [dist=1, compact] [126.0 MB]
Creating vector for RHS... [dist=2, compact] [126.0 MB]
Allocating iteration vectors... [2 x 504.0 MB]
TOTAL: [1.2 GB]

Starting iterations...
Iteration 18: max relative diff=inf, 5.10 sec so far

Jacobi: 21 iterations in 46.59 seconds (average 0.282857, setup 40.65)

Value in the initial state: 0.50048828125

Time for model checking: 46.929 seconds.

Result: 0.50048828125 (exact floating point)

---------------------------------------------------------------------

Note: There were 60 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_egl.10-2_rep4.log

```
Command(s):
../bin/prism  models/egl.10-2/model.prism models/egl.10-2/property.props
Wallclock time: 49.334 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:08:42 GMT+01:00 2026
Hostname: n23m0294.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/egl.10-2/model.prism models/egl.10-2/property.props

Parsing PRISM model file "models/egl.10-2/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Parsing properties file "models/egl.10-2/property.props"...

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

Reachability (BFS): 101 iterations in 0.07 seconds (average 0.000693, setup 0.00)

Time for model construction: 0.154 seconds.

Type:        DTMC
States:      66060286 (1 initial)
Transitions: 67108861

Transition matrix: 18729 nodes (3 terminal), 67108861 minterms, vars: 169r/169c

Prob0: 63 iterations in 0.13 seconds (average 0.002063, setup 0.00)

Prob1: 3 iterations in 0.01 seconds (average 0.003333, setup 0.00)

yes = 12628991, no = 53429760, maybe = 1535

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=169, nodes=4809] [225.4 KB]
Adding explicit sparse matrices... [levels=159, num=21, compact] [524.0 KB]
Creating vector for diagonals... [dist=1, compact] [126.0 MB]
Creating vector for RHS... [dist=2, compact] [126.0 MB]
Allocating iteration vectors... [2 x 504.0 MB]
TOTAL: [1.2 GB]

Starting iterations...
Iteration 18: max relative diff=inf, 5.04 sec so far

Jacobi: 21 iterations in 48.27 seconds (average 0.280000, setup 42.39)

Value in the initial state: 0.50048828125

Time for model checking: 48.573 seconds.

Result: 0.50048828125 (exact floating point)

---------------------------------------------------------------------

Note: There were 60 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_egl.10-2_rep5.log

```
Command(s):
../bin/prism  models/egl.10-2/model.prism models/egl.10-2/property.props
Wallclock time: 49.626 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:12:54 GMT+01:00 2026
Hostname: n23m0394.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/egl.10-2/model.prism models/egl.10-2/property.props

Parsing PRISM model file "models/egl.10-2/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Parsing properties file "models/egl.10-2/property.props"...

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

Reachability (BFS): 101 iterations in 0.08 seconds (average 0.000792, setup 0.00)

Time for model construction: 0.304 seconds.

Type:        DTMC
States:      66060286 (1 initial)
Transitions: 67108861

Transition matrix: 18729 nodes (3 terminal), 67108861 minterms, vars: 169r/169c

Prob0: 63 iterations in 0.15 seconds (average 0.002381, setup 0.00)

Prob1: 3 iterations in 0.02 seconds (average 0.006667, setup 0.00)

yes = 12628991, no = 53429760, maybe = 1535

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=169, nodes=4809] [225.4 KB]
Adding explicit sparse matrices... [levels=159, num=21, compact] [524.0 KB]
Creating vector for diagonals... [dist=1, compact] [126.0 MB]
Creating vector for RHS... [dist=2, compact] [126.0 MB]
Allocating iteration vectors... [2 x 504.0 MB]
TOTAL: [1.2 GB]

Starting iterations...
Iteration 17: max relative diff=inf, 5.14 sec so far

Jacobi: 21 iterations in 47.32 seconds (average 0.301429, setup 40.99)

Value in the initial state: 0.50048828125

Time for model checking: 47.718 seconds.

Result: 0.50048828125 (exact floating point)

---------------------------------------------------------------------

Note: There were 60 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

