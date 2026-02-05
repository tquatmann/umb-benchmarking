# Log files for prism_from-prism_to-umb_ex on model [cluster.64-2000-20](../../models/cluster.64-2000-20)

Parsed values: `[0.389, 0.383, 0.384, 0.314, 0.522]`



### Log file: prism_from-prism_to-umb_ex_cluster.64-2000-20_rep1.log

```
Command(s):
../bin/prism -ex models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_ex/cluster.64-2000-20/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2.189 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:41:39 GMT+01:00 2026
Hostname: n23m0249.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/cluster.64-2000-20/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:explicit)...

Computing reachable states... 151060 states
Reachable states exploration and model construction done in 0.89 secs.
Sorting reachable states list...

Time for model construction: 1.046 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/cluster.64-2000-20/model.umb"...
Model export size: 16727 Kb
Time for exporting: 0.389 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/cluster.64-2000-20/model.umb:	Size of output file is 17128960 bytes
```



### Log file: prism_from-prism_to-umb_ex_cluster.64-2000-20_rep2.log

```
Command(s):
../bin/prism -ex models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_ex/cluster.64-2000-20/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 4.011 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:26:56 GMT+01:00 2026
Hostname: n23m0256.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/cluster.64-2000-20/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:explicit)...

Computing reachable states... 151060 states
Reachable states exploration and model construction done in 0.778 secs.
Sorting reachable states list...

Time for model construction: 0.919 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/cluster.64-2000-20/model_rep2.umb"...
Model export size: 16727 Kb
Time for exporting: 0.383 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/cluster.64-2000-20/model_rep2.umb:	Size of output file is 17128960 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_ex_cluster.64-2000-20_rep3.log

```
Command(s):
../bin/prism -ex models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_ex/cluster.64-2000-20/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2.123 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:55 GMT+01:00 2026
Hostname: n23m0350.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/cluster.64-2000-20/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:explicit)...

Computing reachable states... 151060 states
Reachable states exploration and model construction done in 0.873 secs.
Sorting reachable states list...

Time for model construction: 1.021 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/cluster.64-2000-20/model_rep3.umb"...
Model export size: 16727 Kb
Time for exporting: 0.384 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/cluster.64-2000-20/model_rep3.umb:	Size of output file is 17128960 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_ex_cluster.64-2000-20_rep4.log

```
Command(s):
../bin/prism -ex models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_ex/cluster.64-2000-20/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 1.849 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:20:07 GMT+01:00 2026
Hostname: n23m0341.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/cluster.64-2000-20/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:explicit)...

Computing reachable states... 151060 states
Reachable states exploration and model construction done in 0.787 secs.
Sorting reachable states list...

Time for model construction: 0.915 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/cluster.64-2000-20/model_rep4.umb"...
Model export size: 16727 Kb
Time for exporting: 0.314 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/cluster.64-2000-20/model_rep4.umb:	Size of output file is 17128960 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_ex_cluster.64-2000-20_rep5.log

```
Command(s):
../bin/prism -ex models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_ex/cluster.64-2000-20/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 3.086 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:12 GMT+01:00 2026
Hostname: n23m0229.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/cluster.64-2000-20/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:explicit)...

Computing reachable states... 151060 states
Reachable states exploration and model construction done in 1.146 secs.
Sorting reachable states list...

Time for model construction: 1.381 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/cluster.64-2000-20/model_rep5.umb"...
Model export size: 16727 Kb
Time for exporting: 0.522 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/cluster.64-2000-20/model_rep5.umb:	Size of output file is 17128960 bytes
Removing output file to save space for repetition #5
```

