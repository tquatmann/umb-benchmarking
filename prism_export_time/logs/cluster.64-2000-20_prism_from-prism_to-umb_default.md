# Log files for prism_from-prism_to-umb_default on model [cluster.64-2000-20](../../models/cluster.64-2000-20)

Parsed values: `[1.389, 1.217, 1.171, 1.255, 1.395]`



### Log file: prism_from-prism_to-umb_default_cluster.64-2000-20_rep1.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_default/cluster.64-2000-20/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2.552 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:41:39 GMT+01:00 2026
Hostname: n23m0379.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/cluster.64-2000-20/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.02 seconds (average 0.000150, setup 0.00)

Time for model construction: 0.065 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/cluster.64-2000-20/model.umb"...
Model export size: 16727 Kb
Time for exporting: 1.389 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/cluster.64-2000-20/model.umb:	Size of output file is 17128960 bytes
```



### Log file: prism_from-prism_to-umb_default_cluster.64-2000-20_rep2.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_default/cluster.64-2000-20/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 1.790 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:53:48 GMT+01:00 2026
Hostname: n23m0308.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/cluster.64-2000-20/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.02 seconds (average 0.000150, setup 0.00)

Time for model construction: 0.043 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/cluster.64-2000-20/model_rep2.umb"...
Model export size: 16727 Kb
Time for exporting: 1.217 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/cluster.64-2000-20/model_rep2.umb:	Size of output file is 17128960 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_default_cluster.64-2000-20_rep3.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_default/cluster.64-2000-20/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 1.761 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:45:39 GMT+01:00 2026
Hostname: r23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/cluster.64-2000-20/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.02 seconds (average 0.000150, setup 0.00)

Time for model construction: 0.048 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/cluster.64-2000-20/model_rep3.umb"...
Model export size: 16727 Kb
Time for exporting: 1.171 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/cluster.64-2000-20/model_rep3.umb:	Size of output file is 17128960 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_default_cluster.64-2000-20_rep4.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_default/cluster.64-2000-20/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 1.870 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:33 GMT+01:00 2026
Hostname: n23m0166.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/cluster.64-2000-20/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.02 seconds (average 0.000150, setup 0.00)

Time for model construction: 0.05 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/cluster.64-2000-20/model_rep4.umb"...
Model export size: 16727 Kb
Time for exporting: 1.255 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/cluster.64-2000-20/model_rep4.umb:	Size of output file is 17128960 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_default_cluster.64-2000-20_rep5.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_default/cluster.64-2000-20/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2.482 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:11 GMT+01:00 2026
Hostname: n23m0083.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/cluster.64-2000-20/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.02 seconds (average 0.000150, setup 0.00)

Time for model construction: 0.073 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/cluster.64-2000-20/model_rep5.umb"...
Model export size: 16727 Kb
Time for exporting: 1.395 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/cluster.64-2000-20/model_rep5.umb:	Size of output file is 17128960 bytes
Removing output file to save space for repetition #5
```

