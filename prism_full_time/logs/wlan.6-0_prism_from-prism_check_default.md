# Log files

Tool configuration: prism_from-prism_check_default
Benchmark: [wlan.6-0](../../models/wlan.6-0)
Parsed values: [73.221, 66.577, 70.041, 59.669, 57.807]



### Log file: prism_from-prism_check_default_wlan.6-0_rep1.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism models/wlan.6-0/property.props
Wallclock time: 73.221 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:28:40 GMT+01:00 2026
Hostname: n23m0288.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism models/wlan.6-0/property.props

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Parsing properties file "models/wlan.6-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.29 seconds (average 0.001487, setup 0.00)

Time for model construction: 0.394 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 3158 iterations in 70.28 seconds (average 0.022255, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 5007548, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 70.49 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_wlan.6-0_rep2.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism models/wlan.6-0/property.props
Wallclock time: 66.577 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:10 GMT+01:00 2026
Hostname: n23m0225.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism models/wlan.6-0/property.props

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Parsing properties file "models/wlan.6-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.33 seconds (average 0.001692, setup 0.00)

Time for model construction: 0.411 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 3158 iterations in 62.20 seconds (average 0.019696, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 5007548, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 62.429 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_wlan.6-0_rep3.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism models/wlan.6-0/property.props
Wallclock time: 70.041 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:22:36 GMT+01:00 2026
Hostname: n23m0110.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism models/wlan.6-0/property.props

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Parsing properties file "models/wlan.6-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.38 seconds (average 0.001949, setup 0.00)

Time for model construction: 0.501 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 3158 iterations in 67.85 seconds (average 0.021485, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 5007548, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 68.035 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_wlan.6-0_rep4.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism models/wlan.6-0/property.props
Wallclock time: 59.669 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:06 GMT+01:00 2026
Hostname: n23m0101.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism models/wlan.6-0/property.props

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Parsing properties file "models/wlan.6-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.30 seconds (average 0.001538, setup 0.00)

Time for model construction: 0.377 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 3158 iterations in 58.09 seconds (average 0.018395, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 5007548, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 58.234 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_wlan.6-0_rep5.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism models/wlan.6-0/property.props
Wallclock time: 57.807 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:07:08 GMT+01:00 2026
Hostname: r23m0017.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism models/wlan.6-0/property.props

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Parsing properties file "models/wlan.6-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.31 seconds (average 0.001590, setup 0.00)

Time for model construction: 0.354 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 3158 iterations in 56.63 seconds (average 0.017932, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 5007548, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 56.821 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

