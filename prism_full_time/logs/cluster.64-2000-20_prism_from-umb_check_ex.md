# Log files for prism_from-umb_check_ex on model [cluster.64-2000-20](../../models/cluster.64-2000-20)

Parsed values: `[461.482, 465.666, 638.911, 444.544, 483.645]`



### Log file: prism_from-umb_check_ex_cluster.64-2000-20_rep1.log

```
Command(s):
../bin/prism -ex -importmodel models/cluster.64-2000-20/prism.model.umb models/cluster.64-2000-20/property.props
Wallclock time: 461.482 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 08:01:35 GMT+01:00 2026
Hostname: r23m0131.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/cluster.64-2000-20/prism.model.umb models/cluster.64-2000-20/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   x
Labels:      "minimum"

Parsing properties file "models/cluster.64-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:explicit)...

Time for model construction: 0.253 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Starting backwards transient probability computation...

Uniformisation: q.t = 41.057295 x 2000.0 = 82114.59000000001
Fox-Glynn (1.25E-7): left = 80105, right = 84548
Backwards transient probability computation took 84549 iters and 460.465 seconds.

Value in the initial state: 0.0010445396729789366

Time for model checking: 460.496 seconds.

Result: 0.0010445396729789366


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_cluster.64-2000-20_rep2.log

```
Command(s):
../bin/prism -ex -importmodel models/cluster.64-2000-20/prism.model.umb models/cluster.64-2000-20/property.props
Wallclock time: 465.666 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:41 GMT+01:00 2026
Hostname: r23m0133.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/cluster.64-2000-20/prism.model.umb models/cluster.64-2000-20/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   x
Labels:      "minimum"

Parsing properties file "models/cluster.64-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:explicit)...

Time for model construction: 0.195 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Starting backwards transient probability computation...

Uniformisation: q.t = 41.057295 x 2000.0 = 82114.59000000001
Fox-Glynn (1.25E-7): left = 80105, right = 84548
Backwards transient probability computation took 84549 iters and 460.771 seconds.

Value in the initial state: 0.0010445396729789366

Time for model checking: 460.803 seconds.

Result: 0.0010445396729789366


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_cluster.64-2000-20_rep3.log

```
Command(s):
../bin/prism -ex -importmodel models/cluster.64-2000-20/prism.model.umb models/cluster.64-2000-20/property.props
Wallclock time: 638.911 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 02:57:25 GMT+01:00 2026
Hostname: n23m0181.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/cluster.64-2000-20/prism.model.umb models/cluster.64-2000-20/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   x
Labels:      "minimum"

Parsing properties file "models/cluster.64-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:explicit)...

Time for model construction: 0.364 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Starting backwards transient probability computation...

Uniformisation: q.t = 41.057295 x 2000.0 = 82114.59000000001
Fox-Glynn (1.25E-7): left = 80105, right = 84548
Backwards transient probability computation took 84549 iters and 637.139 seconds.

Value in the initial state: 0.0010445396729789366

Time for model checking: 637.175 seconds.

Result: 0.0010445396729789366


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_cluster.64-2000-20_rep4.log

```
Command(s):
../bin/prism -ex -importmodel models/cluster.64-2000-20/prism.model.umb models/cluster.64-2000-20/property.props
Wallclock time: 444.544 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:08:44 GMT+01:00 2026
Hostname: n23m0351.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/cluster.64-2000-20/prism.model.umb models/cluster.64-2000-20/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   x
Labels:      "minimum"

Parsing properties file "models/cluster.64-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:explicit)...

Time for model construction: 0.366 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Starting backwards transient probability computation...

Uniformisation: q.t = 41.057295 x 2000.0 = 82114.59000000001
Fox-Glynn (1.25E-7): left = 80105, right = 84548
Backwards transient probability computation took 84549 iters and 441.555 seconds.

Value in the initial state: 0.0010445396729789366

Time for model checking: 441.594 seconds.

Result: 0.0010445396729789366


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_cluster.64-2000-20_rep5.log

```
Command(s):
../bin/prism -ex -importmodel models/cluster.64-2000-20/prism.model.umb models/cluster.64-2000-20/property.props
Wallclock time: 483.645 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 02:59:59 GMT+01:00 2026
Hostname: n23m0295.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/cluster.64-2000-20/prism.model.umb models/cluster.64-2000-20/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   x
Labels:      "minimum"

Parsing properties file "models/cluster.64-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:explicit)...

Time for model construction: 0.26 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Starting backwards transient probability computation...

Uniformisation: q.t = 41.057295 x 2000.0 = 82114.59000000001
Fox-Glynn (1.25E-7): left = 80105, right = 84548
Backwards transient probability computation took 84549 iters and 482.587 seconds.

Value in the initial state: 0.0010445396729789366

Time for model checking: 482.62 seconds.

Result: 0.0010445396729789366


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

