# Log files

Tool configuration: prism_from-umb_check_ex
Benchmark: [consensus.4-4](../../models/consensus.4-4)
Parsed values: [7.246, 6.0, 5.895, 6.174, 6.142]



### Log file: prism_from-umb_check_ex_consensus.4-4_rep1.log

```
Command(s):
../bin/prism -ex -importmodel models/consensus.4-4/prism.model.umb models/consensus.4-4/property.props
Wallclock time: 7.246 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:20:46 GMT+01:00 2026
Hostname: r23m0061.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/consensus.4-4/prism.model.umb models/consensus.4-4/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [done]
Variables:   x
Labels:      "finished" "agree"

Parsing properties file "models/consensus.4-4/property.props"...

1 property:
(1) "disagree": Pmax=? [ F "finished"&!"agree" ]

---------------------------------------------------------------------

Model checking: "disagree": Pmax=? [ F "finished"&!"agree" ]

Building model (engine:explicit)...

Time for model construction: 0.153 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352
Choices:     115840
Max/avg:     4/2.69

Starting probabilistic reachability (max)...
Starting Prob0 (max)...
Prob0 (max) took 149 iterations and 0.092 seconds.
Starting Prob1 (max)...
Prob1 (max) took 2595 iterations and 1.558 seconds.
target=56, yes=10872, no=910, maybe=31354
Starting value iteration (max, with Power method)...
Value iteration (max, with Power method) took 6873 iterations, 812168664 multiplications and 3.65 seconds.
Probabilistic reachability took 5.316 seconds.

Value in the initial state: 0.15605695062063785

Time for model checking: 5.34 seconds.

Result: 0.15605695062063785 (+/- 1.5602125169600354E-6 estimated; rel err 9.99771244250946E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_consensus.4-4_rep2.log

```
Command(s):
../bin/prism -ex -importmodel models/consensus.4-4/prism.model.umb models/consensus.4-4/property.props
Wallclock time: 6.000 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:01:00 GMT+01:00 2026
Hostname: n23m0175.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/consensus.4-4/prism.model.umb models/consensus.4-4/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [done]
Variables:   x
Labels:      "finished" "agree"

Parsing properties file "models/consensus.4-4/property.props"...

1 property:
(1) "disagree": Pmax=? [ F "finished"&!"agree" ]

---------------------------------------------------------------------

Model checking: "disagree": Pmax=? [ F "finished"&!"agree" ]

Building model (engine:explicit)...

Time for model construction: 0.171 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352
Choices:     115840
Max/avg:     4/2.69

Starting probabilistic reachability (max)...
Starting Prob0 (max)...
Prob0 (max) took 149 iterations and 0.089 seconds.
Starting Prob1 (max)...
Prob1 (max) took 2595 iterations and 1.485 seconds.
target=56, yes=10872, no=910, maybe=31354
Starting value iteration (max, with Power method)...
Value iteration (max, with Power method) took 6873 iterations, 812168664 multiplications and 3.381 seconds.
Probabilistic reachability took 4.968 seconds.

Value in the initial state: 0.15605695062063785

Time for model checking: 4.986 seconds.

Result: 0.15605695062063785 (+/- 1.5602125169600354E-6 estimated; rel err 9.99771244250946E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_consensus.4-4_rep3.log

```
Command(s):
../bin/prism -ex -importmodel models/consensus.4-4/prism.model.umb models/consensus.4-4/property.props
Wallclock time: 5.895 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:15:51 GMT+01:00 2026
Hostname: n23m0168.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/consensus.4-4/prism.model.umb models/consensus.4-4/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [done]
Variables:   x
Labels:      "finished" "agree"

Parsing properties file "models/consensus.4-4/property.props"...

1 property:
(1) "disagree": Pmax=? [ F "finished"&!"agree" ]

---------------------------------------------------------------------

Model checking: "disagree": Pmax=? [ F "finished"&!"agree" ]

Building model (engine:explicit)...

Time for model construction: 0.073 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352
Choices:     115840
Max/avg:     4/2.69

Starting probabilistic reachability (max)...
Starting Prob0 (max)...
Prob0 (max) took 149 iterations and 0.082 seconds.
Starting Prob1 (max)...
Prob1 (max) took 2595 iterations and 1.43 seconds.
target=56, yes=10872, no=910, maybe=31354
Starting value iteration (max, with Power method)...
Value iteration (max, with Power method) took 6873 iterations, 812168664 multiplications and 3.4 seconds.
Probabilistic reachability took 4.923 seconds.

Value in the initial state: 0.15605695062063785

Time for model checking: 4.939 seconds.

Result: 0.15605695062063785 (+/- 1.5602125169600354E-6 estimated; rel err 9.99771244250946E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_consensus.4-4_rep4.log

```
Command(s):
../bin/prism -ex -importmodel models/consensus.4-4/prism.model.umb models/consensus.4-4/property.props
Wallclock time: 6.174 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:16:29 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/consensus.4-4/prism.model.umb models/consensus.4-4/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [done]
Variables:   x
Labels:      "finished" "agree"

Parsing properties file "models/consensus.4-4/property.props"...

1 property:
(1) "disagree": Pmax=? [ F "finished"&!"agree" ]

---------------------------------------------------------------------

Model checking: "disagree": Pmax=? [ F "finished"&!"agree" ]

Building model (engine:explicit)...

Time for model construction: 0.296 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352
Choices:     115840
Max/avg:     4/2.69

Starting probabilistic reachability (max)...
Starting Prob0 (max)...
Prob0 (max) took 149 iterations and 0.082 seconds.
Starting Prob1 (max)...
Prob1 (max) took 2595 iterations and 1.484 seconds.
target=56, yes=10872, no=910, maybe=31354
Starting value iteration (max, with Power method)...
Value iteration (max, with Power method) took 6873 iterations, 812168664 multiplications and 3.465 seconds.
Probabilistic reachability took 5.041 seconds.

Value in the initial state: 0.15605695062063785

Time for model checking: 5.06 seconds.

Result: 0.15605695062063785 (+/- 1.5602125169600354E-6 estimated; rel err 9.99771244250946E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_consensus.4-4_rep5.log

```
Command(s):
../bin/prism -ex -importmodel models/consensus.4-4/prism.model.umb models/consensus.4-4/property.props
Wallclock time: 6.142 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:18:59 GMT+01:00 2026
Hostname: n23m0355.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/consensus.4-4/prism.model.umb models/consensus.4-4/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [done]
Variables:   x
Labels:      "finished" "agree"

Parsing properties file "models/consensus.4-4/property.props"...

1 property:
(1) "disagree": Pmax=? [ F "finished"&!"agree" ]

---------------------------------------------------------------------

Model checking: "disagree": Pmax=? [ F "finished"&!"agree" ]

Building model (engine:explicit)...

Time for model construction: 0.313 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352
Choices:     115840
Max/avg:     4/2.69

Starting probabilistic reachability (max)...
Starting Prob0 (max)...
Prob0 (max) took 149 iterations and 0.076 seconds.
Starting Prob1 (max)...
Prob1 (max) took 2595 iterations and 1.398 seconds.
target=56, yes=10872, no=910, maybe=31354
Starting value iteration (max, with Power method)...
Value iteration (max, with Power method) took 6873 iterations, 812168664 multiplications and 3.387 seconds.
Probabilistic reachability took 4.873 seconds.

Value in the initial state: 0.15605695062063785

Time for model checking: 4.892 seconds.

Result: 0.15605695062063785 (+/- 1.5602125169600354E-6 estimated; rel err 9.99771244250946E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

