# Log files for prism_from-prism_check_ex on model [cluster.64-2000-20](../../models/cluster.64-2000-20)

Parsed values: `[1.147, 0.88, 1.005, 1.119, 0.761]`



### Log file: prism_from-prism_check_ex_cluster.64-2000-20_rep1.log

```
Command(s):
../bin/prism -ex models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props
Wallclock time: 501.709 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:59:33 GMT+01:00 2026
Hostname: r23m0211.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Parsing properties file "models/cluster.64-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:explicit)...

Computing reachable states... 151060 states
Reachable states exploration and model construction done in 0.799 secs.
Sorting reachable states list...

Time for model construction: 1.147 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Starting backwards transient probability computation...

Uniformisation: q.t = 41.057295 x 2000.0 = 82114.59000000001
Fox-Glynn (1.25E-7): left = 80105, right = 84548
Backwards transient probability computation took 84549 iters and 497.928 seconds.

Value in the initial state: 0.0010445396729789366

Time for model checking: 497.961 seconds.

Result: 0.0010445396729789366


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_cluster.64-2000-20_rep2.log

```
Command(s):
../bin/prism -ex models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props
Wallclock time: 673.775 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:24:22 GMT+01:00 2026
Hostname: n23m0330.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Parsing properties file "models/cluster.64-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:explicit)...

Computing reachable states... 151060 states
Reachable states exploration and model construction done in 0.726 secs.
Sorting reachable states list...

Time for model construction: 0.88 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Starting backwards transient probability computation...

Uniformisation: q.t = 41.057295 x 2000.0 = 82114.59000000001
Fox-Glynn (1.25E-7): left = 80105, right = 84548
Backwards transient probability computation took 84549 iters and 671.758 seconds.

Value in the initial state: 0.0010445396729789366

Time for model checking: 671.785 seconds.

Result: 0.0010445396729789366


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_cluster.64-2000-20_rep3.log

```
Command(s):
../bin/prism -ex models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props
Wallclock time: 569.727 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:06 GMT+01:00 2026
Hostname: r23m0128.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Parsing properties file "models/cluster.64-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:explicit)...

Computing reachable states... 151060 states
Reachable states exploration and model construction done in 0.841 secs.
Sorting reachable states list...

Time for model construction: 1.005 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Starting backwards transient probability computation...

Uniformisation: q.t = 41.057295 x 2000.0 = 82114.59000000001
Fox-Glynn (1.25E-7): left = 80105, right = 84548
Backwards transient probability computation took 84549 iters and 565.463 seconds.

Value in the initial state: 0.0010445396729789366

Time for model checking: 565.496 seconds.

Result: 0.0010445396729789366


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_cluster.64-2000-20_rep4.log

```
Command(s):
../bin/prism -ex models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props
Wallclock time: 767.816 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:49:26 GMT+01:00 2026
Hostname: n23m0244.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Parsing properties file "models/cluster.64-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:explicit)...

Computing reachable states... 151060 states
Reachable states exploration and model construction done in 0.75 secs.
Sorting reachable states list...

Time for model construction: 1.119 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Starting backwards transient probability computation...

Uniformisation: q.t = 41.057295 x 2000.0 = 82114.59000000001
Fox-Glynn (1.25E-7): left = 80105, right = 84548
Backwards transient probability computation took 84549 iters and 763.146 seconds.

Value in the initial state: 0.0010445396729789366

Time for model checking: 763.188 seconds.

Result: 0.0010445396729789366


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_cluster.64-2000-20_rep5.log

```
Command(s):
../bin/prism -ex models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props
Wallclock time: 568.790 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:54:30 GMT+01:00 2026
Hostname: n23m0237.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.64-2000-20/model.prism models/cluster.64-2000-20/property.props

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Parsing properties file "models/cluster.64-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:explicit)...

Computing reachable states... 151060 states
Reachable states exploration and model construction done in 0.651 secs.
Sorting reachable states list...

Time for model construction: 0.761 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Starting backwards transient probability computation...

Uniformisation: q.t = 41.057295 x 2000.0 = 82114.59000000001
Fox-Glynn (1.25E-7): left = 80105, right = 84548
Backwards transient probability computation took 84549 iters and 567.449 seconds.

Value in the initial state: 0.0010445396729789366

Time for model checking: 567.473 seconds.

Result: 0.0010445396729789366


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

