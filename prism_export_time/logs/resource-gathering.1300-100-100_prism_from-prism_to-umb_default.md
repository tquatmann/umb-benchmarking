# Log files

Tool configuration: prism_from-prism_to-umb_default
Benchmark: [resource-gathering.1300-100-100](../../models/resource-gathering.1300-100-100)
Parsed values: [5.57, 7.757, 7.848, 6.643, 5.392]



### Log file: prism_from-prism_to-umb_default_resource-gathering.1300-100-100_rep1.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism -exportmodel out/prism_from-prism_to-umb_default/resource-gathering.1300-100-100/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 9.131 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:27:32 GMT+01:00 2026
Hostname: r23m0055.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/resource-gathering.1300-100-100/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/resource-gathering.1300-100-100/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1215 iterations in 0.40 seconds (average 0.000329, setup 0.00)

Time for model construction: 0.513 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/resource-gathering.1300-100-100/model.umb"...
Model export size: 95798 Kb
Time for exporting: 5.57 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/resource-gathering.1300-100-100/model.umb:	Size of output file is 98097664 bytes
```



### Log file: prism_from-prism_to-umb_default_resource-gathering.1300-100-100_rep2.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism -exportmodel out/prism_from-prism_to-umb_default/resource-gathering.1300-100-100/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 8.794 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:10 GMT+01:00 2026
Hostname: n23m0218.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/resource-gathering.1300-100-100/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/resource-gathering.1300-100-100/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1215 iterations in 0.42 seconds (average 0.000346, setup 0.00)

Time for model construction: 0.451 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/resource-gathering.1300-100-100/model_rep2.umb"...
Model export size: 95798 Kb
Time for exporting: 7.757 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/resource-gathering.1300-100-100/model_rep2.umb:	Size of output file is 98097664 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_default_resource-gathering.1300-100-100_rep3.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism -exportmodel out/prism_from-prism_to-umb_default/resource-gathering.1300-100-100/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 9.284 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:26:08 GMT+01:00 2026
Hostname: n23m0017.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/resource-gathering.1300-100-100/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/resource-gathering.1300-100-100/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1215 iterations in 0.59 seconds (average 0.000486, setup 0.00)

Time for model construction: 0.655 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/resource-gathering.1300-100-100/model_rep3.umb"...
Model export size: 95798 Kb
Time for exporting: 7.848 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/resource-gathering.1300-100-100/model_rep3.umb:	Size of output file is 98097664 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_default_resource-gathering.1300-100-100_rep4.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism -exportmodel out/prism_from-prism_to-umb_default/resource-gathering.1300-100-100/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 7.930 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:18:38 GMT+01:00 2026
Hostname: n23m0096.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/resource-gathering.1300-100-100/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/resource-gathering.1300-100-100/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1215 iterations in 0.58 seconds (average 0.000477, setup 0.00)

Time for model construction: 0.611 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/resource-gathering.1300-100-100/model_rep4.umb"...
Model export size: 95798 Kb
Time for exporting: 6.643 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/resource-gathering.1300-100-100/model_rep4.umb:	Size of output file is 98097664 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_default_resource-gathering.1300-100-100_rep5.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism -exportmodel out/prism_from-prism_to-umb_default/resource-gathering.1300-100-100/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 6.399 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:45:40 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/resource-gathering.1300-100-100/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/resource-gathering.1300-100-100/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1215 iterations in 0.44 seconds (average 0.000362, setup 0.00)

Time for model construction: 0.462 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/resource-gathering.1300-100-100/model_rep5.umb"...
Model export size: 95798 Kb
Time for exporting: 5.392 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/resource-gathering.1300-100-100/model_rep5.umb:	Size of output file is 98097664 bytes
Removing output file to save space for repetition #5
```

