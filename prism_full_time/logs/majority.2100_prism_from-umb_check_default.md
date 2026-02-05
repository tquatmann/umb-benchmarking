# Log files

Tool configuration: prism_from-umb_check_default
Benchmark: [majority.2100](../../models/majority.2100)
Parsed values: [82.929, 90.792, 90.405, 82.531, 89.573]



### Log file: prism_from-umb_check_default_majority.2100_rep1.log

```
Command(s):
../bin/prism  -importmodel models/majority.2100/prism.model.umb models/majority.2100/property.props
Wallclock time: 82.929 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:48:55 GMT+01:00 2026
Hostname: n23m0379.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/majority.2100/prism.model.umb models/majority.2100/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/majority.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 4% 10% 18% 24% 30% 36% 42% 48% 54% 60% 66% 72% 78% 84% 90% 96% 100% ]

Computing reachable states...

Reachability (BFS): 44 iterations in 0.07 seconds (average 0.001591, setup 0.00)

Time for model construction: 49.19 seconds.

Type:        CTMC
States:      192000 (1 initial)
Transitions: 1961600

Rate matrix: 5862 nodes (85 terminal), 1961600 minterms, vars: 18r/18c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 189000 of 192000 (98.4%)

Building hybrid MTBDD matrix... [levels=18, nodes=7680] [360.0 KB]
Adding explicit sparse matrices... [levels=9, num=256, compact] [669.6 KB]
Creating vector for diagonals... [1.5 MB]
Allocating iteration vectors... [3 x 1.5 MB]
TOTAL: [6.9 MB]

Uniformisation: q.t = 3.287227 x 2100.000000 = 6903.175850
Fox-Glynn: left = 6319, right = 7610

Starting iterations...
Iteration 1238 (of 7610): max relative diff=0.004719, 5.01 sec so far
Iteration 2480 (of 7610): max relative diff=0.000978, 10.02 sec so far
Iteration 3705 (of 7610): max relative diff=0.000453, 15.03 sec so far
Iteration 4940 (of 7610): max relative diff=0.000288, 20.04 sec so far
Iteration 6175 (of 7610): max relative diff=0.000210, 25.05 sec so far
Iteration 7395 (of 7610): max relative diff=0.000165, 30.06 sec so far

Iterative method: 7610 iterations in 32.98 seconds (average 0.004066, setup 2.04)

Value in the initial state: 0.05429919316250489

Time for model checking: 33.056 seconds.

Result: 0.05429919316250489


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_majority.2100_rep2.log

```
Command(s):
../bin/prism  -importmodel models/majority.2100/prism.model.umb models/majority.2100/property.props
Wallclock time: 90.792 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:21:34 GMT+01:00 2026
Hostname: n23m0295.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/majority.2100/prism.model.umb models/majority.2100/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/majority.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 4% 10% 16% 22% 26% 32% 38% 44% 50% 54% 60% 66% 72% 78% 82% 88% 94% 100% ]

Computing reachable states...

Reachability (BFS): 44 iterations in 0.07 seconds (average 0.001591, setup 0.00)

Time for model construction: 53.886 seconds.

Type:        CTMC
States:      192000 (1 initial)
Transitions: 1961600

Rate matrix: 5862 nodes (85 terminal), 1961600 minterms, vars: 18r/18c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 189000 of 192000 (98.4%)

Building hybrid MTBDD matrix... [levels=18, nodes=7680] [360.0 KB]
Adding explicit sparse matrices... [levels=9, num=256, compact] [669.6 KB]
Creating vector for diagonals... [1.5 MB]
Allocating iteration vectors... [3 x 1.5 MB]
TOTAL: [6.9 MB]

Uniformisation: q.t = 3.287227 x 2100.000000 = 6903.175850
Fox-Glynn: left = 6319, right = 7610

Starting iterations...
Iteration 1144 (of 7610): max relative diff=0.005732, 5.01 sec so far
Iteration 2285 (of 7610): max relative diff=0.001165, 10.02 sec so far
Iteration 3427 (of 7610): max relative diff=0.000519, 15.03 sec so far
Iteration 4565 (of 7610): max relative diff=0.000324, 20.04 sec so far
Iteration 5697 (of 7610): max relative diff=0.000235, 25.05 sec so far
Iteration 6804 (of 7610): max relative diff=0.000184, 30.06 sec so far

Iterative method: 7610 iterations in 35.91 seconds (average 0.004428, setup 2.21)

Value in the initial state: 0.05429919316250489

Time for model checking: 36.058 seconds.

Result: 0.05429919316250489


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_majority.2100_rep3.log

```
Command(s):
../bin/prism  -importmodel models/majority.2100/prism.model.umb models/majority.2100/property.props
Wallclock time: 90.405 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:22:15 GMT+01:00 2026
Hostname: n23m0053.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/majority.2100/prism.model.umb models/majority.2100/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/majority.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 4% 10% 16% 22% 28% 34% 38% 44% 50% 56% 62% 66% 72% 78% 84% 88% 94% 100% ]

Computing reachable states...

Reachability (BFS): 44 iterations in 0.07 seconds (average 0.001591, setup 0.00)

Time for model construction: 53.727 seconds.

Type:        CTMC
States:      192000 (1 initial)
Transitions: 1961600

Rate matrix: 5862 nodes (85 terminal), 1961600 minterms, vars: 18r/18c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 189000 of 192000 (98.4%)

Building hybrid MTBDD matrix... [levels=18, nodes=7680] [360.0 KB]
Adding explicit sparse matrices... [levels=9, num=256, compact] [669.6 KB]
Creating vector for diagonals... [1.5 MB]
Allocating iteration vectors... [3 x 1.5 MB]
TOTAL: [6.9 MB]

Uniformisation: q.t = 3.287227 x 2100.000000 = 6903.175850
Fox-Glynn: left = 6319, right = 7610

Starting iterations...
Iteration 1106 (of 7610): max relative diff=0.006203, 5.01 sec so far
Iteration 2263 (of 7610): max relative diff=0.001190, 10.02 sec so far
Iteration 3356 (of 7610): max relative diff=0.000539, 15.03 sec so far
Iteration 4479 (of 7610): max relative diff=0.000333, 20.04 sec so far
Iteration 5612 (of 7610): max relative diff=0.000240, 25.05 sec so far
Iteration 6804 (of 7610): max relative diff=0.000184, 30.06 sec so far

Iterative method: 7610 iterations in 35.89 seconds (average 0.004403, setup 2.38)

Value in the initial state: 0.05429919316250489

Time for model checking: 36.062 seconds.

Result: 0.05429919316250489


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_majority.2100_rep4.log

```
Command(s):
../bin/prism  -importmodel models/majority.2100/prism.model.umb models/majority.2100/property.props
Wallclock time: 82.531 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:30 GMT+01:00 2026
Hostname: n23m0132.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/majority.2100/prism.model.umb models/majority.2100/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/majority.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 4% 10% 18% 24% 30% 36% 42% 48% 54% 60% 66% 72% 78% 84% 90% 98% 100% ]

Computing reachable states...

Reachability (BFS): 44 iterations in 0.05 seconds (average 0.001136, setup 0.00)

Time for model construction: 49.054 seconds.

Type:        CTMC
States:      192000 (1 initial)
Transitions: 1961600

Rate matrix: 5862 nodes (85 terminal), 1961600 minterms, vars: 18r/18c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 189000 of 192000 (98.4%)

Building hybrid MTBDD matrix... [levels=18, nodes=7680] [360.0 KB]
Adding explicit sparse matrices... [levels=9, num=256, compact] [669.6 KB]
Creating vector for diagonals... [1.5 MB]
Allocating iteration vectors... [3 x 1.5 MB]
TOTAL: [6.9 MB]

Uniformisation: q.t = 3.287227 x 2100.000000 = 6903.175850
Fox-Glynn: left = 6319, right = 7610

Starting iterations...
Iteration 1240 (of 7610): max relative diff=0.004700, 5.01 sec so far
Iteration 2483 (of 7610): max relative diff=0.000975, 10.02 sec so far
Iteration 3726 (of 7610): max relative diff=0.000449, 15.03 sec so far
Iteration 4970 (of 7610): max relative diff=0.000285, 20.04 sec so far
Iteration 6210 (of 7610): max relative diff=0.000208, 25.05 sec so far
Iteration 7431 (of 7610): max relative diff=0.000164, 30.06 sec so far

Iterative method: 7610 iterations in 32.81 seconds (average 0.004046, setup 2.02)

Value in the initial state: 0.05429919316250489

Time for model checking: 32.873 seconds.

Result: 0.05429919316250489


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_majority.2100_rep5.log

```
Command(s):
../bin/prism  -importmodel models/majority.2100/prism.model.umb models/majority.2100/property.props
Wallclock time: 89.573 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:08:49 GMT+01:00 2026
Hostname: n23m0396.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/majority.2100/prism.model.umb models/majority.2100/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/majority.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 4% 10% 16% 22% 26% 32% 38% 44% 50% 54% 60% 66% 72% 78% 82% 88% 94% 98% 100% ]

Computing reachable states...

Reachability (BFS): 44 iterations in 0.08 seconds (average 0.001818, setup 0.00)

Time for model construction: 54.162 seconds.

Type:        CTMC
States:      192000 (1 initial)
Transitions: 1961600

Rate matrix: 5862 nodes (85 terminal), 1961600 minterms, vars: 18r/18c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 189000 of 192000 (98.4%)

Building hybrid MTBDD matrix... [levels=18, nodes=7680] [360.0 KB]
Adding explicit sparse matrices... [levels=9, num=256, compact] [669.6 KB]
Creating vector for diagonals... [1.5 MB]
Allocating iteration vectors... [3 x 1.5 MB]
TOTAL: [6.9 MB]

Uniformisation: q.t = 3.287227 x 2100.000000 = 6903.175850
Fox-Glynn: left = 6319, right = 7610

Starting iterations...
Iteration 1195 (of 7610): max relative diff=0.005158, 5.01 sec so far
Iteration 2388 (of 7610): max relative diff=0.001060, 10.02 sec so far
Iteration 3576 (of 7610): max relative diff=0.000481, 15.03 sec so far
Iteration 4758 (of 7610): max relative diff=0.000304, 20.04 sec so far
Iteration 5910 (of 7610): max relative diff=0.000223, 25.05 sec so far
Iteration 7083 (of 7610): max relative diff=0.000175, 30.06 sec so far

Iterative method: 7610 iterations in 34.43 seconds (average 0.004248, setup 2.10)

Value in the initial state: 0.05429919316250489

Time for model checking: 34.535 seconds.

Result: 0.05429919316250489


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

