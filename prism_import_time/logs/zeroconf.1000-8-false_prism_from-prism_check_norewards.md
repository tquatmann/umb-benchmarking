# Log files for prism_from-prism_check_norewards on model [zeroconf.1000-8-false](../../models/zeroconf.1000-8-false)

Parsed values: `[45.622, 58.787, 41.789, 39.454, 39.127]`



### Log file: prism_from-prism_check_norewards_zeroconf.1000-8-false_rep1.log

```
Command(s):
../bin/prism  models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props
Wallclock time: 131.402 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:57:45 GMT+01:00 2026
Hostname: n23m0242.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Parsing properties file "models/zeroconf.1000-8-false/property.props"...

1 property:
(1) "correct_max": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "correct_max": Pmax=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 592 iterations in 44.86 seconds (average 0.075777, setup 0.00)

Time for model construction: 45.622 seconds.

Type:        MDP
States:      1870338 (1 initial)
Transitions: 4245554

Transition matrix: 154038 nodes (6 terminal), 4245554 minterms, vars: 58r/58c/7nd

Prob0A: 131 iterations in 2.55 seconds (average 0.019466, setup 0.00)

Prob1E: 2127 iterations in 65.27 seconds (average 0.030686, setup 0.00)

yes = 171749, no = 611330, maybe = 1087259

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=9, levels=58, nodes=272480] [12.5 MB]
Adding sparse bits... [levels=24-43, num=4846, compact=9/9] [8.0 MB]
Creating vector for yes... [dist=2, compact] [3.6 MB]
Allocating iteration vectors... [3 x 14.3 MB]
TOTAL: [66.8 MB]

Starting iterations...
Iteration 103: max relative diff=inf, 5.02 sec so far
Iteration 208: max relative diff=0.000931, 10.06 sec so far
Iteration 311: max relative diff=0.000001, 15.09 sec so far

Iterative method: 311 iterations in 16.76 seconds (average 0.048521, setup 1.67)

Value in the initial state: 4.801413635072425E-8

Time for model checking: 84.944 seconds.

Result: 4.801413635072425E-8 (+/- 4.0740549090035865E-13 estimated; rel err 8.485115465254294E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_zeroconf.1000-8-false_rep2.log

```
Command(s):
../bin/prism  models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props
Wallclock time: 171.208 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:51:28 GMT+01:00 2026
Hostname: n23m0242.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Parsing properties file "models/zeroconf.1000-8-false/property.props"...

1 property:
(1) "correct_max": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "correct_max": Pmax=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 592 iterations in 58.03 seconds (average 0.098024, setup 0.00)

Time for model construction: 58.787 seconds.

Type:        MDP
States:      1870338 (1 initial)
Transitions: 4245554

Transition matrix: 154038 nodes (6 terminal), 4245554 minterms, vars: 58r/58c/7nd

Prob0A: 131 iterations in 3.52 seconds (average 0.026870, setup 0.00)

Prob1E: 2127 iterations in 86.92 seconds (average 0.040865, setup 0.00)

yes = 171749, no = 611330, maybe = 1087259

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=9, levels=58, nodes=272480] [12.5 MB]
Adding sparse bits... [levels=24-43, num=4846, compact=9/9] [8.0 MB]
Creating vector for yes... [dist=2, compact] [3.6 MB]
Allocating iteration vectors... [3 x 14.3 MB]
TOTAL: [66.8 MB]

Starting iterations...
Iteration 86: max relative diff=inf, 5.01 sec so far
Iteration 171: max relative diff=0.001037, 10.02 sec so far
Iteration 256: max relative diff=0.000014, 15.04 sec so far

Iterative method: 311 iterations in 20.16 seconds (average 0.058746, setup 1.89)

Value in the initial state: 4.801413635072425E-8

Time for model checking: 111.125 seconds.

Result: 4.801413635072425E-8 (+/- 4.0740549090035865E-13 estimated; rel err 8.485115465254294E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_zeroconf.1000-8-false_rep3.log

```
Command(s):
../bin/prism  models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props
Wallclock time: 133.823 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:00:30 GMT+01:00 2026
Hostname: n23m0040.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Parsing properties file "models/zeroconf.1000-8-false/property.props"...

1 property:
(1) "correct_max": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "correct_max": Pmax=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 592 iterations in 41.20 seconds (average 0.069595, setup 0.00)

Time for model construction: 41.789 seconds.

Type:        MDP
States:      1870338 (1 initial)
Transitions: 4245554

Transition matrix: 154038 nodes (6 terminal), 4245554 minterms, vars: 58r/58c/7nd

Prob0A: 131 iterations in 2.50 seconds (average 0.019084, setup 0.00)

Prob1E: 2127 iterations in 70.62 seconds (average 0.033202, setup 0.00)

yes = 171749, no = 611330, maybe = 1087259

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=9, levels=58, nodes=272480] [12.5 MB]
Adding sparse bits... [levels=24-43, num=4846, compact=9/9] [8.0 MB]
Creating vector for yes... [dist=2, compact] [3.6 MB]
Allocating iteration vectors... [3 x 14.3 MB]
TOTAL: [66.8 MB]

Starting iterations...
Iteration 108: max relative diff=inf, 5.05 sec so far
Iteration 215: max relative diff=0.000927, 10.07 sec so far

Iterative method: 311 iterations in 16.15 seconds (average 0.046849, setup 1.58)

Value in the initial state: 4.801413635072425E-8

Time for model checking: 89.559 seconds.

Result: 4.801413635072425E-8 (+/- 4.0740549090035865E-13 estimated; rel err 8.485115465254294E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_zeroconf.1000-8-false_rep4.log

```
Command(s):
../bin/prism  models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props
Wallclock time: 109.752 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:09:13 GMT+01:00 2026
Hostname: n23m0325.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Parsing properties file "models/zeroconf.1000-8-false/property.props"...

1 property:
(1) "correct_max": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "correct_max": Pmax=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 592 iterations in 39.03 seconds (average 0.065929, setup 0.00)

Time for model construction: 39.454 seconds.

Type:        MDP
States:      1870338 (1 initial)
Transitions: 4245554

Transition matrix: 154038 nodes (6 terminal), 4245554 minterms, vars: 58r/58c/7nd

Prob0A: 131 iterations in 2.10 seconds (average 0.016031, setup 0.00)

Prob1E: 2127 iterations in 52.40 seconds (average 0.024636, setup 0.00)

yes = 171749, no = 611330, maybe = 1087259

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=9, levels=58, nodes=272480] [12.5 MB]
Adding sparse bits... [levels=24-43, num=4846, compact=9/9] [8.0 MB]
Creating vector for yes... [dist=2, compact] [3.6 MB]
Allocating iteration vectors... [3 x 14.3 MB]
TOTAL: [66.8 MB]

Starting iterations...
Iteration 119: max relative diff=inf, 5.04 sec so far
Iteration 237: max relative diff=0.000149, 10.05 sec so far

Iterative method: 311 iterations in 14.90 seconds (average 0.042733, setup 1.61)

Value in the initial state: 4.801413635072425E-8

Time for model checking: 69.612 seconds.

Result: 4.801413635072425E-8 (+/- 4.0740549090035865E-13 estimated; rel err 8.485115465254294E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_zeroconf.1000-8-false_rep5.log

```
Command(s):
../bin/prism  models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props
Wallclock time: 114.012 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:22:07 GMT+01:00 2026
Hostname: r23m0214.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Parsing properties file "models/zeroconf.1000-8-false/property.props"...

1 property:
(1) "correct_max": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "correct_max": Pmax=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 592 iterations in 38.66 seconds (average 0.065304, setup 0.00)

Time for model construction: 39.127 seconds.

Type:        MDP
States:      1870338 (1 initial)
Transitions: 4245554

Transition matrix: 154038 nodes (6 terminal), 4245554 minterms, vars: 58r/58c/7nd

Prob0A: 131 iterations in 2.05 seconds (average 0.015649, setup 0.00)

Prob1E: 2127 iterations in 55.47 seconds (average 0.026079, setup 0.00)

yes = 171749, no = 611330, maybe = 1087259

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=9, levels=58, nodes=272480] [12.5 MB]
Adding sparse bits... [levels=24-43, num=4846, compact=9/9] [8.0 MB]
Creating vector for yes... [dist=2, compact] [3.6 MB]
Allocating iteration vectors... [3 x 14.3 MB]
TOTAL: [66.8 MB]

Starting iterations...
Iteration 109: max relative diff=inf, 5.03 sec so far
Iteration 217: max relative diff=0.000926, 10.06 sec so far

Iterative method: 311 iterations in 16.28 seconds (average 0.046752, setup 1.74)

Value in the initial state: 4.801413635072425E-8

Time for model checking: 74.117 seconds.

Result: 4.801413635072425E-8 (+/- 4.0740549090035865E-13 estimated; rel err 8.485115465254294E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

