# Log files

Tool configuration: prism_from-prism_to-tra_default
Benchmark: [haddad-monmege.100-0.7](../../models/haddad-monmege.100-0.7)
Parsed values: [4551.0, 4551.0, 4551.0, 4551.0, 4551.0]



### Log file: prism_from-prism_to-tra_default_haddad-monmege.100-0.7_rep1.log

```
Command(s):
../bin/prism  models/haddad-monmege.100-0.7/model.prism -exportmodel out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model.tra,lab,rew:precision=17
Wallclock time: 0.520 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:38:54 GMT+01:00 2026
Hostname: r23m0141.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/haddad-monmege.100-0.7/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/haddad-monmege.100-0.7/model.prism"...

Type:        DTMC
Modules:     main
Actions:     []
Variables:   x
Labels:      "Target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 101 iterations in 0.01 seconds (average 0.000099, setup 0.00)

Time for model construction: 0.016 seconds.

Type:        DTMC
States:      201 (1 initial)
Transitions: 400

Transition matrix: 131 nodes (5 terminal), 400 minterms, vars: 8r/8c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model.trew"...
Time for exporting: 0.008 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model.tra:	Size of output file is 4506 bytes
out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model.lab:	Size of output file is 45 bytes
out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model.srew:	File does not exist.
out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_haddad-monmege.100-0.7_rep2.log

```
Command(s):
../bin/prism  models/haddad-monmege.100-0.7/model.prism -exportmodel out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep2.tra,lab,rew:precision=17
Wallclock time: 0.664 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:33:03 GMT+01:00 2026
Hostname: n23m0250.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/haddad-monmege.100-0.7/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/haddad-monmege.100-0.7/model.prism"...

Type:        DTMC
Modules:     main
Actions:     []
Variables:   x
Labels:      "Target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 101 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.018 seconds.

Type:        DTMC
States:      201 (1 initial)
Transitions: 400

Transition matrix: 131 nodes (5 terminal), 400 minterms, vars: 8r/8c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep2.trew"...
Time for exporting: 0.006 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep2.tra:	Size of output file is 4506 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep2.lab:	Size of output file is 45 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_haddad-monmege.100-0.7_rep3.log

```
Command(s):
../bin/prism  models/haddad-monmege.100-0.7/model.prism -exportmodel out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep3.tra,lab,rew:precision=17
Wallclock time: 0.916 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:16 GMT+01:00 2026
Hostname: n23m0242.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/haddad-monmege.100-0.7/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/haddad-monmege.100-0.7/model.prism"...

Type:        DTMC
Modules:     main
Actions:     []
Variables:   x
Labels:      "Target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 101 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.04 seconds.

Type:        DTMC
States:      201 (1 initial)
Transitions: 400

Transition matrix: 131 nodes (5 terminal), 400 minterms, vars: 8r/8c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep3.trew"...
Time for exporting: 0.013 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep3.tra:	Size of output file is 4506 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep3.lab:	Size of output file is 45 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_haddad-monmege.100-0.7_rep4.log

```
Command(s):
../bin/prism  models/haddad-monmege.100-0.7/model.prism -exportmodel out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep4.tra,lab,rew:precision=17
Wallclock time: 0.643 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:24 GMT+01:00 2026
Hostname: n23m0166.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/haddad-monmege.100-0.7/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/haddad-monmege.100-0.7/model.prism"...

Type:        DTMC
Modules:     main
Actions:     []
Variables:   x
Labels:      "Target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 101 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.02 seconds.

Type:        DTMC
States:      201 (1 initial)
Transitions: 400

Transition matrix: 131 nodes (5 terminal), 400 minterms, vars: 8r/8c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep4.trew"...
Time for exporting: 0.01 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep4.tra:	Size of output file is 4506 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep4.lab:	Size of output file is 45 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_haddad-monmege.100-0.7_rep5.log

```
Command(s):
../bin/prism  models/haddad-monmege.100-0.7/model.prism -exportmodel out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep5.tra,lab,rew:precision=17
Wallclock time: 0.511 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:47:42 GMT+01:00 2026
Hostname: n23m0247.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/haddad-monmege.100-0.7/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/haddad-monmege.100-0.7/model.prism"...

Type:        DTMC
Modules:     main
Actions:     []
Variables:   x
Labels:      "Target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 101 iterations in 0.01 seconds (average 0.000099, setup 0.00)

Time for model construction: 0.016 seconds.

Type:        DTMC
States:      201 (1 initial)
Transitions: 400

Transition matrix: 131 nodes (5 terminal), 400 minterms, vars: 8r/8c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep5.trew"...
Time for exporting: 0.007 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep5.tra:	Size of output file is 4506 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep5.lab:	Size of output file is 45 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_default/haddad-monmege.100-0.7/model_rep5.trew:	File does not exist.
```

