# Log files for prism_from-prism_to-tra_default on model [eajs.5-250-11](../../models/eajs.5-250-11)

Parsed values: `[267926272.0, 267926272.0, 267926272.0, 267926272.0, 267926272.0]`



### Log file: prism_from-prism_to-tra_default_eajs.5-250-11_rep1.log

```
Command(s):
../bin/prism  models/eajs.5-250-11/model.prism -exportmodel out/prism_from-prism_to-tra_default/eajs.5-250-11/model.tra,lab,rew:precision=17
Wallclock time: 12.631 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:40:06 GMT+01:00 2026
Hostname: r23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.5-250-11/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/eajs.5-250-11/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/eajs.5-250-11/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_5 Process_4
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 loc_5 t_5 t_4 loc_4
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.09 seconds (average 0.001233, setup 0.00)

Time for model construction: 0.376 seconds.

Type:        MDP
States:      3049471 (1 initial)
Transitions: 6977654

Transition matrix: 25363 nodes (7 terminal), 6977654 minterms, vars: 43r/43c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/eajs.5-250-11/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/eajs.5-250-11/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/eajs.5-250-11/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/eajs.5-250-11/model.trew"...
Time for exporting: 10.695 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/eajs.5-250-11/model.tra:	Size of output file is 265797862 bytes
out/prism_from-prism_to-tra_default/eajs.5-250-11/model.lab:	Size of output file is 110224 bytes
out/prism_from-prism_to-tra_default/eajs.5-250-11/model.srew:	Size of output file is 60 bytes
out/prism_from-prism_to-tra_default/eajs.5-250-11/model.trew:	Size of output file is 2018126 bytes
```



### Log file: prism_from-prism_to-tra_default_eajs.5-250-11_rep2.log

```
Command(s):
../bin/prism  models/eajs.5-250-11/model.prism -exportmodel out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep2.tra,lab,rew:precision=17
Wallclock time: 11.274 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:08 GMT+01:00 2026
Hostname: n23m0138.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.5-250-11/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/eajs.5-250-11/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_5 Process_4
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 loc_5 t_5 t_4 loc_4
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.08 seconds (average 0.001096, setup 0.00)

Time for model construction: 0.256 seconds.

Type:        MDP
States:      3049471 (1 initial)
Transitions: 6977654

Transition matrix: 25363 nodes (7 terminal), 6977654 minterms, vars: 43r/43c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep2.trew"...
Time for exporting: 10.499 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep2.tra:	Size of output file is 265797862 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep2.lab:	Size of output file is 110224 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep2.srew:	Size of output file is 60 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep2.trew:	Size of output file is 2018126 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_default_eajs.5-250-11_rep3.log

```
Command(s):
../bin/prism  models/eajs.5-250-11/model.prism -exportmodel out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep3.tra,lab,rew:precision=17
Wallclock time: 13.604 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:22 GMT+01:00 2026
Hostname: n23m0180.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.5-250-11/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/eajs.5-250-11/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_5 Process_4
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 loc_5 t_5 t_4 loc_4
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.11 seconds (average 0.001507, setup 0.00)

Time for model construction: 0.352 seconds.

Type:        MDP
States:      3049471 (1 initial)
Transitions: 6977654

Transition matrix: 25363 nodes (7 terminal), 6977654 minterms, vars: 43r/43c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep3.trew"...
Time for exporting: 12.37 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep3.tra:	Size of output file is 265797862 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep3.lab:	Size of output file is 110224 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep3.srew:	Size of output file is 60 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep3.trew:	Size of output file is 2018126 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_default_eajs.5-250-11_rep4.log

```
Command(s):
../bin/prism  models/eajs.5-250-11/model.prism -exportmodel out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep4.tra,lab,rew:precision=17
Wallclock time: 52.996 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:56:26 GMT+01:00 2026
Hostname: r23m0217.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.5-250-11/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/eajs.5-250-11/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_5 Process_4
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 loc_5 t_5 t_4 loc_4
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.40 seconds (average 0.005479, setup 0.00)

Time for model construction: 1.266 seconds.

Type:        MDP
States:      3049471 (1 initial)
Transitions: 6977654

Transition matrix: 25363 nodes (7 terminal), 6977654 minterms, vars: 43r/43c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep4.trew"...
Time for exporting: 49.641 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep4.tra:	Size of output file is 265797862 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep4.lab:	Size of output file is 110224 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep4.srew:	Size of output file is 60 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep4.trew:	Size of output file is 2018126 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_default_eajs.5-250-11_rep5.log

```
Command(s):
../bin/prism  models/eajs.5-250-11/model.prism -exportmodel out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep5.tra,lab,rew:precision=17
Wallclock time: 14.572 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:41:09 GMT+01:00 2026
Hostname: n23m0402.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.5-250-11/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/eajs.5-250-11/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_5 Process_4
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 loc_5 t_5 t_4 loc_4
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.13 seconds (average 0.001781, setup 0.00)

Time for model construction: 0.582 seconds.

Type:        MDP
States:      3049471 (1 initial)
Transitions: 6977654

Transition matrix: 25363 nodes (7 terminal), 6977654 minterms, vars: 43r/43c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep5.trew"...
Time for exporting: 13.248 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep5.tra:	Size of output file is 265797862 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep5.lab:	Size of output file is 110224 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep5.srew:	Size of output file is 60 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/eajs.5-250-11/model_rep5.trew:	Size of output file is 2018126 bytes
Removing output file to save space for repetition #5
```

