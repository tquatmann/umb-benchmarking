# Log files for prism_from-prism_to-umb_norewards on model [crowds.5-20](../../models/crowds.5-20)

Parsed values: `[40.959, 42.069, 38.001, 33.778, 40.347]`



### Log file: prism_from-prism_to-umb_norewards_crowds.5-20_rep1.log

```
Command(s):
../bin/prism  models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/crowds.5-20/model.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 42.038 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:44:44 GMT+01:00 2026
Hostname: r23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/crowds.5-20/model.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 47 iterations in 0.14 seconds (average 0.002979, setup 0.00)

Time for model construction: 0.274 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 33232 nodes (7 terminal), 7374951 minterms, vars: 78r/78c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/crowds.5-20/model.umb"...
Model export size: 132104 Kb
Time for exporting: 40.959 seconds.

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/crowds.5-20/model.umb:	Size of output file is 135275008 bytes
```



### Log file: prism_from-prism_to-umb_norewards_crowds.5-20_rep2.log

```
Command(s):
../bin/prism  models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/crowds.5-20/model_rep2.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 43.120 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:10 GMT+01:00 2026
Hostname: n23m0079.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/crowds.5-20/model_rep2.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 47 iterations in 0.12 seconds (average 0.002553, setup 0.00)

Time for model construction: 0.234 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 33232 nodes (7 terminal), 7374951 minterms, vars: 78r/78c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/crowds.5-20/model_rep2.umb"...
Model export size: 132104 Kb
Time for exporting: 42.069 seconds.

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/crowds.5-20/model_rep2.umb:	Size of output file is 135275008 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_norewards_crowds.5-20_rep3.log

```
Command(s):
../bin/prism  models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/crowds.5-20/model_rep3.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 38.882 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:03:26 GMT+01:00 2026
Hostname: r23m0196.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/crowds.5-20/model_rep3.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 47 iterations in 0.13 seconds (average 0.002766, setup 0.00)

Time for model construction: 0.249 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 33232 nodes (7 terminal), 7374951 minterms, vars: 78r/78c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/crowds.5-20/model_rep3.umb"...
Model export size: 132104 Kb
Time for exporting: 38.001 seconds.

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/crowds.5-20/model_rep3.umb:	Size of output file is 135275008 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_norewards_crowds.5-20_rep4.log

```
Command(s):
../bin/prism  models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/crowds.5-20/model_rep4.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 34.437 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:48 GMT+01:00 2026
Hostname: n23m0205.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/crowds.5-20/model_rep4.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 47 iterations in 0.09 seconds (average 0.001915, setup 0.00)

Time for model construction: 0.166 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 33232 nodes (7 terminal), 7374951 minterms, vars: 78r/78c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/crowds.5-20/model_rep4.umb"...
Model export size: 132104 Kb
Time for exporting: 33.778 seconds.

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/crowds.5-20/model_rep4.umb:	Size of output file is 135275008 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_norewards_crowds.5-20_rep5.log

```
Command(s):
../bin/prism  models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/crowds.5-20/model_rep5.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 41.294 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:56:50 GMT+01:00 2026
Hostname: n23m0165.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/crowds.5-20/model_rep5.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 47 iterations in 0.15 seconds (average 0.003191, setup 0.00)

Time for model construction: 0.302 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 33232 nodes (7 terminal), 7374951 minterms, vars: 78r/78c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/crowds.5-20/model_rep5.umb"...
Model export size: 132104 Kb
Time for exporting: 40.347 seconds.

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/crowds.5-20/model_rep5.umb:	Size of output file is 135275008 bytes
Removing output file to save space for repetition #5
```

