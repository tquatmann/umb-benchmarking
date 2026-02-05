# Log files for prism_from-prism_check_ex on model [csma.4-2](../../models/csma.4-2)

Parsed values: `[16.551, 17.772, 16.402, 16.032, 16.649]`



### Log file: prism_from-prism_check_ex_csma.4-2_rep1.log

```
Command(s):
../bin/prism -ex models/csma.4-2/model.prism models/csma.4-2/property.props
Wallclock time: 16.551 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:44:46 GMT+01:00 2026
Hostname: r23m0141.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.4-2/model.prism models/csma.4-2/property.props

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.4-2/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:explicit)...

Computing reachable states... 685275 761962 states
Reachable states exploration and model construction done in 3.381 secs.
Sorting reachable states list...

Time for model construction: 4.087 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068
Choices:     825504
Max/avg:     4/1.08

Starting probabilistic reachability (max)...
Starting Prob0 (max)...
Prob0 (max) took 186 iterations and 1.241 seconds.
Starting Prob1 (max)...
Prob1 (max) took 1197 iterations and 9.38 seconds.
target=9, yes=142601, no=25408, maybe=593953
Starting value iteration (max, with Power method)...
Value iteration (max, with Power method) took 172 iterations, 190125188 multiplications and 1.143 seconds.
Probabilistic reachability took 11.78 seconds.

Value in the initial state: 0.776459404375732

Time for model checking: 11.832 seconds.

Result: 0.776459404375732 (+/- 6.170079467349154E-6 estimated; rel err 7.946428921560754E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_csma.4-2_rep2.log

```
Command(s):
../bin/prism -ex models/csma.4-2/model.prism models/csma.4-2/property.props
Wallclock time: 17.772 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:22:07 GMT+01:00 2026
Hostname: n23m0243.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.4-2/model.prism models/csma.4-2/property.props

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.4-2/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:explicit)...

Computing reachable states... 672594 761962 states
Reachable states exploration and model construction done in 3.428 secs.
Sorting reachable states list...

Time for model construction: 4.284 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068
Choices:     825504
Max/avg:     4/1.08

Starting probabilistic reachability (max)...
Starting Prob0 (max)...
Prob0 (max) took 186 iterations and 1.235 seconds.
Starting Prob1 (max)...
Prob1 (max) took 1197 iterations and 8.942 seconds.
target=9, yes=142601, no=25408, maybe=593953
Starting value iteration (max, with Power method)...
Value iteration (max, with Power method) took 172 iterations, 190125188 multiplications and 1.151 seconds.
Probabilistic reachability took 11.371 seconds.

Value in the initial state: 0.776459404375732

Time for model checking: 11.445 seconds.

Result: 0.776459404375732 (+/- 6.170079467349154E-6 estimated; rel err 7.946428921560754E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_csma.4-2_rep3.log

```
Command(s):
../bin/prism -ex models/csma.4-2/model.prism models/csma.4-2/property.props
Wallclock time: 16.402 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:10:10 GMT+01:00 2026
Hostname: r23m0219.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.4-2/model.prism models/csma.4-2/property.props

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.4-2/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:explicit)...

Computing reachable states... 687747 761962 states
Reachable states exploration and model construction done in 3.348 secs.
Sorting reachable states list...

Time for model construction: 4.156 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068
Choices:     825504
Max/avg:     4/1.08

Starting probabilistic reachability (max)...
Starting Prob0 (max)...
Prob0 (max) took 186 iterations and 1.253 seconds.
Starting Prob1 (max)...
Prob1 (max) took 1197 iterations and 9.268 seconds.
target=9, yes=142601, no=25408, maybe=593953
Starting value iteration (max, with Power method)...
Value iteration (max, with Power method) took 172 iterations, 190125188 multiplications and 0.998 seconds.
Probabilistic reachability took 11.54 seconds.

Value in the initial state: 0.776459404375732

Time for model checking: 11.589 seconds.

Result: 0.776459404375732 (+/- 6.170079467349154E-6 estimated; rel err 7.946428921560754E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_csma.4-2_rep4.log

```
Command(s):
../bin/prism -ex models/csma.4-2/model.prism models/csma.4-2/property.props
Wallclock time: 16.032 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:23:31 GMT+01:00 2026
Hostname: n23m0058.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.4-2/model.prism models/csma.4-2/property.props

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.4-2/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:explicit)...

Computing reachable states... 700758 761962 states
Reachable states exploration and model construction done in 3.254 secs.
Sorting reachable states list...

Time for model construction: 4.013 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068
Choices:     825504
Max/avg:     4/1.08

Starting probabilistic reachability (max)...
Starting Prob0 (max)...
Prob0 (max) took 186 iterations and 1.226 seconds.
Starting Prob1 (max)...
Prob1 (max) took 1197 iterations and 8.997 seconds.
target=9, yes=142601, no=25408, maybe=593953
Starting value iteration (max, with Power method)...
Value iteration (max, with Power method) took 172 iterations, 190125188 multiplications and 1.1 seconds.
Probabilistic reachability took 11.339 seconds.

Value in the initial state: 0.776459404375732

Time for model checking: 11.388 seconds.

Result: 0.776459404375732 (+/- 6.170079467349154E-6 estimated; rel err 7.946428921560754E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_csma.4-2_rep5.log

```
Command(s):
../bin/prism -ex models/csma.4-2/model.prism models/csma.4-2/property.props
Wallclock time: 16.649 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:06 GMT+01:00 2026
Hostname: r23m0136.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.4-2/model.prism models/csma.4-2/property.props

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Parsing properties file "models/csma.4-2/property.props"...

1 property:
(1) "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

---------------------------------------------------------------------

Model checking: "all_before_max": Pmax=? [ !"collision_max_backoff" U "all_delivered" ]

Building model (engine:explicit)...

Computing reachable states... 673065 761962 states
Reachable states exploration and model construction done in 3.407 secs.
Sorting reachable states list...

Time for model construction: 4.202 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068
Choices:     825504
Max/avg:     4/1.08

Starting probabilistic reachability (max)...
Starting Prob0 (max)...
Prob0 (max) took 186 iterations and 1.222 seconds.
Starting Prob1 (max)...
Prob1 (max) took 1197 iterations and 8.976 seconds.
target=9, yes=142601, no=25408, maybe=593953
Starting value iteration (max, with Power method)...
Value iteration (max, with Power method) took 172 iterations, 190125188 multiplications and 1.123 seconds.
Probabilistic reachability took 11.341 seconds.

Value in the initial state: 0.776459404375732

Time for model checking: 11.391 seconds.

Result: 0.776459404375732 (+/- 6.170079467349154E-6 estimated; rel err 7.946428921560754E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

