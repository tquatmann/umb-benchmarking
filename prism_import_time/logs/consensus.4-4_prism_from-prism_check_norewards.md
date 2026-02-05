# Log files for prism_from-prism_check_norewards on model [consensus.4-4](../../models/consensus.4-4)

Parsed values: `[0.042, 0.039, 0.059, 0.049, 0.056]`



### Log file: prism_from-prism_check_norewards_consensus.4-4_rep1.log

```
Command(s):
../bin/prism  models/consensus.4-4/model.prism models/consensus.4-4/property.props
Wallclock time: 7.167 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:51:30 GMT+01:00 2026
Hostname: r23m0206.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.4-4/model.prism models/consensus.4-4/property.props

Parsing PRISM model file "models/consensus.4-4/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4
Labels:      "finished" "agree"

Parsing properties file "models/consensus.4-4/property.props"...

1 property:
(1) "disagree": Pmax=? [ F "finished"&!"agree" ]

---------------------------------------------------------------------

Model checking: "disagree": Pmax=? [ F "finished"&!"agree" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.02 seconds (average 0.000103, setup 0.00)

Time for model construction: 0.042 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352

Transition matrix: 2336 nodes (3 terminal), 144352 minterms, vars: 18r/18c/4nd

Prob0A: 149 iterations in 0.10 seconds (average 0.000671, setup 0.00)

Prob1E: 2480 iterations in 1.75 seconds (average 0.000706, setup 0.00)

yes = 10872, no = 910, maybe = 31354

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=18, nodes=6080] [285.0 KB]
Adding sparse bits... [levels=18-18, num=4, compact=4/4] [630.2 KB]
Creating vector for yes... [dist=2, compact] [84.3 KB]
Allocating iteration vectors... [3 x 337.0 KB]
TOTAL: [2.0 MB]

Starting iterations...

Iterative method: 6873 iterations in 4.65 seconds (average 0.000675, setup 0.01)

Value in the initial state: 0.15605695062063785

Time for model checking: 6.527 seconds.

Result: 0.15605695062063785 (+/- 1.5602140768172048E-6 estimated; rel err 9.997722437944864E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_consensus.4-4_rep2.log

```
Command(s):
../bin/prism  models/consensus.4-4/model.prism models/consensus.4-4/property.props
Wallclock time: 6.963 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:25:14 GMT+01:00 2026
Hostname: n23m0110.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.4-4/model.prism models/consensus.4-4/property.props

Parsing PRISM model file "models/consensus.4-4/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4
Labels:      "finished" "agree"

Parsing properties file "models/consensus.4-4/property.props"...

1 property:
(1) "disagree": Pmax=? [ F "finished"&!"agree" ]

---------------------------------------------------------------------

Model checking: "disagree": Pmax=? [ F "finished"&!"agree" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.02 seconds (average 0.000103, setup 0.00)

Time for model construction: 0.039 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352

Transition matrix: 2336 nodes (3 terminal), 144352 minterms, vars: 18r/18c/4nd

Prob0A: 149 iterations in 0.09 seconds (average 0.000604, setup 0.00)

Prob1E: 2480 iterations in 1.75 seconds (average 0.000706, setup 0.00)

yes = 10872, no = 910, maybe = 31354

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=18, nodes=6080] [285.0 KB]
Adding sparse bits... [levels=18-18, num=4, compact=4/4] [630.2 KB]
Creating vector for yes... [dist=2, compact] [84.3 KB]
Allocating iteration vectors... [3 x 337.0 KB]
TOTAL: [2.0 MB]

Starting iterations...

Iterative method: 6873 iterations in 4.45 seconds (average 0.000646, setup 0.01)

Value in the initial state: 0.15605695062063785

Time for model checking: 6.323 seconds.

Result: 0.15605695062063785 (+/- 1.5602140768172048E-6 estimated; rel err 9.997722437944864E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_consensus.4-4_rep3.log

```
Command(s):
../bin/prism  models/consensus.4-4/model.prism models/consensus.4-4/property.props
Wallclock time: 11.653 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:10 GMT+01:00 2026
Hostname: n23m0156.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.4-4/model.prism models/consensus.4-4/property.props

Parsing PRISM model file "models/consensus.4-4/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4
Labels:      "finished" "agree"

Parsing properties file "models/consensus.4-4/property.props"...

1 property:
(1) "disagree": Pmax=? [ F "finished"&!"agree" ]

---------------------------------------------------------------------

Model checking: "disagree": Pmax=? [ F "finished"&!"agree" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.02 seconds (average 0.000103, setup 0.00)

Time for model construction: 0.059 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352

Transition matrix: 2336 nodes (3 terminal), 144352 minterms, vars: 18r/18c/4nd

Prob0A: 149 iterations in 0.08 seconds (average 0.000537, setup 0.00)

Prob1E: 2480 iterations in 1.66 seconds (average 0.000669, setup 0.00)

yes = 10872, no = 910, maybe = 31354

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=18, nodes=6080] [285.0 KB]
Adding sparse bits... [levels=18-18, num=4, compact=4/4] [630.2 KB]
Creating vector for yes... [dist=2, compact] [84.3 KB]
Allocating iteration vectors... [3 x 337.0 KB]
TOTAL: [2.0 MB]

Starting iterations...

Iterative method: 6873 iterations in 4.64 seconds (average 0.000674, setup 0.01)

Value in the initial state: 0.15605695062063785

Time for model checking: 6.412 seconds.

Result: 0.15605695062063785 (+/- 1.5602140768172048E-6 estimated; rel err 9.997722437944864E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_consensus.4-4_rep4.log

```
Command(s):
../bin/prism  models/consensus.4-4/model.prism models/consensus.4-4/property.props
Wallclock time: 8.297 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:22:16 GMT+01:00 2026
Hostname: n23m0053.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.4-4/model.prism models/consensus.4-4/property.props

Parsing PRISM model file "models/consensus.4-4/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4
Labels:      "finished" "agree"

Parsing properties file "models/consensus.4-4/property.props"...

1 property:
(1) "disagree": Pmax=? [ F "finished"&!"agree" ]

---------------------------------------------------------------------

Model checking: "disagree": Pmax=? [ F "finished"&!"agree" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.02 seconds (average 0.000103, setup 0.00)

Time for model construction: 0.049 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352

Transition matrix: 2336 nodes (3 terminal), 144352 minterms, vars: 18r/18c/4nd

Prob0A: 149 iterations in 0.12 seconds (average 0.000805, setup 0.00)

Prob1E: 2480 iterations in 2.20 seconds (average 0.000887, setup 0.00)

yes = 10872, no = 910, maybe = 31354

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=18, nodes=6080] [285.0 KB]
Adding sparse bits... [levels=18-18, num=4, compact=4/4] [630.2 KB]
Creating vector for yes... [dist=2, compact] [84.3 KB]
Allocating iteration vectors... [3 x 337.0 KB]
TOTAL: [2.0 MB]

Starting iterations...
Iteration 6610: max relative diff=0.000002, 5.01 sec so far

Iterative method: 6873 iterations in 5.22 seconds (average 0.000757, setup 0.02)

Value in the initial state: 0.15605695062063785

Time for model checking: 7.571 seconds.

Result: 0.15605695062063785 (+/- 1.5602140768172048E-6 estimated; rel err 9.997722437944864E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_consensus.4-4_rep5.log

```
Command(s):
../bin/prism  models/consensus.4-4/model.prism models/consensus.4-4/property.props
Wallclock time: 8.688 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:07:59 GMT+01:00 2026
Hostname: n23m0053.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.4-4/model.prism models/consensus.4-4/property.props

Parsing PRISM model file "models/consensus.4-4/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4
Labels:      "finished" "agree"

Parsing properties file "models/consensus.4-4/property.props"...

1 property:
(1) "disagree": Pmax=? [ F "finished"&!"agree" ]

---------------------------------------------------------------------

Model checking: "disagree": Pmax=? [ F "finished"&!"agree" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.02 seconds (average 0.000103, setup 0.00)

Time for model construction: 0.056 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352

Transition matrix: 2336 nodes (3 terminal), 144352 minterms, vars: 18r/18c/4nd

Prob0A: 149 iterations in 0.13 seconds (average 0.000872, setup 0.00)

Prob1E: 2480 iterations in 2.52 seconds (average 0.001016, setup 0.00)

yes = 10872, no = 910, maybe = 31354

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=18, nodes=6080] [285.0 KB]
Adding sparse bits... [levels=18-18, num=4, compact=4/4] [630.2 KB]
Creating vector for yes... [dist=2, compact] [84.3 KB]
Allocating iteration vectors... [3 x 337.0 KB]
TOTAL: [2.0 MB]

Starting iterations...
Iteration 6583: max relative diff=0.000002, 5.01 sec so far

Iterative method: 6873 iterations in 5.25 seconds (average 0.000761, setup 0.02)

Value in the initial state: 0.15605695062063785

Time for model checking: 7.933 seconds.

Result: 0.15605695062063785 (+/- 1.5602140768172048E-6 estimated; rel err 9.997722437944864E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

