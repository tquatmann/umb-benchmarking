# Log files

Tool configuration: prism_from-prism_check_default
Benchmark: [wlan.5-0](../../models/wlan.5-0)
Parsed values: [0.389, 0.306, 0.233, 0.227, 0.293]



### Log file: prism_from-prism_check_default_wlan.5-0_rep1.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism models/wlan.5-0/property.props
Wallclock time: 18.352 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:20:16 GMT+01:00 2026
Hostname: r23m0197.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 170 iterations in 0.23 seconds (average 0.001353, setup 0.00)

Time for model construction: 0.389 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 1622 iterations in 15.79 seconds (average 0.009735, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1295218, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 15.861 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_wlan.5-0_rep2.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism models/wlan.5-0/property.props
Wallclock time: 20.120 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:06:37 GMT+01:00 2026
Hostname: n23m0072.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 170 iterations in 0.24 seconds (average 0.001412, setup 0.00)

Time for model construction: 0.306 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 1622 iterations in 19.06 seconds (average 0.011751, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1295218, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 19.126 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_wlan.5-0_rep3.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism models/wlan.5-0/property.props
Wallclock time: 15.646 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:36:44 GMT+01:00 2026
Hostname: n23m0114.hpc.itc.rwth-aachen.de
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

Time for model construction: 0.233 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 1622 iterations in 14.80 seconds (average 0.009125, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1295218, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 14.836 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_wlan.5-0_rep4.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism models/wlan.5-0/property.props
Wallclock time: 12.304 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:19 GMT+01:00 2026
Hostname: n23m0340.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 170 iterations in 0.18 seconds (average 0.001059, setup 0.00)

Time for model construction: 0.227 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 1622 iterations in 11.52 seconds (average 0.007102, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1295218, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 11.554 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_wlan.5-0_rep5.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism models/wlan.5-0/property.props
Wallclock time: 16.004 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:07:17 GMT+01:00 2026
Hostname: n23m0210.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 170 iterations in 0.18 seconds (average 0.001059, setup 0.00)

Time for model construction: 0.293 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 1622 iterations in 12.30 seconds (average 0.007583, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1295218, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 12.349 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

