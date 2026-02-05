# Log files

Tool configuration: storm_from-umb-gz_check_exact
Benchmark: [egl.10-2](../../models/egl.10-2)
Parsed values: [50.634, 57.566, 50.679, 50.495, 54.607]



### Log file: storm_from-umb-gz_check_exact_egl.10-2_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/egl.10-2/storm.model.exact.umb.gz --prop models/egl.10-2/property.props --exact
Wallclock time: 50.634 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:40:05 2026
Command line arguments: --timemem --buildfull --explicit-umb models/egl.10-2/storm.model.exact.umb.gz --prop models/egl.10-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.015s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 2.962s seconds.
Time for model construction: 30.302s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	66060286
Transitions: 	67108861
Reward Models:  none
State Labels: 	4 labels
   * knowB -> 36680703 item(s)
   * knowA -> 40865279 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "unfairA": P=? [F ((!"knowA") & "knowB")] ...
Result (for initial states): 1025/2048 (approx. 0.5004882812)
Time for model checking: 18.134s.

Performance statistics:
  * peak memory usage: 20992MB
  * CPU time: 44.581s
  * wallclock time: 49.371s
```



### Log file: storm_from-umb-gz_check_exact_egl.10-2_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/egl.10-2/storm.model.exact.umb.gz --prop models/egl.10-2/property.props --exact
Wallclock time: 57.566 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:27:42 2026
Command line arguments: --timemem --buildfull --explicit-umb models/egl.10-2/storm.model.exact.umb.gz --prop models/egl.10-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.009s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 3.262s seconds.
Time for model construction: 34.303s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	66060286
Transitions: 	67108861
Reward Models:  none
State Labels: 	4 labels
   * knowB -> 36680703 item(s)
   * knowA -> 40865279 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "unfairA": P=? [F ((!"knowA") & "knowB")] ...
Result (for initial states): 1025/2048 (approx. 0.5004882812)
Time for model checking: 20.976s.

Performance statistics:
  * peak memory usage: 20992MB
  * CPU time: 50.809s
  * wallclock time: 56.300s
```



### Log file: storm_from-umb-gz_check_exact_egl.10-2_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/egl.10-2/storm.model.exact.umb.gz --prop models/egl.10-2/property.props --exact
Wallclock time: 50.679 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:06:35 2026
Command line arguments: --timemem --buildfull --explicit-umb models/egl.10-2/storm.model.exact.umb.gz --prop models/egl.10-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.018s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 2.927s seconds.
Time for model construction: 30.431s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	66060286
Transitions: 	67108861
Reward Models:  none
State Labels: 	4 labels
   * knowB -> 36680703 item(s)
   * knowA -> 40865279 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "unfairA": P=? [F ((!"knowA") & "knowB")] ...
Result (for initial states): 1025/2048 (approx. 0.5004882812)
Time for model checking: 18.196s.

Performance statistics:
  * peak memory usage: 20993MB
  * CPU time: 44.884s
  * wallclock time: 49.547s
```



### Log file: storm_from-umb-gz_check_exact_egl.10-2_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/egl.10-2/storm.model.exact.umb.gz --prop models/egl.10-2/property.props --exact
Wallclock time: 50.495 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:07:29 2026
Command line arguments: --timemem --buildfull --explicit-umb models/egl.10-2/storm.model.exact.umb.gz --prop models/egl.10-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.013s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 2.922s seconds.
Time for model construction: 30.344s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	66060286
Transitions: 	67108861
Reward Models:  none
State Labels: 	4 labels
   * knowB -> 36680703 item(s)
   * knowA -> 40865279 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "unfairA": P=? [F ((!"knowA") & "knowB")] ...
Result (for initial states): 1025/2048 (approx. 0.5004882812)
Time for model checking: 18.133s.

Performance statistics:
  * peak memory usage: 20992MB
  * CPU time: 44.711s
  * wallclock time: 49.382s
```



### Log file: storm_from-umb-gz_check_exact_egl.10-2_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/egl.10-2/storm.model.exact.umb.gz --prop models/egl.10-2/property.props --exact
Wallclock time: 54.607 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:04:34 2026
Command line arguments: --timemem --buildfull --explicit-umb models/egl.10-2/storm.model.exact.umb.gz --prop models/egl.10-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.016s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 3.180s seconds.
Time for model construction: 32.956s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	66060286
Transitions: 	67108861
Reward Models:  none
State Labels: 	4 labels
   * knowB -> 36680703 item(s)
   * knowA -> 40865279 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "unfairA": P=? [F ((!"knowA") & "knowB")] ...
Result (for initial states): 1025/2048 (approx. 0.5004882812)
Time for model checking: 19.480s.

Performance statistics:
  * peak memory usage: 20993MB
  * CPU time: 48.127s
  * wallclock time: 53.421s
```

