# Log files

Tool configuration: prism_from-prism_to-tra_default
Benchmark: [fms.8](../../models/fms.8)
Parsed values: [1427153307.0, 1427153307.0, 1427153307.0, 1427153307.0, 1427153307.0]



### Log file: prism_from-prism_to-tra_default_fms.8_rep1.log

```
Command(s):
../bin/prism  models/fms.8/model.prism -exportmodel out/prism_from-prism_to-tra_default/fms.8/model.tra,lab,rew:precision=17
Wallclock time: 64.274 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:36:43 GMT+01:00 2026
Hostname: n23m0110.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/fms.8/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 65 iterations in 3.53 seconds (average 0.054308, setup 0.00)

Time for model construction: 3.724 seconds.

Type:        CTMC
States:      4459455 (1 initial)
Transitions: 38533968

Rate matrix: 215250 nodes (84 terminal), 38533968 minterms, vars: 70r/70c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/fms.8/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/fms.8/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/fms.8/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/fms.8/model.trew"...
Time for exporting: 59.992 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/fms.8/model.tra:	Size of output file is 1197181637 bytes
out/prism_from-prism_to-tra_default/fms.8/model.lab:	Size of output file is 33 bytes
out/prism_from-prism_to-tra_default/fms.8/model.srew:	Size of output file is 60 bytes
out/prism_from-prism_to-tra_default/fms.8/model.trew:	Size of output file is 229971577 bytes
```



### Log file: prism_from-prism_to-tra_default_fms.8_rep2.log

```
Command(s):
../bin/prism  models/fms.8/model.prism -exportmodel out/prism_from-prism_to-tra_default/fms.8/model_rep2.tra,lab,rew:precision=17
Wallclock time: 63.189 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:20 GMT+01:00 2026
Hostname: n23m0169.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/fms.8/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 65 iterations in 3.12 seconds (average 0.048000, setup 0.00)

Time for model construction: 3.316 seconds.

Type:        CTMC
States:      4459455 (1 initial)
Transitions: 38533968

Rate matrix: 215250 nodes (84 terminal), 38533968 minterms, vars: 70r/70c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/fms.8/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/fms.8/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/fms.8/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/fms.8/model_rep2.trew"...
Time for exporting: 58.981 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/fms.8/model_rep2.tra:	Size of output file is 1197181637 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/fms.8/model_rep2.lab:	Size of output file is 33 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/fms.8/model_rep2.srew:	Size of output file is 60 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/fms.8/model_rep2.trew:	Size of output file is 229971577 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_default_fms.8_rep3.log

```
Command(s):
../bin/prism  models/fms.8/model.prism -exportmodel out/prism_from-prism_to-tra_default/fms.8/model_rep3.tra,lab,rew:precision=17
Wallclock time: 71.490 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:01 GMT+01:00 2026
Hostname: n23m0341.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/fms.8/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 65 iterations in 4.94 seconds (average 0.076000, setup 0.00)

Time for model construction: 5.198 seconds.

Type:        CTMC
States:      4459455 (1 initial)
Transitions: 38533968

Rate matrix: 215250 nodes (84 terminal), 38533968 minterms, vars: 70r/70c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/fms.8/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/fms.8/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/fms.8/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/fms.8/model_rep3.trew"...
Time for exporting: 65.67 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/fms.8/model_rep3.tra:	Size of output file is 1197181637 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/fms.8/model_rep3.lab:	Size of output file is 33 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/fms.8/model_rep3.srew:	Size of output file is 60 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/fms.8/model_rep3.trew:	Size of output file is 229971577 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_default_fms.8_rep4.log

```
Command(s):
../bin/prism  models/fms.8/model.prism -exportmodel out/prism_from-prism_to-tra_default/fms.8/model_rep4.tra,lab,rew:precision=17
Wallclock time: 292.847 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:23 GMT+01:00 2026
Hostname: r23m0217.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/fms.8/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 65 iterations in 10.28 seconds (average 0.158154, setup 0.00)

Time for model construction: 10.999 seconds.

Type:        CTMC
States:      4459455 (1 initial)
Transitions: 38533968

Rate matrix: 215250 nodes (84 terminal), 38533968 minterms, vars: 70r/70c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/fms.8/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/fms.8/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/fms.8/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/fms.8/model_rep4.trew"...
Time for exporting: 279.203 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/fms.8/model_rep4.tra:	Size of output file is 1197181637 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/fms.8/model_rep4.lab:	Size of output file is 33 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/fms.8/model_rep4.srew:	Size of output file is 60 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/fms.8/model_rep4.trew:	Size of output file is 229971577 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_default_fms.8_rep5.log

```
Command(s):
../bin/prism  models/fms.8/model.prism -exportmodel out/prism_from-prism_to-tra_default/fms.8/model_rep5.tra,lab,rew:precision=17
Wallclock time: 74.569 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:55:19 GMT+01:00 2026
Hostname: r23m0015.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/fms.8/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 65 iterations in 5.58 seconds (average 0.085846, setup 0.00)

Time for model construction: 5.889 seconds.

Type:        CTMC
States:      4459455 (1 initial)
Transitions: 38533968

Rate matrix: 215250 nodes (84 terminal), 38533968 minterms, vars: 70r/70c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/fms.8/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/fms.8/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/fms.8/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/fms.8/model_rep5.trew"...
Time for exporting: 67.984 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/fms.8/model_rep5.tra:	Size of output file is 1197181637 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/fms.8/model_rep5.lab:	Size of output file is 33 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/fms.8/model_rep5.srew:	Size of output file is 60 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/fms.8/model_rep5.trew:	Size of output file is 229971577 bytes
Removing output file to save space for repetition #5
```

