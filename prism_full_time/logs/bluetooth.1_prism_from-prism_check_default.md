# Log files for prism_from-prism_check_default on model [bluetooth.1](../../models/bluetooth.1)

Parsed values: `[7.494, 8.292, 4.721, 4.796, 5.48]`



### Log file: prism_from-prism_check_default_bluetooth.1_rep1.log

```
Command(s):
../bin/prism  models/bluetooth.1/model.prism models/bluetooth.1/property.props
Wallclock time: 7.494 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:25:04 GMT+01:00 2026
Hostname: n23m0165.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/bluetooth.1/model.prism models/bluetooth.1/property.props

Parsing PRISM model file "models/bluetooth.1/model.prism"...

Type:        DTMC
Modules:     receiver1 frequency1 sender_frequency replies
Actions:     [] [time] [reply]
Variables:   y1 receiver freq1 train1 z1 f1 t1 send freq train c rep rec
Labels:      "target"
Rewards:     "time"

Parsing properties file "models/bluetooth.1/property.props"...

1 property:
(1) "time": filter(max, R=? [ F "target" ], "init")

---------------------------------------------------------------------

Model checking: "time": filter(max, R=? [ F "target" ], "init")

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 50 iterations in 0.11 seconds (average 0.002200, setup 0.00)

Time for model construction: 4.114 seconds.

Type:        DTMC
States:      3411945339 (536870912 initial)
Transitions: 5035263739

Transition matrix: 14727 nodes (4 terminal), 5035263739 minterms, vars: 52r/52c

Warning: Switching to MTBDD engine, as number of states is too large for Hybrid engine.

Prob0: 49 iterations in 0.18 seconds (average 0.003673, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 1636000575, inf = 0, maybe = 1775944764

Computing remaining rewards...
Engine: MTBDD

Iteration matrix MTBDD... [nodes=11441] [223.5 Kb]
Diagonals MTBDD... [nodes=4425] [86.4 Kb]

Starting iterations...

Jacobi: 47 iterations in 0.41 seconds (average 0.008511, setup 0.01)

Maximum value over states satisfying filter: 8229.0

There are 32768 states with (approximately) this value.
The first 10 states are displayed below. To view them all, enable verbose mode or use a print filter.
4479:(0,0,0,0,1,1,0,1,2,0,3,128,0)
4735:(0,0,0,0,1,1,0,1,2,0,5,128,0)
4991:(0,0,0,0,1,1,0,1,2,0,7,128,0)
5247:(0,0,0,0,1,1,0,1,2,0,9,128,0)
5503:(0,0,0,0,1,1,0,1,2,0,11,128,0)
5759:(0,0,0,0,1,1,0,1,2,0,13,128,0)
6015:(0,0,0,0,1,1,0,1,2,0,15,128,0)
6271:(0,0,0,0,1,1,0,1,2,1,1,128,0)
233777:(0,0,0,0,2,1,0,1,2,0,3,128,0)
234033:(0,0,0,0,2,1,0,1,2,0,5,128,0)

Time for model checking: 0.656 seconds.

Result: 8229.0

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_bluetooth.1_rep2.log

```
Command(s):
../bin/prism  models/bluetooth.1/model.prism models/bluetooth.1/property.props
Wallclock time: 8.292 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:25:41 GMT+01:00 2026
Hostname: n23m0273.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/bluetooth.1/model.prism models/bluetooth.1/property.props

Parsing PRISM model file "models/bluetooth.1/model.prism"...

Type:        DTMC
Modules:     receiver1 frequency1 sender_frequency replies
Actions:     [] [time] [reply]
Variables:   y1 receiver freq1 train1 z1 f1 t1 send freq train c rep rec
Labels:      "target"
Rewards:     "time"

Parsing properties file "models/bluetooth.1/property.props"...

1 property:
(1) "time": filter(max, R=? [ F "target" ], "init")

---------------------------------------------------------------------

Model checking: "time": filter(max, R=? [ F "target" ], "init")

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 50 iterations in 0.12 seconds (average 0.002400, setup 0.00)

Time for model construction: 4.688 seconds.

Type:        DTMC
States:      3411945339 (536870912 initial)
Transitions: 5035263739

Transition matrix: 14727 nodes (4 terminal), 5035263739 minterms, vars: 52r/52c

Warning: Switching to MTBDD engine, as number of states is too large for Hybrid engine.

Prob0: 49 iterations in 0.21 seconds (average 0.004286, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 1636000575, inf = 0, maybe = 1775944764

Computing remaining rewards...
Engine: MTBDD

Iteration matrix MTBDD... [nodes=11441] [223.5 Kb]
Diagonals MTBDD... [nodes=4425] [86.4 Kb]

Starting iterations...

Jacobi: 47 iterations in 0.52 seconds (average 0.010851, setup 0.01)

Maximum value over states satisfying filter: 8229.0

There are 32768 states with (approximately) this value.
The first 10 states are displayed below. To view them all, enable verbose mode or use a print filter.
4479:(0,0,0,0,1,1,0,1,2,0,3,128,0)
4735:(0,0,0,0,1,1,0,1,2,0,5,128,0)
4991:(0,0,0,0,1,1,0,1,2,0,7,128,0)
5247:(0,0,0,0,1,1,0,1,2,0,9,128,0)
5503:(0,0,0,0,1,1,0,1,2,0,11,128,0)
5759:(0,0,0,0,1,1,0,1,2,0,13,128,0)
6015:(0,0,0,0,1,1,0,1,2,0,15,128,0)
6271:(0,0,0,0,1,1,0,1,2,1,1,128,0)
233777:(0,0,0,0,2,1,0,1,2,0,3,128,0)
234033:(0,0,0,0,2,1,0,1,2,0,5,128,0)

Time for model checking: 0.791 seconds.

Result: 8229.0

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_bluetooth.1_rep3.log

```
Command(s):
../bin/prism  models/bluetooth.1/model.prism models/bluetooth.1/property.props
Wallclock time: 4.721 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:05 GMT+01:00 2026
Hostname: n23m0114.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/bluetooth.1/model.prism models/bluetooth.1/property.props

Parsing PRISM model file "models/bluetooth.1/model.prism"...

Type:        DTMC
Modules:     receiver1 frequency1 sender_frequency replies
Actions:     [] [time] [reply]
Variables:   y1 receiver freq1 train1 z1 f1 t1 send freq train c rep rec
Labels:      "target"
Rewards:     "time"

Parsing properties file "models/bluetooth.1/property.props"...

1 property:
(1) "time": filter(max, R=? [ F "target" ], "init")

---------------------------------------------------------------------

Model checking: "time": filter(max, R=? [ F "target" ], "init")

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 50 iterations in 0.10 seconds (average 0.002000, setup 0.00)

Time for model construction: 3.286 seconds.

Type:        DTMC
States:      3411945339 (536870912 initial)
Transitions: 5035263739

Transition matrix: 14727 nodes (4 terminal), 5035263739 minterms, vars: 52r/52c

Warning: Switching to MTBDD engine, as number of states is too large for Hybrid engine.

Prob0: 49 iterations in 0.16 seconds (average 0.003265, setup 0.00)

Prob1: 1 iterations in 0.01 seconds (average 0.010000, setup 0.00)

goal = 1636000575, inf = 0, maybe = 1775944764

Computing remaining rewards...
Engine: MTBDD

Iteration matrix MTBDD... [nodes=11441] [223.5 Kb]
Diagonals MTBDD... [nodes=4425] [86.4 Kb]

Starting iterations...

Jacobi: 47 iterations in 0.40 seconds (average 0.008298, setup 0.01)

Maximum value over states satisfying filter: 8229.0

There are 32768 states with (approximately) this value.
The first 10 states are displayed below. To view them all, enable verbose mode or use a print filter.
4479:(0,0,0,0,1,1,0,1,2,0,3,128,0)
4735:(0,0,0,0,1,1,0,1,2,0,5,128,0)
4991:(0,0,0,0,1,1,0,1,2,0,7,128,0)
5247:(0,0,0,0,1,1,0,1,2,0,9,128,0)
5503:(0,0,0,0,1,1,0,1,2,0,11,128,0)
5759:(0,0,0,0,1,1,0,1,2,0,13,128,0)
6015:(0,0,0,0,1,1,0,1,2,0,15,128,0)
6271:(0,0,0,0,1,1,0,1,2,1,1,128,0)
233777:(0,0,0,0,2,1,0,1,2,0,3,128,0)
234033:(0,0,0,0,2,1,0,1,2,0,5,128,0)

Time for model checking: 0.583 seconds.

Result: 8229.0

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_bluetooth.1_rep4.log

```
Command(s):
../bin/prism  models/bluetooth.1/model.prism models/bluetooth.1/property.props
Wallclock time: 4.796 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:36:42 GMT+01:00 2026
Hostname: n23m0031.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/bluetooth.1/model.prism models/bluetooth.1/property.props

Parsing PRISM model file "models/bluetooth.1/model.prism"...

Type:        DTMC
Modules:     receiver1 frequency1 sender_frequency replies
Actions:     [] [time] [reply]
Variables:   y1 receiver freq1 train1 z1 f1 t1 send freq train c rep rec
Labels:      "target"
Rewards:     "time"

Parsing properties file "models/bluetooth.1/property.props"...

1 property:
(1) "time": filter(max, R=? [ F "target" ], "init")

---------------------------------------------------------------------

Model checking: "time": filter(max, R=? [ F "target" ], "init")

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 50 iterations in 0.10 seconds (average 0.002000, setup 0.00)

Time for model construction: 3.385 seconds.

Type:        DTMC
States:      3411945339 (536870912 initial)
Transitions: 5035263739

Transition matrix: 14727 nodes (4 terminal), 5035263739 minterms, vars: 52r/52c

Warning: Switching to MTBDD engine, as number of states is too large for Hybrid engine.

Prob0: 49 iterations in 0.18 seconds (average 0.003673, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 1636000575, inf = 0, maybe = 1775944764

Computing remaining rewards...
Engine: MTBDD

Iteration matrix MTBDD... [nodes=11441] [223.5 Kb]
Diagonals MTBDD... [nodes=4425] [86.4 Kb]

Starting iterations...

Jacobi: 47 iterations in 0.44 seconds (average 0.009362, setup 0.00)

Maximum value over states satisfying filter: 8229.0

There are 32768 states with (approximately) this value.
The first 10 states are displayed below. To view them all, enable verbose mode or use a print filter.
4479:(0,0,0,0,1,1,0,1,2,0,3,128,0)
4735:(0,0,0,0,1,1,0,1,2,0,5,128,0)
4991:(0,0,0,0,1,1,0,1,2,0,7,128,0)
5247:(0,0,0,0,1,1,0,1,2,0,9,128,0)
5503:(0,0,0,0,1,1,0,1,2,0,11,128,0)
5759:(0,0,0,0,1,1,0,1,2,0,13,128,0)
6015:(0,0,0,0,1,1,0,1,2,0,15,128,0)
6271:(0,0,0,0,1,1,0,1,2,1,1,128,0)
233777:(0,0,0,0,2,1,0,1,2,0,3,128,0)
234033:(0,0,0,0,2,1,0,1,2,0,5,128,0)

Time for model checking: 0.667 seconds.

Result: 8229.0

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_bluetooth.1_rep5.log

```
Command(s):
../bin/prism  models/bluetooth.1/model.prism models/bluetooth.1/property.props
Wallclock time: 5.480 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:24:37 GMT+01:00 2026
Hostname: n23m0098.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/bluetooth.1/model.prism models/bluetooth.1/property.props

Parsing PRISM model file "models/bluetooth.1/model.prism"...

Type:        DTMC
Modules:     receiver1 frequency1 sender_frequency replies
Actions:     [] [time] [reply]
Variables:   y1 receiver freq1 train1 z1 f1 t1 send freq train c rep rec
Labels:      "target"
Rewards:     "time"

Parsing properties file "models/bluetooth.1/property.props"...

1 property:
(1) "time": filter(max, R=? [ F "target" ], "init")

---------------------------------------------------------------------

Model checking: "time": filter(max, R=? [ F "target" ], "init")

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 50 iterations in 0.08 seconds (average 0.001600, setup 0.00)

Time for model construction: 2.793 seconds.

Type:        DTMC
States:      3411945339 (536870912 initial)
Transitions: 5035263739

Transition matrix: 14727 nodes (4 terminal), 5035263739 minterms, vars: 52r/52c

Warning: Switching to MTBDD engine, as number of states is too large for Hybrid engine.

Prob0: 49 iterations in 0.12 seconds (average 0.002449, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 1636000575, inf = 0, maybe = 1775944764

Computing remaining rewards...
Engine: MTBDD

Iteration matrix MTBDD... [nodes=11441] [223.5 Kb]
Diagonals MTBDD... [nodes=4425] [86.4 Kb]

Starting iterations...

Jacobi: 47 iterations in 0.30 seconds (average 0.006170, setup 0.01)

Maximum value over states satisfying filter: 8229.0

There are 32768 states with (approximately) this value.
The first 10 states are displayed below. To view them all, enable verbose mode or use a print filter.
4479:(0,0,0,0,1,1,0,1,2,0,3,128,0)
4735:(0,0,0,0,1,1,0,1,2,0,5,128,0)
4991:(0,0,0,0,1,1,0,1,2,0,7,128,0)
5247:(0,0,0,0,1,1,0,1,2,0,9,128,0)
5503:(0,0,0,0,1,1,0,1,2,0,11,128,0)
5759:(0,0,0,0,1,1,0,1,2,0,13,128,0)
6015:(0,0,0,0,1,1,0,1,2,0,15,128,0)
6271:(0,0,0,0,1,1,0,1,2,1,1,128,0)
233777:(0,0,0,0,2,1,0,1,2,0,3,128,0)
234033:(0,0,0,0,2,1,0,1,2,0,5,128,0)

Time for model checking: 0.467 seconds.

Result: 8229.0

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

