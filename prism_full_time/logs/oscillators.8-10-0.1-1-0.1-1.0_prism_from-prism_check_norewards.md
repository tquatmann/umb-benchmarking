# Log files for prism_from-prism_check_norewards on model [oscillators.8-10-0.1-1-0.1-1.0](../../models/oscillators.8-10-0.1-1-0.1-1.0)

Parsed values: `[26.301, 27.077, 30.011, 25.097, 24.412]`



### Log file: prism_from-prism_check_norewards_oscillators.8-10-0.1-1-0.1-1.0_rep1.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 26.301 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:18:11 GMT+01:00 2026
Hostname: r23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Parsing properties file "models/oscillators.8-10-0.1-1-0.1-1.0/property.props"...

1 property:
(1) "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2 iterations in 0.05 seconds (average 0.025000, setup 0.00)

Time for model construction: 21.56 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Prob0: 15 iterations in 0.63 seconds (average 0.042000, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 2, inf = 0, maybe = 24309

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=40, nodes=80630] [3.7 MB]
Adding explicit sparse matrices... [levels=40, num=1, compact] [397.7 KB]
Creating vector for diagonals... [dist=1, compact] [47.5 KB]
Creating vector for RHS... [dist=9, compact] [47.6 KB]
Allocating iteration vectors... [2 x 189.9 KB]
TOTAL: [4.5 MB]

Starting iterations...

Jacobi: 3153 iterations in 1.12 seconds (average 0.000162, setup 0.61)

Value in the initial state: 6.007026913359109

Time for model checking: 1.967 seconds.

Result: 6.007026913359109 (+/- 5.972365002887012E-5 estimated; rel err 9.94229772735825E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_oscillators.8-10-0.1-1-0.1-1.0_rep2.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 27.077 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 02:59:27 GMT+01:00 2026
Hostname: n23m0053.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Parsing properties file "models/oscillators.8-10-0.1-1-0.1-1.0/property.props"...

1 property:
(1) "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2 iterations in 0.08 seconds (average 0.040000, setup 0.00)

Time for model construction: 22.028 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Prob0: 15 iterations in 0.81 seconds (average 0.054000, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 2, inf = 0, maybe = 24309

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=40, nodes=80630] [3.7 MB]
Adding explicit sparse matrices... [levels=40, num=1, compact] [397.7 KB]
Creating vector for diagonals... [dist=1, compact] [47.5 KB]
Creating vector for RHS... [dist=9, compact] [47.6 KB]
Allocating iteration vectors... [2 x 189.9 KB]
TOTAL: [4.5 MB]

Starting iterations...

Jacobi: 3153 iterations in 1.06 seconds (average 0.000146, setup 0.60)

Value in the initial state: 6.007026913359109

Time for model checking: 2.145 seconds.

Result: 6.007026913359109 (+/- 5.972365002887012E-5 estimated; rel err 9.94229772735825E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_oscillators.8-10-0.1-1-0.1-1.0_rep3.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 30.011 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:10:14 GMT+01:00 2026
Hostname: n23m0166.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Parsing properties file "models/oscillators.8-10-0.1-1-0.1-1.0/property.props"...

1 property:
(1) "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2 iterations in 0.06 seconds (average 0.030000, setup 0.00)

Time for model construction: 24.644 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Prob0: 15 iterations in 0.73 seconds (average 0.048667, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 2, inf = 0, maybe = 24309

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=40, nodes=80630] [3.7 MB]
Adding explicit sparse matrices... [levels=40, num=1, compact] [397.7 KB]
Creating vector for diagonals... [dist=1, compact] [47.5 KB]
Creating vector for RHS... [dist=9, compact] [47.6 KB]
Allocating iteration vectors... [2 x 189.9 KB]
TOTAL: [4.5 MB]

Starting iterations...

Jacobi: 3153 iterations in 1.12 seconds (average 0.000162, setup 0.61)

Value in the initial state: 6.007026913359109

Time for model checking: 2.073 seconds.

Result: 6.007026913359109 (+/- 5.972365002887012E-5 estimated; rel err 9.94229772735825E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_oscillators.8-10-0.1-1-0.1-1.0_rep4.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 25.097 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 02:50:13 GMT+01:00 2026
Hostname: n23m0031.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Parsing properties file "models/oscillators.8-10-0.1-1-0.1-1.0/property.props"...

1 property:
(1) "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2 iterations in 0.06 seconds (average 0.030000, setup 0.00)

Time for model construction: 20.296 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Prob0: 15 iterations in 0.63 seconds (average 0.042000, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 2, inf = 0, maybe = 24309

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=40, nodes=80630] [3.7 MB]
Adding explicit sparse matrices... [levels=40, num=1, compact] [397.7 KB]
Creating vector for diagonals... [dist=1, compact] [47.5 KB]
Creating vector for RHS... [dist=9, compact] [47.6 KB]
Allocating iteration vectors... [2 x 189.9 KB]
TOTAL: [4.5 MB]

Starting iterations...

Jacobi: 3153 iterations in 1.05 seconds (average 0.000149, setup 0.58)

Value in the initial state: 6.007026913359109

Time for model checking: 1.9 seconds.

Result: 6.007026913359109 (+/- 5.972365002887012E-5 estimated; rel err 9.94229772735825E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_oscillators.8-10-0.1-1-0.1-1.0_rep5.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 24.412 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:06 GMT+01:00 2026
Hostname: n23m0132.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Parsing properties file "models/oscillators.8-10-0.1-1-0.1-1.0/property.props"...

1 property:
(1) "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2 iterations in 0.06 seconds (average 0.030000, setup 0.00)

Time for model construction: 19.961 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Prob0: 15 iterations in 0.63 seconds (average 0.042000, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 2, inf = 0, maybe = 24309

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=40, nodes=80630] [3.7 MB]
Adding explicit sparse matrices... [levels=40, num=1, compact] [397.7 KB]
Creating vector for diagonals... [dist=1, compact] [47.5 KB]
Creating vector for RHS... [dist=9, compact] [47.6 KB]
Allocating iteration vectors... [2 x 189.9 KB]
TOTAL: [4.5 MB]

Starting iterations...

Jacobi: 3153 iterations in 1.03 seconds (average 0.000149, setup 0.56)

Value in the initial state: 6.007026913359109

Time for model checking: 1.862 seconds.

Result: 6.007026913359109 (+/- 5.972365002887012E-5 estimated; rel err 9.94229772735825E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

