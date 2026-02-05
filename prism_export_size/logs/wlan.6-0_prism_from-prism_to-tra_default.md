# Log files

Tool configuration: prism_from-prism_to-tra_default
Benchmark: [wlan.6-0](../../models/wlan.6-0)
Parsed values: [255342682.0, 255342682.0, 255342682.0, 255342682.0, 255342682.0]



### Log file: prism_from-prism_to-tra_default_wlan.6-0_rep1.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-tra_default/wlan.6-0/model.tra,lab,rew:precision=17
Wallclock time: 11.064 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:40:29 GMT+01:00 2026
Hostname: n23m0380.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/wlan.6-0/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.44 seconds (average 0.002256, setup 0.00)

Time for model construction: 0.502 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/wlan.6-0/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/wlan.6-0/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/wlan.6-0/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/wlan.6-0/model.trew"...
Time for exporting: 9.709 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/wlan.6-0/model.tra:	Size of output file is 255342633 bytes
out/prism_from-prism_to-tra_default/wlan.6-0/model.lab:	Size of output file is 49 bytes
out/prism_from-prism_to-tra_default/wlan.6-0/model.srew:	File does not exist.
out/prism_from-prism_to-tra_default/wlan.6-0/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_wlan.6-0_rep2.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-tra_default/wlan.6-0/model_rep2.tra,lab,rew:precision=17
Wallclock time: 9.379 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:23:42 GMT+01:00 2026
Hostname: n23m0249.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/wlan.6-0/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.28 seconds (average 0.001436, setup 0.00)

Time for model construction: 0.335 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/wlan.6-0/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/wlan.6-0/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/wlan.6-0/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/wlan.6-0/model_rep2.trew"...
Time for exporting: 8.432 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/wlan.6-0/model_rep2.tra:	Size of output file is 255342633 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/wlan.6-0/model_rep2.lab:	Size of output file is 49 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/wlan.6-0/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_default/wlan.6-0/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_wlan.6-0_rep3.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-tra_default/wlan.6-0/model_rep3.tra,lab,rew:precision=17
Wallclock time: 9.141 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:30:00 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/wlan.6-0/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.28 seconds (average 0.001436, setup 0.00)

Time for model construction: 0.322 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/wlan.6-0/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/wlan.6-0/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/wlan.6-0/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/wlan.6-0/model_rep3.trew"...
Time for exporting: 8.291 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/wlan.6-0/model_rep3.tra:	Size of output file is 255342633 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/wlan.6-0/model_rep3.lab:	Size of output file is 49 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/wlan.6-0/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_default/wlan.6-0/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_wlan.6-0_rep4.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-tra_default/wlan.6-0/model_rep4.tra,lab,rew:precision=17
Wallclock time: 11.236 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:40 GMT+01:00 2026
Hostname: n23m0220.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/wlan.6-0/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.33 seconds (average 0.001692, setup 0.00)

Time for model construction: 0.419 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/wlan.6-0/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/wlan.6-0/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/wlan.6-0/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/wlan.6-0/model_rep4.trew"...
Time for exporting: 9.807 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/wlan.6-0/model_rep4.tra:	Size of output file is 255342633 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/wlan.6-0/model_rep4.lab:	Size of output file is 49 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/wlan.6-0/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_default/wlan.6-0/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_wlan.6-0_rep5.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-tra_default/wlan.6-0/model_rep5.tra,lab,rew:precision=17
Wallclock time: 9.830 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:23:53 GMT+01:00 2026
Hostname: n23m0341.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/wlan.6-0/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.30 seconds (average 0.001538, setup 0.00)

Time for model construction: 0.352 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/wlan.6-0/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/wlan.6-0/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/wlan.6-0/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/wlan.6-0/model_rep5.trew"...
Time for exporting: 8.82 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/wlan.6-0/model_rep5.tra:	Size of output file is 255342633 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/wlan.6-0/model_rep5.lab:	Size of output file is 49 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/wlan.6-0/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_default/wlan.6-0/model_rep5.trew:	File does not exist.
```

