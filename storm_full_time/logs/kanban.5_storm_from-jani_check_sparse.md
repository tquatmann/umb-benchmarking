# Log files

Tool configuration: storm_from-jani_check_sparse
Benchmark: [kanban.5](../../models/kanban.5)
Parsed values: [118.412, 39.308, 32.252, 28.606, 27.951]



### Log file: storm_from-jani_check_sparse_kanban.5_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/kanban.5/model.jani --janiproperty
Wallclock time: 118.412 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:26:42 2026
Command line arguments: --timemem --buildfull --jani models/kanban.5/model.jani --janiproperty
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.066s.

Time for model construction: 85.156s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2546432
Transitions: 	24460016
Reward Models:  throughput
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "throughput": R{"throughput"}min=? [LRA] ...
Result (for initial states): 0.307124777
Time for model checking: 33.028s.

Performance statistics:
  * peak memory usage: 2945MB
  * CPU time: 115.973s
  * wallclock time: 118.265s
```



### Log file: storm_from-jani_check_sparse_kanban.5_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/kanban.5/model.jani --janiproperty
Wallclock time: 39.308 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:08 2026
Command line arguments: --timemem --buildfull --jani models/kanban.5/model.jani --janiproperty
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.010s.

Time for model construction: 25.723s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2546432
Transitions: 	24460016
Reward Models:  throughput
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "throughput": R{"throughput"}min=? [LRA] ...
Result (for initial states): 0.307124777
Time for model checking: 12.339s.

Performance statistics:
  * peak memory usage: 2944MB
  * CPU time: 37.341s
  * wallclock time: 38.080s
```



### Log file: storm_from-jani_check_sparse_kanban.5_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/kanban.5/model.jani --janiproperty
Wallclock time: 32.252 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:13:54 2026
Command line arguments: --timemem --buildfull --jani models/kanban.5/model.jani --janiproperty
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 22.060s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2546432
Transitions: 	24460016
Reward Models:  throughput
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "throughput": R{"throughput"}min=? [LRA] ...
Result (for initial states): 0.307124777
Time for model checking: 10.136s.

Performance statistics:
  * peak memory usage: 2944MB
  * CPU time: 31.605s
  * wallclock time: 32.205s
```



### Log file: storm_from-jani_check_sparse_kanban.5_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/kanban.5/model.jani --janiproperty
Wallclock time: 28.606 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:23:59 2026
Command line arguments: --timemem --buildfull --jani models/kanban.5/model.jani --janiproperty
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.016s.

Time for model construction: 18.678s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2546432
Transitions: 	24460016
Reward Models:  throughput
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "throughput": R{"throughput"}min=? [LRA] ...
Result (for initial states): 0.307124777
Time for model checking: 9.851s.

Performance statistics:
  * peak memory usage: 2944MB
  * CPU time: 27.942s
  * wallclock time: 28.551s
```



### Log file: storm_from-jani_check_sparse_kanban.5_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/kanban.5/model.jani --janiproperty
Wallclock time: 27.951 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:11:12 2026
Command line arguments: --timemem --buildfull --jani models/kanban.5/model.jani --janiproperty
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 18.718s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2546432
Transitions: 	24460016
Reward Models:  throughput
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "throughput": R{"throughput"}min=? [LRA] ...
Result (for initial states): 0.307124777
Time for model checking: 9.162s.

Performance statistics:
  * peak memory usage: 2945MB
  * CPU time: 27.353s
  * wallclock time: 27.890s
```

