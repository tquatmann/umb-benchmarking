# Log files

Tool configuration: prism_from-umb_check_default
Benchmark: [cluster.128-2000-20](../../models/cluster.128-2000-20)
Parsed values: [134.034, 308.914, 126.014, 120.504, 188.195]



### Log file: prism_from-umb_check_default_cluster.128-2000-20_rep1.log

```
Command(s):
../bin/prism  -importmodel models/cluster.128-2000-20/prism.model.umb models/cluster.128-2000-20/property.props
Wallclock time: 863.383 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 08:03:39 GMT+01:00 2026
Hostname: r23m0062.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/cluster.128-2000-20/prism.model.umb models/cluster.128-2000-20/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   x
Labels:      "minimum"

Parsing properties file "models/cluster.128-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 10% 12% 14% 16% 20% 22% 24% 26% 28% 30% 34% 36% 38% 40% 42% 44% 46% 48% 50% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 100% ]

Computing reachable states...

Reachability (BFS): 261 iterations in 1.09 seconds (average 0.004176, setup 0.00)

Time for model construction: 134.034 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 57334 nodes (134 terminal), 2908192 minterms, vars: 20r/20c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 141117 of 597012 (23.6%)

Building hybrid MTBDD matrix... [levels=20, nodes=124622] [5.7 MB]
Adding explicit sparse matrices... [levels=5, num=7348, compact] [671.9 KB]
Creating vector for diagonals... [dist=3024, compact] [1.2 MB]
Allocating iteration vectors... [3 x 4.6 MB]
TOTAL: [21.2 MB]

Uniformisation: q.t = 41.318415 x 2000.000000 = 82636.830000
Fox-Glynn: left = 80621, right = 85077

Starting iterations...
Iteration 600 (of 85077): max relative diff=0.010963, 5.01 sec so far
Iteration 1192 (of 85077): max relative diff=0.004882, 10.02 sec so far
Iteration 1792 (of 85077): max relative diff=0.002500, 15.04 sec so far
Iteration 2395 (of 85077): max relative diff=0.001192, 20.05 sec so far
Iteration 2977 (of 85077): max relative diff=0.000552, 25.06 sec so far
Iteration 3568 (of 85077): max relative diff=0.000294, 30.07 sec so far
Iteration 4156 (of 85077): max relative diff=0.000251, 35.08 sec so far
Iteration 4751 (of 85077): max relative diff=0.000218, 40.09 sec so far
Iteration 5340 (of 85077): max relative diff=0.000193, 45.10 sec so far
Iteration 5941 (of 85077): max relative diff=0.000173, 50.11 sec so far
Iteration 6542 (of 85077): max relative diff=0.000157, 55.12 sec so far
Iteration 7120 (of 85077): max relative diff=0.000144, 60.13 sec so far
Iteration 7711 (of 85077): max relative diff=0.000133, 65.14 sec so far
Iteration 8297 (of 85077): max relative diff=0.000123, 70.15 sec so far
Iteration 8895 (of 85077): max relative diff=0.000115, 75.16 sec so far
Iteration 9484 (of 85077): max relative diff=0.000107, 80.17 sec so far
Iteration 10089 (of 85077): max relative diff=0.000101, 85.18 sec so far
Iteration 10689 (of 85077): max relative diff=0.000095, 90.19 sec so far
Iteration 11283 (of 85077): max relative diff=0.000090, 95.20 sec so far
Iteration 11881 (of 85077): max relative diff=0.000085, 100.21 sec so far
Iteration 12474 (of 85077): max relative diff=0.000081, 105.22 sec so far
Iteration 13072 (of 85077): max relative diff=0.000078, 110.23 sec so far
Iteration 13676 (of 85077): max relative diff=0.000074, 115.24 sec so far
Iteration 14259 (of 85077): max relative diff=0.000071, 120.25 sec so far
Iteration 14852 (of 85077): max relative diff=0.000068, 125.26 sec so far
Iteration 15450 (of 85077): max relative diff=0.000065, 130.27 sec so far
Iteration 16041 (of 85077): max relative diff=0.000063, 135.28 sec so far
Iteration 16640 (of 85077): max relative diff=0.000061, 140.29 sec so far
Iteration 17239 (of 85077): max relative diff=0.000059, 145.30 sec so far
Iteration 17823 (of 85077): max relative diff=0.000057, 150.31 sec so far
Iteration 18422 (of 85077): max relative diff=0.000055, 155.32 sec so far
Iteration 19015 (of 85077): max relative diff=0.000053, 160.33 sec so far
Iteration 19615 (of 85077): max relative diff=0.000051, 165.34 sec so far
Iteration 20211 (of 85077): max relative diff=0.000050, 170.35 sec so far
Iteration 20810 (of 85077): max relative diff=0.000048, 175.36 sec so far
Iteration 21406 (of 85077): max relative diff=0.000047, 180.37 sec so far
Iteration 22004 (of 85077): max relative diff=0.000046, 185.38 sec so far
Iteration 22591 (of 85077): max relative diff=0.000045, 190.39 sec so far
Iteration 23190 (of 85077): max relative diff=0.000043, 195.40 sec so far
Iteration 23787 (of 85077): max relative diff=0.000042, 200.41 sec so far
Iteration 24384 (of 85077): max relative diff=0.000041, 205.42 sec so far
Iteration 24987 (of 85077): max relative diff=0.000040, 210.43 sec so far
Iteration 25587 (of 85077): max relative diff=0.000039, 215.44 sec so far
Iteration 26180 (of 85077): max relative diff=0.000038, 220.45 sec so far
Iteration 26776 (of 85077): max relative diff=0.000038, 225.46 sec so far
Iteration 27374 (of 85077): max relative diff=0.000037, 230.47 sec so far
Iteration 27972 (of 85077): max relative diff=0.000036, 235.48 sec so far
Iteration 28557 (of 85077): max relative diff=0.000035, 240.49 sec so far
Iteration 29158 (of 85077): max relative diff=0.000034, 245.50 sec so far
Iteration 29754 (of 85077): max relative diff=0.000034, 250.51 sec so far
Iteration 30347 (of 85077): max relative diff=0.000033, 255.52 sec so far
Iteration 30940 (of 85077): max relative diff=0.000032, 260.53 sec so far
Iteration 31530 (of 85077): max relative diff=0.000032, 265.54 sec so far
Iteration 32117 (of 85077): max relative diff=0.000031, 270.55 sec so far
Iteration 32721 (of 85077): max relative diff=0.000031, 275.57 sec so far
Iteration 33321 (of 85077): max relative diff=0.000030, 280.58 sec so far
Iteration 33912 (of 85077): max relative diff=0.000030, 285.59 sec so far
Iteration 34511 (of 85077): max relative diff=0.000029, 290.60 sec so far
Iteration 35109 (of 85077): max relative diff=0.000029, 295.61 sec so far
Iteration 35697 (of 85077): max relative diff=0.000028, 300.62 sec so far
Iteration 36297 (of 85077): max relative diff=0.000028, 305.63 sec so far
Iteration 36902 (of 85077): max relative diff=0.000027, 310.64 sec so far
Iteration 37493 (of 85077): max relative diff=0.000027, 315.65 sec so far
Iteration 38093 (of 85077): max relative diff=0.000026, 320.66 sec so far
Iteration 38687 (of 85077): max relative diff=0.000026, 325.67 sec so far
Iteration 39280 (of 85077): max relative diff=0.000026, 330.68 sec so far
Iteration 39874 (of 85077): max relative diff=0.000025, 335.69 sec so far
Iteration 40478 (of 85077): max relative diff=0.000025, 340.70 sec so far
Iteration 41073 (of 85077): max relative diff=0.000024, 345.71 sec so far
Iteration 41664 (of 85077): max relative diff=0.000024, 350.72 sec so far
Iteration 42268 (of 85077): max relative diff=0.000024, 355.73 sec so far
Iteration 42855 (of 85077): max relative diff=0.000023, 360.75 sec so far
Iteration 43456 (of 85077): max relative diff=0.000023, 365.76 sec so far
Iteration 44044 (of 85077): max relative diff=0.000023, 370.77 sec so far
Iteration 44641 (of 85077): max relative diff=0.000022, 375.78 sec so far
Iteration 45237 (of 85077): max relative diff=0.000022, 380.79 sec so far
Iteration 45833 (of 85077): max relative diff=0.000022, 385.80 sec so far
Iteration 46428 (of 85077): max relative diff=0.000022, 390.81 sec so far
Iteration 47024 (of 85077): max relative diff=0.000021, 395.82 sec so far
Iteration 47620 (of 85077): max relative diff=0.000021, 400.83 sec so far
Iteration 48225 (of 85077): max relative diff=0.000021, 405.84 sec so far
Iteration 48818 (of 85077): max relative diff=0.000021, 410.85 sec so far
Iteration 49421 (of 85077): max relative diff=0.000020, 415.86 sec so far
Iteration 50003 (of 85077): max relative diff=0.000020, 420.87 sec so far
Iteration 50597 (of 85077): max relative diff=0.000020, 425.88 sec so far
Iteration 51188 (of 85077): max relative diff=0.000020, 430.89 sec so far
Iteration 51791 (of 85077): max relative diff=0.000019, 435.90 sec so far
Iteration 52397 (of 85077): max relative diff=0.000019, 440.91 sec so far
Iteration 52989 (of 85077): max relative diff=0.000019, 445.92 sec so far
Iteration 53584 (of 85077): max relative diff=0.000019, 450.93 sec so far
Iteration 54180 (of 85077): max relative diff=0.000019, 455.94 sec so far
Iteration 54779 (of 85077): max relative diff=0.000018, 460.95 sec so far
Iteration 55380 (of 85077): max relative diff=0.000018, 465.96 sec so far
Iteration 55980 (of 85077): max relative diff=0.000018, 470.97 sec so far
Iteration 56577 (of 85077): max relative diff=0.000018, 475.98 sec so far
Iteration 57173 (of 85077): max relative diff=0.000018, 480.99 sec so far
Iteration 57761 (of 85077): max relative diff=0.000017, 486.00 sec so far
Iteration 58362 (of 85077): max relative diff=0.000017, 491.01 sec so far
Iteration 58952 (of 85077): max relative diff=0.000017, 496.02 sec so far
Iteration 59560 (of 85077): max relative diff=0.000017, 501.04 sec so far
Iteration 60157 (of 85077): max relative diff=0.000017, 506.05 sec so far
Iteration 60751 (of 85077): max relative diff=0.000017, 511.06 sec so far
Iteration 61349 (of 85077): max relative diff=0.000016, 516.07 sec so far
Iteration 61943 (of 85077): max relative diff=0.000016, 521.08 sec so far
Iteration 62540 (of 85077): max relative diff=0.000016, 526.10 sec so far
Iteration 63145 (of 85077): max relative diff=0.000016, 531.11 sec so far
Iteration 63739 (of 85077): max relative diff=0.000016, 536.12 sec so far
Iteration 64336 (of 85077): max relative diff=0.000016, 541.13 sec so far
Iteration 64927 (of 85077): max relative diff=0.000015, 546.14 sec so far
Iteration 65528 (of 85077): max relative diff=0.000015, 551.15 sec so far
Iteration 66122 (of 85077): max relative diff=0.000015, 556.16 sec so far
Iteration 66717 (of 85077): max relative diff=0.000015, 561.17 sec so far
Iteration 67323 (of 85077): max relative diff=0.000015, 566.18 sec so far
Iteration 67915 (of 85077): max relative diff=0.000015, 571.19 sec so far
Iteration 68508 (of 85077): max relative diff=0.000015, 576.20 sec so far
Iteration 69110 (of 85077): max relative diff=0.000014, 581.21 sec so far
Iteration 69709 (of 85077): max relative diff=0.000014, 586.22 sec so far
Iteration 70306 (of 85077): max relative diff=0.000014, 591.23 sec so far
Iteration 70906 (of 85077): max relative diff=0.000014, 596.24 sec so far
Iteration 71505 (of 85077): max relative diff=0.000014, 601.25 sec so far
Iteration 72092 (of 85077): max relative diff=0.000014, 606.26 sec so far
Iteration 72691 (of 85077): max relative diff=0.000014, 611.27 sec so far
Iteration 73285 (of 85077): max relative diff=0.000014, 616.28 sec so far
Iteration 73881 (of 85077): max relative diff=0.000014, 621.29 sec so far
Iteration 74482 (of 85077): max relative diff=0.000013, 626.30 sec so far
Iteration 75084 (of 85077): max relative diff=0.000013, 631.31 sec so far
Iteration 75675 (of 85077): max relative diff=0.000013, 636.32 sec so far
Iteration 76277 (of 85077): max relative diff=0.000013, 641.33 sec so far
Iteration 76876 (of 85077): max relative diff=0.000013, 646.34 sec so far
Iteration 77473 (of 85077): max relative diff=0.000013, 651.35 sec so far
Iteration 78064 (of 85077): max relative diff=0.000013, 656.36 sec so far
Iteration 78663 (of 85077): max relative diff=0.000013, 661.38 sec so far
Iteration 79260 (of 85077): max relative diff=0.000013, 666.39 sec so far
Iteration 79855 (of 85077): max relative diff=0.000013, 671.40 sec so far
Iteration 80454 (of 85077): max relative diff=0.000012, 676.41 sec so far
Iteration 81021 (of 85077): max relative diff=0.000012, 681.42 sec so far
Iteration 81572 (of 85077): max relative diff=0.000012, 686.43 sec so far
Iteration 82140 (of 85077): max relative diff=0.000012, 691.44 sec so far
Iteration 82698 (of 85077): max relative diff=0.000012, 696.45 sec so far
Iteration 83258 (of 85077): max relative diff=0.000012, 701.46 sec so far
Iteration 83815 (of 85077): max relative diff=0.000012, 706.47 sec so far
Iteration 84373 (of 85077): max relative diff=0.000012, 711.48 sec so far
Iteration 84925 (of 85077): max relative diff=0.000012, 716.49 sec so far

Iterative method: 85077 iterations in 726.65 seconds (average 0.008439, setup 8.67)

Value in the initial state: 0.001072402533769736

Time for model checking: 728.67 seconds.

Result: 0.001072402533769736


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_cluster.128-2000-20_rep2.log

```
Command(s):
../bin/prism  -importmodel models/cluster.128-2000-20/prism.model.umb models/cluster.128-2000-20/property.props
Wallclock time: 1576.901 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:28:12 GMT+01:00 2026
Hostname: n23m0275.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/cluster.128-2000-20/prism.model.umb models/cluster.128-2000-20/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   x
Labels:      "minimum"

Parsing properties file "models/cluster.128-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 261 iterations in 2.26 seconds (average 0.008659, setup 0.00)

Time for model construction: 308.914 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 57334 nodes (134 terminal), 2908192 minterms, vars: 20r/20c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 141117 of 597012 (23.6%)

Building hybrid MTBDD matrix... [levels=20, nodes=124622] [5.7 MB]
Adding explicit sparse matrices... [levels=5, num=7348, compact] [671.9 KB]
Creating vector for diagonals... [dist=3024, compact] [1.2 MB]
Allocating iteration vectors... [3 x 4.6 MB]
TOTAL: [21.2 MB]

Uniformisation: q.t = 41.318415 x 2000.000000 = 82636.830000
Fox-Glynn: left = 80621, right = 85077

Starting iterations...
Iteration 330 (of 85077): max relative diff=0.018921, 5.02 sec so far
Iteration 662 (of 85077): max relative diff=0.009759, 10.03 sec so far
Iteration 992 (of 85077): max relative diff=0.006202, 15.04 sec so far
Iteration 1321 (of 85077): max relative diff=0.004262, 20.05 sec so far
Iteration 1653 (of 85077): max relative diff=0.002895, 25.06 sec so far
Iteration 1982 (of 85077): max relative diff=0.001997, 30.07 sec so far
Iteration 2313 (of 85077): max relative diff=0.001335, 35.08 sec so far
Iteration 2649 (of 85077): max relative diff=0.000853, 40.09 sec so far
Iteration 2980 (of 85077): max relative diff=0.000550, 45.10 sec so far
Iteration 3312 (of 85077): max relative diff=0.000370, 50.12 sec so far
Iteration 3646 (of 85077): max relative diff=0.000288, 55.13 sec so far
Iteration 3975 (of 85077): max relative diff=0.000263, 60.14 sec so far
Iteration 4308 (of 85077): max relative diff=0.000242, 65.15 sec so far
Iteration 4638 (of 85077): max relative diff=0.000224, 70.17 sec so far
Iteration 4969 (of 85077): max relative diff=0.000208, 75.18 sec so far
Iteration 5301 (of 85077): max relative diff=0.000195, 80.19 sec so far
Iteration 5632 (of 85077): max relative diff=0.000183, 85.20 sec so far
Iteration 5962 (of 85077): max relative diff=0.000173, 90.21 sec so far
Iteration 6294 (of 85077): max relative diff=0.000163, 95.22 sec so far
Iteration 6624 (of 85077): max relative diff=0.000155, 100.23 sec so far
Iteration 6959 (of 85077): max relative diff=0.000147, 105.25 sec so far
Iteration 7291 (of 85077): max relative diff=0.000140, 110.26 sec so far
Iteration 7621 (of 85077): max relative diff=0.000134, 115.27 sec so far
Iteration 7955 (of 85077): max relative diff=0.000128, 120.28 sec so far
Iteration 8283 (of 85077): max relative diff=0.000123, 125.29 sec so far
Iteration 8615 (of 85077): max relative diff=0.000118, 130.30 sec so far
Iteration 8947 (of 85077): max relative diff=0.000114, 135.31 sec so far
Iteration 9275 (of 85077): max relative diff=0.000110, 140.32 sec so far
Iteration 9607 (of 85077): max relative diff=0.000106, 145.33 sec so far
Iteration 9935 (of 85077): max relative diff=0.000102, 150.34 sec so far
Iteration 10266 (of 85077): max relative diff=0.000099, 155.35 sec so far
Iteration 10599 (of 85077): max relative diff=0.000096, 160.37 sec so far
Iteration 10932 (of 85077): max relative diff=0.000093, 165.39 sec so far
Iteration 11265 (of 85077): max relative diff=0.000090, 170.40 sec so far
Iteration 11600 (of 85077): max relative diff=0.000087, 175.41 sec so far
Iteration 11929 (of 85077): max relative diff=0.000085, 180.42 sec so far
Iteration 12263 (of 85077): max relative diff=0.000083, 185.44 sec so far
Iteration 12593 (of 85077): max relative diff=0.000080, 190.45 sec so far
Iteration 12924 (of 85077): max relative diff=0.000078, 195.47 sec so far
Iteration 13254 (of 85077): max relative diff=0.000076, 200.48 sec so far
Iteration 13585 (of 85077): max relative diff=0.000075, 205.49 sec so far
Iteration 13917 (of 85077): max relative diff=0.000073, 210.51 sec so far
Iteration 14250 (of 85077): max relative diff=0.000071, 215.52 sec so far
Iteration 14578 (of 85077): max relative diff=0.000069, 220.53 sec so far
Iteration 14913 (of 85077): max relative diff=0.000068, 225.55 sec so far
Iteration 15245 (of 85077): max relative diff=0.000066, 230.57 sec so far
Iteration 15576 (of 85077): max relative diff=0.000065, 235.58 sec so far
Iteration 15910 (of 85077): max relative diff=0.000064, 240.59 sec so far
Iteration 16240 (of 85077): max relative diff=0.000062, 245.60 sec so far
Iteration 16571 (of 85077): max relative diff=0.000061, 250.62 sec so far
Iteration 16904 (of 85077): max relative diff=0.000060, 255.64 sec so far
Iteration 17229 (of 85077): max relative diff=0.000059, 260.65 sec so far
Iteration 17566 (of 85077): max relative diff=0.000057, 265.67 sec so far
Iteration 17896 (of 85077): max relative diff=0.000056, 270.69 sec so far
Iteration 18225 (of 85077): max relative diff=0.000055, 275.71 sec so far
Iteration 18561 (of 85077): max relative diff=0.000054, 280.72 sec so far
Iteration 18894 (of 85077): max relative diff=0.000053, 285.73 sec so far
Iteration 19227 (of 85077): max relative diff=0.000052, 290.74 sec so far
Iteration 19564 (of 85077): max relative diff=0.000052, 295.75 sec so far
Iteration 19891 (of 85077): max relative diff=0.000051, 300.76 sec so far
Iteration 20227 (of 85077): max relative diff=0.000050, 305.78 sec so far
Iteration 20558 (of 85077): max relative diff=0.000049, 310.79 sec so far
Iteration 20892 (of 85077): max relative diff=0.000048, 315.80 sec so far
Iteration 21223 (of 85077): max relative diff=0.000047, 320.81 sec so far
Iteration 21554 (of 85077): max relative diff=0.000047, 325.82 sec so far
Iteration 21884 (of 85077): max relative diff=0.000046, 330.84 sec so far
Iteration 22219 (of 85077): max relative diff=0.000045, 335.85 sec so far
Iteration 22548 (of 85077): max relative diff=0.000045, 340.86 sec so far
Iteration 22883 (of 85077): max relative diff=0.000044, 345.87 sec so far
Iteration 23213 (of 85077): max relative diff=0.000043, 350.88 sec so far
Iteration 23541 (of 85077): max relative diff=0.000043, 355.89 sec so far
Iteration 23876 (of 85077): max relative diff=0.000042, 360.91 sec so far
Iteration 24208 (of 85077): max relative diff=0.000042, 365.93 sec so far
Iteration 24541 (of 85077): max relative diff=0.000041, 370.95 sec so far
Iteration 24875 (of 85077): max relative diff=0.000040, 375.96 sec so far
Iteration 25200 (of 85077): max relative diff=0.000040, 380.97 sec so far
Iteration 25534 (of 85077): max relative diff=0.000039, 385.98 sec so far
Iteration 25862 (of 85077): max relative diff=0.000039, 390.99 sec so far
Iteration 26191 (of 85077): max relative diff=0.000038, 396.00 sec so far
Iteration 26527 (of 85077): max relative diff=0.000038, 401.01 sec so far
Iteration 26857 (of 85077): max relative diff=0.000037, 406.02 sec so far
Iteration 27187 (of 85077): max relative diff=0.000037, 411.03 sec so far
Iteration 27521 (of 85077): max relative diff=0.000037, 416.04 sec so far
Iteration 27850 (of 85077): max relative diff=0.000036, 421.05 sec so far
Iteration 28182 (of 85077): max relative diff=0.000036, 426.06 sec so far
Iteration 28515 (of 85077): max relative diff=0.000035, 431.07 sec so far
Iteration 28844 (of 85077): max relative diff=0.000035, 436.08 sec so far
Iteration 29175 (of 85077): max relative diff=0.000034, 441.09 sec so far
Iteration 29504 (of 85077): max relative diff=0.000034, 446.10 sec so far
Iteration 29833 (of 85077): max relative diff=0.000034, 451.11 sec so far
Iteration 30165 (of 85077): max relative diff=0.000033, 456.12 sec so far
Iteration 30495 (of 85077): max relative diff=0.000033, 461.14 sec so far
Iteration 30828 (of 85077): max relative diff=0.000033, 466.15 sec so far
Iteration 31156 (of 85077): max relative diff=0.000032, 471.16 sec so far
Iteration 31486 (of 85077): max relative diff=0.000032, 476.17 sec so far
Iteration 31820 (of 85077): max relative diff=0.000032, 481.18 sec so far
Iteration 32150 (of 85077): max relative diff=0.000031, 486.20 sec so far
Iteration 32482 (of 85077): max relative diff=0.000031, 491.21 sec so far
Iteration 32814 (of 85077): max relative diff=0.000031, 496.22 sec so far
Iteration 33141 (of 85077): max relative diff=0.000030, 501.23 sec so far
Iteration 33473 (of 85077): max relative diff=0.000030, 506.24 sec so far
Iteration 33805 (of 85077): max relative diff=0.000030, 511.25 sec so far
Iteration 34134 (of 85077): max relative diff=0.000029, 516.26 sec so far
Iteration 34468 (of 85077): max relative diff=0.000029, 521.27 sec so far
Iteration 34797 (of 85077): max relative diff=0.000029, 526.28 sec so far
Iteration 35126 (of 85077): max relative diff=0.000029, 531.29 sec so far
Iteration 35460 (of 85077): max relative diff=0.000028, 536.30 sec so far
Iteration 35787 (of 85077): max relative diff=0.000028, 541.31 sec so far
Iteration 36121 (of 85077): max relative diff=0.000028, 546.32 sec so far
Iteration 36450 (of 85077): max relative diff=0.000028, 551.33 sec so far
Iteration 36779 (of 85077): max relative diff=0.000027, 556.34 sec so far
Iteration 37111 (of 85077): max relative diff=0.000027, 561.36 sec so far
Iteration 37441 (of 85077): max relative diff=0.000027, 566.38 sec so far
Iteration 37773 (of 85077): max relative diff=0.000027, 571.40 sec so far
Iteration 38107 (of 85077): max relative diff=0.000026, 576.41 sec so far
Iteration 38434 (of 85077): max relative diff=0.000026, 581.42 sec so far
Iteration 38768 (of 85077): max relative diff=0.000026, 586.43 sec so far
Iteration 39099 (of 85077): max relative diff=0.000026, 591.45 sec so far
Iteration 39428 (of 85077): max relative diff=0.000025, 596.46 sec so far
Iteration 39760 (of 85077): max relative diff=0.000025, 601.47 sec so far
Iteration 40094 (of 85077): max relative diff=0.000025, 606.49 sec so far
Iteration 40426 (of 85077): max relative diff=0.000025, 611.50 sec so far
Iteration 40761 (of 85077): max relative diff=0.000025, 616.51 sec so far
Iteration 41091 (of 85077): max relative diff=0.000024, 621.52 sec so far
Iteration 41426 (of 85077): max relative diff=0.000024, 626.53 sec so far
Iteration 41760 (of 85077): max relative diff=0.000024, 631.54 sec so far
Iteration 42093 (of 85077): max relative diff=0.000024, 636.55 sec so far
Iteration 42427 (of 85077): max relative diff=0.000024, 641.57 sec so far
Iteration 42761 (of 85077): max relative diff=0.000023, 646.58 sec so far
Iteration 43095 (of 85077): max relative diff=0.000023, 651.59 sec so far
Iteration 43428 (of 85077): max relative diff=0.000023, 656.60 sec so far
Iteration 43762 (of 85077): max relative diff=0.000023, 661.61 sec so far
Iteration 44097 (of 85077): max relative diff=0.000023, 666.62 sec so far
Iteration 44430 (of 85077): max relative diff=0.000023, 671.63 sec so far
Iteration 44764 (of 85077): max relative diff=0.000022, 676.64 sec so far
Iteration 45094 (of 85077): max relative diff=0.000022, 681.65 sec so far
Iteration 45426 (of 85077): max relative diff=0.000022, 686.67 sec so far
Iteration 45760 (of 85077): max relative diff=0.000022, 691.69 sec so far
Iteration 46093 (of 85077): max relative diff=0.000022, 696.70 sec so far
Iteration 46428 (of 85077): max relative diff=0.000022, 701.72 sec so far
Iteration 46761 (of 85077): max relative diff=0.000021, 706.73 sec so far
Iteration 47097 (of 85077): max relative diff=0.000021, 711.74 sec so far
Iteration 47431 (of 85077): max relative diff=0.000021, 716.75 sec so far
Iteration 47766 (of 85077): max relative diff=0.000021, 721.77 sec so far
Iteration 48102 (of 85077): max relative diff=0.000021, 726.79 sec so far
Iteration 48436 (of 85077): max relative diff=0.000021, 731.80 sec so far
Iteration 48771 (of 85077): max relative diff=0.000021, 736.82 sec so far
Iteration 49103 (of 85077): max relative diff=0.000020, 741.83 sec so far
Iteration 49436 (of 85077): max relative diff=0.000020, 746.84 sec so far
Iteration 49768 (of 85077): max relative diff=0.000020, 751.85 sec so far
Iteration 50101 (of 85077): max relative diff=0.000020, 756.86 sec so far
Iteration 50434 (of 85077): max relative diff=0.000020, 761.87 sec so far
Iteration 50768 (of 85077): max relative diff=0.000020, 766.88 sec so far
Iteration 51104 (of 85077): max relative diff=0.000020, 771.90 sec so far
Iteration 51438 (of 85077): max relative diff=0.000019, 776.91 sec so far
Iteration 51771 (of 85077): max relative diff=0.000019, 781.92 sec so far
Iteration 52105 (of 85077): max relative diff=0.000019, 786.93 sec so far
Iteration 52438 (of 85077): max relative diff=0.000019, 791.95 sec so far
Iteration 52772 (of 85077): max relative diff=0.000019, 796.96 sec so far
Iteration 53104 (of 85077): max relative diff=0.000019, 801.97 sec so far
Iteration 53436 (of 85077): max relative diff=0.000019, 806.98 sec so far
Iteration 53771 (of 85077): max relative diff=0.000019, 812.00 sec so far
Iteration 54103 (of 85077): max relative diff=0.000019, 817.01 sec so far
Iteration 54438 (of 85077): max relative diff=0.000018, 822.02 sec so far
Iteration 54772 (of 85077): max relative diff=0.000018, 827.04 sec so far
Iteration 55105 (of 85077): max relative diff=0.000018, 832.06 sec so far
Iteration 55441 (of 85077): max relative diff=0.000018, 837.08 sec so far
Iteration 55776 (of 85077): max relative diff=0.000018, 842.09 sec so far
Iteration 56109 (of 85077): max relative diff=0.000018, 847.11 sec so far
Iteration 56444 (of 85077): max relative diff=0.000018, 852.13 sec so far
Iteration 56778 (of 85077): max relative diff=0.000018, 857.14 sec so far
Iteration 57109 (of 85077): max relative diff=0.000018, 862.15 sec so far
Iteration 57443 (of 85077): max relative diff=0.000017, 867.16 sec so far
Iteration 57777 (of 85077): max relative diff=0.000017, 872.18 sec so far
Iteration 58109 (of 85077): max relative diff=0.000017, 877.19 sec so far
Iteration 58444 (of 85077): max relative diff=0.000017, 882.21 sec so far
Iteration 58779 (of 85077): max relative diff=0.000017, 887.22 sec so far
Iteration 59145 (of 85077): max relative diff=0.000017, 892.23 sec so far
Iteration 59520 (of 85077): max relative diff=0.000017, 897.24 sec so far
Iteration 59896 (of 85077): max relative diff=0.000017, 902.25 sec so far
Iteration 60270 (of 85077): max relative diff=0.000017, 907.26 sec so far
Iteration 60645 (of 85077): max relative diff=0.000017, 912.27 sec so far
Iteration 61019 (of 85077): max relative diff=0.000016, 917.28 sec so far
Iteration 61390 (of 85077): max relative diff=0.000016, 922.30 sec so far
Iteration 61764 (of 85077): max relative diff=0.000016, 927.31 sec so far
Iteration 62138 (of 85077): max relative diff=0.000016, 932.32 sec so far
Iteration 62512 (of 85077): max relative diff=0.000016, 937.33 sec so far
Iteration 62883 (of 85077): max relative diff=0.000016, 942.35 sec so far
Iteration 63259 (of 85077): max relative diff=0.000016, 947.37 sec so far
Iteration 63633 (of 85077): max relative diff=0.000016, 952.38 sec so far
Iteration 64009 (of 85077): max relative diff=0.000016, 957.40 sec so far
Iteration 64383 (of 85077): max relative diff=0.000016, 962.41 sec so far
Iteration 64758 (of 85077): max relative diff=0.000015, 967.42 sec so far
Iteration 65124 (of 85077): max relative diff=0.000015, 972.43 sec so far
Iteration 65487 (of 85077): max relative diff=0.000015, 977.44 sec so far
Iteration 65853 (of 85077): max relative diff=0.000015, 982.46 sec so far
Iteration 66219 (of 85077): max relative diff=0.000015, 987.47 sec so far
Iteration 66591 (of 85077): max relative diff=0.000015, 992.48 sec so far
Iteration 66966 (of 85077): max relative diff=0.000015, 997.49 sec so far
Iteration 67336 (of 85077): max relative diff=0.000015, 1002.50 sec so far
Iteration 67710 (of 85077): max relative diff=0.000015, 1007.51 sec so far
Iteration 68086 (of 85077): max relative diff=0.000015, 1012.52 sec so far
Iteration 68460 (of 85077): max relative diff=0.000015, 1017.53 sec so far
Iteration 68834 (of 85077): max relative diff=0.000015, 1022.54 sec so far
Iteration 69211 (of 85077): max relative diff=0.000014, 1027.55 sec so far
Iteration 69585 (of 85077): max relative diff=0.000014, 1032.56 sec so far
Iteration 69954 (of 85077): max relative diff=0.000014, 1037.57 sec so far
Iteration 70326 (of 85077): max relative diff=0.000014, 1042.58 sec so far
Iteration 70699 (of 85077): max relative diff=0.000014, 1047.59 sec so far
Iteration 71071 (of 85077): max relative diff=0.000014, 1052.61 sec so far
Iteration 71445 (of 85077): max relative diff=0.000014, 1057.62 sec so far
Iteration 71819 (of 85077): max relative diff=0.000014, 1062.63 sec so far
Iteration 72193 (of 85077): max relative diff=0.000014, 1067.64 sec so far
Iteration 72567 (of 85077): max relative diff=0.000014, 1072.65 sec so far
Iteration 72941 (of 85077): max relative diff=0.000014, 1077.66 sec so far
Iteration 73315 (of 85077): max relative diff=0.000014, 1082.67 sec so far
Iteration 73692 (of 85077): max relative diff=0.000014, 1087.68 sec so far
Iteration 74067 (of 85077): max relative diff=0.000014, 1092.69 sec so far
Iteration 74437 (of 85077): max relative diff=0.000013, 1097.70 sec so far
Iteration 74814 (of 85077): max relative diff=0.000013, 1102.71 sec so far
Iteration 75189 (of 85077): max relative diff=0.000013, 1107.72 sec so far
Iteration 75565 (of 85077): max relative diff=0.000013, 1112.74 sec so far
Iteration 75942 (of 85077): max relative diff=0.000013, 1117.76 sec so far
Iteration 76316 (of 85077): max relative diff=0.000013, 1122.78 sec so far
Iteration 76688 (of 85077): max relative diff=0.000013, 1127.79 sec so far
Iteration 77062 (of 85077): max relative diff=0.000013, 1132.80 sec so far
Iteration 77436 (of 85077): max relative diff=0.000013, 1137.82 sec so far
Iteration 77810 (of 85077): max relative diff=0.000013, 1142.84 sec so far
Iteration 78184 (of 85077): max relative diff=0.000013, 1147.85 sec so far
Iteration 78554 (of 85077): max relative diff=0.000013, 1152.87 sec so far
Iteration 78920 (of 85077): max relative diff=0.000013, 1157.88 sec so far
Iteration 79293 (of 85077): max relative diff=0.000013, 1162.90 sec so far
Iteration 79666 (of 85077): max relative diff=0.000013, 1167.92 sec so far
Iteration 80042 (of 85077): max relative diff=0.000013, 1172.93 sec so far
Iteration 80416 (of 85077): max relative diff=0.000012, 1177.95 sec so far
Iteration 80779 (of 85077): max relative diff=0.000012, 1182.97 sec so far
Iteration 81125 (of 85077): max relative diff=0.000012, 1187.98 sec so far
Iteration 81474 (of 85077): max relative diff=0.000012, 1192.99 sec so far
Iteration 81822 (of 85077): max relative diff=0.000012, 1198.00 sec so far
Iteration 82170 (of 85077): max relative diff=0.000012, 1203.01 sec so far
Iteration 82519 (of 85077): max relative diff=0.000012, 1208.03 sec so far
Iteration 82867 (of 85077): max relative diff=0.000012, 1213.04 sec so far
Iteration 83209 (of 85077): max relative diff=0.000012, 1218.05 sec so far
Iteration 83558 (of 85077): max relative diff=0.000012, 1223.07 sec so far
Iteration 83907 (of 85077): max relative diff=0.000012, 1228.09 sec so far
Iteration 84255 (of 85077): max relative diff=0.000012, 1233.10 sec so far
Iteration 84603 (of 85077): max relative diff=0.000012, 1238.11 sec so far
Iteration 84951 (of 85077): max relative diff=0.000012, 1243.12 sec so far

Iterative method: 85077 iterations in 1263.20 seconds (average 0.014633, setup 18.28)

Value in the initial state: 0.001072402533769736

Time for model checking: 1267.054 seconds.

Result: 0.001072402533769736


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_cluster.128-2000-20_rep3.log

```
Command(s):
../bin/prism  -importmodel models/cluster.128-2000-20/prism.model.umb models/cluster.128-2000-20/property.props
Wallclock time: 786.007 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:07:30 GMT+01:00 2026
Hostname: n23m0237.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/cluster.128-2000-20/prism.model.umb models/cluster.128-2000-20/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   x
Labels:      "minimum"

Parsing properties file "models/cluster.128-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 8% 10% 12% 16% 18% 20% 24% 26% 28% 30% 32% 36% 38% 40% 42% 44% 46% 50% 52% 54% 56% 58% 60% 64% 66% 68% 70% 72% 74% 76% 80% 82% 84% 86% 88% 90% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 261 iterations in 0.98 seconds (average 0.003755, setup 0.00)

Time for model construction: 126.014 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 57334 nodes (134 terminal), 2908192 minterms, vars: 20r/20c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 141117 of 597012 (23.6%)

Building hybrid MTBDD matrix... [levels=20, nodes=124622] [5.7 MB]
Adding explicit sparse matrices... [levels=5, num=7348, compact] [671.9 KB]
Creating vector for diagonals... [dist=3024, compact] [1.2 MB]
Allocating iteration vectors... [3 x 4.6 MB]
TOTAL: [21.2 MB]

Uniformisation: q.t = 41.318415 x 2000.000000 = 82636.830000
Fox-Glynn: left = 80621, right = 85077

Starting iterations...
Iteration 660 (of 85077): max relative diff=0.009778, 5.01 sec so far
Iteration 1320 (of 85077): max relative diff=0.004267, 10.02 sec so far
Iteration 1976 (of 85077): max relative diff=0.002009, 15.03 sec so far
Iteration 2630 (of 85077): max relative diff=0.000878, 20.04 sec so far
Iteration 3284 (of 85077): max relative diff=0.000382, 25.05 sec so far
Iteration 3943 (of 85077): max relative diff=0.000265, 30.06 sec so far
Iteration 4603 (of 85077): max relative diff=0.000226, 35.07 sec so far
Iteration 5262 (of 85077): max relative diff=0.000196, 40.08 sec so far
Iteration 5921 (of 85077): max relative diff=0.000174, 45.09 sec so far
Iteration 6581 (of 85077): max relative diff=0.000156, 50.10 sec so far
Iteration 7241 (of 85077): max relative diff=0.000141, 55.11 sec so far
Iteration 7901 (of 85077): max relative diff=0.000129, 60.12 sec so far
Iteration 8561 (of 85077): max relative diff=0.000119, 65.13 sec so far
Iteration 9220 (of 85077): max relative diff=0.000111, 70.14 sec so far
Iteration 9878 (of 85077): max relative diff=0.000103, 75.15 sec so far
Iteration 10533 (of 85077): max relative diff=0.000097, 80.16 sec so far
Iteration 11188 (of 85077): max relative diff=0.000091, 85.17 sec so far
Iteration 11847 (of 85077): max relative diff=0.000086, 90.18 sec so far
Iteration 12508 (of 85077): max relative diff=0.000081, 95.19 sec so far
Iteration 13168 (of 85077): max relative diff=0.000077, 100.20 sec so far
Iteration 13827 (of 85077): max relative diff=0.000073, 105.21 sec so far
Iteration 14487 (of 85077): max relative diff=0.000070, 110.22 sec so far
Iteration 15146 (of 85077): max relative diff=0.000067, 115.23 sec so far
Iteration 15806 (of 85077): max relative diff=0.000064, 120.24 sec so far
Iteration 16466 (of 85077): max relative diff=0.000061, 125.25 sec so far
Iteration 17125 (of 85077): max relative diff=0.000059, 130.26 sec so far
Iteration 17782 (of 85077): max relative diff=0.000057, 135.27 sec so far
Iteration 18440 (of 85077): max relative diff=0.000055, 140.28 sec so far
Iteration 19095 (of 85077): max relative diff=0.000053, 145.29 sec so far
Iteration 19755 (of 85077): max relative diff=0.000051, 150.30 sec so far
Iteration 20415 (of 85077): max relative diff=0.000049, 155.31 sec so far
Iteration 21074 (of 85077): max relative diff=0.000048, 160.32 sec so far
Iteration 21734 (of 85077): max relative diff=0.000046, 165.33 sec so far
Iteration 22394 (of 85077): max relative diff=0.000045, 170.34 sec so far
Iteration 23053 (of 85077): max relative diff=0.000044, 175.35 sec so far
Iteration 23713 (of 85077): max relative diff=0.000042, 180.36 sec so far
Iteration 24373 (of 85077): max relative diff=0.000041, 185.37 sec so far
Iteration 25033 (of 85077): max relative diff=0.000040, 190.38 sec so far
Iteration 25690 (of 85077): max relative diff=0.000039, 195.39 sec so far
Iteration 26347 (of 85077): max relative diff=0.000038, 200.40 sec so far
Iteration 27003 (of 85077): max relative diff=0.000037, 205.41 sec so far
Iteration 27662 (of 85077): max relative diff=0.000036, 210.42 sec so far
Iteration 28321 (of 85077): max relative diff=0.000036, 215.43 sec so far
Iteration 28982 (of 85077): max relative diff=0.000035, 220.44 sec so far
Iteration 29641 (of 85077): max relative diff=0.000034, 225.45 sec so far
Iteration 30300 (of 85077): max relative diff=0.000033, 230.46 sec so far
Iteration 30960 (of 85077): max relative diff=0.000032, 235.47 sec so far
Iteration 31619 (of 85077): max relative diff=0.000032, 240.48 sec so far
Iteration 32278 (of 85077): max relative diff=0.000031, 245.49 sec so far
Iteration 32938 (of 85077): max relative diff=0.000031, 250.50 sec so far
Iteration 33593 (of 85077): max relative diff=0.000030, 255.51 sec so far
Iteration 34248 (of 85077): max relative diff=0.000029, 260.52 sec so far
Iteration 34904 (of 85077): max relative diff=0.000029, 265.53 sec so far
Iteration 35564 (of 85077): max relative diff=0.000028, 270.54 sec so far
Iteration 36224 (of 85077): max relative diff=0.000028, 275.55 sec so far
Iteration 36883 (of 85077): max relative diff=0.000027, 280.56 sec so far
Iteration 37543 (of 85077): max relative diff=0.000027, 285.57 sec so far
Iteration 38203 (of 85077): max relative diff=0.000026, 290.58 sec so far
Iteration 38863 (of 85077): max relative diff=0.000026, 295.59 sec so far
Iteration 39523 (of 85077): max relative diff=0.000025, 300.60 sec so far
Iteration 40182 (of 85077): max relative diff=0.000025, 305.61 sec so far
Iteration 40842 (of 85077): max relative diff=0.000025, 310.62 sec so far
Iteration 41497 (of 85077): max relative diff=0.000024, 315.63 sec so far
Iteration 42154 (of 85077): max relative diff=0.000024, 320.64 sec so far
Iteration 42810 (of 85077): max relative diff=0.000023, 325.65 sec so far
Iteration 43468 (of 85077): max relative diff=0.000023, 330.66 sec so far
Iteration 44128 (of 85077): max relative diff=0.000023, 335.67 sec so far
Iteration 44788 (of 85077): max relative diff=0.000022, 340.68 sec so far
Iteration 45447 (of 85077): max relative diff=0.000022, 345.69 sec so far
Iteration 46107 (of 85077): max relative diff=0.000022, 350.70 sec so far
Iteration 46767 (of 85077): max relative diff=0.000021, 355.71 sec so far
Iteration 47427 (of 85077): max relative diff=0.000021, 360.72 sec so far
Iteration 48086 (of 85077): max relative diff=0.000021, 365.73 sec so far
Iteration 48745 (of 85077): max relative diff=0.000021, 370.74 sec so far
Iteration 49400 (of 85077): max relative diff=0.000020, 375.75 sec so far
Iteration 50056 (of 85077): max relative diff=0.000020, 380.76 sec so far
Iteration 50713 (of 85077): max relative diff=0.000020, 385.77 sec so far
Iteration 51373 (of 85077): max relative diff=0.000020, 390.78 sec so far
Iteration 52033 (of 85077): max relative diff=0.000019, 395.79 sec so far
Iteration 52691 (of 85077): max relative diff=0.000019, 400.80 sec so far
Iteration 53351 (of 85077): max relative diff=0.000019, 405.81 sec so far
Iteration 54011 (of 85077): max relative diff=0.000019, 410.82 sec so far
Iteration 54671 (of 85077): max relative diff=0.000018, 415.83 sec so far
Iteration 55331 (of 85077): max relative diff=0.000018, 420.84 sec so far
Iteration 55990 (of 85077): max relative diff=0.000018, 425.85 sec so far
Iteration 56648 (of 85077): max relative diff=0.000018, 430.86 sec so far
Iteration 57301 (of 85077): max relative diff=0.000017, 435.87 sec so far
Iteration 57958 (of 85077): max relative diff=0.000017, 440.88 sec so far
Iteration 58614 (of 85077): max relative diff=0.000017, 445.89 sec so far
Iteration 59274 (of 85077): max relative diff=0.000017, 450.90 sec so far
Iteration 59933 (of 85077): max relative diff=0.000017, 455.91 sec so far
Iteration 60592 (of 85077): max relative diff=0.000017, 460.92 sec so far
Iteration 61251 (of 85077): max relative diff=0.000016, 465.93 sec so far
Iteration 61911 (of 85077): max relative diff=0.000016, 470.94 sec so far
Iteration 62571 (of 85077): max relative diff=0.000016, 475.95 sec so far
Iteration 63230 (of 85077): max relative diff=0.000016, 480.96 sec so far
Iteration 63890 (of 85077): max relative diff=0.000016, 485.97 sec so far
Iteration 64549 (of 85077): max relative diff=0.000016, 490.98 sec so far
Iteration 65201 (of 85077): max relative diff=0.000015, 495.99 sec so far
Iteration 65858 (of 85077): max relative diff=0.000015, 501.00 sec so far
Iteration 66514 (of 85077): max relative diff=0.000015, 506.01 sec so far
Iteration 67174 (of 85077): max relative diff=0.000015, 511.02 sec so far
Iteration 67833 (of 85077): max relative diff=0.000015, 516.03 sec so far
Iteration 68494 (of 85077): max relative diff=0.000015, 521.04 sec so far
Iteration 69154 (of 85077): max relative diff=0.000014, 526.05 sec so far
Iteration 69812 (of 85077): max relative diff=0.000014, 531.06 sec so far
Iteration 70472 (of 85077): max relative diff=0.000014, 536.07 sec so far
Iteration 71132 (of 85077): max relative diff=0.000014, 541.08 sec so far
Iteration 71792 (of 85077): max relative diff=0.000014, 546.09 sec so far
Iteration 72451 (of 85077): max relative diff=0.000014, 551.10 sec so far
Iteration 73109 (of 85077): max relative diff=0.000014, 556.11 sec so far
Iteration 73765 (of 85077): max relative diff=0.000014, 561.12 sec so far
Iteration 74421 (of 85077): max relative diff=0.000013, 566.13 sec so far
Iteration 75080 (of 85077): max relative diff=0.000013, 571.14 sec so far
Iteration 75740 (of 85077): max relative diff=0.000013, 576.15 sec so far
Iteration 76400 (of 85077): max relative diff=0.000013, 581.16 sec so far
Iteration 77060 (of 85077): max relative diff=0.000013, 586.17 sec so far
Iteration 77720 (of 85077): max relative diff=0.000013, 591.18 sec so far
Iteration 78379 (of 85077): max relative diff=0.000013, 596.19 sec so far
Iteration 79038 (of 85077): max relative diff=0.000013, 601.20 sec so far
Iteration 79698 (of 85077): max relative diff=0.000013, 606.21 sec so far
Iteration 80358 (of 85077): max relative diff=0.000012, 611.22 sec so far
Iteration 80987 (of 85077): max relative diff=0.000012, 616.23 sec so far
Iteration 81599 (of 85077): max relative diff=0.000012, 621.24 sec so far
Iteration 82213 (of 85077): max relative diff=0.000012, 626.25 sec so far
Iteration 82829 (of 85077): max relative diff=0.000012, 631.26 sec so far
Iteration 83445 (of 85077): max relative diff=0.000012, 636.27 sec so far
Iteration 84060 (of 85077): max relative diff=0.000012, 641.28 sec so far
Iteration 84676 (of 85077): max relative diff=0.000012, 646.29 sec so far

Iterative method: 85077 iterations in 657.71 seconds (average 0.007635, setup 8.16)

Value in the initial state: 0.001072402533769736

Time for model checking: 659.337 seconds.

Result: 0.001072402533769736


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_cluster.128-2000-20_rep4.log

```
Command(s):
../bin/prism  -importmodel models/cluster.128-2000-20/prism.model.umb models/cluster.128-2000-20/property.props
Wallclock time: 772.976 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:38:12 GMT+01:00 2026
Hostname: n23m0046.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/cluster.128-2000-20/prism.model.umb models/cluster.128-2000-20/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   x
Labels:      "minimum"

Parsing properties file "models/cluster.128-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 8% 10% 14% 16% 18% 20% 24% 26% 28% 32% 34% 36% 38% 42% 44% 46% 48% 52% 54% 56% 58% 60% 64% 66% 68% 70% 74% 76% 78% 80% 82% 86% 88% 90% 92% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 261 iterations in 0.98 seconds (average 0.003755, setup 0.00)

Time for model construction: 120.504 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 57334 nodes (134 terminal), 2908192 minterms, vars: 20r/20c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 141117 of 597012 (23.6%)

Building hybrid MTBDD matrix... [levels=20, nodes=124622] [5.7 MB]
Adding explicit sparse matrices... [levels=5, num=7348, compact] [671.9 KB]
Creating vector for diagonals... [dist=3024, compact] [1.2 MB]
Allocating iteration vectors... [3 x 4.6 MB]
TOTAL: [21.2 MB]

Uniformisation: q.t = 41.318415 x 2000.000000 = 82636.830000
Fox-Glynn: left = 80621, right = 85077

Starting iterations...
Iteration 667 (of 85077): max relative diff=0.009712, 5.01 sec so far
Iteration 1333 (of 85077): max relative diff=0.004204, 10.02 sec so far
Iteration 2000 (of 85077): max relative diff=0.001958, 15.03 sec so far
Iteration 2667 (of 85077): max relative diff=0.000833, 20.04 sec so far
Iteration 3334 (of 85077): max relative diff=0.000361, 25.05 sec so far
Iteration 4002 (of 85077): max relative diff=0.000261, 30.06 sec so far
Iteration 4670 (of 85077): max relative diff=0.000222, 35.07 sec so far
Iteration 5333 (of 85077): max relative diff=0.000194, 40.08 sec so far
Iteration 5996 (of 85077): max relative diff=0.000172, 45.09 sec so far
Iteration 6660 (of 85077): max relative diff=0.000154, 50.10 sec so far
Iteration 7327 (of 85077): max relative diff=0.000140, 55.11 sec so far
Iteration 7994 (of 85077): max relative diff=0.000128, 60.12 sec so far
Iteration 8661 (of 85077): max relative diff=0.000118, 65.13 sec so far
Iteration 9328 (of 85077): max relative diff=0.000109, 70.14 sec so far
Iteration 9995 (of 85077): max relative diff=0.000102, 75.15 sec so far
Iteration 10662 (of 85077): max relative diff=0.000095, 80.16 sec so far
Iteration 11330 (of 85077): max relative diff=0.000090, 85.17 sec so far
Iteration 11996 (of 85077): max relative diff=0.000085, 90.18 sec so far
Iteration 12663 (of 85077): max relative diff=0.000080, 95.19 sec so far
Iteration 13325 (of 85077): max relative diff=0.000076, 100.20 sec so far
Iteration 13991 (of 85077): max relative diff=0.000072, 105.21 sec so far
Iteration 14654 (of 85077): max relative diff=0.000069, 110.22 sec so far
Iteration 15321 (of 85077): max relative diff=0.000066, 115.23 sec so far
Iteration 15989 (of 85077): max relative diff=0.000063, 120.24 sec so far
Iteration 16656 (of 85077): max relative diff=0.000061, 125.25 sec so far
Iteration 17323 (of 85077): max relative diff=0.000058, 130.26 sec so far
Iteration 17989 (of 85077): max relative diff=0.000056, 135.27 sec so far
Iteration 18657 (of 85077): max relative diff=0.000054, 140.28 sec so far
Iteration 19324 (of 85077): max relative diff=0.000052, 145.29 sec so far
Iteration 19992 (of 85077): max relative diff=0.000050, 150.30 sec so far
Iteration 20659 (of 85077): max relative diff=0.000049, 155.31 sec so far
Iteration 21321 (of 85077): max relative diff=0.000047, 160.32 sec so far
Iteration 21984 (of 85077): max relative diff=0.000046, 165.33 sec so far
Iteration 22648 (of 85077): max relative diff=0.000044, 170.34 sec so far
Iteration 23315 (of 85077): max relative diff=0.000043, 175.35 sec so far
Iteration 23983 (of 85077): max relative diff=0.000042, 180.36 sec so far
Iteration 24650 (of 85077): max relative diff=0.000041, 185.37 sec so far
Iteration 25316 (of 85077): max relative diff=0.000040, 190.38 sec so far
Iteration 25984 (of 85077): max relative diff=0.000039, 195.39 sec so far
Iteration 26650 (of 85077): max relative diff=0.000038, 200.40 sec so far
Iteration 27317 (of 85077): max relative diff=0.000037, 205.41 sec so far
Iteration 27984 (of 85077): max relative diff=0.000036, 210.42 sec so far
Iteration 28652 (of 85077): max relative diff=0.000035, 215.43 sec so far
Iteration 29313 (of 85077): max relative diff=0.000034, 220.44 sec so far
Iteration 29976 (of 85077): max relative diff=0.000034, 225.45 sec so far
Iteration 30640 (of 85077): max relative diff=0.000033, 230.46 sec so far
Iteration 31308 (of 85077): max relative diff=0.000032, 235.47 sec so far
Iteration 31974 (of 85077): max relative diff=0.000031, 240.48 sec so far
Iteration 32641 (of 85077): max relative diff=0.000031, 245.49 sec so far
Iteration 33308 (of 85077): max relative diff=0.000030, 250.50 sec so far
Iteration 33976 (of 85077): max relative diff=0.000030, 255.51 sec so far
Iteration 34643 (of 85077): max relative diff=0.000029, 260.52 sec so far
Iteration 35310 (of 85077): max relative diff=0.000028, 265.53 sec so far
Iteration 35976 (of 85077): max relative diff=0.000028, 270.54 sec so far
Iteration 36643 (of 85077): max relative diff=0.000027, 275.55 sec so far
Iteration 37305 (of 85077): max relative diff=0.000027, 280.56 sec so far
Iteration 37969 (of 85077): max relative diff=0.000026, 285.57 sec so far
Iteration 38633 (of 85077): max relative diff=0.000026, 290.58 sec so far
Iteration 39300 (of 85077): max relative diff=0.000026, 295.59 sec so far
Iteration 39967 (of 85077): max relative diff=0.000025, 300.60 sec so far
Iteration 40634 (of 85077): max relative diff=0.000025, 305.61 sec so far
Iteration 41302 (of 85077): max relative diff=0.000024, 310.62 sec so far
Iteration 41969 (of 85077): max relative diff=0.000024, 315.63 sec so far
Iteration 42636 (of 85077): max relative diff=0.000024, 320.64 sec so far
Iteration 43302 (of 85077): max relative diff=0.000023, 325.65 sec so far
Iteration 43969 (of 85077): max relative diff=0.000023, 330.66 sec so far
Iteration 44636 (of 85077): max relative diff=0.000022, 335.67 sec so far
Iteration 45298 (of 85077): max relative diff=0.000022, 340.68 sec so far
Iteration 45962 (of 85077): max relative diff=0.000022, 345.69 sec so far
Iteration 46625 (of 85077): max relative diff=0.000022, 350.70 sec so far
Iteration 47292 (of 85077): max relative diff=0.000021, 355.71 sec so far
Iteration 47960 (of 85077): max relative diff=0.000021, 360.72 sec so far
Iteration 48627 (of 85077): max relative diff=0.000021, 365.73 sec so far
Iteration 49293 (of 85077): max relative diff=0.000020, 370.74 sec so far
Iteration 49961 (of 85077): max relative diff=0.000020, 375.75 sec so far
Iteration 50627 (of 85077): max relative diff=0.000020, 380.76 sec so far
Iteration 51294 (of 85077): max relative diff=0.000020, 385.77 sec so far
Iteration 51962 (of 85077): max relative diff=0.000019, 390.78 sec so far
Iteration 52629 (of 85077): max relative diff=0.000019, 395.79 sec so far
Iteration 53291 (of 85077): max relative diff=0.000019, 400.80 sec so far
Iteration 53954 (of 85077): max relative diff=0.000019, 405.81 sec so far
Iteration 54618 (of 85077): max relative diff=0.000018, 410.82 sec so far
Iteration 55286 (of 85077): max relative diff=0.000018, 415.83 sec so far
Iteration 55953 (of 85077): max relative diff=0.000018, 420.84 sec so far
Iteration 56620 (of 85077): max relative diff=0.000018, 425.85 sec so far
Iteration 57287 (of 85077): max relative diff=0.000018, 430.86 sec so far
Iteration 57954 (of 85077): max relative diff=0.000017, 435.87 sec so far
Iteration 58621 (of 85077): max relative diff=0.000017, 440.88 sec so far
Iteration 59288 (of 85077): max relative diff=0.000017, 445.89 sec so far
Iteration 59955 (of 85077): max relative diff=0.000017, 450.90 sec so far
Iteration 60621 (of 85077): max relative diff=0.000017, 455.91 sec so far
Iteration 61284 (of 85077): max relative diff=0.000016, 460.92 sec so far
Iteration 61948 (of 85077): max relative diff=0.000016, 465.93 sec so far
Iteration 62613 (of 85077): max relative diff=0.000016, 470.94 sec so far
Iteration 63279 (of 85077): max relative diff=0.000016, 475.95 sec so far
Iteration 63947 (of 85077): max relative diff=0.000016, 480.96 sec so far
Iteration 64615 (of 85077): max relative diff=0.000016, 485.97 sec so far
Iteration 65281 (of 85077): max relative diff=0.000015, 490.98 sec so far
Iteration 65947 (of 85077): max relative diff=0.000015, 495.99 sec so far
Iteration 66615 (of 85077): max relative diff=0.000015, 501.00 sec so far
Iteration 67283 (of 85077): max relative diff=0.000015, 506.01 sec so far
Iteration 67950 (of 85077): max relative diff=0.000015, 511.02 sec so far
Iteration 68617 (of 85077): max relative diff=0.000015, 516.03 sec so far
Iteration 69277 (of 85077): max relative diff=0.000014, 521.04 sec so far
Iteration 69941 (of 85077): max relative diff=0.000014, 526.05 sec so far
Iteration 70607 (of 85077): max relative diff=0.000014, 531.06 sec so far
Iteration 71274 (of 85077): max relative diff=0.000014, 536.07 sec so far
Iteration 71941 (of 85077): max relative diff=0.000014, 541.08 sec so far
Iteration 72607 (of 85077): max relative diff=0.000014, 546.09 sec so far
Iteration 73275 (of 85077): max relative diff=0.000014, 551.10 sec so far
Iteration 73942 (of 85077): max relative diff=0.000014, 556.11 sec so far
Iteration 74609 (of 85077): max relative diff=0.000013, 561.12 sec so far
Iteration 75276 (of 85077): max relative diff=0.000013, 566.13 sec so far
Iteration 75942 (of 85077): max relative diff=0.000013, 571.14 sec so far
Iteration 76610 (of 85077): max relative diff=0.000013, 576.15 sec so far
Iteration 77270 (of 85077): max relative diff=0.000013, 581.16 sec so far
Iteration 77933 (of 85077): max relative diff=0.000013, 586.17 sec so far
Iteration 78598 (of 85077): max relative diff=0.000013, 591.18 sec so far
Iteration 79265 (of 85077): max relative diff=0.000013, 596.19 sec so far
Iteration 79931 (of 85077): max relative diff=0.000013, 601.20 sec so far
Iteration 80599 (of 85077): max relative diff=0.000012, 606.21 sec so far
Iteration 81224 (of 85077): max relative diff=0.000012, 611.22 sec so far
Iteration 81849 (of 85077): max relative diff=0.000012, 616.23 sec so far
Iteration 82473 (of 85077): max relative diff=0.000012, 621.24 sec so far
Iteration 83097 (of 85077): max relative diff=0.000012, 626.25 sec so far
Iteration 83721 (of 85077): max relative diff=0.000012, 631.26 sec so far
Iteration 84345 (of 85077): max relative diff=0.000012, 636.27 sec so far
Iteration 84964 (of 85077): max relative diff=0.000012, 641.28 sec so far

Iterative method: 85077 iterations in 650.27 seconds (average 0.007548, setup 8.08)

Value in the initial state: 0.001072402533769736

Time for model checking: 651.82 seconds.

Result: 0.001072402533769736


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_cluster.128-2000-20_rep5.log

```
Command(s):
../bin/prism  -importmodel models/cluster.128-2000-20/prism.model.umb models/cluster.128-2000-20/property.props
Wallclock time: 914.763 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:54:00 GMT+01:00 2026
Hostname: n23m0239.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/cluster.128-2000-20/prism.model.umb models/cluster.128-2000-20/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   x
Labels:      "minimum"

Parsing properties file "models/cluster.128-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 261 iterations in 1.42 seconds (average 0.005441, setup 0.00)

Time for model construction: 188.195 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 57334 nodes (134 terminal), 2908192 minterms, vars: 20r/20c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 141117 of 597012 (23.6%)

Building hybrid MTBDD matrix... [levels=20, nodes=124622] [5.7 MB]
Adding explicit sparse matrices... [levels=5, num=7348, compact] [671.9 KB]
Creating vector for diagonals... [dist=3024, compact] [1.2 MB]
Allocating iteration vectors... [3 x 4.6 MB]
TOTAL: [21.2 MB]

Uniformisation: q.t = 41.318415 x 2000.000000 = 82636.830000
Fox-Glynn: left = 80621, right = 85077

Starting iterations...
Iteration 471 (of 85077): max relative diff=0.013680, 5.01 sec so far
Iteration 945 (of 85077): max relative diff=0.006664, 10.02 sec so far
Iteration 1417 (of 85077): max relative diff=0.003768, 15.03 sec so far
Iteration 1891 (of 85077): max relative diff=0.002206, 20.04 sec so far
Iteration 2365 (of 85077): max relative diff=0.001243, 25.06 sec so far
Iteration 2838 (of 85077): max relative diff=0.000667, 30.08 sec so far
Iteration 3311 (of 85077): max relative diff=0.000371, 35.09 sec so far
Iteration 3784 (of 85077): max relative diff=0.000277, 40.10 sec so far
Iteration 4252 (of 85077): max relative diff=0.000245, 45.11 sec so far
Iteration 4723 (of 85077): max relative diff=0.000220, 50.12 sec so far
Iteration 5195 (of 85077): max relative diff=0.000199, 55.13 sec so far
Iteration 5668 (of 85077): max relative diff=0.000182, 60.14 sec so far
Iteration 6140 (of 85077): max relative diff=0.000168, 65.15 sec so far
Iteration 6612 (of 85077): max relative diff=0.000155, 70.16 sec so far
Iteration 7085 (of 85077): max relative diff=0.000145, 75.17 sec so far
Iteration 7558 (of 85077): max relative diff=0.000135, 80.18 sec so far
Iteration 8031 (of 85077): max relative diff=0.000127, 85.19 sec so far
Iteration 8503 (of 85077): max relative diff=0.000120, 90.20 sec so far
Iteration 8976 (of 85077): max relative diff=0.000114, 95.21 sec so far
Iteration 9448 (of 85077): max relative diff=0.000108, 100.22 sec so far
Iteration 9916 (of 85077): max relative diff=0.000103, 105.23 sec so far
Iteration 10387 (of 85077): max relative diff=0.000098, 110.24 sec so far
Iteration 10859 (of 85077): max relative diff=0.000094, 115.25 sec so far
Iteration 11332 (of 85077): max relative diff=0.000090, 120.27 sec so far
Iteration 11804 (of 85077): max relative diff=0.000086, 125.28 sec so far
Iteration 12277 (of 85077): max relative diff=0.000083, 130.29 sec so far
Iteration 12750 (of 85077): max relative diff=0.000079, 135.30 sec so far
Iteration 13223 (of 85077): max relative diff=0.000077, 140.31 sec so far
Iteration 13696 (of 85077): max relative diff=0.000074, 145.32 sec so far
Iteration 14168 (of 85077): max relative diff=0.000071, 150.33 sec so far
Iteration 14640 (of 85077): max relative diff=0.000069, 155.34 sec so far
Iteration 15113 (of 85077): max relative diff=0.000067, 160.35 sec so far
Iteration 15580 (of 85077): max relative diff=0.000065, 165.36 sec so far
Iteration 16050 (of 85077): max relative diff=0.000063, 170.37 sec so far
Iteration 16522 (of 85077): max relative diff=0.000061, 175.38 sec so far
Iteration 17054 (of 85077): max relative diff=0.000059, 180.39 sec so far
Iteration 17709 (of 85077): max relative diff=0.000057, 185.40 sec so far
Iteration 18365 (of 85077): max relative diff=0.000055, 190.41 sec so far
Iteration 18988 (of 85077): max relative diff=0.000053, 195.42 sec so far
Iteration 19461 (of 85077): max relative diff=0.000052, 200.43 sec so far
Iteration 19934 (of 85077): max relative diff=0.000051, 205.44 sec so far
Iteration 20406 (of 85077): max relative diff=0.000049, 210.45 sec so far
Iteration 20879 (of 85077): max relative diff=0.000048, 215.46 sec so far
Iteration 21351 (of 85077): max relative diff=0.000047, 220.47 sec so far
Iteration 21819 (of 85077): max relative diff=0.000046, 225.48 sec so far
Iteration 22290 (of 85077): max relative diff=0.000045, 230.49 sec so far
Iteration 22761 (of 85077): max relative diff=0.000044, 235.50 sec so far
Iteration 23408 (of 85077): max relative diff=0.000043, 240.51 sec so far
Iteration 24069 (of 85077): max relative diff=0.000042, 245.52 sec so far
Iteration 24722 (of 85077): max relative diff=0.000041, 250.53 sec so far
Iteration 25375 (of 85077): max relative diff=0.000040, 255.54 sec so far
Iteration 26030 (of 85077): max relative diff=0.000039, 260.55 sec so far
Iteration 26690 (of 85077): max relative diff=0.000038, 265.56 sec so far
Iteration 27348 (of 85077): max relative diff=0.000037, 270.57 sec so far
Iteration 28008 (of 85077): max relative diff=0.000036, 275.58 sec so far
Iteration 28656 (of 85077): max relative diff=0.000035, 280.59 sec so far
Iteration 29310 (of 85077): max relative diff=0.000034, 285.60 sec so far
Iteration 29964 (of 85077): max relative diff=0.000034, 290.61 sec so far
Iteration 30621 (of 85077): max relative diff=0.000033, 295.62 sec so far
Iteration 31281 (of 85077): max relative diff=0.000032, 300.63 sec so far
Iteration 31941 (of 85077): max relative diff=0.000031, 305.64 sec so far
Iteration 32600 (of 85077): max relative diff=0.000031, 310.65 sec so far
Iteration 33247 (of 85077): max relative diff=0.000030, 315.66 sec so far
Iteration 33908 (of 85077): max relative diff=0.000030, 320.67 sec so far
Iteration 34566 (of 85077): max relative diff=0.000029, 325.68 sec so far
Iteration 35225 (of 85077): max relative diff=0.000029, 330.69 sec so far
Iteration 35885 (of 85077): max relative diff=0.000028, 335.70 sec so far
Iteration 36538 (of 85077): max relative diff=0.000027, 340.71 sec so far
Iteration 37189 (of 85077): max relative diff=0.000027, 345.72 sec so far
Iteration 37836 (of 85077): max relative diff=0.000027, 350.73 sec so far
Iteration 38497 (of 85077): max relative diff=0.000026, 355.74 sec so far
Iteration 39157 (of 85077): max relative diff=0.000026, 360.75 sec so far
Iteration 39817 (of 85077): max relative diff=0.000025, 365.76 sec so far
Iteration 40478 (of 85077): max relative diff=0.000025, 370.77 sec so far
Iteration 41139 (of 85077): max relative diff=0.000024, 375.78 sec so far
Iteration 41798 (of 85077): max relative diff=0.000024, 380.79 sec so far
Iteration 42435 (of 85077): max relative diff=0.000024, 385.80 sec so far
Iteration 43095 (of 85077): max relative diff=0.000023, 390.81 sec so far
Iteration 43751 (of 85077): max relative diff=0.000023, 395.82 sec so far
Iteration 44407 (of 85077): max relative diff=0.000023, 400.83 sec so far
Iteration 45061 (of 85077): max relative diff=0.000022, 405.84 sec so far
Iteration 45715 (of 85077): max relative diff=0.000022, 410.85 sec so far
Iteration 46375 (of 85077): max relative diff=0.000022, 415.86 sec so far
Iteration 47036 (of 85077): max relative diff=0.000021, 420.87 sec so far
Iteration 47695 (of 85077): max relative diff=0.000021, 425.88 sec so far
Iteration 48356 (of 85077): max relative diff=0.000021, 430.89 sec so far
Iteration 49016 (of 85077): max relative diff=0.000020, 435.90 sec so far
Iteration 49676 (of 85077): max relative diff=0.000020, 440.91 sec so far
Iteration 50336 (of 85077): max relative diff=0.000020, 445.92 sec so far
Iteration 50994 (of 85077): max relative diff=0.000020, 450.93 sec so far
Iteration 51644 (of 85077): max relative diff=0.000019, 455.94 sec so far
Iteration 52292 (of 85077): max relative diff=0.000019, 460.95 sec so far
Iteration 52944 (of 85077): max relative diff=0.000019, 465.96 sec so far
Iteration 53600 (of 85077): max relative diff=0.000019, 470.97 sec so far
Iteration 54260 (of 85077): max relative diff=0.000018, 475.98 sec so far
Iteration 54920 (of 85077): max relative diff=0.000018, 480.99 sec so far
Iteration 55581 (of 85077): max relative diff=0.000018, 486.00 sec so far
Iteration 56241 (of 85077): max relative diff=0.000018, 491.01 sec so far
Iteration 56902 (of 85077): max relative diff=0.000018, 496.02 sec so far
Iteration 57562 (of 85077): max relative diff=0.000017, 501.03 sec so far
Iteration 58222 (of 85077): max relative diff=0.000017, 506.04 sec so far
Iteration 58881 (of 85077): max relative diff=0.000017, 511.05 sec so far
Iteration 59542 (of 85077): max relative diff=0.000017, 516.06 sec so far
Iteration 60191 (of 85077): max relative diff=0.000017, 521.07 sec so far
Iteration 60826 (of 85077): max relative diff=0.000016, 526.08 sec so far
Iteration 61455 (of 85077): max relative diff=0.000016, 531.09 sec so far
Iteration 62113 (of 85077): max relative diff=0.000016, 536.10 sec so far
Iteration 62769 (of 85077): max relative diff=0.000016, 541.11 sec so far
Iteration 63428 (of 85077): max relative diff=0.000016, 546.12 sec so far
Iteration 64088 (of 85077): max relative diff=0.000016, 551.13 sec so far
Iteration 64749 (of 85077): max relative diff=0.000015, 556.14 sec so far
Iteration 65408 (of 85077): max relative diff=0.000015, 561.15 sec so far
Iteration 66069 (of 85077): max relative diff=0.000015, 566.16 sec so far
Iteration 66727 (of 85077): max relative diff=0.000015, 571.17 sec so far
Iteration 67386 (of 85077): max relative diff=0.000015, 576.18 sec so far
Iteration 68033 (of 85077): max relative diff=0.000015, 581.19 sec so far
Iteration 68691 (of 85077): max relative diff=0.000015, 586.20 sec so far
Iteration 69346 (of 85077): max relative diff=0.000014, 591.21 sec so far
Iteration 70007 (of 85077): max relative diff=0.000014, 596.22 sec so far
Iteration 70667 (of 85077): max relative diff=0.000014, 601.23 sec so far
Iteration 71328 (of 85077): max relative diff=0.000014, 606.24 sec so far
Iteration 71986 (of 85077): max relative diff=0.000014, 611.25 sec so far
Iteration 72646 (of 85077): max relative diff=0.000014, 616.26 sec so far
Iteration 73306 (of 85077): max relative diff=0.000014, 621.27 sec so far
Iteration 73966 (of 85077): max relative diff=0.000014, 626.28 sec so far
Iteration 74626 (of 85077): max relative diff=0.000013, 631.29 sec so far
Iteration 75287 (of 85077): max relative diff=0.000013, 636.30 sec so far
Iteration 75933 (of 85077): max relative diff=0.000013, 641.31 sec so far
Iteration 76591 (of 85077): max relative diff=0.000013, 646.32 sec so far
Iteration 77246 (of 85077): max relative diff=0.000013, 651.33 sec so far
Iteration 77905 (of 85077): max relative diff=0.000013, 656.34 sec so far
Iteration 78564 (of 85077): max relative diff=0.000013, 661.35 sec so far
Iteration 79223 (of 85077): max relative diff=0.000013, 666.36 sec so far
Iteration 79859 (of 85077): max relative diff=0.000013, 671.37 sec so far
Iteration 80520 (of 85077): max relative diff=0.000012, 676.38 sec so far
Iteration 81143 (of 85077): max relative diff=0.000012, 681.39 sec so far
Iteration 81759 (of 85077): max relative diff=0.000012, 686.40 sec so far
Iteration 82376 (of 85077): max relative diff=0.000012, 691.41 sec so far
Iteration 82990 (of 85077): max relative diff=0.000012, 696.42 sec so far
Iteration 83595 (of 85077): max relative diff=0.000012, 701.43 sec so far
Iteration 84208 (of 85077): max relative diff=0.000012, 706.44 sec so far
Iteration 84820 (of 85077): max relative diff=0.000012, 711.45 sec so far

Iterative method: 85077 iterations in 723.58 seconds (average 0.008387, setup 10.04)

Value in the initial state: 0.001072402533769736

Time for model checking: 725.512 seconds.

Result: 0.001072402533769736


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

