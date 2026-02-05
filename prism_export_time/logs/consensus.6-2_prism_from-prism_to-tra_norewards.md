# Log files

Tool configuration: prism_from-prism_to-tra_norewards
Benchmark: [consensus.6-2](../../models/consensus.6-2)
Parsed values: [3.753, 3.565, 3.01, 3.026, 2.953]



### Log file: prism_from-prism_to-tra_norewards_consensus.6-2_rep1.log

```
Command(s):
../bin/prism  models/consensus.6-2/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/consensus.6-2/model.tra,lab:precision=17
Wallclock time: 4.586 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:28:33 GMT+01:00 2026
Hostname: n23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.6-2/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/consensus.6-2/model.tra,lab:precision=17'

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 149 iterations in 0.06 seconds (average 0.000403, setup 0.00)

Time for model construction: 0.091 seconds.

Type:        MDP
States:      1258240 (1 initial)
Transitions: 6236736

Transition matrix: 7075 nodes (3 terminal), 6236736 minterms, vars: 24r/24c/6nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/consensus.6-2/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/consensus.6-2/model.lab"...
Time for exporting: 3.753 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/consensus.6-2/model.tra:	Size of output file is 118624455 bytes
out/prism_from-prism_to-tra_norewards/consensus.6-2/model.lab:	Size of output file is 1150296 bytes
```



### Log file: prism_from-prism_to-tra_norewards_consensus.6-2_rep2.log

```
Command(s):
../bin/prism  models/consensus.6-2/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep2.tra,lab:precision=17
Wallclock time: 4.285 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:28 GMT+01:00 2026
Hostname: n23m0364.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.6-2/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep2.tra,lab:precision=17'

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 149 iterations in 0.05 seconds (average 0.000336, setup 0.00)

Time for model construction: 0.086 seconds.

Type:        MDP
States:      1258240 (1 initial)
Transitions: 6236736

Transition matrix: 7075 nodes (3 terminal), 6236736 minterms, vars: 24r/24c/6nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep2.lab"...
Time for exporting: 3.565 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep2.tra:	Size of output file is 118624455 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep2.lab:	Size of output file is 1150296 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_norewards_consensus.6-2_rep3.log

```
Command(s):
../bin/prism  models/consensus.6-2/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep3.tra,lab:precision=17
Wallclock time: 3.640 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:19:07 GMT+01:00 2026
Hostname: n23m0308.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.6-2/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep3.tra,lab:precision=17'

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 149 iterations in 0.05 seconds (average 0.000336, setup 0.00)

Time for model construction: 0.073 seconds.

Type:        MDP
States:      1258240 (1 initial)
Transitions: 6236736

Transition matrix: 7075 nodes (3 terminal), 6236736 minterms, vars: 24r/24c/6nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep3.lab"...
Time for exporting: 3.01 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep3.tra:	Size of output file is 118624455 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep3.lab:	Size of output file is 1150296 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_norewards_consensus.6-2_rep4.log

```
Command(s):
../bin/prism  models/consensus.6-2/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep4.tra,lab:precision=17
Wallclock time: 3.999 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:10 GMT+01:00 2026
Hostname: n23m0154.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.6-2/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep4.tra,lab:precision=17'

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 149 iterations in 0.05 seconds (average 0.000336, setup 0.00)

Time for model construction: 0.096 seconds.

Type:        MDP
States:      1258240 (1 initial)
Transitions: 6236736

Transition matrix: 7075 nodes (3 terminal), 6236736 minterms, vars: 24r/24c/6nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep4.lab"...
Time for exporting: 3.026 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep4.tra:	Size of output file is 118624455 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep4.lab:	Size of output file is 1150296 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_norewards_consensus.6-2_rep5.log

```
Command(s):
../bin/prism  models/consensus.6-2/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep5.tra,lab:precision=17
Wallclock time: 3.891 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:52:47 GMT+01:00 2026
Hostname: n23m0287.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.6-2/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep5.tra,lab:precision=17'

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 149 iterations in 0.05 seconds (average 0.000336, setup 0.00)

Time for model construction: 0.075 seconds.

Type:        MDP
States:      1258240 (1 initial)
Transitions: 6236736

Transition matrix: 7075 nodes (3 terminal), 6236736 minterms, vars: 24r/24c/6nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep5.lab"...
Time for exporting: 2.953 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep5.tra:	Size of output file is 118624455 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_norewards/consensus.6-2/model_rep5.lab:	Size of output file is 1150296 bytes
Removing output file to save space for repetition #5
```

