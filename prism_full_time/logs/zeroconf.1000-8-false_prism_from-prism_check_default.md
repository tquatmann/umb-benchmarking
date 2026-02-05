# Log files for prism_from-prism_check_default on model [zeroconf.1000-8-false](../../models/zeroconf.1000-8-false)

Parsed values: `[151.225, 173.826, 116.56, 116.249, 165.688]`



### Log file: prism_from-prism_check_default_zeroconf.1000-8-false_rep1.log

```
Command(s):
../bin/prism  models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props
Wallclock time: 151.225 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:23:29 GMT+01:00 2026
Hostname: r23m0130.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 592 iterations in 52.32 seconds (average 0.088378, setup 0.00)

Time for model construction: 52.917 seconds.

Type:        MDP
States:      1870338 (1 initial)
Transitions: 4245554

Transition matrix: 154038 nodes (6 terminal), 4245554 minterms, vars: 58r/58c/7nd

Prob0A: 131 iterations in 3.11 seconds (average 0.023740, setup 0.00)

Prob1E: 2127 iterations in 76.95 seconds (average 0.036178, setup 0.00)

yes = 171749, no = 611330, maybe = 1087259

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=9, levels=58, nodes=272480] [12.5 MB]
Adding sparse bits... [levels=24-43, num=4846, compact=9/9] [8.0 MB]
Creating vector for yes... [dist=2, compact] [3.6 MB]
Allocating iteration vectors... [3 x 14.3 MB]
TOTAL: [66.8 MB]

Starting iterations...
Iteration 101: max relative diff=inf, 5.02 sec so far
Iteration 203: max relative diff=0.000934, 10.07 sec so far
Iteration 305: max relative diff=0.000004, 15.13 sec so far

Iterative method: 311 iterations in 17.20 seconds (average 0.049614, setup 1.77)

Value in the initial state: 4.801413635072425E-8

Time for model checking: 97.576 seconds.

Result: 4.801413635072425E-8 (+/- 4.0740549090035865E-13 estimated; rel err 8.485115465254294E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_zeroconf.1000-8-false_rep2.log

```
Command(s):
../bin/prism  models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props
Wallclock time: 173.826 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:01:30 GMT+01:00 2026
Hostname: r23m0015.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 592 iterations in 59.18 seconds (average 0.099966, setup 0.00)

Time for model construction: 59.976 seconds.

Type:        MDP
States:      1870338 (1 initial)
Transitions: 4245554

Transition matrix: 154038 nodes (6 terminal), 4245554 minterms, vars: 58r/58c/7nd

Prob0A: 131 iterations in 3.55 seconds (average 0.027099, setup 0.00)

Prob1E: 2127 iterations in 87.78 seconds (average 0.041269, setup 0.00)

yes = 171749, no = 611330, maybe = 1087259

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=9, levels=58, nodes=272480] [12.5 MB]
Adding sparse bits... [levels=24-43, num=4846, compact=9/9] [8.0 MB]
Creating vector for yes... [dist=2, compact] [3.6 MB]
Allocating iteration vectors... [3 x 14.3 MB]
TOTAL: [66.8 MB]

Starting iterations...
Iteration 82: max relative diff=inf, 5.04 sec so far
Iteration 163: max relative diff=0.051717, 10.06 sec so far
Iteration 244: max relative diff=0.000015, 15.08 sec so far

Iterative method: 311 iterations in 21.12 seconds (average 0.061736, setup 1.92)

Value in the initial state: 4.801413635072425E-8

Time for model checking: 113.09 seconds.

Result: 4.801413635072425E-8 (+/- 4.0740549090035865E-13 estimated; rel err 8.485115465254294E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_zeroconf.1000-8-false_rep3.log

```
Command(s):
../bin/prism  models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props
Wallclock time: 116.560 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:24:08 GMT+01:00 2026
Hostname: n23m0051.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 592 iterations in 43.57 seconds (average 0.073598, setup 0.00)

Time for model construction: 44.142 seconds.

Type:        MDP
States:      1870338 (1 initial)
Transitions: 4245554

Transition matrix: 154038 nodes (6 terminal), 4245554 minterms, vars: 58r/58c/7nd

Prob0A: 131 iterations in 2.41 seconds (average 0.018397, setup 0.00)

Prob1E: 2127 iterations in 53.87 seconds (average 0.025327, setup 0.00)

yes = 171749, no = 611330, maybe = 1087259

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=9, levels=58, nodes=272480] [12.5 MB]
Adding sparse bits... [levels=24-43, num=4846, compact=9/9] [8.0 MB]
Creating vector for yes... [dist=2, compact] [3.6 MB]
Allocating iteration vectors... [3 x 14.3 MB]
TOTAL: [66.8 MB]

Starting iterations...
Iteration 116: max relative diff=inf, 5.03 sec so far
Iteration 229: max relative diff=0.000850, 10.06 sec so far

Iterative method: 311 iterations in 15.23 seconds (average 0.043859, setup 1.59)

Value in the initial state: 4.801413635072425E-8

Time for model checking: 71.746 seconds.

Result: 4.801413635072425E-8 (+/- 4.0740549090035865E-13 estimated; rel err 8.485115465254294E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_zeroconf.1000-8-false_rep4.log

```
Command(s):
../bin/prism  models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props
Wallclock time: 116.249 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:05:35 GMT+01:00 2026
Hostname: n23m0386.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 592 iterations in 40.81 seconds (average 0.068936, setup 0.00)

Time for model construction: 41.336 seconds.

Type:        MDP
States:      1870338 (1 initial)
Transitions: 4245554

Transition matrix: 154038 nodes (6 terminal), 4245554 minterms, vars: 58r/58c/7nd

Prob0A: 131 iterations in 2.27 seconds (average 0.017328, setup 0.00)

Prob1E: 2127 iterations in 56.88 seconds (average 0.026742, setup 0.00)

yes = 171749, no = 611330, maybe = 1087259

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=9, levels=58, nodes=272480] [12.5 MB]
Adding sparse bits... [levels=24-43, num=4846, compact=9/9] [8.0 MB]
Creating vector for yes... [dist=2, compact] [3.6 MB]
Allocating iteration vectors... [3 x 14.3 MB]
TOTAL: [66.8 MB]

Starting iterations...
Iteration 119: max relative diff=inf, 5.03 sec so far
Iteration 238: max relative diff=0.000108, 10.07 sec so far

Iterative method: 311 iterations in 14.70 seconds (average 0.042347, setup 1.53)

Value in the initial state: 4.801413635072425E-8

Time for model checking: 74.134 seconds.

Result: 4.801413635072425E-8 (+/- 4.0740549090035865E-13 estimated; rel err 8.485115465254294E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_zeroconf.1000-8-false_rep5.log

```
Command(s):
../bin/prism  models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props
Wallclock time: 165.688 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:58:55 GMT+01:00 2026
Hostname: n23m0096.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 592 iterations in 56.19 seconds (average 0.094916, setup 0.00)

Time for model construction: 57.059 seconds.

Type:        MDP
States:      1870338 (1 initial)
Transitions: 4245554

Transition matrix: 154038 nodes (6 terminal), 4245554 minterms, vars: 58r/58c/7nd

Prob0A: 131 iterations in 3.33 seconds (average 0.025420, setup 0.00)

Prob1E: 2127 iterations in 84.58 seconds (average 0.039765, setup 0.00)

yes = 171749, no = 611330, maybe = 1087259

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=9, levels=58, nodes=272480] [12.5 MB]
Adding sparse bits... [levels=24-43, num=4846, compact=9/9] [8.0 MB]
Creating vector for yes... [dist=2, compact] [3.6 MB]
Allocating iteration vectors... [3 x 14.3 MB]
TOTAL: [66.8 MB]

Starting iterations...
Iteration 94: max relative diff=inf, 5.03 sec so far
Iteration 173: max relative diff=0.001020, 10.08 sec so far
Iteration 266: max relative diff=0.000013, 15.13 sec so far

Iterative method: 311 iterations in 19.25 seconds (average 0.056270, setup 1.75)

Value in the initial state: 4.801413635072425E-8

Time for model checking: 107.648 seconds.

Result: 4.801413635072425E-8 (+/- 4.0740549090035865E-13 estimated; rel err 8.485115465254294E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

