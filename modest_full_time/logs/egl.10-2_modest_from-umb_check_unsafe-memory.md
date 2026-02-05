# Log files for modest_from-umb_check_unsafe-memory on model [egl.10-2](../../models/egl.10-2)

Parsed values: `[TO, TO, 3778.501, TO, TO]`



### Log file: modest_from-umb_check_unsafe-memory_egl.10-2_rep1.log

```
Command(s):
../bin/modest mcsta models/egl.10-2/modest.model.umb models/egl.10-2/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.009 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/egl.10-2/modest.model.umb models/egl.10-2/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.
```



### Log file: modest_from-umb_check_unsafe-memory_egl.10-2_rep2.log

```
Command(s):
../bin/modest mcsta models/egl.10-2/modest.model.umb models/egl.10-2/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.039 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/egl.10-2/modest.model.umb models/egl.10-2/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.
```



### Log file: modest_from-umb_check_unsafe-memory_egl.10-2_rep3.log

```
Command(s):
../bin/modest mcsta models/egl.10-2/modest.model.umb models/egl.10-2/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 3778.501 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/egl.10-2/modest.model.umb models/egl.10-2/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

Peak memory usage: 1553 MB
Analysis results for UMB

+ State space (UMB)
  States:            66060286
  Choices:           66060286
  Branches:          67108861
  Time (decompress): 0.1 s
  Time (validate):   0.0 s
  Time (load):       10.2 s

+ Property unfairA
  Probability: 0.50048828125
  Bounds:      [0.50048828125, 0.50048828125]
  Time:        3768.1 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        3768.1 s

```



### Log file: modest_from-umb_check_unsafe-memory_egl.10-2_rep4.log

```
Command(s):
../bin/modest mcsta models/egl.10-2/modest.model.umb models/egl.10-2/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.008 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/egl.10-2/modest.model.umb models/egl.10-2/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.
```



### Log file: modest_from-umb_check_unsafe-memory_egl.10-2_rep5.log

```
Command(s):
../bin/modest mcsta models/egl.10-2/modest.model.umb models/egl.10-2/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.046 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/egl.10-2/modest.model.umb models/egl.10-2/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

##############################Output to stderr##############################
Fatal error. System.AccessViolationException: Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
```

