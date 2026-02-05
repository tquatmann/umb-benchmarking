# Log files

Tool configuration: storm_from-prism_check_exact
Benchmark: [firewire.false-36-800](../../models/firewire.false-36-800)
Parsed values: [95.662, 93.01, 99.183, 104.652, 382.396]



### Log file: storm_from-prism_check_exact_firewire.false-36-800_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/firewire.false-36-800/model.prism --prismcompat --prop models/firewire.false-36-800/property.props --exact
Wallclock time: 95.662 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:48:24 2026
Command line arguments: --timemem --buildfull --prism models/firewire.false-36-800/model.prism --prismcompat --prop models/firewire.false-36-800/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.036s.

Time for model construction: 2.213s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	212268
Transitions: 	481792
Choices: 	478756
Reward Models:  time
State Labels: 	3 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * done -> 2 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "deadline": Pmin=? [true Urew{"time"}<=800 "done"] ...
Result (for initial states): 481/512 (approx. 0.939453125)
Time for model checking: 93.147s.

Performance statistics:
  * peak memory usage: 767MB
  * CPU time: 94.950s
  * wallclock time: 95.498s
```



### Log file: storm_from-prism_check_exact_firewire.false-36-800_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/firewire.false-36-800/model.prism --prismcompat --prop models/firewire.false-36-800/property.props --exact
Wallclock time: 93.010 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:38:21 2026
Command line arguments: --timemem --buildfull --prism models/firewire.false-36-800/model.prism --prismcompat --prop models/firewire.false-36-800/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.016s.

Time for model construction: 2.181s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	212268
Transitions: 	481792
Choices: 	478756
Reward Models:  time
State Labels: 	3 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * done -> 2 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "deadline": Pmin=? [true Urew{"time"}<=800 "done"] ...
Result (for initial states): 481/512 (approx. 0.939453125)
Time for model checking: 90.653s.

Performance statistics:
  * peak memory usage: 768MB
  * CPU time: 92.517s
  * wallclock time: 92.939s
```



### Log file: storm_from-prism_check_exact_firewire.false-36-800_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/firewire.false-36-800/model.prism --prismcompat --prop models/firewire.false-36-800/property.props --exact
Wallclock time: 99.183 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:57:56 2026
Command line arguments: --timemem --buildfull --prism models/firewire.false-36-800/model.prism --prismcompat --prop models/firewire.false-36-800/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.008s.

Time for model construction: 2.308s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	212268
Transitions: 	481792
Choices: 	478756
Reward Models:  time
State Labels: 	3 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * done -> 2 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "deadline": Pmin=? [true Urew{"time"}<=800 "done"] ...
Result (for initial states): 481/512 (approx. 0.939453125)
Time for model checking: 96.698s.

Performance statistics:
  * peak memory usage: 767MB
  * CPU time: 98.564s
  * wallclock time: 99.107s
```



### Log file: storm_from-prism_check_exact_firewire.false-36-800_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/firewire.false-36-800/model.prism --prismcompat --prop models/firewire.false-36-800/property.props --exact
Wallclock time: 104.652 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:37:19 2026
Command line arguments: --timemem --buildfull --prism models/firewire.false-36-800/model.prism --prismcompat --prop models/firewire.false-36-800/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.031s.

Time for model construction: 2.480s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	212268
Transitions: 	481792
Choices: 	478756
Reward Models:  time
State Labels: 	3 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * done -> 2 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "deadline": Pmin=? [true Urew{"time"}<=800 "done"] ...
Result (for initial states): 481/512 (approx. 0.939453125)
Time for model checking: 101.179s.

Performance statistics:
  * peak memory usage: 768MB
  * CPU time: 103.242s
  * wallclock time: 103.782s
```



### Log file: storm_from-prism_check_exact_firewire.false-36-800_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/firewire.false-36-800/model.prism --prismcompat --prop models/firewire.false-36-800/property.props --exact
Wallclock time: 382.396 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:12:21 2026
Command line arguments: --timemem --buildfull --prism models/firewire.false-36-800/model.prism --prismcompat --prop models/firewire.false-36-800/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.037s.

Time for model construction: 10.123s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	212268
Transitions: 	481792
Choices: 	478756
Reward Models:  time
State Labels: 	3 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * done -> 2 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "deadline": Pmin=? [true Urew{"time"}<=800 "done"] ...
Result (for initial states): 481/512 (approx. 0.939453125)
Time for model checking: 371.711s.

Performance statistics:
  * peak memory usage: 767MB
  * CPU time: 378.141s
  * wallclock time: 382.155s
```

