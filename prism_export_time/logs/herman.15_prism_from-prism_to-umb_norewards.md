# Log files

Tool configuration: prism_from-prism_to-umb_norewards
Benchmark: [herman.15](../../models/herman.15)
Parsed values: [17.167, 17.108, 14.775, 15.474, 16.072]



### Log file: prism_from-prism_to-umb_norewards_herman.15_rep1.log

```
Command(s):
../bin/prism  models/herman.15/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/herman.15/model.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 17.859 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:35:41 GMT+01:00 2026
Hostname: n23m0099.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/herman.15/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/herman.15/model.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/herman.15/model.prism"...

Type:        DTMC
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10 process11 process12 process13 process14 process15
Actions:     [step]
Variables:   x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15
Labels:      "stable"
Rewards:     "steps"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.015 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908

Transition matrix: 810 nodes (9 terminal), 14348908 minterms, vars: 15r/15c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/herman.15/model.umb"...
Model export size: 280524 Kb
Time for exporting: 17.167 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/herman.15/model.umb:	Size of output file is 287257088 bytes
```



### Log file: prism_from-prism_to-umb_norewards_herman.15_rep2.log

```
Command(s):
../bin/prism  models/herman.15/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/herman.15/model_rep2.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 17.691 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:01:24 GMT+01:00 2026
Hostname: n23m0042.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/herman.15/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/herman.15/model_rep2.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/herman.15/model.prism"...

Type:        DTMC
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10 process11 process12 process13 process14 process15
Actions:     [step]
Variables:   x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15
Labels:      "stable"
Rewards:     "steps"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.014 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908

Transition matrix: 810 nodes (9 terminal), 14348908 minterms, vars: 15r/15c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/herman.15/model_rep2.umb"...
Model export size: 280524 Kb
Time for exporting: 17.108 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/herman.15/model_rep2.umb:	Size of output file is 287257088 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_norewards_herman.15_rep3.log

```
Command(s):
../bin/prism  models/herman.15/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/herman.15/model_rep3.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 15.309 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:14 GMT+01:00 2026
Hostname: r23m0197.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/herman.15/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/herman.15/model_rep3.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/herman.15/model.prism"...

Type:        DTMC
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10 process11 process12 process13 process14 process15
Actions:     [step]
Variables:   x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15
Labels:      "stable"
Rewards:     "steps"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.013 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908

Transition matrix: 810 nodes (9 terminal), 14348908 minterms, vars: 15r/15c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/herman.15/model_rep3.umb"...
Model export size: 280524 Kb
Time for exporting: 14.775 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/herman.15/model_rep3.umb:	Size of output file is 287257088 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_norewards_herman.15_rep4.log

```
Command(s):
../bin/prism  models/herman.15/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/herman.15/model_rep4.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 15.987 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:34:02 GMT+01:00 2026
Hostname: n23m0281.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/herman.15/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/herman.15/model_rep4.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/herman.15/model.prism"...

Type:        DTMC
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10 process11 process12 process13 process14 process15
Actions:     [step]
Variables:   x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15
Labels:      "stable"
Rewards:     "steps"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.013 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908

Transition matrix: 810 nodes (9 terminal), 14348908 minterms, vars: 15r/15c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/herman.15/model_rep4.umb"...
Model export size: 280524 Kb
Time for exporting: 15.474 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/herman.15/model_rep4.umb:	Size of output file is 287257088 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_norewards_herman.15_rep5.log

```
Command(s):
../bin/prism  models/herman.15/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/herman.15/model_rep5.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 16.699 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:25:55 GMT+01:00 2026
Hostname: n23m0252.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/herman.15/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/herman.15/model_rep5.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/herman.15/model.prism"...

Type:        DTMC
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10 process11 process12 process13 process14 process15
Actions:     [step]
Variables:   x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15
Labels:      "stable"
Rewards:     "steps"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.028 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908

Transition matrix: 810 nodes (9 terminal), 14348908 minterms, vars: 15r/15c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/herman.15/model_rep5.umb"...
Model export size: 280524 Kb
Time for exporting: 16.072 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/herman.15/model_rep5.umb:	Size of output file is 287257088 bytes
Removing output file to save space for repetition #5
```

