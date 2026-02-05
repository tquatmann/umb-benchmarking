# Log files

Tool configuration: prism_from-umb_check_default
Benchmark: [csma.3-4](../../models/csma.3-4)
Parsed values: [209.524, 262.035, 174.755, 263.349, 239.787]



### Log file: prism_from-umb_check_default_csma.3-4_rep1.log

```
Command(s):
../bin/prism  -importmodel models/csma.3-4/prism.model.umb models/csma.3-4/property.props
Wallclock time: 464.977 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:20:15 GMT+01:00 2026
Hostname: r23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/csma.3-4/prism.model.umb models/csma.3-4/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   x
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.3-4/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 135 iterations in 10.39 seconds (average 0.076963, setup 0.00)

Time for model construction: 209.524 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 409392 nodes (6 terminal), 2396727 minterms, vars: 21r/21c/3nd

Prob0A: 133 iterations in 7.05 seconds (average 0.053008, setup 0.00)

Prob1E: 533 iterations in 51.94 seconds (average 0.097448, setup 0.00)

yes = 710317, no = 31622, maybe = 718348

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=3, levels=21, nodes=372670] [17.1 MB]
Adding sparse bits... [levels=4-17, num=15356, compact=3/3] [2.3 MB]
Creating vector for yes... [dist=2, compact] [2.8 MB]
Allocating iteration vectors... [3 x 11.1 MB]
TOTAL: [55.5 MB]

Starting iterations...

Iterative method: 97 iterations in 194.75 seconds (average 0.049691, setup 189.93)

Value in the initial state: 0.9324464641692023

Time for model checking: 254.59 seconds.

Result: 0.9324464641692023 (+/- 3.784720206123637E-6 estimated; rel err 4.0589142128344855E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_csma.3-4_rep2.log

```
Command(s):
../bin/prism  -importmodel models/csma.3-4/prism.model.umb models/csma.3-4/property.props
Wallclock time: 709.555 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:24:01 GMT+01:00 2026
Hostname: r23m0071.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/csma.3-4/prism.model.umb models/csma.3-4/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   x
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.3-4/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 135 iterations in 12.13 seconds (average 0.089852, setup 0.00)

Time for model construction: 262.035 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 409392 nodes (6 terminal), 2396727 minterms, vars: 21r/21c/3nd

Prob0A: 133 iterations in 8.53 seconds (average 0.064135, setup 0.00)

Prob1E: 533 iterations in 61.26 seconds (average 0.114934, setup 0.00)

yes = 710317, no = 31622, maybe = 718348

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=3, levels=21, nodes=372670] [17.1 MB]
Adding sparse bits... [levels=4-17, num=15356, compact=3/3] [2.3 MB]
Creating vector for yes... [dist=2, compact] [2.8 MB]
Allocating iteration vectors... [3 x 11.1 MB]
TOTAL: [55.5 MB]

Starting iterations...
Iteration 95: max relative diff=0.000001, 5.04 sec so far

Iterative method: 97 iterations in 375.09 seconds (average 0.052990, setup 369.95)

Value in the initial state: 0.9324464641692023

Time for model checking: 446.256 seconds.

Result: 0.9324464641692023 (+/- 3.784720206123637E-6 estimated; rel err 4.0589142128344855E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_csma.3-4_rep3.log

```
Command(s):
../bin/prism  -importmodel models/csma.3-4/prism.model.umb models/csma.3-4/property.props
Wallclock time: 373.425 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:06 GMT+01:00 2026
Hostname: r23m0136.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/csma.3-4/prism.model.umb models/csma.3-4/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   x
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.3-4/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 8% 10% 12% 14% 16% 18% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 135 iterations in 9.19 seconds (average 0.068074, setup 0.00)

Time for model construction: 174.755 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 409392 nodes (6 terminal), 2396727 minterms, vars: 21r/21c/3nd

Prob0A: 133 iterations in 6.27 seconds (average 0.047143, setup 0.00)

Prob1E: 533 iterations in 44.38 seconds (average 0.083265, setup 0.00)

yes = 710317, no = 31622, maybe = 718348

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=3, levels=21, nodes=372670] [17.1 MB]
Adding sparse bits... [levels=4-17, num=15356, compact=3/3] [2.3 MB]
Creating vector for yes... [dist=2, compact] [2.8 MB]
Allocating iteration vectors... [3 x 11.1 MB]
TOTAL: [55.5 MB]

Starting iterations...

Iterative method: 97 iterations in 146.27 seconds (average 0.045464, setup 141.86)

Value in the initial state: 0.9324464641692023

Time for model checking: 197.422 seconds.

Result: 0.9324464641692023 (+/- 3.784720206123637E-6 estimated; rel err 4.0589142128344855E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_csma.3-4_rep4.log

```
Command(s):
../bin/prism  -importmodel models/csma.3-4/prism.model.umb models/csma.3-4/property.props
Wallclock time: 586.192 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:10 GMT+01:00 2026
Hostname: n23m0085.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/csma.3-4/prism.model.umb models/csma.3-4/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   x
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.3-4/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 135 iterations in 11.96 seconds (average 0.088593, setup 0.00)

Time for model construction: 263.349 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 409392 nodes (6 terminal), 2396727 minterms, vars: 21r/21c/3nd

Prob0A: 133 iterations in 8.53 seconds (average 0.064135, setup 0.00)

Prob1E: 533 iterations in 60.65 seconds (average 0.113790, setup 0.00)

yes = 710317, no = 31622, maybe = 718348

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=3, levels=21, nodes=372670] [17.1 MB]
Adding sparse bits... [levels=4-17, num=15356, compact=3/3] [2.3 MB]
Creating vector for yes... [dist=2, compact] [2.8 MB]
Allocating iteration vectors... [3 x 11.1 MB]
TOTAL: [55.5 MB]

Starting iterations...

Iterative method: 97 iterations in 246.34 seconds (average 0.048969, setup 241.59)

Value in the initial state: 0.9324464641692023

Time for model checking: 317.152 seconds.

Result: 0.9324464641692023 (+/- 3.784720206123637E-6 estimated; rel err 4.0589142128344855E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_csma.3-4_rep5.log

```
Command(s):
../bin/prism  -importmodel models/csma.3-4/prism.model.umb models/csma.3-4/property.props
Wallclock time: 712.338 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:02:01 GMT+01:00 2026
Hostname: n23m0061.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/csma.3-4/prism.model.umb models/csma.3-4/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   x
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.3-4/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 135 iterations in 11.12 seconds (average 0.082370, setup 0.00)

Time for model construction: 239.787 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 409392 nodes (6 terminal), 2396727 minterms, vars: 21r/21c/3nd

Prob0A: 133 iterations in 7.89 seconds (average 0.059323, setup 0.00)

Prob1E: 533 iterations in 55.58 seconds (average 0.104278, setup 0.00)

yes = 710317, no = 31622, maybe = 718348

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=3, levels=21, nodes=372670] [17.1 MB]
Adding sparse bits... [levels=4-17, num=15356, compact=3/3] [2.3 MB]
Creating vector for yes... [dist=2, compact] [2.8 MB]
Allocating iteration vectors... [3 x 11.1 MB]
TOTAL: [55.5 MB]

Starting iterations...

Iterative method: 97 iterations in 406.93 seconds (average 0.047732, setup 402.30)

Value in the initial state: 0.9324464641692023

Time for model checking: 471.513 seconds.

Result: 0.9324464641692023 (+/- 3.784720206123637E-6 estimated; rel err 4.0589142128344855E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

