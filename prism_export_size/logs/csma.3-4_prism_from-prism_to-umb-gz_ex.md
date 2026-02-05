# Log files

Tool configuration: prism_from-prism_to-umb-gz_ex
Benchmark: [csma.3-4](../../models/csma.3-4)
Parsed values: [55807758.0, 55807758.0, 55807758.0, 55807758.0, 55807758.0]



### Log file: prism_from-prism_to-umb-gz_ex_csma.3-4_rep1.log

```
Command(s):
../bin/prism -ex models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/csma.3-4/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 9.851 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:33:02 GMT+01:00 2026
Hostname: n23m0275.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/csma.3-4/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 837818 1460287 states
Reachable states exploration and model construction done in 5.386 secs.
Sorting reachable states list...

Time for model construction: 6.711 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727
Choices:     1471059
Max/avg:     3/1.01

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/csma.3-4/model.umb.gz"...
Time for exporting: 2.31 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/csma.3-4/model.umb.gz:	Size of output file is 55807758 bytes
```



### Log file: prism_from-prism_to-umb-gz_ex_csma.3-4_rep2.log

```
Command(s):
../bin/prism -ex models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/csma.3-4/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 13.272 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:12 GMT+01:00 2026
Hostname: n23m0092.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/csma.3-4/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 647879 1248568 1460287 states
Reachable states exploration and model construction done in 7.104 secs.
Sorting reachable states list...

Time for model construction: 8.852 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727
Choices:     1471059
Max/avg:     3/1.01

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/csma.3-4/model.umb_rep2.gz"...
Time for exporting: 3.18 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/csma.3-4/model.umb_rep2.gz:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_ex_csma.3-4_rep3.log

```
Command(s):
../bin/prism -ex models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/csma.3-4/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 10.619 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:01:24 GMT+01:00 2026
Hostname: n23m0279.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/csma.3-4/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 781571 1460287 states
Reachable states exploration and model construction done in 5.932 secs.
Sorting reachable states list...

Time for model construction: 7.531 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727
Choices:     1471059
Max/avg:     3/1.01

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/csma.3-4/model.umb_rep3.gz"...
Time for exporting: 2.419 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/csma.3-4/model.umb_rep3.gz:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_ex_csma.3-4_rep4.log

```
Command(s):
../bin/prism -ex models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/csma.3-4/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 11.926 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:41:37 GMT+01:00 2026
Hostname: r23m0212.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/csma.3-4/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 673098 1311263 1460287 states
Reachable states exploration and model construction done in 6.719 secs.
Sorting reachable states list...

Time for model construction: 8.367 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727
Choices:     1471059
Max/avg:     3/1.01

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/csma.3-4/model.umb_rep4.gz"...
Time for exporting: 2.857 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/csma.3-4/model.umb_rep4.gz:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_ex_csma.3-4_rep5.log

```
Command(s):
../bin/prism -ex models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/csma.3-4/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 9.735 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:01:54 GMT+01:00 2026
Hostname: n23m0380.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/csma.3-4/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 820073 1460287 states
Reachable states exploration and model construction done in 5.547 secs.
Sorting reachable states list...

Time for model construction: 6.998 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727
Choices:     1471059
Max/avg:     3/1.01

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/csma.3-4/model.umb_rep5.gz"...
Time for exporting: 2.191 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/csma.3-4/model.umb_rep5.gz:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #5
```

