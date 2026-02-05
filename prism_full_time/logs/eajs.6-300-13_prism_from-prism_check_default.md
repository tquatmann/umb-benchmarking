# Log files for prism_from-prism_check_default on model [eajs.6-300-13](../../models/eajs.6-300-13)

Parsed values: `[37.767, 47.233, 45.844, 37.491, 39.628]`



### Log file: prism_from-prism_check_default_eajs.6-300-13_rep1.log

```
Command(s):
../bin/prism  models/eajs.6-300-13/model.prism models/eajs.6-300-13/property.props
Wallclock time: 37.767 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 08:03:38 GMT+01:00 2026
Hostname: r23m0061.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.6-300-13/model.prism models/eajs.6-300-13/property.props

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Parsing properties file "models/eajs.6-300-13/property.props"...

1 property:
(1) "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

---------------------------------------------------------------------

Model checking: "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 89 iterations in 0.18 seconds (average 0.002022, setup 0.00)

Time for model construction: 0.697 seconds.

Type:        MDP
States:      7901694 (1 initial)
Transitions: 19722777

Transition matrix: 38911 nodes (7 terminal), 19722777 minterms, vars: 50r/50c/5nd

Prob0E: 300 iterations in 0.42 seconds (average 0.001400, setup 0.00)

Prob1A: 1 iterations in 0.01 seconds (average 0.010000, setup 0.00)

goal = 28620, inf = 0, maybe = 7873074

Computing remaining rewards...
Switching engine since hybrid engine does yet support this computation...
Engine: Sparse

Building sparse matrix (transitions)... [n=7901694, nc=11854302, nnz=19651307, k=12] [300.3 MB]
Building sparse matrix (transition rewards)... [n=7901694, nc=11854302, nnz=257760, k=12] [78.3 MB]
Creating vector for state rewards... [60.3 MB]
Creating vector for inf... [60.3 MB]
Allocating iteration vectors... [2 x 60.3 MB]
TOTAL: [619.7 MB]

Starting iterations...
Iteration 63: max relative diff=0.047887, 5.02 sec so far
Iteration 126: max relative diff=0.014911, 10.06 sec so far

Iterative method: 153 iterations in 35.95 seconds (average 0.079804, setup 23.74)

Value in the initial state: 12.05111075489705

Time for model checking: 36.468 seconds.

Result: 12.05111075489705 (+/- 7.207650548638103E-5 estimated; rel err 5.9809014249655175E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_eajs.6-300-13_rep2.log

```
Command(s):
../bin/prism  models/eajs.6-300-13/model.prism models/eajs.6-300-13/property.props
Wallclock time: 47.233 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:13 GMT+01:00 2026
Hostname: n23m0113.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.6-300-13/model.prism models/eajs.6-300-13/property.props

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Parsing properties file "models/eajs.6-300-13/property.props"...

1 property:
(1) "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

---------------------------------------------------------------------

Model checking: "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 89 iterations in 0.17 seconds (average 0.001910, setup 0.00)

Time for model construction: 0.528 seconds.

Type:        MDP
States:      7901694 (1 initial)
Transitions: 19722777

Transition matrix: 38911 nodes (7 terminal), 19722777 minterms, vars: 50r/50c/5nd

Prob0E: 300 iterations in 0.40 seconds (average 0.001333, setup 0.00)

Prob1A: 1 iterations in 0.01 seconds (average 0.010000, setup 0.00)

goal = 28620, inf = 0, maybe = 7873074

Computing remaining rewards...
Switching engine since hybrid engine does yet support this computation...
Engine: Sparse

Building sparse matrix (transitions)... [n=7901694, nc=11854302, nnz=19651307, k=12] [300.3 MB]
Building sparse matrix (transition rewards)... [n=7901694, nc=11854302, nnz=257760, k=12] [78.3 MB]
Creating vector for state rewards... [60.3 MB]
Creating vector for inf... [60.3 MB]
Allocating iteration vectors... [2 x 60.3 MB]
TOTAL: [619.7 MB]

Starting iterations...
Iteration 61: max relative diff=0.047887, 5.06 sec so far
Iteration 121: max relative diff=0.015231, 10.11 sec so far

Iterative method: 153 iterations in 38.23 seconds (average 0.083725, setup 25.42)

Value in the initial state: 12.05111075489705

Time for model checking: 38.757 seconds.

Result: 12.05111075489705 (+/- 7.207650548638103E-5 estimated; rel err 5.9809014249655175E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_eajs.6-300-13_rep3.log

```
Command(s):
../bin/prism  models/eajs.6-300-13/model.prism models/eajs.6-300-13/property.props
Wallclock time: 45.844 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:10:22 GMT+01:00 2026
Hostname: n23m0402.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.6-300-13/model.prism models/eajs.6-300-13/property.props

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Parsing properties file "models/eajs.6-300-13/property.props"...

1 property:
(1) "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

---------------------------------------------------------------------

Model checking: "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 89 iterations in 0.19 seconds (average 0.002135, setup 0.00)

Time for model construction: 0.719 seconds.

Type:        MDP
States:      7901694 (1 initial)
Transitions: 19722777

Transition matrix: 38911 nodes (7 terminal), 19722777 minterms, vars: 50r/50c/5nd

Prob0E: 300 iterations in 0.46 seconds (average 0.001533, setup 0.00)

Prob1A: 1 iterations in 0.01 seconds (average 0.010000, setup 0.00)

goal = 28620, inf = 0, maybe = 7873074

Computing remaining rewards...
Switching engine since hybrid engine does yet support this computation...
Engine: Sparse

Building sparse matrix (transitions)... [n=7901694, nc=11854302, nnz=19651307, k=12] [300.3 MB]
Building sparse matrix (transition rewards)... [n=7901694, nc=11854302, nnz=257760, k=12] [78.3 MB]
Creating vector for state rewards... [60.3 MB]
Creating vector for inf... [60.3 MB]
Allocating iteration vectors... [2 x 60.3 MB]
TOTAL: [619.7 MB]

Starting iterations...
Iteration 56: max relative diff=0.064945, 5.07 sec so far
Iteration 112: max relative diff=0.018029, 10.15 sec so far

Iterative method: 153 iterations in 42.96 seconds (average 0.090850, setup 29.06)

Value in the initial state: 12.05111075489705

Time for model checking: 43.605 seconds.

Result: 12.05111075489705 (+/- 7.207650548638103E-5 estimated; rel err 5.9809014249655175E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_eajs.6-300-13_rep4.log

```
Command(s):
../bin/prism  models/eajs.6-300-13/model.prism models/eajs.6-300-13/property.props
Wallclock time: 37.491 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:04 GMT+01:00 2026
Hostname: r23m0066.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.6-300-13/model.prism models/eajs.6-300-13/property.props

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Parsing properties file "models/eajs.6-300-13/property.props"...

1 property:
(1) "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

---------------------------------------------------------------------

Model checking: "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 89 iterations in 0.18 seconds (average 0.002022, setup 0.00)

Time for model construction: 0.636 seconds.

Type:        MDP
States:      7901694 (1 initial)
Transitions: 19722777

Transition matrix: 38911 nodes (7 terminal), 19722777 minterms, vars: 50r/50c/5nd

Prob0E: 300 iterations in 0.43 seconds (average 0.001433, setup 0.00)

Prob1A: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 28620, inf = 0, maybe = 7873074

Computing remaining rewards...
Switching engine since hybrid engine does yet support this computation...
Engine: Sparse

Building sparse matrix (transitions)... [n=7901694, nc=11854302, nnz=19651307, k=12] [300.3 MB]
Building sparse matrix (transition rewards)... [n=7901694, nc=11854302, nnz=257760, k=12] [78.3 MB]
Creating vector for state rewards... [60.3 MB]
Creating vector for inf... [60.3 MB]
Allocating iteration vectors... [2 x 60.3 MB]
TOTAL: [619.7 MB]

Starting iterations...
Iteration 62: max relative diff=0.047887, 5.01 sec so far
Iteration 124: max relative diff=0.015231, 10.07 sec so far

Iterative method: 153 iterations in 35.41 seconds (average 0.081242, setup 22.98)

Value in the initial state: 12.05111075489705

Time for model checking: 35.934 seconds.

Result: 12.05111075489705 (+/- 7.207650548638103E-5 estimated; rel err 5.9809014249655175E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_eajs.6-300-13_rep5.log

```
Command(s):
../bin/prism  models/eajs.6-300-13/model.prism models/eajs.6-300-13/property.props
Wallclock time: 39.628 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:24:33 GMT+01:00 2026
Hostname: n23m0117.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.6-300-13/model.prism models/eajs.6-300-13/property.props

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Parsing properties file "models/eajs.6-300-13/property.props"...

1 property:
(1) "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

---------------------------------------------------------------------

Model checking: "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 89 iterations in 0.15 seconds (average 0.001685, setup 0.00)

Time for model construction: 0.436 seconds.

Type:        MDP
States:      7901694 (1 initial)
Transitions: 19722777

Transition matrix: 38911 nodes (7 terminal), 19722777 minterms, vars: 50r/50c/5nd

Prob0E: 300 iterations in 0.35 seconds (average 0.001167, setup 0.00)

Prob1A: 1 iterations in 0.01 seconds (average 0.010000, setup 0.00)

goal = 28620, inf = 0, maybe = 7873074

Computing remaining rewards...
Switching engine since hybrid engine does yet support this computation...
Engine: Sparse

Building sparse matrix (transitions)... [n=7901694, nc=11854302, nnz=19651307, k=12] [300.3 MB]
Building sparse matrix (transition rewards)... [n=7901694, nc=11854302, nnz=257760, k=12] [78.3 MB]
Creating vector for state rewards... [60.3 MB]
Creating vector for inf... [60.3 MB]
Allocating iteration vectors... [2 x 60.3 MB]
TOTAL: [619.7 MB]

Starting iterations...
Iteration 51: max relative diff=0.069067, 5.08 sec so far
Iteration 102: max relative diff=0.020987, 10.13 sec so far
Iteration 153: max relative diff=0.000001, 15.18 sec so far

Iterative method: 153 iterations in 38.07 seconds (average 0.099216, setup 22.89)

Value in the initial state: 12.05111075489705

Time for model checking: 38.537 seconds.

Result: 12.05111075489705 (+/- 7.207650548638103E-5 estimated; rel err 5.9809014249655175E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

