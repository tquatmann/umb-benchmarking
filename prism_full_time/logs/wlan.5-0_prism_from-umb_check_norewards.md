# Log files for prism_from-umb_check_norewards on model [wlan.5-0](../../models/wlan.5-0)

Parsed values: `[233.922, 223.988, 292.609, 216.687, 242.153]`



### Log file: prism_from-umb_check_norewards_wlan.5-0_rep1.log

```
Command(s):
../bin/prism  -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props
Wallclock time: 233.922 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:18:11 GMT+01:00 2026
Hostname: r23m0080.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 170 iterations in 1.93 seconds (average 0.011353, setup 0.00)

Time for model construction: 171.532 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 182051 nodes (7 terminal), 2929960 minterms, vars: 21r/21c/3nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 1622 iterations in 61.48 seconds (average 0.037904, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1295218, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 61.612 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_wlan.5-0_rep2.log

```
Command(s):
../bin/prism  -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props
Wallclock time: 223.988 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:50 GMT+01:00 2026
Hostname: n23m0324.hpc.itc.rwth-aachen.de
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
Importing transitions... [ 2% 4% 6% 8% 10% 12% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 170 iterations in 1.86 seconds (average 0.010941, setup 0.00)

Time for model construction: 161.899 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 182051 nodes (7 terminal), 2929960 minterms, vars: 21r/21c/3nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 1622 iterations in 61.15 seconds (average 0.037700, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1295218, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 61.301 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_wlan.5-0_rep3.log

```
Command(s):
../bin/prism  -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props
Wallclock time: 292.609 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:50 GMT+01:00 2026
Hostname: r23m0214.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 170 iterations in 2.20 seconds (average 0.012941, setup 0.00)

Time for model construction: 216.333 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 182051 nodes (7 terminal), 2929960 minterms, vars: 21r/21c/3nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 1622 iterations in 74.97 seconds (average 0.046221, setup 0.00)

Prob1A: 1 iterations in 0.01 seconds (average 0.010000, setup 0.00)

yes = 1295218, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 75.334 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_wlan.5-0_rep4.log

```
Command(s):
../bin/prism  -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props
Wallclock time: 216.687 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:55:32 GMT+01:00 2026
Hostname: n23m0168.hpc.itc.rwth-aachen.de
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
Importing transitions... [ 2% 4% 6% 8% 10% 12% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 170 iterations in 1.91 seconds (average 0.011235, setup 0.00)

Time for model construction: 153.948 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 182051 nodes (7 terminal), 2929960 minterms, vars: 21r/21c/3nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 1622 iterations in 61.69 seconds (average 0.038033, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1295218, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 61.852 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_wlan.5-0_rep5.log

```
Command(s):
../bin/prism  -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props
Wallclock time: 242.153 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:51:27 GMT+01:00 2026
Hostname: n23m0333.hpc.itc.rwth-aachen.de
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
Importing transitions... [ 2% 4% 6% 8% 10% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 170 iterations in 2.10 seconds (average 0.012353, setup 0.00)

Time for model construction: 171.848 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 182051 nodes (7 terminal), 2929960 minterms, vars: 21r/21c/3nd

Probability bound in formula is 0/1 so not computing exact probabilities...

Prob0E: 1622 iterations in 69.33 seconds (average 0.042744, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1295218, no = 0, maybe = 0

Property satisfied in 1 of 1 initial states.

Time for model checking: 69.501 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

