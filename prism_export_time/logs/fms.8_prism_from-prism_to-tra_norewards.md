# Log files

Tool configuration: prism_from-prism_to-tra_norewards
Benchmark: [fms.8](../../models/fms.8)
Parsed values: [46.307, 46.507, 46.411, 48.897, 47.272]



### Log file: prism_from-prism_to-tra_norewards_fms.8_rep1.log

```
Command(s):
../bin/prism  models/fms.8/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/fms.8/model.tra,lab:precision=17
Wallclock time: 50.432 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:23:16 GMT+01:00 2026
Hostname: n23m0133.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/fms.8/model.tra,lab:precision=17'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 65 iterations in 3.43 seconds (average 0.052769, setup 0.00)

Time for model construction: 3.612 seconds.

Type:        CTMC
States:      4459455 (1 initial)
Transitions: 38533968

Rate matrix: 215250 nodes (84 terminal), 38533968 minterms, vars: 70r/70c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/fms.8/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/fms.8/model.lab"...
Time for exporting: 46.307 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/fms.8/model.tra:	Size of output file is 1197181637 bytes
out/prism_from-prism_to-tra_norewards/fms.8/model.lab:	Size of output file is 33 bytes
```



### Log file: prism_from-prism_to-tra_norewards_fms.8_rep2.log

```
Command(s):
../bin/prism  models/fms.8/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/fms.8/model_rep2.tra,lab:precision=17
Wallclock time: 50.057 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:43:39 GMT+01:00 2026
Hostname: r23m0196.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/fms.8/model_rep2.tra,lab:precision=17'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 65 iterations in 2.87 seconds (average 0.044154, setup 0.00)

Time for model construction: 3.03 seconds.

Type:        CTMC
States:      4459455 (1 initial)
Transitions: 38533968

Rate matrix: 215250 nodes (84 terminal), 38533968 minterms, vars: 70r/70c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/fms.8/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/fms.8/model_rep2.lab"...
Time for exporting: 46.507 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/fms.8/model_rep2.tra:	Size of output file is 1197181637 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_norewards/fms.8/model_rep2.lab:	Size of output file is 33 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_norewards_fms.8_rep3.log

```
Command(s):
../bin/prism  models/fms.8/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/fms.8/model_rep3.tra,lab:precision=17
Wallclock time: 50.765 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:43:38 GMT+01:00 2026
Hostname: n23m0383.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/fms.8/model_rep3.tra,lab:precision=17'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 65 iterations in 3.59 seconds (average 0.055231, setup 0.00)

Time for model construction: 3.779 seconds.

Type:        CTMC
States:      4459455 (1 initial)
Transitions: 38533968

Rate matrix: 215250 nodes (84 terminal), 38533968 minterms, vars: 70r/70c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/fms.8/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/fms.8/model_rep3.lab"...
Time for exporting: 46.411 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/fms.8/model_rep3.tra:	Size of output file is 1197181637 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_norewards/fms.8/model_rep3.lab:	Size of output file is 33 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_norewards_fms.8_rep4.log

```
Command(s):
../bin/prism  models/fms.8/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/fms.8/model_rep4.tra,lab:precision=17
Wallclock time: 52.790 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:24:24 GMT+01:00 2026
Hostname: n23m0341.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/fms.8/model_rep4.tra,lab:precision=17'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 65 iterations in 3.11 seconds (average 0.047846, setup 0.00)

Time for model construction: 3.279 seconds.

Type:        CTMC
States:      4459455 (1 initial)
Transitions: 38533968

Rate matrix: 215250 nodes (84 terminal), 38533968 minterms, vars: 70r/70c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/fms.8/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/fms.8/model_rep4.lab"...
Time for exporting: 48.897 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/fms.8/model_rep4.tra:	Size of output file is 1197181637 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_norewards/fms.8/model_rep4.lab:	Size of output file is 33 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_norewards_fms.8_rep5.log

```
Command(s):
../bin/prism  models/fms.8/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/fms.8/model_rep5.tra,lab:precision=17
Wallclock time: 51.213 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:24:54 GMT+01:00 2026
Hostname: r23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/fms.8/model_rep5.tra,lab:precision=17'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 65 iterations in 3.18 seconds (average 0.048923, setup 0.00)

Time for model construction: 3.366 seconds.

Type:        CTMC
States:      4459455 (1 initial)
Transitions: 38533968

Rate matrix: 215250 nodes (84 terminal), 38533968 minterms, vars: 70r/70c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/fms.8/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/fms.8/model_rep5.lab"...
Time for exporting: 47.272 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/fms.8/model_rep5.tra:	Size of output file is 1197181637 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_norewards/fms.8/model_rep5.lab:	Size of output file is 33 bytes
Removing output file to save space for repetition #5
```

