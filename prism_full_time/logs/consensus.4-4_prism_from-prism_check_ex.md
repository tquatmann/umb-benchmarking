# Log files for prism_from-prism_check_ex on model [consensus.4-4](../../models/consensus.4-4)

Parsed values: `[6.264, 6.214, 9.371, 6.493, 6.994]`



### Log file: prism_from-prism_check_ex_consensus.4-4_rep1.log

```
Command(s):
../bin/prism -ex models/consensus.4-4/model.prism models/consensus.4-4/property.props
Wallclock time: 6.264 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:25:02 GMT+01:00 2026
Hostname: r23m0212.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/consensus.4-4/model.prism models/consensus.4-4/property.props

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

Building model (engine:explicit)...

Computing reachable states... 43136 states
Reachable states exploration and model construction done in 0.243 secs.
Sorting reachable states list...

Time for model construction: 0.454 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352
Choices:     115840
Max/avg:     4/2.69

Starting probabilistic reachability (max)...
Starting Prob0 (max)...
Prob0 (max) took 149 iterations and 0.075 seconds.
Starting Prob1 (max)...
Prob1 (max) took 2595 iterations and 1.407 seconds.
target=56, yes=10872, no=910, maybe=31354
Starting value iteration (max, with Power method)...
Value iteration (max, with Power method) took 6873 iterations, 812168664 multiplications and 3.441 seconds.
Probabilistic reachability took 4.937 seconds.

Value in the initial state: 0.15605695062063785

Time for model checking: 4.96 seconds.

Result: 0.15605695062063785 (+/- 1.5602125169600354E-6 estimated; rel err 9.99771244250946E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_consensus.4-4_rep2.log

```
Command(s):
../bin/prism -ex models/consensus.4-4/model.prism models/consensus.4-4/property.props
Wallclock time: 6.214 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:54:00 GMT+01:00 2026
Hostname: n23m0237.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/consensus.4-4/model.prism models/consensus.4-4/property.props

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

Building model (engine:explicit)...

Computing reachable states... 43136 states
Reachable states exploration and model construction done in 0.244 secs.
Sorting reachable states list...

Time for model construction: 0.345 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352
Choices:     115840
Max/avg:     4/2.69

Starting probabilistic reachability (max)...
Starting Prob0 (max)...
Prob0 (max) took 149 iterations and 0.087 seconds.
Starting Prob1 (max)...
Prob1 (max) took 2595 iterations and 1.444 seconds.
target=56, yes=10872, no=910, maybe=31354
Starting value iteration (max, with Power method)...
Value iteration (max, with Power method) took 6873 iterations, 812168664 multiplications and 3.428 seconds.
Probabilistic reachability took 4.971 seconds.

Value in the initial state: 0.15605695062063785

Time for model checking: 4.989 seconds.

Result: 0.15605695062063785 (+/- 1.5602125169600354E-6 estimated; rel err 9.99771244250946E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_consensus.4-4_rep3.log

```
Command(s):
../bin/prism -ex models/consensus.4-4/model.prism models/consensus.4-4/property.props
Wallclock time: 9.371 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:18:03 GMT+01:00 2026
Hostname: n23m0295.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/consensus.4-4/model.prism models/consensus.4-4/property.props

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

Building model (engine:explicit)...

Computing reachable states... 43136 states
Reachable states exploration and model construction done in 0.254 secs.
Sorting reachable states list...

Time for model construction: 0.516 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352
Choices:     115840
Max/avg:     4/2.69

Starting probabilistic reachability (max)...
Starting Prob0 (max)...
Prob0 (max) took 149 iterations and 0.087 seconds.
Starting Prob1 (max)...
Prob1 (max) took 2595 iterations and 1.485 seconds.
target=56, yes=10872, no=910, maybe=31354
Starting value iteration (max, with Power method)...
Value iteration (max, with Power method) took 6873 iterations, 812168664 multiplications and 3.755 seconds.
Probabilistic reachability took 5.36 seconds.

Value in the initial state: 0.15605695062063785

Time for model checking: 5.386 seconds.

Result: 0.15605695062063785 (+/- 1.5602125169600354E-6 estimated; rel err 9.99771244250946E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_consensus.4-4_rep4.log

```
Command(s):
../bin/prism -ex models/consensus.4-4/model.prism models/consensus.4-4/property.props
Wallclock time: 6.493 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:24 GMT+01:00 2026
Hostname: n23m0120.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/consensus.4-4/model.prism models/consensus.4-4/property.props

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

Building model (engine:explicit)...

Computing reachable states... 43136 states
Reachable states exploration and model construction done in 0.237 secs.
Sorting reachable states list...

Time for model construction: 0.376 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352
Choices:     115840
Max/avg:     4/2.69

Starting probabilistic reachability (max)...
Starting Prob0 (max)...
Prob0 (max) took 149 iterations and 0.085 seconds.
Starting Prob1 (max)...
Prob1 (max) took 2595 iterations and 1.46 seconds.
target=56, yes=10872, no=910, maybe=31354
Starting value iteration (max, with Power method)...
Value iteration (max, with Power method) took 6873 iterations, 812168664 multiplications and 3.556 seconds.
Probabilistic reachability took 5.117 seconds.

Value in the initial state: 0.15605695062063785

Time for model checking: 5.139 seconds.

Result: 0.15605695062063785 (+/- 1.5602125169600354E-6 estimated; rel err 9.99771244250946E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_consensus.4-4_rep5.log

```
Command(s):
../bin/prism -ex models/consensus.4-4/model.prism models/consensus.4-4/property.props
Wallclock time: 6.994 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:26:10 GMT+01:00 2026
Hostname: n23m0124.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/consensus.4-4/model.prism models/consensus.4-4/property.props

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

Building model (engine:explicit)...

Computing reachable states... 43136 states
Reachable states exploration and model construction done in 0.261 secs.
Sorting reachable states list...

Time for model construction: 0.379 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352
Choices:     115840
Max/avg:     4/2.69

Starting probabilistic reachability (max)...
Starting Prob0 (max)...
Prob0 (max) took 149 iterations and 0.091 seconds.
Starting Prob1 (max)...
Prob1 (max) took 2595 iterations and 1.572 seconds.
target=56, yes=10872, no=910, maybe=31354
Starting value iteration (max, with Power method)...
Value iteration (max, with Power method) took 6873 iterations, 812168664 multiplications and 4.068 seconds.
Probabilistic reachability took 5.75 seconds.

Value in the initial state: 0.15605695062063785

Time for model checking: 5.775 seconds.

Result: 0.15605695062063785 (+/- 1.5602125169600354E-6 estimated; rel err 9.99771244250946E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

