# Log files

Tool configuration: prism_from-umb_check_ex
Benchmark: [speed-ind.2100](../../models/speed-ind.2100)
Parsed values: [1848.005, 1708.815, 1682.897, 1789.517, 1645.373]



### Log file: prism_from-umb_check_ex_speed-ind.2100_rep1.log

```
Command(s):
../bin/prism -ex -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props
Wallclock time: 1848.005 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:31:16 GMT+01:00 2026
Hostname: r23m0203.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/speed-ind.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:explicit)...

Time for model construction: 0.821 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Starting backwards transient probability computation...

Uniformisation: q.t = 2.7979107707826114 x 2100.0 = 5875.612618643484
Fox-Glynn (1.25E-7): left = 5336, right = 6527
Backwards transient probability computation took 6528 iters and 1846.37 seconds.

Value in the initial state: 0.04229449797846379

Time for model checking: 1846.449 seconds.

Result: 0.04229449797846379


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_speed-ind.2100_rep2.log

```
Command(s):
../bin/prism -ex -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props
Wallclock time: 1708.815 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:06 GMT+01:00 2026
Hostname: n23m0202.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/speed-ind.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:explicit)...

Time for model construction: 0.848 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Starting backwards transient probability computation...

Uniformisation: q.t = 2.7979107707826114 x 2100.0 = 5875.612618643484
Fox-Glynn (1.25E-7): left = 5336, right = 6527
Backwards transient probability computation took 6528 iters and 1706.307 seconds.

Value in the initial state: 0.04229449797846379

Time for model checking: 1706.393 seconds.

Result: 0.04229449797846379


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_speed-ind.2100_rep3.log

```
Command(s):
../bin/prism -ex -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props
Wallclock time: 1682.897 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:54:00 GMT+01:00 2026
Hostname: n23m0277.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/speed-ind.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:explicit)...

Time for model construction: 0.851 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Starting backwards transient probability computation...

Uniformisation: q.t = 2.7979107707826114 x 2100.0 = 5875.612618643484
Fox-Glynn (1.25E-7): left = 5336, right = 6527
Backwards transient probability computation took 6528 iters and 1681.071 seconds.

Value in the initial state: 0.04229449797846379

Time for model checking: 1681.136 seconds.

Result: 0.04229449797846379


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_speed-ind.2100_rep4.log

```
Command(s):
../bin/prism -ex -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props
Wallclock time: 1789.517 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:17:29 GMT+01:00 2026
Hostname: n23m0333.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/speed-ind.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:explicit)...

Time for model construction: 0.792 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Starting backwards transient probability computation...

Uniformisation: q.t = 2.7979107707826114 x 2100.0 = 5875.612618643484
Fox-Glynn (1.25E-7): left = 5336, right = 6527
Backwards transient probability computation took 6528 iters and 1787.679 seconds.

Value in the initial state: 0.04229449797846379

Time for model checking: 1787.756 seconds.

Result: 0.04229449797846379


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_speed-ind.2100_rep5.log

```
Command(s):
../bin/prism -ex -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props
Wallclock time: 1645.373 seconds
Return code: 0
##############################
[0.002s][warning][perf,memops] Cannot use file /tmp/hsperfdata_tq429871/135364 because it is locked by another process (errno = 11)
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:08 GMT+01:00 2026
Hostname: r23m0154.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/speed-ind.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:explicit)...

Time for model construction: 0.738 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Starting backwards transient probability computation...

Uniformisation: q.t = 2.7979107707826114 x 2100.0 = 5875.612618643484
Fox-Glynn (1.25E-7): left = 5336, right = 6527
Backwards transient probability computation took 6528 iters and 1641.008 seconds.

Value in the initial state: 0.04229449797846379

Time for model checking: 1641.08 seconds.

Result: 0.04229449797846379


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

