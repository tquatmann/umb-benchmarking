# Log files

Tool configuration: prism_from-prism_check_norewards
Benchmark: [mapk-cascade.4-30](../../models/mapk-cascade.4-30)
Parsed values: [1.828, 3.375, 2.819, 2.22, 2.184]



### Log file: prism_from-prism_check_norewards_mapk-cascade.4-30_rep1.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism models/mapk-cascade.4-30/property.props
Wallclock time: 283.407 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:56:42 GMT+01:00 2026
Hostname: r23m0072.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism models/mapk-cascade.4-30/property.props

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Parsing properties file "models/mapk-cascade.4-30/property.props"...

1 property:
(1) "activated_time": R{"time"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "activated_time": R{"time"}=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 1.71 seconds (average 0.038864, setup 0.00)

Time for model construction: 1.828 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Diagonals vector: 52485 nodes (128 terminal), 99535 minterms
Embedded Markov chain: 929797 nodes (681 terminal), 910872 minterms

Prob0: 23 iterations in 0.20 seconds (average 0.008696, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 1461, inf = 0, maybe = 98074

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=58, nodes=912853] [41.8 MB]
Adding explicit sparse matrices... [levels=24, num=25482, compact] [902.2 KB]
Creating vector for diagonals... [dist=1, compact] [194.4 KB]
Creating vector for RHS... [dist=128, compact] [195.4 KB]
Allocating iteration vectors... [2 x 777.6 KB]
TOTAL: [44.6 MB]

Starting iterations...
Iteration 468: max relative diff=0.001229, 5.01 sec so far
Iteration 939: max relative diff=0.000106, 10.02 sec so far
Iteration 1409: max relative diff=0.000010, 15.03 sec so far

Jacobi: 1875 iterations in 279.32 seconds (average 0.010651, setup 259.35)

Value in the initial state: 40.67270371188303

Time for model checking: 280.962 seconds.

Result: 40.67270371188303 (+/- 4.0451335066928187E-4 estimated; rel err 9.945573167074662E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_mapk-cascade.4-30_rep2.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism models/mapk-cascade.4-30/property.props
Wallclock time: 815.349 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:01:58 GMT+01:00 2026
Hostname: n23m0096.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism models/mapk-cascade.4-30/property.props

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Parsing properties file "models/mapk-cascade.4-30/property.props"...

1 property:
(1) "activated_time": R{"time"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "activated_time": R{"time"}=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 3.17 seconds (average 0.072045, setup 0.00)

Time for model construction: 3.375 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Diagonals vector: 52485 nodes (128 terminal), 99535 minterms
Embedded Markov chain: 929797 nodes (681 terminal), 910872 minterms

Prob0: 23 iterations in 0.35 seconds (average 0.015217, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 1461, inf = 0, maybe = 98074

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=58, nodes=912853] [41.8 MB]
Adding explicit sparse matrices... [levels=24, num=25482, compact] [902.2 KB]
Creating vector for diagonals... [dist=1, compact] [194.4 KB]
Creating vector for RHS... [dist=128, compact] [195.4 KB]
Allocating iteration vectors... [2 x 777.6 KB]
TOTAL: [44.6 MB]

Starting iterations...
Iteration 280: max relative diff=0.003897, 5.01 sec so far
Iteration 574: max relative diff=0.000690, 10.02 sec so far
Iteration 845: max relative diff=0.000170, 15.04 sec so far
Iteration 1135: max relative diff=0.000040, 20.05 sec so far
Iteration 1429: max relative diff=0.000009, 25.06 sec so far
Iteration 1698: max relative diff=0.000002, 30.07 sec so far

Jacobi: 1875 iterations in 806.93 seconds (average 0.017659, setup 773.82)

Value in the initial state: 40.67270371188303

Time for model checking: 811.2 seconds.

Result: 40.67270371188303 (+/- 4.0451335066928187E-4 estimated; rel err 9.945573167074662E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_mapk-cascade.4-30_rep3.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism models/mapk-cascade.4-30/property.props
Wallclock time: 731.314 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:36:32 GMT+01:00 2026
Hostname: n23m0241.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism models/mapk-cascade.4-30/property.props

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Parsing properties file "models/mapk-cascade.4-30/property.props"...

1 property:
(1) "activated_time": R{"time"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "activated_time": R{"time"}=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 2.62 seconds (average 0.059545, setup 0.00)

Time for model construction: 2.819 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Diagonals vector: 52485 nodes (128 terminal), 99535 minterms
Embedded Markov chain: 929797 nodes (681 terminal), 910872 minterms

Prob0: 23 iterations in 0.31 seconds (average 0.013478, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 1461, inf = 0, maybe = 98074

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=58, nodes=912853] [41.8 MB]
Adding explicit sparse matrices... [levels=24, num=25482, compact] [902.2 KB]
Creating vector for diagonals... [dist=1, compact] [194.4 KB]
Creating vector for RHS... [dist=128, compact] [195.4 KB]
Allocating iteration vectors... [2 x 777.6 KB]
TOTAL: [44.6 MB]

Starting iterations...
Iteration 301: max relative diff=0.003369, 5.02 sec so far
Iteration 603: max relative diff=0.000591, 10.04 sec so far
Iteration 905: max relative diff=0.000126, 15.05 sec so far
Iteration 1206: max relative diff=0.000028, 20.06 sec so far
Iteration 1507: max relative diff=0.000006, 25.07 sec so far
Iteration 1808: max relative diff=0.000001, 30.08 sec so far

Jacobi: 1875 iterations in 722.66 seconds (average 0.016635, setup 691.47)

Value in the initial state: 40.67270371188303

Time for model checking: 726.224 seconds.

Result: 40.67270371188303 (+/- 4.0451335066928187E-4 estimated; rel err 9.945573167074662E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_mapk-cascade.4-30_rep4.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism models/mapk-cascade.4-30/property.props
Wallclock time: 296.620 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:09 GMT+01:00 2026
Hostname: r23m0155.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism models/mapk-cascade.4-30/property.props

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Parsing properties file "models/mapk-cascade.4-30/property.props"...

1 property:
(1) "activated_time": R{"time"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "activated_time": R{"time"}=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 2.07 seconds (average 0.047045, setup 0.00)

Time for model construction: 2.22 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Diagonals vector: 52485 nodes (128 terminal), 99535 minterms
Embedded Markov chain: 929797 nodes (681 terminal), 910872 minterms

Prob0: 23 iterations in 0.23 seconds (average 0.010000, setup 0.00)

Prob1: 1 iterations in 0.01 seconds (average 0.010000, setup 0.00)

goal = 1461, inf = 0, maybe = 98074

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=58, nodes=912853] [41.8 MB]
Adding explicit sparse matrices... [levels=24, num=25482, compact] [902.2 KB]
Creating vector for diagonals... [dist=1, compact] [194.4 KB]
Creating vector for RHS... [dist=128, compact] [195.4 KB]
Allocating iteration vectors... [2 x 777.6 KB]
TOTAL: [44.6 MB]

Starting iterations...
Iteration 464: max relative diff=0.001257, 5.02 sec so far
Iteration 928: max relative diff=0.000112, 10.03 sec so far
Iteration 1392: max relative diff=0.000011, 15.04 sec so far
Iteration 1854: max relative diff=0.000001, 20.05 sec so far

Jacobi: 1875 iterations in 288.39 seconds (average 0.010816, setup 268.11)

Value in the initial state: 40.67270371188303

Time for model checking: 290.024 seconds.

Result: 40.67270371188303 (+/- 4.0451335066928187E-4 estimated; rel err 9.945573167074662E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_mapk-cascade.4-30_rep5.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism models/mapk-cascade.4-30/property.props
Wallclock time: 419.378 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:07:49 GMT+01:00 2026
Hostname: n23m0392.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism models/mapk-cascade.4-30/property.props

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Parsing properties file "models/mapk-cascade.4-30/property.props"...

1 property:
(1) "activated_time": R{"time"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "activated_time": R{"time"}=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 1.87 seconds (average 0.042500, setup 0.00)

Time for model construction: 2.184 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Diagonals vector: 52485 nodes (128 terminal), 99535 minterms
Embedded Markov chain: 929797 nodes (681 terminal), 910872 minterms

Prob0: 23 iterations in 0.21 seconds (average 0.009130, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 1461, inf = 0, maybe = 98074

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=58, nodes=912853] [41.8 MB]
Adding explicit sparse matrices... [levels=24, num=25482, compact] [902.2 KB]
Creating vector for diagonals... [dist=1, compact] [194.4 KB]
Creating vector for RHS... [dist=128, compact] [195.4 KB]
Allocating iteration vectors... [2 x 777.6 KB]
TOTAL: [44.6 MB]

Starting iterations...
Iteration 370: max relative diff=0.002174, 5.01 sec so far
Iteration 747: max relative diff=0.000280, 10.02 sec so far
Iteration 1125: max relative diff=0.000042, 15.04 sec so far
Iteration 1502: max relative diff=0.000006, 20.05 sec so far

Jacobi: 1875 iterations in 413.42 seconds (average 0.013339, setup 388.41)

Value in the initial state: 40.67270371188303

Time for model checking: 415.97 seconds.

Result: 40.67270371188303 (+/- 4.0451335066928187E-4 estimated; rel err 9.945573167074662E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

