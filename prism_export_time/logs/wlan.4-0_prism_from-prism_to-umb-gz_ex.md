# Log files for prism_from-prism_to-umb-gz_ex on model [wlan.4-0](../../models/wlan.4-0)

Parsed values: `[1.204, 1.218, 0.995, 0.959, 0.93]`



### Log file: prism_from-prism_to-umb-gz_ex_wlan.4-0_rep1.log

```
Command(s):
../bin/prism -ex models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/wlan.4-0/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 5.331 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:34:38 GMT+01:00 2026
Hostname: r23m0005.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/wlan.4-0/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 345000 states
Reachable states exploration and model construction done in 1.544 secs.
Sorting reachable states list...

Time for model construction: 2.066 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/wlan.4-0/model.umb.gz"...
Time for exporting: 1.204 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/wlan.4-0/model.umb.gz:	Size of output file is 15199275 bytes
```



### Log file: prism_from-prism_to-umb-gz_ex_wlan.4-0_rep2.log

```
Command(s):
../bin/prism -ex models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/wlan.4-0/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 3.939 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:38 GMT+01:00 2026
Hostname: r23m0047.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/wlan.4-0/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 345000 states
Reachable states exploration and model construction done in 1.563 secs.
Sorting reachable states list...

Time for model construction: 1.906 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/wlan.4-0/model.umb_rep2.gz"...
Time for exporting: 1.218 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/wlan.4-0/model.umb_rep2.gz:	Size of output file is 15199275 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_ex_wlan.4-0_rep3.log

```
Command(s):
../bin/prism -ex models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/wlan.4-0/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 3.880 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:37 GMT+01:00 2026
Hostname: n23m0003.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/wlan.4-0/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 345000 states
Reachable states exploration and model construction done in 1.572 secs.
Sorting reachable states list...

Time for model construction: 1.947 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/wlan.4-0/model.umb_rep3.gz"...
Time for exporting: 0.995 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/wlan.4-0/model.umb_rep3.gz:	Size of output file is 15199275 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_ex_wlan.4-0_rep4.log

```
Command(s):
../bin/prism -ex models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/wlan.4-0/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 3.494 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:02 GMT+01:00 2026
Hostname: n23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/wlan.4-0/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 345000 states
Reachable states exploration and model construction done in 1.538 secs.
Sorting reachable states list...

Time for model construction: 1.809 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/wlan.4-0/model.umb_rep4.gz"...
Time for exporting: 0.959 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/wlan.4-0/model.umb_rep4.gz:	Size of output file is 15199275 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_ex_wlan.4-0_rep5.log

```
Command(s):
../bin/prism -ex models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/wlan.4-0/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 3.499 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:46 GMT+01:00 2026
Hostname: n23m0113.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/wlan.4-0/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 345000 states
Reachable states exploration and model construction done in 1.508 secs.
Sorting reachable states list...

Time for model construction: 1.852 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252
Choices:     440206
Max/avg:     3/1.28

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/wlan.4-0/model.umb_rep5.gz"...
Time for exporting: 0.93 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/wlan.4-0/model.umb_rep5.gz:	Size of output file is 15199275 bytes
Removing output file to save space for repetition #5
```

