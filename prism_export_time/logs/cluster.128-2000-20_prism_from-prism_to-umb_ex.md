# Log files for prism_from-prism_to-umb_ex on model [cluster.128-2000-20](../../models/cluster.128-2000-20)

Parsed values: `[0.947, 0.8, 0.757, 0.73, 0.703]`



### Log file: prism_from-prism_to-umb_ex_cluster.128-2000-20_rep1.log

```
Command(s):
../bin/prism -ex models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_ex/cluster.128-2000-20/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 5.837 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:41:08 GMT+01:00 2026
Hostname: n23m0249.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/cluster.128-2000-20/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:explicit)...

Computing reachable states... 597012 states
Reachable states exploration and model construction done in 2.803 secs.
Sorting reachable states list...

Time for model construction: 3.317 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/cluster.128-2000-20/model.umb"...
Model export size: 66284 Kb
Time for exporting: 0.947 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/cluster.128-2000-20/model.umb:	Size of output file is 67875328 bytes
```



### Log file: prism_from-prism_to-umb_ex_cluster.128-2000-20_rep2.log

```
Command(s):
../bin/prism -ex models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_ex/cluster.128-2000-20/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 4.812 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:16 GMT+01:00 2026
Hostname: n23m0061.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/cluster.128-2000-20/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:explicit)...

Computing reachable states... 597012 states
Reachable states exploration and model construction done in 2.552 secs.
Sorting reachable states list...

Time for model construction: 2.875 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/cluster.128-2000-20/model_rep2.umb"...
Model export size: 66284 Kb
Time for exporting: 0.8 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/cluster.128-2000-20/model_rep2.umb:	Size of output file is 67875328 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_ex_cluster.128-2000-20_rep3.log

```
Command(s):
../bin/prism -ex models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_ex/cluster.128-2000-20/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 4.635 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:09 GMT+01:00 2026
Hostname: n23m0088.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/cluster.128-2000-20/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:explicit)...

Computing reachable states... 597012 states
Reachable states exploration and model construction done in 2.551 secs.
Sorting reachable states list...

Time for model construction: 2.887 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/cluster.128-2000-20/model_rep3.umb"...
Model export size: 66284 Kb
Time for exporting: 0.757 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/cluster.128-2000-20/model_rep3.umb:	Size of output file is 67875328 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_ex_cluster.128-2000-20_rep4.log

```
Command(s):
../bin/prism -ex models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_ex/cluster.128-2000-20/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 4.476 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:37 GMT+01:00 2026
Hostname: r23m0044.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/cluster.128-2000-20/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:explicit)...

Computing reachable states... 597012 states
Reachable states exploration and model construction done in 2.474 secs.
Sorting reachable states list...

Time for model construction: 2.808 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/cluster.128-2000-20/model_rep4.umb"...
Model export size: 66284 Kb
Time for exporting: 0.73 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/cluster.128-2000-20/model_rep4.umb:	Size of output file is 67875328 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_ex_cluster.128-2000-20_rep5.log

```
Command(s):
../bin/prism -ex models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_ex/cluster.128-2000-20/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 4.314 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:11:30 GMT+01:00 2026
Hostname: n23m0099.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/cluster.128-2000-20/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:explicit)...

Computing reachable states... 597012 states
Reachable states exploration and model construction done in 2.587 secs.
Sorting reachable states list...

Time for model construction: 2.885 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/cluster.128-2000-20/model_rep5.umb"...
Model export size: 66284 Kb
Time for exporting: 0.703 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/cluster.128-2000-20/model_rep5.umb:	Size of output file is 67875328 bytes
Removing output file to save space for repetition #5
```

