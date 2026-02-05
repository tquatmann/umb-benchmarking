# Log files

Tool configuration: modest_from-umb_check_unsafe
Benchmark: [nand.60-4](../../models/nand.60-4)
Parsed values: [TO, 5981.117, 4253.752, 5407.85, 5974.232]



### Log file: modest_from-umb_check_unsafe_nand.60-4_rep1.log

```
Command(s):
../bin/modest mcsta models/nand.60-4/modest.model.umb models/nand.60-4/modest.umb.properties.txt --unsafe -D --exhaustive
Wallclock time: 7200.054 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/nand.60-4/modest.model.umb models/nand.60-4/modest.umb.properties.txt --unsafe -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

##############################Output to stderr##############################
Fatal error. System.AccessViolationException: Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
```



### Log file: modest_from-umb_check_unsafe_nand.60-4_rep2.log

```
Command(s):
../bin/modest mcsta models/nand.60-4/modest.model.umb models/nand.60-4/modest.umb.properties.txt --unsafe -D --exhaustive
Wallclock time: 5981.117 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/nand.60-4/modest.model.umb models/nand.60-4/modest.umb.properties.txt --unsafe -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

Peak memory usage: 474 MB
Analysis results for UMB

+ State space (UMB)
  States:            18826082
  Choices:           18826082
  Branches:          29772212
  Time (decompress): 0.1 s
  Time (validate):   0.0 s
  Time (load):       0.5 s

+ Property reliable
  Probability: 0.6867214589192275
  Bounds:      [0.6867214589192275, 0.6867214589192275]
  Time:        5980.3 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        5980.3 s

```



### Log file: modest_from-umb_check_unsafe_nand.60-4_rep3.log

```
Command(s):
../bin/modest mcsta models/nand.60-4/modest.model.umb models/nand.60-4/modest.umb.properties.txt --unsafe -D --exhaustive
Wallclock time: 4253.752 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/nand.60-4/modest.model.umb models/nand.60-4/modest.umb.properties.txt --unsafe -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

Peak memory usage: 384 MB
Analysis results for UMB

+ State space (UMB)
  States:            18826082
  Choices:           18826082
  Branches:          29772212
  Time (decompress): 0.0 s
  Time (validate):   0.0 s
  Time (load):       2.4 s

+ Property reliable
  Probability: 0.6867214589192275
  Bounds:      [0.6867214589192275, 0.6867214589192275]
  Time:        4251.1 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        4251.1 s

```



### Log file: modest_from-umb_check_unsafe_nand.60-4_rep4.log

```
Command(s):
../bin/modest mcsta models/nand.60-4/modest.model.umb models/nand.60-4/modest.umb.properties.txt --unsafe -D --exhaustive
Wallclock time: 5407.850 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/nand.60-4/modest.model.umb models/nand.60-4/modest.umb.properties.txt --unsafe -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

Peak memory usage: 455 MB
Analysis results for UMB

+ State space (UMB)
  States:            18826082
  Choices:           18826082
  Branches:          29772212
  Time (decompress): 0.0 s
  Time (validate):   0.0 s
  Time (load):       0.7 s

+ Property reliable
  Probability: 0.6867214589192275
  Bounds:      [0.6867214589192275, 0.6867214589192275]
  Time:        5406.9 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        5406.9 s

```



### Log file: modest_from-umb_check_unsafe_nand.60-4_rep5.log

```
Command(s):
../bin/modest mcsta models/nand.60-4/modest.model.umb models/nand.60-4/modest.umb.properties.txt --unsafe -D --exhaustive
Wallclock time: 5974.232 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/nand.60-4/modest.model.umb models/nand.60-4/modest.umb.properties.txt --unsafe -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

Peak memory usage: 457 MB
Analysis results for UMB

+ State space (UMB)
  States:            18826082
  Choices:           18826082
  Branches:          29772212
  Time (decompress): 0.1 s
  Time (validate):   0.0 s
  Time (load):       0.9 s

+ Property reliable
  Probability: 0.6867214589192275
  Bounds:      [0.6867214589192275, 0.6867214589192275]
  Time:        5973.1 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        5973.1 s

```

