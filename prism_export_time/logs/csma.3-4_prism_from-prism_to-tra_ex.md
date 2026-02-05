# Log files

Tool configuration: prism_from-prism_to-tra_ex
Benchmark: [csma.3-4](../../models/csma.3-4)
Parsed values: [2.476, 2.422, 2.968, 2.629, 2.602]



### Log file: prism_from-prism_to-tra_ex_csma.3-4_rep1.log

```
Command(s):
../bin/prism -ex models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-tra_ex/csma.3-4/model.tra,lab,rew:precision=17
Wallclock time: 10.503 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:37:19 GMT+01:00 2026
Hostname: n23m0264.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/csma.3-4/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 816500 1460287 states
Reachable states exploration and model construction done in 5.533 secs.
Sorting reachable states list...

Time for model construction: 7.004 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727
Choices:     1471059
Max/avg:     3/1.01

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/csma.3-4/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/csma.3-4/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/csma.3-4/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/csma.3-4/model.trew"...
Time for exporting: 2.476 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/csma.3-4/model.tra:	Size of output file is 55807758 bytes
out/prism_from-prism_to-tra_ex/csma.3-4/model.lab:	Size of output file is 15898 bytes
out/prism_from-prism_to-tra_ex/csma.3-4/model.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/csma.3-4/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_csma.3-4_rep2.log

```
Command(s):
../bin/prism -ex models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-tra_ex/csma.3-4/model_rep2.tra,lab,rew:precision=17
Wallclock time: 10.133 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:34 GMT+01:00 2026
Hostname: n23m0210.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/csma.3-4/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 832859 1460287 states
Reachable states exploration and model construction done in 5.412 secs.
Sorting reachable states list...

Time for model construction: 6.908 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727
Choices:     1471059
Max/avg:     3/1.01

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/csma.3-4/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/csma.3-4/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/csma.3-4/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/csma.3-4/model_rep2.trew"...
Time for exporting: 2.422 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/csma.3-4/model_rep2.tra:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_ex/csma.3-4/model_rep2.lab:	Size of output file is 15898 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_ex/csma.3-4/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/csma.3-4/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_csma.3-4_rep3.log

```
Command(s):
../bin/prism -ex models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-tra_ex/csma.3-4/model_rep3.tra,lab,rew:precision=17
Wallclock time: 13.028 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:21 GMT+01:00 2026
Hostname: n23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/csma.3-4/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 642989 1274346 1460287 states
Reachable states exploration and model construction done in 7.157 secs.
Sorting reachable states list...

Time for model construction: 9.255 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727
Choices:     1471059
Max/avg:     3/1.01

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/csma.3-4/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/csma.3-4/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/csma.3-4/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/csma.3-4/model_rep3.trew"...
Time for exporting: 2.968 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/csma.3-4/model_rep3.tra:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_ex/csma.3-4/model_rep3.lab:	Size of output file is 15898 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_ex/csma.3-4/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/csma.3-4/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_csma.3-4_rep4.log

```
Command(s):
../bin/prism -ex models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-tra_ex/csma.3-4/model_rep4.tra,lab,rew:precision=17
Wallclock time: 10.131 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:42:39 GMT+01:00 2026
Hostname: n23m0379.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/csma.3-4/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 847144 1460287 states
Reachable states exploration and model construction done in 5.399 secs.
Sorting reachable states list...

Time for model construction: 6.906 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727
Choices:     1471059
Max/avg:     3/1.01

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/csma.3-4/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/csma.3-4/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/csma.3-4/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/csma.3-4/model_rep4.trew"...
Time for exporting: 2.629 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/csma.3-4/model_rep4.tra:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_ex/csma.3-4/model_rep4.lab:	Size of output file is 15898 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_ex/csma.3-4/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/csma.3-4/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_csma.3-4_rep5.log

```
Command(s):
../bin/prism -ex models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-tra_ex/csma.3-4/model_rep5.tra,lab,rew:precision=17
Wallclock time: 10.128 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:30:50 GMT+01:00 2026
Hostname: n23m0134.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/csma.3-4/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 844624 1460287 states
Reachable states exploration and model construction done in 5.437 secs.
Sorting reachable states list...

Time for model construction: 6.949 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727
Choices:     1471059
Max/avg:     3/1.01

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/csma.3-4/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/csma.3-4/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/csma.3-4/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/csma.3-4/model_rep5.trew"...
Time for exporting: 2.602 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/csma.3-4/model_rep5.tra:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_ex/csma.3-4/model_rep5.lab:	Size of output file is 15898 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_ex/csma.3-4/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/csma.3-4/model_rep5.trew:	File does not exist.
```

