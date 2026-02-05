# Log files for prism_from-prism_to-tra_default on model [wlan.5-0](../../models/wlan.5-0)

Parsed values: `[61393481.0, 61393481.0, 61393481.0, 61393481.0, 61393481.0]`



### Log file: prism_from-prism_to-tra_default_wlan.5-0_rep1.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-tra_default/wlan.5-0/model.tra,lab,rew:precision=17
Wallclock time: 3.030 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:24:52 GMT+01:00 2026
Hostname: n23m0110.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/wlan.5-0/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.23 seconds (average 0.001353, setup 0.00)

Time for model construction: 0.273 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/wlan.5-0/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/wlan.5-0/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/wlan.5-0/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/wlan.5-0/model.trew"...
Time for exporting: 2.2 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/wlan.5-0/model.tra:	Size of output file is 61393433 bytes
out/prism_from-prism_to-tra_default/wlan.5-0/model.lab:	Size of output file is 48 bytes
out/prism_from-prism_to-tra_default/wlan.5-0/model.srew:	File does not exist.
out/prism_from-prism_to-tra_default/wlan.5-0/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_wlan.5-0_rep2.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-tra_default/wlan.5-0/model_rep2.tra,lab,rew:precision=17
Wallclock time: 3.620 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:00 GMT+01:00 2026
Hostname: n23m0343.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/wlan.5-0/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.26 seconds (average 0.001529, setup 0.00)

Time for model construction: 0.313 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/wlan.5-0/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/wlan.5-0/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/wlan.5-0/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/wlan.5-0/model_rep2.trew"...
Time for exporting: 2.611 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/wlan.5-0/model_rep2.tra:	Size of output file is 61393433 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/wlan.5-0/model_rep2.lab:	Size of output file is 48 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/wlan.5-0/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_default/wlan.5-0/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_wlan.5-0_rep3.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-tra_default/wlan.5-0/model_rep3.tra,lab,rew:precision=17
Wallclock time: 2.971 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:53:17 GMT+01:00 2026
Hostname: n23m0379.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/wlan.5-0/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.20 seconds (average 0.001176, setup 0.00)

Time for model construction: 0.256 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/wlan.5-0/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/wlan.5-0/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/wlan.5-0/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/wlan.5-0/model_rep3.trew"...
Time for exporting: 2.185 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/wlan.5-0/model_rep3.tra:	Size of output file is 61393433 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/wlan.5-0/model_rep3.lab:	Size of output file is 48 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/wlan.5-0/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_default/wlan.5-0/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_wlan.5-0_rep4.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-tra_default/wlan.5-0/model_rep4.tra,lab,rew:precision=17
Wallclock time: 3.708 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:20 GMT+01:00 2026
Hostname: n23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/wlan.5-0/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.26 seconds (average 0.001529, setup 0.00)

Time for model construction: 0.332 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/wlan.5-0/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/wlan.5-0/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/wlan.5-0/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/wlan.5-0/model_rep4.trew"...
Time for exporting: 2.612 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/wlan.5-0/model_rep4.tra:	Size of output file is 61393433 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/wlan.5-0/model_rep4.lab:	Size of output file is 48 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/wlan.5-0/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_default/wlan.5-0/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_wlan.5-0_rep5.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-tra_default/wlan.5-0/model_rep5.tra,lab,rew:precision=17
Wallclock time: 3.648 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:14:00 GMT+01:00 2026
Hostname: n23m0096.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/wlan.5-0/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.29 seconds (average 0.001706, setup 0.00)

Time for model construction: 0.375 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/wlan.5-0/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/wlan.5-0/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/wlan.5-0/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/wlan.5-0/model_rep5.trew"...
Time for exporting: 2.573 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/wlan.5-0/model_rep5.tra:	Size of output file is 61393433 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/wlan.5-0/model_rep5.lab:	Size of output file is 48 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/wlan.5-0/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_default/wlan.5-0/model_rep5.trew:	File does not exist.
```

