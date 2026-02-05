# Log files

Tool configuration: prism_from-prism_to-tra_ex
Benchmark: [wlan.4-0](../../models/wlan.4-0)
Parsed values: [0.813, 0.907, 0.834, 1.035, 0.788]



### Log file: prism_from-prism_to-tra_ex_wlan.4-0_rep1.log

```
Command(s):
../bin/prism -ex models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-tra_ex/wlan.4-0/model.tra,lab,rew:precision=17
Wallclock time: 2.916 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:28:33 GMT+01:00 2026
Hostname: n23m0128.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/wlan.4-0/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 345000 states
Reachable states exploration and model construction done in 1.287 secs.
Sorting reachable states list...

Time for model construction: 1.521 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.4-0/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.4-0/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.4-0/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.4-0/model.trew"...
Time for exporting: 0.813 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/wlan.4-0/model.tra:	Size of output file is 15199275 bytes
out/prism_from-prism_to-tra_ex/wlan.4-0/model.lab:	Size of output file is 48 bytes
out/prism_from-prism_to-tra_ex/wlan.4-0/model.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/wlan.4-0/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_wlan.4-0_rep2.log

```
Command(s):
../bin/prism -ex models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep2.tra,lab,rew:precision=17
Wallclock time: 3.120 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:49 GMT+01:00 2026
Hostname: n23m0200.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 345000 states
Reachable states exploration and model construction done in 1.338 secs.
Sorting reachable states list...

Time for model construction: 1.616 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep2.trew"...
Time for exporting: 0.907 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep2.tra:	Size of output file is 15199275 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep2.lab:	Size of output file is 48 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_wlan.4-0_rep3.log

```
Command(s):
../bin/prism -ex models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep3.tra,lab,rew:precision=17
Wallclock time: 3.180 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:01:24 GMT+01:00 2026
Hostname: n23m0112.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 345000 states
Reachable states exploration and model construction done in 1.334 secs.
Sorting reachable states list...

Time for model construction: 1.73 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep3.trew"...
Time for exporting: 0.834 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep3.tra:	Size of output file is 15199275 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep3.lab:	Size of output file is 48 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_wlan.4-0_rep4.log

```
Command(s):
../bin/prism -ex models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep4.tra,lab,rew:precision=17
Wallclock time: 3.664 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:26 GMT+01:00 2026
Hostname: n23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 345000 states
Reachable states exploration and model construction done in 1.519 secs.
Sorting reachable states list...

Time for model construction: 1.835 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep4.trew"...
Time for exporting: 1.035 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep4.tra:	Size of output file is 15199275 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep4.lab:	Size of output file is 48 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_wlan.4-0_rep5.log

```
Command(s):
../bin/prism -ex models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep5.tra,lab,rew:precision=17
Wallclock time: 2.786 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:25:24 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 345000 states
Reachable states exploration and model construction done in 1.202 secs.
Sorting reachable states list...

Time for model construction: 1.461 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep5.trew"...
Time for exporting: 0.788 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep5.tra:	Size of output file is 15199275 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep5.lab:	Size of output file is 48 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/wlan.4-0/model_rep5.trew:	File does not exist.
```

