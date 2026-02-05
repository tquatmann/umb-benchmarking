# Log files

Tool configuration: storm_from-jani_to-drn-gz_sparse
Benchmark: [oscillators.8-10-0.1-1-0.1-1.0](../../models/oscillators.8-10-0.1-1-0.1-1.0)
Parsed values: [0.071, 0.083, 0.068, 0.078, 0.068]



### Log file: storm_from-jani_to-drn-gz_sparse_oscillators.8-10-0.1-1-0.1-1.0_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --exportbuild out/storm_from-jani_to-drn-gz_sparse/oscillators.8-10-0.1-1-0.1-1.0/model.drn.gz drn --compression gzip
Wallclock time: 42.503 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:22:13 2026
Command line arguments: --timemem --buildfull --jani models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --exportbuild out/storm_from-jani_to-drn-gz_sparse/oscillators.8-10-0.1-1-0.1-1.0/model.drn.gz drn --compression gzip
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 7.611s.

Time for model construction: 32.210s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	24311
Transitions: 	76623
Reward Models:  time_to_synch
State Labels: 	3 labels
   * init -> 1 item(s)
   * deadlock -> 0 item(s)
   * target -> 2 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-drn-gz_sparse/oscillators.8-10-0.1-1-0.1-1.0/model.drn.gz'.
Time for model export: 0.071s.


Performance statistics:
  * peak memory usage: 868MB
  * CPU time: 41.795s
  * wallclock time: 42.222s

############################## Output files ##############################
out/storm_from-jani_to-drn-gz_sparse/oscillators.8-10-0.1-1-0.1-1.0/model.drn.gz:	Size of output file is 298575 bytes
```



### Log file: storm_from-jani_to-drn-gz_sparse_oscillators.8-10-0.1-1-0.1-1.0_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --exportbuild out/storm_from-jani_to-drn-gz_sparse/oscillators.8-10-0.1-1-0.1-1.0/model.drn_rep2.gz drn --compression gzip
Wallclock time: 124.026 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:08:59 2026
Command line arguments: --timemem --buildfull --jani models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --exportbuild out/storm_from-jani_to-drn-gz_sparse/oscillators.8-10-0.1-1-0.1-1.0/model.drn_rep2.gz drn --compression gzip
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 9.181s.

Time for model construction: 111.058s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	24311
Transitions: 	76623
Reward Models:  time_to_synch
State Labels: 	3 labels
   * init -> 1 item(s)
   * deadlock -> 0 item(s)
   * target -> 2 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-drn-gz_sparse/oscillators.8-10-0.1-1-0.1-1.0/model.drn_rep2.gz'.
Time for model export: 0.083s.


Performance statistics:
  * peak memory usage: 868MB
  * CPU time: 122.895s
  * wallclock time: 123.898s

############################## Output files ##############################
out/storm_from-jani_to-drn-gz_sparse/oscillators.8-10-0.1-1-0.1-1.0/model.drn_rep2.gz:	Size of output file is 298581 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-drn-gz_sparse_oscillators.8-10-0.1-1-0.1-1.0_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --exportbuild out/storm_from-jani_to-drn-gz_sparse/oscillators.8-10-0.1-1-0.1-1.0/model.drn_rep3.gz drn --compression gzip
Wallclock time: 46.053 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:34:32 2026
Command line arguments: --timemem --buildfull --jani models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --exportbuild out/storm_from-jani_to-drn-gz_sparse/oscillators.8-10-0.1-1-0.1-1.0/model.drn_rep3.gz drn --compression gzip
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 6.958s.

Time for model construction: 36.563s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	24311
Transitions: 	76623
Reward Models:  time_to_synch
State Labels: 	3 labels
   * init -> 1 item(s)
   * deadlock -> 0 item(s)
   * target -> 2 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-drn-gz_sparse/oscillators.8-10-0.1-1-0.1-1.0/model.drn_rep3.gz'.
Time for model export: 0.068s.


Performance statistics:
  * peak memory usage: 868MB
  * CPU time: 45.610s
  * wallclock time: 45.986s

############################## Output files ##############################
out/storm_from-jani_to-drn-gz_sparse/oscillators.8-10-0.1-1-0.1-1.0/model.drn_rep3.gz:	Size of output file is 298581 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-drn-gz_sparse_oscillators.8-10-0.1-1-0.1-1.0_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --exportbuild out/storm_from-jani_to-drn-gz_sparse/oscillators.8-10-0.1-1-0.1-1.0/model.drn_rep4.gz drn --compression gzip
Wallclock time: 63.301 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:27:11 2026
Command line arguments: --timemem --buildfull --jani models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --exportbuild out/storm_from-jani_to-drn-gz_sparse/oscillators.8-10-0.1-1-0.1-1.0/model.drn_rep4.gz drn --compression gzip
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 7.903s.

Time for model construction: 52.224s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	24311
Transitions: 	76623
Reward Models:  time_to_synch
State Labels: 	3 labels
   * init -> 1 item(s)
   * deadlock -> 0 item(s)
   * target -> 2 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-drn-gz_sparse/oscillators.8-10-0.1-1-0.1-1.0/model.drn_rep4.gz'.
Time for model export: 0.078s.


Performance statistics:
  * peak memory usage: 867MB
  * CPU time: 62.184s
  * wallclock time: 62.730s

############################## Output files ##############################
out/storm_from-jani_to-drn-gz_sparse/oscillators.8-10-0.1-1-0.1-1.0/model.drn_rep4.gz:	Size of output file is 298581 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-drn-gz_sparse_oscillators.8-10-0.1-1-0.1-1.0_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --exportbuild out/storm_from-jani_to-drn-gz_sparse/oscillators.8-10-0.1-1-0.1-1.0/model.drn_rep5.gz drn --compression gzip
Wallclock time: 45.226 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:48:13 2026
Command line arguments: --timemem --buildfull --jani models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --exportbuild out/storm_from-jani_to-drn-gz_sparse/oscillators.8-10-0.1-1-0.1-1.0/model.drn_rep5.gz drn --compression gzip
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 7.012s.

Time for model construction: 35.682s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	24311
Transitions: 	76623
Reward Models:  time_to_synch
State Labels: 	3 labels
   * init -> 1 item(s)
   * deadlock -> 0 item(s)
   * target -> 2 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-drn-gz_sparse/oscillators.8-10-0.1-1-0.1-1.0/model.drn_rep5.gz'.
Time for model export: 0.068s.


Performance statistics:
  * peak memory usage: 868MB
  * CPU time: 44.763s
  * wallclock time: 45.167s

############################## Output files ##############################
out/storm_from-jani_to-drn-gz_sparse/oscillators.8-10-0.1-1-0.1-1.0/model.drn_rep5.gz:	Size of output file is 298581 bytes
Removing output file to save space for repetition #5
```

