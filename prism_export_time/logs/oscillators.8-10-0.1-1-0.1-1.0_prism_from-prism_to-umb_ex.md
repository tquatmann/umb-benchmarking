# Log files for prism_from-prism_to-umb_ex on model [oscillators.8-10-0.1-1-0.1-1.0](../../models/oscillators.8-10-0.1-1-0.1-1.0)

Parsed values: `[0.188, 0.231, 0.651, 0.209, 0.218]`



### Log file: prism_from-prism_to-umb_ex_oscillators.8-10-0.1-1-0.1-1.0_rep1.log

```
Command(s):
../bin/prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 102.863 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:37:50 GMT+01:00 2026
Hostname: n23m0249.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:explicit)...

Computing reachable states... 633 1353 2037 2716 3436 4161 4878 5610 6344 7078 7813 8546 9280 10017 10755 11495 12236 12980 13724 14470 15218 15968 16711 17457 18205 18959 19717 20479 21211 21986 22752 23528 24306 24311 states
Reachable states exploration and model construction done in 99.093 secs.
Sorting reachable states list...

Time for model construction: 99.892 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb"...
Model export size: 1591 Kb
Time for exporting: 0.188 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/oscillators.8-10-0.1-1-0.1-1.0/model.umb:	Size of output file is 1629696 bytes
```



### Log file: prism_from-prism_to-umb_ex_oscillators.8-10-0.1-1-0.1-1.0_rep2.log

```
Command(s):
../bin/prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 105.450 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:52 GMT+01:00 2026
Hostname: n23m0168.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:explicit)...

Computing reachable states... 644 1337 1964 2618 3252 3871 4501 5128 5764 6507 7256 8006 8755 9508 10265 11024 11783 12545 13309 14072 14813 15539 16269 17002 17739 18467 19193 19924 20659 21397 22138 22880 23626 24311 states
Reachable states exploration and model construction done in 101.809 secs.
Sorting reachable states list...

Time for model construction: 102.573 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.umb"...
Model export size: 1591 Kb
Time for exporting: 0.231 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.umb:	Size of output file is 1629696 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_ex_oscillators.8-10-0.1-1-0.1-1.0_rep3.log

```
Command(s):
../bin/prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 197.209 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:32:22 GMT+01:00 2026
Hostname: n23m0308.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:explicit)...

Computing reachable states... 317 695 1076 1454 1827 2208 2589 2970 3341 3727 4112 4495 4873 5251 5636 6024 6408 6781 7165 7551 7936 8309 8704 9098 9480 9863 10249 10638 11021 11399 11786 12173 12563 12939 13330 13721 14113 14496 14880 15269 15655 16036 16413 16798 17186 17568 17946 18333 18718 19106 19478 19861 20245 20631 21009 21396 21784 22172 22545 22931 23317 23705 24081 24311 states
Reachable states exploration and model construction done in 191.062 secs.
Sorting reachable states list...

Time for model construction: 192.169 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.umb"...
Model export size: 1591 Kb
Time for exporting: 0.651 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.umb:	Size of output file is 1629696 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_ex_oscillators.8-10-0.1-1-0.1-1.0_rep4.log

```
Command(s):
../bin/prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 152.950 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:37 GMT+01:00 2026
Hostname: r23m0029.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:explicit)...

Computing reachable states... 419 897 1376 1850 2319 2792 3272 3743 4218 4701 5152 5636 6127 6617 7107 7597 8093 8588 9083 9580 10076 10578 11074 11572 12070 12570 13071 13566 14056 14548 15044 15547 16046 16546 17035 17543 18042 18542 19044 19545 20053 20552 21053 21556 22058 22567 23065 23568 24073 24311 states
Reachable states exploration and model construction done in 148.591 secs.
Sorting reachable states list...

Time for model construction: 149.503 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.umb"...
Model export size: 1591 Kb
Time for exporting: 0.209 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.umb:	Size of output file is 1629696 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_ex_oscillators.8-10-0.1-1-0.1-1.0_rep5.log

```
Command(s):
../bin/prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 188.346 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:53:48 GMT+01:00 2026
Hostname: r23m0197.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:explicit)...

Computing reachable states... 343 738 1129 1526 1917 2311 2704 3099 3496 3893 4288 4683 5084 5479 5875 6269 6664 7060 7456 7853 8252 8645 9039 9436 9833 10228 10624 11023 11422 11822 12224 12626 13023 13422 13823 14223 14619 15019 15422 15818 16216 16614 17009 17407 17808 18203 18602 19000 19402 19804 20207 20607 21007 21406 21807 22205 22607 23011 23413 23811 24211 24311 states
Reachable states exploration and model construction done in 184.005 secs.
Sorting reachable states list...

Time for model construction: 184.941 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.umb"...
Model export size: 1591 Kb
Time for exporting: 0.218 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.umb:	Size of output file is 1629696 bytes
Removing output file to save space for repetition #5
```

