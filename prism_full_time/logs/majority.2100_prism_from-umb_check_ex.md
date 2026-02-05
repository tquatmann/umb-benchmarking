# Log files

Tool configuration: prism_from-umb_check_ex
Benchmark: [majority.2100](../../models/majority.2100)
Parsed values: [375.669, 380.117, 398.624, 412.174, 403.113]



### Log file: prism_from-umb_check_ex_majority.2100_rep1.log

```
Command(s):
../bin/prism -ex -importmodel models/majority.2100/prism.model.umb models/majority.2100/property.props
Wallclock time: 375.669 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:17:09 GMT+01:00 2026
Hostname: r23m0080.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/majority.2100/prism.model.umb models/majority.2100/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/majority.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:explicit)...

Time for model construction: 0.353 seconds.

Type:        CTMC
States:      192000 (1 initial)
Transitions: 1961600

Starting backwards transient probability computation...

Uniformisation: q.t = 3.2872265951801265 x 2100.0 = 6903.175849878266
Fox-Glynn (1.25E-7): left = 6319, right = 7610
Backwards transient probability computation took 7611 iters and 373.682 seconds.

Value in the initial state: 0.054299193162504665

Time for model checking: 373.706 seconds.

Result: 0.054299193162504665


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_majority.2100_rep2.log

```
Command(s):
../bin/prism -ex -importmodel models/majority.2100/prism.model.umb models/majority.2100/property.props
Wallclock time: 380.117 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:08:19 GMT+01:00 2026
Hostname: r23m0214.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/majority.2100/prism.model.umb models/majority.2100/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/majority.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:explicit)...

Time for model construction: 0.616 seconds.

Type:        CTMC
States:      192000 (1 initial)
Transitions: 1961600

Starting backwards transient probability computation...

Uniformisation: q.t = 3.2872265951801265 x 2100.0 = 6903.175849878266
Fox-Glynn (1.25E-7): left = 6319, right = 7610
Backwards transient probability computation took 7611 iters and 378.485 seconds.

Value in the initial state: 0.054299193162504665

Time for model checking: 378.507 seconds.

Result: 0.054299193162504665


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_majority.2100_rep3.log

```
Command(s):
../bin/prism -ex -importmodel models/majority.2100/prism.model.umb models/majority.2100/property.props
Wallclock time: 398.624 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:58:24 GMT+01:00 2026
Hostname: n23m0261.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/majority.2100/prism.model.umb models/majority.2100/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/majority.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:explicit)...

Time for model construction: 0.383 seconds.

Type:        CTMC
States:      192000 (1 initial)
Transitions: 1961600

Starting backwards transient probability computation...

Uniformisation: q.t = 3.2872265951801265 x 2100.0 = 6903.175849878266
Fox-Glynn (1.25E-7): left = 6319, right = 7610
Backwards transient probability computation took 7611 iters and 397.35 seconds.

Value in the initial state: 0.054299193162504665

Time for model checking: 397.373 seconds.

Result: 0.054299193162504665


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_majority.2100_rep4.log

```
Command(s):
../bin/prism -ex -importmodel models/majority.2100/prism.model.umb models/majority.2100/property.props
Wallclock time: 412.174 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 02:50:14 GMT+01:00 2026
Hostname: n23m0033.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/majority.2100/prism.model.umb models/majority.2100/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/majority.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:explicit)...

Time for model construction: 0.393 seconds.

Type:        CTMC
States:      192000 (1 initial)
Transitions: 1961600

Starting backwards transient probability computation...

Uniformisation: q.t = 3.2872265951801265 x 2100.0 = 6903.175849878266
Fox-Glynn (1.25E-7): left = 6319, right = 7610
Backwards transient probability computation took 7611 iters and 409.357 seconds.

Value in the initial state: 0.054299193162504665

Time for model checking: 409.392 seconds.

Result: 0.054299193162504665


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_majority.2100_rep5.log

```
Command(s):
../bin/prism -ex -importmodel models/majority.2100/prism.model.umb models/majority.2100/property.props
Wallclock time: 403.113 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:40 GMT+01:00 2026
Hostname: n23m0124.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/majority.2100/prism.model.umb models/majority.2100/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/majority.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:explicit)...

Time for model construction: 0.286 seconds.

Type:        CTMC
States:      192000 (1 initial)
Transitions: 1961600

Starting backwards transient probability computation...

Uniformisation: q.t = 3.2872265951801265 x 2100.0 = 6903.175849878266
Fox-Glynn (1.25E-7): left = 6319, right = 7610
Backwards transient probability computation took 7611 iters and 402.02 seconds.

Value in the initial state: 0.054299193162504665

Time for model checking: 402.044 seconds.

Result: 0.054299193162504665


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

