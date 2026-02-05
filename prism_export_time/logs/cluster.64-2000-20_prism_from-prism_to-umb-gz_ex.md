# Log files

Tool configuration: prism_from-prism_to-umb-gz_ex
Benchmark: [cluster.64-2000-20](../../models/cluster.64-2000-20)
Parsed values: [1.098, 1.068, 0.861, 1.15, 0.953]



### Log file: prism_from-prism_to-umb-gz_ex_cluster.64-2000-20_rep1.log

```
Command(s):
../bin/prism -ex models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/cluster.64-2000-20/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2.847 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:42:09 GMT+01:00 2026
Hostname: n23m0249.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/cluster.64-2000-20/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:explicit)...

Computing reachable states... 151060 states
Reachable states exploration and model construction done in 0.886 secs.
Sorting reachable states list...

Time for model construction: 1.03 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/cluster.64-2000-20/model.umb.gz"...
Time for exporting: 1.098 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/cluster.64-2000-20/model.umb.gz:	Size of output file is 16105222 bytes
```



### Log file: prism_from-prism_to-umb-gz_ex_cluster.64-2000-20_rep2.log

```
Command(s):
../bin/prism -ex models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/cluster.64-2000-20/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2.914 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:22 GMT+01:00 2026
Hostname: n23m0180.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/cluster.64-2000-20/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:explicit)...

Computing reachable states... 151060 states
Reachable states exploration and model construction done in 0.805 secs.
Sorting reachable states list...

Time for model construction: 0.985 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/cluster.64-2000-20/model.umb_rep2.gz"...
Time for exporting: 1.068 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/cluster.64-2000-20/model.umb_rep2.gz:	Size of output file is 16105222 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_ex_cluster.64-2000-20_rep3.log

```
Command(s):
../bin/prism -ex models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/cluster.64-2000-20/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2.251 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:26:43 GMT+01:00 2026
Hostname: r23m0204.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/cluster.64-2000-20/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:explicit)...

Computing reachable states... 151060 states
Reachable states exploration and model construction done in 0.686 secs.
Sorting reachable states list...

Time for model construction: 0.81 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/cluster.64-2000-20/model.umb_rep3.gz"...
Time for exporting: 0.861 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/cluster.64-2000-20/model.umb_rep3.gz:	Size of output file is 16105222 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_ex_cluster.64-2000-20_rep4.log

```
Command(s):
../bin/prism -ex models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/cluster.64-2000-20/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 3.057 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:10 GMT+01:00 2026
Hostname: n23m0350.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/cluster.64-2000-20/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:explicit)...

Computing reachable states... 151060 states
Reachable states exploration and model construction done in 0.939 secs.
Sorting reachable states list...

Time for model construction: 1.113 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/cluster.64-2000-20/model.umb_rep4.gz"...
Time for exporting: 1.15 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/cluster.64-2000-20/model.umb_rep4.gz:	Size of output file is 16105222 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_ex_cluster.64-2000-20_rep5.log

```
Command(s):
../bin/prism -ex models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/cluster.64-2000-20/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2.611 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:33 GMT+01:00 2026
Hostname: r23m0055.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/cluster.64-2000-20/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:explicit)...

Computing reachable states... 151060 states
Reachable states exploration and model construction done in 0.863 secs.
Sorting reachable states list...

Time for model construction: 1.01 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/cluster.64-2000-20/model.umb_rep5.gz"...
Time for exporting: 0.953 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/cluster.64-2000-20/model.umb_rep5.gz:	Size of output file is 16105222 bytes
Removing output file to save space for repetition #5
```

