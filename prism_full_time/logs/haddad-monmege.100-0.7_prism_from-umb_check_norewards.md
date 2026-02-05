# Log files for prism_from-umb_check_norewards on model [haddad-monmege.100-0.7](../../models/haddad-monmege.100-0.7)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-umb_check_norewards_haddad-monmege.100-0.7_rep1.log

```
Command(s):
../bin/prism  -importmodel models/haddad-monmege.100-0.7/prism.model.umb models/haddad-monmege.100-0.7/property.props
Wallclock time: 0.661 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:20:45 GMT+01:00 2026
Hostname: r23m0077.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/haddad-monmege.100-0.7/prism.model.umb models/haddad-monmege.100-0.7/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     []
Variables:   x
Labels:      "Target"

Parsing properties file "models/haddad-monmege.100-0.7/property.props"...

1 property:
(1) "target": P=? [ F "Target" ]

---------------------------------------------------------------------

Model checking: "target": P=? [ F "Target" ]

Building model (engine:symbolic)...
Importing transitions... [ 100% ]

Computing reachable states...

Reachability (BFS): 101 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.027 seconds.

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



### Log file: prism_from-umb_check_norewards_haddad-monmege.100-0.7_rep2.log

```
Command(s):
../bin/prism  -importmodel models/haddad-monmege.100-0.7/prism.model.umb models/haddad-monmege.100-0.7/property.props
Wallclock time: 4.014 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:40 GMT+01:00 2026
Hostname: r23m0122.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/haddad-monmege.100-0.7/prism.model.umb models/haddad-monmege.100-0.7/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     []
Variables:   x
Labels:      "Target"

Parsing properties file "models/haddad-monmege.100-0.7/property.props"...

1 property:
(1) "target": P=? [ F "Target" ]

---------------------------------------------------------------------

Model checking: "target": P=? [ F "Target" ]

Building model (engine:symbolic)...
Importing transitions... [ 100% ]

Computing reachable states...

Reachability (BFS): 101 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.038 seconds.

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



### Log file: prism_from-umb_check_norewards_haddad-monmege.100-0.7_rep3.log

```
Command(s):
../bin/prism  -importmodel models/haddad-monmege.100-0.7/prism.model.umb models/haddad-monmege.100-0.7/property.props
Wallclock time: 0.900 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:03 GMT+01:00 2026
Hostname: n23m0175.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/haddad-monmege.100-0.7/prism.model.umb models/haddad-monmege.100-0.7/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     []
Variables:   x
Labels:      "Target"

Parsing properties file "models/haddad-monmege.100-0.7/property.props"...

1 property:
(1) "target": P=? [ F "Target" ]

---------------------------------------------------------------------

Model checking: "target": P=? [ F "Target" ]

Building model (engine:symbolic)...
Importing transitions... [ 100% ]

Computing reachable states...

Reachability (BFS): 101 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.041 seconds.

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

Jacobi: 10000 iterations in 0.01 seconds (average 0.000000, setup 0.01)

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_haddad-monmege.100-0.7_rep4.log

```
Command(s):
../bin/prism  -importmodel models/haddad-monmege.100-0.7/prism.model.umb models/haddad-monmege.100-0.7/property.props
Wallclock time: 1.223 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:36:46 GMT+01:00 2026
Hostname: n23m0328.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/haddad-monmege.100-0.7/prism.model.umb models/haddad-monmege.100-0.7/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     []
Variables:   x
Labels:      "Target"

Parsing properties file "models/haddad-monmege.100-0.7/property.props"...

1 property:
(1) "target": P=? [ F "Target" ]

---------------------------------------------------------------------

Model checking: "target": P=? [ F "Target" ]

Building model (engine:symbolic)...
Importing transitions... [ 100% ]

Computing reachable states...

Reachability (BFS): 101 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.044 seconds.

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



### Log file: prism_from-umb_check_norewards_haddad-monmege.100-0.7_rep5.log

```
Command(s):
../bin/prism  -importmodel models/haddad-monmege.100-0.7/prism.model.umb models/haddad-monmege.100-0.7/property.props
Wallclock time: 0.573 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:25 GMT+01:00 2026
Hostname: n23m0175.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/haddad-monmege.100-0.7/prism.model.umb models/haddad-monmege.100-0.7/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     []
Variables:   x
Labels:      "Target"

Parsing properties file "models/haddad-monmege.100-0.7/property.props"...

1 property:
(1) "target": P=? [ F "Target" ]

---------------------------------------------------------------------

Model checking: "target": P=? [ F "Target" ]

Building model (engine:symbolic)...
Importing transitions... [ 100% ]

Computing reachable states...

Reachability (BFS): 101 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.024 seconds.

Type:        DTMC
States:      201 (1 initial)
Transitions: 400

Transition matrix: 131 nodes (5 terminal), 400 minterms, vars: 8r/8c

Prob0: 102 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 102 iterations in 0.01 seconds (average 0.000098, setup 0.00)

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

