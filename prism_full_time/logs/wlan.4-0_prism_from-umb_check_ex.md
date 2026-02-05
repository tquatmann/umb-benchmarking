# Log files

Tool configuration: prism_from-umb_check_ex
Benchmark: [wlan.4-0](../../models/wlan.4-0)
Parsed values: [7.163, 7.472, 6.22, 7.486, 6.255]



### Log file: prism_from-umb_check_ex_wlan.4-0_rep1.log

```
Command(s):
../bin/prism -ex -importmodel models/wlan.4-0/prism.model.umb models/wlan.4-0/property.props
Wallclock time: 7.163 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:32:51 GMT+01:00 2026
Hostname: n23m0275.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/wlan.4-0/prism.model.umb models/wlan.4-0/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   x
Labels:      "target"

Parsing properties file "models/wlan.4-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:explicit)...

Time for model construction: 0.165 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Starting probabilistic reachability (min)...
Starting Prob0 (min)...
Prob0 (min) took 854 iterations and 2.765 seconds.
Starting Prob1 (min)...
Prob1 (min) took 854 iterations and 3.374 seconds.
target=1, yes=345000, no=0, maybe=0
Probabilistic reachability took 6.154 seconds.

Property satisfied in 1 of 1 initial states.

Time for model checking: 6.186 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_wlan.4-0_rep2.log

```
Command(s):
../bin/prism -ex -importmodel models/wlan.4-0/prism.model.umb models/wlan.4-0/property.props
Wallclock time: 7.472 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:51:28 GMT+01:00 2026
Hostname: n23m0335.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/wlan.4-0/prism.model.umb models/wlan.4-0/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   x
Labels:      "target"

Parsing properties file "models/wlan.4-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:explicit)...

Time for model construction: 0.295 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Starting probabilistic reachability (min)...
Starting Prob0 (min)...
Prob0 (min) took 854 iterations and 2.531 seconds.
Starting Prob1 (min)...
Prob1 (min) took 854 iterations and 3.062 seconds.
target=1, yes=345000, no=0, maybe=0
Probabilistic reachability took 5.632 seconds.

Property satisfied in 1 of 1 initial states.

Time for model checking: 5.664 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_wlan.4-0_rep3.log

```
Command(s):
../bin/prism -ex -importmodel models/wlan.4-0/prism.model.umb models/wlan.4-0/property.props
Wallclock time: 6.220 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:36:42 GMT+01:00 2026
Hostname: n23m0046.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/wlan.4-0/prism.model.umb models/wlan.4-0/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   x
Labels:      "target"

Parsing properties file "models/wlan.4-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:explicit)...

Time for model construction: 0.186 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Starting probabilistic reachability (min)...
Starting Prob0 (min)...
Prob0 (min) took 854 iterations and 2.096 seconds.
Starting Prob1 (min)...
Prob1 (min) took 854 iterations and 2.719 seconds.
target=1, yes=345000, no=0, maybe=0
Probabilistic reachability took 4.83 seconds.

Property satisfied in 1 of 1 initial states.

Time for model checking: 4.866 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_wlan.4-0_rep4.log

```
Command(s):
../bin/prism -ex -importmodel models/wlan.4-0/prism.model.umb models/wlan.4-0/property.props
Wallclock time: 7.486 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:23:26 GMT+01:00 2026
Hostname: n23m0042.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/wlan.4-0/prism.model.umb models/wlan.4-0/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   x
Labels:      "target"

Parsing properties file "models/wlan.4-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:explicit)...

Time for model construction: 0.329 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Starting probabilistic reachability (min)...
Starting Prob0 (min)...
Prob0 (min) took 854 iterations and 2.577 seconds.
Starting Prob1 (min)...
Prob1 (min) took 854 iterations and 3.319 seconds.
target=1, yes=345000, no=0, maybe=0
Probabilistic reachability took 5.912 seconds.

Property satisfied in 1 of 1 initial states.

Time for model checking: 5.951 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_wlan.4-0_rep5.log

```
Command(s):
../bin/prism -ex -importmodel models/wlan.4-0/prism.model.umb models/wlan.4-0/property.props
Wallclock time: 6.255 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:07 GMT+01:00 2026
Hostname: n23m0237.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/wlan.4-0/prism.model.umb models/wlan.4-0/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   x
Labels:      "target"

Parsing properties file "models/wlan.4-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:explicit)...

Time for model construction: 0.164 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Starting probabilistic reachability (min)...
Starting Prob0 (min)...
Prob0 (min) took 854 iterations and 2.406 seconds.
Starting Prob1 (min)...
Prob1 (min) took 854 iterations and 2.925 seconds.
target=1, yes=345000, no=0, maybe=0
Probabilistic reachability took 5.343 seconds.

Property satisfied in 1 of 1 initial states.

Time for model checking: 5.374 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

