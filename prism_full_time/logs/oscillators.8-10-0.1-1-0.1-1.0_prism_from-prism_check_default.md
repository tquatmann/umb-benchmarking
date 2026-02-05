# Log files

Tool configuration: prism_from-prism_check_default
Benchmark: [oscillators.8-10-0.1-1-0.1-1.0](../../models/oscillators.8-10-0.1-1-0.1-1.0)
Parsed values: [24.704, 32.844, 38.381, 28.865, 33.536]



### Log file: prism_from-prism_check_default_oscillators.8-10-0.1-1-0.1-1.0_rep1.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 24.704 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:47:53 GMT+01:00 2026
Hostname: n23m0191.hpc.itc.rwth-aachen.de
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

Time for model construction: 20.176 seconds.

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

Time for model checking: 1.885 seconds.

Result: 6.007026913359109 (+/- 5.972365002887012E-5 estimated; rel err 9.94229772735825E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_oscillators.8-10-0.1-1-0.1-1.0_rep2.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 32.844 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:07 GMT+01:00 2026
Hostname: n23m0001.hpc.itc.rwth-aachen.de
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

Time for model construction: 23.223 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Prob0: 15 iterations in 0.69 seconds (average 0.046000, setup 0.00)

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

Jacobi: 3153 iterations in 1.06 seconds (average 0.000155, setup 0.57)

Value in the initial state: 6.007026913359109

Time for model checking: 1.99 seconds.

Result: 6.007026913359109 (+/- 5.972365002887012E-5 estimated; rel err 9.94229772735825E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_oscillators.8-10-0.1-1-0.1-1.0_rep3.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 38.381 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:13 GMT+01:00 2026
Hostname: n23m0375.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 2 iterations in 0.09 seconds (average 0.045000, setup 0.00)

Time for model construction: 27.657 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Prob0: 15 iterations in 0.86 seconds (average 0.057333, setup 0.00)

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

Jacobi: 3153 iterations in 1.31 seconds (average 0.000168, setup 0.78)

Value in the initial state: 6.007026913359109

Time for model checking: 2.5 seconds.

Result: 6.007026913359109 (+/- 5.972365002887012E-5 estimated; rel err 9.94229772735825E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_oscillators.8-10-0.1-1-0.1-1.0_rep4.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 28.865 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:22:07 GMT+01:00 2026
Hostname: r23m0204.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 2 iterations in 0.07 seconds (average 0.035000, setup 0.00)

Time for model construction: 24.187 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Prob0: 15 iterations in 0.72 seconds (average 0.048000, setup 0.00)

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

Jacobi: 3153 iterations in 1.03 seconds (average 0.000146, setup 0.57)

Value in the initial state: 6.007026913359109

Time for model checking: 1.989 seconds.

Result: 6.007026913359109 (+/- 5.972365002887012E-5 estimated; rel err 9.94229772735825E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_oscillators.8-10-0.1-1-0.1-1.0_rep5.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 33.536 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:58:25 GMT+01:00 2026
Hostname: n23m0127.hpc.itc.rwth-aachen.de
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

Time for model construction: 28.232 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Prob0: 15 iterations in 0.67 seconds (average 0.044667, setup 0.00)

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

Jacobi: 3153 iterations in 1.26 seconds (average 0.000184, setup 0.68)

Value in the initial state: 6.007026913359109

Time for model checking: 2.149 seconds.

Result: 6.007026913359109 (+/- 5.972365002887012E-5 estimated; rel err 9.94229772735825E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

