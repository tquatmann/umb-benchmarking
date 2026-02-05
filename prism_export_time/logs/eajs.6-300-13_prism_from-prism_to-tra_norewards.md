# Log files

Tool configuration: prism_from-prism_to-tra_norewards
Benchmark: [eajs.6-300-13](../../models/eajs.6-300-13)
Parsed values: [32.529, 34.74, 29.675, 36.827, 29.594]



### Log file: prism_from-prism_to-tra_norewards_eajs.6-300-13_rep1.log

```
Command(s):
../bin/prism  models/eajs.6-300-13/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model.tra,lab:precision=17
Wallclock time: 34.270 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:43:11 GMT+01:00 2026
Hostname: n23m0389.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.6-300-13/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model.tra,lab:precision=17'

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 89 iterations in 0.22 seconds (average 0.002472, setup 0.00)

Time for model construction: 0.789 seconds.

Type:        MDP
States:      7901694 (1 initial)
Transitions: 19722777

Transition matrix: 38911 nodes (7 terminal), 19722777 minterms, vars: 50r/50c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model.lab"...
Time for exporting: 32.529 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model.tra:	Size of output file is 765312868 bytes
out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model.lab:	Size of output file is 246520 bytes
```



### Log file: prism_from-prism_to-tra_norewards_eajs.6-300-13_rep2.log

```
Command(s):
../bin/prism  models/eajs.6-300-13/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep2.tra,lab:precision=17
Wallclock time: 37.008 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:21 GMT+01:00 2026
Hostname: r23m0047.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.6-300-13/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep2.tra,lab:precision=17'

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 89 iterations in 0.24 seconds (average 0.002697, setup 0.00)

Time for model construction: 1.088 seconds.

Type:        MDP
States:      7901694 (1 initial)
Transitions: 19722777

Transition matrix: 38911 nodes (7 terminal), 19722777 minterms, vars: 50r/50c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep2.lab"...
Time for exporting: 34.74 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep2.tra:	Size of output file is 765312868 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep2.lab:	Size of output file is 246520 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_norewards_eajs.6-300-13_rep3.log

```
Command(s):
../bin/prism  models/eajs.6-300-13/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep3.tra,lab:precision=17
Wallclock time: 30.675 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:46:10 GMT+01:00 2026
Hostname: n23m0383.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.6-300-13/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep3.tra,lab:precision=17'

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 89 iterations in 0.15 seconds (average 0.001685, setup 0.00)

Time for model construction: 0.469 seconds.

Type:        MDP
States:      7901694 (1 initial)
Transitions: 19722777

Transition matrix: 38911 nodes (7 terminal), 19722777 minterms, vars: 50r/50c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep3.lab"...
Time for exporting: 29.675 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep3.tra:	Size of output file is 765312868 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep3.lab:	Size of output file is 246520 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_norewards_eajs.6-300-13_rep4.log

```
Command(s):
../bin/prism  models/eajs.6-300-13/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep4.tra,lab:precision=17
Wallclock time: 38.246 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:10 GMT+01:00 2026
Hostname: n23m0162.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.6-300-13/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep4.tra,lab:precision=17'

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 89 iterations in 0.20 seconds (average 0.002247, setup 0.00)

Time for model construction: 0.646 seconds.

Type:        MDP
States:      7901694 (1 initial)
Transitions: 19722777

Transition matrix: 38911 nodes (7 terminal), 19722777 minterms, vars: 50r/50c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep4.lab"...
Time for exporting: 36.827 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep4.tra:	Size of output file is 765312868 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep4.lab:	Size of output file is 246520 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_norewards_eajs.6-300-13_rep5.log

```
Command(s):
../bin/prism  models/eajs.6-300-13/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep5.tra,lab:precision=17
Wallclock time: 32.252 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:03 GMT+01:00 2026
Hostname: r23m0022.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.6-300-13/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep5.tra,lab:precision=17'

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 89 iterations in 0.16 seconds (average 0.001798, setup 0.00)

Time for model construction: 0.571 seconds.

Type:        MDP
States:      7901694 (1 initial)
Transitions: 19722777

Transition matrix: 38911 nodes (7 terminal), 19722777 minterms, vars: 50r/50c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep5.lab"...
Time for exporting: 29.594 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep5.tra:	Size of output file is 765312868 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_norewards/eajs.6-300-13/model_rep5.lab:	Size of output file is 246520 bytes
Removing output file to save space for repetition #5
```

