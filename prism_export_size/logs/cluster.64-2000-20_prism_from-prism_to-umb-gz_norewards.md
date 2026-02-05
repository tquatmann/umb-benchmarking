# Log files

Tool configuration: prism_from-prism_to-umb-gz_norewards
Benchmark: [cluster.64-2000-20](../../models/cluster.64-2000-20)
Parsed values: [16240478.0, 16240478.0, 16240478.0, 16240478.0, 16240478.0]



### Log file: prism_from-prism_to-umb-gz_norewards_cluster.64-2000-20_rep1.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/cluster.64-2000-20/model.umb.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 0.893 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:43:10 GMT+01:00 2026
Hostname: r23m0140.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/cluster.64-2000-20/model.umb.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.02 seconds (average 0.000150, setup 0.00)

Time for model construction: 0.04 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/cluster.64-2000-20/model.umb.gz"...
Time for exporting: 0.347 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/cluster.64-2000-20/model.umb.gz:	Size of output file is 16240478 bytes
```



### Log file: prism_from-prism_to-umb-gz_norewards_cluster.64-2000-20_rep2.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/cluster.64-2000-20/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 1.715 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:44:10 GMT+01:00 2026
Hostname: n23m0275.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/cluster.64-2000-20/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true'

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

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/cluster.64-2000-20/model.umb_rep2.gz"...
Time for exporting: 0.433 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/cluster.64-2000-20/model.umb_rep2.gz:	Size of output file is 16240478 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_norewards_cluster.64-2000-20_rep3.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/cluster.64-2000-20/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 1.152 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:30:20 GMT+01:00 2026
Hostname: n23m0275.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/cluster.64-2000-20/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.02 seconds (average 0.000150, setup 0.00)

Time for model construction: 0.055 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/cluster.64-2000-20/model.umb_rep3.gz"...
Time for exporting: 0.428 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/cluster.64-2000-20/model.umb_rep3.gz:	Size of output file is 16240478 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_norewards_cluster.64-2000-20_rep4.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/cluster.64-2000-20/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 3.831 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:49:22 GMT+01:00 2026
Hostname: r23m0215.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/cluster.64-2000-20/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.09 seconds (average 0.000677, setup 0.00)

Time for model construction: 0.172 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/cluster.64-2000-20/model.umb_rep4.gz"...
Time for exporting: 1.627 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/cluster.64-2000-20/model.umb_rep4.gz:	Size of output file is 16240478 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_norewards_cluster.64-2000-20_rep5.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/cluster.64-2000-20/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 4.434 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:23 GMT+01:00 2026
Hostname: r23m0217.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/cluster.64-2000-20/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.10 seconds (average 0.000752, setup 0.00)

Time for model construction: 0.201 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/cluster.64-2000-20/model.umb_rep5.gz"...
Time for exporting: 1.625 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/cluster.64-2000-20/model.umb_rep5.gz:	Size of output file is 16240478 bytes
Removing output file to save space for repetition #5
```

