# Log files

Tool configuration: prism_from-prism_to-tra_ex
Benchmark: [wlan.5-0](../../models/wlan.5-0)
Parsed values: [61393481.0, 61393481.0, 61393481.0, 61393481.0, 61393481.0]



### Log file: prism_from-prism_to-tra_ex_wlan.5-0_rep1.log

```
Command(s):
../bin/prism -ex models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-tra_ex/wlan.5-0/model.tra,lab,rew:precision=17
Wallclock time: 9.232 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:28:32 GMT+01:00 2026
Hostname: n23m0096.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/wlan.5-0/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 672760 1295218 states
Reachable states exploration and model construction done in 5.174 secs.
Sorting reachable states list...

Time for model construction: 5.84 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960
Choices:     1646074
Max/avg:     3/1.27

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.5-0/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.5-0/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.5-0/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.5-0/model.trew"...
Time for exporting: 2.808 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/wlan.5-0/model.tra:	Size of output file is 61393433 bytes
out/prism_from-prism_to-tra_ex/wlan.5-0/model.lab:	Size of output file is 48 bytes
out/prism_from-prism_to-tra_ex/wlan.5-0/model.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/wlan.5-0/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_wlan.5-0_rep2.log

```
Command(s):
../bin/prism -ex models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep2.tra,lab,rew:precision=17
Wallclock time: 8.891 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:40 GMT+01:00 2026
Hostname: n23m0138.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 676210 1295218 states
Reachable states exploration and model construction done in 5.001 secs.
Sorting reachable states list...

Time for model construction: 5.715 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960
Choices:     1646074
Max/avg:     3/1.27

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep2.trew"...
Time for exporting: 2.591 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep2.tra:	Size of output file is 61393433 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep2.lab:	Size of output file is 48 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_wlan.5-0_rep3.log

```
Command(s):
../bin/prism -ex models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep3.tra,lab,rew:precision=17
Wallclock time: 10.969 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:56:52 GMT+01:00 2026
Hostname: n23m0144.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 587361 1295218 states
Reachable states exploration and model construction done in 5.804 secs.
Sorting reachable states list...

Time for model construction: 6.621 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960
Choices:     1646074
Max/avg:     3/1.27

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep3.trew"...
Time for exporting: 3.242 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep3.tra:	Size of output file is 61393433 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep3.lab:	Size of output file is 48 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_wlan.5-0_rep4.log

```
Command(s):
../bin/prism -ex models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep4.tra,lab,rew:precision=17
Wallclock time: 10.178 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:12 GMT+01:00 2026
Hostname: n23m0079.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 611513 1295218 states
Reachable states exploration and model construction done in 5.638 secs.
Sorting reachable states list...

Time for model construction: 6.38 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960
Choices:     1646074
Max/avg:     3/1.27

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep4.trew"...
Time for exporting: 3.106 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep4.tra:	Size of output file is 61393433 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep4.lab:	Size of output file is 48 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_wlan.5-0_rep5.log

```
Command(s):
../bin/prism -ex models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep5.tra,lab,rew:precision=17
Wallclock time: 8.999 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:41:07 GMT+01:00 2026
Hostname: n23m0341.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 672770 1295218 states
Reachable states exploration and model construction done in 5.075 secs.
Sorting reachable states list...

Time for model construction: 5.813 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960
Choices:     1646074
Max/avg:     3/1.27

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep5.trew"...
Time for exporting: 2.611 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep5.tra:	Size of output file is 61393433 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep5.lab:	Size of output file is 48 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/wlan.5-0/model_rep5.trew:	File does not exist.
```

