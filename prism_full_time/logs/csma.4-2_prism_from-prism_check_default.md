# Log files for prism_from-prism_check_default on model [csma.4-2](../../models/csma.4-2)

Parsed values: `[26.818, 24.913, 30.375, 31.516, 28.596]`



### Log file: prism_from-prism_check_default_csma.4-2_rep1.log

```
Command(s):
../bin/prism  models/csma.4-2/model.prism models/csma.4-2/property.props
Wallclock time: 26.818 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:23:28 GMT+01:00 2026
Hostname: n23m0275.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.4-2/model.prism models/csma.4-2/property.props

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.4-2/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 193 iterations in 1.01 seconds (average 0.005233, setup 0.00)

Time for model construction: 1.095 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 52233 nodes (4 terminal), 1327068 minterms, vars: 54r/54c/17nd

Prob0A: 186 iterations in 1.69 seconds (average 0.009086, setup 0.00)

Prob1E: 1017 iterations in 18.28 seconds (average 0.017974, setup 0.00)

yes = 142601, no = 25408, maybe = 593953

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=18, levels=54, nodes=144135] [6.6 MB]
Adding sparse bits... [levels=26-54, num=998, compact=18/18] [14.4 MB]
Creating vector for yes... [dist=2, compact] [1.5 MB]
Allocating iteration vectors... [3 x 5.8 MB]
TOTAL: [39.9 MB]

Starting iterations...

Iterative method: 172 iterations in 5.03 seconds (average 0.027616, setup 0.28)

Value in the initial state: 0.776459404375732

Time for model checking: 25.116 seconds.

Result: 0.776459404375732 (+/- 6.170084370362843E-6 estimated; rel err 7.946435236139033E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_csma.4-2_rep2.log

```
Command(s):
../bin/prism  models/csma.4-2/model.prism models/csma.4-2/property.props
Wallclock time: 24.913 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:11:22 GMT+01:00 2026
Hostname: n23m0333.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.4-2/model.prism models/csma.4-2/property.props

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.4-2/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 193 iterations in 1.50 seconds (average 0.007772, setup 0.00)

Time for model construction: 1.609 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 52233 nodes (4 terminal), 1327068 minterms, vars: 54r/54c/17nd

Prob0A: 186 iterations in 1.76 seconds (average 0.009462, setup 0.00)

Prob1E: 1017 iterations in 15.86 seconds (average 0.015595, setup 0.00)

yes = 142601, no = 25408, maybe = 593953

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=18, levels=54, nodes=144135] [6.6 MB]
Adding sparse bits... [levels=26-54, num=998, compact=18/18] [14.4 MB]
Creating vector for yes... [dist=2, compact] [1.5 MB]
Allocating iteration vectors... [3 x 5.8 MB]
TOTAL: [39.9 MB]

Starting iterations...

Iterative method: 172 iterations in 4.98 seconds (average 0.027384, setup 0.27)

Value in the initial state: 0.776459404375732

Time for model checking: 22.701 seconds.

Result: 0.776459404375732 (+/- 6.170084370362843E-6 estimated; rel err 7.946435236139033E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_csma.4-2_rep3.log

```
Command(s):
../bin/prism  models/csma.4-2/model.prism models/csma.4-2/property.props
Wallclock time: 30.375 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:36:48 GMT+01:00 2026
Hostname: n23m0132.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.4-2/model.prism models/csma.4-2/property.props

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.4-2/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 193 iterations in 1.10 seconds (average 0.005699, setup 0.00)

Time for model construction: 1.217 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 52233 nodes (4 terminal), 1327068 minterms, vars: 54r/54c/17nd

Prob0A: 186 iterations in 1.99 seconds (average 0.010699, setup 0.00)

Prob1E: 1017 iterations in 18.22 seconds (average 0.017915, setup 0.00)

yes = 142601, no = 25408, maybe = 593953

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=18, levels=54, nodes=144135] [6.6 MB]
Adding sparse bits... [levels=26-54, num=998, compact=18/18] [14.4 MB]
Creating vector for yes... [dist=2, compact] [1.5 MB]
Allocating iteration vectors... [3 x 5.8 MB]
TOTAL: [39.9 MB]

Starting iterations...

Iterative method: 172 iterations in 5.23 seconds (average 0.028721, setup 0.29)

Value in the initial state: 0.776459404375732

Time for model checking: 25.531 seconds.

Result: 0.776459404375732 (+/- 6.170084370362843E-6 estimated; rel err 7.946435236139033E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_csma.4-2_rep4.log

```
Command(s):
../bin/prism  models/csma.4-2/model.prism models/csma.4-2/property.props
Wallclock time: 31.516 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:13 GMT+01:00 2026
Hostname: n23m0075.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.4-2/model.prism models/csma.4-2/property.props

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.4-2/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 193 iterations in 1.06 seconds (average 0.005492, setup 0.00)

Time for model construction: 1.178 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 52233 nodes (4 terminal), 1327068 minterms, vars: 54r/54c/17nd

Prob0A: 186 iterations in 1.74 seconds (average 0.009355, setup 0.00)

Prob1E: 1017 iterations in 16.12 seconds (average 0.015851, setup 0.00)

yes = 142601, no = 25408, maybe = 593953

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=18, levels=54, nodes=144135] [6.6 MB]
Adding sparse bits... [levels=26-54, num=998, compact=18/18] [14.4 MB]
Creating vector for yes... [dist=2, compact] [1.5 MB]
Allocating iteration vectors... [3 x 5.8 MB]
TOTAL: [39.9 MB]

Starting iterations...
Iteration 163: max relative diff=0.000047, 5.03 sec so far

Iterative method: 172 iterations in 5.62 seconds (average 0.030872, setup 0.31)

Value in the initial state: 0.776459404375732

Time for model checking: 23.601 seconds.

Result: 0.776459404375732 (+/- 6.170084370362843E-6 estimated; rel err 7.946435236139033E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_csma.4-2_rep5.log

```
Command(s):
../bin/prism  models/csma.4-2/model.prism models/csma.4-2/property.props
Wallclock time: 28.596 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:25 GMT+01:00 2026
Hostname: n23m0196.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.4-2/model.prism models/csma.4-2/property.props

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.4-2/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 193 iterations in 1.14 seconds (average 0.005907, setup 0.00)

Time for model construction: 1.258 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 52233 nodes (4 terminal), 1327068 minterms, vars: 54r/54c/17nd

Prob0A: 186 iterations in 2.00 seconds (average 0.010753, setup 0.00)

Prob1E: 1017 iterations in 18.30 seconds (average 0.017994, setup 0.00)

yes = 142601, no = 25408, maybe = 593953

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=18, levels=54, nodes=144135] [6.6 MB]
Adding sparse bits... [levels=26-54, num=998, compact=18/18] [14.4 MB]
Creating vector for yes... [dist=2, compact] [1.5 MB]
Allocating iteration vectors... [3 x 5.8 MB]
TOTAL: [39.9 MB]

Starting iterations...
Iteration 153: max relative diff=0.001402, 5.04 sec so far

Iterative method: 172 iterations in 5.98 seconds (average 0.032907, setup 0.32)

Value in the initial state: 0.776459404375732

Time for model checking: 26.393 seconds.

Result: 0.776459404375732 (+/- 6.170084370362843E-6 estimated; rel err 7.946435236139033E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

