# Log files for prism_from-prism_to-umb-gz_norewards on model [mapk-cascade.4-30](../../models/mapk-cascade.4-30)

Parsed values: `[1.205, 1.252, 1.445, 1.264, 1.196]`



### Log file: prism_from-prism_to-umb-gz_norewards_mapk-cascade.4-30_rep1.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/mapk-cascade.4-30/model.umb.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 3.500 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:44:11 GMT+01:00 2026
Hostname: r23m0139.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/mapk-cascade.4-30/model.umb.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 1.58 seconds (average 0.035909, setup 0.00)

Time for model construction: 1.724 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/mapk-cascade.4-30/model.umb.gz"...
Time for exporting: 1.205 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/mapk-cascade.4-30/model.umb.gz:	Size of output file is 22829859 bytes
```



### Log file: prism_from-prism_to-umb-gz_norewards_mapk-cascade.4-30_rep2.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/mapk-cascade.4-30/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 3.609 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:51:46 GMT+01:00 2026
Hostname: n23m0063.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/mapk-cascade.4-30/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 1.59 seconds (average 0.036136, setup 0.00)

Time for model construction: 1.709 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/mapk-cascade.4-30/model.umb_rep2.gz"...
Time for exporting: 1.252 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/mapk-cascade.4-30/model.umb_rep2.gz:	Size of output file is 22829859 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_norewards_mapk-cascade.4-30_rep3.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/mapk-cascade.4-30/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 6.329 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:11:00 GMT+01:00 2026
Hostname: n23m0036.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/mapk-cascade.4-30/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 3.80 seconds (average 0.086364, setup 0.00)

Time for model construction: 4.038 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/mapk-cascade.4-30/model.umb_rep3.gz"...
Time for exporting: 1.445 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/mapk-cascade.4-30/model.umb_rep3.gz:	Size of output file is 22829859 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_norewards_mapk-cascade.4-30_rep4.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/mapk-cascade.4-30/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 5.793 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:02:24 GMT+01:00 2026
Hostname: n23m0041.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/mapk-cascade.4-30/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 3.64 seconds (average 0.082727, setup 0.00)

Time for model construction: 3.852 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/mapk-cascade.4-30/model.umb_rep4.gz"...
Time for exporting: 1.264 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/mapk-cascade.4-30/model.umb_rep4.gz:	Size of output file is 22829859 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_norewards_mapk-cascade.4-30_rep5.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/mapk-cascade.4-30/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 3.519 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:26:43 GMT+01:00 2026
Hostname: n23m0058.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/mapk-cascade.4-30/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 1.69 seconds (average 0.038409, setup 0.00)

Time for model construction: 1.806 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/mapk-cascade.4-30/model.umb_rep5.gz"...
Time for exporting: 1.196 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/mapk-cascade.4-30/model.umb_rep5.gz:	Size of output file is 22829859 bytes
Removing output file to save space for repetition #5
```

