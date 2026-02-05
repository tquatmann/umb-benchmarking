# Log files

Tool configuration: prism_from-prism_to-umb-gz_ex
Benchmark: [mapk-cascade.4-30](../../models/mapk-cascade.4-30)
Parsed values: [22829859.0, 22829859.0, 22829859.0, 22829859.0, 22829859.0]



### Log file: prism_from-prism_to-umb-gz_ex_mapk-cascade.4-30_rep1.log

```
Command(s):
../bin/prism -ex models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/mapk-cascade.4-30/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2.833 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:37:50 GMT+01:00 2026
Hostname: r23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/mapk-cascade.4-30/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 99535 states
Reachable states exploration and model construction done in 1.113 secs.
Sorting reachable states list...

Time for model construction: 1.226 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/mapk-cascade.4-30/model.umb.gz"...
Time for exporting: 0.977 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/mapk-cascade.4-30/model.umb.gz:	Size of output file is 22829859 bytes
```



### Log file: prism_from-prism_to-umb-gz_ex_mapk-cascade.4-30_rep2.log

```
Command(s):
../bin/prism -ex models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/mapk-cascade.4-30/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 3.028 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:23:23 GMT+01:00 2026
Hostname: n23m0055.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/mapk-cascade.4-30/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 99535 states
Reachable states exploration and model construction done in 1.082 secs.
Sorting reachable states list...

Time for model construction: 1.191 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/mapk-cascade.4-30/model.umb_rep2.gz"...
Time for exporting: 1.195 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/mapk-cascade.4-30/model.umb_rep2.gz:	Size of output file is 22829859 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_ex_mapk-cascade.4-30_rep3.log

```
Command(s):
../bin/prism -ex models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/mapk-cascade.4-30/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 3.296 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:34 GMT+01:00 2026
Hostname: n23m0165.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/mapk-cascade.4-30/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 99535 states
Reachable states exploration and model construction done in 1.332 secs.
Sorting reachable states list...

Time for model construction: 1.493 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/mapk-cascade.4-30/model.umb_rep3.gz"...
Time for exporting: 1.11 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/mapk-cascade.4-30/model.umb_rep3.gz:	Size of output file is 22829859 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_ex_mapk-cascade.4-30_rep4.log

```
Command(s):
../bin/prism -ex models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/mapk-cascade.4-30/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 3.125 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:11 GMT+01:00 2026
Hostname: n23m0158.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/mapk-cascade.4-30/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 99535 states
Reachable states exploration and model construction done in 1.272 secs.
Sorting reachable states list...

Time for model construction: 1.433 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/mapk-cascade.4-30/model.umb_rep4.gz"...
Time for exporting: 1.064 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/mapk-cascade.4-30/model.umb_rep4.gz:	Size of output file is 22829859 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_ex_mapk-cascade.4-30_rep5.log

```
Command(s):
../bin/prism -ex models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/mapk-cascade.4-30/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2.666 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:26:58 GMT+01:00 2026
Hostname: n23m0351.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/mapk-cascade.4-30/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 99535 states
Reachable states exploration and model construction done in 1.095 secs.
Sorting reachable states list...

Time for model construction: 1.204 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/mapk-cascade.4-30/model.umb_rep5.gz"...
Time for exporting: 0.926 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/mapk-cascade.4-30/model.umb_rep5.gz:	Size of output file is 22829859 bytes
Removing output file to save space for repetition #5
```

