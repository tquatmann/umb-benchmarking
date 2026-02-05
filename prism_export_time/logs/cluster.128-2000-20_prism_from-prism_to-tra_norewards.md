# Log files

Tool configuration: prism_from-prism_to-tra_norewards
Benchmark: [cluster.128-2000-20](../../models/cluster.128-2000-20)
Parsed values: [1.772, 1.54, 1.648, 1.631, 1.448]



### Log file: prism_from-prism_to-tra_norewards_cluster.128-2000-20_rep1.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model.tra,lab:precision=17
Wallclock time: 3.251 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:40:37 GMT+01:00 2026
Hostname: n23m0241.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model.tra,lab:precision=17'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.08 seconds (average 0.000307, setup 0.00)

Time for model construction: 0.179 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model.lab"...
Time for exporting: 1.772 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model.tra:	Size of output file is 90018223 bytes
out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model.lab:	Size of output file is 1398482 bytes
```



### Log file: prism_from-prism_to-tra_norewards_cluster.128-2000-20_rep2.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep2.tra,lab:precision=17
Wallclock time: 2.206 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:00 GMT+01:00 2026
Hostname: n23m0308.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep2.tra,lab:precision=17'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.06 seconds (average 0.000230, setup 0.00)

Time for model construction: 0.108 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep2.lab"...
Time for exporting: 1.54 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep2.tra:	Size of output file is 90018223 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep2.lab:	Size of output file is 1398482 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_norewards_cluster.128-2000-20_rep3.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep3.tra,lab:precision=17
Wallclock time: 2.557 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:01 GMT+01:00 2026
Hostname: n23m0166.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep3.tra,lab:precision=17'

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

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep3.lab"...
Time for exporting: 1.648 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep3.tra:	Size of output file is 90018223 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep3.lab:	Size of output file is 1398482 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_norewards_cluster.128-2000-20_rep4.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep4.tra,lab:precision=17
Wallclock time: 2.333 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:27:29 GMT+01:00 2026
Hostname: n23m0252.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep4.tra,lab:precision=17'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.08 seconds (average 0.000307, setup 0.00)

Time for model construction: 0.111 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep4.lab"...
Time for exporting: 1.631 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep4.tra:	Size of output file is 90018223 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep4.lab:	Size of output file is 1398482 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_norewards_cluster.128-2000-20_rep5.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep5.tra,lab:precision=17
Wallclock time: 2.033 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:22:10 GMT+01:00 2026
Hostname: n23m0036.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep5.tra,lab:precision=17'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.06 seconds (average 0.000230, setup 0.00)

Time for model construction: 0.094 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep5.lab"...
Time for exporting: 1.448 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep5.tra:	Size of output file is 90018223 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_norewards/cluster.128-2000-20/model_rep5.lab:	Size of output file is 1398482 bytes
Removing output file to save space for repetition #5
```

