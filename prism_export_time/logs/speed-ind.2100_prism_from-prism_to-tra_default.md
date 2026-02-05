# Log files

Tool configuration: prism_from-prism_to-tra_default
Benchmark: [speed-ind.2100](../../models/speed-ind.2100)
Parsed values: [7.542, 7.953, 9.108, 8.73, 7.503]



### Log file: prism_from-prism_to-tra_default_speed-ind.2100_rep1.log

```
Command(s):
../bin/prism  models/speed-ind.2100/model.prism -exportmodel out/prism_from-prism_to-tra_default/speed-ind.2100/model.tra,lab,rew:precision=17
Wallclock time: 28.965 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:28:32 GMT+01:00 2026
Hostname: r23m0134.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/speed-ind.2100/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/speed-ind.2100/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/speed-ind.2100/model.prism"...

Type:        CTMC
Modules:     S1_def S2_def S3_def S4_def Y_def Z_def CC_def XX_def
Actions:     []
Variables:   S1 S2 S3 S4 Y Z CC XX
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.64 seconds (average 0.016842, setup 0.00)

Time for model construction: 20.778 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 33024 nodes (187 terminal), 9518080 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/speed-ind.2100/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/speed-ind.2100/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/speed-ind.2100/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/speed-ind.2100/model.trew"...
Time for exporting: 7.542 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/speed-ind.2100/model.tra:	Size of output file is 333652357 bytes
out/prism_from-prism_to-tra_default/speed-ind.2100/model.lab:	Size of output file is 245803 bytes
out/prism_from-prism_to-tra_default/speed-ind.2100/model.srew:	File does not exist.
out/prism_from-prism_to-tra_default/speed-ind.2100/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_speed-ind.2100_rep2.log

```
Command(s):
../bin/prism  models/speed-ind.2100/model.prism -exportmodel out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep2.tra,lab,rew:precision=17
Wallclock time: 28.693 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:52 GMT+01:00 2026
Hostname: n23m0250.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/speed-ind.2100/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/speed-ind.2100/model.prism"...

Type:        CTMC
Modules:     S1_def S2_def S3_def S4_def Y_def Z_def CC_def XX_def
Actions:     []
Variables:   S1 S2 S3 S4 Y Z CC XX
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.64 seconds (average 0.016842, setup 0.00)

Time for model construction: 20.018 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 33024 nodes (187 terminal), 9518080 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep2.trew"...
Time for exporting: 7.953 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep2.tra:	Size of output file is 333652357 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep2.lab:	Size of output file is 245803 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_speed-ind.2100_rep3.log

```
Command(s):
../bin/prism  models/speed-ind.2100/model.prism -exportmodel out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep3.tra,lab,rew:precision=17
Wallclock time: 37.038 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:01 GMT+01:00 2026
Hostname: r23m0212.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/speed-ind.2100/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/speed-ind.2100/model.prism"...

Type:        CTMC
Modules:     S1_def S2_def S3_def S4_def Y_def Z_def CC_def XX_def
Actions:     []
Variables:   S1 S2 S3 S4 Y Z CC XX
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.80 seconds (average 0.021053, setup 0.00)

Time for model construction: 26.587 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 33024 nodes (187 terminal), 9518080 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep3.trew"...
Time for exporting: 9.108 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep3.tra:	Size of output file is 333652357 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep3.lab:	Size of output file is 245803 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_speed-ind.2100_rep4.log

```
Command(s):
../bin/prism  models/speed-ind.2100/model.prism -exportmodel out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep4.tra,lab,rew:precision=17
Wallclock time: 41.948 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:27:15 GMT+01:00 2026
Hostname: n23m0396.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/speed-ind.2100/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/speed-ind.2100/model.prism"...

Type:        CTMC
Modules:     S1_def S2_def S3_def S4_def Y_def Z_def CC_def XX_def
Actions:     []
Variables:   S1 S2 S3 S4 Y Z CC XX
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.98 seconds (average 0.025789, setup 0.00)

Time for model construction: 32.296 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 33024 nodes (187 terminal), 9518080 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep4.trew"...
Time for exporting: 8.73 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep4.tra:	Size of output file is 333652357 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep4.lab:	Size of output file is 245803 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_speed-ind.2100_rep5.log

```
Command(s):
../bin/prism  models/speed-ind.2100/model.prism -exportmodel out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep5.tra,lab,rew:precision=17
Wallclock time: 28.418 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:21 GMT+01:00 2026
Hostname: n23m0192.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/speed-ind.2100/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/speed-ind.2100/model.prism"...

Type:        CTMC
Modules:     S1_def S2_def S3_def S4_def Y_def Z_def CC_def XX_def
Actions:     []
Variables:   S1 S2 S3 S4 Y Z CC XX
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.63 seconds (average 0.016579, setup 0.00)

Time for model construction: 19.856 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 33024 nodes (187 terminal), 9518080 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep5.trew"...
Time for exporting: 7.503 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep5.tra:	Size of output file is 333652357 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep5.lab:	Size of output file is 245803 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_default/speed-ind.2100/model_rep5.trew:	File does not exist.
```

