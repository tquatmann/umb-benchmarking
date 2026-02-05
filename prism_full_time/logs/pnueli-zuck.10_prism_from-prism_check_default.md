# Log files

Tool configuration: prism_from-prism_check_default
Benchmark: [pnueli-zuck.10](../../models/pnueli-zuck.10)
Parsed values: [8.295, 8.241, 9.236, 8.28, 11.204]



### Log file: prism_from-prism_check_default_pnueli-zuck.10_rep1.log

```
Command(s):
../bin/prism  models/pnueli-zuck.10/model.prism models/pnueli-zuck.10/property.props
Wallclock time: 8.295 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:49:26 GMT+01:00 2026
Hostname: n23m0096.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.10/model.prism models/pnueli-zuck.10/property.props

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Parsing properties file "models/pnueli-zuck.10/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.65 seconds (average 0.008904, setup 0.00)

Time for model construction: 0.733 seconds.

Type:        MDP
States:      69994757110 (1 initial)
Transitions: 891923978050

Transition matrix: 22186 nodes (3 terminal), 891923978050 minterms, vars: 40r/40c/10nd

Warning: Switching to MTBDD engine, as number of states is too large for Hybrid engine.

Prob0A: 90 iterations in 3.60 seconds (average 0.040000, setup 0.00)

Prob1E: 91 iterations in 3.28 seconds (average 0.036044, setup 0.00)

yes = 69994757110, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 6.901 seconds.

Result: 1.0 (exact floating point)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_pnueli-zuck.10_rep2.log

```
Command(s):
../bin/prism  models/pnueli-zuck.10/model.prism models/pnueli-zuck.10/property.props
Wallclock time: 8.241 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:07:49 GMT+01:00 2026
Hostname: r23m0203.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.10/model.prism models/pnueli-zuck.10/property.props

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Parsing properties file "models/pnueli-zuck.10/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.56 seconds (average 0.007671, setup 0.00)

Time for model construction: 0.641 seconds.

Type:        MDP
States:      69994757110 (1 initial)
Transitions: 891923978050

Transition matrix: 22186 nodes (3 terminal), 891923978050 minterms, vars: 40r/40c/10nd

Warning: Switching to MTBDD engine, as number of states is too large for Hybrid engine.

Prob0A: 90 iterations in 3.02 seconds (average 0.033556, setup 0.00)

Prob1E: 91 iterations in 3.36 seconds (average 0.036923, setup 0.00)

yes = 69994757110, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 6.408 seconds.

Result: 1.0 (exact floating point)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_pnueli-zuck.10_rep3.log

```
Command(s):
../bin/prism  models/pnueli-zuck.10/model.prism models/pnueli-zuck.10/property.props
Wallclock time: 9.236 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:22:09 GMT+01:00 2026
Hostname: n23m0095.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.10/model.prism models/pnueli-zuck.10/property.props

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Parsing properties file "models/pnueli-zuck.10/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.63 seconds (average 0.008630, setup 0.00)

Time for model construction: 0.727 seconds.

Type:        MDP
States:      69994757110 (1 initial)
Transitions: 891923978050

Transition matrix: 22186 nodes (3 terminal), 891923978050 minterms, vars: 40r/40c/10nd

Warning: Switching to MTBDD engine, as number of states is too large for Hybrid engine.

Prob0A: 90 iterations in 3.56 seconds (average 0.039556, setup 0.00)

Prob1E: 91 iterations in 4.21 seconds (average 0.046264, setup 0.00)

yes = 69994757110, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 7.796 seconds.

Result: 1.0 (exact floating point)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_pnueli-zuck.10_rep4.log

```
Command(s):
../bin/prism  models/pnueli-zuck.10/model.prism models/pnueli-zuck.10/property.props
Wallclock time: 8.280 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:07:30 GMT+01:00 2026
Hostname: n23m0267.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.10/model.prism models/pnueli-zuck.10/property.props

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Parsing properties file "models/pnueli-zuck.10/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.59 seconds (average 0.008082, setup 0.00)

Time for model construction: 0.664 seconds.

Type:        MDP
States:      69994757110 (1 initial)
Transitions: 891923978050

Transition matrix: 22186 nodes (3 terminal), 891923978050 minterms, vars: 40r/40c/10nd

Warning: Switching to MTBDD engine, as number of states is too large for Hybrid engine.

Prob0A: 90 iterations in 3.34 seconds (average 0.037111, setup 0.00)

Prob1E: 91 iterations in 3.57 seconds (average 0.039231, setup 0.00)

yes = 69994757110, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 6.919 seconds.

Result: 1.0 (exact floating point)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_pnueli-zuck.10_rep5.log

```
Command(s):
../bin/prism  models/pnueli-zuck.10/model.prism models/pnueli-zuck.10/property.props
Wallclock time: 11.204 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:03:33 GMT+01:00 2026
Hostname: r23m0015.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.10/model.prism models/pnueli-zuck.10/property.props

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Parsing properties file "models/pnueli-zuck.10/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 1.04 seconds (average 0.014247, setup 0.00)

Time for model construction: 1.149 seconds.

Type:        MDP
States:      69994757110 (1 initial)
Transitions: 891923978050

Transition matrix: 22186 nodes (3 terminal), 891923978050 minterms, vars: 40r/40c/10nd

Warning: Switching to MTBDD engine, as number of states is too large for Hybrid engine.

Prob0A: 90 iterations in 4.56 seconds (average 0.050667, setup 0.00)

Prob1E: 91 iterations in 4.70 seconds (average 0.051648, setup 0.00)

yes = 69994757110, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 9.303 seconds.

Result: 1.0 (exact floating point)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

