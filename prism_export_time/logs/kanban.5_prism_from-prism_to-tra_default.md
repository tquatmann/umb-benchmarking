# Log files for prism_from-prism_to-tra_default on model [kanban.5](../../models/kanban.5)

Parsed values: `[20.579, 20.675, 18.681, 17.366, 19.915]`



### Log file: prism_from-prism_to-tra_default_kanban.5_rep1.log

```
Command(s):
../bin/prism  models/kanban.5/model.prism -exportmodel out/prism_from-prism_to-tra_default/kanban.5/model.tra,lab,rew:precision=17
Wallclock time: 21.470 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:50:30 GMT+01:00 2026
Hostname: r23m0069.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/kanban.5/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/kanban.5/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 71 iterations in 0.15 seconds (average 0.002113, setup 0.00)

Time for model construction: 0.174 seconds.

Type:        CTMC
States:      2546432 (1 initial)
Transitions: 24460016

Rate matrix: 6308 nodes (14 terminal), 24460016 minterms, vars: 48r/48c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/kanban.5/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/kanban.5/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/kanban.5/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/kanban.5/model.trew"...
Time for exporting: 20.579 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/kanban.5/model.tra:	Size of output file is 828977159 bytes
out/prism_from-prism_to-tra_default/kanban.5/model.lab:	Size of output file is 27 bytes
out/prism_from-prism_to-tra_default/kanban.5/model.srew:	Size of output file is 58 bytes
out/prism_from-prism_to-tra_default/kanban.5/model.trew:	Size of output file is 27081599 bytes
```



### Log file: prism_from-prism_to-tra_default_kanban.5_rep2.log

```
Command(s):
../bin/prism  models/kanban.5/model.prism -exportmodel out/prism_from-prism_to-tra_default/kanban.5/model_rep2.tra,lab,rew:precision=17
Wallclock time: 21.575 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:42:09 GMT+01:00 2026
Hostname: n23m0402.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/kanban.5/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/kanban.5/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 71 iterations in 0.15 seconds (average 0.002113, setup 0.00)

Time for model construction: 0.18 seconds.

Type:        CTMC
States:      2546432 (1 initial)
Transitions: 24460016

Rate matrix: 6308 nodes (14 terminal), 24460016 minterms, vars: 48r/48c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/kanban.5/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/kanban.5/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/kanban.5/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/kanban.5/model_rep2.trew"...
Time for exporting: 20.675 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/kanban.5/model_rep2.tra:	Size of output file is 828977159 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/kanban.5/model_rep2.lab:	Size of output file is 27 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/kanban.5/model_rep2.srew:	Size of output file is 58 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/kanban.5/model_rep2.trew:	Size of output file is 27081599 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_default_kanban.5_rep3.log

```
Command(s):
../bin/prism  models/kanban.5/model.prism -exportmodel out/prism_from-prism_to-tra_default/kanban.5/model_rep3.tra,lab,rew:precision=17
Wallclock time: 19.372 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:51:16 GMT+01:00 2026
Hostname: n23m0109.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/kanban.5/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/kanban.5/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 71 iterations in 0.11 seconds (average 0.001549, setup 0.00)

Time for model construction: 0.128 seconds.

Type:        CTMC
States:      2546432 (1 initial)
Transitions: 24460016

Rate matrix: 6308 nodes (14 terminal), 24460016 minterms, vars: 48r/48c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/kanban.5/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/kanban.5/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/kanban.5/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/kanban.5/model_rep3.trew"...
Time for exporting: 18.681 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/kanban.5/model_rep3.tra:	Size of output file is 828977159 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/kanban.5/model_rep3.lab:	Size of output file is 27 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/kanban.5/model_rep3.srew:	Size of output file is 58 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/kanban.5/model_rep3.trew:	Size of output file is 27081599 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_default_kanban.5_rep4.log

```
Command(s):
../bin/prism  models/kanban.5/model.prism -exportmodel out/prism_from-prism_to-tra_default/kanban.5/model_rep4.tra,lab,rew:precision=17
Wallclock time: 18.047 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:56:50 GMT+01:00 2026
Hostname: n23m0241.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/kanban.5/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/kanban.5/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 71 iterations in 0.10 seconds (average 0.001408, setup 0.00)

Time for model construction: 0.122 seconds.

Type:        CTMC
States:      2546432 (1 initial)
Transitions: 24460016

Rate matrix: 6308 nodes (14 terminal), 24460016 minterms, vars: 48r/48c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/kanban.5/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/kanban.5/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/kanban.5/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/kanban.5/model_rep4.trew"...
Time for exporting: 17.366 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/kanban.5/model_rep4.tra:	Size of output file is 828977159 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/kanban.5/model_rep4.lab:	Size of output file is 27 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/kanban.5/model_rep4.srew:	Size of output file is 58 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/kanban.5/model_rep4.trew:	Size of output file is 27081599 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_default_kanban.5_rep5.log

```
Command(s):
../bin/prism  models/kanban.5/model.prism -exportmodel out/prism_from-prism_to-tra_default/kanban.5/model_rep5.tra,lab,rew:precision=17
Wallclock time: 20.654 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:27:15 GMT+01:00 2026
Hostname: n23m0042.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/kanban.5/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/kanban.5/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 71 iterations in 0.11 seconds (average 0.001549, setup 0.00)

Time for model construction: 0.128 seconds.

Type:        CTMC
States:      2546432 (1 initial)
Transitions: 24460016

Rate matrix: 6308 nodes (14 terminal), 24460016 minterms, vars: 48r/48c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/kanban.5/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/kanban.5/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/kanban.5/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/kanban.5/model_rep5.trew"...
Time for exporting: 19.915 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/kanban.5/model_rep5.tra:	Size of output file is 828977159 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/kanban.5/model_rep5.lab:	Size of output file is 27 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/kanban.5/model_rep5.srew:	Size of output file is 58 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/kanban.5/model_rep5.trew:	Size of output file is 27081599 bytes
Removing output file to save space for repetition #5
```

