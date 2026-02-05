# Log files

Tool configuration: prism_from-prism_to-umb_ex
Benchmark: [wlan.4-0](../../models/wlan.4-0)
Parsed values: [20335616.0, 20335616.0, 20335616.0, 20335616.0, 20335616.0]



### Log file: prism_from-prism_to-umb_ex_wlan.4-0_rep1.log

```
Command(s):
../bin/prism -ex models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-umb_ex/wlan.4-0/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2.635 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:36:44 GMT+01:00 2026
Hostname: n23m0241.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/wlan.4-0/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 345000 states
Reachable states exploration and model construction done in 1.448 secs.
Sorting reachable states list...

Time for model construction: 1.755 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/wlan.4-0/model.umb"...
Model export size: 19859 Kb
Time for exporting: 0.245 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/wlan.4-0/model.umb:	Size of output file is 20335616 bytes
```



### Log file: prism_from-prism_to-umb_ex_wlan.4-0_rep2.log

```
Command(s):
../bin/prism -ex models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-umb_ex/wlan.4-0/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2.532 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:38:36 GMT+01:00 2026
Hostname: n23m0244.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/wlan.4-0/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 345000 states
Reachable states exploration and model construction done in 1.345 secs.
Sorting reachable states list...

Time for model construction: 1.614 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/wlan.4-0/model_rep2.umb"...
Model export size: 19859 Kb
Time for exporting: 0.341 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/wlan.4-0/model_rep2.umb:	Size of output file is 20335616 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_ex_wlan.4-0_rep3.log

```
Command(s):
../bin/prism -ex models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-umb_ex/wlan.4-0/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 3.652 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:58:53 GMT+01:00 2026
Hostname: n23m0036.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/wlan.4-0/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 345000 states
Reachable states exploration and model construction done in 1.607 secs.
Sorting reachable states list...

Time for model construction: 1.983 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/wlan.4-0/model_rep3.umb"...
Model export size: 19859 Kb
Time for exporting: 0.386 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/wlan.4-0/model_rep3.umb:	Size of output file is 20335616 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_ex_wlan.4-0_rep4.log

```
Command(s):
../bin/prism -ex models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-umb_ex/wlan.4-0/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 3.307 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:55 GMT+01:00 2026
Hostname: n23m0211.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/wlan.4-0/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 345000 states
Reachable states exploration and model construction done in 1.247 secs.
Sorting reachable states list...

Time for model construction: 1.567 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/wlan.4-0/model_rep4.umb"...
Model export size: 19859 Kb
Time for exporting: 0.348 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/wlan.4-0/model_rep4.umb:	Size of output file is 20335616 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_ex_wlan.4-0_rep5.log

```
Command(s):
../bin/prism -ex models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-umb_ex/wlan.4-0/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2.241 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:26:44 GMT+01:00 2026
Hostname: n23m0380.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/wlan.4-0/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 345000 states
Reachable states exploration and model construction done in 1.289 secs.
Sorting reachable states list...

Time for model construction: 1.508 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/wlan.4-0/model_rep5.umb"...
Model export size: 19859 Kb
Time for exporting: 0.211 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/wlan.4-0/model_rep5.umb:	Size of output file is 20335616 bytes
Removing output file to save space for repetition #5
```

