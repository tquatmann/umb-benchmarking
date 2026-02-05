# Log files for prism_from-prism_check_norewards on model [eajs.5-250-11](../../models/eajs.5-250-11)

Parsed values: `[14.304, 11.749, 14.445, 12.588, 12.811]`



### Log file: prism_from-prism_check_norewards_eajs.5-250-11_rep1.log

```
Command(s):
../bin/prism  models/eajs.5-250-11/model.prism models/eajs.5-250-11/property.props
Wallclock time: 14.304 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 08:03:08 GMT+01:00 2026
Hostname: r23m0015.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 73 iterations in 0.14 seconds (average 0.001918, setup 0.00)

Time for model construction: 0.564 seconds.

Type:        MDP
States:      3049471 (1 initial)
Transitions: 6977654

Transition matrix: 25363 nodes (7 terminal), 6977654 minterms, vars: 43r/43c/5nd

Prob0E: 250 iterations in 0.30 seconds (average 0.001200, setup 0.00)

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

Iterative method: 128 iterations in 12.61 seconds (average 0.036172, setup 7.98)

Value in the initial state: 10.03294060879421

Time for model checking: 12.944 seconds.

Result: 10.03294060879421 (+/- 7.366896484458609E-5 estimated; rel err 7.342709153487141E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_eajs.5-250-11_rep2.log

```
Command(s):
../bin/prism  models/eajs.5-250-11/model.prism models/eajs.5-250-11/property.props
Wallclock time: 11.749 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:53:29 GMT+01:00 2026
Hostname: n23m0249.hpc.itc.rwth-aachen.de
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

Time for model construction: 0.287 seconds.

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

Iterative method: 128 iterations in 10.45 seconds (average 0.028047, setup 6.86)

Value in the initial state: 10.03294060879421

Time for model checking: 10.731 seconds.

Result: 10.03294060879421 (+/- 7.366896484458609E-5 estimated; rel err 7.342709153487141E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_eajs.5-250-11_rep3.log

```
Command(s):
../bin/prism  models/eajs.5-250-11/model.prism models/eajs.5-250-11/property.props
Wallclock time: 14.445 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 02:51:45 GMT+01:00 2026
Hostname: r23m0016.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 73 iterations in 0.12 seconds (average 0.001644, setup 0.00)

Time for model construction: 0.709 seconds.

Type:        MDP
States:      3049471 (1 initial)
Transitions: 6977654

Transition matrix: 25363 nodes (7 terminal), 6977654 minterms, vars: 43r/43c/5nd

Prob0E: 250 iterations in 0.33 seconds (average 0.001320, setup 0.00)

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

Iterative method: 128 iterations in 12.47 seconds (average 0.035156, setup 7.97)

Value in the initial state: 10.03294060879421

Time for model checking: 12.891 seconds.

Result: 10.03294060879421 (+/- 7.366896484458609E-5 estimated; rel err 7.342709153487141E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_eajs.5-250-11_rep4.log

```
Command(s):
../bin/prism  models/eajs.5-250-11/model.prism models/eajs.5-250-11/property.props
Wallclock time: 12.588 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:07:18 GMT+01:00 2026
Hostname: n23m0021.hpc.itc.rwth-aachen.de
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

Time for model construction: 0.425 seconds.

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

Iterative method: 128 iterations in 10.74 seconds (average 0.031094, setup 6.76)

Value in the initial state: 10.03294060879421

Time for model checking: 11.033 seconds.

Result: 10.03294060879421 (+/- 7.366896484458609E-5 estimated; rel err 7.342709153487141E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_eajs.5-250-11_rep5.log

```
Command(s):
../bin/prism  models/eajs.5-250-11/model.prism models/eajs.5-250-11/property.props
Wallclock time: 12.811 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:28:43 GMT+01:00 2026
Hostname: n23m0252.hpc.itc.rwth-aachen.de
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

Time for model construction: 0.296 seconds.

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

Iterative method: 128 iterations in 11.50 seconds (average 0.030078, setup 7.65)

Value in the initial state: 10.03294060879421

Time for model checking: 11.786 seconds.

Result: 10.03294060879421 (+/- 7.366896484458609E-5 estimated; rel err 7.342709153487141E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

