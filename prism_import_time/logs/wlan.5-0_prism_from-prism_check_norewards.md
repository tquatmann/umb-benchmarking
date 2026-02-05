# Log files for prism_from-prism_check_norewards on model [wlan.5-0](../../models/wlan.5-0)

Parsed values: `[0.284, 0.26, 0.271, 0.366, 0.299]`



### Log file: prism_from-prism_check_norewards_wlan.5-0_rep1.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism models/wlan.5-0/property.props
Wallclock time: 14.435 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:33:21 GMT+01:00 2026
Hostname: n23m0176.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism models/wlan.5-0/property.props

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Parsing properties file "models/wlan.5-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.19 seconds (average 0.001118, setup 0.00)

Time for model construction: 0.284 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 1622 iterations in 13.25 seconds (average 0.008169, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1295218, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 13.306 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_wlan.5-0_rep2.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism models/wlan.5-0/property.props
Wallclock time: 12.935 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:03 GMT+01:00 2026
Hostname: n23m0175.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism models/wlan.5-0/property.props

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Parsing properties file "models/wlan.5-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.19 seconds (average 0.001118, setup 0.00)

Time for model construction: 0.26 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 1622 iterations in 11.75 seconds (average 0.007244, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1295218, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 11.805 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_wlan.5-0_rep3.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism models/wlan.5-0/property.props
Wallclock time: 17.941 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:09:44 GMT+01:00 2026
Hostname: n23m0031.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism models/wlan.5-0/property.props

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Parsing properties file "models/wlan.5-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.22 seconds (average 0.001294, setup 0.00)

Time for model construction: 0.271 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 1622 iterations in 16.95 seconds (average 0.010450, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1295218, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 17.048 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_wlan.5-0_rep4.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism models/wlan.5-0/property.props
Wallclock time: 16.594 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 02:49:45 GMT+01:00 2026
Hostname: n23m0023.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism models/wlan.5-0/property.props

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Parsing properties file "models/wlan.5-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.19 seconds (average 0.001118, setup 0.00)

Time for model construction: 0.366 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 1622 iterations in 11.90 seconds (average 0.007337, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1295218, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 11.975 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_wlan.5-0_rep5.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism models/wlan.5-0/property.props
Wallclock time: 13.133 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:23:55 GMT+01:00 2026
Hostname: n23m0041.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism models/wlan.5-0/property.props

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Parsing properties file "models/wlan.5-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.17 seconds (average 0.001000, setup 0.00)

Time for model construction: 0.299 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 1622 iterations in 11.46 seconds (average 0.007065, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1295218, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 11.494 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

