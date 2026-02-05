# Log files

Tool configuration: prism_from-prism_check_ex
Benchmark: [majority.2100](../../models/majority.2100)
Parsed values: [458.237, 471.677, 407.744, 422.863, 424.513]



### Log file: prism_from-prism_check_ex_majority.2100_rep1.log

```
Command(s):
../bin/prism -ex models/majority.2100/model.prism models/majority.2100/property.props
Wallclock time: 458.237 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:48:24 GMT+01:00 2026
Hostname: r23m0083.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/majority.2100/model.prism models/majority.2100/property.props

Parsing PRISM model file "models/majority.2100/model.prism"...

Type:        CTMC
Modules:     D_def Y_def Z_def CC_def XX_def EE_def
Actions:     []
Variables:   D Y Z CC XX EE
Labels:      "target"

Parsing properties file "models/majority.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:explicit)...

Computing reachable states... 192000 states
Reachable states exploration and model construction done in 1.139 secs.
Sorting reachable states list...

Time for model construction: 1.532 seconds.

Type:        CTMC
States:      192000 (1 initial)
Transitions: 1961600

Starting backwards transient probability computation...

Uniformisation: q.t = 3.2872265951801265 x 2100.0 = 6903.175849878266
Fox-Glynn (1.25E-7): left = 6319, right = 7610
Backwards transient probability computation took 7611 iters and 454.888 seconds.

Value in the initial state: 0.054299193162504256

Time for model checking: 454.912 seconds.

Result: 0.054299193162504256


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_majority.2100_rep2.log

```
Command(s):
../bin/prism -ex models/majority.2100/model.prism models/majority.2100/property.props
Wallclock time: 471.677 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:50:57 GMT+01:00 2026
Hostname: n23m0308.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/majority.2100/model.prism models/majority.2100/property.props

Parsing PRISM model file "models/majority.2100/model.prism"...

Type:        CTMC
Modules:     D_def Y_def Z_def CC_def XX_def EE_def
Actions:     []
Variables:   D Y Z CC XX EE
Labels:      "target"

Parsing properties file "models/majority.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:explicit)...

Computing reachable states... 192000 states
Reachable states exploration and model construction done in 1.216 secs.
Sorting reachable states list...

Time for model construction: 1.56 seconds.

Type:        CTMC
States:      192000 (1 initial)
Transitions: 1961600

Starting backwards transient probability computation...

Uniformisation: q.t = 3.2872265951801265 x 2100.0 = 6903.175849878266
Fox-Glynn (1.25E-7): left = 6319, right = 7610
Backwards transient probability computation took 7611 iters and 468.765 seconds.

Value in the initial state: 0.054299193162504256

Time for model checking: 468.789 seconds.

Result: 0.054299193162504256


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_majority.2100_rep3.log

```
Command(s):
../bin/prism -ex models/majority.2100/model.prism models/majority.2100/property.props
Wallclock time: 407.744 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:22:35 GMT+01:00 2026
Hostname: n23m0094.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/majority.2100/model.prism models/majority.2100/property.props

Parsing PRISM model file "models/majority.2100/model.prism"...

Type:        CTMC
Modules:     D_def Y_def Z_def CC_def XX_def EE_def
Actions:     []
Variables:   D Y Z CC XX EE
Labels:      "target"

Parsing properties file "models/majority.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:explicit)...

Computing reachable states... 192000 states
Reachable states exploration and model construction done in 1.154 secs.
Sorting reachable states list...

Time for model construction: 1.336 seconds.

Type:        CTMC
States:      192000 (1 initial)
Transitions: 1961600

Starting backwards transient probability computation...

Uniformisation: q.t = 3.2872265951801265 x 2100.0 = 6903.175849878266
Fox-Glynn (1.25E-7): left = 6319, right = 7610
Backwards transient probability computation took 7611 iters and 405.66 seconds.

Value in the initial state: 0.054299193162504256

Time for model checking: 405.697 seconds.

Result: 0.054299193162504256


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_majority.2100_rep4.log

```
Command(s):
../bin/prism -ex models/majority.2100/model.prism models/majority.2100/property.props
Wallclock time: 422.863 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:03:33 GMT+01:00 2026
Hostname: r23m0023.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/majority.2100/model.prism models/majority.2100/property.props

Parsing PRISM model file "models/majority.2100/model.prism"...

Type:        CTMC
Modules:     D_def Y_def Z_def CC_def XX_def EE_def
Actions:     []
Variables:   D Y Z CC XX EE
Labels:      "target"

Parsing properties file "models/majority.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:explicit)...

Computing reachable states... 192000 states
Reachable states exploration and model construction done in 1.238 secs.
Sorting reachable states list...

Time for model construction: 1.414 seconds.

Type:        CTMC
States:      192000 (1 initial)
Transitions: 1961600

Starting backwards transient probability computation...

Uniformisation: q.t = 3.2872265951801265 x 2100.0 = 6903.175849878266
Fox-Glynn (1.25E-7): left = 6319, right = 7610
Backwards transient probability computation took 7611 iters and 420.817 seconds.

Value in the initial state: 0.054299193162504256

Time for model checking: 420.837 seconds.

Result: 0.054299193162504256


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_majority.2100_rep5.log

```
Command(s):
../bin/prism -ex models/majority.2100/model.prism models/majority.2100/property.props
Wallclock time: 424.513 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:24:19 GMT+01:00 2026
Hostname: n23m0399.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/majority.2100/model.prism models/majority.2100/property.props

Parsing PRISM model file "models/majority.2100/model.prism"...

Type:        CTMC
Modules:     D_def Y_def Z_def CC_def XX_def EE_def
Actions:     []
Variables:   D Y Z CC XX EE
Labels:      "target"

Parsing properties file "models/majority.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:explicit)...

Computing reachable states... 192000 states
Reachable states exploration and model construction done in 1.326 secs.
Sorting reachable states list...

Time for model construction: 1.574 seconds.

Type:        CTMC
States:      192000 (1 initial)
Transitions: 1961600

Starting backwards transient probability computation...

Uniformisation: q.t = 3.2872265951801265 x 2100.0 = 6903.175849878266
Fox-Glynn (1.25E-7): left = 6319, right = 7610
Backwards transient probability computation took 7611 iters and 419.832 seconds.

Value in the initial state: 0.054299193162504256

Time for model checking: 419.856 seconds.

Result: 0.054299193162504256


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

