# Log files for prism_from-prism_check_ex on model [oscillators.8-10-0.1-1-0.1-1.0](../../models/oscillators.8-10-0.1-1-0.1-1.0)

Parsed values: `[119.911, 111.016, 266.83, 143.913, 157.762]`



### Log file: prism_from-prism_check_ex_oscillators.8-10-0.1-1-0.1-1.0_rep1.log

```
Command(s):
../bin/prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 119.911 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:43:12 GMT+01:00 2026
Hostname: r23m0197.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Parsing properties file "models/oscillators.8-10-0.1-1-0.1-1.0/property.props"...

1 property:
(1) "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 534 1153 1770 2392 3010 3628 4253 4872 5494 6122 6744 7373 7998 8623 9254 9880 10511 11142 11772 12409 13042 13677 14317 14952 15595 16233 16871 17516 18156 18799 19447 20095 20751 21403 22055 22715 23375 24036 24311 states
Reachable states exploration and model construction done in 115.324 secs.
Sorting reachable states list...

Time for model construction: 116.198 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623
Building reward structure...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.013 seconds)
Starting Prob1...
Prob1 took 0.014 seconds.
target=2, inf=0, rest=24309
Starting value iteration (with Jacobi) ...
Value iteration (with Jacobi) took 3154 iterations, 241662634 multiplications and 0.608 seconds.
Expected reachability took 0.643 seconds.

Value in the initial state: 6.007026913358374

Time for model checking: 0.736 seconds.

Result: 6.007026913358374 (+/- 5.972359070145227E-5 estimated; rel err 9.942287851023186E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_oscillators.8-10-0.1-1-0.1-1.0_rep2.log

```
Command(s):
../bin/prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 111.016 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:05:34 GMT+01:00 2026
Hostname: r23m0204.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Parsing properties file "models/oscillators.8-10-0.1-1-0.1-1.0/property.props"...

1 property:
(1) "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 570 1197 1801 2414 3119 3803 4496 5150 5819 6496 7158 7844 8508 9174 9899 10607 11325 12047 12747 13428 14148 14877 15587 16298 16929 17554 18177 18806 19466 20179 20935 21694 22448 23201 23961 24311 states
Reachable states exploration and model construction done in 106.462 secs.
Sorting reachable states list...

Time for model construction: 107.262 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623
Building reward structure...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.012 seconds)
Starting Prob1...
Prob1 took 0.012 seconds.
target=2, inf=0, rest=24309
Starting value iteration (with Jacobi) ...
Value iteration (with Jacobi) took 3154 iterations, 241662634 multiplications and 0.6 seconds.
Expected reachability took 0.632 seconds.

Value in the initial state: 6.007026913358374

Time for model checking: 0.735 seconds.

Result: 6.007026913358374 (+/- 5.972359070145227E-5 estimated; rel err 9.942287851023186E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_oscillators.8-10-0.1-1-0.1-1.0_rep3.log

```
Command(s):
../bin/prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 266.830 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:36:31 GMT+01:00 2026
Hostname: n23m0275.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Parsing properties file "models/oscillators.8-10-0.1-1-0.1-1.0/property.props"...

1 property:
(1) "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 249 561 821 1090 1352 1623 1948 2232 2499 2764 3032 3323 3644 3907 4178 4441 4709 5022 5315 5580 5847 6112 6404 6714 6981 7245 7510 7782 8100 8383 8652 8920 9187 9482 9797 10062 10334 10635 10938 11206 11478 11743 12025 12349 12621 12890 13159 13426 13734 14031 14304 14572 14840 15121 15444 15717 15982 16243 16509 16833 17108 17381 17651 17923 18226 18535 18808 19075 19347 19618 19946 20229 20506 20771 21046 21342 21657 21926 22196 22466 22740 23062 23349 23617 23887 24158 24311 states
Reachable states exploration and model construction done in 260.192 secs.
Sorting reachable states list...

Time for model construction: 261.468 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623
Building reward structure...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.013 seconds)
Starting Prob1...
Prob1 took 0.019 seconds.
target=2, inf=0, rest=24309
Starting value iteration (with Jacobi) ...
Value iteration (with Jacobi) took 3154 iterations, 241662634 multiplications and 0.643 seconds.
Expected reachability took 0.703 seconds.

Value in the initial state: 6.007026913358374

Time for model checking: 0.803 seconds.

Result: 6.007026913358374 (+/- 5.972359070145227E-5 estimated; rel err 9.942287851023186E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_oscillators.8-10-0.1-1-0.1-1.0_rep4.log

```
Command(s):
../bin/prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 143.913 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:59:26 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Parsing properties file "models/oscillators.8-10-0.1-1-0.1-1.0/property.props"...

1 property:
(1) "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 456 973 1492 2013 2536 3059 3583 4106 4630 5156 5681 6208 6733 7258 7782 8306 8832 9358 9883 10409 10934 11463 11992 12519 13047 13573 14100 14627 15153 15680 16204 16730 17255 17781 18308 18832 19355 19882 20406 20931 21455 21979 22503 23030 23556 24083 24311 states
Reachable states exploration and model construction done in 139.463 secs.
Sorting reachable states list...

Time for model construction: 140.318 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623
Building reward structure...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.013 seconds)
Starting Prob1...
Prob1 took 0.014 seconds.
target=2, inf=0, rest=24309
Starting value iteration (with Jacobi) ...
Value iteration (with Jacobi) took 3154 iterations, 241662634 multiplications and 0.57 seconds.
Expected reachability took 0.606 seconds.

Value in the initial state: 6.007026913358374

Time for model checking: 0.685 seconds.

Result: 6.007026913358374 (+/- 5.972359070145227E-5 estimated; rel err 9.942287851023186E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_oscillators.8-10-0.1-1-0.1-1.0_rep5.log

```
Command(s):
../bin/prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 157.762 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:38 GMT+01:00 2026
Hostname: r23m0071.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism models/oscillators.8-10-0.1-1-0.1-1.0/property.props

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Parsing properties file "models/oscillators.8-10-0.1-1-0.1-1.0/property.props"...

1 property:
(1) "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 388 843 1287 1745 2202 2661 3228 3755 4240 4721 5190 5663 6124 6592 7062 7531 8005 8464 8932 9407 9883 10342 10812 11283 11758 12216 12784 13324 13807 14294 14764 15242 15707 16179 16652 17131 17586 18065 18546 19015 19492 19970 20452 20916 21395 21886 22466 23007 23506 23999 24311 states
Reachable states exploration and model construction done in 152.138 secs.
Sorting reachable states list...

Time for model construction: 153.075 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623
Building reward structure...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.012 seconds)
Starting Prob1...
Prob1 took 0.015 seconds.
target=2, inf=0, rest=24309
Starting value iteration (with Jacobi) ...
Value iteration (with Jacobi) took 3154 iterations, 241662634 multiplications and 0.623 seconds.
Expected reachability took 0.664 seconds.

Value in the initial state: 6.007026913358374

Time for model checking: 0.754 seconds.

Result: 6.007026913358374 (+/- 5.972359070145227E-5 estimated; rel err 9.942287851023186E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

