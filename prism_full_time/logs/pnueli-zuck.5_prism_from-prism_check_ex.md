# Log files for prism_from-prism_check_ex on model [pnueli-zuck.5](../../models/pnueli-zuck.5)

Parsed values: `[4.323, 4.352, 5.151, 4.997, 4.6]`



### Log file: prism_from-prism_check_ex_pnueli-zuck.5_rep1.log

```
Command(s):
../bin/prism -ex models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props
Wallclock time: 4.323 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:49:26 GMT+01:00 2026
Hostname: n23m0099.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props

Parsing PRISM model file "models/pnueli-zuck.5/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4
Actions:     []
Variables:   p0 p1 p2 p3 p4
Labels:      "target"

Parsing properties file "models/pnueli-zuck.5/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 397435 states
Reachable states exploration and model construction done in 2.533 secs.
Sorting reachable states list...

Time for model construction: 3.173 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2313746
Choices:     2145026
Max/avg:     10/5.40

Starting probabilistic reachability (max)...
Starting Prob0 (max)...
Prob0 (max) took 45 iterations and 0.206 seconds.
Starting Prob1 (max)...
Prob1 (max) took 45 iterations and 0.245 seconds.
target=10000, yes=397435, no=0, maybe=0
Probabilistic reachability took 0.467 seconds.

Value in the initial state: 1.0

Time for model checking: 0.497 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_pnueli-zuck.5_rep2.log

```
Command(s):
../bin/prism -ex models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props
Wallclock time: 4.352 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:19 GMT+01:00 2026
Hostname: n23m0396.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props

Parsing PRISM model file "models/pnueli-zuck.5/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4
Actions:     []
Variables:   p0 p1 p2 p3 p4
Labels:      "target"

Parsing properties file "models/pnueli-zuck.5/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 397435 states
Reachable states exploration and model construction done in 2.475 secs.
Sorting reachable states list...

Time for model construction: 3.082 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2313746
Choices:     2145026
Max/avg:     10/5.40

Starting probabilistic reachability (max)...
Starting Prob0 (max)...
Prob0 (max) took 45 iterations and 0.21 seconds.
Starting Prob1 (max)...
Prob1 (max) took 45 iterations and 0.247 seconds.
target=10000, yes=397435, no=0, maybe=0
Probabilistic reachability took 0.473 seconds.

Value in the initial state: 1.0

Time for model checking: 0.505 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_pnueli-zuck.5_rep3.log

```
Command(s):
../bin/prism -ex models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props
Wallclock time: 5.151 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:38 GMT+01:00 2026
Hostname: r23m0052.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props

Parsing PRISM model file "models/pnueli-zuck.5/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4
Actions:     []
Variables:   p0 p1 p2 p3 p4
Labels:      "target"

Parsing properties file "models/pnueli-zuck.5/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 393950 397435 states
Reachable states exploration and model construction done in 3.038 secs.
Sorting reachable states list...

Time for model construction: 3.774 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2313746
Choices:     2145026
Max/avg:     10/5.40

Starting probabilistic reachability (max)...
Starting Prob0 (max)...
Prob0 (max) took 45 iterations and 0.247 seconds.
Starting Prob1 (max)...
Prob1 (max) took 45 iterations and 0.288 seconds.
target=10000, yes=397435, no=0, maybe=0
Probabilistic reachability took 0.553 seconds.

Value in the initial state: 1.0

Time for model checking: 0.589 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_pnueli-zuck.5_rep4.log

```
Command(s):
../bin/prism -ex models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props
Wallclock time: 4.997 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:05:03 GMT+01:00 2026
Hostname: n23m0111.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props

Parsing PRISM model file "models/pnueli-zuck.5/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4
Actions:     []
Variables:   p0 p1 p2 p3 p4
Labels:      "target"

Parsing properties file "models/pnueli-zuck.5/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 397435 states
Reachable states exploration and model construction done in 2.964 secs.
Sorting reachable states list...

Time for model construction: 3.723 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2313746
Choices:     2145026
Max/avg:     10/5.40

Starting probabilistic reachability (max)...
Starting Prob0 (max)...
Prob0 (max) took 45 iterations and 0.24 seconds.
Starting Prob1 (max)...
Prob1 (max) took 45 iterations and 0.297 seconds.
target=10000, yes=397435, no=0, maybe=0
Probabilistic reachability took 0.551 seconds.

Value in the initial state: 1.0

Time for model checking: 0.581 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_pnueli-zuck.5_rep5.log

```
Command(s):
../bin/prism -ex models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props
Wallclock time: 4.600 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:38:12 GMT+01:00 2026
Hostname: n23m0191.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pnueli-zuck.5/model.prism models/pnueli-zuck.5/property.props

Parsing PRISM model file "models/pnueli-zuck.5/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4
Actions:     []
Variables:   p0 p1 p2 p3 p4
Labels:      "target"

Parsing properties file "models/pnueli-zuck.5/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 397435 states
Reachable states exploration and model construction done in 2.44 secs.
Sorting reachable states list...

Time for model construction: 3.066 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2313746
Choices:     2145026
Max/avg:     10/5.40

Starting probabilistic reachability (max)...
Starting Prob0 (max)...
Prob0 (max) took 45 iterations and 0.21 seconds.
Starting Prob1 (max)...
Prob1 (max) took 45 iterations and 0.246 seconds.
target=10000, yes=397435, no=0, maybe=0
Probabilistic reachability took 0.471 seconds.

Value in the initial state: 1.0

Time for model checking: 0.505 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

