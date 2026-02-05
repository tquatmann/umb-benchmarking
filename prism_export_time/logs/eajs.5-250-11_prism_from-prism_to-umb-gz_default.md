# Log files for prism_from-prism_to-umb-gz_default on model [eajs.5-250-11](../../models/eajs.5-250-11)

Parsed values: `[9.412, 10.685, 9.381, 9.085, 9.299]`



### Log file: prism_from-prism_to-umb-gz_default_eajs.5-250-11_rep1.log

```
Command(s):
../bin/prism  models/eajs.5-250-11/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/eajs.5-250-11/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 10.253 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:41:38 GMT+01:00 2026
Hostname: r23m0131.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.5-250-11/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/eajs.5-250-11/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

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

Time for model construction: 0.3 seconds.

Type:        MDP
States:      3049471 (1 initial)
Transitions: 6977654

Transition matrix: 25363 nodes (7 terminal), 6977654 minterms, vars: 43r/43c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/eajs.5-250-11/model.umb.gz"...
Time for exporting: 9.412 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/eajs.5-250-11/model.umb.gz:	Size of output file is 260469420 bytes
```



### Log file: prism_from-prism_to-umb-gz_default_eajs.5-250-11_rep2.log

```
Command(s):
../bin/prism  models/eajs.5-250-11/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/eajs.5-250-11/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 13.408 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:42 GMT+01:00 2026
Hostname: n23m0227.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.5-250-11/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/eajs.5-250-11/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

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

Time for model construction: 0.346 seconds.

Type:        MDP
States:      3049471 (1 initial)
Transitions: 6977654

Transition matrix: 25363 nodes (7 terminal), 6977654 minterms, vars: 43r/43c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/eajs.5-250-11/model.umb_rep2.gz"...
Time for exporting: 10.685 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/eajs.5-250-11/model.umb_rep2.gz:	Size of output file is 260469420 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_default_eajs.5-250-11_rep3.log

```
Command(s):
../bin/prism  models/eajs.5-250-11/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/eajs.5-250-11/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 11.507 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:32:22 GMT+01:00 2026
Hostname: n23m0328.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.5-250-11/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/eajs.5-250-11/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

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

Time for model construction: 0.329 seconds.

Type:        MDP
States:      3049471 (1 initial)
Transitions: 6977654

Transition matrix: 25363 nodes (7 terminal), 6977654 minterms, vars: 43r/43c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/eajs.5-250-11/model.umb_rep3.gz"...
Time for exporting: 9.381 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/eajs.5-250-11/model.umb_rep3.gz:	Size of output file is 260469420 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_default_eajs.5-250-11_rep4.log

```
Command(s):
../bin/prism  models/eajs.5-250-11/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/eajs.5-250-11/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 9.896 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:18:36 GMT+01:00 2026
Hostname: n23m0033.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.5-250-11/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/eajs.5-250-11/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

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

Time for model construction: 0.269 seconds.

Type:        MDP
States:      3049471 (1 initial)
Transitions: 6977654

Transition matrix: 25363 nodes (7 terminal), 6977654 minterms, vars: 43r/43c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/eajs.5-250-11/model.umb_rep4.gz"...
Time for exporting: 9.085 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/eajs.5-250-11/model.umb_rep4.gz:	Size of output file is 260469420 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_default_eajs.5-250-11_rep5.log

```
Command(s):
../bin/prism  models/eajs.5-250-11/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/eajs.5-250-11/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 10.161 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:26:44 GMT+01:00 2026
Hostname: n23m0249.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.5-250-11/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/eajs.5-250-11/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

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

Time for model construction: 0.277 seconds.

Type:        MDP
States:      3049471 (1 initial)
Transitions: 6977654

Transition matrix: 25363 nodes (7 terminal), 6977654 minterms, vars: 43r/43c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/eajs.5-250-11/model.umb_rep5.gz"...
Time for exporting: 9.299 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/eajs.5-250-11/model.umb_rep5.gz:	Size of output file is 260469420 bytes
Removing output file to save space for repetition #5
```

