# Log files for prism_from-prism_to-tra_default on model [mapk-cascade.4-30](../../models/mapk-cascade.4-30)

Parsed values: `[23628203.0, 23628203.0, 23628203.0, 23628203.0, 23628203.0]`



### Log file: prism_from-prism_to-tra_default_mapk-cascade.4-30_rep1.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model.tra,lab,rew:precision=17
Wallclock time: 4.948 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:31:28 GMT+01:00 2026
Hostname: n23m0276.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 2.47 seconds (average 0.056136, setup 0.00)

Time for model construction: 2.65 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model.trew"...
Time for exporting: 1.515 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model.tra:	Size of output file is 22829859 bytes
out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model.lab:	Size of output file is 13065 bytes
out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model.srew:	Size of output file is 785224 bytes
out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model.trew:	Size of output file is 55 bytes
```



### Log file: prism_from-prism_to-tra_default_mapk-cascade.4-30_rep2.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep2.tra,lab,rew:precision=17
Wallclock time: 4.449 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:10 GMT+01:00 2026
Hostname: n23m0157.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 1.86 seconds (average 0.042273, setup 0.00)

Time for model construction: 2.009 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep2.trew"...
Time for exporting: 1.495 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep2.tra:	Size of output file is 22829859 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep2.lab:	Size of output file is 13065 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep2.srew:	Size of output file is 785224 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep2.trew:	Size of output file is 55 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_default_mapk-cascade.4-30_rep3.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep3.tra,lab,rew:precision=17
Wallclock time: 4.597 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:03:24 GMT+01:00 2026
Hostname: n23m0134.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 2.30 seconds (average 0.052273, setup 0.00)

Time for model construction: 2.433 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep3.trew"...
Time for exporting: 1.279 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep3.tra:	Size of output file is 22829859 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep3.lab:	Size of output file is 13065 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep3.srew:	Size of output file is 785224 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep3.trew:	Size of output file is 55 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_default_mapk-cascade.4-30_rep4.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep4.tra,lab,rew:precision=17
Wallclock time: 3.869 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:29 GMT+01:00 2026
Hostname: n23m0230.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 1.78 seconds (average 0.040455, setup 0.00)

Time for model construction: 1.889 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep4.trew"...
Time for exporting: 1.392 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep4.tra:	Size of output file is 22829859 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep4.lab:	Size of output file is 13065 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep4.srew:	Size of output file is 785224 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep4.trew:	Size of output file is 55 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_default_mapk-cascade.4-30_rep5.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep5.tra,lab,rew:precision=17
Wallclock time: 3.678 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:50:45 GMT+01:00 2026
Hostname: n23m0044.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 1.78 seconds (average 0.040455, setup 0.00)

Time for model construction: 1.905 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep5.trew"...
Time for exporting: 1.266 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep5.tra:	Size of output file is 22829859 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep5.lab:	Size of output file is 13065 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep5.srew:	Size of output file is 785224 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/mapk-cascade.4-30/model_rep5.trew:	Size of output file is 55 bytes
Removing output file to save space for repetition #5
```

