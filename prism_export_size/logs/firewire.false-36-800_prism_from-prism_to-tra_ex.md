# Log files

Tool configuration: prism_from-prism_to-tra_ex
Benchmark: [firewire.false-36-800](../../models/firewire.false-36-800)
Parsed values: [15698419.0, 15698419.0, 15698419.0, 15698419.0, 15698419.0]



### Log file: prism_from-prism_to-tra_ex_firewire.false-36-800_rep1.log

```
Command(s):
../bin/prism -ex models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-tra_ex/firewire.false-36-800/model.tra,lab,rew:precision=17
Wallclock time: 606.295 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:45:15 GMT+01:00 2026
Hostname: r23m0141.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/firewire.false-36-800/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 212268 states
Reachable states exploration and model construction done in 1.048 secs.
Sorting reachable states list...

Time for model construction: 1.303 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481790
Choices:     478754
Max/avg:     3/2.26

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/firewire.false-36-800/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/firewire.false-36-800/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/firewire.false-36-800/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/firewire.false-36-800/model.trew"...
Time for exporting: 604.425 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/firewire.false-36-800/model.tra:	Size of output file is 12179048 bytes
out/prism_from-prism_to-tra_ex/firewire.false-36-800/model.lab:	Size of output file is 52 bytes
out/prism_from-prism_to-tra_ex/firewire.false-36-800/model.srew:	Size of output file is 51 bytes
out/prism_from-prism_to-tra_ex/firewire.false-36-800/model.trew:	Size of output file is 3519268 bytes
```



### Log file: prism_from-prism_to-tra_ex_firewire.false-36-800_rep2.log

```
Command(s):
../bin/prism -ex models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep2.tra,lab,rew:precision=17
Wallclock time: 596.053 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:56:20 GMT+01:00 2026
Hostname: r23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 212268 states
Reachable states exploration and model construction done in 1.038 secs.
Sorting reachable states list...

Time for model construction: 1.298 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481790
Choices:     478754
Max/avg:     3/2.26

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep2.trew"...
Time for exporting: 594.183 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep2.tra:	Size of output file is 12179048 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep2.lab:	Size of output file is 52 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep2.srew:	Size of output file is 51 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep2.trew:	Size of output file is 3519268 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_ex_firewire.false-36-800_rep3.log

```
Command(s):
../bin/prism -ex models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep3.tra,lab,rew:precision=17
Wallclock time: 662.431 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:33:03 GMT+01:00 2026
Hostname: n23m0252.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 212268 states
Reachable states exploration and model construction done in 1.198 secs.
Sorting reachable states list...

Time for model construction: 1.454 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481790
Choices:     478754
Max/avg:     3/2.26

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep3.trew"...
Time for exporting: 660.266 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep3.tra:	Size of output file is 12179048 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep3.lab:	Size of output file is 52 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep3.srew:	Size of output file is 51 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep3.trew:	Size of output file is 3519268 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_ex_firewire.false-36-800_rep4.log

```
Command(s):
../bin/prism -ex models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep4.tra,lab,rew:precision=17
Wallclock time: 617.996 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:51:16 GMT+01:00 2026
Hostname: n23m0055.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 212268 states
Reachable states exploration and model construction done in 1.072 secs.
Sorting reachable states list...

Time for model construction: 1.35 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481790
Choices:     478754
Max/avg:     3/2.26

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep4.trew"...
Time for exporting: 616.066 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep4.tra:	Size of output file is 12179048 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep4.lab:	Size of output file is 52 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep4.srew:	Size of output file is 51 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep4.trew:	Size of output file is 3519268 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_ex_firewire.false-36-800_rep5.log

```
Command(s):
../bin/prism -ex models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep5.tra,lab,rew:precision=17
Wallclock time: 657.530 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:51:16 GMT+01:00 2026
Hostname: n23m0099.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 212268 states
Reachable states exploration and model construction done in 1.177 secs.
Sorting reachable states list...

Time for model construction: 1.431 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481790
Choices:     478754
Max/avg:     3/2.26

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep5.trew"...
Time for exporting: 655.482 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep5.tra:	Size of output file is 12179048 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep5.lab:	Size of output file is 52 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep5.srew:	Size of output file is 51 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_ex/firewire.false-36-800/model_rep5.trew:	Size of output file is 3519268 bytes
Removing output file to save space for repetition #5
```

