# Log files for prism_from-umb_check_ex on model [resource-gathering.1300-100-100](../../models/resource-gathering.1300-100-100)

Parsed values: `[24.719, 22.089, 22.606, 21.035, 24.914]`



### Log file: prism_from-umb_check_ex_resource-gathering.1300-100-100_rep1.log

```
Command(s):
../bin/prism -ex -importmodel models/resource-gathering.1300-100-100/prism.model.umb models/resource-gathering.1300-100-100/property.props
Wallclock time: 24.719 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:41:39 GMT+01:00 2026
Hostname: r23m0197.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/resource-gathering.1300-100-100/prism.model.umb models/resource-gathering.1300-100-100/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [right] [left] [top] [down]
Variables:   x
Labels:      "success"

Parsing properties file "models/resource-gathering.1300-100-100/property.props"...

1 property:
(1) "prgoldgem": Pmax=? [ F<=1300 "success" ]

---------------------------------------------------------------------

Model checking: "prgoldgem": Pmax=? [ F<=1300 "success" ]

Building model (engine:explicit)...

Time for model construction: 0.661 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526
Choices:     3080702
Max/avg:     4/3.21

Starting bounded probabilistic reachability (max)...
Bounded probabilistic reachability (max) took 1300 iterations and 22.949 seconds.

Value in the initial state: 0.6630608525241822

Time for model checking: 23.001 seconds.

Result: 0.6630608525241822 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_resource-gathering.1300-100-100_rep2.log

```
Command(s):
../bin/prism -ex -importmodel models/resource-gathering.1300-100-100/prism.model.umb models/resource-gathering.1300-100-100/property.props
Wallclock time: 22.089 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:00:57 GMT+01:00 2026
Hostname: n23m0168.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/resource-gathering.1300-100-100/prism.model.umb models/resource-gathering.1300-100-100/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [right] [left] [top] [down]
Variables:   x
Labels:      "success"

Parsing properties file "models/resource-gathering.1300-100-100/property.props"...

1 property:
(1) "prgoldgem": Pmax=? [ F<=1300 "success" ]

---------------------------------------------------------------------

Model checking: "prgoldgem": Pmax=? [ F<=1300 "success" ]

Building model (engine:explicit)...

Time for model construction: 0.558 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526
Choices:     3080702
Max/avg:     4/3.21

Starting bounded probabilistic reachability (max)...
Bounded probabilistic reachability (max) took 1300 iterations and 20.564 seconds.

Value in the initial state: 0.6630608525241822

Time for model checking: 20.609 seconds.

Result: 0.6630608525241822 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_resource-gathering.1300-100-100_rep3.log

```
Command(s):
../bin/prism -ex -importmodel models/resource-gathering.1300-100-100/prism.model.umb models/resource-gathering.1300-100-100/property.props
Wallclock time: 22.606 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 02:55:51 GMT+01:00 2026
Hostname: n23m0323.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/resource-gathering.1300-100-100/prism.model.umb models/resource-gathering.1300-100-100/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [right] [left] [top] [down]
Variables:   x
Labels:      "success"

Parsing properties file "models/resource-gathering.1300-100-100/property.props"...

1 property:
(1) "prgoldgem": Pmax=? [ F<=1300 "success" ]

---------------------------------------------------------------------

Model checking: "prgoldgem": Pmax=? [ F<=1300 "success" ]

Building model (engine:explicit)...

Time for model construction: 0.544 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526
Choices:     3080702
Max/avg:     4/3.21

Starting bounded probabilistic reachability (max)...
Bounded probabilistic reachability (max) took 1300 iterations and 20.826 seconds.

Value in the initial state: 0.6630608525241822

Time for model checking: 20.878 seconds.

Result: 0.6630608525241822 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_resource-gathering.1300-100-100_rep4.log

```
Command(s):
../bin/prism -ex -importmodel models/resource-gathering.1300-100-100/prism.model.umb models/resource-gathering.1300-100-100/property.props
Wallclock time: 21.035 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:55:32 GMT+01:00 2026
Hostname: n23m0307.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/resource-gathering.1300-100-100/prism.model.umb models/resource-gathering.1300-100-100/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [right] [left] [top] [down]
Variables:   x
Labels:      "success"

Parsing properties file "models/resource-gathering.1300-100-100/property.props"...

1 property:
(1) "prgoldgem": Pmax=? [ F<=1300 "success" ]

---------------------------------------------------------------------

Model checking: "prgoldgem": Pmax=? [ F<=1300 "success" ]

Building model (engine:explicit)...

Time for model construction: 0.339 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526
Choices:     3080702
Max/avg:     4/3.21

Starting bounded probabilistic reachability (max)...
Bounded probabilistic reachability (max) took 1300 iterations and 19.931 seconds.

Value in the initial state: 0.6630608525241822

Time for model checking: 19.976 seconds.

Result: 0.6630608525241822 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_resource-gathering.1300-100-100_rep5.log

```
Command(s):
../bin/prism -ex -importmodel models/resource-gathering.1300-100-100/prism.model.umb models/resource-gathering.1300-100-100/property.props
Wallclock time: 24.914 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:15:51 GMT+01:00 2026
Hostname: n23m0036.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/resource-gathering.1300-100-100/prism.model.umb models/resource-gathering.1300-100-100/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [right] [left] [top] [down]
Variables:   x
Labels:      "success"

Parsing properties file "models/resource-gathering.1300-100-100/property.props"...

1 property:
(1) "prgoldgem": Pmax=? [ F<=1300 "success" ]

---------------------------------------------------------------------

Model checking: "prgoldgem": Pmax=? [ F<=1300 "success" ]

Building model (engine:explicit)...

Time for model construction: 0.501 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526
Choices:     3080702
Max/avg:     4/3.21

Starting bounded probabilistic reachability (max)...
Bounded probabilistic reachability (max) took 1300 iterations and 23.215 seconds.

Value in the initial state: 0.6630608525241822

Time for model checking: 23.34 seconds.

Result: 0.6630608525241822 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

