# Log files

Tool configuration: storm_from-umb_check_exact
Benchmark: [resource-gathering.1300-100-100](../../models/resource-gathering.1300-100-100)
Parsed values: [939.556, 982.426, 1027.577, 1024.051, 924.102]



### Log file: storm_from-umb_check_exact_resource-gathering.1300-100-100_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/resource-gathering.1300-100-100/storm.model.exact.umb --prop models/resource-gathering.1300-100-100/property.props --exact
Wallclock time: 939.556 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:41:08 2026
Command line arguments: --timemem --buildfull --explicit-umb models/resource-gathering.1300-100-100/storm.model.exact.umb --prop models/resource-gathering.1300-100-100/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.014s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.103s seconds.
Time for model construction: 1.498s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	958894
Transitions: 	3325526
Choices: 	3080702
Reward Models:  none
State Labels: 	3 labels
   * success -> 94 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "prgoldgem": Pmax=? [true U<=1300 "success"] ...
Result (for initial states): 663060852524178402183203507211353729666956663727350680069210275332115007280621137868004961937357709723179891739352387145366201684190399713388720604667954409751611188058893055489955897549953315586276348761790028621965783364895926897299241911/1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (approx. 0.6630608525)
Time for model checking: 937.872s.

Performance statistics:
  * peak memory usage: 2018MB
  * CPU time: 936.560s
  * wallclock time: 939.418s
```



### Log file: storm_from-umb_check_exact_resource-gathering.1300-100-100_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/resource-gathering.1300-100-100/storm.model.exact.umb --prop models/resource-gathering.1300-100-100/property.props --exact
Wallclock time: 982.426 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:05 2026
Command line arguments: --timemem --buildfull --explicit-umb models/resource-gathering.1300-100-100/storm.model.exact.umb --prop models/resource-gathering.1300-100-100/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.020s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.101s seconds.
Time for model construction: 1.626s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	958894
Transitions: 	3325526
Choices: 	3080702
Reward Models:  none
State Labels: 	3 labels
   * success -> 94 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "prgoldgem": Pmax=? [true U<=1300 "success"] ...
Result (for initial states): 663060852524178402183203507211353729666956663727350680069210275332115007280621137868004961937357709723179891739352387145366201684190399713388720604667954409751611188058893055489955897549953315586276348761790028621965783364895926897299241911/1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (approx. 0.6630608525)
Time for model checking: 980.544s.

Performance statistics:
  * peak memory usage: 2017MB
  * CPU time: 978.433s
  * wallclock time: 982.258s
```



### Log file: storm_from-umb_check_exact_resource-gathering.1300-100-100_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/resource-gathering.1300-100-100/storm.model.exact.umb --prop models/resource-gathering.1300-100-100/property.props --exact
Wallclock time: 1027.577 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:13:54 2026
Command line arguments: --timemem --buildfull --explicit-umb models/resource-gathering.1300-100-100/storm.model.exact.umb --prop models/resource-gathering.1300-100-100/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.018s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.108s seconds.
Time for model construction: 1.769s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	958894
Transitions: 	3325526
Choices: 	3080702
Reward Models:  none
State Labels: 	3 labels
   * success -> 94 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "prgoldgem": Pmax=? [true U<=1300 "success"] ...
Result (for initial states): 663060852524178402183203507211353729666956663727350680069210275332115007280621137868004961937357709723179891739352387145366201684190399713388720604667954409751611188058893055489955897549953315586276348761790028621965783364895926897299241911/1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (approx. 0.6630608525)
Time for model checking: 1025.630s.

Performance statistics:
  * peak memory usage: 2016MB
  * CPU time: 1020.810s
  * wallclock time: 1027.454s
```



### Log file: storm_from-umb_check_exact_resource-gathering.1300-100-100_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/resource-gathering.1300-100-100/storm.model.exact.umb --prop models/resource-gathering.1300-100-100/property.props --exact
Wallclock time: 1024.051 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:24:20 2026
Command line arguments: --timemem --buildfull --explicit-umb models/resource-gathering.1300-100-100/storm.model.exact.umb --prop models/resource-gathering.1300-100-100/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.013s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.111s seconds.
Time for model construction: 1.717s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	958894
Transitions: 	3325526
Choices: 	3080702
Reward Models:  none
State Labels: 	3 labels
   * success -> 94 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "prgoldgem": Pmax=? [true U<=1300 "success"] ...
Result (for initial states): 663060852524178402183203507211353729666956663727350680069210275332115007280621137868004961937357709723179891739352387145366201684190399713388720604667954409751611188058893055489955897549953315586276348761790028621965783364895926897299241911/1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (approx. 0.6630608525)
Time for model checking: 1022.073s.

Performance statistics:
  * peak memory usage: 2018MB
  * CPU time: 1019.773s
  * wallclock time: 1023.846s
```



### Log file: storm_from-umb_check_exact_resource-gathering.1300-100-100_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/resource-gathering.1300-100-100/storm.model.exact.umb --prop models/resource-gathering.1300-100-100/property.props --exact
Wallclock time: 924.102 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:13:17 2026
Command line arguments: --timemem --buildfull --explicit-umb models/resource-gathering.1300-100-100/storm.model.exact.umb --prop models/resource-gathering.1300-100-100/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.010s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.111s seconds.
Time for model construction: 1.495s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	958894
Transitions: 	3325526
Choices: 	3080702
Reward Models:  none
State Labels: 	3 labels
   * success -> 94 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "prgoldgem": Pmax=? [true U<=1300 "success"] ...
Result (for initial states): 663060852524178402183203507211353729666956663727350680069210275332115007280621137868004961937357709723179891739352387145366201684190399713388720604667954409751611188058893055489955897549953315586276348761790028621965783364895926897299241911/1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (approx. 0.6630608525)
Time for model checking: 922.450s.

Performance statistics:
  * peak memory usage: 2018MB
  * CPU time: 921.592s
  * wallclock time: 923.990s
```

