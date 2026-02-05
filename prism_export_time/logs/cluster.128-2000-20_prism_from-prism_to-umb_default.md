# Log files for prism_from-prism_to-umb_default on model [cluster.128-2000-20](../../models/cluster.128-2000-20)

Parsed values: `[3.672, 3.987, 4.092, 4.171, 4.284]`



### Log file: prism_from-prism_to-umb_default_cluster.128-2000-20_rep1.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_default/cluster.128-2000-20/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 4.549 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:40:36 GMT+01:00 2026
Hostname: r23m0140.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/cluster.128-2000-20/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.07 seconds (average 0.000268, setup 0.00)

Time for model construction: 0.115 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/cluster.128-2000-20/model.umb"...
Model export size: 66284 Kb
Time for exporting: 3.672 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/cluster.128-2000-20/model.umb:	Size of output file is 67875328 bytes
```



### Log file: prism_from-prism_to-umb_default_cluster.128-2000-20_rep2.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_default/cluster.128-2000-20/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 4.705 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:11:30 GMT+01:00 2026
Hostname: n23m0063.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/cluster.128-2000-20/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.07 seconds (average 0.000268, setup 0.00)

Time for model construction: 0.104 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/cluster.128-2000-20/model_rep2.umb"...
Model export size: 66284 Kb
Time for exporting: 3.987 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/cluster.128-2000-20/model_rep2.umb:	Size of output file is 67875328 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_default_cluster.128-2000-20_rep3.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_default/cluster.128-2000-20/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 5.220 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:10 GMT+01:00 2026
Hostname: n23m0148.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/cluster.128-2000-20/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.08 seconds (average 0.000307, setup 0.00)

Time for model construction: 0.145 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/cluster.128-2000-20/model_rep3.umb"...
Model export size: 66284 Kb
Time for exporting: 4.092 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/cluster.128-2000-20/model_rep3.umb:	Size of output file is 67875328 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_default_cluster.128-2000-20_rep4.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_default/cluster.128-2000-20/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 5.097 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:10 GMT+01:00 2026
Hostname: n23m0073.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/cluster.128-2000-20/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.07 seconds (average 0.000268, setup 0.00)

Time for model construction: 0.127 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/cluster.128-2000-20/model_rep4.umb"...
Model export size: 66284 Kb
Time for exporting: 4.171 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/cluster.128-2000-20/model_rep4.umb:	Size of output file is 67875328 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_default_cluster.128-2000-20_rep5.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb_default/cluster.128-2000-20/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 5.010 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:16:02 GMT+01:00 2026
Hostname: n23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/cluster.128-2000-20/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.07 seconds (average 0.000268, setup 0.00)

Time for model construction: 0.129 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/cluster.128-2000-20/model_rep5.umb"...
Model export size: 66284 Kb
Time for exporting: 4.284 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/cluster.128-2000-20/model_rep5.umb:	Size of output file is 67875328 bytes
Removing output file to save space for repetition #5
```

