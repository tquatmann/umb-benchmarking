# Log files

Tool configuration: prism_from-prism_check_norewards
Benchmark: [pnueli-zuck.5](../../models/pnueli-zuck.5)
Parsed values: [1.466, 1.428, 1.247, 0.992, 0.824]



### Log file: prism_from-prism_check_norewards_pnueli-zuck.5_rep1.log

```
Command(s):
../bin/prism  models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props
Wallclock time: 1.466 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:45:49 GMT+01:00 2026
Hostname: n23m0379.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props

Parsing PRISM model file "models/pnueli-zuck.5/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4
Actions:     []
Variables:   p0 p1 p2 p3 p4
Labels:      "target"

Parsing properties file "models/pnueli-zuck.5/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.05 seconds (average 0.001316, setup 0.00)

Time for model construction: 0.09 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2492035

Transition matrix: 5161 nodes (3 terminal), 2492035 minterms, vars: 20r/20c/5nd

Prob0A: 45 iterations in 0.13 seconds (average 0.002889, setup 0.00)

Prob1E: 46 iterations in 0.08 seconds (average 0.001739, setup 0.00)

yes = 397435, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 0.212 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_pnueli-zuck.5_rep2.log

```
Command(s):
../bin/prism  models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props
Wallclock time: 1.428 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:07 GMT+01:00 2026
Hostname: n23m0146.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props

Parsing PRISM model file "models/pnueli-zuck.5/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4
Actions:     []
Variables:   p0 p1 p2 p3 p4
Labels:      "target"

Parsing properties file "models/pnueli-zuck.5/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.05 seconds (average 0.001316, setup 0.00)

Time for model construction: 0.1 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2492035

Transition matrix: 5161 nodes (3 terminal), 2492035 minterms, vars: 20r/20c/5nd

Prob0A: 45 iterations in 0.13 seconds (average 0.002889, setup 0.00)

Prob1E: 46 iterations in 0.10 seconds (average 0.002174, setup 0.00)

yes = 397435, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 0.238 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_pnueli-zuck.5_rep3.log

```
Command(s):
../bin/prism  models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props
Wallclock time: 1.247 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:04:03 GMT+01:00 2026
Hostname: r23m0015.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props

Parsing PRISM model file "models/pnueli-zuck.5/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4
Actions:     []
Variables:   p0 p1 p2 p3 p4
Labels:      "target"

Parsing properties file "models/pnueli-zuck.5/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.08 seconds (average 0.002105, setup 0.00)

Time for model construction: 0.112 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2492035

Transition matrix: 5161 nodes (3 terminal), 2492035 minterms, vars: 20r/20c/5nd

Prob0A: 45 iterations in 0.27 seconds (average 0.006000, setup 0.00)

Prob1E: 46 iterations in 0.19 seconds (average 0.004130, setup 0.00)

yes = 397435, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 0.46 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_pnueli-zuck.5_rep4.log

```
Command(s):
../bin/prism  models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props
Wallclock time: 0.992 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:30 GMT+01:00 2026
Hostname: n23m0033.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props

Parsing PRISM model file "models/pnueli-zuck.5/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4
Actions:     []
Variables:   p0 p1 p2 p3 p4
Labels:      "target"

Parsing properties file "models/pnueli-zuck.5/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.05 seconds (average 0.001316, setup 0.00)

Time for model construction: 0.082 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2492035

Transition matrix: 5161 nodes (3 terminal), 2492035 minterms, vars: 20r/20c/5nd

Prob0A: 45 iterations in 0.16 seconds (average 0.003556, setup 0.00)

Prob1E: 46 iterations in 0.12 seconds (average 0.002609, setup 0.00)

yes = 397435, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 0.284 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_pnueli-zuck.5_rep5.log

```
Command(s):
../bin/prism  models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props
Wallclock time: 0.824 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:07:15 GMT+01:00 2026
Hostname: r23m0211.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props

Parsing PRISM model file "models/pnueli-zuck.5/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4
Actions:     []
Variables:   p0 p1 p2 p3 p4
Labels:      "target"

Parsing properties file "models/pnueli-zuck.5/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.05 seconds (average 0.001316, setup 0.00)

Time for model construction: 0.097 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2492035

Transition matrix: 5161 nodes (3 terminal), 2492035 minterms, vars: 20r/20c/5nd

Prob0A: 45 iterations in 0.11 seconds (average 0.002444, setup 0.00)

Prob1E: 46 iterations in 0.09 seconds (average 0.001957, setup 0.00)

yes = 397435, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 0.206 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

