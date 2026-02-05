# Log files for prism_from-prism_to-tra_ex on model [mapk-cascade.4-30](../../models/mapk-cascade.4-30)

Parsed values: `[1.207, 1.198, 1.28, 1.499, 1.268]`



### Log file: prism_from-prism_to-tra_ex_mapk-cascade.4-30_rep1.log

```
Command(s):
../bin/prism -ex models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model.tra,lab,rew:precision=17
Wallclock time: 3.069 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:24:20 GMT+01:00 2026
Hostname: n23m0133.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 99535 states
Reachable states exploration and model construction done in 1.093 secs.
Sorting reachable states list...

Time for model construction: 1.341 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model.trew"...
Time for exporting: 1.207 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model.tra:	Size of output file is 22829859 bytes
out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model.lab:	Size of output file is 13065 bytes
out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model.srew:	Size of output file is 785224 bytes
out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model.trew:	Size of output file is 55 bytes
```



### Log file: prism_from-prism_to-tra_ex_mapk-cascade.4-30_rep2.log

```
Command(s):
../bin/prism -ex models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep2.tra,lab,rew:precision=17
Wallclock time: 3.228 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:57:21 GMT+01:00 2026
Hostname: r23m0203.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 99535 states
Reachable states exploration and model construction done in 1.039 secs.
Sorting reachable states list...

Time for model construction: 1.192 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep2.trew"...
Time for exporting: 1.198 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep2.tra:	Size of output file is 22829859 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep2.lab:	Size of output file is 13065 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep2.srew:	Size of output file is 785224 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep2.trew:	Size of output file is 55 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_ex_mapk-cascade.4-30_rep3.log

```
Command(s):
../bin/prism -ex models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep3.tra,lab,rew:precision=17
Wallclock time: 3.323 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:10 GMT+01:00 2026
Hostname: n23m0012.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 99535 states
Reachable states exploration and model construction done in 1.255 secs.
Sorting reachable states list...

Time for model construction: 1.372 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep3.trew"...
Time for exporting: 1.28 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep3.tra:	Size of output file is 22829859 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep3.lab:	Size of output file is 13065 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep3.srew:	Size of output file is 785224 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep3.trew:	Size of output file is 55 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_ex_mapk-cascade.4-30_rep4.log

```
Command(s):
../bin/prism -ex models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep4.tra,lab,rew:precision=17
Wallclock time: 3.919 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:34 GMT+01:00 2026
Hostname: n23m0174.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 99535 states
Reachable states exploration and model construction done in 1.463 secs.
Sorting reachable states list...

Time for model construction: 1.668 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep4.trew"...
Time for exporting: 1.499 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep4.tra:	Size of output file is 22829859 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep4.lab:	Size of output file is 13065 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep4.srew:	Size of output file is 785224 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep4.trew:	Size of output file is 55 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_ex_mapk-cascade.4-30_rep5.log

```
Command(s):
../bin/prism -ex models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep5.tra,lab,rew:precision=17
Wallclock time: 3.188 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:18:38 GMT+01:00 2026
Hostname: n23m0099.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 99535 states
Reachable states exploration and model construction done in 1.191 secs.
Sorting reachable states list...

Time for model construction: 1.315 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep5.trew"...
Time for exporting: 1.268 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep5.tra:	Size of output file is 22829859 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep5.lab:	Size of output file is 13065 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep5.srew:	Size of output file is 785224 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_ex/mapk-cascade.4-30/model_rep5.trew:	Size of output file is 55 bytes
Removing output file to save space for repetition #5
```

