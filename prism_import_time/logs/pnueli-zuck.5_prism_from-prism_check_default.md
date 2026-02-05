# Log files for prism_from-prism_check_default on model [pnueli-zuck.5](../../models/pnueli-zuck.5)

Parsed values: `[0.191, 0.121, 0.089, 0.116, 0.092]`



### Log file: prism_from-prism_check_default_pnueli-zuck.5_rep1.log

```
Command(s):
../bin/prism  models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props
Wallclock time: 2.954 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:44:15 GMT+01:00 2026
Hostname: n23m0182.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 38 iterations in 0.04 seconds (average 0.001053, setup 0.00)

Time for model construction: 0.191 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2492035

Transition matrix: 5161 nodes (3 terminal), 2492035 minterms, vars: 20r/20c/5nd

Prob0A: 45 iterations in 0.12 seconds (average 0.002667, setup 0.00)

Prob1E: 46 iterations in 0.08 seconds (average 0.001739, setup 0.00)

yes = 397435, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 0.228 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_pnueli-zuck.5_rep2.log

```
Command(s):
../bin/prism  models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props
Wallclock time: 0.872 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:09:50 GMT+01:00 2026
Hostname: n23m0292.hpc.itc.rwth-aachen.de
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

Time for model construction: 0.121 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2492035

Transition matrix: 5161 nodes (3 terminal), 2492035 minterms, vars: 20r/20c/5nd

Prob0A: 45 iterations in 0.12 seconds (average 0.002667, setup 0.00)

Prob1E: 46 iterations in 0.09 seconds (average 0.001957, setup 0.00)

yes = 397435, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 0.216 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_pnueli-zuck.5_rep3.log

```
Command(s):
../bin/prism  models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props
Wallclock time: 1.001 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:06:38 GMT+01:00 2026
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

Reachability (BFS): 38 iterations in 0.06 seconds (average 0.001579, setup 0.00)

Time for model construction: 0.089 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2492035

Transition matrix: 5161 nodes (3 terminal), 2492035 minterms, vars: 20r/20c/5nd

Prob0A: 45 iterations in 0.15 seconds (average 0.003333, setup 0.00)

Prob1E: 46 iterations in 0.13 seconds (average 0.002826, setup 0.00)

yes = 397435, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 0.281 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_pnueli-zuck.5_rep4.log

```
Command(s):
../bin/prism  models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props
Wallclock time: 3.550 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:02:02 GMT+01:00 2026
Hostname: n23m0272.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 38 iterations in 0.04 seconds (average 0.001053, setup 0.00)

Time for model construction: 0.116 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2492035

Transition matrix: 5161 nodes (3 terminal), 2492035 minterms, vars: 20r/20c/5nd

Prob0A: 45 iterations in 0.11 seconds (average 0.002444, setup 0.00)

Prob1E: 46 iterations in 0.08 seconds (average 0.001739, setup 0.00)

yes = 397435, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 0.207 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_pnueli-zuck.5_rep5.log

```
Command(s):
../bin/prism  models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props
Wallclock time: 1.178 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:01 GMT+01:00 2026
Hostname: r23m0140.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 38 iterations in 0.04 seconds (average 0.001053, setup 0.00)

Time for model construction: 0.092 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2492035

Transition matrix: 5161 nodes (3 terminal), 2492035 minterms, vars: 20r/20c/5nd

Prob0A: 45 iterations in 0.11 seconds (average 0.002444, setup 0.00)

Prob1E: 46 iterations in 0.08 seconds (average 0.001739, setup 0.00)

yes = 397435, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 0.199 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

