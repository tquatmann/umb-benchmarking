# Log files

Tool configuration: storm_from-jani_check_exact
Benchmark: [polling.18-16](../../models/polling.18-16)
Parsed values: [195.872, 208.13400000000001, 189.21, 220.314, 232.577]



### Log file: storm_from-jani_check_exact_polling.18-16_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/polling.18-16/model.jani --janiproperty  --exact
Wallclock time: 269.143 seconds
Return code: -9
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:44:15 2026
Command line arguments: --timemem --buildfull --jani models/polling.18-16/model.jani --janiproperty --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.036s.

Time for model construction: 195.836s.

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
```



### Log file: storm_from-jani_check_exact_polling.18-16_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/polling.18-16/model.jani --janiproperty  --exact
Wallclock time: 281.597 seconds
Return code: -9
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:06 2026
Command line arguments: --timemem --buildfull --jani models/polling.18-16/model.jani --janiproperty --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.008s.

Time for model construction: 208.126s.

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
```



### Log file: storm_from-jani_check_exact_polling.18-16_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/polling.18-16/model.jani --janiproperty  --exact
Wallclock time: 257.526 seconds
Return code: -9
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:24:12 2026
Command line arguments: --timemem --buildfull --jani models/polling.18-16/model.jani --janiproperty --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.026s.

Time for model construction: 189.184s.

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
```



### Log file: storm_from-jani_check_exact_polling.18-16_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/polling.18-16/model.jani --janiproperty  --exact
Wallclock time: 298.187 seconds
Return code: -9
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:09:50 2026
Command line arguments: --timemem --buildfull --jani models/polling.18-16/model.jani --janiproperty --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.025s.

Time for model construction: 220.289s.

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
```



### Log file: storm_from-jani_check_exact_polling.18-16_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/polling.18-16/model.jani --janiproperty  --exact
Wallclock time: 322.661 seconds
Return code: -9
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:07:06 2026
Command line arguments: --timemem --buildfull --jani models/polling.18-16/model.jani --janiproperty --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.023s.

Time for model construction: 232.554s.

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
```

