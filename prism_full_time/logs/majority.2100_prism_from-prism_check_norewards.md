# Log files for prism_from-prism_check_norewards on model [majority.2100](../../models/majority.2100)

Parsed values: `[85.24, 56.249, 59.505, 61.168, 57.269]`



### Log file: prism_from-prism_check_norewards_majority.2100_rep1.log

```
Command(s):
../bin/prism  models/majority.2100/model.prism models/majority.2100/property.props
Wallclock time: 85.240 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:52:03 GMT+01:00 2026
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

Reachability (BFS): 44 iterations in 0.03 seconds (average 0.000682, setup 0.00)

Time for model construction: 49.366 seconds.

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
Iteration 1192 (of 7610): max relative diff=0.005190, 5.01 sec so far
Iteration 2386 (of 7610): max relative diff=0.001062, 10.02 sec so far
Iteration 3585 (of 7610): max relative diff=0.000479, 15.03 sec so far
Iteration 4785 (of 7610): max relative diff=0.000302, 20.04 sec so far
Iteration 5989 (of 7610): max relative diff=0.000219, 25.05 sec so far
Iteration 7134 (of 7610): max relative diff=0.000173, 30.06 sec so far

Iterative method: 7610 iterations in 34.55 seconds (average 0.004227, setup 2.38)

Value in the initial state: 0.05429919316250449

Time for model checking: 34.655 seconds.

Result: 0.05429919316250449


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_majority.2100_rep2.log

```
Command(s):
../bin/prism  models/majority.2100/model.prism models/majority.2100/property.props
Wallclock time: 56.249 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:06 GMT+01:00 2026
Hostname: r23m0099.hpc.itc.rwth-aachen.de
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

Time for model construction: 28.582 seconds.

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
Iteration 1553 (of 7610): max relative diff=0.002674, 5.01 sec so far
Iteration 3109 (of 7610): max relative diff=0.000621, 10.02 sec so far
Iteration 4660 (of 7610): max relative diff=0.000314, 15.03 sec so far
Iteration 6216 (of 7610): max relative diff=0.000208, 20.04 sec so far

Iterative method: 7610 iterations in 26.69 seconds (average 0.003238, setup 2.05)

Value in the initial state: 0.05429919316250449

Time for model checking: 26.741 seconds.

Result: 0.05429919316250449


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_majority.2100_rep3.log

```
Command(s):
../bin/prism  models/majority.2100/model.prism models/majority.2100/property.props
Wallclock time: 59.505 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:28:12 GMT+01:00 2026
Hostname: r23m0203.hpc.itc.rwth-aachen.de
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

Time for model construction: 31.739 seconds.

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
Iteration 4637 (of 7610): max relative diff=0.000316, 15.03 sec so far
Iteration 6185 (of 7610): max relative diff=0.000209, 20.04 sec so far

Iterative method: 7610 iterations in 26.87 seconds (average 0.003261, setup 2.05)

Value in the initial state: 0.05429919316250449

Time for model checking: 26.936 seconds.

Result: 0.05429919316250449


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_majority.2100_rep4.log

```
Command(s):
../bin/prism  models/majority.2100/model.prism models/majority.2100/property.props
Wallclock time: 61.168 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:05 GMT+01:00 2026
Hostname: n23m0153.hpc.itc.rwth-aachen.de
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
Iteration 1546 (of 7610): max relative diff=0.002700, 5.01 sec so far
Iteration 3089 (of 7610): max relative diff=0.000628, 10.02 sec so far
Iteration 4636 (of 7610): max relative diff=0.000316, 15.03 sec so far
Iteration 6185 (of 7610): max relative diff=0.000209, 20.04 sec so far

Iterative method: 7610 iterations in 26.80 seconds (average 0.003254, setup 2.04)

Value in the initial state: 0.05429919316250449

Time for model checking: 26.863 seconds.

Result: 0.05429919316250449


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_majority.2100_rep5.log

```
Command(s):
../bin/prism  models/majority.2100/model.prism models/majority.2100/property.props
Wallclock time: 57.269 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:38:22 GMT+01:00 2026
Hostname: n23m0190.hpc.itc.rwth-aachen.de
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

Time for model construction: 29.119 seconds.

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
Iteration 1554 (of 7610): max relative diff=0.002671, 5.01 sec so far
Iteration 3094 (of 7610): max relative diff=0.000626, 10.02 sec so far
Iteration 4642 (of 7610): max relative diff=0.000316, 15.03 sec so far
Iteration 6189 (of 7610): max relative diff=0.000209, 20.04 sec so far

Iterative method: 7610 iterations in 26.76 seconds (average 0.003248, setup 2.04)

Value in the initial state: 0.05429919316250449

Time for model checking: 26.849 seconds.

Result: 0.05429919316250449


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

