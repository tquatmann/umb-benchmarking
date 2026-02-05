# Log files

Tool configuration: prism_from-umb_check_default
Benchmark: [wlan.5-0](../../models/wlan.5-0)
Parsed values: [310.456, 220.218, 275.008, 221.937, 307.343]



### Log file: prism_from-umb_check_default_wlan.5-0_rep1.log

```
Command(s):
../bin/prism  -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props
Wallclock time: 310.456 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:17:39 GMT+01:00 2026
Hostname: r23m0130.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   x
Labels:      "target"

Parsing properties file "models/wlan.5-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 170 iterations in 2.67 seconds (average 0.015706, setup 0.00)

Time for model construction: 224.138 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 182051 nodes (7 terminal), 2929960 minterms, vars: 21r/21c/3nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 1622 iterations in 85.19 seconds (average 0.052522, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1295218, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 85.448 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_wlan.5-0_rep2.log

```
Command(s):
../bin/prism  -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props
Wallclock time: 220.218 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:02:32 GMT+01:00 2026
Hostname: n23m0325.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   x
Labels:      "target"

Parsing properties file "models/wlan.5-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 170 iterations in 1.95 seconds (average 0.011471, setup 0.00)

Time for model construction: 156.814 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 182051 nodes (7 terminal), 2929960 minterms, vars: 21r/21c/3nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 1622 iterations in 62.44 seconds (average 0.038496, setup 0.00)

Prob1A: 1 iterations in 0.01 seconds (average 0.010000, setup 0.00)

yes = 1295218, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 62.583 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_wlan.5-0_rep3.log

```
Command(s):
../bin/prism  -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props
Wallclock time: 275.008 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:06:36 GMT+01:00 2026
Hostname: n23m0021.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   x
Labels:      "target"

Parsing properties file "models/wlan.5-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 170 iterations in 2.35 seconds (average 0.013824, setup 0.00)

Time for model construction: 201.023 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 182051 nodes (7 terminal), 2929960 minterms, vars: 21r/21c/3nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 1622 iterations in 72.94 seconds (average 0.044969, setup 0.00)

Prob1A: 1 iterations in 0.01 seconds (average 0.010000, setup 0.00)

yes = 1295218, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 73.094 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_wlan.5-0_rep4.log

```
Command(s):
../bin/prism  -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props
Wallclock time: 221.937 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:11 GMT+01:00 2026
Hostname: r23m0211.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   x
Labels:      "target"

Parsing properties file "models/wlan.5-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 170 iterations in 2.02 seconds (average 0.011882, setup 0.00)

Time for model construction: 158.748 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 182051 nodes (7 terminal), 2929960 minterms, vars: 21r/21c/3nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 1622 iterations in 62.04 seconds (average 0.038249, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1295218, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 62.198 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_wlan.5-0_rep5.log

```
Command(s):
../bin/prism  -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props
Wallclock time: 307.343 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:38:17 GMT+01:00 2026
Hostname: n23m0267.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   x
Labels:      "target"

Parsing properties file "models/wlan.5-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 170 iterations in 2.68 seconds (average 0.015765, setup 0.00)

Time for model construction: 225.721 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 182051 nodes (7 terminal), 2929960 minterms, vars: 21r/21c/3nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 1622 iterations in 80.76 seconds (average 0.049790, setup 0.00)

Prob1A: 1 iterations in 0.01 seconds (average 0.010000, setup 0.00)

yes = 1295218, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 80.896 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

