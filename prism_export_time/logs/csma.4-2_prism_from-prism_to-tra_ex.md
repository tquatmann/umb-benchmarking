# Log files for prism_from-prism_to-tra_ex on model [csma.4-2](../../models/csma.4-2)

Parsed values: `[1.39, 11.221, 1.752, 1.367, 1.527]`



### Log file: prism_from-prism_to-tra_ex_csma.4-2_rep1.log

```
Command(s):
../bin/prism -ex models/csma.4-2/model.prism -exportmodel out/prism_from-prism_to-tra_ex/csma.4-2/model.tra,lab,rew:precision=17
Wallclock time: 5.860 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:44:12 GMT+01:00 2026
Hostname: n23m0275.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.4-2/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/csma.4-2/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 710307 761962 states
Reachable states exploration and model construction done in 3.221 secs.
Sorting reachable states list...

Time for model construction: 3.925 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068
Choices:     825504
Max/avg:     4/1.08

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/csma.4-2/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/csma.4-2/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/csma.4-2/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/csma.4-2/model.trew"...
Time for exporting: 1.39 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/csma.4-2/model.tra:	Size of output file is 28902491 bytes
out/prism_from-prism_to-tra_ex/csma.4-2/model.lab:	Size of output file is 34592 bytes
out/prism_from-prism_to-tra_ex/csma.4-2/model.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/csma.4-2/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_csma.4-2_rep2.log

```
Command(s):
../bin/prism -ex models/csma.4-2/model.prism -exportmodel out/prism_from-prism_to-tra_ex/csma.4-2/model_rep2.tra,lab,rew:precision=17
Wallclock time: 17.227 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:23:53 GMT+01:00 2026
Hostname: n23m0396.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.4-2/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/csma.4-2/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 579039 761962 states
Reachable states exploration and model construction done in 4.069 secs.
Sorting reachable states list...

Time for model construction: 5.243 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068
Choices:     825504
Max/avg:     4/1.08

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/csma.4-2/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/csma.4-2/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/csma.4-2/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/csma.4-2/model_rep2.trew"...
Time for exporting: 11.221 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/csma.4-2/model_rep2.tra:	Size of output file is 28902491 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_ex/csma.4-2/model_rep2.lab:	Size of output file is 34592 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_ex/csma.4-2/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/csma.4-2/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_csma.4-2_rep3.log

```
Command(s):
../bin/prism -ex models/csma.4-2/model.prism -exportmodel out/prism_from-prism_to-tra_ex/csma.4-2/model_rep3.tra,lab,rew:precision=17
Wallclock time: 7.309 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:40 GMT+01:00 2026
Hostname: n23m0343.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.4-2/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/csma.4-2/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 618577 761962 states
Reachable states exploration and model construction done in 3.712 secs.
Sorting reachable states list...

Time for model construction: 4.549 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068
Choices:     825504
Max/avg:     4/1.08

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/csma.4-2/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/csma.4-2/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/csma.4-2/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/csma.4-2/model_rep3.trew"...
Time for exporting: 1.752 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/csma.4-2/model_rep3.tra:	Size of output file is 28902491 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_ex/csma.4-2/model_rep3.lab:	Size of output file is 34592 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_ex/csma.4-2/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/csma.4-2/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_csma.4-2_rep4.log

```
Command(s):
../bin/prism -ex models/csma.4-2/model.prism -exportmodel out/prism_from-prism_to-tra_ex/csma.4-2/model_rep4.tra,lab,rew:precision=17
Wallclock time: 6.052 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:31:01 GMT+01:00 2026
Hostname: r23m0015.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.4-2/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/csma.4-2/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 695709 761962 states
Reachable states exploration and model construction done in 3.29 secs.
Sorting reachable states list...

Time for model construction: 4.078 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068
Choices:     825504
Max/avg:     4/1.08

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/csma.4-2/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/csma.4-2/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/csma.4-2/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/csma.4-2/model_rep4.trew"...
Time for exporting: 1.367 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/csma.4-2/model_rep4.tra:	Size of output file is 28902491 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_ex/csma.4-2/model_rep4.lab:	Size of output file is 34592 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_ex/csma.4-2/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/csma.4-2/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_csma.4-2_rep5.log

```
Command(s):
../bin/prism -ex models/csma.4-2/model.prism -exportmodel out/prism_from-prism_to-tra_ex/csma.4-2/model_rep5.tra,lab,rew:precision=17
Wallclock time: 7.148 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:33 GMT+01:00 2026
Hostname: n23m0234.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/csma.4-2/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/csma.4-2/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:explicit)...

Computing reachable states... 618610 761962 states
Reachable states exploration and model construction done in 3.705 secs.
Sorting reachable states list...

Time for model construction: 4.566 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068
Choices:     825504
Max/avg:     4/1.08

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/csma.4-2/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/csma.4-2/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/csma.4-2/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/csma.4-2/model_rep5.trew"...
Time for exporting: 1.527 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/csma.4-2/model_rep5.tra:	Size of output file is 28902491 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_ex/csma.4-2/model_rep5.lab:	Size of output file is 34592 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_ex/csma.4-2/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/csma.4-2/model_rep5.trew:	File does not exist.
```

