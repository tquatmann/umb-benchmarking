# Log files for prism_from-prism_to-umb_ex on model [wlan.5-0](../../models/wlan.5-0)

Parsed values: `[0.454, 0.483, 0.52, 0.435, 0.597]`



### Log file: prism_from-prism_to-umb_ex_wlan.5-0_rep1.log

```
Command(s):
../bin/prism -ex models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-umb_ex/wlan.5-0/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 6.839 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:43:08 GMT+01:00 2026
Hostname: r23m0061.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/wlan.5-0/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 675148 1295218 states
Reachable states exploration and model construction done in 5.016 secs.
Sorting reachable states list...

Time for model construction: 5.738 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960
Choices:     1646074
Max/avg:     3/1.27

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/wlan.5-0/model.umb"...
Model export size: 75515 Kb
Time for exporting: 0.454 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/wlan.5-0/model.umb:	Size of output file is 77327360 bytes
```



### Log file: prism_from-prism_to-umb_ex_wlan.5-0_rep2.log

```
Command(s):
../bin/prism -ex models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-umb_ex/wlan.5-0/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 6.714 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:06 GMT+01:00 2026
Hostname: n23m0202.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/wlan.5-0/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 676196 1295218 states
Reachable states exploration and model construction done in 5.012 secs.
Sorting reachable states list...

Time for model construction: 5.683 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960
Choices:     1646074
Max/avg:     3/1.27

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/wlan.5-0/model_rep2.umb"...
Model export size: 75515 Kb
Time for exporting: 0.483 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/wlan.5-0/model_rep2.umb:	Size of output file is 77327360 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_ex_wlan.5-0_rep3.log

```
Command(s):
../bin/prism -ex models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-umb_ex/wlan.5-0/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 6.810 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:54:48 GMT+01:00 2026
Hostname: n23m0308.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/wlan.5-0/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 676150 1295218 states
Reachable states exploration and model construction done in 5.046 secs.
Sorting reachable states list...

Time for model construction: 5.687 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960
Choices:     1646074
Max/avg:     3/1.27

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/wlan.5-0/model_rep3.umb"...
Model export size: 75515 Kb
Time for exporting: 0.52 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/wlan.5-0/model_rep3.umb:	Size of output file is 77327360 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_ex_wlan.5-0_rep4.log

```
Command(s):
../bin/prism -ex models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-umb_ex/wlan.5-0/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 6.749 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:27:59 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/wlan.5-0/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 673761 1295218 states
Reachable states exploration and model construction done in 5.077 secs.
Sorting reachable states list...

Time for model construction: 5.744 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960
Choices:     1646074
Max/avg:     3/1.27

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/wlan.5-0/model_rep4.umb"...
Model export size: 75515 Kb
Time for exporting: 0.435 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/wlan.5-0/model_rep4.umb:	Size of output file is 77327360 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_ex_wlan.5-0_rep5.log

```
Command(s):
../bin/prism -ex models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-umb_ex/wlan.5-0/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 7.832 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:59:22 GMT+01:00 2026
Hostname: n23m0041.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/wlan.5-0/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 607727 1295218 states
Reachable states exploration and model construction done in 5.684 secs.
Sorting reachable states list...

Time for model construction: 6.513 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960
Choices:     1646074
Max/avg:     3/1.27

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/wlan.5-0/model_rep5.umb"...
Model export size: 75515 Kb
Time for exporting: 0.597 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/wlan.5-0/model_rep5.umb:	Size of output file is 77327360 bytes
Removing output file to save space for repetition #5
```

