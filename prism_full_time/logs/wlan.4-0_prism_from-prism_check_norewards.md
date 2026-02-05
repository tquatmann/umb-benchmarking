# Log files

Tool configuration: prism_from-prism_check_norewards
Benchmark: [wlan.4-0](../../models/wlan.4-0)
Parsed values: [5.063, 5.128, 5.295, 5.306, 5.04]



### Log file: prism_from-prism_check_norewards_wlan.4-0_rep1.log

```
Command(s):
../bin/prism  models/wlan.4-0/model.prism models/wlan.4-0/property.props
Wallclock time: 5.063 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:53:36 GMT+01:00 2026
Hostname: n23m0201.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.4-0/model.prism models/wlan.4-0/property.props

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Parsing properties file "models/wlan.4-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 145 iterations in 0.14 seconds (average 0.000966, setup 0.00)

Time for model construction: 0.187 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252

Transition matrix: 14365 nodes (6 terminal), 762252 minterms, vars: 43r/43c/7nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 854 iterations in 4.27 seconds (average 0.005000, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 345000, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 4.294 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_wlan.4-0_rep2.log

```
Command(s):
../bin/prism  models/wlan.4-0/model.prism models/wlan.4-0/property.props
Wallclock time: 5.128 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:07:34 GMT+01:00 2026
Hostname: n23m0252.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.4-0/model.prism models/wlan.4-0/property.props

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Parsing properties file "models/wlan.4-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 145 iterations in 0.14 seconds (average 0.000966, setup 0.00)

Time for model construction: 0.177 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252

Transition matrix: 14365 nodes (6 terminal), 762252 minterms, vars: 43r/43c/7nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 854 iterations in 4.38 seconds (average 0.005129, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 345000, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 4.404 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_wlan.4-0_rep3.log

```
Command(s):
../bin/prism  models/wlan.4-0/model.prism models/wlan.4-0/property.props
Wallclock time: 5.295 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:11:42 GMT+01:00 2026
Hostname: r23m0017.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.4-0/model.prism models/wlan.4-0/property.props

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Parsing properties file "models/wlan.4-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 145 iterations in 0.16 seconds (average 0.001103, setup 0.00)

Time for model construction: 0.202 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252

Transition matrix: 14365 nodes (6 terminal), 762252 minterms, vars: 43r/43c/7nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 854 iterations in 4.46 seconds (average 0.005222, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 345000, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 4.478 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_wlan.4-0_rep4.log

```
Command(s):
../bin/prism  models/wlan.4-0/model.prism models/wlan.4-0/property.props
Wallclock time: 5.306 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:24:22 GMT+01:00 2026
Hostname: n23m0330.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.4-0/model.prism models/wlan.4-0/property.props

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Parsing properties file "models/wlan.4-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 145 iterations in 0.13 seconds (average 0.000897, setup 0.00)

Time for model construction: 0.19 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252

Transition matrix: 14365 nodes (6 terminal), 762252 minterms, vars: 43r/43c/7nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 854 iterations in 3.94 seconds (average 0.004614, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 345000, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 3.966 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_wlan.4-0_rep5.log

```
Command(s):
../bin/prism  models/wlan.4-0/model.prism models/wlan.4-0/property.props
Wallclock time: 5.040 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 02:53:17 GMT+01:00 2026
Hostname: n23m0175.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.4-0/model.prism models/wlan.4-0/property.props

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Parsing properties file "models/wlan.4-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 145 iterations in 0.13 seconds (average 0.000897, setup 0.00)

Time for model construction: 0.197 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252

Transition matrix: 14365 nodes (6 terminal), 762252 minterms, vars: 43r/43c/7nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 854 iterations in 4.01 seconds (average 0.004696, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 345000, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 4.031 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

