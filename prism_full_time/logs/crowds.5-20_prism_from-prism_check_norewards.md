# Log files for prism_from-prism_check_norewards on model [crowds.5-20](../../models/crowds.5-20)

Parsed values: `[4.037, 5.374, 4.387, 4.104, 4.991]`



### Log file: prism_from-prism_check_norewards_crowds.5-20_rep1.log

```
Command(s):
../bin/prism  models/crowds.5-20/model.prism models/crowds.5-20/property.props
Wallclock time: 4.037 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:46:20 GMT+01:00 2026
Hostname: r23m0077.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.5-20/model.prism models/crowds.5-20/property.props

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Parsing properties file "models/crowds.5-20/property.props"...

1 property:
(1) "positive": P=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "positive": P=? [ F "target" ]

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 47 iterations in 0.09 seconds (average 0.001915, setup 0.00)

Time for model construction: 0.169 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 33232 nodes (7 terminal), 7374951 minterms, vars: 78r/78c

Prob0: 14 iterations in 0.03 seconds (average 0.002143, setup 0.00)

Prob1: 30 iterations in 0.06 seconds (average 0.002000, setup 0.00)

yes = 47399, no = 1745849, maybe = 268703

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=78, nodes=31625] [1.4 MB]
Adding explicit sparse matrices... [levels=64, num=350, compact] [605.9 KB]
Creating vector for diagonals... [dist=1, compact] [3.9 MB]
Creating vector for RHS... [dist=2, compact] [3.9 MB]
Allocating iteration vectors... [2 x 15.7 MB]
TOTAL: [41.4 MB]

Starting iterations...

Jacobi: 187 iterations in 3.19 seconds (average 0.015294, setup 0.33)

Value in the initial state: 0.08606841127862043

Time for model checking: 3.299 seconds.

Result: 0.08606841127862043 (+/- 7.183528306181446E-7 estimated; rel err 8.34630057586046E-6)

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_crowds.5-20_rep2.log

```
Command(s):
../bin/prism  models/crowds.5-20/model.prism models/crowds.5-20/property.props
Wallclock time: 5.374 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:20:02 GMT+01:00 2026
Hostname: n23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.5-20/model.prism models/crowds.5-20/property.props

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Parsing properties file "models/crowds.5-20/property.props"...

1 property:
(1) "positive": P=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "positive": P=? [ F "target" ]

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 47 iterations in 0.16 seconds (average 0.003404, setup 0.00)

Time for model construction: 0.32 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 33232 nodes (7 terminal), 7374951 minterms, vars: 78r/78c

Prob0: 14 iterations in 0.04 seconds (average 0.002857, setup 0.00)

Prob1: 30 iterations in 0.08 seconds (average 0.002667, setup 0.00)

yes = 47399, no = 1745849, maybe = 268703

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=78, nodes=31625] [1.4 MB]
Adding explicit sparse matrices... [levels=64, num=350, compact] [605.9 KB]
Creating vector for diagonals... [dist=1, compact] [3.9 MB]
Creating vector for RHS... [dist=2, compact] [3.9 MB]
Allocating iteration vectors... [2 x 15.7 MB]
TOTAL: [41.4 MB]

Starting iterations...

Jacobi: 187 iterations in 4.14 seconds (average 0.020000, setup 0.40)

Value in the initial state: 0.08606841127862043

Time for model checking: 4.319 seconds.

Result: 0.08606841127862043 (+/- 7.183528306181446E-7 estimated; rel err 8.34630057586046E-6)

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_crowds.5-20_rep3.log

```
Command(s):
../bin/prism  models/crowds.5-20/model.prism models/crowds.5-20/property.props
Wallclock time: 4.387 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:24:22 GMT+01:00 2026
Hostname: n23m0355.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.5-20/model.prism models/crowds.5-20/property.props

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Parsing properties file "models/crowds.5-20/property.props"...

1 property:
(1) "positive": P=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "positive": P=? [ F "target" ]

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 47 iterations in 0.09 seconds (average 0.001915, setup 0.00)

Time for model construction: 0.183 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 33232 nodes (7 terminal), 7374951 minterms, vars: 78r/78c

Prob0: 14 iterations in 0.03 seconds (average 0.002143, setup 0.00)

Prob1: 30 iterations in 0.06 seconds (average 0.002000, setup 0.00)

yes = 47399, no = 1745849, maybe = 268703

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=78, nodes=31625] [1.4 MB]
Adding explicit sparse matrices... [levels=64, num=350, compact] [605.9 KB]
Creating vector for diagonals... [dist=1, compact] [3.9 MB]
Creating vector for RHS... [dist=2, compact] [3.9 MB]
Allocating iteration vectors... [2 x 15.7 MB]
TOTAL: [41.4 MB]

Starting iterations...

Jacobi: 187 iterations in 3.12 seconds (average 0.014920, setup 0.33)

Value in the initial state: 0.08606841127862043

Time for model checking: 3.236 seconds.

Result: 0.08606841127862043 (+/- 7.183528306181446E-7 estimated; rel err 8.34630057586046E-6)

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_crowds.5-20_rep4.log

```
Command(s):
../bin/prism  models/crowds.5-20/model.prism models/crowds.5-20/property.props
Wallclock time: 4.104 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:13:48 GMT+01:00 2026
Hostname: n23m0386.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.5-20/model.prism models/crowds.5-20/property.props

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Parsing properties file "models/crowds.5-20/property.props"...

1 property:
(1) "positive": P=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "positive": P=? [ F "target" ]

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 47 iterations in 0.10 seconds (average 0.002128, setup 0.00)

Time for model construction: 0.193 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 33232 nodes (7 terminal), 7374951 minterms, vars: 78r/78c

Prob0: 14 iterations in 0.03 seconds (average 0.002143, setup 0.00)

Prob1: 30 iterations in 0.06 seconds (average 0.002000, setup 0.00)

yes = 47399, no = 1745849, maybe = 268703

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=78, nodes=31625] [1.4 MB]
Adding explicit sparse matrices... [levels=64, num=350, compact] [605.9 KB]
Creating vector for diagonals... [dist=1, compact] [3.9 MB]
Creating vector for RHS... [dist=2, compact] [3.9 MB]
Allocating iteration vectors... [2 x 15.7 MB]
TOTAL: [41.4 MB]

Starting iterations...

Jacobi: 187 iterations in 3.23 seconds (average 0.015455, setup 0.34)

Value in the initial state: 0.08606841127862043

Time for model checking: 3.351 seconds.

Result: 0.08606841127862043 (+/- 7.183528306181446E-7 estimated; rel err 8.34630057586046E-6)

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_crowds.5-20_rep5.log

```
Command(s):
../bin/prism  models/crowds.5-20/model.prism models/crowds.5-20/property.props
Wallclock time: 4.991 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:01 GMT+01:00 2026
Hostname: n23m0167.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.5-20/model.prism models/crowds.5-20/property.props

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Parsing properties file "models/crowds.5-20/property.props"...

1 property:
(1) "positive": P=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "positive": P=? [ F "target" ]

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 47 iterations in 0.09 seconds (average 0.001915, setup 0.00)

Time for model construction: 0.191 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 33232 nodes (7 terminal), 7374951 minterms, vars: 78r/78c

Prob0: 14 iterations in 0.03 seconds (average 0.002143, setup 0.00)

Prob1: 30 iterations in 0.06 seconds (average 0.002000, setup 0.00)

yes = 47399, no = 1745849, maybe = 268703

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=78, nodes=31625] [1.4 MB]
Adding explicit sparse matrices... [levels=64, num=350, compact] [605.9 KB]
Creating vector for diagonals... [dist=1, compact] [3.9 MB]
Creating vector for RHS... [dist=2, compact] [3.9 MB]
Allocating iteration vectors... [2 x 15.7 MB]
TOTAL: [41.4 MB]

Starting iterations...

Jacobi: 187 iterations in 3.77 seconds (average 0.018021, setup 0.40)

Value in the initial state: 0.08606841127862043

Time for model checking: 3.905 seconds.

Result: 0.08606841127862043 (+/- 7.183528306181446E-7 estimated; rel err 8.34630057586046E-6)

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

