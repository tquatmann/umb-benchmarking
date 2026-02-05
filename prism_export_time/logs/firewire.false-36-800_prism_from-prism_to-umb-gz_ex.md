# Log files for prism_from-prism_to-umb-gz_ex on model [firewire.false-36-800](../../models/firewire.false-36-800)

Parsed values: `[0.555, 0.771, 0.565, 0.653, 0.531]`



### Log file: prism_from-prism_to-umb-gz_ex_firewire.false-36-800_rep1.log

```
Command(s):
../bin/prism -ex models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/firewire.false-36-800/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2.424 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:41:33 GMT+01:00 2026
Hostname: r23m0141.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/firewire.false-36-800/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 212268 states
Reachable states exploration and model construction done in 1.076 secs.
Sorting reachable states list...

Time for model construction: 1.322 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481790
Choices:     478754
Max/avg:     3/2.26

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/firewire.false-36-800/model.umb.gz"...
Time for exporting: 0.555 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/firewire.false-36-800/model.umb.gz:	Size of output file is 12179048 bytes
```



### Log file: prism_from-prism_to-umb-gz_ex_firewire.false-36-800_rep2.log

```
Command(s):
../bin/prism -ex models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/firewire.false-36-800/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 3.166 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:27:14 GMT+01:00 2026
Hostname: r23m0204.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/firewire.false-36-800/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 212268 states
Reachable states exploration and model construction done in 1.25 secs.
Sorting reachable states list...

Time for model construction: 1.617 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481790
Choices:     478754
Max/avg:     3/2.26

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/firewire.false-36-800/model.umb_rep2.gz"...
Time for exporting: 0.771 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/firewire.false-36-800/model.umb_rep2.gz:	Size of output file is 12179048 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_ex_firewire.false-36-800_rep3.log

```
Command(s):
../bin/prism -ex models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/firewire.false-36-800/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2.475 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:32:21 GMT+01:00 2026
Hostname: n23m0200.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/firewire.false-36-800/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 212268 states
Reachable states exploration and model construction done in 1.073 secs.
Sorting reachable states list...

Time for model construction: 1.315 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481790
Choices:     478754
Max/avg:     3/2.26

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/firewire.false-36-800/model.umb_rep3.gz"...
Time for exporting: 0.565 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/firewire.false-36-800/model.umb_rep3.gz:	Size of output file is 12179048 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_ex_firewire.false-36-800_rep4.log

```
Command(s):
../bin/prism -ex models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/firewire.false-36-800/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2.775 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:08 GMT+01:00 2026
Hostname: n23m0410.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/firewire.false-36-800/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 212268 states
Reachable states exploration and model construction done in 1.213 secs.
Sorting reachable states list...

Time for model construction: 1.488 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481790
Choices:     478754
Max/avg:     3/2.26

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/firewire.false-36-800/model.umb_rep4.gz"...
Time for exporting: 0.653 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/firewire.false-36-800/model.umb_rep4.gz:	Size of output file is 12179048 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_ex_firewire.false-36-800_rep5.log

```
Command(s):
../bin/prism -ex models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/firewire.false-36-800/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2.328 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:50:16 GMT+01:00 2026
Hostname: r23m0196.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/firewire.false-36-800/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 212268 states
Reachable states exploration and model construction done in 1.016 secs.
Sorting reachable states list...

Time for model construction: 1.263 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481790
Choices:     478754
Max/avg:     3/2.26

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/firewire.false-36-800/model.umb_rep5.gz"...
Time for exporting: 0.531 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/firewire.false-36-800/model.umb_rep5.gz:	Size of output file is 12179048 bytes
Removing output file to save space for repetition #5
```

