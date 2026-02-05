# Log files

Tool configuration: prism_from-prism_check_norewards
Benchmark: [csma.4-2](../../models/csma.4-2)
Parsed values: [28.463, 26.858, 30.575, 29.311, 31.173]



### Log file: prism_from-prism_check_norewards_csma.4-2_rep1.log

```
Command(s):
../bin/prism  models/csma.4-2/model.prism models/csma.4-2/property.props
Wallclock time: 28.463 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:33:51 GMT+01:00 2026
Hostname: r23m0206.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 193 iterations in 1.17 seconds (average 0.006062, setup 0.00)

Time for model construction: 1.272 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 52233 nodes (4 terminal), 1327068 minterms, vars: 54r/54c/17nd

Prob0A: 186 iterations in 2.34 seconds (average 0.012581, setup 0.00)

Prob1E: 1017 iterations in 19.09 seconds (average 0.018771, setup 0.00)

yes = 142601, no = 25408, maybe = 593953

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=18, levels=54, nodes=144135] [6.6 MB]
Adding sparse bits... [levels=26-54, num=998, compact=18/18] [14.4 MB]
Creating vector for yes... [dist=2, compact] [1.5 MB]
Allocating iteration vectors... [3 x 5.8 MB]
TOTAL: [39.9 MB]

Starting iterations...

Iterative method: 172 iterations in 5.09 seconds (average 0.027965, setup 0.28)

Value in the initial state: 0.776459404375732

Time for model checking: 26.629 seconds.

Result: 0.776459404375732 (+/- 6.170084370362843E-6 estimated; rel err 7.946435236139033E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_csma.4-2_rep2.log

```
Command(s):
../bin/prism  models/csma.4-2/model.prism models/csma.4-2/property.props
Wallclock time: 26.858 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:06 GMT+01:00 2026
Hostname: r23m0173.hpc.itc.rwth-aachen.de
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

Time for model construction: 1.224 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 52233 nodes (4 terminal), 1327068 minterms, vars: 54r/54c/17nd

Prob0A: 186 iterations in 2.33 seconds (average 0.012527, setup 0.00)

Prob1E: 1017 iterations in 17.12 seconds (average 0.016834, setup 0.00)

yes = 142601, no = 25408, maybe = 593953

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=18, levels=54, nodes=144135] [6.6 MB]
Adding sparse bits... [levels=26-54, num=998, compact=18/18] [14.4 MB]
Creating vector for yes... [dist=2, compact] [1.5 MB]
Allocating iteration vectors... [3 x 5.8 MB]
TOTAL: [39.9 MB]

Starting iterations...

Iterative method: 172 iterations in 4.97 seconds (average 0.027326, setup 0.27)

Value in the initial state: 0.776459404375732

Time for model checking: 24.523 seconds.

Result: 0.776459404375732 (+/- 6.170084370362843E-6 estimated; rel err 7.946435236139033E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_csma.4-2_rep3.log

```
Command(s):
../bin/prism  models/csma.4-2/model.prism models/csma.4-2/property.props
Wallclock time: 30.575 seconds
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

Time for model construction: 1.226 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 52233 nodes (4 terminal), 1327068 minterms, vars: 54r/54c/17nd

Prob0A: 186 iterations in 2.04 seconds (average 0.010968, setup 0.00)

Prob1E: 1017 iterations in 18.41 seconds (average 0.018102, setup 0.00)

yes = 142601, no = 25408, maybe = 593953

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=18, levels=54, nodes=144135] [6.6 MB]
Adding sparse bits... [levels=26-54, num=998, compact=18/18] [14.4 MB]
Creating vector for yes... [dist=2, compact] [1.5 MB]
Allocating iteration vectors... [3 x 5.8 MB]
TOTAL: [39.9 MB]

Starting iterations...

Iterative method: 172 iterations in 5.23 seconds (average 0.028779, setup 0.28)

Value in the initial state: 0.776459404375732

Time for model checking: 25.766 seconds.

Result: 0.776459404375732 (+/- 6.170084370362843E-6 estimated; rel err 7.946435236139033E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_csma.4-2_rep4.log

```
Command(s):
../bin/prism  models/csma.4-2/model.prism models/csma.4-2/property.props
Wallclock time: 29.311 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:05:06 GMT+01:00 2026
Hostname: r23m0023.hpc.itc.rwth-aachen.de
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

Time for model construction: 1.244 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 52233 nodes (4 terminal), 1327068 minterms, vars: 54r/54c/17nd

Prob0A: 186 iterations in 2.28 seconds (average 0.012258, setup 0.00)

Prob1E: 1017 iterations in 19.58 seconds (average 0.019253, setup 0.00)

yes = 142601, no = 25408, maybe = 593953

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=18, levels=54, nodes=144135] [6.6 MB]
Adding sparse bits... [levels=26-54, num=998, compact=18/18] [14.4 MB]
Creating vector for yes... [dist=2, compact] [1.5 MB]
Allocating iteration vectors... [3 x 5.8 MB]
TOTAL: [39.9 MB]

Starting iterations...
Iteration 167: max relative diff=0.000007, 5.01 sec so far

Iterative method: 172 iterations in 5.46 seconds (average 0.030000, setup 0.30)

Value in the initial state: 0.776459404375732

Time for model checking: 27.462 seconds.

Result: 0.776459404375732 (+/- 6.170084370362843E-6 estimated; rel err 7.946435236139033E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_csma.4-2_rep5.log

```
Command(s):
../bin/prism  models/csma.4-2/model.prism models/csma.4-2/property.props
Wallclock time: 31.173 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:07:37 GMT+01:00 2026
Hostname: n23m0386.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 193 iterations in 1.09 seconds (average 0.005648, setup 0.00)

Time for model construction: 1.188 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 52233 nodes (4 terminal), 1327068 minterms, vars: 54r/54c/17nd

Prob0A: 186 iterations in 2.25 seconds (average 0.012097, setup 0.00)

Prob1E: 1017 iterations in 21.57 seconds (average 0.021209, setup 0.00)

yes = 142601, no = 25408, maybe = 593953

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=18, levels=54, nodes=144135] [6.6 MB]
Adding sparse bits... [levels=26-54, num=998, compact=18/18] [14.4 MB]
Creating vector for yes... [dist=2, compact] [1.5 MB]
Allocating iteration vectors... [3 x 5.8 MB]
TOTAL: [39.9 MB]

Starting iterations...
Iteration 169: max relative diff=0.000003, 5.01 sec so far

Iterative method: 172 iterations in 5.40 seconds (average 0.029651, setup 0.30)

Value in the initial state: 0.776459404375732

Time for model checking: 29.358 seconds.

Result: 0.776459404375732 (+/- 6.170084370362843E-6 estimated; rel err 7.946435236139033E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

