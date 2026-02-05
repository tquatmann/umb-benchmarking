# Log files for prism_from-prism_check_norewards on model [rabin.10](../../models/rabin.10)

Parsed values: `[55.476, 49.001, 59.218, 55.16, 47.644]`



### Log file: prism_from-prism_check_norewards_rabin.10_rep1.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism models/rabin.10/property.props
Wallclock time: 55.476 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:26:05 GMT+01:00 2026
Hostname: n23m0165.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism models/rabin.10/property.props

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Parsing properties file "models/rabin.10/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 49.99 seconds (average 1.190238, setup 0.00)

Time for model construction: 53.112 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Warning: Switching to MTBDD engine, as number of states is too large for Hybrid engine.

Prob0A: 5 iterations in 0.89 seconds (average 0.178000, setup 0.00)

Prob1E: 6 iterations in 0.53 seconds (average 0.088333, setup 0.00)

yes = 358055586147376, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 1.466 seconds.

Result: 1.0 (exact floating point)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_rabin.10_rep2.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism models/rabin.10/property.props
Wallclock time: 49.001 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:04:02 GMT+01:00 2026
Hostname: r23m0017.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism models/rabin.10/property.props

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Parsing properties file "models/rabin.10/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 43.59 seconds (average 1.037857, setup 0.00)

Time for model construction: 46.541 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Warning: Switching to MTBDD engine, as number of states is too large for Hybrid engine.

Prob0A: 5 iterations in 0.74 seconds (average 0.148000, setup 0.00)

Prob1E: 6 iterations in 0.39 seconds (average 0.065000, setup 0.00)

yes = 358055586147376, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 1.176 seconds.

Result: 1.0 (exact floating point)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_rabin.10_rep3.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism models/rabin.10/property.props
Wallclock time: 59.218 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:23:55 GMT+01:00 2026
Hostname: n23m0392.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism models/rabin.10/property.props

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Parsing properties file "models/rabin.10/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 53.51 seconds (average 1.274048, setup 0.00)

Time for model construction: 56.871 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Warning: Switching to MTBDD engine, as number of states is too large for Hybrid engine.

Prob0A: 5 iterations in 0.91 seconds (average 0.182000, setup 0.00)

Prob1E: 6 iterations in 0.54 seconds (average 0.090000, setup 0.00)

yes = 358055586147376, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 1.501 seconds.

Result: 1.0 (exact floating point)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_rabin.10_rep4.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism models/rabin.10/property.props
Wallclock time: 55.160 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:36:30 GMT+01:00 2026
Hostname: n23m0033.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism models/rabin.10/property.props

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Parsing properties file "models/rabin.10/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 48.42 seconds (average 1.152857, setup 0.00)

Time for model construction: 51.669 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Warning: Switching to MTBDD engine, as number of states is too large for Hybrid engine.

Prob0A: 5 iterations in 0.79 seconds (average 0.158000, setup 0.00)

Prob1E: 6 iterations in 0.41 seconds (average 0.068333, setup 0.00)

yes = 358055586147376, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 1.248 seconds.

Result: 1.0 (exact floating point)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_rabin.10_rep5.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism models/rabin.10/property.props
Wallclock time: 47.644 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:04:04 GMT+01:00 2026
Hostname: n23m0294.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism models/rabin.10/property.props

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Parsing properties file "models/rabin.10/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 43.21 seconds (average 1.028810, setup 0.00)

Time for model construction: 45.854 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Warning: Switching to MTBDD engine, as number of states is too large for Hybrid engine.

Prob0A: 5 iterations in 0.69 seconds (average 0.138000, setup 0.00)

Prob1E: 6 iterations in 0.37 seconds (average 0.061667, setup 0.00)

yes = 358055586147376, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 1.086 seconds.

Result: 1.0 (exact floating point)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

