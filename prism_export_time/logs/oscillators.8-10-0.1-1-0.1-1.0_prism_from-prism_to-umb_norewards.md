# Log files for prism_from-prism_to-umb_norewards on model [oscillators.8-10-0.1-1-0.1-1.0](../../models/oscillators.8-10-0.1-1-0.1-1.0)

Parsed values: `[0.944, 1.023, 0.783, 1.076, 1.025]`



### Log file: prism_from-prism_to-umb_norewards_oscillators.8-10-0.1-1-0.1-1.0_rep1.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 32.034 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:40:29 GMT+01:00 2026
Hostname: r23m0005.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb:states=false,obs=false,rewards=false,zip=false'

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

Time for model construction: 27.88 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb"...
Model export size: 1701 Kb
Time for exporting: 0.944 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb:	Size of output file is 1741824 bytes
```



### Log file: prism_from-prism_to-umb_norewards_oscillators.8-10-0.1-1-0.1-1.0_rep2.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 28.060 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:59:53 GMT+01:00 2026
Hostname: n23m0042.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.umb:states=false,obs=false,rewards=false,zip=false'

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

Time for model construction: 23.726 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.umb"...
Model export size: 1701 Kb
Time for exporting: 1.023 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.umb:	Size of output file is 1741824 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_norewards_oscillators.8-10-0.1-1-0.1-1.0_rep3.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 23.753 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:27:29 GMT+01:00 2026
Hostname: n23m0383.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.umb:states=false,obs=false,rewards=false,zip=false'

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

Time for model construction: 20.233 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.umb"...
Model export size: 1701 Kb
Time for exporting: 0.783 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.umb:	Size of output file is 1741824 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_norewards_oscillators.8-10-0.1-1-0.1-1.0_rep4.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 39.015 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:09 GMT+01:00 2026
Hostname: r23m0084.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.umb:states=false,obs=false,rewards=false,zip=false'

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

Time for model construction: 33.839 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.umb"...
Model export size: 1701 Kb
Time for exporting: 1.076 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.umb:	Size of output file is 1741824 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_norewards_oscillators.8-10-0.1-1-0.1-1.0_rep5.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 30.291 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:55:19 GMT+01:00 2026
Hostname: r23m0195.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.umb:states=false,obs=false,rewards=false,zip=false'

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

Time for model construction: 25.879 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.umb"...
Model export size: 1701 Kb
Time for exporting: 1.025 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.umb:	Size of output file is 1741824 bytes
Removing output file to save space for repetition #5
```

