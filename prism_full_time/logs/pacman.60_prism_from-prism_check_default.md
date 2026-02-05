# Log files for prism_from-prism_check_default on model [pacman.60](../../models/pacman.60)

Parsed values: `[TO, TO, TO, TO, TO]`



### Log file: prism_from-prism_check_default_pacman.60_rep1.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism models/pacman.60/property.props
Wallclock time: 7200.350 seconds
Return code: None (timeout)
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:33:52 GMT+01:00 2026
Hostname: r23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism models/pacman.60/property.props

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Parsing properties file "models/pacman.60/property.props"...

1 property:
(1) "crash": Pmin=? [ F "Crash" ]

---------------------------------------------------------------------

Model checking: "crash": Pmin=? [ F "Crash" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 52.47 seconds (average 0.286721, setup 0.00)

Time for model construction: 1148.539 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Prob0E: 166 iterations in 1700.97 seconds (average 10.246807, setup 0.00)

Prob1A: 41 iterations in 217.75 seconds (average 5.310976, setup 0.00)

yes = 6111954, no = 21126260, maybe = 11548307

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... 
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_pacman.60_rep2.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism models/pacman.60/property.props
Wallclock time: 7200.352 seconds
Return code: None (timeout)
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:59:26 GMT+01:00 2026
Hostname: n23m0402.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism models/pacman.60/property.props

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Parsing properties file "models/pacman.60/property.props"...

1 property:
(1) "crash": Pmin=? [ F "Crash" ]

---------------------------------------------------------------------

Model checking: "crash": Pmin=? [ F "Crash" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 56.33 seconds (average 0.307814, setup 0.00)

Time for model construction: 2035.941 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Prob0E: 166 iterations in 1920.99 seconds (average 11.572229, setup 0.00)

Prob1A: 41 iterations in 251.06 seconds (average 6.123415, setup 0.00)

yes = 6111954, no = 21126260, maybe = 11548307

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... 
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_pacman.60_rep3.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism models/pacman.60/property.props
Wallclock time: 7200.346 seconds
Return code: None (timeout)
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:23:26 GMT+01:00 2026
Hostname: n23m0274.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism models/pacman.60/property.props

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Parsing properties file "models/pacman.60/property.props"...

1 property:
(1) "crash": Pmin=? [ F "Crash" ]

---------------------------------------------------------------------

Model checking: "crash": Pmin=? [ F "Crash" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 46.88 seconds (average 0.256175, setup 0.00)

Time for model construction: 1041.16 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Prob0E: 166 iterations in 1596.61 seconds (average 9.618133, setup 0.00)

Prob1A: 41 iterations in 208.14 seconds (average 5.076585, setup 0.00)

yes = 6111954, no = 21126260, maybe = 11548307

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... 
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_pacman.60_rep4.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism models/pacman.60/property.props
Wallclock time: 7200.360 seconds
Return code: None (timeout)
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:01:00 GMT+01:00 2026
Hostname: n23m0333.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism models/pacman.60/property.props

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Parsing properties file "models/pacman.60/property.props"...

1 property:
(1) "crash": Pmin=? [ F "Crash" ]

---------------------------------------------------------------------

Model checking: "crash": Pmin=? [ F "Crash" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 55.16 seconds (average 0.301421, setup 0.00)

Time for model construction: 1712.611 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Prob0E: 166 iterations in 1594.06 seconds (average 9.602771, setup 0.00)

Prob1A: 41 iterations in 205.26 seconds (average 5.006341, setup 0.00)

yes = 6111954, no = 21126260, maybe = 11548307

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... 
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_pacman.60_rep5.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism models/pacman.60/property.props
Wallclock time: 7200.371 seconds
Return code: None (timeout)
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:07:06 GMT+01:00 2026
Hostname: n23m0275.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism models/pacman.60/property.props

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Parsing properties file "models/pacman.60/property.props"...

1 property:
(1) "crash": Pmin=? [ F "Crash" ]

---------------------------------------------------------------------

Model checking: "crash": Pmin=? [ F "Crash" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 47.40 seconds (average 0.259016, setup 0.00)

Time for model construction: 1048.37 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Prob0E: 166 iterations in 1656.20 seconds (average 9.977108, setup 0.00)

Prob1A: 41 iterations in 213.39 seconds (average 5.204634, setup 0.00)

yes = 6111954, no = 21126260, maybe = 11548307

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... 
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

