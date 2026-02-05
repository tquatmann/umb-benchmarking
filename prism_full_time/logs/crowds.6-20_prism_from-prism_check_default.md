# Log files for prism_from-prism_check_default on model [crowds.6-20](../../models/crowds.6-20)

Parsed values: `[16.973, 17.077, 18.94, 16.124, 15.87]`



### Log file: prism_from-prism_check_default_crowds.6-20_rep1.log

```
Command(s):
../bin/prism  models/crowds.6-20/model.prism models/crowds.6-20/property.props
Wallclock time: 16.973 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:30:14 GMT+01:00 2026
Hostname: n23m0275.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.6-20/model.prism models/crowds.6-20/property.props

Parsing PRISM model file "models/crowds.6-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Parsing properties file "models/crowds.6-20/property.props"...

1 property:
(1) "positive": P=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "positive": P=? [ F "target" ]

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 56 iterations in 0.15 seconds (average 0.002679, setup 0.00)

Time for model construction: 0.25 seconds.

Warning: Deadlocks detected and fixed in 230230 states

Type:        DTMC
States:      10633591 (1 initial)
Transitions: 38261191

Transition matrix: 40814 nodes (7 terminal), 38261191 minterms, vars: 78r/78c

Prob0: 14 iterations in 0.05 seconds (average 0.003571, setup 0.00)

Prob1: 37 iterations in 0.10 seconds (average 0.002703, setup 0.00)

yes = 363561, no = 8587502, maybe = 1682528

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=78, nodes=41560] [1.9 MB]
Adding explicit sparse matrices... [levels=54, num=322, compact] [925.3 KB]
Creating vector for diagonals... [dist=1, compact] [20.3 MB]
Creating vector for RHS... [dist=2, compact] [20.3 MB]
Allocating iteration vectors... [2 x 81.1 MB]
TOTAL: [205.6 MB]

Starting iterations...
Iteration 73: max relative diff=0.014551, 5.07 sec so far
Iteration 146: max relative diff=0.000120, 10.13 sec so far

Jacobi: 206 iterations in 15.84 seconds (average 0.069369, setup 1.55)

Value in the initial state: 0.12047517459031545

Time for model checking: 16.083 seconds.

Result: 0.12047517459031545 (+/- 1.135270177688272E-6 estimated; rel err 9.423270657617557E-6)

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_crowds.6-20_rep2.log

```
Command(s):
../bin/prism  models/crowds.6-20/model.prism models/crowds.6-20/property.props
Wallclock time: 17.077 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:28:58 GMT+01:00 2026
Hostname: n23m0142.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.6-20/model.prism models/crowds.6-20/property.props

Parsing PRISM model file "models/crowds.6-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Parsing properties file "models/crowds.6-20/property.props"...

1 property:
(1) "positive": P=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "positive": P=? [ F "target" ]

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 56 iterations in 0.15 seconds (average 0.002679, setup 0.00)

Time for model construction: 0.25 seconds.

Warning: Deadlocks detected and fixed in 230230 states

Type:        DTMC
States:      10633591 (1 initial)
Transitions: 38261191

Transition matrix: 40814 nodes (7 terminal), 38261191 minterms, vars: 78r/78c

Prob0: 14 iterations in 0.05 seconds (average 0.003571, setup 0.00)

Prob1: 37 iterations in 0.09 seconds (average 0.002432, setup 0.00)

yes = 363561, no = 8587502, maybe = 1682528

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=78, nodes=41560] [1.9 MB]
Adding explicit sparse matrices... [levels=54, num=322, compact] [925.3 KB]
Creating vector for diagonals... [dist=1, compact] [20.3 MB]
Creating vector for RHS... [dist=2, compact] [20.3 MB]
Allocating iteration vectors... [2 x 81.1 MB]
TOTAL: [205.6 MB]

Starting iterations...
Iteration 79: max relative diff=0.010682, 5.03 sec so far
Iteration 160: max relative diff=0.000048, 10.09 sec so far

Jacobi: 206 iterations in 14.33 seconds (average 0.062961, setup 1.36)

Value in the initial state: 0.12047517459031545

Time for model checking: 14.535 seconds.

Result: 0.12047517459031545 (+/- 1.135270177688272E-6 estimated; rel err 9.423270657617557E-6)

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_crowds.6-20_rep3.log

```
Command(s):
../bin/prism  models/crowds.6-20/model.prism models/crowds.6-20/property.props
Wallclock time: 18.940 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:04 GMT+01:00 2026
Hostname: n23m0242.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.6-20/model.prism models/crowds.6-20/property.props

Parsing PRISM model file "models/crowds.6-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Parsing properties file "models/crowds.6-20/property.props"...

1 property:
(1) "positive": P=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "positive": P=? [ F "target" ]

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 56 iterations in 0.22 seconds (average 0.003929, setup 0.00)

Time for model construction: 0.405 seconds.

Warning: Deadlocks detected and fixed in 230230 states

Type:        DTMC
States:      10633591 (1 initial)
Transitions: 38261191

Transition matrix: 40814 nodes (7 terminal), 38261191 minterms, vars: 78r/78c

Prob0: 14 iterations in 0.06 seconds (average 0.004286, setup 0.00)

Prob1: 37 iterations in 0.13 seconds (average 0.003514, setup 0.00)

yes = 363561, no = 8587502, maybe = 1682528

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=78, nodes=41560] [1.9 MB]
Adding explicit sparse matrices... [levels=54, num=322, compact] [925.3 KB]
Creating vector for diagonals... [dist=1, compact] [20.3 MB]
Creating vector for RHS... [dist=2, compact] [20.3 MB]
Allocating iteration vectors... [2 x 81.1 MB]
TOTAL: [205.6 MB]

Starting iterations...
Iteration 66: max relative diff=0.020422, 5.06 sec so far
Iteration 133: max relative diff=0.000362, 10.13 sec so far
Iteration 199: max relative diff=0.000002, 15.15 sec so far

Jacobi: 206 iterations in 17.22 seconds (average 0.076117, setup 1.54)

Value in the initial state: 0.12047517459031545

Time for model checking: 17.506 seconds.

Result: 0.12047517459031545 (+/- 1.135270177688272E-6 estimated; rel err 9.423270657617557E-6)

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_crowds.6-20_rep4.log

```
Command(s):
../bin/prism  models/crowds.6-20/model.prism models/crowds.6-20/property.props
Wallclock time: 16.124 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:50 GMT+01:00 2026
Hostname: n23m0267.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.6-20/model.prism models/crowds.6-20/property.props

Parsing PRISM model file "models/crowds.6-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Parsing properties file "models/crowds.6-20/property.props"...

1 property:
(1) "positive": P=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "positive": P=? [ F "target" ]

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 56 iterations in 0.19 seconds (average 0.003393, setup 0.00)

Time for model construction: 0.332 seconds.

Warning: Deadlocks detected and fixed in 230230 states

Type:        DTMC
States:      10633591 (1 initial)
Transitions: 38261191

Transition matrix: 40814 nodes (7 terminal), 38261191 minterms, vars: 78r/78c

Prob0: 14 iterations in 0.05 seconds (average 0.003571, setup 0.00)

Prob1: 37 iterations in 0.09 seconds (average 0.002432, setup 0.00)

yes = 363561, no = 8587502, maybe = 1682528

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=78, nodes=41560] [1.9 MB]
Adding explicit sparse matrices... [levels=54, num=322, compact] [925.3 KB]
Creating vector for diagonals... [dist=1, compact] [20.3 MB]
Creating vector for RHS... [dist=2, compact] [20.3 MB]
Allocating iteration vectors... [2 x 81.1 MB]
TOTAL: [205.6 MB]

Starting iterations...
Iteration 77: max relative diff=0.011356, 5.05 sec so far
Iteration 155: max relative diff=0.000060, 10.09 sec so far

Jacobi: 206 iterations in 14.71 seconds (average 0.064951, setup 1.33)

Value in the initial state: 0.12047517459031545

Time for model checking: 14.923 seconds.

Result: 0.12047517459031545 (+/- 1.135270177688272E-6 estimated; rel err 9.423270657617557E-6)

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_crowds.6-20_rep5.log

```
Command(s):
../bin/prism  models/crowds.6-20/model.prism models/crowds.6-20/property.props
Wallclock time: 15.870 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:15:20 GMT+01:00 2026
Hostname: n23m0341.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.6-20/model.prism models/crowds.6-20/property.props

Parsing PRISM model file "models/crowds.6-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Parsing properties file "models/crowds.6-20/property.props"...

1 property:
(1) "positive": P=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "positive": P=? [ F "target" ]

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 56 iterations in 0.13 seconds (average 0.002321, setup 0.00)

Time for model construction: 0.232 seconds.

Warning: Deadlocks detected and fixed in 230230 states

Type:        DTMC
States:      10633591 (1 initial)
Transitions: 38261191

Transition matrix: 40814 nodes (7 terminal), 38261191 minterms, vars: 78r/78c

Prob0: 14 iterations in 0.05 seconds (average 0.003571, setup 0.00)

Prob1: 37 iterations in 0.09 seconds (average 0.002432, setup 0.00)

yes = 363561, no = 8587502, maybe = 1682528

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=78, nodes=41560] [1.9 MB]
Adding explicit sparse matrices... [levels=54, num=322, compact] [925.3 KB]
Creating vector for diagonals... [dist=1, compact] [20.3 MB]
Creating vector for RHS... [dist=2, compact] [20.3 MB]
Allocating iteration vectors... [2 x 81.1 MB]
TOTAL: [205.6 MB]

Starting iterations...
Iteration 77: max relative diff=0.011356, 5.03 sec so far
Iteration 155: max relative diff=0.000060, 10.08 sec so far

Jacobi: 206 iterations in 14.86 seconds (average 0.065049, setup 1.46)

Value in the initial state: 0.12047517459031545

Time for model checking: 15.064 seconds.

Result: 0.12047517459031545 (+/- 1.135270177688272E-6 estimated; rel err 9.423270657617557E-6)

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

