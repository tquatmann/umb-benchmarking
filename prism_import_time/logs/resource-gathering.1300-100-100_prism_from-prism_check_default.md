# Log files

Tool configuration: prism_from-prism_check_default
Benchmark: [resource-gathering.1300-100-100](../../models/resource-gathering.1300-100-100)
Parsed values: [0.461, 0.468, 0.4, 0.392, 0.429]



### Log file: prism_from-prism_check_default_resource-gathering.1300-100-100_rep1.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism models/resource-gathering.1300-100-100/property.props
Wallclock time: 19.805 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:54:07 GMT+01:00 2026
Hostname: n23m0215.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/resource-gathering.1300-100-100/model.prism models/resource-gathering.1300-100-100/property.props

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Parsing properties file "models/resource-gathering.1300-100-100/property.props"...

1 property:
(1) "prgoldgem": Pmax=? [ F<=1300 "success" ]

---------------------------------------------------------------------

Model checking: "prgoldgem": Pmax=? [ F<=1300 "success" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1215 iterations in 0.38 seconds (average 0.000313, setup 0.00)

Time for model construction: 0.461 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Prob0A: 1203 iterations in 0.57 seconds (average 0.000474, setup 0.00)

yes = 94, no = 0, maybe = 958800

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=23, nodes=2605] [122.1 KB]
Adding sparse bits... [levels=15-16, num=44, compact=4/4] [2.8 MB]
Creating vector for yes... [dist=2, compact] [1.8 MB]
Allocating iteration vectors... [3 x 7.3 MB]
TOTAL: [26.7 MB]

Starting iterations...
Iteration 353 (of 1300): 5.01 sec so far
Iteration 724 (of 1300): 10.02 sec so far
Iteration 1106 (of 1300): 15.03 sec so far

Iterative method: 1300 iterations in 17.55 seconds (average 0.013485, setup 0.02)

Value in the initial state: 0.6630608525241822

Time for model checking: 18.184 seconds.

Result: 0.6630608525241822 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_resource-gathering.1300-100-100_rep2.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism models/resource-gathering.1300-100-100/property.props
Wallclock time: 21.385 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:07:38 GMT+01:00 2026
Hostname: n23m0057.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/resource-gathering.1300-100-100/model.prism models/resource-gathering.1300-100-100/property.props

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Parsing properties file "models/resource-gathering.1300-100-100/property.props"...

1 property:
(1) "prgoldgem": Pmax=? [ F<=1300 "success" ]

---------------------------------------------------------------------

Model checking: "prgoldgem": Pmax=? [ F<=1300 "success" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1215 iterations in 0.44 seconds (average 0.000362, setup 0.00)

Time for model construction: 0.468 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Prob0A: 1203 iterations in 0.65 seconds (average 0.000540, setup 0.00)

yes = 94, no = 0, maybe = 958800

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=23, nodes=2605] [122.1 KB]
Adding sparse bits... [levels=15-16, num=44, compact=4/4] [2.8 MB]
Creating vector for yes... [dist=2, compact] [1.8 MB]
Allocating iteration vectors... [3 x 7.3 MB]
TOTAL: [26.7 MB]

Starting iterations...
Iteration 358 (of 1300): 5.01 sec so far
Iteration 678 (of 1300): 10.03 sec so far
Iteration 986 (of 1300): 15.05 sec so far

Iterative method: 1300 iterations in 19.46 seconds (average 0.014954, setup 0.02)

Value in the initial state: 0.6630608525241822

Time for model checking: 20.194 seconds.

Result: 0.6630608525241822 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_resource-gathering.1300-100-100_rep3.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism models/resource-gathering.1300-100-100/property.props
Wallclock time: 18.293 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:06:36 GMT+01:00 2026
Hostname: n23m0386.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/resource-gathering.1300-100-100/model.prism models/resource-gathering.1300-100-100/property.props

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Parsing properties file "models/resource-gathering.1300-100-100/property.props"...

1 property:
(1) "prgoldgem": Pmax=? [ F<=1300 "success" ]

---------------------------------------------------------------------

Model checking: "prgoldgem": Pmax=? [ F<=1300 "success" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1215 iterations in 0.38 seconds (average 0.000313, setup 0.00)

Time for model construction: 0.4 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Prob0A: 1203 iterations in 0.56 seconds (average 0.000466, setup 0.00)

yes = 94, no = 0, maybe = 958800

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=23, nodes=2605] [122.1 KB]
Adding sparse bits... [levels=15-16, num=44, compact=4/4] [2.8 MB]
Creating vector for yes... [dist=2, compact] [1.8 MB]
Allocating iteration vectors... [3 x 7.3 MB]
TOTAL: [26.7 MB]

Starting iterations...
Iteration 386 (of 1300): 5.01 sec so far
Iteration 773 (of 1300): 10.02 sec so far
Iteration 1167 (of 1300): 15.03 sec so far

Iterative method: 1300 iterations in 16.72 seconds (average 0.012846, setup 0.02)

Value in the initial state: 0.6630608525241822

Time for model checking: 17.334 seconds.

Result: 0.6630608525241822 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_resource-gathering.1300-100-100_rep4.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism models/resource-gathering.1300-100-100/property.props
Wallclock time: 18.620 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:21 GMT+01:00 2026
Hostname: n23m0114.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/resource-gathering.1300-100-100/model.prism models/resource-gathering.1300-100-100/property.props

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Parsing properties file "models/resource-gathering.1300-100-100/property.props"...

1 property:
(1) "prgoldgem": Pmax=? [ F<=1300 "success" ]

---------------------------------------------------------------------

Model checking: "prgoldgem": Pmax=? [ F<=1300 "success" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1215 iterations in 0.36 seconds (average 0.000296, setup 0.00)

Time for model construction: 0.392 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Prob0A: 1203 iterations in 0.54 seconds (average 0.000449, setup 0.00)

yes = 94, no = 0, maybe = 958800

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=23, nodes=2605] [122.1 KB]
Adding sparse bits... [levels=15-16, num=44, compact=4/4] [2.8 MB]
Creating vector for yes... [dist=2, compact] [1.8 MB]
Allocating iteration vectors... [3 x 7.3 MB]
TOTAL: [26.7 MB]

Starting iterations...
Iteration 385 (of 1300): 5.02 sec so far
Iteration 770 (of 1300): 10.04 sec so far
Iteration 1153 (of 1300): 15.06 sec so far

Iterative method: 1300 iterations in 17.01 seconds (average 0.013069, setup 0.02)

Value in the initial state: 0.6630608525241822

Time for model checking: 17.583 seconds.

Result: 0.6630608525241822 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_resource-gathering.1300-100-100_rep5.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism models/resource-gathering.1300-100-100/property.props
Wallclock time: 20.429 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:03:34 GMT+01:00 2026
Hostname: n23m0341.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/resource-gathering.1300-100-100/model.prism models/resource-gathering.1300-100-100/property.props

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Parsing properties file "models/resource-gathering.1300-100-100/property.props"...

1 property:
(1) "prgoldgem": Pmax=? [ F<=1300 "success" ]

---------------------------------------------------------------------

Model checking: "prgoldgem": Pmax=? [ F<=1300 "success" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1215 iterations in 0.40 seconds (average 0.000329, setup 0.00)

Time for model construction: 0.429 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Prob0A: 1203 iterations in 0.57 seconds (average 0.000474, setup 0.00)

yes = 94, no = 0, maybe = 958800

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=23, nodes=2605] [122.1 KB]
Adding sparse bits... [levels=15-16, num=44, compact=4/4] [2.8 MB]
Creating vector for yes... [dist=2, compact] [1.8 MB]
Allocating iteration vectors... [3 x 7.3 MB]
TOTAL: [26.7 MB]

Starting iterations...
Iteration 347 (of 1300): 5.02 sec so far
Iteration 694 (of 1300): 10.03 sec so far
Iteration 1039 (of 1300): 15.04 sec so far

Iterative method: 1300 iterations in 18.79 seconds (average 0.014431, setup 0.03)

Value in the initial state: 0.6630608525241822

Time for model checking: 19.424 seconds.

Result: 0.6630608525241822 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

