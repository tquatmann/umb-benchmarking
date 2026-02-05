# Log files for prism_from-prism_to-umb_default on model [wlan.5-0](../../models/wlan.5-0)

Parsed values: `[77327360.0, 77327360.0, 77327360.0, 77327360.0, 77327360.0]`



### Log file: prism_from-prism_to-umb_default_wlan.5-0_rep1.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-umb_default/wlan.5-0/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 7.765 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:40:29 GMT+01:00 2026
Hostname: r23m0047.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/wlan.5-0/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.19 seconds (average 0.001118, setup 0.00)

Time for model construction: 0.236 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/wlan.5-0/model.umb"...
Model export size: 75515 Kb
Time for exporting: 6.997 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/wlan.5-0/model.umb:	Size of output file is 77327360 bytes
```



### Log file: prism_from-prism_to-umb_default_wlan.5-0_rep2.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-umb_default/wlan.5-0/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 8.969 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:00:53 GMT+01:00 2026
Hostname: n23m0042.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/wlan.5-0/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.21 seconds (average 0.001235, setup 0.00)

Time for model construction: 0.266 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/wlan.5-0/model_rep2.umb"...
Model export size: 75515 Kb
Time for exporting: 8.142 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/wlan.5-0/model_rep2.umb:	Size of output file is 77327360 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_default_wlan.5-0_rep3.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-umb_default/wlan.5-0/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 9.085 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:23 GMT+01:00 2026
Hostname: n23m0205.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/wlan.5-0/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.20 seconds (average 0.001176, setup 0.00)

Time for model construction: 0.267 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/wlan.5-0/model_rep3.umb"...
Model export size: 75515 Kb
Time for exporting: 7.053 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/wlan.5-0/model_rep3.umb:	Size of output file is 77327360 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_default_wlan.5-0_rep4.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-umb_default/wlan.5-0/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 9.371 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:25 GMT+01:00 2026
Hostname: n23m0375.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/wlan.5-0/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.24 seconds (average 0.001412, setup 0.00)

Time for model construction: 0.33 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/wlan.5-0/model_rep4.umb"...
Model export size: 75515 Kb
Time for exporting: 8.179 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/wlan.5-0/model_rep4.umb:	Size of output file is 77327360 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_default_wlan.5-0_rep5.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-umb_default/wlan.5-0/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 10.090 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:27 GMT+01:00 2026
Hostname: r23m0005.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/wlan.5-0/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.22 seconds (average 0.001294, setup 0.00)

Time for model construction: 0.306 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/wlan.5-0/model_rep5.umb"...
Model export size: 75515 Kb
Time for exporting: 8.58 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/wlan.5-0/model_rep5.umb:	Size of output file is 77327360 bytes
Removing output file to save space for repetition #5
```

