# Log files

Tool configuration: prism_from-prism_to-umb_default
Benchmark: [oscillators.8-10-0.1-1-0.1-1.0](../../models/oscillators.8-10-0.1-1-0.1-1.0)
Parsed values: [1936896.0, 1936896.0, 1936896.0, 1936896.0, 1936896.0]



### Log file: prism_from-prism_to-umb_default_oscillators.8-10-0.1-1-0.1-1.0_rep1.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb_default/oscillators.8-10-0.1-1-0.1-1.0/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 24.613 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:39:25 GMT+01:00 2026
Hostname: r23m0157.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/oscillators.8-10-0.1-1-0.1-1.0/model.umb:states=false,obs=false,rewards=true,zip=false'

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

Time for model construction: 21.008 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/oscillators.8-10-0.1-1-0.1-1.0/model.umb"...
Model export size: 1891 Kb
Time for exporting: 0.936 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/oscillators.8-10-0.1-1-0.1-1.0/model.umb:	Size of output file is 1936896 bytes
```



### Log file: prism_from-prism_to-umb_default_oscillators.8-10-0.1-1-0.1-1.0_rep2.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 24.054 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:21 GMT+01:00 2026
Hostname: n23m0061.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2 iterations in 0.05 seconds (average 0.025000, setup 0.00)

Time for model construction: 20.435 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.umb"...
Model export size: 1891 Kb
Time for exporting: 0.781 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.umb:	Size of output file is 1936896 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_default_oscillators.8-10-0.1-1-0.1-1.0_rep3.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 36.279 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:53:48 GMT+01:00 2026
Hostname: n23m0113.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

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

Time for model construction: 31.967 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.umb"...
Model export size: 1891 Kb
Time for exporting: 0.881 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.umb:	Size of output file is 1936896 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_default_oscillators.8-10-0.1-1-0.1-1.0_rep4.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 27.313 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:11 GMT+01:00 2026
Hostname: n23m0160.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

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

Time for model construction: 23.194 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.umb"...
Model export size: 1891 Kb
Time for exporting: 0.964 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.umb:	Size of output file is 1936896 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_default_oscillators.8-10-0.1-1-0.1-1.0_rep5.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 25.939 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:21:09 GMT+01:00 2026
Hostname: n23m0389.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

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

Time for model construction: 22.178 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.umb"...
Model export size: 1891 Kb
Time for exporting: 0.959 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.umb:	Size of output file is 1936896 bytes
Removing output file to save space for repetition #5
```

