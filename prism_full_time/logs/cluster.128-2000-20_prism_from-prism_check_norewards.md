# Log files

Tool configuration: prism_from-prism_check_norewards
Benchmark: [cluster.128-2000-20](../../models/cluster.128-2000-20)
Parsed values: [362.287, 357.374, 568.305, 350.502, 1633.089]



### Log file: prism_from-prism_check_norewards_cluster.128-2000-20_rep1.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism models/cluster.128-2000-20/property.props
Wallclock time: 362.287 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 08:01:04 GMT+01:00 2026
Hostname: r23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism models/cluster.128-2000-20/property.props

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Parsing properties file "models/cluster.128-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.07 seconds (average 0.000268, setup 0.00)

Time for model construction: 0.097 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 141117 of 597012 (23.6%)

Building hybrid MTBDD matrix... [levels=25, nodes=35758] [1.6 MB]
Adding explicit sparse matrices... [levels=12, num=1209, compact] [569.7 KB]
Creating vector for diagonals... [dist=2672, compact] [1.2 MB]
Allocating iteration vectors... [3 x 4.6 MB]
TOTAL: [17.0 MB]

Uniformisation: q.t = 41.318415 x 2000.000000 = 82636.830000
Fox-Glynn: left = 80621, right = 85077

Starting iterations...
Iteration 1173 (of 85077): max relative diff=0.005019, 5.01 sec so far
Iteration 2373 (of 85077): max relative diff=0.001228, 10.02 sec so far
Iteration 3558 (of 85077): max relative diff=0.000295, 15.03 sec so far
Iteration 4736 (of 85077): max relative diff=0.000219, 20.04 sec so far
Iteration 5917 (of 85077): max relative diff=0.000174, 25.05 sec so far
Iteration 7082 (of 85077): max relative diff=0.000145, 30.06 sec so far
Iteration 8244 (of 85077): max relative diff=0.000124, 35.07 sec so far
Iteration 9405 (of 85077): max relative diff=0.000108, 40.08 sec so far
Iteration 10575 (of 85077): max relative diff=0.000096, 45.09 sec so far
Iteration 11706 (of 85077): max relative diff=0.000087, 50.10 sec so far
Iteration 12848 (of 85077): max relative diff=0.000079, 55.11 sec so far
Iteration 13998 (of 85077): max relative diff=0.000072, 60.12 sec so far
Iteration 15124 (of 85077): max relative diff=0.000067, 65.13 sec so far
Iteration 16316 (of 85077): max relative diff=0.000062, 70.14 sec so far
Iteration 17514 (of 85077): max relative diff=0.000058, 75.15 sec so far
Iteration 18717 (of 85077): max relative diff=0.000054, 80.16 sec so far
Iteration 19922 (of 85077): max relative diff=0.000051, 85.17 sec so far
Iteration 21112 (of 85077): max relative diff=0.000048, 90.18 sec so far
Iteration 22296 (of 85077): max relative diff=0.000045, 95.19 sec so far
Iteration 23492 (of 85077): max relative diff=0.000043, 100.20 sec so far
Iteration 24699 (of 85077): max relative diff=0.000041, 105.21 sec so far
Iteration 25895 (of 85077): max relative diff=0.000039, 110.22 sec so far
Iteration 27086 (of 85077): max relative diff=0.000037, 115.23 sec so far
Iteration 28268 (of 85077): max relative diff=0.000036, 120.24 sec so far
Iteration 29405 (of 85077): max relative diff=0.000034, 125.25 sec so far
Iteration 30605 (of 85077): max relative diff=0.000033, 130.26 sec so far
Iteration 31807 (of 85077): max relative diff=0.000032, 135.27 sec so far
Iteration 33017 (of 85077): max relative diff=0.000030, 140.28 sec so far
Iteration 34207 (of 85077): max relative diff=0.000029, 145.29 sec so far
Iteration 35406 (of 85077): max relative diff=0.000028, 150.30 sec so far
Iteration 36582 (of 85077): max relative diff=0.000027, 155.31 sec so far
Iteration 37771 (of 85077): max relative diff=0.000027, 160.32 sec so far
Iteration 38967 (of 85077): max relative diff=0.000026, 165.33 sec so far
Iteration 40182 (of 85077): max relative diff=0.000025, 170.34 sec so far
Iteration 41354 (of 85077): max relative diff=0.000024, 175.35 sec so far
Iteration 42555 (of 85077): max relative diff=0.000024, 180.36 sec so far
Iteration 43700 (of 85077): max relative diff=0.000023, 185.37 sec so far
Iteration 44884 (of 85077): max relative diff=0.000022, 190.38 sec so far
Iteration 46088 (of 85077): max relative diff=0.000022, 195.39 sec so far
Iteration 47284 (of 85077): max relative diff=0.000021, 200.40 sec so far
Iteration 48489 (of 85077): max relative diff=0.000021, 205.41 sec so far
Iteration 49693 (of 85077): max relative diff=0.000020, 210.42 sec so far
Iteration 50897 (of 85077): max relative diff=0.000020, 215.43 sec so far
Iteration 52104 (of 85077): max relative diff=0.000019, 220.44 sec so far
Iteration 53296 (of 85077): max relative diff=0.000019, 225.45 sec so far
Iteration 54504 (of 85077): max relative diff=0.000018, 230.46 sec so far
Iteration 55683 (of 85077): max relative diff=0.000018, 235.47 sec so far
Iteration 56870 (of 85077): max relative diff=0.000018, 240.48 sec so far
Iteration 58062 (of 85077): max relative diff=0.000017, 245.49 sec so far
Iteration 59249 (of 85077): max relative diff=0.000017, 250.50 sec so far
Iteration 60429 (of 85077): max relative diff=0.000017, 255.51 sec so far
Iteration 61633 (of 85077): max relative diff=0.000016, 260.52 sec so far
Iteration 62819 (of 85077): max relative diff=0.000016, 265.53 sec so far
Iteration 64031 (of 85077): max relative diff=0.000016, 270.54 sec so far
Iteration 65225 (of 85077): max relative diff=0.000015, 275.55 sec so far
Iteration 66432 (of 85077): max relative diff=0.000015, 280.56 sec so far
Iteration 67629 (of 85077): max relative diff=0.000015, 285.57 sec so far
Iteration 68831 (of 85077): max relative diff=0.000015, 290.58 sec so far
Iteration 70011 (of 85077): max relative diff=0.000014, 295.59 sec so far
Iteration 71208 (of 85077): max relative diff=0.000014, 300.60 sec so far
Iteration 72387 (of 85077): max relative diff=0.000014, 305.61 sec so far
Iteration 73595 (of 85077): max relative diff=0.000014, 310.62 sec so far
Iteration 74795 (of 85077): max relative diff=0.000013, 315.63 sec so far
Iteration 75988 (of 85077): max relative diff=0.000013, 320.64 sec so far
Iteration 77185 (of 85077): max relative diff=0.000013, 325.65 sec so far
Iteration 78383 (of 85077): max relative diff=0.000013, 330.66 sec so far
Iteration 79588 (of 85077): max relative diff=0.000013, 335.67 sec so far
Iteration 80778 (of 85077): max relative diff=0.000012, 340.68 sec so far
Iteration 81889 (of 85077): max relative diff=0.000012, 345.69 sec so far
Iteration 83012 (of 85077): max relative diff=0.000012, 350.70 sec so far
Iteration 84090 (of 85077): max relative diff=0.000012, 355.71 sec so far

Iterative method: 85077 iterations in 360.46 seconds (average 0.004234, setup 0.26)

Value in the initial state: 0.001072402533769736

Time for model checking: 361.655 seconds.

Result: 0.001072402533769736


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_cluster.128-2000-20_rep2.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism models/cluster.128-2000-20/property.props
Wallclock time: 357.374 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:21:45 GMT+01:00 2026
Hostname: n23m0212.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism models/cluster.128-2000-20/property.props

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Parsing properties file "models/cluster.128-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.06 seconds (average 0.000230, setup 0.00)

Time for model construction: 0.12 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 141117 of 597012 (23.6%)

Building hybrid MTBDD matrix... [levels=25, nodes=35758] [1.6 MB]
Adding explicit sparse matrices... [levels=12, num=1209, compact] [569.7 KB]
Creating vector for diagonals... [dist=2672, compact] [1.2 MB]
Allocating iteration vectors... [3 x 4.6 MB]
TOTAL: [17.0 MB]

Uniformisation: q.t = 41.318415 x 2000.000000 = 82636.830000
Fox-Glynn: left = 80621, right = 85077

Starting iterations...
Iteration 1217 (of 85077): max relative diff=0.004729, 5.01 sec so far
Iteration 2435 (of 85077): max relative diff=0.001133, 10.02 sec so far
Iteration 3609 (of 85077): max relative diff=0.000291, 15.03 sec so far
Iteration 4811 (of 85077): max relative diff=0.000216, 20.04 sec so far
Iteration 6019 (of 85077): max relative diff=0.000171, 25.05 sec so far
Iteration 7235 (of 85077): max relative diff=0.000142, 30.06 sec so far
Iteration 8426 (of 85077): max relative diff=0.000121, 35.07 sec so far
Iteration 9646 (of 85077): max relative diff=0.000106, 40.08 sec so far
Iteration 10865 (of 85077): max relative diff=0.000094, 45.09 sec so far
Iteration 12087 (of 85077): max relative diff=0.000084, 50.10 sec so far
Iteration 13308 (of 85077): max relative diff=0.000076, 55.11 sec so far
Iteration 14527 (of 85077): max relative diff=0.000070, 60.12 sec so far
Iteration 15746 (of 85077): max relative diff=0.000064, 65.13 sec so far
Iteration 16964 (of 85077): max relative diff=0.000060, 70.14 sec so far
Iteration 18155 (of 85077): max relative diff=0.000056, 75.15 sec so far
Iteration 19362 (of 85077): max relative diff=0.000052, 80.16 sec so far
Iteration 20572 (of 85077): max relative diff=0.000049, 85.17 sec so far
Iteration 21790 (of 85077): max relative diff=0.000046, 90.18 sec so far
Iteration 23006 (of 85077): max relative diff=0.000044, 95.19 sec so far
Iteration 24218 (of 85077): max relative diff=0.000042, 100.20 sec so far
Iteration 25433 (of 85077): max relative diff=0.000040, 105.21 sec so far
Iteration 26646 (of 85077): max relative diff=0.000038, 110.22 sec so far
Iteration 27861 (of 85077): max relative diff=0.000036, 115.23 sec so far
Iteration 29071 (of 85077): max relative diff=0.000035, 120.24 sec so far
Iteration 30287 (of 85077): max relative diff=0.000033, 125.25 sec so far
Iteration 31499 (of 85077): max relative diff=0.000032, 130.26 sec so far
Iteration 32672 (of 85077): max relative diff=0.000031, 135.27 sec so far
Iteration 33866 (of 85077): max relative diff=0.000030, 140.28 sec so far
Iteration 35065 (of 85077): max relative diff=0.000029, 145.29 sec so far
Iteration 36279 (of 85077): max relative diff=0.000028, 150.30 sec so far
Iteration 37471 (of 85077): max relative diff=0.000027, 155.31 sec so far
Iteration 38688 (of 85077): max relative diff=0.000026, 160.32 sec so far
Iteration 39900 (of 85077): max relative diff=0.000025, 165.33 sec so far
Iteration 41115 (of 85077): max relative diff=0.000024, 170.34 sec so far
Iteration 42333 (of 85077): max relative diff=0.000024, 175.35 sec so far
Iteration 43550 (of 85077): max relative diff=0.000023, 180.36 sec so far
Iteration 44766 (of 85077): max relative diff=0.000022, 185.37 sec so far
Iteration 45984 (of 85077): max relative diff=0.000022, 190.38 sec so far
Iteration 47165 (of 85077): max relative diff=0.000021, 195.39 sec so far
Iteration 48377 (of 85077): max relative diff=0.000021, 200.40 sec so far
Iteration 49588 (of 85077): max relative diff=0.000020, 205.41 sec so far
Iteration 50805 (of 85077): max relative diff=0.000020, 210.42 sec so far
Iteration 52020 (of 85077): max relative diff=0.000019, 215.43 sec so far
Iteration 53238 (of 85077): max relative diff=0.000019, 220.44 sec so far
Iteration 54454 (of 85077): max relative diff=0.000018, 225.45 sec so far
Iteration 55673 (of 85077): max relative diff=0.000018, 230.46 sec so far
Iteration 56892 (of 85077): max relative diff=0.000018, 235.47 sec so far
Iteration 58108 (of 85077): max relative diff=0.000017, 240.48 sec so far
Iteration 59326 (of 85077): max relative diff=0.000017, 245.49 sec so far
Iteration 60543 (of 85077): max relative diff=0.000017, 250.50 sec so far
Iteration 61734 (of 85077): max relative diff=0.000016, 255.51 sec so far
Iteration 62947 (of 85077): max relative diff=0.000016, 260.52 sec so far
Iteration 64156 (of 85077): max relative diff=0.000016, 265.53 sec so far
Iteration 65371 (of 85077): max relative diff=0.000015, 270.54 sec so far
Iteration 66590 (of 85077): max relative diff=0.000015, 275.55 sec so far
Iteration 67807 (of 85077): max relative diff=0.000015, 280.56 sec so far
Iteration 69024 (of 85077): max relative diff=0.000015, 285.57 sec so far
Iteration 70239 (of 85077): max relative diff=0.000014, 290.58 sec so far
Iteration 71457 (of 85077): max relative diff=0.000014, 295.59 sec so far
Iteration 72675 (of 85077): max relative diff=0.000014, 300.60 sec so far
Iteration 73893 (of 85077): max relative diff=0.000014, 305.61 sec so far
Iteration 75109 (of 85077): max relative diff=0.000013, 310.62 sec so far
Iteration 76301 (of 85077): max relative diff=0.000013, 315.63 sec so far
Iteration 77512 (of 85077): max relative diff=0.000013, 320.64 sec so far
Iteration 78721 (of 85077): max relative diff=0.000013, 325.65 sec so far
Iteration 79940 (of 85077): max relative diff=0.000013, 330.66 sec so far
Iteration 81101 (of 85077): max relative diff=0.000012, 335.67 sec so far
Iteration 82196 (of 85077): max relative diff=0.000012, 340.68 sec so far
Iteration 83290 (of 85077): max relative diff=0.000012, 345.69 sec so far
Iteration 84383 (of 85077): max relative diff=0.000012, 350.70 sec so far

Iterative method: 85077 iterations in 354.13 seconds (average 0.004160, setup 0.25)

Value in the initial state: 0.001072402533769736

Time for model checking: 355.06 seconds.

Result: 0.001072402533769736


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_cluster.128-2000-20_rep3.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism models/cluster.128-2000-20/property.props
Wallclock time: 568.305 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:22:36 GMT+01:00 2026
Hostname: r23m0211.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism models/cluster.128-2000-20/property.props

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Parsing properties file "models/cluster.128-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.08 seconds (average 0.000307, setup 0.00)

Time for model construction: 0.143 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 141117 of 597012 (23.6%)

Building hybrid MTBDD matrix... [levels=25, nodes=35758] [1.6 MB]
Adding explicit sparse matrices... [levels=12, num=1209, compact] [569.7 KB]
Creating vector for diagonals... [dist=2672, compact] [1.2 MB]
Allocating iteration vectors... [3 x 4.6 MB]
TOTAL: [17.0 MB]

Uniformisation: q.t = 41.318415 x 2000.000000 = 82636.830000
Fox-Glynn: left = 80621, right = 85077

Starting iterations...
Iteration 727 (of 85077): max relative diff=0.009015, 5.01 sec so far
Iteration 1454 (of 85077): max relative diff=0.003618, 10.02 sec so far
Iteration 2182 (of 85077): max relative diff=0.001559, 15.03 sec so far
Iteration 2921 (of 85077): max relative diff=0.000593, 20.04 sec so far
Iteration 3636 (of 85077): max relative diff=0.000289, 25.05 sec so far
Iteration 4360 (of 85077): max relative diff=0.000239, 30.06 sec so far
Iteration 5089 (of 85077): max relative diff=0.000203, 35.07 sec so far
Iteration 5815 (of 85077): max relative diff=0.000177, 40.08 sec so far
Iteration 6554 (of 85077): max relative diff=0.000157, 45.09 sec so far
Iteration 7284 (of 85077): max relative diff=0.000141, 50.10 sec so far
Iteration 8015 (of 85077): max relative diff=0.000127, 55.11 sec so far
Iteration 8745 (of 85077): max relative diff=0.000117, 60.12 sec so far
Iteration 9472 (of 85077): max relative diff=0.000108, 65.13 sec so far
Iteration 10202 (of 85077): max relative diff=0.000100, 70.14 sec so far
Iteration 10943 (of 85077): max relative diff=0.000093, 75.15 sec so far
Iteration 11670 (of 85077): max relative diff=0.000087, 80.16 sec so far
Iteration 12393 (of 85077): max relative diff=0.000082, 85.17 sec so far
Iteration 13128 (of 85077): max relative diff=0.000077, 90.18 sec so far
Iteration 13855 (of 85077): max relative diff=0.000073, 95.19 sec so far
Iteration 14600 (of 85077): max relative diff=0.000069, 100.20 sec so far
Iteration 15331 (of 85077): max relative diff=0.000066, 105.21 sec so far
Iteration 16092 (of 85077): max relative diff=0.000063, 110.22 sec so far
Iteration 16859 (of 85077): max relative diff=0.000060, 115.23 sec so far
Iteration 17626 (of 85077): max relative diff=0.000057, 120.24 sec so far
Iteration 18410 (of 85077): max relative diff=0.000055, 125.25 sec so far
Iteration 19173 (of 85077): max relative diff=0.000053, 130.26 sec so far
Iteration 19943 (of 85077): max relative diff=0.000051, 135.27 sec so far
Iteration 20712 (of 85077): max relative diff=0.000049, 140.28 sec so far
Iteration 21460 (of 85077): max relative diff=0.000047, 145.29 sec so far
Iteration 22229 (of 85077): max relative diff=0.000045, 150.30 sec so far
Iteration 23001 (of 85077): max relative diff=0.000044, 155.31 sec so far
Iteration 23764 (of 85077): max relative diff=0.000042, 160.32 sec so far
Iteration 24527 (of 85077): max relative diff=0.000041, 165.33 sec so far
Iteration 25289 (of 85077): max relative diff=0.000040, 170.34 sec so far
Iteration 26056 (of 85077): max relative diff=0.000039, 175.35 sec so far
Iteration 26837 (of 85077): max relative diff=0.000037, 180.36 sec so far
Iteration 27604 (of 85077): max relative diff=0.000036, 185.37 sec so far
Iteration 28367 (of 85077): max relative diff=0.000035, 190.38 sec so far
Iteration 29133 (of 85077): max relative diff=0.000035, 195.39 sec so far
Iteration 29900 (of 85077): max relative diff=0.000034, 200.40 sec so far
Iteration 30665 (of 85077): max relative diff=0.000033, 205.41 sec so far
Iteration 31425 (of 85077): max relative diff=0.000032, 210.42 sec so far
Iteration 32188 (of 85077): max relative diff=0.000031, 215.43 sec so far
Iteration 32953 (of 85077): max relative diff=0.000030, 220.44 sec so far
Iteration 33723 (of 85077): max relative diff=0.000030, 225.45 sec so far
Iteration 34492 (of 85077): max relative diff=0.000029, 230.46 sec so far
Iteration 35267 (of 85077): max relative diff=0.000028, 235.47 sec so far
Iteration 36033 (of 85077): max relative diff=0.000028, 240.48 sec so far
Iteration 36800 (of 85077): max relative diff=0.000027, 245.49 sec so far
Iteration 37563 (of 85077): max relative diff=0.000027, 250.50 sec so far
Iteration 38328 (of 85077): max relative diff=0.000026, 255.51 sec so far
Iteration 39106 (of 85077): max relative diff=0.000026, 260.52 sec so far
Iteration 39854 (of 85077): max relative diff=0.000025, 265.53 sec so far
Iteration 40617 (of 85077): max relative diff=0.000025, 270.54 sec so far
Iteration 41379 (of 85077): max relative diff=0.000024, 275.55 sec so far
Iteration 42149 (of 85077): max relative diff=0.000024, 280.56 sec so far
Iteration 42918 (of 85077): max relative diff=0.000023, 285.57 sec so far
Iteration 43692 (of 85077): max relative diff=0.000023, 290.58 sec so far
Iteration 44455 (of 85077): max relative diff=0.000023, 295.59 sec so far
Iteration 45218 (of 85077): max relative diff=0.000022, 300.60 sec so far
Iteration 45984 (of 85077): max relative diff=0.000022, 305.61 sec so far
Iteration 46753 (of 85077): max relative diff=0.000021, 310.62 sec so far
Iteration 47536 (of 85077): max relative diff=0.000021, 315.63 sec so far
Iteration 48303 (of 85077): max relative diff=0.000021, 320.64 sec so far
Iteration 49047 (of 85077): max relative diff=0.000020, 325.65 sec so far
Iteration 49807 (of 85077): max relative diff=0.000020, 330.66 sec so far
Iteration 50570 (of 85077): max relative diff=0.000020, 335.67 sec so far
Iteration 51348 (of 85077): max relative diff=0.000020, 340.68 sec so far
Iteration 52114 (of 85077): max relative diff=0.000019, 345.69 sec so far
Iteration 52880 (of 85077): max relative diff=0.000019, 350.70 sec so far
Iteration 53641 (of 85077): max relative diff=0.000019, 355.71 sec so far
Iteration 54409 (of 85077): max relative diff=0.000018, 360.72 sec so far
Iteration 55178 (of 85077): max relative diff=0.000018, 365.73 sec so far
Iteration 55958 (of 85077): max relative diff=0.000018, 370.74 sec so far
Iteration 56720 (of 85077): max relative diff=0.000018, 375.75 sec so far
Iteration 57486 (of 85077): max relative diff=0.000017, 380.76 sec so far
Iteration 58236 (of 85077): max relative diff=0.000017, 385.77 sec so far
Iteration 59000 (of 85077): max relative diff=0.000017, 390.78 sec so far
Iteration 59778 (of 85077): max relative diff=0.000017, 395.79 sec so far
Iteration 60539 (of 85077): max relative diff=0.000017, 400.80 sec so far
Iteration 61301 (of 85077): max relative diff=0.000016, 405.81 sec so far
Iteration 62070 (of 85077): max relative diff=0.000016, 410.82 sec so far
Iteration 62832 (of 85077): max relative diff=0.000016, 415.83 sec so far
Iteration 63617 (of 85077): max relative diff=0.000016, 420.84 sec so far
Iteration 64381 (of 85077): max relative diff=0.000016, 425.85 sec so far
Iteration 65145 (of 85077): max relative diff=0.000015, 430.86 sec so far
Iteration 65909 (of 85077): max relative diff=0.000015, 435.87 sec so far
Iteration 66675 (of 85077): max relative diff=0.000015, 440.88 sec so far
Iteration 67429 (of 85077): max relative diff=0.000015, 445.89 sec so far
Iteration 68207 (of 85077): max relative diff=0.000015, 450.90 sec so far
Iteration 68972 (of 85077): max relative diff=0.000015, 455.91 sec so far
Iteration 69738 (of 85077): max relative diff=0.000014, 460.92 sec so far
Iteration 70509 (of 85077): max relative diff=0.000014, 465.93 sec so far
Iteration 71278 (of 85077): max relative diff=0.000014, 470.94 sec so far
Iteration 72059 (of 85077): max relative diff=0.000014, 475.95 sec so far
Iteration 72826 (of 85077): max relative diff=0.000014, 480.96 sec so far
Iteration 73591 (of 85077): max relative diff=0.000014, 485.97 sec so far
Iteration 74356 (of 85077): max relative diff=0.000013, 490.98 sec so far
Iteration 75124 (of 85077): max relative diff=0.000013, 495.99 sec so far
Iteration 75891 (of 85077): max relative diff=0.000013, 501.00 sec so far
Iteration 76650 (of 85077): max relative diff=0.000013, 506.01 sec so far
Iteration 77414 (of 85077): max relative diff=0.000013, 511.02 sec so far
Iteration 78183 (of 85077): max relative diff=0.000013, 516.03 sec so far
Iteration 78952 (of 85077): max relative diff=0.000013, 521.04 sec so far
Iteration 79725 (of 85077): max relative diff=0.000013, 526.05 sec so far
Iteration 80508 (of 85077): max relative diff=0.000012, 531.06 sec so far
Iteration 81188 (of 85077): max relative diff=0.000012, 536.07 sec so far
Iteration 81856 (of 85077): max relative diff=0.000012, 541.08 sec so far
Iteration 82525 (of 85077): max relative diff=0.000012, 546.09 sec so far
Iteration 83193 (of 85077): max relative diff=0.000012, 551.10 sec so far
Iteration 83874 (of 85077): max relative diff=0.000012, 556.11 sec so far
Iteration 84539 (of 85077): max relative diff=0.000012, 561.12 sec so far

Iterative method: 85077 iterations in 565.50 seconds (average 0.006644, setup 0.29)

Value in the initial state: 0.001072402533769736

Time for model checking: 567.441 seconds.

Result: 0.001072402533769736


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_cluster.128-2000-20_rep4.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism models/cluster.128-2000-20/property.props
Wallclock time: 350.502 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:16:28 GMT+01:00 2026
Hostname: n23m0341.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism models/cluster.128-2000-20/property.props

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Parsing properties file "models/cluster.128-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.06 seconds (average 0.000230, setup 0.00)

Time for model construction: 0.095 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 141117 of 597012 (23.6%)

Building hybrid MTBDD matrix... [levels=25, nodes=35758] [1.6 MB]
Adding explicit sparse matrices... [levels=12, num=1209, compact] [569.7 KB]
Creating vector for diagonals... [dist=2672, compact] [1.2 MB]
Allocating iteration vectors... [3 x 4.6 MB]
TOTAL: [17.0 MB]

Uniformisation: q.t = 41.318415 x 2000.000000 = 82636.830000
Fox-Glynn: left = 80621, right = 85077

Starting iterations...
Iteration 1227 (of 85077): max relative diff=0.004675, 5.01 sec so far
Iteration 2467 (of 85077): max relative diff=0.001085, 10.02 sec so far
Iteration 3716 (of 85077): max relative diff=0.000282, 15.03 sec so far
Iteration 4961 (of 85077): max relative diff=0.000209, 20.04 sec so far
Iteration 6209 (of 85077): max relative diff=0.000166, 25.05 sec so far
Iteration 7405 (of 85077): max relative diff=0.000138, 30.06 sec so far
Iteration 8604 (of 85077): max relative diff=0.000119, 35.07 sec so far
Iteration 9824 (of 85077): max relative diff=0.000104, 40.08 sec so far
Iteration 11043 (of 85077): max relative diff=0.000092, 45.09 sec so far
Iteration 12282 (of 85077): max relative diff=0.000083, 50.10 sec so far
Iteration 13520 (of 85077): max relative diff=0.000075, 55.11 sec so far
Iteration 14732 (of 85077): max relative diff=0.000069, 60.12 sec so far
Iteration 15957 (of 85077): max relative diff=0.000063, 65.13 sec so far
Iteration 17196 (of 85077): max relative diff=0.000059, 70.14 sec so far
Iteration 18437 (of 85077): max relative diff=0.000055, 75.15 sec so far
Iteration 19677 (of 85077): max relative diff=0.000051, 80.16 sec so far
Iteration 20918 (of 85077): max relative diff=0.000048, 85.17 sec so far
Iteration 22136 (of 85077): max relative diff=0.000046, 90.18 sec so far
Iteration 23330 (of 85077): max relative diff=0.000043, 95.19 sec so far
Iteration 24553 (of 85077): max relative diff=0.000041, 100.20 sec so far
Iteration 25785 (of 85077): max relative diff=0.000039, 105.21 sec so far
Iteration 27022 (of 85077): max relative diff=0.000037, 110.22 sec so far
Iteration 28262 (of 85077): max relative diff=0.000036, 115.23 sec so far
Iteration 29494 (of 85077): max relative diff=0.000034, 120.24 sec so far
Iteration 30694 (of 85077): max relative diff=0.000033, 125.25 sec so far
Iteration 31905 (of 85077): max relative diff=0.000032, 130.26 sec so far
Iteration 33138 (of 85077): max relative diff=0.000030, 135.27 sec so far
Iteration 34378 (of 85077): max relative diff=0.000029, 140.28 sec so far
Iteration 35626 (of 85077): max relative diff=0.000028, 145.29 sec so far
Iteration 36872 (of 85077): max relative diff=0.000027, 150.30 sec so far
Iteration 38065 (of 85077): max relative diff=0.000026, 155.31 sec so far
Iteration 39301 (of 85077): max relative diff=0.000026, 160.32 sec so far
Iteration 40540 (of 85077): max relative diff=0.000025, 165.33 sec so far
Iteration 41793 (of 85077): max relative diff=0.000024, 170.34 sec so far
Iteration 43046 (of 85077): max relative diff=0.000023, 175.35 sec so far
Iteration 44294 (of 85077): max relative diff=0.000023, 180.36 sec so far
Iteration 45496 (of 85077): max relative diff=0.000022, 185.37 sec so far
Iteration 46735 (of 85077): max relative diff=0.000021, 190.38 sec so far
Iteration 47973 (of 85077): max relative diff=0.000021, 195.39 sec so far
Iteration 49209 (of 85077): max relative diff=0.000020, 200.40 sec so far
Iteration 50446 (of 85077): max relative diff=0.000020, 205.41 sec so far
Iteration 51683 (of 85077): max relative diff=0.000019, 210.42 sec so far
Iteration 52865 (of 85077): max relative diff=0.000019, 215.43 sec so far
Iteration 54082 (of 85077): max relative diff=0.000019, 220.44 sec so far
Iteration 55305 (of 85077): max relative diff=0.000018, 225.45 sec so far
Iteration 56531 (of 85077): max relative diff=0.000018, 230.46 sec so far
Iteration 57756 (of 85077): max relative diff=0.000017, 235.47 sec so far
Iteration 58982 (of 85077): max relative diff=0.000017, 240.48 sec so far
Iteration 60210 (of 85077): max relative diff=0.000017, 245.49 sec so far
Iteration 61436 (of 85077): max relative diff=0.000016, 250.50 sec so far
Iteration 62661 (of 85077): max relative diff=0.000016, 255.51 sec so far
Iteration 63888 (of 85077): max relative diff=0.000016, 260.52 sec so far
Iteration 65116 (of 85077): max relative diff=0.000015, 265.53 sec so far
Iteration 66344 (of 85077): max relative diff=0.000015, 270.54 sec so far
Iteration 67545 (of 85077): max relative diff=0.000015, 275.55 sec so far
Iteration 68759 (of 85077): max relative diff=0.000015, 280.56 sec so far
Iteration 69984 (of 85077): max relative diff=0.000014, 285.57 sec so far
Iteration 71211 (of 85077): max relative diff=0.000014, 290.58 sec so far
Iteration 72437 (of 85077): max relative diff=0.000014, 295.59 sec so far
Iteration 73663 (of 85077): max relative diff=0.000014, 300.60 sec so far
Iteration 74888 (of 85077): max relative diff=0.000013, 305.61 sec so far
Iteration 76113 (of 85077): max relative diff=0.000013, 310.62 sec so far
Iteration 77339 (of 85077): max relative diff=0.000013, 315.63 sec so far
Iteration 78567 (of 85077): max relative diff=0.000013, 320.64 sec so far
Iteration 79792 (of 85077): max relative diff=0.000013, 325.65 sec so far
Iteration 80986 (of 85077): max relative diff=0.000012, 330.66 sec so far
Iteration 82117 (of 85077): max relative diff=0.000012, 335.67 sec so far
Iteration 83255 (of 85077): max relative diff=0.000012, 340.68 sec so far
Iteration 84405 (of 85077): max relative diff=0.000012, 345.69 sec so far

Iterative method: 85077 iterations in 348.87 seconds (average 0.004098, setup 0.26)

Value in the initial state: 0.001072402533769736

Time for model checking: 349.862 seconds.

Result: 0.001072402533769736


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_cluster.128-2000-20_rep5.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism models/cluster.128-2000-20/property.props
Wallclock time: 1633.089 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:50:37 GMT+01:00 2026
Hostname: r23m0207.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism models/cluster.128-2000-20/property.props

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Parsing properties file "models/cluster.128-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.29 seconds (average 0.001111, setup 0.00)

Time for model construction: 0.51 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 141117 of 597012 (23.6%)

Building hybrid MTBDD matrix... [levels=25, nodes=35758] [1.6 MB]
Adding explicit sparse matrices... [levels=12, num=1209, compact] [569.7 KB]
Creating vector for diagonals... [dist=2672, compact] [1.2 MB]
Allocating iteration vectors... [3 x 4.6 MB]
TOTAL: [17.0 MB]

Uniformisation: q.t = 41.318415 x 2000.000000 = 82636.830000
Fox-Glynn: left = 80621, right = 85077

Starting iterations...
Iteration 266 (of 85077): max relative diff=0.024040, 5.01 sec so far
Iteration 532 (of 85077): max relative diff=0.012430, 10.03 sec so far
Iteration 798 (of 85077): max relative diff=0.008019, 15.05 sec so far
Iteration 1064 (of 85077): max relative diff=0.005718, 20.07 sec so far
Iteration 1330 (of 85077): max relative diff=0.004219, 25.08 sec so far
Iteration 1595 (of 85077): max relative diff=0.003117, 30.09 sec so far
Iteration 1861 (of 85077): max relative diff=0.002291, 35.10 sec so far
Iteration 2127 (of 85077): max relative diff=0.001666, 40.11 sec so far
Iteration 2393 (of 85077): max relative diff=0.001194, 45.12 sec so far
Iteration 2659 (of 85077): max relative diff=0.000842, 50.13 sec so far
Iteration 2925 (of 85077): max relative diff=0.000590, 55.15 sec so far
Iteration 3189 (of 85077): max relative diff=0.000425, 60.16 sec so far
Iteration 3455 (of 85077): max relative diff=0.000321, 65.18 sec so far
Iteration 3719 (of 85077): max relative diff=0.000282, 70.19 sec so far
Iteration 3985 (of 85077): max relative diff=0.000262, 75.21 sec so far
Iteration 4250 (of 85077): max relative diff=0.000245, 80.22 sec so far
Iteration 4514 (of 85077): max relative diff=0.000230, 85.23 sec so far
Iteration 4779 (of 85077): max relative diff=0.000217, 90.25 sec so far
Iteration 5045 (of 85077): max relative diff=0.000205, 95.27 sec so far
Iteration 5309 (of 85077): max relative diff=0.000195, 100.28 sec so far
Iteration 5573 (of 85077): max relative diff=0.000185, 105.30 sec so far
Iteration 5837 (of 85077): max relative diff=0.000177, 110.31 sec so far
Iteration 6100 (of 85077): max relative diff=0.000169, 115.32 sec so far
Iteration 6364 (of 85077): max relative diff=0.000161, 120.33 sec so far
Iteration 6628 (of 85077): max relative diff=0.000155, 125.35 sec so far
Iteration 6894 (of 85077): max relative diff=0.000149, 130.36 sec so far
Iteration 7160 (of 85077): max relative diff=0.000143, 135.38 sec so far
Iteration 7425 (of 85077): max relative diff=0.000138, 140.39 sec so far
Iteration 7691 (of 85077): max relative diff=0.000133, 145.40 sec so far
Iteration 7957 (of 85077): max relative diff=0.000128, 150.42 sec so far
Iteration 8223 (of 85077): max relative diff=0.000124, 155.43 sec so far
Iteration 8489 (of 85077): max relative diff=0.000120, 160.44 sec so far
Iteration 8755 (of 85077): max relative diff=0.000116, 165.46 sec so far
Iteration 9021 (of 85077): max relative diff=0.000113, 170.47 sec so far
Iteration 9287 (of 85077): max relative diff=0.000110, 175.48 sec so far
Iteration 9553 (of 85077): max relative diff=0.000107, 180.50 sec so far
Iteration 9819 (of 85077): max relative diff=0.000104, 185.51 sec so far
Iteration 10085 (of 85077): max relative diff=0.000101, 190.52 sec so far
Iteration 10351 (of 85077): max relative diff=0.000098, 195.54 sec so far
Iteration 10617 (of 85077): max relative diff=0.000096, 200.55 sec so far
Iteration 10883 (of 85077): max relative diff=0.000093, 205.56 sec so far
Iteration 11148 (of 85077): max relative diff=0.000091, 210.57 sec so far
Iteration 11414 (of 85077): max relative diff=0.000089, 215.59 sec so far
Iteration 11680 (of 85077): max relative diff=0.000087, 220.61 sec so far
Iteration 11946 (of 85077): max relative diff=0.000085, 225.63 sec so far
Iteration 12212 (of 85077): max relative diff=0.000083, 230.65 sec so far
Iteration 12478 (of 85077): max relative diff=0.000081, 235.67 sec so far
Iteration 12744 (of 85077): max relative diff=0.000080, 240.68 sec so far
Iteration 13010 (of 85077): max relative diff=0.000078, 245.69 sec so far
Iteration 13276 (of 85077): max relative diff=0.000076, 250.70 sec so far
Iteration 13542 (of 85077): max relative diff=0.000075, 255.71 sec so far
Iteration 13808 (of 85077): max relative diff=0.000073, 260.73 sec so far
Iteration 14074 (of 85077): max relative diff=0.000072, 265.74 sec so far
Iteration 14340 (of 85077): max relative diff=0.000071, 270.75 sec so far
Iteration 14605 (of 85077): max relative diff=0.000069, 275.76 sec so far
Iteration 14871 (of 85077): max relative diff=0.000068, 280.78 sec so far
Iteration 15137 (of 85077): max relative diff=0.000067, 285.80 sec so far
Iteration 15402 (of 85077): max relative diff=0.000066, 290.81 sec so far
Iteration 15668 (of 85077): max relative diff=0.000065, 295.82 sec so far
Iteration 15934 (of 85077): max relative diff=0.000063, 300.83 sec so far
Iteration 16200 (of 85077): max relative diff=0.000062, 305.84 sec so far
Iteration 16466 (of 85077): max relative diff=0.000061, 310.85 sec so far
Iteration 16732 (of 85077): max relative diff=0.000060, 315.86 sec so far
Iteration 16998 (of 85077): max relative diff=0.000059, 320.88 sec so far
Iteration 17263 (of 85077): max relative diff=0.000059, 325.90 sec so far
Iteration 17528 (of 85077): max relative diff=0.000058, 330.92 sec so far
Iteration 17794 (of 85077): max relative diff=0.000057, 335.94 sec so far
Iteration 18060 (of 85077): max relative diff=0.000056, 340.95 sec so far
Iteration 18326 (of 85077): max relative diff=0.000055, 345.96 sec so far
Iteration 18592 (of 85077): max relative diff=0.000054, 350.97 sec so far
Iteration 18858 (of 85077): max relative diff=0.000054, 355.98 sec so far
Iteration 19124 (of 85077): max relative diff=0.000053, 361.00 sec so far
Iteration 19390 (of 85077): max relative diff=0.000052, 366.02 sec so far
Iteration 19656 (of 85077): max relative diff=0.000051, 371.03 sec so far
Iteration 19922 (of 85077): max relative diff=0.000051, 376.05 sec so far
Iteration 20188 (of 85077): max relative diff=0.000050, 381.07 sec so far
Iteration 20453 (of 85077): max relative diff=0.000049, 386.08 sec so far
Iteration 20719 (of 85077): max relative diff=0.000049, 391.09 sec so far
Iteration 20985 (of 85077): max relative diff=0.000048, 396.11 sec so far
Iteration 21251 (of 85077): max relative diff=0.000047, 401.12 sec so far
Iteration 21517 (of 85077): max relative diff=0.000047, 406.14 sec so far
Iteration 21783 (of 85077): max relative diff=0.000046, 411.16 sec so far
Iteration 22049 (of 85077): max relative diff=0.000046, 416.17 sec so far
Iteration 22314 (of 85077): max relative diff=0.000045, 421.18 sec so far
Iteration 22578 (of 85077): max relative diff=0.000045, 426.19 sec so far
Iteration 22844 (of 85077): max relative diff=0.000044, 431.21 sec so far
Iteration 23110 (of 85077): max relative diff=0.000044, 436.22 sec so far
Iteration 23376 (of 85077): max relative diff=0.000043, 441.24 sec so far
Iteration 23642 (of 85077): max relative diff=0.000043, 446.26 sec so far
Iteration 23908 (of 85077): max relative diff=0.000042, 451.28 sec so far
Iteration 24174 (of 85077): max relative diff=0.000042, 456.30 sec so far
Iteration 24440 (of 85077): max relative diff=0.000041, 461.31 sec so far
Iteration 24706 (of 85077): max relative diff=0.000041, 466.33 sec so far
Iteration 24972 (of 85077): max relative diff=0.000040, 471.34 sec so far
Iteration 25238 (of 85077): max relative diff=0.000040, 476.36 sec so far
Iteration 25504 (of 85077): max relative diff=0.000039, 481.37 sec so far
Iteration 25770 (of 85077): max relative diff=0.000039, 486.38 sec so far
Iteration 26036 (of 85077): max relative diff=0.000039, 491.39 sec so far
Iteration 26300 (of 85077): max relative diff=0.000038, 496.41 sec so far
Iteration 26564 (of 85077): max relative diff=0.000038, 501.43 sec so far
Iteration 26829 (of 85077): max relative diff=0.000038, 506.44 sec so far
Iteration 27094 (of 85077): max relative diff=0.000037, 511.46 sec so far
Iteration 27359 (of 85077): max relative diff=0.000037, 516.48 sec so far
Iteration 27625 (of 85077): max relative diff=0.000036, 521.50 sec so far
Iteration 27891 (of 85077): max relative diff=0.000036, 526.51 sec so far
Iteration 28155 (of 85077): max relative diff=0.000036, 531.53 sec so far
Iteration 28419 (of 85077): max relative diff=0.000035, 536.54 sec so far
Iteration 28682 (of 85077): max relative diff=0.000035, 541.55 sec so far
Iteration 28944 (of 85077): max relative diff=0.000035, 546.57 sec so far
Iteration 29205 (of 85077): max relative diff=0.000034, 551.58 sec so far
Iteration 29466 (of 85077): max relative diff=0.000034, 556.60 sec so far
Iteration 29726 (of 85077): max relative diff=0.000034, 561.61 sec so far
Iteration 29989 (of 85077): max relative diff=0.000034, 566.62 sec so far
Iteration 30252 (of 85077): max relative diff=0.000033, 571.63 sec so far
Iteration 30515 (of 85077): max relative diff=0.000033, 576.65 sec so far
Iteration 30778 (of 85077): max relative diff=0.000033, 581.67 sec so far
Iteration 31041 (of 85077): max relative diff=0.000032, 586.68 sec so far
Iteration 31304 (of 85077): max relative diff=0.000032, 591.69 sec so far
Iteration 31566 (of 85077): max relative diff=0.000032, 596.70 sec so far
Iteration 31829 (of 85077): max relative diff=0.000032, 601.71 sec so far
Iteration 32090 (of 85077): max relative diff=0.000031, 606.72 sec so far
Iteration 32350 (of 85077): max relative diff=0.000031, 611.73 sec so far
Iteration 32611 (of 85077): max relative diff=0.000031, 616.75 sec so far
Iteration 32874 (of 85077): max relative diff=0.000031, 621.77 sec so far
Iteration 33137 (of 85077): max relative diff=0.000030, 626.79 sec so far
Iteration 33401 (of 85077): max relative diff=0.000030, 631.81 sec so far
Iteration 33664 (of 85077): max relative diff=0.000030, 636.83 sec so far
Iteration 33927 (of 85077): max relative diff=0.000030, 641.84 sec so far
Iteration 34190 (of 85077): max relative diff=0.000029, 646.85 sec so far
Iteration 34453 (of 85077): max relative diff=0.000029, 651.86 sec so far
Iteration 34716 (of 85077): max relative diff=0.000029, 656.87 sec so far
Iteration 34979 (of 85077): max relative diff=0.000029, 661.88 sec so far
Iteration 35240 (of 85077): max relative diff=0.000029, 666.89 sec so far
Iteration 35502 (of 85077): max relative diff=0.000028, 671.91 sec so far
Iteration 35766 (of 85077): max relative diff=0.000028, 676.93 sec so far
Iteration 36031 (of 85077): max relative diff=0.000028, 681.94 sec so far
Iteration 36297 (of 85077): max relative diff=0.000028, 686.95 sec so far
Iteration 36562 (of 85077): max relative diff=0.000027, 691.96 sec so far
Iteration 36828 (of 85077): max relative diff=0.000027, 696.98 sec so far
Iteration 37093 (of 85077): max relative diff=0.000027, 702.00 sec so far
Iteration 37357 (of 85077): max relative diff=0.000027, 707.01 sec so far
Iteration 37622 (of 85077): max relative diff=0.000027, 712.03 sec so far
Iteration 37886 (of 85077): max relative diff=0.000027, 717.04 sec so far
Iteration 38148 (of 85077): max relative diff=0.000026, 722.05 sec so far
Iteration 38411 (of 85077): max relative diff=0.000026, 727.07 sec so far
Iteration 38675 (of 85077): max relative diff=0.000026, 732.08 sec so far
Iteration 38940 (of 85077): max relative diff=0.000026, 737.09 sec so far
Iteration 39205 (of 85077): max relative diff=0.000026, 742.11 sec so far
Iteration 39469 (of 85077): max relative diff=0.000025, 747.12 sec so far
Iteration 39733 (of 85077): max relative diff=0.000025, 752.13 sec so far
Iteration 39995 (of 85077): max relative diff=0.000025, 757.14 sec so far
Iteration 40258 (of 85077): max relative diff=0.000025, 762.16 sec so far
Iteration 40523 (of 85077): max relative diff=0.000025, 767.17 sec so far
Iteration 40788 (of 85077): max relative diff=0.000025, 772.19 sec so far
Iteration 41053 (of 85077): max relative diff=0.000024, 777.20 sec so far
Iteration 41318 (of 85077): max relative diff=0.000024, 782.22 sec so far
Iteration 41583 (of 85077): max relative diff=0.000024, 787.23 sec so far
Iteration 41848 (of 85077): max relative diff=0.000024, 792.25 sec so far
Iteration 42113 (of 85077): max relative diff=0.000024, 797.27 sec so far
Iteration 42379 (of 85077): max relative diff=0.000024, 802.29 sec so far
Iteration 42644 (of 85077): max relative diff=0.000024, 807.31 sec so far
Iteration 42910 (of 85077): max relative diff=0.000023, 812.33 sec so far
Iteration 43176 (of 85077): max relative diff=0.000023, 817.35 sec so far
Iteration 43442 (of 85077): max relative diff=0.000023, 822.36 sec so far
Iteration 43708 (of 85077): max relative diff=0.000023, 827.38 sec so far
Iteration 43975 (of 85077): max relative diff=0.000023, 832.40 sec so far
Iteration 44241 (of 85077): max relative diff=0.000023, 837.41 sec so far
Iteration 44507 (of 85077): max relative diff=0.000023, 842.42 sec so far
Iteration 44773 (of 85077): max relative diff=0.000022, 847.44 sec so far
Iteration 45039 (of 85077): max relative diff=0.000022, 852.46 sec so far
Iteration 45305 (of 85077): max relative diff=0.000022, 857.47 sec so far
Iteration 45571 (of 85077): max relative diff=0.000022, 862.48 sec so far
Iteration 45837 (of 85077): max relative diff=0.000022, 867.49 sec so far
Iteration 46103 (of 85077): max relative diff=0.000022, 872.50 sec so far
Iteration 46369 (of 85077): max relative diff=0.000022, 877.52 sec so far
Iteration 46635 (of 85077): max relative diff=0.000022, 882.53 sec so far
Iteration 46901 (of 85077): max relative diff=0.000021, 887.54 sec so far
Iteration 47167 (of 85077): max relative diff=0.000021, 892.55 sec so far
Iteration 47433 (of 85077): max relative diff=0.000021, 897.56 sec so far
Iteration 47699 (of 85077): max relative diff=0.000021, 902.57 sec so far
Iteration 47965 (of 85077): max relative diff=0.000021, 907.59 sec so far
Iteration 48231 (of 85077): max relative diff=0.000021, 912.60 sec so far
Iteration 48497 (of 85077): max relative diff=0.000021, 917.62 sec so far
Iteration 48763 (of 85077): max relative diff=0.000021, 922.63 sec so far
Iteration 49029 (of 85077): max relative diff=0.000020, 927.64 sec so far
Iteration 49295 (of 85077): max relative diff=0.000020, 932.66 sec so far
Iteration 49561 (of 85077): max relative diff=0.000020, 937.67 sec so far
Iteration 49828 (of 85077): max relative diff=0.000020, 942.69 sec so far
Iteration 50094 (of 85077): max relative diff=0.000020, 947.70 sec so far
Iteration 50360 (of 85077): max relative diff=0.000020, 952.72 sec so far
Iteration 50627 (of 85077): max relative diff=0.000020, 957.74 sec so far
Iteration 50893 (of 85077): max relative diff=0.000020, 962.76 sec so far
Iteration 51159 (of 85077): max relative diff=0.000020, 967.77 sec so far
Iteration 51425 (of 85077): max relative diff=0.000020, 972.78 sec so far
Iteration 51691 (of 85077): max relative diff=0.000019, 977.80 sec so far
Iteration 51958 (of 85077): max relative diff=0.000019, 982.82 sec so far
Iteration 52224 (of 85077): max relative diff=0.000019, 987.84 sec so far
Iteration 52490 (of 85077): max relative diff=0.000019, 992.85 sec so far
Iteration 52756 (of 85077): max relative diff=0.000019, 997.86 sec so far
Iteration 53022 (of 85077): max relative diff=0.000019, 1002.88 sec so far
Iteration 53288 (of 85077): max relative diff=0.000019, 1007.89 sec so far
Iteration 53554 (of 85077): max relative diff=0.000019, 1012.91 sec so far
Iteration 53820 (of 85077): max relative diff=0.000019, 1017.92 sec so far
Iteration 54086 (of 85077): max relative diff=0.000019, 1022.93 sec so far
Iteration 54352 (of 85077): max relative diff=0.000018, 1027.95 sec so far
Iteration 54619 (of 85077): max relative diff=0.000018, 1032.97 sec so far
Iteration 54885 (of 85077): max relative diff=0.000018, 1037.99 sec so far
Iteration 55152 (of 85077): max relative diff=0.000018, 1043.01 sec so far
Iteration 55418 (of 85077): max relative diff=0.000018, 1048.02 sec so far
Iteration 55684 (of 85077): max relative diff=0.000018, 1053.04 sec so far
Iteration 55950 (of 85077): max relative diff=0.000018, 1058.05 sec so far
Iteration 56216 (of 85077): max relative diff=0.000018, 1063.06 sec so far
Iteration 56482 (of 85077): max relative diff=0.000018, 1068.08 sec so far
Iteration 56748 (of 85077): max relative diff=0.000018, 1073.09 sec so far
Iteration 57014 (of 85077): max relative diff=0.000018, 1078.10 sec so far
Iteration 57280 (of 85077): max relative diff=0.000018, 1083.12 sec so far
Iteration 57546 (of 85077): max relative diff=0.000017, 1088.13 sec so far
Iteration 57812 (of 85077): max relative diff=0.000017, 1093.15 sec so far
Iteration 58079 (of 85077): max relative diff=0.000017, 1098.17 sec so far
Iteration 58345 (of 85077): max relative diff=0.000017, 1103.18 sec so far
Iteration 58611 (of 85077): max relative diff=0.000017, 1108.19 sec so far
Iteration 58877 (of 85077): max relative diff=0.000017, 1113.20 sec so far
Iteration 59143 (of 85077): max relative diff=0.000017, 1118.22 sec so far
Iteration 59409 (of 85077): max relative diff=0.000017, 1123.24 sec so far
Iteration 59675 (of 85077): max relative diff=0.000017, 1128.25 sec so far
Iteration 59941 (of 85077): max relative diff=0.000017, 1133.26 sec so far
Iteration 60207 (of 85077): max relative diff=0.000017, 1138.27 sec so far
Iteration 60473 (of 85077): max relative diff=0.000017, 1143.28 sec so far
Iteration 60739 (of 85077): max relative diff=0.000017, 1148.29 sec so far
Iteration 61006 (of 85077): max relative diff=0.000016, 1153.31 sec so far
Iteration 61272 (of 85077): max relative diff=0.000016, 1158.33 sec so far
Iteration 61538 (of 85077): max relative diff=0.000016, 1163.35 sec so far
Iteration 61805 (of 85077): max relative diff=0.000016, 1168.37 sec so far
Iteration 62071 (of 85077): max relative diff=0.000016, 1173.38 sec so far
Iteration 62337 (of 85077): max relative diff=0.000016, 1178.40 sec so far
Iteration 62603 (of 85077): max relative diff=0.000016, 1183.41 sec so far
Iteration 62869 (of 85077): max relative diff=0.000016, 1188.42 sec so far
Iteration 63135 (of 85077): max relative diff=0.000016, 1193.43 sec so far
Iteration 63401 (of 85077): max relative diff=0.000016, 1198.45 sec so far
Iteration 63667 (of 85077): max relative diff=0.000016, 1203.47 sec so far
Iteration 63933 (of 85077): max relative diff=0.000016, 1208.48 sec so far
Iteration 64199 (of 85077): max relative diff=0.000016, 1213.49 sec so far
Iteration 64465 (of 85077): max relative diff=0.000016, 1218.50 sec so far
Iteration 64731 (of 85077): max relative diff=0.000015, 1223.52 sec so far
Iteration 64997 (of 85077): max relative diff=0.000015, 1228.53 sec so far
Iteration 65263 (of 85077): max relative diff=0.000015, 1233.54 sec so far
Iteration 65529 (of 85077): max relative diff=0.000015, 1238.55 sec so far
Iteration 65795 (of 85077): max relative diff=0.000015, 1243.56 sec so far
Iteration 66061 (of 85077): max relative diff=0.000015, 1248.57 sec so far
Iteration 66327 (of 85077): max relative diff=0.000015, 1253.58 sec so far
Iteration 66593 (of 85077): max relative diff=0.000015, 1258.60 sec so far
Iteration 66859 (of 85077): max relative diff=0.000015, 1263.62 sec so far
Iteration 67126 (of 85077): max relative diff=0.000015, 1268.64 sec so far
Iteration 67392 (of 85077): max relative diff=0.000015, 1273.66 sec so far
Iteration 67658 (of 85077): max relative diff=0.000015, 1278.68 sec so far
Iteration 67924 (of 85077): max relative diff=0.000015, 1283.69 sec so far
Iteration 68190 (of 85077): max relative diff=0.000015, 1288.70 sec so far
Iteration 68456 (of 85077): max relative diff=0.000015, 1293.72 sec so far
Iteration 68722 (of 85077): max relative diff=0.000015, 1298.73 sec so far
Iteration 68988 (of 85077): max relative diff=0.000015, 1303.75 sec so far
Iteration 69254 (of 85077): max relative diff=0.000014, 1308.76 sec so far
Iteration 69520 (of 85077): max relative diff=0.000014, 1313.77 sec so far
Iteration 69786 (of 85077): max relative diff=0.000014, 1318.78 sec so far
Iteration 70052 (of 85077): max relative diff=0.000014, 1323.79 sec so far
Iteration 70317 (of 85077): max relative diff=0.000014, 1328.80 sec so far
Iteration 70584 (of 85077): max relative diff=0.000014, 1333.82 sec so far
Iteration 70850 (of 85077): max relative diff=0.000014, 1338.84 sec so far
Iteration 71116 (of 85077): max relative diff=0.000014, 1343.85 sec so far
Iteration 71382 (of 85077): max relative diff=0.000014, 1348.86 sec so far
Iteration 71648 (of 85077): max relative diff=0.000014, 1353.87 sec so far
Iteration 71914 (of 85077): max relative diff=0.000014, 1358.89 sec so far
Iteration 72180 (of 85077): max relative diff=0.000014, 1363.90 sec so far
Iteration 72446 (of 85077): max relative diff=0.000014, 1368.91 sec so far
Iteration 72712 (of 85077): max relative diff=0.000014, 1373.92 sec so far
Iteration 72978 (of 85077): max relative diff=0.000014, 1378.94 sec so far
Iteration 73244 (of 85077): max relative diff=0.000014, 1383.95 sec so far
Iteration 73510 (of 85077): max relative diff=0.000014, 1388.96 sec so far
Iteration 73776 (of 85077): max relative diff=0.000014, 1393.97 sec so far
Iteration 74042 (of 85077): max relative diff=0.000014, 1398.99 sec so far
Iteration 74308 (of 85077): max relative diff=0.000013, 1404.00 sec so far
Iteration 74574 (of 85077): max relative diff=0.000013, 1409.02 sec so far
Iteration 74840 (of 85077): max relative diff=0.000013, 1414.04 sec so far
Iteration 75106 (of 85077): max relative diff=0.000013, 1419.05 sec so far
Iteration 75372 (of 85077): max relative diff=0.000013, 1424.06 sec so far
Iteration 75638 (of 85077): max relative diff=0.000013, 1429.07 sec so far
Iteration 75904 (of 85077): max relative diff=0.000013, 1434.09 sec so far
Iteration 76170 (of 85077): max relative diff=0.000013, 1439.10 sec so far
Iteration 76436 (of 85077): max relative diff=0.000013, 1444.12 sec so far
Iteration 76702 (of 85077): max relative diff=0.000013, 1449.13 sec so far
Iteration 76968 (of 85077): max relative diff=0.000013, 1454.14 sec so far
Iteration 77234 (of 85077): max relative diff=0.000013, 1459.16 sec so far
Iteration 77500 (of 85077): max relative diff=0.000013, 1464.17 sec so far
Iteration 77766 (of 85077): max relative diff=0.000013, 1469.18 sec so far
Iteration 78032 (of 85077): max relative diff=0.000013, 1474.20 sec so far
Iteration 78298 (of 85077): max relative diff=0.000013, 1479.21 sec so far
Iteration 78564 (of 85077): max relative diff=0.000013, 1484.22 sec so far
Iteration 78830 (of 85077): max relative diff=0.000013, 1489.24 sec so far
Iteration 79096 (of 85077): max relative diff=0.000013, 1494.25 sec so far
Iteration 79362 (of 85077): max relative diff=0.000013, 1499.26 sec so far
Iteration 79628 (of 85077): max relative diff=0.000013, 1504.28 sec so far
Iteration 79894 (of 85077): max relative diff=0.000013, 1509.29 sec so far
Iteration 80161 (of 85077): max relative diff=0.000012, 1514.31 sec so far
Iteration 80427 (of 85077): max relative diff=0.000012, 1519.33 sec so far
Iteration 80689 (of 85077): max relative diff=0.000012, 1524.35 sec so far
Iteration 80940 (of 85077): max relative diff=0.000012, 1529.37 sec so far
Iteration 81190 (of 85077): max relative diff=0.000012, 1534.38 sec so far
Iteration 81440 (of 85077): max relative diff=0.000012, 1539.39 sec so far
Iteration 81690 (of 85077): max relative diff=0.000012, 1544.40 sec so far
Iteration 81940 (of 85077): max relative diff=0.000012, 1549.41 sec so far
Iteration 82190 (of 85077): max relative diff=0.000012, 1554.42 sec so far
Iteration 82440 (of 85077): max relative diff=0.000012, 1559.43 sec so far
Iteration 82690 (of 85077): max relative diff=0.000012, 1564.44 sec so far
Iteration 82940 (of 85077): max relative diff=0.000012, 1569.45 sec so far
Iteration 83191 (of 85077): max relative diff=0.000012, 1574.47 sec so far
Iteration 83441 (of 85077): max relative diff=0.000012, 1579.48 sec so far
Iteration 83691 (of 85077): max relative diff=0.000012, 1584.49 sec so far
Iteration 83941 (of 85077): max relative diff=0.000012, 1589.50 sec so far
Iteration 84192 (of 85077): max relative diff=0.000012, 1594.52 sec so far
Iteration 84443 (of 85077): max relative diff=0.000012, 1599.54 sec so far
Iteration 84694 (of 85077): max relative diff=0.000012, 1604.57 sec so far
Iteration 84944 (of 85077): max relative diff=0.000012, 1609.58 sec so far

Iterative method: 85077 iterations in 1613.44 seconds (average 0.018950, setup 1.20)

Value in the initial state: 0.001072402533769736

Time for model checking: 1625.265 seconds.

Result: 0.001072402533769736


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

