# Log files

Tool configuration: prism_from-prism_to-umb-gz_ex
Benchmark: [csma.4-2](../../models/csma.4-2)
Parsed values: [1.393, 1.562, 1.817, 1.33, 1.383]



### Log file: prism_from-prism_to-umb-gz_ex_csma.4-2_rep1.log

```
Command(s):
../bin/prism -ex models/csma.4-2/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/csma.4-2/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 9.666 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:45:49 GMT+01:00 2026
Hostname: n23m0263.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.4-2/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/csma.4-2/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 634769 761962 states
Reachable states exploration and model construction done in 3.587 secs.
Sorting reachable states list...

Time for model construction: 4.507 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068
Choices:     825504
Max/avg:     4/1.08

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/csma.4-2/model.umb.gz"...
Time for exporting: 1.393 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/csma.4-2/model.umb.gz:	Size of output file is 28902491 bytes
```



### Log file: prism_from-prism_to-umb-gz_ex_csma.4-2_rep2.log

```
Command(s):
../bin/prism -ex models/csma.4-2/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/csma.4-2/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 7.354 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:52 GMT+01:00 2026
Hostname: n23m0167.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.4-2/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/csma.4-2/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 552278 761962 states
Reachable states exploration and model construction done in 4.188 secs.
Sorting reachable states list...

Time for model construction: 5.075 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068
Choices:     825504
Max/avg:     4/1.08

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/csma.4-2/model.umb_rep2.gz"...
Time for exporting: 1.562 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/csma.4-2/model.umb_rep2.gz:	Size of output file is 28902491 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_ex_csma.4-2_rep3.log

```
Command(s):
../bin/prism -ex models/csma.4-2/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/csma.4-2/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 9.065 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:26 GMT+01:00 2026
Hostname: n23m0350.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.4-2/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/csma.4-2/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 459587 761962 states
Reachable states exploration and model construction done in 5.08 secs.
Sorting reachable states list...

Time for model construction: 6.355 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068
Choices:     825504
Max/avg:     4/1.08

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/csma.4-2/model.umb_rep3.gz"...
Time for exporting: 1.817 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/csma.4-2/model.umb_rep3.gz:	Size of output file is 28902491 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_ex_csma.4-2_rep4.log

```
Command(s):
../bin/prism -ex models/csma.4-2/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/csma.4-2/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 5.804 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:40:37 GMT+01:00 2026
Hostname: n23m0063.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.4-2/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/csma.4-2/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 709386 761962 states
Reachable states exploration and model construction done in 3.193 secs.
Sorting reachable states list...

Time for model construction: 3.886 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068
Choices:     825504
Max/avg:     4/1.08

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/csma.4-2/model.umb_rep4.gz"...
Time for exporting: 1.33 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/csma.4-2/model.umb_rep4.gz:	Size of output file is 28902491 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_ex_csma.4-2_rep5.log

```
Command(s):
../bin/prism -ex models/csma.4-2/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/csma.4-2/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 6.331 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:20:39 GMT+01:00 2026
Hostname: n23m0256.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.4-2/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/csma.4-2/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 643898 761962 states
Reachable states exploration and model construction done in 3.543 secs.
Sorting reachable states list...

Time for model construction: 4.345 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068
Choices:     825504
Max/avg:     4/1.08

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/csma.4-2/model.umb_rep5.gz"...
Time for exporting: 1.383 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/csma.4-2/model.umb_rep5.gz:	Size of output file is 28902491 bytes
Removing output file to save space for repetition #5
```

