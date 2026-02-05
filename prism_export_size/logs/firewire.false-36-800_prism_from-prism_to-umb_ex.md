# Log files for prism_from-prism_to-umb_ex on model [firewire.false-36-800](../../models/firewire.false-36-800)

Parsed values: `[19044864.0, 19044864.0, 19044864.0, 19044864.0, 19044864.0]`



### Log file: prism_from-prism_to-umb_ex_firewire.false-36-800_rep1.log

```
Command(s):
../bin/prism -ex models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb_ex/firewire.false-36-800/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2.055 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:38:54 GMT+01:00 2026
Hostname: r23m0077.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/firewire.false-36-800/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 212268 states
Reachable states exploration and model construction done in 1.024 secs.
Sorting reachable states list...

Time for model construction: 1.269 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481790
Choices:     478754
Max/avg:     3/2.26

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/firewire.false-36-800/model.umb"...
Model export size: 18598 Kb
Time for exporting: 0.274 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/firewire.false-36-800/model.umb:	Size of output file is 19044864 bytes
```



### Log file: prism_from-prism_to-umb_ex_firewire.false-36-800_rep2.log

```
Command(s):
../bin/prism -ex models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb_ex/firewire.false-36-800/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 9.265 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:50:22 GMT+01:00 2026
Hostname: r23m0217.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/firewire.false-36-800/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 122144 212268 states
Reachable states exploration and model construction done in 4.635 secs.
Sorting reachable states list...

Time for model construction: 5.739 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481790
Choices:     478754
Max/avg:     3/2.26

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/firewire.false-36-800/model_rep2.umb"...
Model export size: 18598 Kb
Time for exporting: 1.295 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/firewire.false-36-800/model_rep2.umb:	Size of output file is 19044864 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_ex_firewire.false-36-800_rep3.log

```
Command(s):
../bin/prism -ex models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb_ex/firewire.false-36-800/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2.645 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:00:53 GMT+01:00 2026
Hostname: n23m0041.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/firewire.false-36-800/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 212268 states
Reachable states exploration and model construction done in 1.278 secs.
Sorting reachable states list...

Time for model construction: 1.597 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481790
Choices:     478754
Max/avg:     3/2.26

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/firewire.false-36-800/model_rep3.umb"...
Model export size: 18598 Kb
Time for exporting: 0.354 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/firewire.false-36-800/model_rep3.umb:	Size of output file is 19044864 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_ex_firewire.false-36-800_rep4.log

```
Command(s):
../bin/prism -ex models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb_ex/firewire.false-36-800/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2.067 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:29:30 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/firewire.false-36-800/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 212268 states
Reachable states exploration and model construction done in 1.027 secs.
Sorting reachable states list...

Time for model construction: 1.278 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481790
Choices:     478754
Max/avg:     3/2.26

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/firewire.false-36-800/model_rep4.umb"...
Model export size: 18598 Kb
Time for exporting: 0.275 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/firewire.false-36-800/model_rep4.umb:	Size of output file is 19044864 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_ex_firewire.false-36-800_rep5.log

```
Command(s):
../bin/prism -ex models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb_ex/firewire.false-36-800/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2.108 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:39:36 GMT+01:00 2026
Hostname: n23m0041.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/firewire.false-36-800/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 212268 states
Reachable states exploration and model construction done in 1.037 secs.
Sorting reachable states list...

Time for model construction: 1.283 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481790
Choices:     478754
Max/avg:     3/2.26

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/firewire.false-36-800/model_rep5.umb"...
Model export size: 18598 Kb
Time for exporting: 0.276 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/firewire.false-36-800/model_rep5.umb:	Size of output file is 19044864 bytes
Removing output file to save space for repetition #5
```

