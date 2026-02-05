# Log files

Tool configuration: prism_from-prism_check_default
Benchmark: [csma.3-4](../../models/csma.3-4)
Parsed values: [1.124, 1.692, 2.101, 1.062, 1.191]



### Log file: prism_from-prism_check_default_csma.3-4_rep1.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism models/csma.3-4/property.props
Wallclock time: 31.772 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:49:59 GMT+01:00 2026
Hostname: n23m0200.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism models/csma.3-4/property.props

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.3-4/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 0.90 seconds (average 0.006667, setup 0.00)

Time for model construction: 1.124 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Prob0A: 133 iterations in 2.10 seconds (average 0.015789, setup 0.00)

Prob1E: 533 iterations in 18.75 seconds (average 0.035178, setup 0.00)

yes = 710317, no = 31622, maybe = 718348

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=14, levels=51, nodes=195961] [9.0 MB]
Adding sparse bits... [levels=17-50, num=4654, compact=14/14] [8.7 MB]
Creating vector for yes... [dist=2, compact] [2.8 MB]
Allocating iteration vectors... [3 x 11.1 MB]
TOTAL: [53.9 MB]

Starting iterations...

Iterative method: 97 iterations in 6.37 seconds (average 0.036804, setup 2.80)

Value in the initial state: 0.9324464641692023

Time for model checking: 27.354 seconds.

Result: 0.9324464641692023 (+/- 3.784720206123637E-6 estimated; rel err 4.0589142128344855E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_csma.3-4_rep2.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism models/csma.3-4/property.props
Wallclock time: 40.154 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:22:07 GMT+01:00 2026
Hostname: n23m0237.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism models/csma.3-4/property.props

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.3-4/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 1.46 seconds (average 0.010815, setup 0.00)

Time for model construction: 1.692 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Prob0A: 133 iterations in 3.01 seconds (average 0.022632, setup 0.00)

Prob1E: 533 iterations in 27.31 seconds (average 0.051238, setup 0.00)

yes = 710317, no = 31622, maybe = 718348

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=14, levels=51, nodes=195961] [9.0 MB]
Adding sparse bits... [levels=17-50, num=4654, compact=14/14] [8.7 MB]
Creating vector for yes... [dist=2, compact] [2.8 MB]
Allocating iteration vectors... [3 x 11.1 MB]
TOTAL: [53.9 MB]

Starting iterations...

Iterative method: 97 iterations in 7.19 seconds (average 0.038866, setup 3.42)

Value in the initial state: 0.9324464641692023

Time for model checking: 37.706 seconds.

Result: 0.9324464641692023 (+/- 3.784720206123637E-6 estimated; rel err 4.0589142128344855E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_csma.3-4_rep3.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism models/csma.3-4/property.props
Wallclock time: 43.301 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:18:31 GMT+01:00 2026
Hostname: n23m0099.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism models/csma.3-4/property.props

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.3-4/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 1.58 seconds (average 0.011704, setup 0.00)

Time for model construction: 2.101 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Prob0A: 133 iterations in 3.20 seconds (average 0.024060, setup 0.00)

Prob1E: 533 iterations in 28.25 seconds (average 0.053002, setup 0.00)

yes = 710317, no = 31622, maybe = 718348

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=14, levels=51, nodes=195961] [9.0 MB]
Adding sparse bits... [levels=17-50, num=4654, compact=14/14] [8.7 MB]
Creating vector for yes... [dist=2, compact] [2.8 MB]
Allocating iteration vectors... [3 x 11.1 MB]
TOTAL: [53.9 MB]

Starting iterations...

Iterative method: 97 iterations in 8.61 seconds (average 0.048454, setup 3.91)

Value in the initial state: 0.9324464641692023

Time for model checking: 40.382 seconds.

Result: 0.9324464641692023 (+/- 3.784720206123637E-6 estimated; rel err 4.0589142128344855E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_csma.3-4_rep4.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism models/csma.3-4/property.props
Wallclock time: 28.046 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:28:43 GMT+01:00 2026
Hostname: n23m0142.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism models/csma.3-4/property.props

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.3-4/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 0.89 seconds (average 0.006593, setup 0.00)

Time for model construction: 1.062 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Prob0A: 133 iterations in 2.03 seconds (average 0.015263, setup 0.00)

Prob1E: 533 iterations in 17.81 seconds (average 0.033415, setup 0.00)

yes = 710317, no = 31622, maybe = 718348

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=14, levels=51, nodes=195961] [9.0 MB]
Adding sparse bits... [levels=17-50, num=4654, compact=14/14] [8.7 MB]
Creating vector for yes... [dist=2, compact] [2.8 MB]
Allocating iteration vectors... [3 x 11.1 MB]
TOTAL: [53.9 MB]

Starting iterations...

Iterative method: 97 iterations in 6.32 seconds (average 0.035876, setup 2.84)

Value in the initial state: 0.9324464641692023

Time for model checking: 26.415 seconds.

Result: 0.9324464641692023 (+/- 3.784720206123637E-6 estimated; rel err 4.0589142128344855E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_csma.3-4_rep5.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism models/csma.3-4/property.props
Wallclock time: 31.873 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:20:33 GMT+01:00 2026
Hostname: r23m0023.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism models/csma.3-4/property.props

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.3-4/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 0.94 seconds (average 0.006963, setup 0.00)

Time for model construction: 1.191 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Prob0A: 133 iterations in 2.17 seconds (average 0.016316, setup 0.00)

Prob1E: 533 iterations in 19.31 seconds (average 0.036229, setup 0.00)

yes = 710317, no = 31622, maybe = 718348

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=14, levels=51, nodes=195961] [9.0 MB]
Adding sparse bits... [levels=17-50, num=4654, compact=14/14] [8.7 MB]
Creating vector for yes... [dist=2, compact] [2.8 MB]
Allocating iteration vectors... [3 x 11.1 MB]
TOTAL: [53.9 MB]

Starting iterations...

Iterative method: 97 iterations in 6.59 seconds (average 0.037835, setup 2.92)

Value in the initial state: 0.9324464641692023

Time for model checking: 28.313 seconds.

Result: 0.9324464641692023 (+/- 3.784720206123637E-6 estimated; rel err 4.0589142128344855E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

