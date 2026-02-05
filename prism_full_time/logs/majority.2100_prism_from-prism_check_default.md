# Log files

Tool configuration: prism_from-prism_check_default
Benchmark: [majority.2100](../../models/majority.2100)
Parsed values: [58.751, 82.33, 61.948, 64.148, 59.618]



### Log file: prism_from-prism_check_default_majority.2100_rep1.log

```
Command(s):
../bin/prism  models/majority.2100/model.prism models/majority.2100/property.props
Wallclock time: 58.751 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:49:58 GMT+01:00 2026
Hostname: n23m0201.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/majority.2100/model.prism models/majority.2100/property.props

Parsing PRISM model file "models/majority.2100/model.prism"...

Type:        CTMC
Modules:     D_def Y_def Z_def CC_def XX_def EE_def
Actions:     []
Variables:   D Y Z CC XX EE
Labels:      "target"

Parsing properties file "models/majority.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 0.02 seconds (average 0.000455, setup 0.00)

Time for model construction: 29.601 seconds.

Type:        CTMC
States:      192000 (1 initial)
Transitions: 1961600

Rate matrix: 9569 nodes (85 terminal), 1961600 minterms, vars: 43r/43c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 189000 of 192000 (98.4%)

Building hybrid MTBDD matrix... [levels=43, nodes=12162] [570.1 KB]
Adding explicit sparse matrices... [levels=23, num=71, compact] [696.5 KB]
Creating vector for diagonals... [1.5 MB]
Allocating iteration vectors... [3 x 1.5 MB]
TOTAL: [7.1 MB]

Uniformisation: q.t = 3.287227 x 2100.000000 = 6903.175850
Fox-Glynn: left = 6319, right = 7610

Starting iterations...
Iteration 1501 (of 7610): max relative diff=0.002871, 5.01 sec so far
Iteration 3009 (of 7610): max relative diff=0.000661, 10.02 sec so far
Iteration 4519 (of 7610): max relative diff=0.000329, 15.03 sec so far
Iteration 6029 (of 7610): max relative diff=0.000217, 20.04 sec so far
Iteration 7508 (of 7610): max relative diff=0.000162, 25.05 sec so far

Iterative method: 7610 iterations in 27.65 seconds (average 0.003338, setup 2.25)

Value in the initial state: 0.05429919316250449

Time for model checking: 27.754 seconds.

Result: 0.05429919316250449


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_majority.2100_rep2.log

```
Command(s):
../bin/prism  models/majority.2100/model.prism models/majority.2100/property.props
Wallclock time: 82.330 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:50:56 GMT+01:00 2026
Hostname: r23m0196.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/majority.2100/model.prism models/majority.2100/property.props

Parsing PRISM model file "models/majority.2100/model.prism"...

Type:        CTMC
Modules:     D_def Y_def Z_def CC_def XX_def EE_def
Actions:     []
Variables:   D Y Z CC XX EE
Labels:      "target"

Parsing properties file "models/majority.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 0.02 seconds (average 0.000455, setup 0.00)

Time for model construction: 47.259 seconds.

Type:        CTMC
States:      192000 (1 initial)
Transitions: 1961600

Rate matrix: 9569 nodes (85 terminal), 1961600 minterms, vars: 43r/43c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 189000 of 192000 (98.4%)

Building hybrid MTBDD matrix... [levels=43, nodes=12162] [570.1 KB]
Adding explicit sparse matrices... [levels=23, num=71, compact] [696.5 KB]
Creating vector for diagonals... [1.5 MB]
Allocating iteration vectors... [3 x 1.5 MB]
TOTAL: [7.1 MB]

Uniformisation: q.t = 3.287227 x 2100.000000 = 6903.175850
Fox-Glynn: left = 6319, right = 7610

Starting iterations...
Iteration 1243 (of 7610): max relative diff=0.004671, 5.01 sec so far
Iteration 2484 (of 7610): max relative diff=0.000975, 10.02 sec so far
Iteration 3711 (of 7610): max relative diff=0.000452, 15.03 sec so far
Iteration 4937 (of 7610): max relative diff=0.000288, 20.04 sec so far
Iteration 6161 (of 7610): max relative diff=0.000211, 25.05 sec so far
Iteration 7328 (of 7610): max relative diff=0.000167, 30.06 sec so far

Iterative method: 7610 iterations in 33.75 seconds (average 0.004106, setup 2.50)

Value in the initial state: 0.05429919316250449

Time for model checking: 33.912 seconds.

Result: 0.05429919316250449


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_majority.2100_rep3.log

```
Command(s):
../bin/prism  models/majority.2100/model.prism models/majority.2100/property.props
Wallclock time: 61.948 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:50:57 GMT+01:00 2026
Hostname: n23m0254.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/majority.2100/model.prism models/majority.2100/property.props

Parsing PRISM model file "models/majority.2100/model.prism"...

Type:        CTMC
Modules:     D_def Y_def Z_def CC_def XX_def EE_def
Actions:     []
Variables:   D Y Z CC XX EE
Labels:      "target"

Parsing properties file "models/majority.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 0.01 seconds (average 0.000227, setup 0.00)

Time for model construction: 33.19 seconds.

Type:        CTMC
States:      192000 (1 initial)
Transitions: 1961600

Rate matrix: 9569 nodes (85 terminal), 1961600 minterms, vars: 43r/43c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 189000 of 192000 (98.4%)

Building hybrid MTBDD matrix... [levels=43, nodes=12162] [570.1 KB]
Adding explicit sparse matrices... [levels=23, num=71, compact] [696.5 KB]
Creating vector for diagonals... [1.5 MB]
Allocating iteration vectors... [3 x 1.5 MB]
TOTAL: [7.1 MB]

Uniformisation: q.t = 3.287227 x 2100.000000 = 6903.175850
Fox-Glynn: left = 6319, right = 7610

Starting iterations...
Iteration 1552 (of 7610): max relative diff=0.002678, 5.01 sec so far
Iteration 3104 (of 7610): max relative diff=0.000622, 10.02 sec so far
Iteration 4660 (of 7610): max relative diff=0.000314, 15.03 sec so far
Iteration 6215 (of 7610): max relative diff=0.000208, 20.04 sec so far

Iterative method: 7610 iterations in 26.77 seconds (average 0.003248, setup 2.05)

Value in the initial state: 0.05429919316250449

Time for model checking: 26.853 seconds.

Result: 0.05429919316250449


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_majority.2100_rep4.log

```
Command(s):
../bin/prism  models/majority.2100/model.prism models/majority.2100/property.props
Wallclock time: 64.148 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:01:31 GMT+01:00 2026
Hostname: n23m0185.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/majority.2100/model.prism models/majority.2100/property.props

Parsing PRISM model file "models/majority.2100/model.prism"...

Type:        CTMC
Modules:     D_def Y_def Z_def CC_def XX_def EE_def
Actions:     []
Variables:   D Y Z CC XX EE
Labels:      "target"

Parsing properties file "models/majority.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 0.02 seconds (average 0.000455, setup 0.00)

Time for model construction: 30.914 seconds.

Type:        CTMC
States:      192000 (1 initial)
Transitions: 1961600

Rate matrix: 9569 nodes (85 terminal), 1961600 minterms, vars: 43r/43c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 189000 of 192000 (98.4%)

Building hybrid MTBDD matrix... [levels=43, nodes=12162] [570.1 KB]
Adding explicit sparse matrices... [levels=23, num=71, compact] [696.5 KB]
Creating vector for diagonals... [1.5 MB]
Allocating iteration vectors... [3 x 1.5 MB]
TOTAL: [7.1 MB]

Uniformisation: q.t = 3.287227 x 2100.000000 = 6903.175850
Fox-Glynn: left = 6319, right = 7610

Starting iterations...
Iteration 1303 (of 7610): max relative diff=0.004127, 5.01 sec so far
Iteration 2607 (of 7610): max relative diff=0.000881, 10.02 sec so far
Iteration 3912 (of 7610): max relative diff=0.000413, 15.03 sec so far
Iteration 5219 (of 7610): max relative diff=0.000266, 20.04 sec so far
Iteration 6515 (of 7610): max relative diff=0.000195, 25.05 sec so far

Iterative method: 7610 iterations in 31.80 seconds (average 0.003859, setup 2.43)

Value in the initial state: 0.05429919316250449

Time for model checking: 31.903 seconds.

Result: 0.05429919316250449


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_majority.2100_rep5.log

```
Command(s):
../bin/prism  models/majority.2100/model.prism models/majority.2100/property.props
Wallclock time: 59.618 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:01 GMT+01:00 2026
Hostname: r23m0176.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/majority.2100/model.prism models/majority.2100/property.props

Parsing PRISM model file "models/majority.2100/model.prism"...

Type:        CTMC
Modules:     D_def Y_def Z_def CC_def XX_def EE_def
Actions:     []
Variables:   D Y Z CC XX EE
Labels:      "target"

Parsing properties file "models/majority.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 0.02 seconds (average 0.000455, setup 0.00)

Time for model construction: 31.234 seconds.

Type:        CTMC
States:      192000 (1 initial)
Transitions: 1961600

Rate matrix: 9569 nodes (85 terminal), 1961600 minterms, vars: 43r/43c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 189000 of 192000 (98.4%)

Building hybrid MTBDD matrix... [levels=43, nodes=12162] [570.1 KB]
Adding explicit sparse matrices... [levels=23, num=71, compact] [696.5 KB]
Creating vector for diagonals... [1.5 MB]
Allocating iteration vectors... [3 x 1.5 MB]
TOTAL: [7.1 MB]

Uniformisation: q.t = 3.287227 x 2100.000000 = 6903.175850
Fox-Glynn: left = 6319, right = 7610

Starting iterations...
Iteration 1511 (of 7610): max relative diff=0.002831, 5.01 sec so far
Iteration 3058 (of 7610): max relative diff=0.000640, 10.02 sec so far
Iteration 4614 (of 7610): max relative diff=0.000319, 15.03 sec so far
Iteration 6170 (of 7610): max relative diff=0.000210, 20.04 sec so far

Iterative method: 7610 iterations in 26.94 seconds (average 0.003264, setup 2.10)

Value in the initial state: 0.05429919316250449

Time for model checking: 27.03 seconds.

Result: 0.05429919316250449


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

