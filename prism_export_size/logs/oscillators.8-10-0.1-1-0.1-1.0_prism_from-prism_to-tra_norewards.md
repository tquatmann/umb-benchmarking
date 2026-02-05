# Log files

Tool configuration: prism_from-prism_to-tra_norewards
Benchmark: [oscillators.8-10-0.1-1-0.1-1.0](../../models/oscillators.8-10-0.1-1-0.1-1.0)
Parsed values: [2481787.0, 2481787.0, 2481787.0, 2481787.0, 2481787.0]



### Log file: prism_from-prism_to-tra_norewards_oscillators.8-10-0.1-1-0.1-1.0_rep1.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.tra,lab:precision=17
Wallclock time: 25.376 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:37:49 GMT+01:00 2026
Hostname: n23m0113.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.tra,lab:precision=17'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2 iterations in 0.07 seconds (average 0.035000, setup 0.00)

Time for model construction: 22.343 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.lab"...
Time for exporting: 0.292 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.tra:	Size of output file is 2481733 bytes
out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.lab:	Size of output file is 54 bytes
```



### Log file: prism_from-prism_to-tra_norewards_oscillators.8-10-0.1-1-0.1-1.0_rep2.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.tra,lab:precision=17
Wallclock time: 24.001 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:48 GMT+01:00 2026
Hostname: n23m0204.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.tra,lab:precision=17'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2 iterations in 0.06 seconds (average 0.030000, setup 0.00)

Time for model construction: 20.986 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.lab"...
Time for exporting: 0.268 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.tra:	Size of output file is 2481733 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.lab:	Size of output file is 54 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_norewards_oscillators.8-10-0.1-1-0.1-1.0_rep3.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.tra,lab:precision=17
Wallclock time: 28.483 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:49:15 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.tra,lab:precision=17'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2 iterations in 0.07 seconds (average 0.035000, setup 0.00)

Time for model construction: 25.377 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.lab"...
Time for exporting: 0.33 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.tra:	Size of output file is 2481733 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.lab:	Size of output file is 54 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_norewards_oscillators.8-10-0.1-1-0.1-1.0_rep4.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.tra,lab:precision=17
Wallclock time: 35.297 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:54:18 GMT+01:00 2026
Hostname: r23m0015.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.tra,lab:precision=17'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2 iterations in 0.09 seconds (average 0.045000, setup 0.00)

Time for model construction: 31.545 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.lab"...
Time for exporting: 0.432 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.tra:	Size of output file is 2481733 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.lab:	Size of output file is 54 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_norewards_oscillators.8-10-0.1-1-0.1-1.0_rep5.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.tra,lab:precision=17
Wallclock time: 43.357 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:28 GMT+01:00 2026
Hostname: n23m0063.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.tra,lab:precision=17'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2 iterations in 0.12 seconds (average 0.060000, setup 0.00)

Time for model construction: 39.584 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.lab"...
Time for exporting: 0.459 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.tra:	Size of output file is 2481733 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.lab:	Size of output file is 54 bytes
Removing output file to save space for repetition #5
```

