# Log files

Tool configuration: prism_from-umb_check_default
Benchmark: [oscillators.8-10-0.1-1-0.1-1.0](../../models/oscillators.8-10-0.1-1-0.1-1.0)
Parsed values: [9.555, 18.472, 7.648, 9.358, 7.133]



### Log file: prism_from-umb_check_default_oscillators.8-10-0.1-1-0.1-1.0_rep1.log

```
Command(s):
../bin/prism  -importmodel models/oscillators.8-10-0.1-1-0.1-1.0/prism.model.umb models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 9.555 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:26:36 GMT+01:00 2026
Hostname: n23m0174.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/oscillators.8-10-0.1-1-0.1-1.0/prism.model.umb models/oscillators.8-10-0.1-1-0.1-1.0/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     [step]
Variables:   x
Labels:      "target"
Rewards:     "time_to_synch"

Parsing properties file "models/oscillators.8-10-0.1-1-0.1-1.0/property.props"...

1 property:
(1) "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 100% ]

Computing reachable states...

Reachability (BFS): 2 iterations in 0.03 seconds (average 0.015000, setup 0.00)

Time for model construction: 2.392 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80917 nodes (438 terminal), 76623 minterms, vars: 15r/15c

Prob0: 15 iterations in 0.20 seconds (average 0.013333, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 2, inf = 0, maybe = 24309

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=15, nodes=81533] [3.7 MB]
Adding explicit sparse matrices... [levels=15, num=1, compact] [397.7 KB]
Creating vector for diagonals... [dist=1, compact] [47.5 KB]
Creating vector for RHS... [dist=9, compact] [47.6 KB]
Allocating iteration vectors... [2 x 189.9 KB]
TOTAL: [4.6 MB]

Starting iterations...

Jacobi: 3153 iterations in 5.31 seconds (average 0.000162, setup 4.80)

Value in the initial state: 6.007026913358401

Time for model checking: 5.559 seconds.

Result: 6.007026913358401 (+/- 5.972365002886308E-5 estimated; rel err 9.94229772735825E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_oscillators.8-10-0.1-1-0.1-1.0_rep2.log

```
Command(s):
../bin/prism  -importmodel models/oscillators.8-10-0.1-1-0.1-1.0/prism.model.umb models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 18.472 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:13:55 GMT+01:00 2026
Hostname: n23m0095.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/oscillators.8-10-0.1-1-0.1-1.0/prism.model.umb models/oscillators.8-10-0.1-1-0.1-1.0/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     [step]
Variables:   x
Labels:      "target"
Rewards:     "time_to_synch"

Parsing properties file "models/oscillators.8-10-0.1-1-0.1-1.0/property.props"...

1 property:
(1) "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 82% 100% ]

Computing reachable states...

Reachability (BFS): 2 iterations in 0.02 seconds (average 0.010000, setup 0.00)

Time for model construction: 4.106 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80917 nodes (438 terminal), 76623 minterms, vars: 15r/15c

Prob0: 15 iterations in 0.26 seconds (average 0.017333, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 2, inf = 0, maybe = 24309

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=15, nodes=81533] [3.7 MB]
Adding explicit sparse matrices... [levels=15, num=1, compact] [397.7 KB]
Creating vector for diagonals... [dist=1, compact] [47.5 KB]
Creating vector for RHS... [dist=9, compact] [47.6 KB]
Allocating iteration vectors... [2 x 189.9 KB]
TOTAL: [4.6 MB]

Starting iterations...

Jacobi: 3153 iterations in 13.15 seconds (average 0.000174, setup 12.60)

Value in the initial state: 6.007026913358401

Time for model checking: 13.49 seconds.

Result: 6.007026913358401 (+/- 5.972365002886308E-5 estimated; rel err 9.94229772735825E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_oscillators.8-10-0.1-1-0.1-1.0_rep3.log

```
Command(s):
../bin/prism  -importmodel models/oscillators.8-10-0.1-1-0.1-1.0/prism.model.umb models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 7.648 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:09:14 GMT+01:00 2026
Hostname: r23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/oscillators.8-10-0.1-1-0.1-1.0/prism.model.umb models/oscillators.8-10-0.1-1-0.1-1.0/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     [step]
Variables:   x
Labels:      "target"
Rewards:     "time_to_synch"

Parsing properties file "models/oscillators.8-10-0.1-1-0.1-1.0/property.props"...

1 property:
(1) "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 100% ]

Computing reachable states...

Reachability (BFS): 2 iterations in 0.02 seconds (average 0.010000, setup 0.00)

Time for model construction: 2.017 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80917 nodes (438 terminal), 76623 minterms, vars: 15r/15c

Prob0: 15 iterations in 0.14 seconds (average 0.009333, setup 0.00)

Prob1: 1 iterations in 0.01 seconds (average 0.010000, setup 0.00)

goal = 2, inf = 0, maybe = 24309

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=15, nodes=81533] [3.7 MB]
Adding explicit sparse matrices... [levels=15, num=1, compact] [397.7 KB]
Creating vector for diagonals... [dist=1, compact] [47.5 KB]
Creating vector for RHS... [dist=9, compact] [47.6 KB]
Allocating iteration vectors... [2 x 189.9 KB]
TOTAL: [4.6 MB]

Starting iterations...

Jacobi: 3153 iterations in 4.70 seconds (average 0.000174, setup 4.15)

Value in the initial state: 6.007026913358401

Time for model checking: 4.896 seconds.

Result: 6.007026913358401 (+/- 5.972365002886308E-5 estimated; rel err 9.94229772735825E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_oscillators.8-10-0.1-1-0.1-1.0_rep4.log

```
Command(s):
../bin/prism  -importmodel models/oscillators.8-10-0.1-1-0.1-1.0/prism.model.umb models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 9.358 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:22:01 GMT+01:00 2026
Hostname: n23m0203.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/oscillators.8-10-0.1-1-0.1-1.0/prism.model.umb models/oscillators.8-10-0.1-1-0.1-1.0/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     [step]
Variables:   x
Labels:      "target"
Rewards:     "time_to_synch"

Parsing properties file "models/oscillators.8-10-0.1-1-0.1-1.0/property.props"...

1 property:
(1) "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 100% ]

Computing reachable states...

Reachability (BFS): 2 iterations in 0.02 seconds (average 0.010000, setup 0.00)

Time for model construction: 1.976 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80917 nodes (438 terminal), 76623 minterms, vars: 15r/15c

Prob0: 15 iterations in 0.17 seconds (average 0.011333, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 2, inf = 0, maybe = 24309

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=15, nodes=81533] [3.7 MB]
Adding explicit sparse matrices... [levels=15, num=1, compact] [397.7 KB]
Creating vector for diagonals... [dist=1, compact] [47.5 KB]
Creating vector for RHS... [dist=9, compact] [47.6 KB]
Allocating iteration vectors... [2 x 189.9 KB]
TOTAL: [4.6 MB]

Starting iterations...

Jacobi: 3153 iterations in 5.70 seconds (average 0.000152, setup 5.22)

Value in the initial state: 6.007026913358401

Time for model checking: 5.914 seconds.

Result: 6.007026913358401 (+/- 5.972365002886308E-5 estimated; rel err 9.94229772735825E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_oscillators.8-10-0.1-1-0.1-1.0_rep5.log

```
Command(s):
../bin/prism  -importmodel models/oscillators.8-10-0.1-1-0.1-1.0/prism.model.umb models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 7.133 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:50 GMT+01:00 2026
Hostname: n23m0204.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/oscillators.8-10-0.1-1-0.1-1.0/prism.model.umb models/oscillators.8-10-0.1-1-0.1-1.0/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     [step]
Variables:   x
Labels:      "target"
Rewards:     "time_to_synch"

Parsing properties file "models/oscillators.8-10-0.1-1-0.1-1.0/property.props"...

1 property:
(1) "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 100% ]

Computing reachable states...

Reachability (BFS): 2 iterations in 0.02 seconds (average 0.010000, setup 0.00)

Time for model construction: 1.972 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80917 nodes (438 terminal), 76623 minterms, vars: 15r/15c

Prob0: 15 iterations in 0.17 seconds (average 0.011333, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 2, inf = 0, maybe = 24309

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=15, nodes=81533] [3.7 MB]
Adding explicit sparse matrices... [levels=15, num=1, compact] [397.7 KB]
Creating vector for diagonals... [dist=1, compact] [47.5 KB]
Creating vector for RHS... [dist=9, compact] [47.6 KB]
Allocating iteration vectors... [2 x 189.9 KB]
TOTAL: [4.6 MB]

Starting iterations...

Jacobi: 3153 iterations in 4.33 seconds (average 0.000149, setup 3.86)

Value in the initial state: 6.007026913358401

Time for model checking: 4.552 seconds.

Result: 6.007026913358401 (+/- 5.972365002886308E-5 estimated; rel err 9.94229772735825E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

