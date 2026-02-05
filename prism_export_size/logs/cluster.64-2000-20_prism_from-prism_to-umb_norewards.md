# Log files for prism_from-prism_to-umb_norewards on model [cluster.64-2000-20](../../models/cluster.64-2000-20)

Parsed values: `[17128960.0, 17128960.0, 17128960.0, 17128960.0, 17128960.0]`



### Log file: prism_from-prism_to-umb_norewards_cluster.64-2000-20_rep1.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/cluster.64-2000-20/model.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 1.789 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:43:41 GMT+01:00 2026
Hostname: r23m0129.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/cluster.64-2000-20/model.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.03 seconds (average 0.000226, setup 0.00)

Time for model construction: 0.077 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/cluster.64-2000-20/model.umb"...
Model export size: 16727 Kb
Time for exporting: 1.215 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/cluster.64-2000-20/model.umb:	Size of output file is 17128960 bytes
```



### Log file: prism_from-prism_to-umb_norewards_cluster.64-2000-20_rep2.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/cluster.64-2000-20/model_rep2.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 1.959 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:59:53 GMT+01:00 2026
Hostname: n23m0120.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/cluster.64-2000-20/model_rep2.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.02 seconds (average 0.000150, setup 0.00)

Time for model construction: 0.045 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/cluster.64-2000-20/model_rep2.umb"...
Model export size: 16727 Kb
Time for exporting: 1.231 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/cluster.64-2000-20/model_rep2.umb:	Size of output file is 17128960 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_norewards_cluster.64-2000-20_rep3.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/cluster.64-2000-20/model_rep3.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 2.211 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:11 GMT+01:00 2026
Hostname: n23m0006.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/cluster.64-2000-20/model_rep3.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.02 seconds (average 0.000150, setup 0.00)

Time for model construction: 0.052 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/cluster.64-2000-20/model_rep3.umb"...
Model export size: 16727 Kb
Time for exporting: 1.499 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/cluster.64-2000-20/model_rep3.umb:	Size of output file is 17128960 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_norewards_cluster.64-2000-20_rep4.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/cluster.64-2000-20/model_rep4.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 1.784 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:43:39 GMT+01:00 2026
Hostname: n23m0379.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/cluster.64-2000-20/model_rep4.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.02 seconds (average 0.000150, setup 0.00)

Time for model construction: 0.083 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/cluster.64-2000-20/model_rep4.umb"...
Model export size: 16727 Kb
Time for exporting: 1.197 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/cluster.64-2000-20/model_rep4.umb:	Size of output file is 17128960 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_norewards_cluster.64-2000-20_rep5.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/cluster.64-2000-20/model_rep5.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 1.808 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:15 GMT+01:00 2026
Hostname: n23m0375.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/cluster.64-2000-20/model_rep5.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.02 seconds (average 0.000150, setup 0.00)

Time for model construction: 0.047 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/cluster.64-2000-20/model_rep5.umb"...
Model export size: 16727 Kb
Time for exporting: 1.231 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/cluster.64-2000-20/model_rep5.umb:	Size of output file is 17128960 bytes
Removing output file to save space for repetition #5
```

