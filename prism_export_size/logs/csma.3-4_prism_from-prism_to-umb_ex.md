# Log files

Tool configuration: prism_from-prism_to-umb_ex
Benchmark: [csma.3-4](../../models/csma.3-4)
Parsed values: [68240384.0, 68240384.0, 68240384.0, 68240384.0, 68240384.0]



### Log file: prism_from-prism_to-umb_ex_csma.3-4_rep1.log

```
Command(s):
../bin/prism -ex models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb_ex/csma.3-4/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 8.009 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:47:21 GMT+01:00 2026
Hostname: r23m0065.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/csma.3-4/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 811295 1460287 states
Reachable states exploration and model construction done in 5.515 secs.
Sorting reachable states list...

Time for model construction: 6.861 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727
Choices:     1471059
Max/avg:     3/1.01

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/csma.3-4/model.umb"...
Model export size: 66641 Kb
Time for exporting: 0.566 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/csma.3-4/model.umb:	Size of output file is 68240384 bytes
```



### Log file: prism_from-prism_to-umb_ex_csma.3-4_rep2.log

```
Command(s):
../bin/prism -ex models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb_ex/csma.3-4/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 8.304 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:30:30 GMT+01:00 2026
Hostname: n23m0351.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/csma.3-4/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 811218 1460287 states
Reachable states exploration and model construction done in 5.694 secs.
Sorting reachable states list...

Time for model construction: 7.198 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727
Choices:     1471059
Max/avg:     3/1.01

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/csma.3-4/model_rep2.umb"...
Model export size: 66641 Kb
Time for exporting: 0.522 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/csma.3-4/model_rep2.umb:	Size of output file is 68240384 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_ex_csma.3-4_rep3.log

```
Command(s):
../bin/prism -ex models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb_ex/csma.3-4/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 9.267 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:29 GMT+01:00 2026
Hostname: r23m0177.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/csma.3-4/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 698580 1381851 1460287 states
Reachable states exploration and model construction done in 6.361 secs.
Sorting reachable states list...

Time for model construction: 7.892 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727
Choices:     1471059
Max/avg:     3/1.01

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/csma.3-4/model_rep3.umb"...
Model export size: 66641 Kb
Time for exporting: 0.682 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/csma.3-4/model_rep3.umb:	Size of output file is 68240384 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_ex_csma.3-4_rep4.log

```
Command(s):
../bin/prism -ex models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb_ex/csma.3-4/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 8.094 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:53:17 GMT+01:00 2026
Hostname: r23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/csma.3-4/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 851305 1460287 states
Reachable states exploration and model construction done in 5.403 secs.
Sorting reachable states list...

Time for model construction: 6.908 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727
Choices:     1471059
Max/avg:     3/1.01

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/csma.3-4/model_rep4.umb"...
Model export size: 66641 Kb
Time for exporting: 0.603 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/csma.3-4/model_rep4.umb:	Size of output file is 68240384 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_ex_csma.3-4_rep5.log

```
Command(s):
../bin/prism -ex models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb_ex/csma.3-4/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 8.877 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:42:08 GMT+01:00 2026
Hostname: n23m0252.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/csma.3-4/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 730928 1432508 1460287 states
Reachable states exploration and model construction done in 6.145 secs.
Sorting reachable states list...

Time for model construction: 7.564 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727
Choices:     1471059
Max/avg:     3/1.01

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/csma.3-4/model_rep5.umb"...
Model export size: 66641 Kb
Time for exporting: 0.645 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/csma.3-4/model_rep5.umb:	Size of output file is 68240384 bytes
Removing output file to save space for repetition #5
```

