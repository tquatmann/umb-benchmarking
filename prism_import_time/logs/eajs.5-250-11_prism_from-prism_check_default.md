# Log files for prism_from-prism_check_default on model [eajs.5-250-11](../../models/eajs.5-250-11)

Parsed values: `[0.339, 0.257, 0.298, 0.329, 0.288]`



### Log file: prism_from-prism_check_default_eajs.5-250-11_rep1.log

```
Command(s):
../bin/prism  models/eajs.5-250-11/model.prism models/eajs.5-250-11/property.props
Wallclock time: 11.716 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 08:00:03 GMT+01:00 2026
Hostname: r23m0141.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.5-250-11/model.prism models/eajs.5-250-11/property.props

Parsing PRISM model file "models/eajs.5-250-11/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_5 Process_4
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 loc_5 t_5 t_4 loc_4
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Parsing properties file "models/eajs.5-250-11/property.props"...

1 property:
(1) "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

---------------------------------------------------------------------

Model checking: "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.10 seconds (average 0.001370, setup 0.00)

Time for model construction: 0.339 seconds.

Type:        MDP
States:      3049471 (1 initial)
Transitions: 6977654

Transition matrix: 25363 nodes (7 terminal), 6977654 minterms, vars: 43r/43c/5nd

Prob0E: 250 iterations in 0.24 seconds (average 0.000960, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 13476, inf = 0, maybe = 3035995

Computing remaining rewards...
Switching engine since hybrid engine does yet support this computation...
Engine: Sparse

Building sparse matrix (transitions)... [n=3049471, nc=4237377, nnz=6946802, k=10] [107.3 MB]
Building sparse matrix (transition rewards)... [n=3049471, nc=4237377, nnz=105040, k=10] [29.0 MB]
Creating vector for state rewards... [23.3 MB]
Creating vector for inf... [23.3 MB]
Allocating iteration vectors... [2 x 23.3 MB]
TOTAL: [229.4 MB]

Starting iterations...

Iterative method: 128 iterations in 10.54 seconds (average 0.028672, setup 6.87)

Value in the initial state: 10.03294060879421

Time for model checking: 10.82 seconds.

Result: 10.03294060879421 (+/- 7.366896484458609E-5 estimated; rel err 7.342709153487141E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_eajs.5-250-11_rep2.log

```
Command(s):
../bin/prism  models/eajs.5-250-11/model.prism models/eajs.5-250-11/property.props
Wallclock time: 11.260 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:00:57 GMT+01:00 2026
Hostname: n23m0307.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.5-250-11/model.prism models/eajs.5-250-11/property.props

Parsing PRISM model file "models/eajs.5-250-11/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_5 Process_4
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 loc_5 t_5 t_4 loc_4
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Parsing properties file "models/eajs.5-250-11/property.props"...

1 property:
(1) "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

---------------------------------------------------------------------

Model checking: "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.08 seconds (average 0.001096, setup 0.00)

Time for model construction: 0.257 seconds.

Type:        MDP
States:      3049471 (1 initial)
Transitions: 6977654

Transition matrix: 25363 nodes (7 terminal), 6977654 minterms, vars: 43r/43c/5nd

Prob0E: 250 iterations in 0.21 seconds (average 0.000840, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 13476, inf = 0, maybe = 3035995

Computing remaining rewards...
Switching engine since hybrid engine does yet support this computation...
Engine: Sparse

Building sparse matrix (transitions)... [n=3049471, nc=4237377, nnz=6946802, k=10] [107.3 MB]
Building sparse matrix (transition rewards)... [n=3049471, nc=4237377, nnz=105040, k=10] [29.0 MB]
Creating vector for state rewards... [23.3 MB]
Creating vector for inf... [23.3 MB]
Allocating iteration vectors... [2 x 23.3 MB]
TOTAL: [229.4 MB]

Starting iterations...

Iterative method: 128 iterations in 10.19 seconds (average 0.026953, setup 6.74)

Value in the initial state: 10.03294060879421

Time for model checking: 10.462 seconds.

Result: 10.03294060879421 (+/- 7.366896484458609E-5 estimated; rel err 7.342709153487141E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_eajs.5-250-11_rep3.log

```
Command(s):
../bin/prism  models/eajs.5-250-11/model.prism models/eajs.5-250-11/property.props
Wallclock time: 11.779 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:23:32 GMT+01:00 2026
Hostname: n23m0052.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.5-250-11/model.prism models/eajs.5-250-11/property.props

Parsing PRISM model file "models/eajs.5-250-11/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_5 Process_4
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 loc_5 t_5 t_4 loc_4
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Parsing properties file "models/eajs.5-250-11/property.props"...

1 property:
(1) "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

---------------------------------------------------------------------

Model checking: "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.09 seconds (average 0.001233, setup 0.00)

Time for model construction: 0.298 seconds.

Type:        MDP
States:      3049471 (1 initial)
Transitions: 6977654

Transition matrix: 25363 nodes (7 terminal), 6977654 minterms, vars: 43r/43c/5nd

Prob0E: 250 iterations in 0.24 seconds (average 0.000960, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 13476, inf = 0, maybe = 3035995

Computing remaining rewards...
Switching engine since hybrid engine does yet support this computation...
Engine: Sparse

Building sparse matrix (transitions)... [n=3049471, nc=4237377, nnz=6946802, k=10] [107.3 MB]
Building sparse matrix (transition rewards)... [n=3049471, nc=4237377, nnz=105040, k=10] [29.0 MB]
Creating vector for state rewards... [23.3 MB]
Creating vector for inf... [23.3 MB]
Allocating iteration vectors... [2 x 23.3 MB]
TOTAL: [229.4 MB]

Starting iterations...

Iterative method: 128 iterations in 10.62 seconds (average 0.030156, setup 6.76)

Value in the initial state: 10.03294060879421

Time for model checking: 10.888 seconds.

Result: 10.03294060879421 (+/- 7.366896484458609E-5 estimated; rel err 7.342709153487141E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_eajs.5-250-11_rep4.log

```
Command(s):
../bin/prism  models/eajs.5-250-11/model.prism models/eajs.5-250-11/property.props
Wallclock time: 12.913 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:24:38 GMT+01:00 2026
Hostname: n23m0142.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.5-250-11/model.prism models/eajs.5-250-11/property.props

Parsing PRISM model file "models/eajs.5-250-11/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_5 Process_4
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 loc_5 t_5 t_4 loc_4
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Parsing properties file "models/eajs.5-250-11/property.props"...

1 property:
(1) "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

---------------------------------------------------------------------

Model checking: "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.11 seconds (average 0.001507, setup 0.00)

Time for model construction: 0.329 seconds.

Type:        MDP
States:      3049471 (1 initial)
Transitions: 6977654

Transition matrix: 25363 nodes (7 terminal), 6977654 minterms, vars: 43r/43c/5nd

Prob0E: 250 iterations in 0.25 seconds (average 0.001000, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 13476, inf = 0, maybe = 3035995

Computing remaining rewards...
Switching engine since hybrid engine does yet support this computation...
Engine: Sparse

Building sparse matrix (transitions)... [n=3049471, nc=4237377, nnz=6946802, k=10] [107.3 MB]
Building sparse matrix (transition rewards)... [n=3049471, nc=4237377, nnz=105040, k=10] [29.0 MB]
Creating vector for state rewards... [23.3 MB]
Creating vector for inf... [23.3 MB]
Allocating iteration vectors... [2 x 23.3 MB]
TOTAL: [229.4 MB]

Starting iterations...

Iterative method: 128 iterations in 11.59 seconds (average 0.030625, setup 7.67)

Value in the initial state: 10.03294060879421

Time for model checking: 11.907 seconds.

Result: 10.03294060879421 (+/- 7.366896484458609E-5 estimated; rel err 7.342709153487141E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_eajs.5-250-11_rep5.log

```
Command(s):
../bin/prism  models/eajs.5-250-11/model.prism models/eajs.5-250-11/property.props
Wallclock time: 11.845 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:08:07 GMT+01:00 2026
Hostname: n23m0134.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.5-250-11/model.prism models/eajs.5-250-11/property.props

Parsing PRISM model file "models/eajs.5-250-11/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_5 Process_4
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 loc_5 t_5 t_4 loc_4
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Parsing properties file "models/eajs.5-250-11/property.props"...

1 property:
(1) "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

---------------------------------------------------------------------

Model checking: "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.09 seconds (average 0.001233, setup 0.00)

Time for model construction: 0.288 seconds.

Type:        MDP
States:      3049471 (1 initial)
Transitions: 6977654

Transition matrix: 25363 nodes (7 terminal), 6977654 minterms, vars: 43r/43c/5nd

Prob0E: 250 iterations in 0.22 seconds (average 0.000880, setup 0.00)

Prob1A: 1 iterations in 0.01 seconds (average 0.010000, setup 0.00)

goal = 13476, inf = 0, maybe = 3035995

Computing remaining rewards...
Switching engine since hybrid engine does yet support this computation...
Engine: Sparse

Building sparse matrix (transitions)... [n=3049471, nc=4237377, nnz=6946802, k=10] [107.3 MB]
Building sparse matrix (transition rewards)... [n=3049471, nc=4237377, nnz=105040, k=10] [29.0 MB]
Creating vector for state rewards... [23.3 MB]
Creating vector for inf... [23.3 MB]
Allocating iteration vectors... [2 x 23.3 MB]
TOTAL: [229.4 MB]

Starting iterations...

Iterative method: 128 iterations in 10.42 seconds (average 0.028203, setup 6.81)

Value in the initial state: 10.03294060879421

Time for model checking: 10.687 seconds.

Result: 10.03294060879421 (+/- 7.366896484458609E-5 estimated; rel err 7.342709153487141E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

