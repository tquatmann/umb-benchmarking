# Log files

Tool configuration: prism_from-prism_to-tra_default
Benchmark: [oscillators.8-10-0.1-1-0.1-1.0](../../models/oscillators.8-10-0.1-1-0.1-1.0)
Parsed values: [0.287, 0.427, 0.388, 0.289, 0.354]



### Log file: prism_from-prism_to-tra_default_oscillators.8-10-0.1-1-0.1-1.0_rep1.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model.tra,lab,rew:precision=17
Wallclock time: 23.944 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:33:33 GMT+01:00 2026
Hostname: n23m0244.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model.tra,lab,rew:precision=17'

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

Time for model construction: 20.867 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model.trew"...
Time for exporting: 0.287 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model.tra:	Size of output file is 2481733 bytes
out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model.lab:	Size of output file is 54 bytes
out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model.srew:	Size of output file is 615511 bytes
out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model.trew:	Size of output file is 64 bytes
```



### Log file: prism_from-prism_to-tra_default_oscillators.8-10-0.1-1-0.1-1.0_rep2.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.tra,lab,rew:precision=17
Wallclock time: 34.672 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:56:50 GMT+01:00 2026
Hostname: n23m0165.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.tra,lab,rew:precision=17'

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

Time for model construction: 30.555 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.trew"...
Time for exporting: 0.427 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.tra:	Size of output file is 2481733 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.lab:	Size of output file is 54 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.srew:	Size of output file is 615511 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.trew:	Size of output file is 64 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_default_oscillators.8-10-0.1-1-0.1-1.0_rep3.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.tra,lab,rew:precision=17
Wallclock time: 27.741 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:28:47 GMT+01:00 2026
Hostname: r23m0212.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2 iterations in 0.08 seconds (average 0.040000, setup 0.00)

Time for model construction: 24.289 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.trew"...
Time for exporting: 0.388 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.tra:	Size of output file is 2481733 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.lab:	Size of output file is 54 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.srew:	Size of output file is 615511 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.trew:	Size of output file is 64 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_default_oscillators.8-10-0.1-1-0.1-1.0_rep4.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.tra,lab,rew:precision=17
Wallclock time: 23.116 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:40:37 GMT+01:00 2026
Hostname: n23m0041.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.tra,lab,rew:precision=17'

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

Time for model construction: 20.092 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.trew"...
Time for exporting: 0.289 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.tra:	Size of output file is 2481733 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.lab:	Size of output file is 54 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.srew:	Size of output file is 615511 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.trew:	Size of output file is 64 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_default_oscillators.8-10-0.1-1-0.1-1.0_rep5.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.tra,lab,rew:precision=17
Wallclock time: 29.349 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:31:20 GMT+01:00 2026
Hostname: r23m0212.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.tra,lab,rew:precision=17'

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

Time for model construction: 25.857 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.trew"...
Time for exporting: 0.354 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.tra:	Size of output file is 2481733 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.lab:	Size of output file is 54 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.srew:	Size of output file is 615511 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.trew:	Size of output file is 64 bytes
Removing output file to save space for repetition #5
```

