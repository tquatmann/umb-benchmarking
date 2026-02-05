# Log files

Tool configuration: prism_from-prism_to-tra_norewards
Benchmark: [resource-gathering.1300-100-100](../../models/resource-gathering.1300-100-100)
Parsed values: [84604300.0, 84604300.0, 84604300.0, 84604300.0, 84604300.0]



### Log file: prism_from-prism_to-tra_norewards_resource-gathering.1300-100-100_rep1.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model.tra,lab:precision=17
Wallclock time: 2.849 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:43:09 GMT+01:00 2026
Hostname: r23m0129.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/resource-gathering.1300-100-100/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model.tra,lab:precision=17'

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1215 iterations in 0.43 seconds (average 0.000354, setup 0.00)

Time for model construction: 0.455 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model.lab"...
Time for exporting: 1.833 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model.tra:	Size of output file is 84603330 bytes
out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model.lab:	Size of output file is 970 bytes
```



### Log file: prism_from-prism_to-tra_norewards_resource-gathering.1300-100-100_rep2.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep2.tra,lab:precision=17
Wallclock time: 2.739 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:25:43 GMT+01:00 2026
Hostname: n23m0109.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/resource-gathering.1300-100-100/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep2.tra,lab:precision=17'

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1215 iterations in 0.46 seconds (average 0.000379, setup 0.00)

Time for model construction: 0.491 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep2.lab"...
Time for exporting: 1.688 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep2.tra:	Size of output file is 84603330 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep2.lab:	Size of output file is 970 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_norewards_resource-gathering.1300-100-100_rep3.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep3.tra,lab:precision=17
Wallclock time: 2.545 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:25:13 GMT+01:00 2026
Hostname: n23m0138.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/resource-gathering.1300-100-100/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep3.tra,lab:precision=17'

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1215 iterations in 0.37 seconds (average 0.000305, setup 0.00)

Time for model construction: 0.393 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep3.lab"...
Time for exporting: 1.597 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep3.tra:	Size of output file is 84603330 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep3.lab:	Size of output file is 970 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_norewards_resource-gathering.1300-100-100_rep4.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep4.tra,lab:precision=17
Wallclock time: 2.843 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:26:08 GMT+01:00 2026
Hostname: r23m0037.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/resource-gathering.1300-100-100/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep4.tra,lab:precision=17'

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1215 iterations in 0.42 seconds (average 0.000346, setup 0.00)

Time for model construction: 0.446 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep4.lab"...
Time for exporting: 1.788 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep4.tra:	Size of output file is 84603330 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep4.lab:	Size of output file is 970 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_norewards_resource-gathering.1300-100-100_rep5.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep5.tra,lab:precision=17
Wallclock time: 11.629 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:47:50 GMT+01:00 2026
Hostname: r23m0215.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/resource-gathering.1300-100-100/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep5.tra,lab:precision=17'

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1215 iterations in 1.63 seconds (average 0.001342, setup 0.00)

Time for model construction: 1.774 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep5.lab"...
Time for exporting: 7.229 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep5.tra:	Size of output file is 84603330 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_norewards/resource-gathering.1300-100-100/model_rep5.lab:	Size of output file is 970 bytes
Removing output file to save space for repetition #5
```

