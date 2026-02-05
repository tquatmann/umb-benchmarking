# Log files for prism_from-prism_to-tra_default on model [embedded.8-12](../../models/embedded.8-12)

Parsed values: `[1330982.0, 1330982.0, 1330982.0, 1330982.0, 1330982.0]`



### Log file: prism_from-prism_to-tra_default_embedded.8-12_rep1.log

```
Command(s):
../bin/prism  models/embedded.8-12/model.prism -exportmodel out/prism_from-prism_to-tra_default/embedded.8-12/model.tra,lab,rew:precision=17
Wallclock time: 0.816 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:40:04 GMT+01:00 2026
Hostname: r23m0138.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/embedded.8-12/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/embedded.8-12/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 21 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.036 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 1819 nodes (9 terminal), 36041 minterms, vars: 16r/16c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/embedded.8-12/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/embedded.8-12/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/embedded.8-12/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/embedded.8-12/model.trew"...
Time for exporting: 0.028 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/embedded.8-12/model.tra:	Size of output file is 1282446 bytes
out/prism_from-prism_to-tra_default/embedded.8-12/model.lab:	Size of output file is 48536 bytes
out/prism_from-prism_to-tra_default/embedded.8-12/model.srew:	File does not exist.
out/prism_from-prism_to-tra_default/embedded.8-12/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_embedded.8-12_rep2.log

```
Command(s):
../bin/prism  models/embedded.8-12/model.prism -exportmodel out/prism_from-prism_to-tra_default/embedded.8-12/model_rep2.tra,lab,rew:precision=17
Wallclock time: 0.522 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:52:46 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/embedded.8-12/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/embedded.8-12/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 21 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.015 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 1819 nodes (9 terminal), 36041 minterms, vars: 16r/16c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/embedded.8-12/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/embedded.8-12/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/embedded.8-12/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/embedded.8-12/model_rep2.trew"...
Time for exporting: 0.024 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/embedded.8-12/model_rep2.tra:	Size of output file is 1282446 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/embedded.8-12/model_rep2.lab:	Size of output file is 48536 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/embedded.8-12/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_default/embedded.8-12/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_embedded.8-12_rep3.log

```
Command(s):
../bin/prism  models/embedded.8-12/model.prism -exportmodel out/prism_from-prism_to-tra_default/embedded.8-12/model_rep3.tra,lab,rew:precision=17
Wallclock time: 0.526 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:39 GMT+01:00 2026
Hostname: n23m0169.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/embedded.8-12/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/embedded.8-12/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 21 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.015 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 1819 nodes (9 terminal), 36041 minterms, vars: 16r/16c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/embedded.8-12/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/embedded.8-12/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/embedded.8-12/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/embedded.8-12/model_rep3.trew"...
Time for exporting: 0.024 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/embedded.8-12/model_rep3.tra:	Size of output file is 1282446 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/embedded.8-12/model_rep3.lab:	Size of output file is 48536 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/embedded.8-12/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_default/embedded.8-12/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_embedded.8-12_rep4.log

```
Command(s):
../bin/prism  models/embedded.8-12/model.prism -exportmodel out/prism_from-prism_to-tra_default/embedded.8-12/model_rep4.tra,lab,rew:precision=17
Wallclock time: 0.668 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:23:23 GMT+01:00 2026
Hostname: n23m0040.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/embedded.8-12/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/embedded.8-12/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 21 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.017 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 1819 nodes (9 terminal), 36041 minterms, vars: 16r/16c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/embedded.8-12/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/embedded.8-12/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/embedded.8-12/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/embedded.8-12/model_rep4.trew"...
Time for exporting: 0.031 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/embedded.8-12/model_rep4.tra:	Size of output file is 1282446 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/embedded.8-12/model_rep4.lab:	Size of output file is 48536 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/embedded.8-12/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_default/embedded.8-12/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_embedded.8-12_rep5.log

```
Command(s):
../bin/prism  models/embedded.8-12/model.prism -exportmodel out/prism_from-prism_to-tra_default/embedded.8-12/model_rep5.tra,lab,rew:precision=17
Wallclock time: 0.517 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:26:08 GMT+01:00 2026
Hostname: n23m0058.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/embedded.8-12/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/embedded.8-12/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 21 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.015 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 1819 nodes (9 terminal), 36041 minterms, vars: 16r/16c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/embedded.8-12/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/embedded.8-12/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/embedded.8-12/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/embedded.8-12/model_rep5.trew"...
Time for exporting: 0.024 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/embedded.8-12/model_rep5.tra:	Size of output file is 1282446 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/embedded.8-12/model_rep5.lab:	Size of output file is 48536 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/embedded.8-12/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_default/embedded.8-12/model_rep5.trew:	File does not exist.
```

