# Log files

Tool configuration: prism_from-prism_check_norewards
Benchmark: [herman.15](../../models/herman.15)
Parsed values: [3.682, 3.817, 3.691, 3.841, 6.037]



### Log file: prism_from-prism_check_norewards_herman.15_rep1.log

```
Command(s):
../bin/prism  models/herman.15/model.prism models/herman.15/property.props
Wallclock time: 3.682 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:33:20 GMT+01:00 2026
Hostname: n23m0275.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/herman.15/model.prism models/herman.15/property.props

Parsing PRISM model file "models/herman.15/model.prism"...

Type:        DTMC
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10 process11 process12 process13 process14 process15
Actions:     [step]
Variables:   x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15
Labels:      "stable"
Rewards:     "steps"

Parsing properties file "models/herman.15/property.props"...

1 property:
(1) "steps": filter(max, R=? [ F "stable" ], "init")

---------------------------------------------------------------------

Model checking: "steps": filter(max, R=? [ F "stable" ], "init")

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.014 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908

Transition matrix: 810 nodes (9 terminal), 14348908 minterms, vars: 15r/15c

Prob0: 6 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 30, inf = 0, maybe = 32738

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=15, nodes=1212] [56.8 KB]
Adding explicit sparse matrices... [levels=8, num=30, compact] [587.7 KB]
Creating vector for diagonals... [dist=2, compact] [64.0 KB]
Creating vector for RHS... [dist=2, compact] [64.0 KB]
Allocating iteration vectors... [2 x 256.0 KB]
TOTAL: [1.3 MB]

Starting iterations...

Jacobi: 245 iterations in 2.99 seconds (average 0.012163, setup 0.01)

Maximum value over states satisfying filter: 33.332616661835104

There are 10 states with (approximately) this value:
5285:(0,0,1,0,1,0,0,1,0,1,0,0,1,0,1)
9513:(0,1,0,0,1,0,1,0,0,1,0,1,0,0,1)
10570:(0,1,0,1,0,0,1,0,1,0,0,1,0,1,0)
11627:(0,1,0,1,1,0,1,0,1,1,0,1,0,1,1)
13741:(0,1,1,0,1,0,1,1,0,1,0,1,1,0,1)
19026:(1,0,0,1,0,1,0,0,1,0,1,0,0,1,0)
21140:(1,0,1,0,0,1,0,1,0,0,1,0,1,0,0)
22197:(1,0,1,0,1,1,0,1,0,1,1,0,1,0,1)
23254:(1,0,1,1,0,1,0,1,1,0,1,0,1,1,0)
27482:(1,1,0,1,0,1,1,0,1,0,1,1,0,1,0)

Time for model checking: 3.064 seconds.

Result: 33.332616661835104


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_herman.15_rep2.log

```
Command(s):
../bin/prism  models/herman.15/model.prism models/herman.15/property.props
Wallclock time: 3.817 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:14:56 GMT+01:00 2026
Hostname: n23m0323.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/herman.15/model.prism models/herman.15/property.props

Parsing PRISM model file "models/herman.15/model.prism"...

Type:        DTMC
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10 process11 process12 process13 process14 process15
Actions:     [step]
Variables:   x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15
Labels:      "stable"
Rewards:     "steps"

Parsing properties file "models/herman.15/property.props"...

1 property:
(1) "steps": filter(max, R=? [ F "stable" ], "init")

---------------------------------------------------------------------

Model checking: "steps": filter(max, R=? [ F "stable" ], "init")

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.02 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908

Transition matrix: 810 nodes (9 terminal), 14348908 minterms, vars: 15r/15c

Prob0: 6 iterations in 0.01 seconds (average 0.001667, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 30, inf = 0, maybe = 32738

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=15, nodes=1212] [56.8 KB]
Adding explicit sparse matrices... [levels=8, num=30, compact] [587.7 KB]
Creating vector for diagonals... [dist=2, compact] [64.0 KB]
Creating vector for RHS... [dist=2, compact] [64.0 KB]
Allocating iteration vectors... [2 x 256.0 KB]
TOTAL: [1.3 MB]

Starting iterations...

Jacobi: 245 iterations in 2.88 seconds (average 0.011755, setup 0.00)

Maximum value over states satisfying filter: 33.332616661835104

There are 10 states with (approximately) this value:
5285:(0,0,1,0,1,0,0,1,0,1,0,0,1,0,1)
9513:(0,1,0,0,1,0,1,0,0,1,0,1,0,0,1)
10570:(0,1,0,1,0,0,1,0,1,0,0,1,0,1,0)
11627:(0,1,0,1,1,0,1,0,1,1,0,1,0,1,1)
13741:(0,1,1,0,1,0,1,1,0,1,0,1,1,0,1)
19026:(1,0,0,1,0,1,0,0,1,0,1,0,0,1,0)
21140:(1,0,1,0,0,1,0,1,0,0,1,0,1,0,0)
22197:(1,0,1,0,1,1,0,1,0,1,1,0,1,0,1)
23254:(1,0,1,1,0,1,0,1,1,0,1,0,1,1,0)
27482:(1,1,0,1,0,1,1,0,1,0,1,1,0,1,0)

Time for model checking: 2.929 seconds.

Result: 33.332616661835104


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_herman.15_rep3.log

```
Command(s):
../bin/prism  models/herman.15/model.prism models/herman.15/property.props
Wallclock time: 3.691 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:26:40 GMT+01:00 2026
Hostname: n23m0119.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/herman.15/model.prism models/herman.15/property.props

Parsing PRISM model file "models/herman.15/model.prism"...

Type:        DTMC
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10 process11 process12 process13 process14 process15
Actions:     [step]
Variables:   x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15
Labels:      "stable"
Rewards:     "steps"

Parsing properties file "models/herman.15/property.props"...

1 property:
(1) "steps": filter(max, R=? [ F "stable" ], "init")

---------------------------------------------------------------------

Model checking: "steps": filter(max, R=? [ F "stable" ], "init")

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.015 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908

Transition matrix: 810 nodes (9 terminal), 14348908 minterms, vars: 15r/15c

Prob0: 6 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 30, inf = 0, maybe = 32738

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=15, nodes=1212] [56.8 KB]
Adding explicit sparse matrices... [levels=8, num=30, compact] [587.7 KB]
Creating vector for diagonals... [dist=2, compact] [64.0 KB]
Creating vector for RHS... [dist=2, compact] [64.0 KB]
Allocating iteration vectors... [2 x 256.0 KB]
TOTAL: [1.3 MB]

Starting iterations...

Jacobi: 245 iterations in 2.51 seconds (average 0.010204, setup 0.01)

Maximum value over states satisfying filter: 33.332616661835104

There are 10 states with (approximately) this value:
5285:(0,0,1,0,1,0,0,1,0,1,0,0,1,0,1)
9513:(0,1,0,0,1,0,1,0,0,1,0,1,0,0,1)
10570:(0,1,0,1,0,0,1,0,1,0,0,1,0,1,0)
11627:(0,1,0,1,1,0,1,0,1,1,0,1,0,1,1)
13741:(0,1,1,0,1,0,1,1,0,1,0,1,1,0,1)
19026:(1,0,0,1,0,1,0,0,1,0,1,0,0,1,0)
21140:(1,0,1,0,0,1,0,1,0,0,1,0,1,0,0)
22197:(1,0,1,0,1,1,0,1,0,1,1,0,1,0,1)
23254:(1,0,1,1,0,1,0,1,1,0,1,0,1,1,0)
27482:(1,1,0,1,0,1,1,0,1,0,1,1,0,1,0)

Time for model checking: 2.543 seconds.

Result: 33.332616661835104


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_herman.15_rep4.log

```
Command(s):
../bin/prism  models/herman.15/model.prism models/herman.15/property.props
Wallclock time: 3.841 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:21:43 GMT+01:00 2026
Hostname: n23m0057.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/herman.15/model.prism models/herman.15/property.props

Parsing PRISM model file "models/herman.15/model.prism"...

Type:        DTMC
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10 process11 process12 process13 process14 process15
Actions:     [step]
Variables:   x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15
Labels:      "stable"
Rewards:     "steps"

Parsing properties file "models/herman.15/property.props"...

1 property:
(1) "steps": filter(max, R=? [ F "stable" ], "init")

---------------------------------------------------------------------

Model checking: "steps": filter(max, R=? [ F "stable" ], "init")

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.123 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908

Transition matrix: 810 nodes (9 terminal), 14348908 minterms, vars: 15r/15c

Prob0: 6 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 30, inf = 0, maybe = 32738

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=15, nodes=1212] [56.8 KB]
Adding explicit sparse matrices... [levels=8, num=30, compact] [587.7 KB]
Creating vector for diagonals... [dist=2, compact] [64.0 KB]
Creating vector for RHS... [dist=2, compact] [64.0 KB]
Allocating iteration vectors... [2 x 256.0 KB]
TOTAL: [1.3 MB]

Starting iterations...

Jacobi: 245 iterations in 3.02 seconds (average 0.012327, setup 0.00)

Maximum value over states satisfying filter: 33.332616661835104

There are 10 states with (approximately) this value:
5285:(0,0,1,0,1,0,0,1,0,1,0,0,1,0,1)
9513:(0,1,0,0,1,0,1,0,0,1,0,1,0,0,1)
10570:(0,1,0,1,0,0,1,0,1,0,0,1,0,1,0)
11627:(0,1,0,1,1,0,1,0,1,1,0,1,0,1,1)
13741:(0,1,1,0,1,0,1,1,0,1,0,1,1,0,1)
19026:(1,0,0,1,0,1,0,0,1,0,1,0,0,1,0)
21140:(1,0,1,0,0,1,0,1,0,0,1,0,1,0,0)
22197:(1,0,1,0,1,1,0,1,0,1,1,0,1,0,1)
23254:(1,0,1,1,0,1,0,1,1,0,1,0,1,1,0)
27482:(1,1,0,1,0,1,1,0,1,0,1,1,0,1,0)

Time for model checking: 3.072 seconds.

Result: 33.332616661835104


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_herman.15_rep5.log

```
Command(s):
../bin/prism  models/herman.15/model.prism models/herman.15/property.props
Wallclock time: 6.037 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:09:40 GMT+01:00 2026
Hostname: n23m0027.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/herman.15/model.prism models/herman.15/property.props

Parsing PRISM model file "models/herman.15/model.prism"...

Type:        DTMC
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10 process11 process12 process13 process14 process15
Actions:     [step]
Variables:   x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15
Labels:      "stable"
Rewards:     "steps"

Parsing properties file "models/herman.15/property.props"...

1 property:
(1) "steps": filter(max, R=? [ F "stable" ], "init")

---------------------------------------------------------------------

Model checking: "steps": filter(max, R=? [ F "stable" ], "init")

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.07 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908

Transition matrix: 810 nodes (9 terminal), 14348908 minterms, vars: 15r/15c

Prob0: 6 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 30, inf = 0, maybe = 32738

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=15, nodes=1212] [56.8 KB]
Adding explicit sparse matrices... [levels=8, num=30, compact] [587.7 KB]
Creating vector for diagonals... [dist=2, compact] [64.0 KB]
Creating vector for RHS... [dist=2, compact] [64.0 KB]
Allocating iteration vectors... [2 x 256.0 KB]
TOTAL: [1.3 MB]

Starting iterations...

Jacobi: 245 iterations in 2.49 seconds (average 0.010122, setup 0.01)

Maximum value over states satisfying filter: 33.332616661835104

There are 10 states with (approximately) this value:
5285:(0,0,1,0,1,0,0,1,0,1,0,0,1,0,1)
9513:(0,1,0,0,1,0,1,0,0,1,0,1,0,0,1)
10570:(0,1,0,1,0,0,1,0,1,0,0,1,0,1,0)
11627:(0,1,0,1,1,0,1,0,1,1,0,1,0,1,1)
13741:(0,1,1,0,1,0,1,1,0,1,0,1,1,0,1)
19026:(1,0,0,1,0,1,0,0,1,0,1,0,0,1,0)
21140:(1,0,1,0,0,1,0,1,0,0,1,0,1,0,0)
22197:(1,0,1,0,1,1,0,1,0,1,1,0,1,0,1)
23254:(1,0,1,1,0,1,0,1,1,0,1,0,1,1,0)
27482:(1,1,0,1,0,1,1,0,1,0,1,1,0,1,0)

Time for model checking: 2.568 seconds.

Result: 33.332616661835104


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

