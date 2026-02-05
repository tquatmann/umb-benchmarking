# Log files

Tool configuration: prism_from-prism_to-umb-gz_norewards
Benchmark: [eajs.6-300-13](../../models/eajs.6-300-13)
Parsed values: [32.437, 29.463, 31.125, 32.928, 31.098]



### Log file: prism_from-prism_to-umb-gz_norewards_eajs.6-300-13_rep1.log

```
Command(s):
../bin/prism  models/eajs.6-300-13/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/eajs.6-300-13/model.umb.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 33.663 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:40:06 GMT+01:00 2026
Hostname: r23m0130.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.6-300-13/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/eajs.6-300-13/model.umb.gz:states=false,obs=false,rewards=false,zip=true'

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

Time for model construction: 0.504 seconds.

Type:        MDP
States:      7901694 (1 initial)
Transitions: 19722777

Transition matrix: 38911 nodes (7 terminal), 19722777 minterms, vars: 50r/50c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/eajs.6-300-13/model.umb.gz"...
Time for exporting: 32.437 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/eajs.6-300-13/model.umb.gz:	Size of output file is 749961178 bytes
```



### Log file: prism_from-prism_to-umb-gz_norewards_eajs.6-300-13_rep2.log

```
Command(s):
../bin/prism  models/eajs.6-300-13/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/eajs.6-300-13/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 30.467 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:31:01 GMT+01:00 2026
Hostname: n23m0380.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.6-300-13/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/eajs.6-300-13/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 89 iterations in 0.14 seconds (average 0.001573, setup 0.00)

Time for model construction: 0.442 seconds.

Type:        MDP
States:      7901694 (1 initial)
Transitions: 19722777

Transition matrix: 38911 nodes (7 terminal), 19722777 minterms, vars: 50r/50c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/eajs.6-300-13/model.umb_rep2.gz"...
Time for exporting: 29.463 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/eajs.6-300-13/model.umb_rep2.gz:	Size of output file is 749961178 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_norewards_eajs.6-300-13_rep3.log

```
Command(s):
../bin/prism  models/eajs.6-300-13/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/eajs.6-300-13/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 32.667 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:02:54 GMT+01:00 2026
Hostname: n23m0041.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.6-300-13/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/eajs.6-300-13/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 89 iterations in 0.21 seconds (average 0.002360, setup 0.00)

Time for model construction: 0.857 seconds.

Type:        MDP
States:      7901694 (1 initial)
Transitions: 19722777

Transition matrix: 38911 nodes (7 terminal), 19722777 minterms, vars: 50r/50c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/eajs.6-300-13/model.umb_rep3.gz"...
Time for exporting: 31.125 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/eajs.6-300-13/model.umb_rep3.gz:	Size of output file is 749961178 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_norewards_eajs.6-300-13_rep4.log

```
Command(s):
../bin/prism  models/eajs.6-300-13/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/eajs.6-300-13/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 34.146 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:02:55 GMT+01:00 2026
Hostname: n23m0058.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.6-300-13/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/eajs.6-300-13/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 89 iterations in 0.18 seconds (average 0.002022, setup 0.00)

Time for model construction: 0.581 seconds.

Type:        MDP
States:      7901694 (1 initial)
Transitions: 19722777

Transition matrix: 38911 nodes (7 terminal), 19722777 minterms, vars: 50r/50c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/eajs.6-300-13/model.umb_rep4.gz"...
Time for exporting: 32.928 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/eajs.6-300-13/model.umb_rep4.gz:	Size of output file is 749961178 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_norewards_eajs.6-300-13_rep5.log

```
Command(s):
../bin/prism  models/eajs.6-300-13/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/eajs.6-300-13/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 32.229 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:44:10 GMT+01:00 2026
Hostname: n23m0342.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.6-300-13/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/eajs.6-300-13/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true'

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

Time for model construction: 0.464 seconds.

Type:        MDP
States:      7901694 (1 initial)
Transitions: 19722777

Transition matrix: 38911 nodes (7 terminal), 19722777 minterms, vars: 50r/50c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/eajs.6-300-13/model.umb_rep5.gz"...
Time for exporting: 31.098 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/eajs.6-300-13/model.umb_rep5.gz:	Size of output file is 749961178 bytes
Removing output file to save space for repetition #5
```

