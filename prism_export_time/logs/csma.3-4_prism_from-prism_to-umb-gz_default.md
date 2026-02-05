# Log files for prism_from-prism_to-umb-gz_default on model [csma.3-4](../../models/csma.3-4)

Parsed values: `[1.808, 1.824, 1.822, 1.99, 1.88]`



### Log file: prism_from-prism_to-umb-gz_default_csma.3-4_rep1.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/csma.3-4/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 3.363 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:38:21 GMT+01:00 2026
Hostname: n23m0275.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/csma.3-4/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 0.87 seconds (average 0.006444, setup 0.00)

Time for model construction: 1.048 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/csma.3-4/model.umb.gz"...
Time for exporting: 1.808 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/csma.3-4/model.umb.gz:	Size of output file is 55807758 bytes
```



### Log file: prism_from-prism_to-umb-gz_default_csma.3-4_rep2.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/csma.3-4/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 3.656 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:26:01 GMT+01:00 2026
Hostname: n23m0379.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/csma.3-4/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 1.08 seconds (average 0.008000, setup 0.00)

Time for model construction: 1.289 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/csma.3-4/model.umb_rep2.gz"...
Time for exporting: 1.824 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/csma.3-4/model.umb_rep2.gz:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_default_csma.3-4_rep3.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/csma.3-4/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 3.517 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:45:39 GMT+01:00 2026
Hostname: n23m0383.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/csma.3-4/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 0.98 seconds (average 0.007259, setup 0.00)

Time for model construction: 1.161 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/csma.3-4/model.umb_rep3.gz"...
Time for exporting: 1.822 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/csma.3-4/model.umb_rep3.gz:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_default_csma.3-4_rep4.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/csma.3-4/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 4.724 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:51:47 GMT+01:00 2026
Hostname: r23m0197.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/csma.3-4/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 1.66 seconds (average 0.012296, setup 0.00)

Time for model construction: 1.942 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/csma.3-4/model.umb_rep4.gz"...
Time for exporting: 1.99 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/csma.3-4/model.umb_rep4.gz:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_default_csma.3-4_rep5.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/csma.3-4/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 3.550 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:51:47 GMT+01:00 2026
Hostname: n23m0112.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/csma.3-4/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 0.92 seconds (average 0.006815, setup 0.00)

Time for model construction: 1.087 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/csma.3-4/model.umb_rep5.gz"...
Time for exporting: 1.88 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/csma.3-4/model.umb_rep5.gz:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #5
```

