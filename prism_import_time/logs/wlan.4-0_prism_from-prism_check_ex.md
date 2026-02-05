# Log files for prism_from-prism_check_ex on model [wlan.4-0](../../models/wlan.4-0)

Parsed values: `[1.709, 1.588, 1.755, 1.844, 1.687]`



### Log file: prism_from-prism_check_ex_wlan.4-0_rep1.log

```
Command(s):
../bin/prism -ex models/wlan.4-0/model.prism models/wlan.4-0/property.props
Wallclock time: 8.064 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:47:53 GMT+01:00 2026
Hostname: r23m0197.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.4-0/model.prism models/wlan.4-0/property.props

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Parsing properties file "models/wlan.4-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 345000 states
Reachable states exploration and model construction done in 1.437 secs.
Sorting reachable states list...

Time for model construction: 1.709 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Starting probabilistic reachability (min)...
Starting Prob0 (min)...
Prob0 (min) took 854 iterations and 2.418 seconds.
Starting Prob1 (min)...
Prob1 (min) took 854 iterations and 3.189 seconds.
target=1, yes=345000, no=0, maybe=0
Probabilistic reachability took 5.62 seconds.

Property satisfied in 1 of 1 initial states.

Time for model checking: 5.655 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_wlan.4-0_rep2.log

```
Command(s):
../bin/prism -ex models/wlan.4-0/model.prism models/wlan.4-0/property.props
Wallclock time: 7.525 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:11:23 GMT+01:00 2026
Hostname: n23m0294.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.4-0/model.prism models/wlan.4-0/property.props

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Parsing properties file "models/wlan.4-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 345000 states
Reachable states exploration and model construction done in 1.336 secs.
Sorting reachable states list...

Time for model construction: 1.588 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Starting probabilistic reachability (min)...
Starting Prob0 (min)...
Prob0 (min) took 854 iterations and 2.215 seconds.
Starting Prob1 (min)...
Prob1 (min) took 854 iterations and 2.88 seconds.
target=1, yes=345000, no=0, maybe=0
Probabilistic reachability took 5.11 seconds.

Property satisfied in 1 of 1 initial states.

Time for model checking: 5.144 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_wlan.4-0_rep3.log

```
Command(s):
../bin/prism -ex models/wlan.4-0/model.prism models/wlan.4-0/property.props
Wallclock time: 8.057 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:24:22 GMT+01:00 2026
Hostname: n23m0328.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.4-0/model.prism models/wlan.4-0/property.props

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Parsing properties file "models/wlan.4-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 345000 states
Reachable states exploration and model construction done in 1.43 secs.
Sorting reachable states list...

Time for model construction: 1.755 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Starting probabilistic reachability (min)...
Starting Prob0 (min)...
Prob0 (min) took 854 iterations and 2.409 seconds.
Starting Prob1 (min)...
Prob1 (min) took 854 iterations and 3.155 seconds.
target=1, yes=345000, no=0, maybe=0
Probabilistic reachability took 5.581 seconds.

Property satisfied in 1 of 1 initial states.

Time for model checking: 5.617 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_wlan.4-0_rep4.log

```
Command(s):
../bin/prism -ex models/wlan.4-0/model.prism models/wlan.4-0/property.props
Wallclock time: 8.615 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:09:09 GMT+01:00 2026
Hostname: n23m0264.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.4-0/model.prism models/wlan.4-0/property.props

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Parsing properties file "models/wlan.4-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 345000 states
Reachable states exploration and model construction done in 1.443 secs.
Sorting reachable states list...

Time for model construction: 1.844 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Starting probabilistic reachability (min)...
Starting Prob0 (min)...
Prob0 (min) took 854 iterations and 2.642 seconds.
Starting Prob1 (min)...
Prob1 (min) took 854 iterations and 3.323 seconds.
target=1, yes=345000, no=0, maybe=0
Probabilistic reachability took 5.979 seconds.

Property satisfied in 1 of 1 initial states.

Time for model checking: 6.047 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_wlan.4-0_rep5.log

```
Command(s):
../bin/prism -ex models/wlan.4-0/model.prism models/wlan.4-0/property.props
Wallclock time: 7.378 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:28:56 GMT+01:00 2026
Hostname: n23m0031.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.4-0/model.prism models/wlan.4-0/property.props

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Parsing properties file "models/wlan.4-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 345000 states
Reachable states exploration and model construction done in 1.267 secs.
Sorting reachable states list...

Time for model construction: 1.687 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Starting probabilistic reachability (min)...
Starting Prob0 (min)...
Prob0 (min) took 854 iterations and 2.138 seconds.
Starting Prob1 (min)...
Prob1 (min) took 854 iterations and 2.849 seconds.
target=1, yes=345000, no=0, maybe=0
Probabilistic reachability took 5.0 seconds.

Property satisfied in 1 of 1 initial states.

Time for model checking: 5.056 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

