# Log files for prism_from-prism_check_default on model [rabin.10](../../models/rabin.10)

Parsed values: `[49.384, 52.068, 62.792, 41.962, 45.52]`



### Log file: prism_from-prism_check_default_rabin.10_rep1.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism models/rabin.10/property.props
Wallclock time: 51.575 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:33:52 GMT+01:00 2026
Hostname: n23m0176.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 42 iterations in 46.47 seconds (average 1.106429, setup 0.00)

Time for model construction: 49.384 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Warning: Switching to MTBDD engine, as number of states is too large for Hybrid engine.

Prob0A: 5 iterations in 0.81 seconds (average 0.162000, setup 0.00)

Prob1E: 6 iterations in 0.46 seconds (average 0.076667, setup 0.00)

yes = 358055586147376, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 1.315 seconds.

Result: 1.0 (exact floating point)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_rabin.10_rep2.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism models/rabin.10/property.props
Wallclock time: 54.330 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:07 GMT+01:00 2026
Hostname: n23m0288.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 42 iterations in 48.84 seconds (average 1.162857, setup 0.00)

Time for model construction: 52.068 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Warning: Switching to MTBDD engine, as number of states is too large for Hybrid engine.

Prob0A: 5 iterations in 0.85 seconds (average 0.170000, setup 0.00)

Prob1E: 6 iterations in 0.47 seconds (average 0.078333, setup 0.00)

yes = 358055586147376, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 1.374 seconds.

Result: 1.0 (exact floating point)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_rabin.10_rep3.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism models/rabin.10/property.props
Wallclock time: 65.845 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:06 GMT+01:00 2026
Hostname: r23m0044.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 42 iterations in 59.15 seconds (average 1.408333, setup 0.00)

Time for model construction: 62.792 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Warning: Switching to MTBDD engine, as number of states is too large for Hybrid engine.

Prob0A: 5 iterations in 1.01 seconds (average 0.202000, setup 0.00)

Prob1E: 6 iterations in 0.63 seconds (average 0.105000, setup 0.00)

yes = 358055586147376, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 1.691 seconds.

Result: 1.0 (exact floating point)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_rabin.10_rep4.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism models/rabin.10/property.props
Wallclock time: 44.506 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:09:51 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 42 iterations in 39.43 seconds (average 0.938810, setup 0.00)

Time for model construction: 41.962 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Warning: Switching to MTBDD engine, as number of states is too large for Hybrid engine.

Prob0A: 5 iterations in 0.69 seconds (average 0.138000, setup 0.00)

Prob1E: 6 iterations in 0.38 seconds (average 0.063333, setup 0.00)

yes = 358055586147376, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 1.143 seconds.

Result: 1.0 (exact floating point)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_rabin.10_rep5.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism models/rabin.10/property.props
Wallclock time: 53.767 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:08 GMT+01:00 2026
Hostname: r23m0118.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 42 iterations in 42.64 seconds (average 1.015238, setup 0.00)

Time for model construction: 45.52 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Warning: Switching to MTBDD engine, as number of states is too large for Hybrid engine.

Prob0A: 5 iterations in 0.81 seconds (average 0.162000, setup 0.00)

Prob1E: 6 iterations in 0.41 seconds (average 0.068333, setup 0.00)

yes = 358055586147376, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 1.272 seconds.

Result: 1.0 (exact floating point)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

