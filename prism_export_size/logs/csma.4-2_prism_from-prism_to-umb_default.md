# Log files

Tool configuration: prism_from-prism_to-umb_default
Benchmark: [csma.4-2](../../models/csma.4-2)
Parsed values: [37532160.0, 37532160.0, 37532160.0, 37532160.0, 37532160.0]



### Log file: prism_from-prism_to-umb_default_csma.4-2_rep1.log

```
Command(s):
../bin/prism  models/csma.4-2/model.prism -exportmodel out/prism_from-prism_to-umb_default/csma.4-2/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 6.094 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:23:48 GMT+01:00 2026
Hostname: r23m0139.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.4-2/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/csma.4-2/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 193 iterations in 1.00 seconds (average 0.005181, setup 0.00)

Time for model construction: 1.096 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 52233 nodes (4 terminal), 1327068 minterms, vars: 54r/54c/17nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/csma.4-2/model.umb"...
Model export size: 36652 Kb
Time for exporting: 4.507 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/csma.4-2/model.umb:	Size of output file is 37532160 bytes
```



### Log file: prism_from-prism_to-umb_default_csma.4-2_rep2.log

```
Command(s):
../bin/prism  models/csma.4-2/model.prism -exportmodel out/prism_from-prism_to-umb_default/csma.4-2/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 7.577 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:55 GMT+01:00 2026
Hostname: n23m0383.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.4-2/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/csma.4-2/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 193 iterations in 1.58 seconds (average 0.008187, setup 0.00)

Time for model construction: 1.722 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 52233 nodes (4 terminal), 1327068 minterms, vars: 54r/54c/17nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/csma.4-2/model_rep2.umb"...
Model export size: 36652 Kb
Time for exporting: 5.124 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/csma.4-2/model_rep2.umb:	Size of output file is 37532160 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_default_csma.4-2_rep3.log

```
Command(s):
../bin/prism  models/csma.4-2/model.prism -exportmodel out/prism_from-prism_to-umb_default/csma.4-2/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 6.059 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:47:11 GMT+01:00 2026
Hostname: r23m0015.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.4-2/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/csma.4-2/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 193 iterations in 0.98 seconds (average 0.005078, setup 0.00)

Time for model construction: 1.065 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 52233 nodes (4 terminal), 1327068 minterms, vars: 54r/54c/17nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/csma.4-2/model_rep3.umb"...
Model export size: 36652 Kb
Time for exporting: 4.522 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/csma.4-2/model_rep3.umb:	Size of output file is 37532160 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_default_csma.4-2_rep4.log

```
Command(s):
../bin/prism  models/csma.4-2/model.prism -exportmodel out/prism_from-prism_to-umb_default/csma.4-2/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 6.382 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:22 GMT+01:00 2026
Hostname: n23m0204.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.4-2/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/csma.4-2/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 193 iterations in 0.96 seconds (average 0.004974, setup 0.00)

Time for model construction: 1.059 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 52233 nodes (4 terminal), 1327068 minterms, vars: 54r/54c/17nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/csma.4-2/model_rep4.umb"...
Model export size: 36652 Kb
Time for exporting: 4.588 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/csma.4-2/model_rep4.umb:	Size of output file is 37532160 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_default_csma.4-2_rep5.log

```
Command(s):
../bin/prism  models/csma.4-2/model.prism -exportmodel out/prism_from-prism_to-umb_default/csma.4-2/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 8.450 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:20 GMT+01:00 2026
Hostname: n23m0165.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.4-2/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/csma.4-2/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 193 iterations in 1.72 seconds (average 0.008912, setup 0.00)

Time for model construction: 1.891 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 52233 nodes (4 terminal), 1327068 minterms, vars: 54r/54c/17nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/csma.4-2/model_rep5.umb"...
Model export size: 36652 Kb
Time for exporting: 5.523 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/csma.4-2/model_rep5.umb:	Size of output file is 37532160 bytes
Removing output file to save space for repetition #5
```

