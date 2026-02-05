# Log files

Tool configuration: storm_from-jani_check_sparse
Benchmark: [polling.18-16](../../models/polling.18-16)
Parsed values: [77.434, 70.358, 69.625, 95.34, 70.786]



### Log file: storm_from-jani_check_sparse_polling.18-16_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/polling.18-16/model.jani --janiproperty
Wallclock time: 77.434 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:18:41 2026
Command line arguments: --timemem --buildfull --jani models/polling.18-16/model.jani --janiproperty
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.006s.

Time for model construction: 65.007s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * serve_s2 -> 131072 item(s)
   * serve_s1 -> 131072 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "s1_before_s2": Pmin=? [(!"serve_s2") U "serve_s1"] ...
Result (for initial states): 0.539005252
Time for model checking: 12.365s.

Performance statistics:
  * peak memory usage: 5743MB
  * CPU time: 75.374s
  * wallclock time: 77.391s
```



### Log file: storm_from-jani_check_sparse_polling.18-16_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/polling.18-16/model.jani --janiproperty
Wallclock time: 70.358 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:07 2026
Command line arguments: --timemem --buildfull --jani models/polling.18-16/model.jani --janiproperty
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

Time for model construction: 59.248s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * serve_s2 -> 131072 item(s)
   * serve_s1 -> 131072 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "s1_before_s2": Pmin=? [(!"serve_s2") U "serve_s1"] ...
Result (for initial states): 0.539005252
Time for model checking: 9.909s.

Performance statistics:
  * peak memory usage: 5742MB
  * CPU time: 68.204s
  * wallclock time: 69.168s
```



### Log file: storm_from-jani_check_sparse_polling.18-16_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/polling.18-16/model.jani --janiproperty
Wallclock time: 69.625 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:24:12 2026
Command line arguments: --timemem --buildfull --jani models/polling.18-16/model.jani --janiproperty
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.026s.

Time for model construction: 59.844s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * serve_s2 -> 131072 item(s)
   * serve_s1 -> 131072 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "s1_before_s2": Pmin=? [(!"serve_s2") U "serve_s1"] ...
Result (for initial states): 0.539005252
Time for model checking: 9.713s.

Performance statistics:
  * peak memory usage: 5743MB
  * CPU time: 68.629s
  * wallclock time: 69.590s
```



### Log file: storm_from-jani_check_sparse_polling.18-16_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/polling.18-16/model.jani --janiproperty
Wallclock time: 95.340 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:07:49 2026
Command line arguments: --timemem --buildfull --jani models/polling.18-16/model.jani --janiproperty
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.045s.

Time for model construction: 75.090s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * serve_s2 -> 131072 item(s)
   * serve_s1 -> 131072 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "s1_before_s2": Pmin=? [(!"serve_s2") U "serve_s1"] ...
Result (for initial states): 0.539005252
Time for model checking: 19.797s.

Performance statistics:
  * peak memory usage: 5743MB
  * CPU time: 92.778s
  * wallclock time: 94.942s
```



### Log file: storm_from-jani_check_sparse_polling.18-16_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/polling.18-16/model.jani --janiproperty
Wallclock time: 70.786 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:01:00 2026
Command line arguments: --timemem --buildfull --jani models/polling.18-16/model.jani --janiproperty
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.028s.

Time for model construction: 60.213s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * serve_s2 -> 131072 item(s)
   * serve_s1 -> 131072 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "s1_before_s2": Pmin=? [(!"serve_s2") U "serve_s1"] ...
Result (for initial states): 0.539005252
Time for model checking: 10.498s.

Performance statistics:
  * peak memory usage: 5743MB
  * CPU time: 69.721s
  * wallclock time: 70.746s
```

