# Log files for prism_from-prism_to-umb-gz_ex on model [oscillators.8-10-0.1-1-0.1-1.0](../../models/oscillators.8-10-0.1-1-0.1-1.0)

Parsed values: `[2091864.0, 2091864.0, 2091864.0, 2091864.0, 2091864.0]`



### Log file: prism_from-prism_to-umb-gz_ex_oscillators.8-10-0.1-1-0.1-1.0_rep1.log

```
Command(s):
../bin/prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 126.264 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:21:42 GMT+01:00 2026
Hostname: n23m0128.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:explicit)...

Computing reachable states... 530 1148 1762 2356 2961 3709 4389 5014 5617 6233 6798 7379 7973 8566 9168 9783 10410 11011 11599 12201 12810 13429 14066 14693 15299 16076 16764 17395 18029 18653 19225 19774 20321 20837 21354 21877 22401 22908 23461 24107 24311 states
Reachable states exploration and model construction done in 121.258 secs.
Sorting reachable states list...

Time for model construction: 122.115 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb.gz"...
Time for exporting: 0.413 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb.gz:	Size of output file is 2091864 bytes
```



### Log file: prism_from-prism_to-umb-gz_ex_oscillators.8-10-0.1-1-0.1-1.0_rep2.log

```
Command(s):
../bin/prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 103.619 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:54:17 GMT+01:00 2026
Hostname: n23m0307.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:explicit)...

Computing reachable states... 649 1371 2106 2809 3548 4291 5034 5778 6443 7170 7909 8652 9396 10131 10877 11623 12361 13027 13758 14468 15205 15967 16710 17478 18244 18966 19709 20458 21202 21952 22697 23362 24095 24311 states
Reachable states exploration and model construction done in 99.989 secs.
Sorting reachable states list...

Time for model construction: 100.77 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep2.gz"...
Time for exporting: 0.258 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep2.gz:	Size of output file is 2091864 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_ex_oscillators.8-10-0.1-1-0.1-1.0_rep3.log

```
Command(s):
../bin/prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 163.526 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:12:01 GMT+01:00 2026
Hostname: n23m0113.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:explicit)...

Computing reachable states... 365 780 1198 1616 2034 2453 2894 3367 3808 4234 4661 5086 5499 5928 6355 6831 7295 7733 8156 8582 9011 9439 9868 10297 10785 11239 11741 12478 13212 13949 14685 15117 15544 15973 16401 16829 17272 17757 18198 18620 19044 19469 19896 20324 20751 21234 21705 22143 22570 22994 23426 23860 24295 24311 states
Reachable states exploration and model construction done in 159.346 secs.
Sorting reachable states list...

Time for model construction: 160.255 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep3.gz"...
Time for exporting: 0.242 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep3.gz:	Size of output file is 2091864 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_ex_oscillators.8-10-0.1-1-0.1-1.0_rep4.log

```
Command(s):
../bin/prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 113.726 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:28:47 GMT+01:00 2026
Hostname: n23m0244.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:explicit)...

Computing reachable states... 509 1100 1692 2267 2865 3471 4081 4743 5485 6224 6964 7709 8457 9203 9952 10702 11450 12104 12684 13293 13903 14506 15114 15678 16260 16853 17449 18062 18687 19317 19946 20724 21501 22282 23067 23851 24311 states
Reachable states exploration and model construction done in 109.857 secs.
Sorting reachable states list...

Time for model construction: 110.644 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep4.gz"...
Time for exporting: 0.243 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep4.gz:	Size of output file is 2091864 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_ex_oscillators.8-10-0.1-1-0.1-1.0_rep5.log

```
Command(s):
../bin/prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 116.186 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:30:50 GMT+01:00 2026
Hostname: n23m0379.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:explicit)...

Computing reachable states... 563 1197 1822 2456 3092 3731 4370 5010 5642 6284 6926 7569 8211 8857 9502 10150 10797 11445 12094 12746 13399 14055 14703 15359 16017 16675 17336 17996 18660 19323 19990 20658 21329 21999 22673 23346 24022 24311 states
Reachable states exploration and model construction done in 112.4 secs.
Sorting reachable states list...

Time for model construction: 113.175 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep5.gz"...
Time for exporting: 0.227 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep5.gz:	Size of output file is 2091864 bytes
Removing output file to save space for repetition #5
```

