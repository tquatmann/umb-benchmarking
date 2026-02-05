# Log files

Tool configuration: prism_from-umb_check_default
Benchmark: [wlan.4-0](../../models/wlan.4-0)
Parsed values: [37.645, 34.758, 32.999, 30.191, 43.922]



### Log file: prism_from-umb_check_default_wlan.4-0_rep1.log

```
Command(s):
../bin/prism  -importmodel models/wlan.4-0/prism.model.umb models/wlan.4-0/property.props
Wallclock time: 54.117 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:48:55 GMT+01:00 2026
Hostname: n23m0197.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/wlan.4-0/prism.model.umb models/wlan.4-0/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   x
Labels:      "target"

Parsing properties file "models/wlan.4-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 8% 18% 26% 34% 44% 52% 60% 68% 76% 84% 90% 98% 100% ]

Computing reachable states...

Reachability (BFS): 145 iterations in 0.89 seconds (average 0.006138, setup 0.00)

Time for model construction: 37.645 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252

Transition matrix: 88372 nodes (6 terminal), 762252 minterms, vars: 19r/19c/3nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 854 iterations in 15.50 seconds (average 0.018150, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 345000, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 15.57 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_wlan.4-0_rep2.log

```
Command(s):
../bin/prism  -importmodel models/wlan.4-0/prism.model.umb models/wlan.4-0/property.props
Wallclock time: 51.289 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:08:50 GMT+01:00 2026
Hostname: n23m0292.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/wlan.4-0/prism.model.umb models/wlan.4-0/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   x
Labels:      "target"

Parsing properties file "models/wlan.4-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 10% 20% 30% 40% 48% 56% 64% 72% 82% 90% 98% 100% ]

Computing reachable states...

Reachability (BFS): 145 iterations in 0.79 seconds (average 0.005448, setup 0.00)

Time for model construction: 34.758 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252

Transition matrix: 88372 nodes (6 terminal), 762252 minterms, vars: 19r/19c/3nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 854 iterations in 14.24 seconds (average 0.016674, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 345000, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 14.343 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_wlan.4-0_rep3.log

```
Command(s):
../bin/prism  -importmodel models/wlan.4-0/prism.model.umb models/wlan.4-0/property.props
Wallclock time: 51.444 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:09 GMT+01:00 2026
Hostname: n23m0271.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/wlan.4-0/prism.model.umb models/wlan.4-0/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   x
Labels:      "target"

Parsing properties file "models/wlan.4-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 10% 20% 32% 42% 50% 60% 68% 78% 86% 94% 100% ]

Computing reachable states...

Reachability (BFS): 145 iterations in 0.79 seconds (average 0.005448, setup 0.00)

Time for model construction: 32.999 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252

Transition matrix: 88372 nodes (6 terminal), 762252 minterms, vars: 19r/19c/3nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 854 iterations in 14.29 seconds (average 0.016733, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 345000, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 14.331 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_wlan.4-0_rep4.log

```
Command(s):
../bin/prism  -importmodel models/wlan.4-0/prism.model.umb models/wlan.4-0/property.props
Wallclock time: 44.713 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:24:23 GMT+01:00 2026
Hostname: n23m0333.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/wlan.4-0/prism.model.umb models/wlan.4-0/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   x
Labels:      "target"

Parsing properties file "models/wlan.4-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 10% 20% 32% 42% 52% 62% 72% 82% 92% 100% ]

Computing reachable states...

Reachability (BFS): 145 iterations in 0.71 seconds (average 0.004897, setup 0.00)

Time for model construction: 30.191 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252

Transition matrix: 88372 nodes (6 terminal), 762252 minterms, vars: 19r/19c/3nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 854 iterations in 12.17 seconds (average 0.014251, setup 0.00)

Prob1A: 1 iterations in 0.01 seconds (average 0.010000, setup 0.00)

yes = 345000, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 12.22 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_wlan.4-0_rep5.log

```
Command(s):
../bin/prism  -importmodel models/wlan.4-0/prism.model.umb models/wlan.4-0/property.props
Wallclock time: 63.672 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:50 GMT+01:00 2026
Hostname: n23m0237.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/wlan.4-0/prism.model.umb models/wlan.4-0/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   x
Labels:      "target"

Parsing properties file "models/wlan.4-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 8% 18% 26% 34% 42% 48% 56% 62% 68% 74% 80% 86% 92% 98% 100% ]

Computing reachable states...

Reachability (BFS): 145 iterations in 1.03 seconds (average 0.007103, setup 0.00)

Time for model construction: 43.922 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252

Transition matrix: 88372 nodes (6 terminal), 762252 minterms, vars: 19r/19c/3nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 854 iterations in 18.99 seconds (average 0.022237, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 345000, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 19.049 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

