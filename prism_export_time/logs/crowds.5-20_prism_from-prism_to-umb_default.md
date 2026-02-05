# Log files for prism_from-prism_to-umb_default on model [crowds.5-20](../../models/crowds.5-20)

Parsed values: `[39.339, 42.29, 34.038, 39.709, 33.734]`



### Log file: prism_from-prism_to-umb_default_crowds.5-20_rep1.log

```
Command(s):
../bin/prism  models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-umb_default/crowds.5-20/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 40.175 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:30:56 GMT+01:00 2026
Hostname: n23m0241.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/crowds.5-20/model.umb:states=false,obs=false,rewards=true,zip=false'

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

Reachability (BFS): 47 iterations in 0.10 seconds (average 0.002128, setup 0.00)

Time for model construction: 0.204 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 33232 nodes (7 terminal), 7374951 minterms, vars: 78r/78c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/crowds.5-20/model.umb"...
Model export size: 132104 Kb
Time for exporting: 39.339 seconds.

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/crowds.5-20/model.umb:	Size of output file is 135275008 bytes
```



### Log file: prism_from-prism_to-umb_default_crowds.5-20_rep2.log

```
Command(s):
../bin/prism  models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-umb_default/crowds.5-20/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 43.405 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:45:41 GMT+01:00 2026
Hostname: n23m0402.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/crowds.5-20/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

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

Reachability (BFS): 47 iterations in 0.21 seconds (average 0.004468, setup 0.00)

Time for model construction: 0.372 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 33232 nodes (7 terminal), 7374951 minterms, vars: 78r/78c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/crowds.5-20/model_rep2.umb"...
Model export size: 132104 Kb
Time for exporting: 42.29 seconds.

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/crowds.5-20/model_rep2.umb:	Size of output file is 135275008 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_default_crowds.5-20_rep3.log

```
Command(s):
../bin/prism  models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-umb_default/crowds.5-20/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 34.783 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:17:34 GMT+01:00 2026
Hostname: n23m0033.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/crowds.5-20/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

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

Time for model construction: 0.18 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 33232 nodes (7 terminal), 7374951 minterms, vars: 78r/78c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/crowds.5-20/model_rep3.umb"...
Model export size: 132104 Kb
Time for exporting: 34.038 seconds.

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/crowds.5-20/model_rep3.umb:	Size of output file is 135275008 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_default_crowds.5-20_rep4.log

```
Command(s):
../bin/prism  models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-umb_default/crowds.5-20/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 40.914 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:08 GMT+01:00 2026
Hostname: n23m0308.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/crowds.5-20/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

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

Reachability (BFS): 47 iterations in 0.10 seconds (average 0.002128, setup 0.00)

Time for model construction: 0.213 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 33232 nodes (7 terminal), 7374951 minterms, vars: 78r/78c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/crowds.5-20/model_rep4.umb"...
Model export size: 132104 Kb
Time for exporting: 39.709 seconds.

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/crowds.5-20/model_rep4.umb:	Size of output file is 135275008 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_default_crowds.5-20_rep5.log

```
Command(s):
../bin/prism  models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-umb_default/crowds.5-20/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 34.399 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:51 GMT+01:00 2026
Hostname: n23m0138.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/crowds.5-20/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

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

Time for model construction: 0.165 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 33232 nodes (7 terminal), 7374951 minterms, vars: 78r/78c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/crowds.5-20/model_rep5.umb"...
Model export size: 132104 Kb
Time for exporting: 33.734 seconds.

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/crowds.5-20/model_rep5.umb:	Size of output file is 135275008 bytes
Removing output file to save space for repetition #5
```

