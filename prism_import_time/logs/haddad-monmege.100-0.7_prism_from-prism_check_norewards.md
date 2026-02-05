# Log files

Tool configuration: prism_from-prism_check_norewards
Benchmark: [haddad-monmege.100-0.7](../../models/haddad-monmege.100-0.7)
Parsed values: [0.054, 0.019, 0.031, 0.031, 0.019]



### Log file: prism_from-prism_check_norewards_haddad-monmege.100-0.7_rep1.log

```
Command(s):
../bin/prism  models/haddad-monmege.100-0.7/model.prism models/haddad-monmege.100-0.7/property.props
Wallclock time: 0.641 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:32:49 GMT+01:00 2026
Hostname: r23m0206.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/haddad-monmege.100-0.7/model.prism models/haddad-monmege.100-0.7/property.props

Parsing PRISM model file "models/haddad-monmege.100-0.7/model.prism"...

Type:        DTMC
Modules:     main
Actions:     []
Variables:   x
Labels:      "Target"

Parsing properties file "models/haddad-monmege.100-0.7/property.props"...

1 property:
(1) "target": P=? [ F "Target" ]

---------------------------------------------------------------------

Model checking: "target": P=? [ F "Target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 101 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.054 seconds.

Type:        DTMC
States:      201 (1 initial)
Transitions: 400

Transition matrix: 131 nodes (5 terminal), 400 minterms, vars: 8r/8c

Prob0: 102 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 102 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1, no = 1, maybe = 199

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=8, nodes=133] [6.2 KB]
Adding explicit sparse matrices... [levels=8, num=1, compact] [1.8 KB]
Creating vector for diagonals... [dist=1, compact] [0.4 KB]
Creating vector for RHS... [dist=2, compact] [0.4 KB]
Allocating iteration vectors... [2 x 1.6 KB]
TOTAL: [12.0 KB]

Starting iterations...

Jacobi: 10000 iterations in 0.02 seconds (average 0.000002, setup 0.00)

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_haddad-monmege.100-0.7_rep2.log

```
Command(s):
../bin/prism  models/haddad-monmege.100-0.7/model.prism models/haddad-monmege.100-0.7/property.props
Wallclock time: 0.617 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:25:39 GMT+01:00 2026
Hostname: n23m0142.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/haddad-monmege.100-0.7/model.prism models/haddad-monmege.100-0.7/property.props

Parsing PRISM model file "models/haddad-monmege.100-0.7/model.prism"...

Type:        DTMC
Modules:     main
Actions:     []
Variables:   x
Labels:      "Target"

Parsing properties file "models/haddad-monmege.100-0.7/property.props"...

1 property:
(1) "target": P=? [ F "Target" ]

---------------------------------------------------------------------

Model checking: "target": P=? [ F "Target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 101 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.019 seconds.

Type:        DTMC
States:      201 (1 initial)
Transitions: 400

Transition matrix: 131 nodes (5 terminal), 400 minterms, vars: 8r/8c

Prob0: 102 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 102 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1, no = 1, maybe = 199

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=8, nodes=133] [6.2 KB]
Adding explicit sparse matrices... [levels=8, num=1, compact] [1.8 KB]
Creating vector for diagonals... [dist=1, compact] [0.4 KB]
Creating vector for RHS... [dist=2, compact] [0.4 KB]
Allocating iteration vectors... [2 x 1.6 KB]
TOTAL: [12.0 KB]

Starting iterations...

Jacobi: 10000 iterations in 0.01 seconds (average 0.000001, setup 0.00)

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_haddad-monmege.100-0.7_rep3.log

```
Command(s):
../bin/prism  models/haddad-monmege.100-0.7/model.prism models/haddad-monmege.100-0.7/property.props
Wallclock time: 2.559 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:24:08 GMT+01:00 2026
Hostname: n23m0117.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/haddad-monmege.100-0.7/model.prism models/haddad-monmege.100-0.7/property.props

Parsing PRISM model file "models/haddad-monmege.100-0.7/model.prism"...

Type:        DTMC
Modules:     main
Actions:     []
Variables:   x
Labels:      "Target"

Parsing properties file "models/haddad-monmege.100-0.7/property.props"...

1 property:
(1) "target": P=? [ F "Target" ]

---------------------------------------------------------------------

Model checking: "target": P=? [ F "Target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 101 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.031 seconds.

Type:        DTMC
States:      201 (1 initial)
Transitions: 400

Transition matrix: 131 nodes (5 terminal), 400 minterms, vars: 8r/8c

Prob0: 102 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 102 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1, no = 1, maybe = 199

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=8, nodes=133] [6.2 KB]
Adding explicit sparse matrices... [levels=8, num=1, compact] [1.8 KB]
Creating vector for diagonals... [dist=1, compact] [0.4 KB]
Creating vector for RHS... [dist=2, compact] [0.4 KB]
Allocating iteration vectors... [2 x 1.6 KB]
TOTAL: [12.0 KB]

Starting iterations...

Jacobi: 10000 iterations in 0.01 seconds (average 0.000001, setup 0.00)

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_haddad-monmege.100-0.7_rep4.log

```
Command(s):
../bin/prism  models/haddad-monmege.100-0.7/model.prism models/haddad-monmege.100-0.7/property.props
Wallclock time: 0.787 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:01 GMT+01:00 2026
Hostname: n23m0168.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/haddad-monmege.100-0.7/model.prism models/haddad-monmege.100-0.7/property.props

Parsing PRISM model file "models/haddad-monmege.100-0.7/model.prism"...

Type:        DTMC
Modules:     main
Actions:     []
Variables:   x
Labels:      "Target"

Parsing properties file "models/haddad-monmege.100-0.7/property.props"...

1 property:
(1) "target": P=? [ F "Target" ]

---------------------------------------------------------------------

Model checking: "target": P=? [ F "Target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 101 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.031 seconds.

Type:        DTMC
States:      201 (1 initial)
Transitions: 400

Transition matrix: 131 nodes (5 terminal), 400 minterms, vars: 8r/8c

Prob0: 102 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 102 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1, no = 1, maybe = 199

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=8, nodes=133] [6.2 KB]
Adding explicit sparse matrices... [levels=8, num=1, compact] [1.8 KB]
Creating vector for diagonals... [dist=1, compact] [0.4 KB]
Creating vector for RHS... [dist=2, compact] [0.4 KB]
Allocating iteration vectors... [2 x 1.6 KB]
TOTAL: [12.0 KB]

Starting iterations...

Jacobi: 10000 iterations in 0.01 seconds (average 0.000001, setup 0.00)

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_haddad-monmege.100-0.7_rep5.log

```
Command(s):
../bin/prism  models/haddad-monmege.100-0.7/model.prism models/haddad-monmege.100-0.7/property.props
Wallclock time: 0.669 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:49:54 GMT+01:00 2026
Hostname: n23m0288.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/haddad-monmege.100-0.7/model.prism models/haddad-monmege.100-0.7/property.props

Parsing PRISM model file "models/haddad-monmege.100-0.7/model.prism"...

Type:        DTMC
Modules:     main
Actions:     []
Variables:   x
Labels:      "Target"

Parsing properties file "models/haddad-monmege.100-0.7/property.props"...

1 property:
(1) "target": P=? [ F "Target" ]

---------------------------------------------------------------------

Model checking: "target": P=? [ F "Target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 101 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.019 seconds.

Type:        DTMC
States:      201 (1 initial)
Transitions: 400

Transition matrix: 131 nodes (5 terminal), 400 minterms, vars: 8r/8c

Prob0: 102 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 102 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1, no = 1, maybe = 199

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=8, nodes=133] [6.2 KB]
Adding explicit sparse matrices... [levels=8, num=1, compact] [1.8 KB]
Creating vector for diagonals... [dist=1, compact] [0.4 KB]
Creating vector for RHS... [dist=2, compact] [0.4 KB]
Allocating iteration vectors... [2 x 1.6 KB]
TOTAL: [12.0 KB]

Starting iterations...

Jacobi: 10000 iterations in 0.02 seconds (average 0.000002, setup 0.00)

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

