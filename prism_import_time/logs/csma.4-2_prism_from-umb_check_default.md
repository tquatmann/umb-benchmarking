# Log files for prism_from-umb_check_default on model [csma.4-2](../../models/csma.4-2)

Parsed values: `[120.409, 98.687, 164.353, 163.404, 89.087]`



### Log file: prism_from-umb_check_default_csma.4-2_rep1.log

```
Command(s):
../bin/prism  -importmodel models/csma.4-2/prism.model.umb models/csma.4-2/property.props
Wallclock time: 326.050 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:19:43 GMT+01:00 2026
Hostname: r23m0157.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/csma.4-2/prism.model.umb models/csma.4-2/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   x
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.4-2/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:symbolic)...
Importing transitions... [ 4% 8% 12% 16% 18% 22% 24% 28% 30% 34% 36% 40% 42% 44% 48% 50% 52% 54% 58% 60% 62% 64% 68% 70% 72% 74% 78% 80% 82% 84% 86% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 193 iterations in 10.64 seconds (average 0.055130, setup 0.00)

Time for model construction: 120.409 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 281710 nodes (4 terminal), 1327068 minterms, vars: 20r/20c/4nd

Prob0A: 186 iterations in 9.08 seconds (average 0.048817, setup 0.00)

Prob1E: 1017 iterations in 73.73 seconds (average 0.072498, setup 0.00)

yes = 142601, no = 25408, maybe = 593953

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=20, nodes=331057] [15.2 MB]
Adding sparse bits... [levels=4-17, num=20041, compact=4/4] [3.3 MB]
Creating vector for yes... [dist=2, compact] [1.5 MB]
Allocating iteration vectors... [3 x 5.8 MB]
TOTAL: [37.3 MB]

Starting iterations...
Iteration 127: max relative diff=0.199869, 5.02 sec so far

Iterative method: 172 iterations in 121.28 seconds (average 0.039535, setup 114.48)

Value in the initial state: 0.776459404375732

Time for model checking: 204.808 seconds.

Result: 0.776459404375732 (+/- 6.170084370362843E-6 estimated; rel err 7.946435236139033E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_csma.4-2_rep2.log

```
Command(s):
../bin/prism  -importmodel models/csma.4-2/prism.model.umb models/csma.4-2/property.props
Wallclock time: 251.978 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:20:33 GMT+01:00 2026
Hostname: n23m0241.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/csma.4-2/prism.model.umb models/csma.4-2/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   x
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.4-2/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:symbolic)...
Importing transitions... [ 4% 8% 12% 18% 22% 26% 28% 32% 36% 40% 42% 46% 50% 54% 56% 60% 62% 66% 70% 72% 76% 78% 82% 84% 86% 90% 92% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 193 iterations in 9.53 seconds (average 0.049378, setup 0.00)

Time for model construction: 98.687 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 281710 nodes (4 terminal), 1327068 minterms, vars: 20r/20c/4nd

Prob0A: 186 iterations in 8.09 seconds (average 0.043495, setup 0.00)

Prob1E: 1017 iterations in 66.03 seconds (average 0.064926, setup 0.00)

yes = 142601, no = 25408, maybe = 593953

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=20, nodes=331057] [15.2 MB]
Adding sparse bits... [levels=4-17, num=20041, compact=4/4] [3.3 MB]
Creating vector for yes... [dist=2, compact] [1.5 MB]
Allocating iteration vectors... [3 x 5.8 MB]
TOTAL: [37.3 MB]

Starting iterations...
Iteration 139: max relative diff=0.021665, 5.03 sec so far

Iterative method: 172 iterations in 77.44 seconds (average 0.036163, setup 71.22)

Value in the initial state: 0.776459404375732

Time for model checking: 152.21 seconds.

Result: 0.776459404375732 (+/- 6.170084370362843E-6 estimated; rel err 7.946435236139033E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_csma.4-2_rep3.log

```
Command(s):
../bin/prism  -importmodel models/csma.4-2/prism.model.umb models/csma.4-2/property.props
Wallclock time: 535.870 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:09 GMT+01:00 2026
Hostname: n23m0347.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/csma.4-2/prism.model.umb models/csma.4-2/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   x
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.4-2/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 193 iterations in 12.83 seconds (average 0.066477, setup 0.00)

Time for model construction: 164.353 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 281710 nodes (4 terminal), 1327068 minterms, vars: 20r/20c/4nd

Prob0A: 186 iterations in 11.11 seconds (average 0.059731, setup 0.00)

Prob1E: 1017 iterations in 96.55 seconds (average 0.094936, setup 0.00)

yes = 142601, no = 25408, maybe = 593953

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=20, nodes=331057] [15.2 MB]
Adding sparse bits... [levels=4-17, num=20041, compact=4/4] [3.3 MB]
Creating vector for yes... [dist=2, compact] [1.5 MB]
Allocating iteration vectors... [3 x 5.8 MB]
TOTAL: [37.3 MB]

Starting iterations...
Iteration 111: max relative diff=1.931766, 5.05 sec so far

Iterative method: 172 iterations in 257.44 seconds (average 0.047151, setup 249.33)

Value in the initial state: 0.776459404375732

Time for model checking: 366.33 seconds.

Result: 0.776459404375732 (+/- 6.170084370362843E-6 estimated; rel err 7.946435236139033E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_csma.4-2_rep4.log

```
Command(s):
../bin/prism  -importmodel models/csma.4-2/prism.model.umb models/csma.4-2/property.props
Wallclock time: 550.152 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 02:50:14 GMT+01:00 2026
Hostname: n23m0033.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/csma.4-2/prism.model.umb models/csma.4-2/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   x
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.4-2/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 6% 10% 12% 14% 16% 18% 20% 22% 24% 26% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 193 iterations in 12.94 seconds (average 0.067047, setup 0.00)

Time for model construction: 163.404 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 281710 nodes (4 terminal), 1327068 minterms, vars: 20r/20c/4nd

Prob0A: 186 iterations in 11.28 seconds (average 0.060645, setup 0.00)

Prob1E: 1017 iterations in 94.29 seconds (average 0.092714, setup 0.00)

yes = 142601, no = 25408, maybe = 593953

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=20, nodes=331057] [15.2 MB]
Adding sparse bits... [levels=4-17, num=20041, compact=4/4] [3.3 MB]
Creating vector for yes... [dist=2, compact] [1.5 MB]
Allocating iteration vectors... [3 x 5.8 MB]
TOTAL: [37.3 MB]

Starting iterations...
Iteration 117: max relative diff=0.707506, 5.03 sec so far

Iterative method: 172 iterations in 277.39 seconds (average 0.043023, setup 269.99)

Value in the initial state: 0.776459404375732

Time for model checking: 384.206 seconds.

Result: 0.776459404375732 (+/- 6.170084370362843E-6 estimated; rel err 7.946435236139033E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_csma.4-2_rep5.log

```
Command(s):
../bin/prism  -importmodel models/csma.4-2/prism.model.umb models/csma.4-2/property.props
Wallclock time: 228.681 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:02:30 GMT+01:00 2026
Hostname: n23m0141.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/csma.4-2/prism.model.umb models/csma.4-2/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   x
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.4-2/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:symbolic)...
Importing transitions... [ 4% 10% 14% 18% 22% 26% 32% 36% 38% 42% 46% 50% 54% 58% 60% 64% 68% 72% 74% 78% 82% 84% 88% 90% 94% 98% 100% ]

Computing reachable states...

Reachability (BFS): 193 iterations in 8.61 seconds (average 0.044611, setup 0.00)

Time for model construction: 89.087 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 281710 nodes (4 terminal), 1327068 minterms, vars: 20r/20c/4nd

Prob0A: 186 iterations in 7.41 seconds (average 0.039839, setup 0.00)

Prob1E: 1017 iterations in 58.91 seconds (average 0.057925, setup 0.00)

yes = 142601, no = 25408, maybe = 593953

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=20, nodes=331057] [15.2 MB]
Adding sparse bits... [levels=4-17, num=20041, compact=4/4] [3.3 MB]
Creating vector for yes... [dist=2, compact] [1.5 MB]
Allocating iteration vectors... [3 x 5.8 MB]
TOTAL: [37.3 MB]

Starting iterations...
Iteration 161: max relative diff=0.000108, 5.01 sec so far

Iterative method: 172 iterations in 72.00 seconds (average 0.031105, setup 66.65)

Value in the initial state: 0.776459404375732

Time for model checking: 138.737 seconds.

Result: 0.776459404375732 (+/- 6.170084370362843E-6 estimated; rel err 7.946435236139033E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

