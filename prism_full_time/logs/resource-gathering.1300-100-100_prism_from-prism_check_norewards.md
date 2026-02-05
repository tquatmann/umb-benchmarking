# Log files for prism_from-prism_check_norewards on model [resource-gathering.1300-100-100](../../models/resource-gathering.1300-100-100)

Parsed values: `[18.738, 20.812, 22.614, 20.263, 25.859]`



### Log file: prism_from-prism_check_norewards_resource-gathering.1300-100-100_rep1.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism models/resource-gathering.1300-100-100/property.props
Wallclock time: 18.738 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:44:46 GMT+01:00 2026
Hostname: n23m0191.hpc.itc.rwth-aachen.de
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

Time for model construction: 0.424 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Prob0A: 1203 iterations in 0.53 seconds (average 0.000441, setup 0.00)

yes = 94, no = 0, maybe = 958800

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=23, nodes=2605] [122.1 KB]
Adding sparse bits... [levels=15-16, num=44, compact=4/4] [2.8 MB]
Creating vector for yes... [dist=2, compact] [1.8 MB]
Allocating iteration vectors... [3 x 7.3 MB]
TOTAL: [26.7 MB]

Starting iterations...
Iteration 396 (of 1300): 5.01 sec so far
Iteration 792 (of 1300): 10.02 sec so far
Iteration 1174 (of 1300): 15.03 sec so far

Iterative method: 1300 iterations in 16.64 seconds (average 0.012777, setup 0.03)

Value in the initial state: 0.6630608525241822

Time for model checking: 17.235 seconds.

Result: 0.6630608525241822 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_resource-gathering.1300-100-100_rep2.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism models/resource-gathering.1300-100-100/property.props
Wallclock time: 20.812 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:22:09 GMT+01:00 2026
Hostname: n23m0101.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 1215 iterations in 0.42 seconds (average 0.000346, setup 0.00)

Time for model construction: 0.5 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Prob0A: 1203 iterations in 0.59 seconds (average 0.000490, setup 0.00)

yes = 94, no = 0, maybe = 958800

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=23, nodes=2605] [122.1 KB]
Adding sparse bits... [levels=15-16, num=44, compact=4/4] [2.8 MB]
Creating vector for yes... [dist=2, compact] [1.8 MB]
Allocating iteration vectors... [3 x 7.3 MB]
TOTAL: [26.7 MB]

Starting iterations...
Iteration 350 (of 1300): 5.01 sec so far
Iteration 704 (of 1300): 10.02 sec so far
Iteration 1058 (of 1300): 15.03 sec so far

Iterative method: 1300 iterations in 18.40 seconds (average 0.014138, setup 0.02)

Value in the initial state: 0.6630608525241822

Time for model checking: 19.066 seconds.

Result: 0.6630608525241822 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_resource-gathering.1300-100-100_rep3.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism models/resource-gathering.1300-100-100/property.props
Wallclock time: 22.614 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:50:57 GMT+01:00 2026
Hostname: r23m0198.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 1215 iterations in 0.47 seconds (average 0.000387, setup 0.00)

Time for model construction: 0.49 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Prob0A: 1203 iterations in 0.72 seconds (average 0.000599, setup 0.00)

yes = 94, no = 0, maybe = 958800

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=23, nodes=2605] [122.1 KB]
Adding sparse bits... [levels=15-16, num=44, compact=4/4] [2.8 MB]
Creating vector for yes... [dist=2, compact] [1.8 MB]
Allocating iteration vectors... [3 x 7.3 MB]
TOTAL: [26.7 MB]

Starting iterations...
Iteration 305 (of 1300): 5.01 sec so far
Iteration 626 (of 1300): 10.02 sec so far
Iteration 950 (of 1300): 15.04 sec so far
Iteration 1266 (of 1300): 20.06 sec so far

Iterative method: 1300 iterations in 20.66 seconds (average 0.015869, setup 0.03)

Value in the initial state: 0.6630608525241822

Time for model checking: 21.466 seconds.

Result: 0.6630608525241822 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_resource-gathering.1300-100-100_rep4.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism models/resource-gathering.1300-100-100/property.props
Wallclock time: 20.263 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:24:33 GMT+01:00 2026
Hostname: n23m0051.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 1215 iterations in 0.45 seconds (average 0.000370, setup 0.00)

Time for model construction: 0.466 seconds.

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
Iteration 348 (of 1300): 5.01 sec so far
Iteration 694 (of 1300): 10.02 sec so far
Iteration 1050 (of 1300): 15.03 sec so far

Iterative method: 1300 iterations in 18.50 seconds (average 0.014208, setup 0.03)

Value in the initial state: 0.6630608525241822

Time for model checking: 19.21 seconds.

Result: 0.6630608525241822 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_resource-gathering.1300-100-100_rep5.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism models/resource-gathering.1300-100-100/property.props
Wallclock time: 25.859 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 02:56:24 GMT+01:00 2026
Hostname: r23m0015.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 1215 iterations in 0.57 seconds (average 0.000469, setup 0.00)

Time for model construction: 0.649 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Prob0A: 1203 iterations in 0.87 seconds (average 0.000723, setup 0.00)

yes = 94, no = 0, maybe = 958800

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=23, nodes=2605] [122.1 KB]
Adding sparse bits... [levels=15-16, num=44, compact=4/4] [2.8 MB]
Creating vector for yes... [dist=2, compact] [1.8 MB]
Allocating iteration vectors... [3 x 7.3 MB]
TOTAL: [26.7 MB]

Starting iterations...
Iteration 282 (of 1300): 5.02 sec so far
Iteration 593 (of 1300): 10.04 sec so far
Iteration 889 (of 1300): 15.05 sec so far
Iteration 1155 (of 1300): 20.06 sec so far

Iterative method: 1300 iterations in 22.37 seconds (average 0.017185, setup 0.03)

Value in the initial state: 0.6630608525241822

Time for model checking: 23.334 seconds.

Result: 0.6630608525241822 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

