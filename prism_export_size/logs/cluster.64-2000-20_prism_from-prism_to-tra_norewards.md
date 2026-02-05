# Log files

Tool configuration: prism_from-prism_to-tra_norewards
Benchmark: [cluster.64-2000-20](../../models/cluster.64-2000-20)
Parsed values: [22452031.0, 22452031.0, 22452031.0, 22452031.0, 22452031.0]



### Log file: prism_from-prism_to-tra_norewards_cluster.64-2000-20_rep1.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model.tra,lab:precision=17
Wallclock time: 1.232 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:40:06 GMT+01:00 2026
Hostname: r23m0131.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model.tra,lab:precision=17'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.02 seconds (average 0.000150, setup 0.00)

Time for model construction: 0.056 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model.lab"...
Time for exporting: 0.41 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model.tra:	Size of output file is 22105902 bytes
out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model.lab:	Size of output file is 346129 bytes
```



### Log file: prism_from-prism_to-tra_norewards_cluster.64-2000-20_rep2.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep2.tra,lab:precision=17
Wallclock time: 1.122 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:28:17 GMT+01:00 2026
Hostname: n23m0041.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep2.tra,lab:precision=17'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.02 seconds (average 0.000150, setup 0.00)

Time for model construction: 0.054 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep2.lab"...
Time for exporting: 0.403 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep2.tra:	Size of output file is 22105902 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep2.lab:	Size of output file is 346129 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_norewards_cluster.64-2000-20_rep3.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep3.tra,lab:precision=17
Wallclock time: 1.263 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:32:56 GMT+01:00 2026
Hostname: r23m0212.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep3.tra,lab:precision=17'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.03 seconds (average 0.000226, setup 0.00)

Time for model construction: 0.064 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep3.lab"...
Time for exporting: 0.448 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep3.tra:	Size of output file is 22105902 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep3.lab:	Size of output file is 346129 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_norewards_cluster.64-2000-20_rep4.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep4.tra,lab:precision=17
Wallclock time: 0.955 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:23:42 GMT+01:00 2026
Hostname: r23m0204.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep4.tra,lab:precision=17'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.03 seconds (average 0.000226, setup 0.00)

Time for model construction: 0.043 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep4.lab"...
Time for exporting: 0.376 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep4.tra:	Size of output file is 22105902 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep4.lab:	Size of output file is 346129 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_norewards_cluster.64-2000-20_rep5.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep5.tra,lab:precision=17
Wallclock time: 0.979 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:46 GMT+01:00 2026
Hostname: n23m0380.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep5.tra,lab:precision=17'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.02 seconds (average 0.000150, setup 0.00)

Time for model construction: 0.041 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep5.lab"...
Time for exporting: 0.389 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep5.tra:	Size of output file is 22105902 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_norewards/cluster.64-2000-20/model_rep5.lab:	Size of output file is 346129 bytes
Removing output file to save space for repetition #5
```

