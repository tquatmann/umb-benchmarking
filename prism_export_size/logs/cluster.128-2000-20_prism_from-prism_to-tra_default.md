# Log files for prism_from-prism_to-tra_default on model [cluster.128-2000-20](../../models/cluster.128-2000-20)

Parsed values: `[91416705.0, 91416705.0, 91416705.0, 91416705.0, 91416705.0]`



### Log file: prism_from-prism_to-tra_default_cluster.128-2000-20_rep1.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-tra_default/cluster.128-2000-20/model.tra,lab,rew:precision=17
Wallclock time: 2.619 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:42:09 GMT+01:00 2026
Hostname: n23m0244.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/cluster.128-2000-20/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.08 seconds (average 0.000307, setup 0.00)

Time for model construction: 0.149 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/cluster.128-2000-20/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/cluster.128-2000-20/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/cluster.128-2000-20/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/cluster.128-2000-20/model.trew"...
Time for exporting: 1.772 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/cluster.128-2000-20/model.tra:	Size of output file is 90018223 bytes
out/prism_from-prism_to-tra_default/cluster.128-2000-20/model.lab:	Size of output file is 1398482 bytes
out/prism_from-prism_to-tra_default/cluster.128-2000-20/model.srew:	File does not exist.
out/prism_from-prism_to-tra_default/cluster.128-2000-20/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_cluster.128-2000-20_rep2.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep2.tra,lab,rew:precision=17
Wallclock time: 2.744 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:22 GMT+01:00 2026
Hostname: n23m0181.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.07 seconds (average 0.000268, setup 0.00)

Time for model construction: 0.149 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep2.trew"...
Time for exporting: 1.752 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep2.tra:	Size of output file is 90018223 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep2.lab:	Size of output file is 1398482 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_cluster.128-2000-20_rep3.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep3.tra,lab,rew:precision=17
Wallclock time: 2.188 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:30:19 GMT+01:00 2026
Hostname: n23m0288.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.07 seconds (average 0.000268, setup 0.00)

Time for model construction: 0.109 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep3.trew"...
Time for exporting: 1.505 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep3.tra:	Size of output file is 90018223 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep3.lab:	Size of output file is 1398482 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_cluster.128-2000-20_rep4.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep4.tra,lab,rew:precision=17
Wallclock time: 2.846 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:22 GMT+01:00 2026
Hostname: r23m0177.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.08 seconds (average 0.000307, setup 0.00)

Time for model construction: 0.142 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep4.trew"...
Time for exporting: 1.714 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep4.tra:	Size of output file is 90018223 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep4.lab:	Size of output file is 1398482 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_cluster.128-2000-20_rep5.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep5.tra,lab,rew:precision=17
Wallclock time: 2.504 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:21 GMT+01:00 2026
Hostname: n23m0192.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.07 seconds (average 0.000268, setup 0.00)

Time for model construction: 0.136 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep5.trew"...
Time for exporting: 1.461 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep5.tra:	Size of output file is 90018223 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep5.lab:	Size of output file is 1398482 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_default/cluster.128-2000-20/model_rep5.trew:	File does not exist.
```

