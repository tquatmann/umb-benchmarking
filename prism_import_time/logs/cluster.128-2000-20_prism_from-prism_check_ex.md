# Log files

Tool configuration: prism_from-prism_check_ex
Benchmark: [cluster.128-2000-20](../../models/cluster.128-2000-20)
Parsed values: [2.869, 3.057, 2.717, 3.778, 2.699]



### Log file: prism_from-prism_check_ex_cluster.128-2000-20_rep1.log

```
Command(s):
../bin/prism -ex models/cluster.128-2000-20/model.prism models/cluster.128-2000-20/property.props
Wallclock time: 2271.832 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 08:02:38 GMT+01:00 2026
Hostname: r23m0219.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.128-2000-20/model.prism models/cluster.128-2000-20/property.props

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Parsing properties file "models/cluster.128-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:explicit)...

Computing reachable states... 597012 states
Reachable states exploration and model construction done in 2.314 secs.
Sorting reachable states list...

Time for model construction: 2.869 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Starting backwards transient probability computation...

Uniformisation: q.t = 41.318415 x 2000.0 = 82636.83
Fox-Glynn (1.25E-7): left = 80621, right = 85077
Backwards transient probability computation took 85078 iters and 2267.211 seconds.

Value in the initial state: 0.0010724025337697357

Time for model checking: 2267.269 seconds.

Result: 0.0010724025337697357


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_cluster.128-2000-20_rep2.log

```
Command(s):
../bin/prism -ex models/cluster.128-2000-20/model.prism models/cluster.128-2000-20/property.props
Wallclock time: 2547.582 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:51:58 GMT+01:00 2026
Hostname: n23m0288.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.128-2000-20/model.prism models/cluster.128-2000-20/property.props

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Parsing properties file "models/cluster.128-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:explicit)...

Computing reachable states... 597012 states
Reachable states exploration and model construction done in 2.74 secs.
Sorting reachable states list...

Time for model construction: 3.057 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Starting backwards transient probability computation...

Uniformisation: q.t = 41.318415 x 2000.0 = 82636.83
Fox-Glynn (1.25E-7): left = 80621, right = 85077
Backwards transient probability computation took 85078 iters and 2543.758 seconds.

Value in the initial state: 0.0010724025337697357

Time for model checking: 2543.819 seconds.

Result: 0.0010724025337697357


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_cluster.128-2000-20_rep3.log

```
Command(s):
../bin/prism -ex models/cluster.128-2000-20/model.prism models/cluster.128-2000-20/property.props
Wallclock time: 2241.768 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:07 GMT+01:00 2026
Hostname: r23m0175.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.128-2000-20/model.prism models/cluster.128-2000-20/property.props

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Parsing properties file "models/cluster.128-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:explicit)...

Computing reachable states... 597012 states
Reachable states exploration and model construction done in 2.397 secs.
Sorting reachable states list...

Time for model construction: 2.717 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Starting backwards transient probability computation...

Uniformisation: q.t = 41.318415 x 2000.0 = 82636.83
Fox-Glynn (1.25E-7): left = 80621, right = 85077
Backwards transient probability computation took 85078 iters and 2235.555 seconds.

Value in the initial state: 0.0010724025337697357

Time for model checking: 2235.605 seconds.

Result: 0.0010724025337697357


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_cluster.128-2000-20_rep4.log

```
Command(s):
../bin/prism -ex models/cluster.128-2000-20/model.prism models/cluster.128-2000-20/property.props
Wallclock time: 2877.227 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:36:30 GMT+01:00 2026
Hostname: n23m0252.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.128-2000-20/model.prism models/cluster.128-2000-20/property.props

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Parsing properties file "models/cluster.128-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:explicit)...

Computing reachable states... 597012 states
Reachable states exploration and model construction done in 2.875 secs.
Sorting reachable states list...

Time for model construction: 3.778 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Starting backwards transient probability computation...

Uniformisation: q.t = 41.318415 x 2000.0 = 82636.83
Fox-Glynn (1.25E-7): left = 80621, right = 85077
Backwards transient probability computation took 85078 iters and 2872.495 seconds.

Value in the initial state: 0.0010724025337697357

Time for model checking: 2872.558 seconds.

Result: 0.0010724025337697357


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_cluster.128-2000-20_rep5.log

```
Command(s):
../bin/prism -ex models/cluster.128-2000-20/model.prism models/cluster.128-2000-20/property.props
Wallclock time: 2351.289 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:55:02 GMT+01:00 2026
Hostname: n23m0341.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.128-2000-20/model.prism models/cluster.128-2000-20/property.props

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Parsing properties file "models/cluster.128-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:explicit)...

Computing reachable states... 597012 states
Reachable states exploration and model construction done in 2.315 secs.
Sorting reachable states list...

Time for model construction: 2.699 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Starting backwards transient probability computation...

Uniformisation: q.t = 41.318415 x 2000.0 = 82636.83
Fox-Glynn (1.25E-7): left = 80621, right = 85077
Backwards transient probability computation took 85078 iters and 2347.876 seconds.

Value in the initial state: 0.0010724025337697357

Time for model checking: 2347.931 seconds.

Result: 0.0010724025337697357


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

