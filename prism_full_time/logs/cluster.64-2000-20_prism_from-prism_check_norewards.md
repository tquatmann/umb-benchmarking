# Log files for prism_from-prism_check_norewards on model [cluster.64-2000-20](../../models/cluster.64-2000-20)

Parsed values: `[77.028, 76.66, 86.538, 76.44, 89.776]`



### Log file: prism_from-prism_check_norewards_cluster.64-2000-20_rep1.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props
Wallclock time: 77.028 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 08:04:09 GMT+01:00 2026
Hostname: r23m0197.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Parsing properties file "models/cluster.64-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.02 seconds (average 0.000150, setup 0.00)

Time for model construction: 0.045 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 36133 of 151060 (23.9%)

Building hybrid MTBDD matrix... [levels=23, nodes=16782] [786.7 KB]
Adding explicit sparse matrices... [levels=16, num=164, compact] [838.5 KB]
Creating vector for diagonals... [dist=1298, compact] [305.2 KB]
Allocating iteration vectors... [3 x 1.2 MB]
TOTAL: [5.3 MB]

Uniformisation: q.t = 41.057295 x 2000.000000 = 82114.590000
Fox-Glynn: left = 80105, right = 84548

Starting iterations...
Iteration 5599 (of 84548): max relative diff=0.000184, 5.01 sec so far
Iteration 11208 (of 84548): max relative diff=0.000091, 10.02 sec so far
Iteration 16812 (of 84548): max relative diff=0.000060, 15.03 sec so far
Iteration 22414 (of 84548): max relative diff=0.000045, 20.04 sec so far
Iteration 28020 (of 84548): max relative diff=0.000036, 25.05 sec so far
Iteration 33625 (of 84548): max relative diff=0.000030, 30.06 sec so far
Iteration 39227 (of 84548): max relative diff=0.000026, 35.07 sec so far
Iteration 44844 (of 84548): max relative diff=0.000022, 40.08 sec so far
Iteration 50449 (of 84548): max relative diff=0.000020, 45.09 sec so far
Iteration 56035 (of 84548): max relative diff=0.000018, 50.10 sec so far
Iteration 61617 (of 84548): max relative diff=0.000016, 55.11 sec so far
Iteration 67186 (of 84548): max relative diff=0.000015, 60.12 sec so far
Iteration 72787 (of 84548): max relative diff=0.000014, 65.13 sec so far
Iteration 78407 (of 84548): max relative diff=0.000013, 70.14 sec so far
Iteration 83763 (of 84548): max relative diff=0.000012, 75.15 sec so far

Iterative method: 84548 iterations in 75.95 seconds (average 0.000898, setup 0.06)

Value in the initial state: 0.0010445396729789396

Time for model checking: 76.121 seconds.

Result: 0.0010445396729789396


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_cluster.64-2000-20_rep2.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props
Wallclock time: 76.660 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:07:24 GMT+01:00 2026
Hostname: n23m0212.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Parsing properties file "models/cluster.64-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.01 seconds (average 0.000075, setup 0.00)

Time for model construction: 0.04 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 36133 of 151060 (23.9%)

Building hybrid MTBDD matrix... [levels=23, nodes=16782] [786.7 KB]
Adding explicit sparse matrices... [levels=16, num=164, compact] [838.5 KB]
Creating vector for diagonals... [dist=1298, compact] [305.2 KB]
Allocating iteration vectors... [3 x 1.2 MB]
TOTAL: [5.3 MB]

Uniformisation: q.t = 41.057295 x 2000.000000 = 82114.590000
Fox-Glynn: left = 80105, right = 84548

Starting iterations...
Iteration 5572 (of 84548): max relative diff=0.000185, 5.01 sec so far
Iteration 11165 (of 84548): max relative diff=0.000091, 10.02 sec so far
Iteration 16762 (of 84548): max relative diff=0.000060, 15.03 sec so far
Iteration 22361 (of 84548): max relative diff=0.000045, 20.04 sec so far
Iteration 27963 (of 84548): max relative diff=0.000036, 25.05 sec so far
Iteration 33551 (of 84548): max relative diff=0.000030, 30.06 sec so far
Iteration 39147 (of 84548): max relative diff=0.000026, 35.07 sec so far
Iteration 44645 (of 84548): max relative diff=0.000022, 40.08 sec so far
Iteration 50252 (of 84548): max relative diff=0.000020, 45.09 sec so far
Iteration 55878 (of 84548): max relative diff=0.000018, 50.10 sec so far
Iteration 61517 (of 84548): max relative diff=0.000016, 55.11 sec so far
Iteration 67156 (of 84548): max relative diff=0.000015, 60.12 sec so far
Iteration 72804 (of 84548): max relative diff=0.000014, 65.13 sec so far
Iteration 78449 (of 84548): max relative diff=0.000013, 70.14 sec so far
Iteration 83827 (of 84548): max relative diff=0.000012, 75.15 sec so far

Iterative method: 84548 iterations in 75.90 seconds (average 0.000897, setup 0.07)

Value in the initial state: 0.0010445396729789396

Time for model checking: 76.076 seconds.

Result: 0.0010445396729789396


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_cluster.64-2000-20_rep3.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props
Wallclock time: 86.538 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:03 GMT+01:00 2026
Hostname: n23m0003.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Parsing properties file "models/cluster.64-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.03 seconds (average 0.000226, setup 0.00)

Time for model construction: 0.061 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 36133 of 151060 (23.9%)

Building hybrid MTBDD matrix... [levels=23, nodes=16782] [786.7 KB]
Adding explicit sparse matrices... [levels=16, num=164, compact] [838.5 KB]
Creating vector for diagonals... [dist=1298, compact] [305.2 KB]
Allocating iteration vectors... [3 x 1.2 MB]
TOTAL: [5.3 MB]

Uniformisation: q.t = 41.057295 x 2000.000000 = 82114.590000
Fox-Glynn: left = 80105, right = 84548

Starting iterations...
Iteration 4831 (of 84548): max relative diff=0.000214, 5.01 sec so far
Iteration 9659 (of 84548): max relative diff=0.000105, 10.02 sec so far
Iteration 14504 (of 84548): max relative diff=0.000070, 15.03 sec so far
Iteration 19339 (of 84548): max relative diff=0.000052, 20.04 sec so far
Iteration 24447 (of 84548): max relative diff=0.000041, 25.05 sec so far
Iteration 29443 (of 84548): max relative diff=0.000034, 30.06 sec so far
Iteration 34440 (of 84548): max relative diff=0.000029, 35.07 sec so far
Iteration 39674 (of 84548): max relative diff=0.000025, 40.08 sec so far
Iteration 44628 (of 84548): max relative diff=0.000022, 45.09 sec so far
Iteration 49612 (of 84548): max relative diff=0.000020, 50.10 sec so far
Iteration 54568 (of 84548): max relative diff=0.000018, 55.11 sec so far
Iteration 59448 (of 84548): max relative diff=0.000017, 60.12 sec so far
Iteration 64429 (of 84548): max relative diff=0.000016, 65.13 sec so far
Iteration 69470 (of 84548): max relative diff=0.000014, 70.14 sec so far
Iteration 74504 (of 84548): max relative diff=0.000013, 75.15 sec so far
Iteration 79525 (of 84548): max relative diff=0.000013, 80.16 sec so far
Iteration 84263 (of 84548): max relative diff=0.000012, 85.17 sec so far

Iterative method: 84548 iterations in 85.55 seconds (average 0.001011, setup 0.07)

Value in the initial state: 0.0010445396729789396

Time for model checking: 85.862 seconds.

Result: 0.0010445396729789396


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_cluster.64-2000-20_rep4.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props
Wallclock time: 76.440 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:10:51 GMT+01:00 2026
Hostname: r23m0203.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Parsing properties file "models/cluster.64-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.02 seconds (average 0.000150, setup 0.00)

Time for model construction: 0.042 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 36133 of 151060 (23.9%)

Building hybrid MTBDD matrix... [levels=23, nodes=16782] [786.7 KB]
Adding explicit sparse matrices... [levels=16, num=164, compact] [838.5 KB]
Creating vector for diagonals... [dist=1298, compact] [305.2 KB]
Allocating iteration vectors... [3 x 1.2 MB]
TOTAL: [5.3 MB]

Uniformisation: q.t = 41.057295 x 2000.000000 = 82114.590000
Fox-Glynn: left = 80105, right = 84548

Starting iterations...
Iteration 5644 (of 84548): max relative diff=0.000183, 5.01 sec so far
Iteration 11193 (of 84548): max relative diff=0.000091, 10.02 sec so far
Iteration 16820 (of 84548): max relative diff=0.000060, 15.03 sec so far
Iteration 22427 (of 84548): max relative diff=0.000045, 20.04 sec so far
Iteration 28091 (of 84548): max relative diff=0.000036, 25.05 sec so far
Iteration 33711 (of 84548): max relative diff=0.000030, 30.06 sec so far
Iteration 39342 (of 84548): max relative diff=0.000026, 35.07 sec so far
Iteration 44994 (of 84548): max relative diff=0.000022, 40.08 sec so far
Iteration 50654 (of 84548): max relative diff=0.000020, 45.09 sec so far
Iteration 56290 (of 84548): max relative diff=0.000018, 50.10 sec so far
Iteration 61950 (of 84548): max relative diff=0.000016, 55.11 sec so far
Iteration 67567 (of 84548): max relative diff=0.000015, 60.12 sec so far
Iteration 73163 (of 84548): max relative diff=0.000014, 65.13 sec so far
Iteration 78671 (of 84548): max relative diff=0.000013, 70.14 sec so far
Iteration 84040 (of 84548): max relative diff=0.000012, 75.15 sec so far

Iterative method: 84548 iterations in 75.68 seconds (average 0.000895, setup 0.05)

Value in the initial state: 0.0010445396729789396

Time for model checking: 75.866 seconds.

Result: 0.0010445396729789396


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_cluster.64-2000-20_rep5.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props
Wallclock time: 89.776 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 02:58:58 GMT+01:00 2026
Hostname: n23m0181.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Parsing properties file "models/cluster.64-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.04 seconds (average 0.000301, setup 0.00)

Time for model construction: 0.053 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 36133 of 151060 (23.9%)

Building hybrid MTBDD matrix... [levels=23, nodes=16782] [786.7 KB]
Adding explicit sparse matrices... [levels=16, num=164, compact] [838.5 KB]
Creating vector for diagonals... [dist=1298, compact] [305.2 KB]
Allocating iteration vectors... [3 x 1.2 MB]
TOTAL: [5.3 MB]

Uniformisation: q.t = 41.057295 x 2000.000000 = 82114.590000
Fox-Glynn: left = 80105, right = 84548

Starting iterations...
Iteration 4745 (of 84548): max relative diff=0.000219, 5.01 sec so far
Iteration 9553 (of 84548): max relative diff=0.000107, 10.02 sec so far
Iteration 14347 (of 84548): max relative diff=0.000071, 15.03 sec so far
Iteration 19142 (of 84548): max relative diff=0.000053, 20.04 sec so far
Iteration 23940 (of 84548): max relative diff=0.000042, 25.05 sec so far
Iteration 28705 (of 84548): max relative diff=0.000035, 30.06 sec so far
Iteration 33517 (of 84548): max relative diff=0.000030, 35.07 sec so far
Iteration 38335 (of 84548): max relative diff=0.000026, 40.08 sec so far
Iteration 43141 (of 84548): max relative diff=0.000023, 45.09 sec so far
Iteration 47933 (of 84548): max relative diff=0.000021, 50.10 sec so far
Iteration 52747 (of 84548): max relative diff=0.000019, 55.11 sec so far
Iteration 57550 (of 84548): max relative diff=0.000017, 60.12 sec so far
Iteration 62298 (of 84548): max relative diff=0.000016, 65.13 sec so far
Iteration 67091 (of 84548): max relative diff=0.000015, 70.14 sec so far
Iteration 71887 (of 84548): max relative diff=0.000014, 75.15 sec so far
Iteration 76702 (of 84548): max relative diff=0.000013, 80.16 sec so far
Iteration 81409 (of 84548): max relative diff=0.000012, 85.17 sec so far

Iterative method: 84548 iterations in 88.78 seconds (average 0.001049, setup 0.07)

Value in the initial state: 0.0010445396729789396

Time for model checking: 89.08 seconds.

Result: 0.0010445396729789396


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

