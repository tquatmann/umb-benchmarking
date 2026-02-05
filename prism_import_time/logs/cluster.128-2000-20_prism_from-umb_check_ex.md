# Log files

Tool configuration: prism_from-umb_check_ex
Benchmark: [cluster.128-2000-20](../../models/cluster.128-2000-20)
Parsed values: [0.522, 0.551, 0.54, 0.756, 0.636]



### Log file: prism_from-umb_check_ex_cluster.128-2000-20_rep1.log

```
Command(s):
../bin/prism -ex -importmodel models/cluster.128-2000-20/prism.model.umb models/cluster.128-2000-20/property.props
Wallclock time: 1953.292 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 08:02:37 GMT+01:00 2026
Hostname: n23m0383.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/cluster.128-2000-20/prism.model.umb models/cluster.128-2000-20/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   x
Labels:      "minimum"

Parsing properties file "models/cluster.128-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:explicit)...

Time for model construction: 0.522 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Starting backwards transient probability computation...

Uniformisation: q.t = 41.318415 x 2000.0 = 82636.83
Fox-Glynn (1.25E-7): left = 80621, right = 85077
Backwards transient probability computation took 85078 iters and 1951.461 seconds.

Value in the initial state: 0.0010724025337697357

Time for model checking: 1951.519 seconds.

Result: 0.0010724025337697357


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_cluster.128-2000-20_rep2.log

```
Command(s):
../bin/prism -ex -importmodel models/cluster.128-2000-20/prism.model.umb models/cluster.128-2000-20/property.props
Wallclock time: 2184.427 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:10:10 GMT+01:00 2026
Hostname: r23m0198.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/cluster.128-2000-20/prism.model.umb models/cluster.128-2000-20/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   x
Labels:      "minimum"

Parsing properties file "models/cluster.128-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:explicit)...

Time for model construction: 0.551 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Starting backwards transient probability computation...

Uniformisation: q.t = 41.318415 x 2000.0 = 82636.83
Fox-Glynn (1.25E-7): left = 80621, right = 85077
Backwards transient probability computation took 85078 iters and 2182.926 seconds.

Value in the initial state: 0.0010724025337697357

Time for model checking: 2182.985 seconds.

Result: 0.0010724025337697357


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_cluster.128-2000-20_rep3.log

```
Command(s):
../bin/prism -ex -importmodel models/cluster.128-2000-20/prism.model.umb models/cluster.128-2000-20/property.props
Wallclock time: 2025.704 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:05 GMT+01:00 2026
Hostname: n23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/cluster.128-2000-20/prism.model.umb models/cluster.128-2000-20/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   x
Labels:      "minimum"

Parsing properties file "models/cluster.128-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:explicit)...

Time for model construction: 0.54 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Starting backwards transient probability computation...

Uniformisation: q.t = 41.318415 x 2000.0 = 82636.83
Fox-Glynn (1.25E-7): left = 80621, right = 85077
Backwards transient probability computation took 85078 iters and 2020.434 seconds.

Value in the initial state: 0.0010724025337697357

Time for model checking: 2020.501 seconds.

Result: 0.0010724025337697357


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_cluster.128-2000-20_rep4.log

```
Command(s):
../bin/prism -ex -importmodel models/cluster.128-2000-20/prism.model.umb models/cluster.128-2000-20/property.props
Wallclock time: 2190.256 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:05:36 GMT+01:00 2026
Hostname: n23m0166.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/cluster.128-2000-20/prism.model.umb models/cluster.128-2000-20/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   x
Labels:      "minimum"

Parsing properties file "models/cluster.128-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:explicit)...

Time for model construction: 0.756 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Starting backwards transient probability computation...

Uniformisation: q.t = 41.318415 x 2000.0 = 82636.83
Fox-Glynn (1.25E-7): left = 80621, right = 85077
Backwards transient probability computation took 85078 iters and 2187.928 seconds.

Value in the initial state: 0.0010724025337697357

Time for model checking: 2187.994 seconds.

Result: 0.0010724025337697357


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_cluster.128-2000-20_rep5.log

```
Command(s):
../bin/prism -ex -importmodel models/cluster.128-2000-20/prism.model.umb models/cluster.128-2000-20/property.props
Wallclock time: 1990.793 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:14:26 GMT+01:00 2026
Hostname: n23m0392.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/cluster.128-2000-20/prism.model.umb models/cluster.128-2000-20/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   x
Labels:      "minimum"

Parsing properties file "models/cluster.128-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:explicit)...

Time for model construction: 0.636 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Starting backwards transient probability computation...

Uniformisation: q.t = 41.318415 x 2000.0 = 82636.83
Fox-Glynn (1.25E-7): left = 80621, right = 85077
Backwards transient probability computation took 85078 iters and 1989.11 seconds.

Value in the initial state: 0.0010724025337697357

Time for model checking: 1989.166 seconds.

Result: 0.0010724025337697357


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

