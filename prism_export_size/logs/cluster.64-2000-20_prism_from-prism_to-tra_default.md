# Log files

Tool configuration: prism_from-prism_to-tra_default
Benchmark: [cluster.64-2000-20](../../models/cluster.64-2000-20)
Parsed values: [22452031.0, 22452031.0, 22452031.0, 22452031.0, 22452031.0]



### Log file: prism_from-prism_to-tra_default_cluster.64-2000-20_rep1.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-tra_default/cluster.64-2000-20/model.tra,lab,rew:precision=17
Wallclock time: 1.012 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:42:08 GMT+01:00 2026
Hostname: n23m0379.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/cluster.64-2000-20/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.02 seconds (average 0.000150, setup 0.00)

Time for model construction: 0.044 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/cluster.64-2000-20/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/cluster.64-2000-20/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/cluster.64-2000-20/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/cluster.64-2000-20/model.trew"...
Time for exporting: 0.4 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/cluster.64-2000-20/model.tra:	Size of output file is 22105902 bytes
out/prism_from-prism_to-tra_default/cluster.64-2000-20/model.lab:	Size of output file is 346129 bytes
out/prism_from-prism_to-tra_default/cluster.64-2000-20/model.srew:	File does not exist.
out/prism_from-prism_to-tra_default/cluster.64-2000-20/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_cluster.64-2000-20_rep2.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep2.tra,lab,rew:precision=17
Wallclock time: 1.535 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:41 GMT+01:00 2026
Hostname: n23m0247.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.02 seconds (average 0.000150, setup 0.00)

Time for model construction: 0.078 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep2.trew"...
Time for exporting: 0.447 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep2.tra:	Size of output file is 22105902 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep2.lab:	Size of output file is 346129 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_cluster.64-2000-20_rep3.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep3.tra,lab,rew:precision=17
Wallclock time: 0.896 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:55 GMT+01:00 2026
Hostname: n23m0351.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.02 seconds (average 0.000150, setup 0.00)

Time for model construction: 0.039 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep3.trew"...
Time for exporting: 0.373 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep3.tra:	Size of output file is 22105902 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep3.lab:	Size of output file is 346129 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_cluster.64-2000-20_rep4.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep4.tra,lab,rew:precision=17
Wallclock time: 1.023 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:21:40 GMT+01:00 2026
Hostname: n23m0109.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.02 seconds (average 0.000150, setup 0.00)

Time for model construction: 0.044 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep4.trew"...
Time for exporting: 0.415 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep4.tra:	Size of output file is 22105902 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep4.lab:	Size of output file is 346129 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_cluster.64-2000-20_rep5.log

```
Command(s):
../bin/prism  models/cluster.64-2000-20/model.prism -exportmodel out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep5.tra,lab,rew:precision=17
Wallclock time: 4.253 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:47:19 GMT+01:00 2026
Hostname: r23m0217.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.64-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/cluster.64-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 133 iterations in 0.09 seconds (average 0.000677, setup 0.00)

Time for model construction: 0.181 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 8225 nodes (71 terminal), 733216 minterms, vars: 23r/23c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep5.trew"...
Time for exporting: 1.758 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep5.tra:	Size of output file is 22105902 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep5.lab:	Size of output file is 346129 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_default/cluster.64-2000-20/model_rep5.trew:	File does not exist.
```

