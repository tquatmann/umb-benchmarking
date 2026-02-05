# Log files for prism_from-prism_check_default on model [cluster.64-2000-20](../../models/cluster.64-2000-20)

Parsed values: `[77.882, 76.401, 83.262, 78.94, 76.769]`



### Log file: prism_from-prism_check_default_cluster.64-2000-20_rep1.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props
Wallclock time: 77.882 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 08:01:05 GMT+01:00 2026
Hostname: r23m0141.hpc.itc.rwth-aachen.de
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

Time for model construction: 0.044 seconds.

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
Iteration 5476 (of 84548): max relative diff=0.000188, 5.01 sec so far
Iteration 11032 (of 84548): max relative diff=0.000092, 10.02 sec so far
Iteration 16571 (of 84548): max relative diff=0.000061, 15.03 sec so far
Iteration 22092 (of 84548): max relative diff=0.000046, 20.04 sec so far
Iteration 27645 (of 84548): max relative diff=0.000036, 25.05 sec so far
Iteration 33168 (of 84548): max relative diff=0.000030, 30.06 sec so far
Iteration 38718 (of 84548): max relative diff=0.000026, 35.07 sec so far
Iteration 44276 (of 84548): max relative diff=0.000023, 40.08 sec so far
Iteration 49814 (of 84548): max relative diff=0.000020, 45.09 sec so far
Iteration 55356 (of 84548): max relative diff=0.000018, 50.10 sec so far
Iteration 60814 (of 84548): max relative diff=0.000016, 55.11 sec so far
Iteration 66193 (of 84548): max relative diff=0.000015, 60.12 sec so far
Iteration 71699 (of 84548): max relative diff=0.000014, 65.13 sec so far
Iteration 77238 (of 84548): max relative diff=0.000013, 70.14 sec so far
Iteration 82606 (of 84548): max relative diff=0.000012, 75.15 sec so far

Iterative method: 84548 iterations in 77.08 seconds (average 0.000911, setup 0.06)

Value in the initial state: 0.0010445396729789396

Time for model checking: 77.271 seconds.

Result: 0.0010445396729789396


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_cluster.64-2000-20_rep2.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props
Wallclock time: 76.401 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:10:44 GMT+01:00 2026
Hostname: n23m0333.hpc.itc.rwth-aachen.de
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

Time for model construction: 0.039 seconds.

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
Iteration 5608 (of 84548): max relative diff=0.000184, 5.01 sec so far
Iteration 11232 (of 84548): max relative diff=0.000090, 10.02 sec so far
Iteration 16854 (of 84548): max relative diff=0.000060, 15.03 sec so far
Iteration 22484 (of 84548): max relative diff=0.000045, 20.04 sec so far
Iteration 28076 (of 84548): max relative diff=0.000036, 25.05 sec so far
Iteration 33683 (of 84548): max relative diff=0.000030, 30.06 sec so far
Iteration 39323 (of 84548): max relative diff=0.000026, 35.07 sec so far
Iteration 44952 (of 84548): max relative diff=0.000022, 40.08 sec so far
Iteration 50578 (of 84548): max relative diff=0.000020, 45.09 sec so far
Iteration 56204 (of 84548): max relative diff=0.000018, 50.10 sec so far
Iteration 61847 (of 84548): max relative diff=0.000016, 55.11 sec so far
Iteration 67463 (of 84548): max relative diff=0.000015, 60.12 sec so far
Iteration 73096 (of 84548): max relative diff=0.000014, 65.13 sec so far
Iteration 78715 (of 84548): max relative diff=0.000013, 70.14 sec so far
Iteration 84061 (of 84548): max relative diff=0.000012, 75.15 sec so far

Iterative method: 84548 iterations in 75.67 seconds (average 0.000894, setup 0.06)

Value in the initial state: 0.0010445396729789396

Time for model checking: 75.84 seconds.

Result: 0.0010445396729789396


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_cluster.64-2000-20_rep3.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props
Wallclock time: 83.262 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:16:52 GMT+01:00 2026
Hostname: n23m0341.hpc.itc.rwth-aachen.de
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
Iteration 5239 (of 84548): max relative diff=0.000197, 5.01 sec so far
Iteration 10296 (of 84548): max relative diff=0.000099, 10.02 sec so far
Iteration 15442 (of 84548): max relative diff=0.000065, 15.03 sec so far
Iteration 20587 (of 84548): max relative diff=0.000049, 20.04 sec so far
Iteration 25765 (of 84548): max relative diff=0.000039, 25.05 sec so far
Iteration 30957 (of 84548): max relative diff=0.000032, 30.06 sec so far
Iteration 36118 (of 84548): max relative diff=0.000028, 35.07 sec so far
Iteration 41328 (of 84548): max relative diff=0.000024, 40.08 sec so far
Iteration 46477 (of 84548): max relative diff=0.000022, 45.09 sec so far
Iteration 51655 (of 84548): max relative diff=0.000019, 50.10 sec so far
Iteration 56826 (of 84548): max relative diff=0.000018, 55.11 sec so far
Iteration 61984 (of 84548): max relative diff=0.000016, 60.12 sec so far
Iteration 67180 (of 84548): max relative diff=0.000015, 65.13 sec so far
Iteration 72261 (of 84548): max relative diff=0.000014, 70.14 sec so far
Iteration 77416 (of 84548): max relative diff=0.000013, 75.15 sec so far
Iteration 82414 (of 84548): max relative diff=0.000012, 80.16 sec so far

Iterative method: 84548 iterations in 82.43 seconds (average 0.000974, setup 0.06)

Value in the initial state: 0.0010445396729789396

Time for model checking: 82.686 seconds.

Result: 0.0010445396729789396


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_cluster.64-2000-20_rep4.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props
Wallclock time: 78.940 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:07:33 GMT+01:00 2026
Hostname: n23m0261.hpc.itc.rwth-aachen.de
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

Time for model construction: 0.059 seconds.

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
Iteration 5603 (of 84548): max relative diff=0.000184, 5.01 sec so far
Iteration 11241 (of 84548): max relative diff=0.000090, 10.02 sec so far
Iteration 16874 (of 84548): max relative diff=0.000060, 15.03 sec so far
Iteration 22503 (of 84548): max relative diff=0.000045, 20.04 sec so far
Iteration 28139 (of 84548): max relative diff=0.000036, 25.05 sec so far
Iteration 33731 (of 84548): max relative diff=0.000030, 30.06 sec so far
Iteration 39318 (of 84548): max relative diff=0.000026, 35.07 sec so far
Iteration 44900 (of 84548): max relative diff=0.000022, 40.08 sec so far
Iteration 50513 (of 84548): max relative diff=0.000020, 45.09 sec so far
Iteration 56127 (of 84548): max relative diff=0.000018, 50.10 sec so far
Iteration 61744 (of 84548): max relative diff=0.000016, 55.11 sec so far
Iteration 67369 (of 84548): max relative diff=0.000015, 60.12 sec so far
Iteration 72980 (of 84548): max relative diff=0.000014, 65.13 sec so far
Iteration 78590 (of 84548): max relative diff=0.000013, 70.14 sec so far
Iteration 83927 (of 84548): max relative diff=0.000012, 75.15 sec so far

Iterative method: 84548 iterations in 75.79 seconds (average 0.000896, setup 0.05)

Value in the initial state: 0.0010445396729789396

Time for model checking: 75.925 seconds.

Result: 0.0010445396729789396


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_cluster.64-2000-20_rep5.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props
Wallclock time: 76.769 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:07 GMT+01:00 2026
Hostname: n23m0210.hpc.itc.rwth-aachen.de
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
Iteration 5573 (of 84548): max relative diff=0.000185, 5.01 sec so far
Iteration 11182 (of 84548): max relative diff=0.000091, 10.02 sec so far
Iteration 16792 (of 84548): max relative diff=0.000060, 15.03 sec so far
Iteration 22411 (of 84548): max relative diff=0.000045, 20.04 sec so far
Iteration 28038 (of 84548): max relative diff=0.000036, 25.05 sec so far
Iteration 33645 (of 84548): max relative diff=0.000030, 30.06 sec so far
Iteration 39274 (of 84548): max relative diff=0.000026, 35.07 sec so far
Iteration 44908 (of 84548): max relative diff=0.000022, 40.08 sec so far
Iteration 50544 (of 84548): max relative diff=0.000020, 45.09 sec so far
Iteration 56193 (of 84548): max relative diff=0.000018, 50.10 sec so far
Iteration 61678 (of 84548): max relative diff=0.000016, 55.11 sec so far
Iteration 67289 (of 84548): max relative diff=0.000015, 60.12 sec so far
Iteration 72907 (of 84548): max relative diff=0.000014, 65.13 sec so far
Iteration 78491 (of 84548): max relative diff=0.000013, 70.14 sec so far
Iteration 83824 (of 84548): max relative diff=0.000012, 75.15 sec so far

Iterative method: 84548 iterations in 75.90 seconds (average 0.000897, setup 0.06)

Value in the initial state: 0.0010445396729789396

Time for model checking: 76.192 seconds.

Result: 0.0010445396729789396


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

