# Log files

Tool configuration: storm_from-umb-xz_check_sparse
Benchmark: [eajs.6-300-13](../../models/eajs.6-300-13)
Parsed values: [2.135, 2.745, 2.191, 2.971, 2.237]



### Log file: storm_from-umb-xz_check_sparse_eajs.6-300-13_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/eajs.6-300-13/storm.model.umb.xz --prop models/eajs.6-300-13/property.props
Wallclock time: 7.094 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 08:00:34 2026
Command line arguments: --timemem --buildfull --explicit-umb models/eajs.6-300-13/storm.model.umb.xz --prop models/eajs.6-300-13/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.003s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 1.782s seconds.
Time for model construction: 2.135s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	7901694
Transitions: 	19722777
Choices: 	11897412
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 28620 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "ExpUtil": R{"utilityLocal"}max=? [F "emptyBattery"] ...
Result (for initial states): 12.05111082
Time for model checking: 4.893s.

Performance statistics:
  * peak memory usage: 2141MB
  * CPU time: 6.646s
  * wallclock time: 7.051s
```



### Log file: storm_from-umb-xz_check_sparse_eajs.6-300-13_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/eajs.6-300-13/storm.model.umb.xz --prop models/eajs.6-300-13/property.props
Wallclock time: 10.584 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:07:08 2026
Command line arguments: --timemem --buildfull --explicit-umb models/eajs.6-300-13/storm.model.umb.xz --prop models/eajs.6-300-13/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.020s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 2.240s seconds.
Time for model construction: 2.745s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	7901694
Transitions: 	19722777
Choices: 	11897412
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 28620 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "ExpUtil": R{"utilityLocal"}max=? [F "emptyBattery"] ...
Result (for initial states): 12.05111082
Time for model checking: 7.715s.

Performance statistics:
  * peak memory usage: 2141MB
  * CPU time: 9.787s
  * wallclock time: 10.500s
```



### Log file: storm_from-umb-xz_check_sparse_eajs.6-300-13_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/eajs.6-300-13/storm.model.umb.xz --prop models/eajs.6-300-13/property.props
Wallclock time: 7.191 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:01 2026
Command line arguments: --timemem --buildfull --explicit-umb models/eajs.6-300-13/storm.model.umb.xz --prop models/eajs.6-300-13/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.016s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 1.845s seconds.
Time for model construction: 2.191s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	7901694
Transitions: 	19722777
Choices: 	11897412
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 28620 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "ExpUtil": R{"utilityLocal"}max=? [F "emptyBattery"] ...
Result (for initial states): 12.05111082
Time for model checking: 4.884s.

Performance statistics:
  * peak memory usage: 2141MB
  * CPU time: 6.667s
  * wallclock time: 7.100s
```



### Log file: storm_from-umb-xz_check_sparse_eajs.6-300-13_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/eajs.6-300-13/storm.model.umb.xz --prop models/eajs.6-300-13/property.props
Wallclock time: 10.310 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:07 2026
Command line arguments: --timemem --buildfull --explicit-umb models/eajs.6-300-13/storm.model.umb.xz --prop models/eajs.6-300-13/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.014s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 2.455s seconds.
Time for model construction: 2.971s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	7901694
Transitions: 	19722777
Choices: 	11897412
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 28620 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "ExpUtil": R{"utilityLocal"}max=? [F "emptyBattery"] ...
Result (for initial states): 12.05111082
Time for model checking: 7.236s.

Performance statistics:
  * peak memory usage: 2140MB
  * CPU time: 9.553s
  * wallclock time: 10.246s
```



### Log file: storm_from-umb-xz_check_sparse_eajs.6-300-13_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/eajs.6-300-13/storm.model.umb.xz --prop models/eajs.6-300-13/property.props
Wallclock time: 7.906 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:06:46 2026
Command line arguments: --timemem --buildfull --explicit-umb models/eajs.6-300-13/storm.model.umb.xz --prop models/eajs.6-300-13/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.010s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 1.877s seconds.
Time for model construction: 2.237s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	7901694
Transitions: 	19722777
Choices: 	11897412
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 28620 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "ExpUtil": R{"utilityLocal"}max=? [F "emptyBattery"] ...
Result (for initial states): 12.05111082
Time for model checking: 5.589s.

Performance statistics:
  * peak memory usage: 2141MB
  * CPU time: 7.408s
  * wallclock time: 7.852s
```

