# Log files

Tool configuration: prism_from-umb_check_ex
Benchmark: [wlan.5-0](../../models/wlan.5-0)
Parsed values: [0.34, 0.434, 0.509, 0.598, 0.38]



### Log file: prism_from-umb_check_ex_wlan.5-0_rep1.log

```
Command(s):
../bin/prism -ex -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props
Wallclock time: 37.528 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:43:44 GMT+01:00 2026
Hostname: r23m0066.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   x
Labels:      "target"

Parsing properties file "models/wlan.5-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:explicit)...

Time for model construction: 0.34 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960
Choices:     1646074
Max/avg:     3/1.27

Starting probabilistic reachability (min)...
Starting Prob0 (min)...
Prob0 (min) took 1622 iterations and 16.141 seconds.
Starting Prob1 (min)...
Prob1 (min) took 1622 iterations and 20.142 seconds.
target=1, yes=1295218, no=0, maybe=0
Probabilistic reachability took 36.302 seconds.

Property satisfied in 1 of 1 initial states.

Time for model checking: 36.387 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_wlan.5-0_rep2.log

```
Command(s):
../bin/prism -ex -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props
Wallclock time: 45.828 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:02 GMT+01:00 2026
Hostname: n23m0252.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   x
Labels:      "target"

Parsing properties file "models/wlan.5-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:explicit)...

Time for model construction: 0.434 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960
Choices:     1646074
Max/avg:     3/1.27

Starting probabilistic reachability (min)...
Starting Prob0 (min)...
Prob0 (min) took 1622 iterations and 19.855 seconds.
Starting Prob1 (min)...
Prob1 (min) took 1622 iterations and 24.436 seconds.
target=1, yes=1295218, no=0, maybe=0
Probabilistic reachability took 44.314 seconds.

Property satisfied in 1 of 1 initial states.

Time for model checking: 44.402 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_wlan.5-0_rep3.log

```
Command(s):
../bin/prism -ex -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props
Wallclock time: 34.255 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:09:08 GMT+01:00 2026
Hostname: n23m0272.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   x
Labels:      "target"

Parsing properties file "models/wlan.5-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:explicit)...

Time for model construction: 0.509 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960
Choices:     1646074
Max/avg:     3/1.27

Starting probabilistic reachability (min)...
Starting Prob0 (min)...
Prob0 (min) took 1622 iterations and 14.37 seconds.
Starting Prob1 (min)...
Prob1 (min) took 1622 iterations and 18.359 seconds.
target=1, yes=1295218, no=0, maybe=0
Probabilistic reachability took 32.747 seconds.

Property satisfied in 1 of 1 initial states.

Time for model checking: 32.807 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_wlan.5-0_rep4.log

```
Command(s):
../bin/prism -ex -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props
Wallclock time: 41.785 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:25:14 GMT+01:00 2026
Hostname: n23m0250.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   x
Labels:      "target"

Parsing properties file "models/wlan.5-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:explicit)...

Time for model construction: 0.598 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960
Choices:     1646074
Max/avg:     3/1.27

Starting probabilistic reachability (min)...
Starting Prob0 (min)...
Prob0 (min) took 1622 iterations and 17.135 seconds.
Starting Prob1 (min)...
Prob1 (min) took 1622 iterations and 22.938 seconds.
target=1, yes=1295218, no=0, maybe=0
Probabilistic reachability took 40.1 seconds.

Property satisfied in 1 of 1 initial states.

Time for model checking: 40.168 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_wlan.5-0_rep5.log

```
Command(s):
../bin/prism -ex -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props
Wallclock time: 41.451 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:05 GMT+01:00 2026
Hostname: n23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/wlan.5-0/prism.model.umb models/wlan.5-0/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   x
Labels:      "target"

Parsing properties file "models/wlan.5-0/property.props"...

1 property:
(1) "sent": P>=1 [ F "target" ]

---------------------------------------------------------------------

Model checking: "sent": P>=1 [ F "target" ]

Building model (engine:explicit)...

Time for model construction: 0.38 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960
Choices:     1646074
Max/avg:     3/1.27

Starting probabilistic reachability (min)...
Starting Prob0 (min)...
Prob0 (min) took 1622 iterations and 15.801 seconds.
Starting Prob1 (min)...
Prob1 (min) took 1622 iterations and 20.261 seconds.
target=1, yes=1295218, no=0, maybe=0
Probabilistic reachability took 36.088 seconds.

Property satisfied in 1 of 1 initial states.

Time for model checking: 36.175 seconds.

Result: true


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

