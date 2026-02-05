# Log files

Tool configuration: prism_from-prism_check_default
Benchmark: [kanban.5](../../models/kanban.5)
Parsed values: [0.561, 0.132, 0.121, 0.298, 0.167]



### Log file: prism_from-prism_check_default_kanban.5_rep1.log

```
Command(s):
../bin/prism  models/kanban.5/model.prism models/kanban.5/property.props
Wallclock time: 1915.823 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:23:36 GMT+01:00 2026
Hostname: r23m0215.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/kanban.5/model.prism models/kanban.5/property.props

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Parsing properties file "models/kanban.5/property.props"...

1 property:
(1) "throughput": R{"throughput"}=? [ S ]

---------------------------------------------------------------------

Model checking: "throughput": R{"throughput"}=? [ S ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 71 iterations in 0.43 seconds (average 0.006056, setup 0.00)

Time for model construction: 0.561 seconds.

Type:        CTMC
States:      2546432 (1 initial)
Transitions: 24460016

Rate matrix: 6308 nodes (14 terminal), 24460016 minterms, vars: 48r/48c

SCCs: 1, BSCCs: 1, non-BSCC states: 0
BSCC sizes: 1:2546432

Computing steady state probabilities for BSCC 1

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=48, nodes=6308] [295.7 KB]
Adding explicit sparse matrices... [levels=27, num=165, compact] [749.6 KB]
Creating vector for diagonals... [dist=187, compact] [4.9 MB]
Allocating iteration vectors... [2 x 19.4 MB]
TOTAL: [44.7 MB]

Starting iterations...
Iteration 27: max relative diff=0.159815, 5.11 sec so far
Iteration 54: max relative diff=0.067739, 10.24 sec so far
Iteration 81: max relative diff=0.036705, 15.35 sec so far
Iteration 108: max relative diff=0.016831, 20.46 sec so far
Iteration 135: max relative diff=0.006954, 25.56 sec so far
Iteration 162: max relative diff=0.003608, 30.68 sec so far
Iteration 189: max relative diff=0.002363, 35.79 sec so far
Iteration 216: max relative diff=0.001486, 40.89 sec so far
Iteration 243: max relative diff=0.000922, 46.00 sec so far
Iteration 270: max relative diff=0.000563, 51.11 sec so far
Iteration 297: max relative diff=0.000347, 56.22 sec so far
Iteration 324: max relative diff=0.000215, 61.34 sec so far
Iteration 351: max relative diff=0.000138, 66.45 sec so far
Iteration 378: max relative diff=0.000092, 71.56 sec so far
Iteration 405: max relative diff=0.000064, 76.68 sec so far
Iteration 432: max relative diff=0.000048, 81.79 sec so far
Iteration 459: max relative diff=0.000038, 86.90 sec so far
Iteration 486: max relative diff=0.000032, 92.01 sec so far
Iteration 513: max relative diff=0.000029, 97.12 sec so far
Iteration 540: max relative diff=0.000026, 102.23 sec so far
Iteration 567: max relative diff=0.000025, 107.34 sec so far
Iteration 594: max relative diff=0.000024, 112.45 sec so far
Iteration 621: max relative diff=0.000024, 117.56 sec so far
Iteration 648: max relative diff=0.000024, 122.66 sec so far
Iteration 675: max relative diff=0.000023, 127.77 sec so far
Iteration 702: max relative diff=0.000023, 132.88 sec so far
Iteration 729: max relative diff=0.000023, 137.99 sec so far
Iteration 756: max relative diff=0.000023, 143.11 sec so far
Iteration 783: max relative diff=0.000023, 148.24 sec so far
Iteration 810: max relative diff=0.000023, 153.36 sec so far
Iteration 837: max relative diff=0.000023, 158.48 sec so far
Iteration 864: max relative diff=0.000023, 163.60 sec so far
Iteration 891: max relative diff=0.000023, 168.72 sec so far
Iteration 918: max relative diff=0.000023, 173.85 sec so far
Iteration 945: max relative diff=0.000023, 178.96 sec so far
Iteration 972: max relative diff=0.000023, 184.09 sec so far
Iteration 999: max relative diff=0.000023, 189.21 sec so far
Iteration 1026: max relative diff=0.000023, 194.32 sec so far
Iteration 1053: max relative diff=0.000023, 199.43 sec so far
Iteration 1080: max relative diff=0.000023, 204.56 sec so far
Iteration 1107: max relative diff=0.000023, 209.67 sec so far
Iteration 1134: max relative diff=0.000023, 214.78 sec so far
Iteration 1161: max relative diff=0.000023, 219.89 sec so far
Iteration 1188: max relative diff=0.000023, 225.01 sec so far
Iteration 1215: max relative diff=0.000023, 230.12 sec so far
Iteration 1242: max relative diff=0.000023, 235.25 sec so far
Iteration 1269: max relative diff=0.000023, 240.37 sec so far
Iteration 1296: max relative diff=0.000023, 245.49 sec so far
Iteration 1323: max relative diff=0.000023, 250.61 sec so far
Iteration 1350: max relative diff=0.000023, 255.73 sec so far
Iteration 1377: max relative diff=0.000023, 260.86 sec so far
Iteration 1404: max relative diff=0.000023, 265.97 sec so far
Iteration 1431: max relative diff=0.000023, 271.09 sec so far
Iteration 1458: max relative diff=0.000023, 276.22 sec so far
Iteration 1485: max relative diff=0.000023, 281.34 sec so far
Iteration 1512: max relative diff=0.000023, 286.45 sec so far
Iteration 1539: max relative diff=0.000023, 291.57 sec so far
Iteration 1566: max relative diff=0.000023, 296.69 sec so far
Iteration 1593: max relative diff=0.000023, 301.80 sec so far
Iteration 1620: max relative diff=0.000023, 306.92 sec so far
Iteration 1647: max relative diff=0.000023, 312.03 sec so far
Iteration 1674: max relative diff=0.000023, 317.16 sec so far
Iteration 1701: max relative diff=0.000023, 322.27 sec so far
Iteration 1728: max relative diff=0.000023, 327.39 sec so far
Iteration 1755: max relative diff=0.000023, 332.50 sec so far
Iteration 1782: max relative diff=0.000023, 337.62 sec so far
Iteration 1809: max relative diff=0.000023, 342.73 sec so far
Iteration 1836: max relative diff=0.000023, 347.85 sec so far
Iteration 1863: max relative diff=0.000023, 352.96 sec so far
Iteration 1890: max relative diff=0.000023, 358.07 sec so far
Iteration 1917: max relative diff=0.000023, 363.19 sec so far
Iteration 1944: max relative diff=0.000023, 368.31 sec so far
Iteration 1971: max relative diff=0.000023, 373.43 sec so far
Iteration 1998: max relative diff=0.000023, 378.55 sec so far
Iteration 2025: max relative diff=0.000023, 383.66 sec so far
Iteration 2052: max relative diff=0.000023, 388.78 sec so far
Iteration 2079: max relative diff=0.000023, 393.89 sec so far
Iteration 2106: max relative diff=0.000023, 399.00 sec so far
Iteration 2133: max relative diff=0.000023, 404.11 sec so far
Iteration 2160: max relative diff=0.000023, 409.23 sec so far
Iteration 2187: max relative diff=0.000023, 414.35 sec so far
Iteration 2214: max relative diff=0.000023, 419.47 sec so far
Iteration 2241: max relative diff=0.000023, 424.58 sec so far
Iteration 2268: max relative diff=0.000023, 429.70 sec so far
Iteration 2295: max relative diff=0.000023, 434.82 sec so far
Iteration 2322: max relative diff=0.000023, 439.94 sec so far
Iteration 2349: max relative diff=0.000023, 445.05 sec so far
Iteration 2376: max relative diff=0.000023, 450.17 sec so far
Iteration 2403: max relative diff=0.000023, 455.29 sec so far
Iteration 2430: max relative diff=0.000023, 460.41 sec so far
Iteration 2457: max relative diff=0.000023, 465.53 sec so far
Iteration 2484: max relative diff=0.000023, 470.64 sec so far
Iteration 2511: max relative diff=0.000023, 475.76 sec so far
Iteration 2538: max relative diff=0.000023, 480.88 sec so far
Iteration 2565: max relative diff=0.000023, 485.99 sec so far
Iteration 2592: max relative diff=0.000023, 491.11 sec so far
Iteration 2619: max relative diff=0.000023, 496.22 sec so far
Iteration 2646: max relative diff=0.000023, 501.34 sec so far
Iteration 2673: max relative diff=0.000023, 506.46 sec so far
Iteration 2700: max relative diff=0.000023, 511.58 sec so far
Iteration 2727: max relative diff=0.000023, 516.69 sec so far
Iteration 2754: max relative diff=0.000023, 521.82 sec so far
Iteration 2781: max relative diff=0.000023, 526.93 sec so far
Iteration 2808: max relative diff=0.000023, 532.05 sec so far
Iteration 2835: max relative diff=0.000023, 537.17 sec so far
Iteration 2862: max relative diff=0.000023, 542.28 sec so far
Iteration 2889: max relative diff=0.000023, 547.40 sec so far
Iteration 2916: max relative diff=0.000023, 552.52 sec so far
Iteration 2943: max relative diff=0.000023, 557.63 sec so far
Iteration 2970: max relative diff=0.000023, 562.75 sec so far
Iteration 2997: max relative diff=0.000023, 567.87 sec so far
Iteration 3024: max relative diff=0.000023, 572.98 sec so far
Iteration 3051: max relative diff=0.000023, 578.10 sec so far
Iteration 3078: max relative diff=0.000023, 583.22 sec so far
Iteration 3105: max relative diff=0.000023, 588.33 sec so far
Iteration 3132: max relative diff=0.000023, 593.44 sec so far
Iteration 3159: max relative diff=0.000023, 598.56 sec so far
Iteration 3186: max relative diff=0.000023, 603.68 sec so far
Iteration 3213: max relative diff=0.000023, 608.79 sec so far
Iteration 3240: max relative diff=0.000023, 613.91 sec so far
Iteration 3267: max relative diff=0.000023, 619.03 sec so far
Iteration 3294: max relative diff=0.000023, 624.15 sec so far
Iteration 3321: max relative diff=0.000023, 629.26 sec so far
Iteration 3348: max relative diff=0.000023, 634.38 sec so far
Iteration 3375: max relative diff=0.000023, 639.50 sec so far
Iteration 3402: max relative diff=0.000023, 644.62 sec so far
Iteration 3429: max relative diff=0.000023, 649.73 sec so far
Iteration 3456: max relative diff=0.000023, 654.84 sec so far
Iteration 3483: max relative diff=0.000023, 659.96 sec so far
Iteration 3510: max relative diff=0.000023, 665.08 sec so far
Iteration 3537: max relative diff=0.000023, 670.20 sec so far
Iteration 3564: max relative diff=0.000023, 675.31 sec so far
Iteration 3591: max relative diff=0.000023, 680.42 sec so far
Iteration 3618: max relative diff=0.000023, 685.53 sec so far
Iteration 3645: max relative diff=0.000023, 690.64 sec so far
Iteration 3672: max relative diff=0.000023, 695.76 sec so far
Iteration 3699: max relative diff=0.000023, 700.87 sec so far
Iteration 3726: max relative diff=0.000023, 705.99 sec so far
Iteration 3753: max relative diff=0.000023, 711.10 sec so far
Iteration 3780: max relative diff=0.000023, 716.22 sec so far
Iteration 3807: max relative diff=0.000023, 721.35 sec so far
Iteration 3834: max relative diff=0.000023, 726.46 sec so far
Iteration 3861: max relative diff=0.000023, 731.58 sec so far
Iteration 3888: max relative diff=0.000023, 736.70 sec so far
Iteration 3915: max relative diff=0.000023, 741.81 sec so far
Iteration 3942: max relative diff=0.000023, 746.93 sec so far
Iteration 3969: max relative diff=0.000023, 752.05 sec so far
Iteration 3996: max relative diff=0.000023, 757.16 sec so far
Iteration 4023: max relative diff=0.000023, 762.26 sec so far
Iteration 4050: max relative diff=0.000023, 767.37 sec so far
Iteration 4077: max relative diff=0.000023, 772.48 sec so far
Iteration 4104: max relative diff=0.000023, 777.60 sec so far
Iteration 4131: max relative diff=0.000023, 782.71 sec so far
Iteration 4158: max relative diff=0.000023, 787.83 sec so far
Iteration 4185: max relative diff=0.000023, 792.94 sec so far
Iteration 4212: max relative diff=0.000023, 798.06 sec so far
Iteration 4239: max relative diff=0.000023, 803.19 sec so far
Iteration 4266: max relative diff=0.000023, 808.29 sec so far
Iteration 4293: max relative diff=0.000023, 813.41 sec so far
Iteration 4320: max relative diff=0.000023, 818.52 sec so far
Iteration 4347: max relative diff=0.000023, 823.64 sec so far
Iteration 4374: max relative diff=0.000023, 828.75 sec so far
Iteration 4401: max relative diff=0.000023, 833.86 sec so far
Iteration 4428: max relative diff=0.000023, 838.98 sec so far
Iteration 4455: max relative diff=0.000023, 844.10 sec so far
Iteration 4482: max relative diff=0.000023, 849.21 sec so far
Iteration 4509: max relative diff=0.000023, 854.33 sec so far
Iteration 4536: max relative diff=0.000023, 859.45 sec so far
Iteration 4563: max relative diff=0.000023, 864.57 sec so far
Iteration 4590: max relative diff=0.000023, 869.68 sec so far
Iteration 4617: max relative diff=0.000023, 874.79 sec so far
Iteration 4644: max relative diff=0.000023, 879.92 sec so far
Iteration 4671: max relative diff=0.000023, 885.03 sec so far
Iteration 4698: max relative diff=0.000023, 890.15 sec so far
Iteration 4725: max relative diff=0.000023, 895.25 sec so far
Iteration 4752: max relative diff=0.000023, 900.37 sec so far
Iteration 4779: max relative diff=0.000023, 905.49 sec so far
Iteration 4806: max relative diff=0.000023, 910.61 sec so far
Iteration 4833: max relative diff=0.000023, 915.72 sec so far
Iteration 4860: max relative diff=0.000023, 920.84 sec so far
Iteration 4887: max relative diff=0.000023, 925.96 sec so far
Iteration 4914: max relative diff=0.000023, 931.07 sec so far
Iteration 4941: max relative diff=0.000023, 936.18 sec so far
Iteration 4968: max relative diff=0.000023, 941.29 sec so far
Iteration 4995: max relative diff=0.000023, 946.40 sec so far
Iteration 5022: max relative diff=0.000023, 951.52 sec so far
Iteration 5049: max relative diff=0.000023, 956.64 sec so far
Iteration 5076: max relative diff=0.000023, 961.75 sec so far
Iteration 5103: max relative diff=0.000023, 966.87 sec so far
Iteration 5130: max relative diff=0.000023, 971.98 sec so far
Iteration 5157: max relative diff=0.000023, 977.10 sec so far
Iteration 5184: max relative diff=0.000023, 982.22 sec so far
Iteration 5211: max relative diff=0.000023, 987.34 sec so far
Iteration 5238: max relative diff=0.000023, 992.46 sec so far
Iteration 5265: max relative diff=0.000023, 997.57 sec so far
Iteration 5292: max relative diff=0.000023, 1002.68 sec so far
Iteration 5319: max relative diff=0.000023, 1007.80 sec so far
Iteration 5346: max relative diff=0.000023, 1012.91 sec so far
Iteration 5373: max relative diff=0.000023, 1018.02 sec so far
Iteration 5400: max relative diff=0.000023, 1023.14 sec so far
Iteration 5427: max relative diff=0.000023, 1028.25 sec so far
Iteration 5454: max relative diff=0.000023, 1033.37 sec so far
Iteration 5481: max relative diff=0.000023, 1038.49 sec so far
Iteration 5508: max relative diff=0.000023, 1043.60 sec so far
Iteration 5535: max relative diff=0.000023, 1048.71 sec so far
Iteration 5562: max relative diff=0.000023, 1053.84 sec so far
Iteration 5589: max relative diff=0.000023, 1058.95 sec so far
Iteration 5616: max relative diff=0.000023, 1064.07 sec so far
Iteration 5643: max relative diff=0.000023, 1069.18 sec so far
Iteration 5670: max relative diff=0.000023, 1074.29 sec so far
Iteration 5697: max relative diff=0.000023, 1079.40 sec so far
Iteration 5724: max relative diff=0.000023, 1084.52 sec so far
Iteration 5751: max relative diff=0.000023, 1089.63 sec so far
Iteration 5778: max relative diff=0.000023, 1094.74 sec so far
Iteration 5805: max relative diff=0.000023, 1099.86 sec so far
Iteration 5832: max relative diff=0.000023, 1104.98 sec so far
Iteration 5859: max relative diff=0.000023, 1110.10 sec so far
Iteration 5886: max relative diff=0.000023, 1115.21 sec so far
Iteration 5913: max relative diff=0.000023, 1120.32 sec so far
Iteration 5940: max relative diff=0.000023, 1125.43 sec so far
Iteration 5967: max relative diff=0.000023, 1130.54 sec so far
Iteration 5994: max relative diff=0.000023, 1135.65 sec so far
Iteration 6021: max relative diff=0.000023, 1140.76 sec so far
Iteration 6048: max relative diff=0.000023, 1145.87 sec so far
Iteration 6075: max relative diff=0.000023, 1151.00 sec so far
Iteration 6102: max relative diff=0.000023, 1156.11 sec so far
Iteration 6129: max relative diff=0.000023, 1161.23 sec so far
Iteration 6156: max relative diff=0.000023, 1166.35 sec so far
Iteration 6183: max relative diff=0.000023, 1171.47 sec so far
Iteration 6210: max relative diff=0.000023, 1176.58 sec so far
Iteration 6237: max relative diff=0.000023, 1181.71 sec so far
Iteration 6264: max relative diff=0.000023, 1186.83 sec so far
Iteration 6291: max relative diff=0.000023, 1191.94 sec so far
Iteration 6318: max relative diff=0.000023, 1197.07 sec so far
Iteration 6345: max relative diff=0.000023, 1202.18 sec so far
Iteration 6372: max relative diff=0.000023, 1207.30 sec so far
Iteration 6399: max relative diff=0.000023, 1212.42 sec so far
Iteration 6426: max relative diff=0.000023, 1217.52 sec so far
Iteration 6453: max relative diff=0.000023, 1222.64 sec so far
Iteration 6480: max relative diff=0.000023, 1227.76 sec so far
Iteration 6507: max relative diff=0.000023, 1232.87 sec so far
Iteration 6534: max relative diff=0.000023, 1237.99 sec so far
Iteration 6561: max relative diff=0.000023, 1243.11 sec so far
Iteration 6588: max relative diff=0.000023, 1248.23 sec so far
Iteration 6615: max relative diff=0.000023, 1253.34 sec so far
Iteration 6642: max relative diff=0.000023, 1258.46 sec so far
Iteration 6669: max relative diff=0.000023, 1263.57 sec so far
Iteration 6696: max relative diff=0.000023, 1268.69 sec so far
Iteration 6723: max relative diff=0.000023, 1273.82 sec so far
Iteration 6750: max relative diff=0.000023, 1278.94 sec so far
Iteration 6777: max relative diff=0.000023, 1284.06 sec so far
Iteration 6804: max relative diff=0.000023, 1289.18 sec so far
Iteration 6831: max relative diff=0.000023, 1294.31 sec so far
Iteration 6858: max relative diff=0.000023, 1299.42 sec so far
Iteration 6885: max relative diff=0.000023, 1304.55 sec so far
Iteration 6912: max relative diff=0.000023, 1309.66 sec so far
Iteration 6939: max relative diff=0.000023, 1314.79 sec so far
Iteration 6966: max relative diff=0.000023, 1319.90 sec so far
Iteration 6993: max relative diff=0.000023, 1325.02 sec so far
Iteration 7020: max relative diff=0.000023, 1330.14 sec so far
Iteration 7047: max relative diff=0.000023, 1335.26 sec so far
Iteration 7074: max relative diff=0.000023, 1340.38 sec so far
Iteration 7101: max relative diff=0.000023, 1345.51 sec so far
Iteration 7128: max relative diff=0.000023, 1350.63 sec so far
Iteration 7155: max relative diff=0.000023, 1355.75 sec so far
Iteration 7182: max relative diff=0.000023, 1360.87 sec so far
Iteration 7209: max relative diff=0.000023, 1365.99 sec so far
Iteration 7236: max relative diff=0.000023, 1371.12 sec so far
Iteration 7263: max relative diff=0.000023, 1376.24 sec so far
Iteration 7290: max relative diff=0.000023, 1381.37 sec so far
Iteration 7317: max relative diff=0.000023, 1386.49 sec so far
Iteration 7344: max relative diff=0.000023, 1391.61 sec so far
Iteration 7371: max relative diff=0.000023, 1396.74 sec so far
Iteration 7398: max relative diff=0.000023, 1401.86 sec so far
Iteration 7425: max relative diff=0.000023, 1407.00 sec so far
Iteration 7452: max relative diff=0.000023, 1412.13 sec so far
Iteration 7479: max relative diff=0.000023, 1417.25 sec so far
Iteration 7506: max relative diff=0.000023, 1422.37 sec so far
Iteration 7533: max relative diff=0.000023, 1427.49 sec so far
Iteration 7560: max relative diff=0.000023, 1432.62 sec so far
Iteration 7587: max relative diff=0.000023, 1437.74 sec so far
Iteration 7614: max relative diff=0.000023, 1442.86 sec so far
Iteration 7641: max relative diff=0.000023, 1447.97 sec so far
Iteration 7668: max relative diff=0.000023, 1453.09 sec so far
Iteration 7695: max relative diff=0.000023, 1458.22 sec so far
Iteration 7722: max relative diff=0.000023, 1463.34 sec so far
Iteration 7749: max relative diff=0.000023, 1468.46 sec so far
Iteration 7776: max relative diff=0.000023, 1473.59 sec so far
Iteration 7803: max relative diff=0.000023, 1478.70 sec so far
Iteration 7830: max relative diff=0.000023, 1483.82 sec so far
Iteration 7857: max relative diff=0.000023, 1488.94 sec so far
Iteration 7884: max relative diff=0.000023, 1494.07 sec so far
Iteration 7911: max relative diff=0.000023, 1499.17 sec so far
Iteration 7938: max relative diff=0.000023, 1504.29 sec so far
Iteration 7965: max relative diff=0.000023, 1509.41 sec so far
Iteration 7992: max relative diff=0.000023, 1514.53 sec so far
Iteration 8019: max relative diff=0.000023, 1519.64 sec so far
Iteration 8046: max relative diff=0.000023, 1524.77 sec so far
Iteration 8073: max relative diff=0.000023, 1529.88 sec so far
Iteration 8100: max relative diff=0.000023, 1535.00 sec so far
Iteration 8127: max relative diff=0.000023, 1540.11 sec so far
Iteration 8154: max relative diff=0.000023, 1545.24 sec so far
Iteration 8181: max relative diff=0.000023, 1550.36 sec so far
Iteration 8208: max relative diff=0.000023, 1555.48 sec so far
Iteration 8235: max relative diff=0.000023, 1560.60 sec so far
Iteration 8262: max relative diff=0.000023, 1565.72 sec so far
Iteration 8289: max relative diff=0.000023, 1570.83 sec so far
Iteration 8316: max relative diff=0.000023, 1575.96 sec so far
Iteration 8343: max relative diff=0.000023, 1581.08 sec so far
Iteration 8370: max relative diff=0.000023, 1586.19 sec so far
Iteration 8397: max relative diff=0.000023, 1591.32 sec so far
Iteration 8424: max relative diff=0.000023, 1596.43 sec so far
Iteration 8451: max relative diff=0.000023, 1601.55 sec so far
Iteration 8478: max relative diff=0.000023, 1606.66 sec so far
Iteration 8505: max relative diff=0.000023, 1611.79 sec so far
Iteration 8532: max relative diff=0.000023, 1616.90 sec so far
Iteration 8559: max relative diff=0.000023, 1622.02 sec so far
Iteration 8586: max relative diff=0.000023, 1627.15 sec so far
Iteration 8613: max relative diff=0.000023, 1632.26 sec so far
Iteration 8640: max relative diff=0.000023, 1637.39 sec so far
Iteration 8667: max relative diff=0.000023, 1642.50 sec so far
Iteration 8694: max relative diff=0.000023, 1647.62 sec so far
Iteration 8721: max relative diff=0.000023, 1652.74 sec so far
Iteration 8748: max relative diff=0.000023, 1657.86 sec so far
Iteration 8775: max relative diff=0.000023, 1662.98 sec so far
Iteration 8802: max relative diff=0.000023, 1668.10 sec so far
Iteration 8829: max relative diff=0.000023, 1673.21 sec so far
Iteration 8856: max relative diff=0.000023, 1678.33 sec so far
Iteration 8883: max relative diff=0.000023, 1683.44 sec so far
Iteration 8910: max relative diff=0.000023, 1688.56 sec so far
Iteration 8937: max relative diff=0.000023, 1693.67 sec so far
Iteration 8964: max relative diff=0.000023, 1698.78 sec so far
Iteration 8991: max relative diff=0.000023, 1703.91 sec so far
Iteration 9018: max relative diff=0.000023, 1709.02 sec so far
Iteration 9045: max relative diff=0.000023, 1714.13 sec so far
Iteration 9072: max relative diff=0.000023, 1719.25 sec so far
Iteration 9099: max relative diff=0.000023, 1724.38 sec so far
Iteration 9126: max relative diff=0.000023, 1729.49 sec so far
Iteration 9153: max relative diff=0.000023, 1734.61 sec so far
Iteration 9180: max relative diff=0.000023, 1739.74 sec so far
Iteration 9207: max relative diff=0.000023, 1744.85 sec so far
Iteration 9234: max relative diff=0.000023, 1749.97 sec so far
Iteration 9261: max relative diff=0.000023, 1755.09 sec so far
Iteration 9288: max relative diff=0.000023, 1760.21 sec so far
Iteration 9315: max relative diff=0.000023, 1765.33 sec so far
Iteration 9342: max relative diff=0.000023, 1770.45 sec so far
Iteration 9369: max relative diff=0.000023, 1775.58 sec so far
Iteration 9396: max relative diff=0.000023, 1780.69 sec so far
Iteration 9423: max relative diff=0.000023, 1785.81 sec so far
Iteration 9450: max relative diff=0.000023, 1790.92 sec so far
Iteration 9477: max relative diff=0.000023, 1796.04 sec so far
Iteration 9504: max relative diff=0.000023, 1801.15 sec so far
Iteration 9531: max relative diff=0.000023, 1806.27 sec so far
Iteration 9558: max relative diff=0.000023, 1811.40 sec so far
Iteration 9585: max relative diff=0.000023, 1816.52 sec so far
Iteration 9612: max relative diff=0.000023, 1821.64 sec so far
Iteration 9639: max relative diff=0.000023, 1826.77 sec so far
Iteration 9666: max relative diff=0.000023, 1831.88 sec so far
Iteration 9693: max relative diff=0.000023, 1837.01 sec so far
Iteration 9720: max relative diff=0.000023, 1842.13 sec so far
Iteration 9747: max relative diff=0.000023, 1847.26 sec so far
Iteration 9774: max relative diff=0.000023, 1852.38 sec so far
Iteration 9801: max relative diff=0.000023, 1857.50 sec so far
Iteration 9828: max relative diff=0.000023, 1862.62 sec so far
Iteration 9855: max relative diff=0.000023, 1867.75 sec so far
Iteration 9882: max relative diff=0.000023, 1872.85 sec so far
Iteration 9909: max relative diff=0.000023, 1877.97 sec so far
Iteration 9936: max relative diff=0.000023, 1883.08 sec so far
Iteration 9963: max relative diff=0.000023, 1888.19 sec so far
Iteration 9990: max relative diff=0.000023, 1893.32 sec so far

Jacobi: 10000 iterations in 1896.58 seconds (average 0.189521, setup 1.37)

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_kanban.5_rep2.log

```
Command(s):
../bin/prism  models/kanban.5/model.prism models/kanban.5/property.props
Wallclock time: 474.520 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:24:33 GMT+01:00 2026
Hostname: n23m0133.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/kanban.5/model.prism models/kanban.5/property.props

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Parsing properties file "models/kanban.5/property.props"...

1 property:
(1) "throughput": R{"throughput"}=? [ S ]

---------------------------------------------------------------------

Model checking: "throughput": R{"throughput"}=? [ S ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 71 iterations in 0.09 seconds (average 0.001268, setup 0.00)

Time for model construction: 0.132 seconds.

Type:        CTMC
States:      2546432 (1 initial)
Transitions: 24460016

Rate matrix: 6308 nodes (14 terminal), 24460016 minterms, vars: 48r/48c

SCCs: 1, BSCCs: 1, non-BSCC states: 0
BSCC sizes: 1:2546432

Computing steady state probabilities for BSCC 1

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=48, nodes=6308] [295.7 KB]
Adding explicit sparse matrices... [levels=27, num=165, compact] [749.6 KB]
Creating vector for diagonals... [dist=187, compact] [4.9 MB]
Allocating iteration vectors... [2 x 19.4 MB]
TOTAL: [44.7 MB]

Starting iterations...
Iteration 117: max relative diff=0.012589, 5.01 sec so far
Iteration 234: max relative diff=0.001080, 10.03 sec so far
Iteration 352: max relative diff=0.000136, 15.05 sec so far
Iteration 470: max relative diff=0.000035, 20.08 sec so far
Iteration 588: max relative diff=0.000025, 25.10 sec so far
Iteration 706: max relative diff=0.000023, 30.11 sec so far
Iteration 827: max relative diff=0.000023, 35.12 sec so far
Iteration 948: max relative diff=0.000023, 40.13 sec so far
Iteration 1070: max relative diff=0.000023, 45.15 sec so far
Iteration 1192: max relative diff=0.000023, 50.18 sec so far
Iteration 1314: max relative diff=0.000023, 55.21 sec so far
Iteration 1436: max relative diff=0.000023, 60.24 sec so far
Iteration 1558: max relative diff=0.000023, 65.27 sec so far
Iteration 1680: max relative diff=0.000023, 70.29 sec so far
Iteration 1802: max relative diff=0.000023, 75.32 sec so far
Iteration 1924: max relative diff=0.000023, 80.35 sec so far
Iteration 2046: max relative diff=0.000023, 85.38 sec so far
Iteration 2167: max relative diff=0.000023, 90.41 sec so far
Iteration 2288: max relative diff=0.000023, 95.43 sec so far
Iteration 2410: max relative diff=0.000023, 100.47 sec so far
Iteration 2532: max relative diff=0.000023, 105.49 sec so far
Iteration 2654: max relative diff=0.000023, 110.52 sec so far
Iteration 2776: max relative diff=0.000023, 115.55 sec so far
Iteration 2898: max relative diff=0.000023, 120.57 sec so far
Iteration 3020: max relative diff=0.000023, 125.61 sec so far
Iteration 3142: max relative diff=0.000023, 130.64 sec so far
Iteration 3264: max relative diff=0.000023, 135.66 sec so far
Iteration 3386: max relative diff=0.000023, 140.68 sec so far
Iteration 3508: max relative diff=0.000023, 145.72 sec so far
Iteration 3621: max relative diff=0.000023, 150.76 sec so far
Iteration 3738: max relative diff=0.000023, 155.78 sec so far
Iteration 3848: max relative diff=0.000023, 160.83 sec so far
Iteration 3965: max relative diff=0.000023, 165.85 sec so far
Iteration 4082: max relative diff=0.000023, 170.90 sec so far
Iteration 4199: max relative diff=0.000023, 175.91 sec so far
Iteration 4316: max relative diff=0.000023, 180.94 sec so far
Iteration 4433: max relative diff=0.000023, 185.97 sec so far
Iteration 4550: max relative diff=0.000023, 191.00 sec so far
Iteration 4667: max relative diff=0.000023, 196.02 sec so far
Iteration 4784: max relative diff=0.000023, 201.05 sec so far
Iteration 4900: max relative diff=0.000023, 206.06 sec so far
Iteration 5014: max relative diff=0.000023, 211.08 sec so far
Iteration 5130: max relative diff=0.000023, 216.11 sec so far
Iteration 5230: max relative diff=0.000023, 221.15 sec so far
Iteration 5324: max relative diff=0.000023, 226.18 sec so far
Iteration 5418: max relative diff=0.000023, 231.22 sec so far
Iteration 5512: max relative diff=0.000023, 236.24 sec so far
Iteration 5606: max relative diff=0.000023, 241.27 sec so far
Iteration 5700: max relative diff=0.000023, 246.30 sec so far
Iteration 5794: max relative diff=0.000023, 251.32 sec so far
Iteration 5888: max relative diff=0.000023, 256.35 sec so far
Iteration 5982: max relative diff=0.000023, 261.37 sec so far
Iteration 6076: max relative diff=0.000023, 266.41 sec so far
Iteration 6170: max relative diff=0.000023, 271.43 sec so far
Iteration 6264: max relative diff=0.000023, 276.45 sec so far
Iteration 6367: max relative diff=0.000023, 281.51 sec so far
Iteration 6460: max relative diff=0.000023, 286.54 sec so far
Iteration 6557: max relative diff=0.000023, 291.58 sec so far
Iteration 6654: max relative diff=0.000023, 296.63 sec so far
Iteration 6751: max relative diff=0.000023, 301.68 sec so far
Iteration 6847: max relative diff=0.000023, 306.69 sec so far
Iteration 6944: max relative diff=0.000023, 311.73 sec so far
Iteration 7040: max relative diff=0.000023, 316.74 sec so far
Iteration 7137: max relative diff=0.000023, 321.78 sec so far
Iteration 7231: max relative diff=0.000023, 326.80 sec so far
Iteration 7328: max relative diff=0.000023, 331.85 sec so far
Iteration 7424: max relative diff=0.000023, 336.87 sec so far
Iteration 7521: max relative diff=0.000023, 341.93 sec so far
Iteration 7617: max relative diff=0.000023, 346.94 sec so far
Iteration 7713: max relative diff=0.000023, 351.96 sec so far
Iteration 7810: max relative diff=0.000023, 357.01 sec so far
Iteration 7907: max relative diff=0.000023, 362.06 sec so far
Iteration 8004: max relative diff=0.000023, 367.10 sec so far
Iteration 8101: max relative diff=0.000023, 372.13 sec so far
Iteration 8198: max relative diff=0.000023, 377.17 sec so far
Iteration 8294: max relative diff=0.000023, 382.20 sec so far
Iteration 8389: max relative diff=0.000023, 387.21 sec so far
Iteration 8486: max relative diff=0.000023, 392.26 sec so far
Iteration 8582: max relative diff=0.000023, 397.27 sec so far
Iteration 8679: max relative diff=0.000023, 402.32 sec so far
Iteration 8776: max relative diff=0.000023, 407.36 sec so far
Iteration 8873: max relative diff=0.000023, 412.38 sec so far
Iteration 8969: max relative diff=0.000023, 417.42 sec so far
Iteration 9066: max relative diff=0.000023, 422.47 sec so far
Iteration 9163: max relative diff=0.000023, 427.52 sec so far
Iteration 9260: max relative diff=0.000023, 432.57 sec so far
Iteration 9357: max relative diff=0.000023, 437.62 sec so far
Iteration 9453: max relative diff=0.000023, 442.63 sec so far
Iteration 9548: max relative diff=0.000023, 447.66 sec so far
Iteration 9644: max relative diff=0.000023, 452.68 sec so far
Iteration 9740: max relative diff=0.000023, 457.69 sec so far
Iteration 9836: max relative diff=0.000023, 462.71 sec so far
Iteration 9933: max relative diff=0.000023, 467.76 sec so far

Jacobi: 10000 iterations in 471.54 seconds (average 0.047126, setup 0.28)

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_kanban.5_rep3.log

```
Command(s):
../bin/prism  models/kanban.5/model.prism models/kanban.5/property.props
Wallclock time: 434.574 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:08:18 GMT+01:00 2026
Hostname: r23m0214.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/kanban.5/model.prism models/kanban.5/property.props

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Parsing properties file "models/kanban.5/property.props"...

1 property:
(1) "throughput": R{"throughput"}=? [ S ]

---------------------------------------------------------------------

Model checking: "throughput": R{"throughput"}=? [ S ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 71 iterations in 0.10 seconds (average 0.001408, setup 0.00)

Time for model construction: 0.121 seconds.

Type:        CTMC
States:      2546432 (1 initial)
Transitions: 24460016

Rate matrix: 6308 nodes (14 terminal), 24460016 minterms, vars: 48r/48c

SCCs: 1, BSCCs: 1, non-BSCC states: 0
BSCC sizes: 1:2546432

Computing steady state probabilities for BSCC 1

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=48, nodes=6308] [295.7 KB]
Adding explicit sparse matrices... [levels=27, num=165, compact] [749.6 KB]
Creating vector for diagonals... [dist=187, compact] [4.9 MB]
Allocating iteration vectors... [2 x 19.4 MB]
TOTAL: [44.7 MB]

Starting iterations...
Iteration 118: max relative diff=0.012221, 5.01 sec so far
Iteration 237: max relative diff=0.001027, 10.04 sec so far
Iteration 356: max relative diff=0.000127, 15.05 sec so far
Iteration 475: max relative diff=0.000034, 20.06 sec so far
Iteration 594: max relative diff=0.000024, 25.08 sec so far
Iteration 709: max relative diff=0.000023, 30.12 sec so far
Iteration 830: max relative diff=0.000023, 35.14 sec so far
Iteration 950: max relative diff=0.000023, 40.17 sec so far
Iteration 1067: max relative diff=0.000023, 45.21 sec so far
Iteration 1185: max relative diff=0.000023, 50.22 sec so far
Iteration 1303: max relative diff=0.000023, 55.25 sec so far
Iteration 1421: max relative diff=0.000023, 60.26 sec so far
Iteration 1539: max relative diff=0.000023, 65.27 sec so far
Iteration 1657: max relative diff=0.000023, 70.28 sec so far
Iteration 1775: max relative diff=0.000023, 75.29 sec so far
Iteration 1893: max relative diff=0.000023, 80.31 sec so far
Iteration 2011: max relative diff=0.000023, 85.32 sec so far
Iteration 2129: max relative diff=0.000023, 90.34 sec so far
Iteration 2248: max relative diff=0.000023, 95.38 sec so far
Iteration 2366: max relative diff=0.000023, 100.41 sec so far
Iteration 2483: max relative diff=0.000023, 105.42 sec so far
Iteration 2600: max relative diff=0.000023, 110.45 sec so far
Iteration 2717: max relative diff=0.000023, 115.50 sec so far
Iteration 2834: max relative diff=0.000023, 120.51 sec so far
Iteration 2950: max relative diff=0.000023, 125.54 sec so far
Iteration 3068: max relative diff=0.000023, 130.58 sec so far
Iteration 3186: max relative diff=0.000023, 135.60 sec so far
Iteration 3304: max relative diff=0.000023, 140.62 sec so far
Iteration 3422: max relative diff=0.000023, 145.64 sec so far
Iteration 3540: max relative diff=0.000023, 150.67 sec so far
Iteration 3658: max relative diff=0.000023, 155.71 sec so far
Iteration 3774: max relative diff=0.000023, 160.75 sec so far
Iteration 3891: max relative diff=0.000023, 165.78 sec so far
Iteration 4008: max relative diff=0.000023, 170.82 sec so far
Iteration 4126: max relative diff=0.000023, 175.85 sec so far
Iteration 4243: max relative diff=0.000023, 180.87 sec so far
Iteration 4358: max relative diff=0.000023, 185.89 sec so far
Iteration 4475: max relative diff=0.000023, 190.94 sec so far
Iteration 4592: max relative diff=0.000023, 195.97 sec so far
Iteration 4708: max relative diff=0.000023, 200.98 sec so far
Iteration 4825: max relative diff=0.000023, 206.01 sec so far
Iteration 4942: max relative diff=0.000023, 211.02 sec so far
Iteration 5059: max relative diff=0.000023, 216.07 sec so far
Iteration 5172: max relative diff=0.000023, 221.08 sec so far
Iteration 5288: max relative diff=0.000023, 226.10 sec so far
Iteration 5406: max relative diff=0.000023, 231.13 sec so far
Iteration 5525: max relative diff=0.000023, 236.17 sec so far
Iteration 5642: max relative diff=0.000023, 241.21 sec so far
Iteration 5759: max relative diff=0.000023, 246.26 sec so far
Iteration 5878: max relative diff=0.000023, 251.31 sec so far
Iteration 5997: max relative diff=0.000023, 256.35 sec so far
Iteration 6116: max relative diff=0.000023, 261.37 sec so far
Iteration 6235: max relative diff=0.000023, 266.42 sec so far
Iteration 6353: max relative diff=0.000023, 271.45 sec so far
Iteration 6469: max relative diff=0.000023, 276.49 sec so far
Iteration 6585: max relative diff=0.000023, 281.53 sec so far
Iteration 6703: max relative diff=0.000023, 286.56 sec so far
Iteration 6820: max relative diff=0.000023, 291.57 sec so far
Iteration 6938: max relative diff=0.000023, 296.59 sec so far
Iteration 7054: max relative diff=0.000023, 301.62 sec so far
Iteration 7170: max relative diff=0.000023, 306.66 sec so far
Iteration 7287: max relative diff=0.000023, 311.69 sec so far
Iteration 7405: max relative diff=0.000023, 316.70 sec so far
Iteration 7524: max relative diff=0.000023, 321.73 sec so far
Iteration 7642: max relative diff=0.000023, 326.77 sec so far
Iteration 7758: max relative diff=0.000023, 331.80 sec so far
Iteration 7870: max relative diff=0.000023, 336.85 sec so far
Iteration 7983: max relative diff=0.000023, 341.88 sec so far
Iteration 8097: max relative diff=0.000023, 346.89 sec so far
Iteration 8210: max relative diff=0.000023, 351.92 sec so far
Iteration 8323: max relative diff=0.000023, 356.95 sec so far
Iteration 8436: max relative diff=0.000023, 361.97 sec so far
Iteration 8550: max relative diff=0.000023, 366.98 sec so far
Iteration 8662: max relative diff=0.000023, 372.01 sec so far
Iteration 8773: max relative diff=0.000023, 377.04 sec so far
Iteration 8888: max relative diff=0.000023, 382.05 sec so far
Iteration 9003: max relative diff=0.000023, 387.10 sec so far
Iteration 9113: max relative diff=0.000023, 392.11 sec so far
Iteration 9225: max relative diff=0.000023, 397.13 sec so far
Iteration 9338: max relative diff=0.000023, 402.17 sec so far
Iteration 9452: max relative diff=0.000023, 407.19 sec so far
Iteration 9564: max relative diff=0.000023, 412.21 sec so far
Iteration 9678: max relative diff=0.000023, 417.23 sec so far
Iteration 9790: max relative diff=0.000023, 422.26 sec so far
Iteration 9899: max relative diff=0.000023, 427.28 sec so far

Jacobi: 10000 iterations in 432.24 seconds (average 0.043194, setup 0.30)

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_kanban.5_rep4.log

```
Command(s):
../bin/prism  models/kanban.5/model.prism models/kanban.5/property.props
Wallclock time: 515.663 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:49:56 GMT+01:00 2026
Hostname: n23m0388.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/kanban.5/model.prism models/kanban.5/property.props

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Parsing properties file "models/kanban.5/property.props"...

1 property:
(1) "throughput": R{"throughput"}=? [ S ]

---------------------------------------------------------------------

Model checking: "throughput": R{"throughput"}=? [ S ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 71 iterations in 0.13 seconds (average 0.001831, setup 0.00)

Time for model construction: 0.298 seconds.

Type:        CTMC
States:      2546432 (1 initial)
Transitions: 24460016

Rate matrix: 6308 nodes (14 terminal), 24460016 minterms, vars: 48r/48c

SCCs: 1, BSCCs: 1, non-BSCC states: 0
BSCC sizes: 1:2546432

Computing steady state probabilities for BSCC 1

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=48, nodes=6308] [295.7 KB]
Adding explicit sparse matrices... [levels=27, num=165, compact] [749.6 KB]
Creating vector for diagonals... [dist=187, compact] [4.9 MB]
Allocating iteration vectors... [2 x 19.4 MB]
TOTAL: [44.7 MB]

Starting iterations...
Iteration 97: max relative diff=0.023718, 5.04 sec so far
Iteration 195: max relative diff=0.002138, 10.07 sec so far
Iteration 293: max relative diff=0.000373, 15.08 sec so far
Iteration 392: max relative diff=0.000075, 20.13 sec so far
Iteration 491: max relative diff=0.000031, 25.15 sec so far
Iteration 589: max relative diff=0.000024, 30.16 sec so far
Iteration 688: max relative diff=0.000023, 35.21 sec so far
Iteration 787: max relative diff=0.000023, 40.25 sec so far
Iteration 885: max relative diff=0.000023, 45.26 sec so far
Iteration 984: max relative diff=0.000023, 50.28 sec so far
Iteration 1083: max relative diff=0.000023, 55.32 sec so far
Iteration 1182: max relative diff=0.000023, 60.36 sec so far
Iteration 1278: max relative diff=0.000023, 65.38 sec so far
Iteration 1376: max relative diff=0.000023, 70.39 sec so far
Iteration 1474: max relative diff=0.000023, 75.41 sec so far
Iteration 1573: max relative diff=0.000023, 80.44 sec so far
Iteration 1672: max relative diff=0.000023, 85.48 sec so far
Iteration 1771: max relative diff=0.000023, 90.53 sec so far
Iteration 1870: max relative diff=0.000023, 95.55 sec so far
Iteration 1969: max relative diff=0.000023, 100.60 sec so far
Iteration 2067: max relative diff=0.000023, 105.62 sec so far
Iteration 2165: max relative diff=0.000023, 110.64 sec so far
Iteration 2264: max relative diff=0.000023, 115.67 sec so far
Iteration 2363: max relative diff=0.000023, 120.70 sec so far
Iteration 2459: max relative diff=0.000023, 125.72 sec so far
Iteration 2558: max relative diff=0.000023, 130.77 sec so far
Iteration 2656: max relative diff=0.000023, 135.79 sec so far
Iteration 2755: max relative diff=0.000023, 140.84 sec so far
Iteration 2854: max relative diff=0.000023, 145.88 sec so far
Iteration 2952: max relative diff=0.000023, 150.89 sec so far
Iteration 3051: max relative diff=0.000023, 155.92 sec so far
Iteration 3150: max relative diff=0.000023, 160.97 sec so far
Iteration 3249: max relative diff=0.000023, 166.02 sec so far
Iteration 3348: max relative diff=0.000023, 171.04 sec so far
Iteration 3446: max relative diff=0.000023, 176.06 sec so far
Iteration 3545: max relative diff=0.000023, 181.10 sec so far
Iteration 3642: max relative diff=0.000023, 186.16 sec so far
Iteration 3740: max relative diff=0.000023, 191.17 sec so far
Iteration 3838: max relative diff=0.000023, 196.19 sec so far
Iteration 3937: max relative diff=0.000023, 201.22 sec so far
Iteration 4036: max relative diff=0.000023, 206.27 sec so far
Iteration 4135: max relative diff=0.000023, 211.30 sec so far
Iteration 4234: max relative diff=0.000023, 216.35 sec so far
Iteration 4333: max relative diff=0.000023, 221.40 sec so far
Iteration 4432: max relative diff=0.000023, 226.43 sec so far
Iteration 4531: max relative diff=0.000023, 231.49 sec so far
Iteration 4630: max relative diff=0.000023, 236.51 sec so far
Iteration 4729: max relative diff=0.000023, 241.56 sec so far
Iteration 4825: max relative diff=0.000023, 246.57 sec so far
Iteration 4923: max relative diff=0.000023, 251.59 sec so far
Iteration 5021: max relative diff=0.000023, 256.60 sec so far
Iteration 5120: max relative diff=0.000023, 261.64 sec so far
Iteration 5218: max relative diff=0.000023, 266.65 sec so far
Iteration 5317: max relative diff=0.000023, 271.69 sec so far
Iteration 5416: max relative diff=0.000023, 276.74 sec so far
Iteration 5515: max relative diff=0.000023, 281.78 sec so far
Iteration 5614: max relative diff=0.000023, 286.81 sec so far
Iteration 5713: max relative diff=0.000023, 291.86 sec so far
Iteration 5812: max relative diff=0.000023, 296.90 sec so far
Iteration 5910: max relative diff=0.000023, 301.94 sec so far
Iteration 6007: max relative diff=0.000023, 306.99 sec so far
Iteration 6105: max relative diff=0.000023, 312.03 sec so far
Iteration 6204: max relative diff=0.000023, 317.07 sec so far
Iteration 6302: max relative diff=0.000023, 322.08 sec so far
Iteration 6401: max relative diff=0.000023, 327.13 sec so far
Iteration 6500: max relative diff=0.000023, 332.17 sec so far
Iteration 6598: max relative diff=0.000023, 337.18 sec so far
Iteration 6697: max relative diff=0.000023, 342.21 sec so far
Iteration 6796: max relative diff=0.000023, 347.26 sec so far
Iteration 6895: max relative diff=0.000023, 352.31 sec so far
Iteration 6994: max relative diff=0.000023, 357.34 sec so far
Iteration 7092: max relative diff=0.000023, 362.40 sec so far
Iteration 7189: max relative diff=0.000023, 367.42 sec so far
Iteration 7287: max relative diff=0.000023, 372.46 sec so far
Iteration 7385: max relative diff=0.000023, 377.47 sec so far
Iteration 7483: max relative diff=0.000023, 382.48 sec so far
Iteration 7582: max relative diff=0.000023, 387.53 sec so far
Iteration 7680: max relative diff=0.000023, 392.54 sec so far
Iteration 7778: max relative diff=0.000023, 397.55 sec so far
Iteration 7877: max relative diff=0.000023, 402.58 sec so far
Iteration 7975: max relative diff=0.000023, 407.60 sec so far
Iteration 8074: max relative diff=0.000023, 412.65 sec so far
Iteration 8172: max relative diff=0.000023, 417.66 sec so far
Iteration 8269: max relative diff=0.000023, 422.69 sec so far
Iteration 8367: max relative diff=0.000023, 427.71 sec so far
Iteration 8465: max relative diff=0.000023, 432.73 sec so far
Iteration 8564: max relative diff=0.000023, 437.77 sec so far
Iteration 8663: max relative diff=0.000023, 442.81 sec so far
Iteration 8761: max relative diff=0.000023, 447.83 sec so far
Iteration 8859: max relative diff=0.000023, 452.84 sec so far
Iteration 8958: max relative diff=0.000023, 457.87 sec so far
Iteration 9057: max relative diff=0.000023, 462.93 sec so far
Iteration 9156: max relative diff=0.000023, 467.97 sec so far
Iteration 9254: max relative diff=0.000023, 472.99 sec so far
Iteration 9353: max relative diff=0.000023, 478.05 sec so far
Iteration 9449: max relative diff=0.000023, 483.07 sec so far
Iteration 9548: max relative diff=0.000023, 488.11 sec so far
Iteration 9646: max relative diff=0.000023, 493.12 sec so far
Iteration 9744: max relative diff=0.000023, 498.13 sec so far
Iteration 9843: max relative diff=0.000023, 503.17 sec so far
Iteration 9942: max relative diff=0.000023, 508.21 sec so far

Jacobi: 10000 iterations in 511.49 seconds (average 0.051118, setup 0.31)

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_kanban.5_rep5.log

```
Command(s):
../bin/prism  models/kanban.5/model.prism models/kanban.5/property.props
Wallclock time: 548.967 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:51:58 GMT+01:00 2026
Hostname: r23m0211.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/kanban.5/model.prism models/kanban.5/property.props

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Parsing properties file "models/kanban.5/property.props"...

1 property:
(1) "throughput": R{"throughput"}=? [ S ]

---------------------------------------------------------------------

Model checking: "throughput": R{"throughput"}=? [ S ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 71 iterations in 0.14 seconds (average 0.001972, setup 0.00)

Time for model construction: 0.167 seconds.

Type:        CTMC
States:      2546432 (1 initial)
Transitions: 24460016

Rate matrix: 6308 nodes (14 terminal), 24460016 minterms, vars: 48r/48c

SCCs: 1, BSCCs: 1, non-BSCC states: 0
BSCC sizes: 1:2546432

Computing steady state probabilities for BSCC 1

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=48, nodes=6308] [295.7 KB]
Adding explicit sparse matrices... [levels=27, num=165, compact] [749.6 KB]
Creating vector for diagonals... [dist=187, compact] [4.9 MB]
Allocating iteration vectors... [2 x 19.4 MB]
TOTAL: [44.7 MB]

Starting iterations...
Iteration 90: max relative diff=0.029110, 5.05 sec so far
Iteration 181: max relative diff=0.002693, 10.06 sec so far
Iteration 273: max relative diff=0.000535, 15.07 sec so far
Iteration 367: max relative diff=0.000108, 20.11 sec so far
Iteration 465: max relative diff=0.000036, 25.13 sec so far
Iteration 563: max relative diff=0.000025, 30.16 sec so far
Iteration 660: max relative diff=0.000024, 35.20 sec so far
Iteration 759: max relative diff=0.000023, 40.22 sec so far
Iteration 858: max relative diff=0.000023, 45.26 sec so far
Iteration 957: max relative diff=0.000023, 50.28 sec so far
Iteration 1053: max relative diff=0.000023, 55.30 sec so far
Iteration 1155: max relative diff=0.000023, 60.31 sec so far
Iteration 1242: max relative diff=0.000023, 65.33 sec so far
Iteration 1334: max relative diff=0.000023, 70.39 sec so far
Iteration 1426: max relative diff=0.000023, 75.45 sec so far
Iteration 1518: max relative diff=0.000023, 80.48 sec so far
Iteration 1610: max relative diff=0.000023, 85.52 sec so far
Iteration 1703: max relative diff=0.000023, 90.56 sec so far
Iteration 1795: max relative diff=0.000023, 95.59 sec so far
Iteration 1887: max relative diff=0.000023, 100.61 sec so far
Iteration 1979: max relative diff=0.000023, 105.62 sec so far
Iteration 2071: max relative diff=0.000023, 110.66 sec so far
Iteration 2163: max relative diff=0.000023, 115.69 sec so far
Iteration 2254: max relative diff=0.000023, 120.73 sec so far
Iteration 2345: max relative diff=0.000023, 125.75 sec so far
Iteration 2436: max relative diff=0.000023, 130.79 sec so far
Iteration 2528: max relative diff=0.000023, 135.83 sec so far
Iteration 2620: max relative diff=0.000023, 140.87 sec so far
Iteration 2712: max relative diff=0.000023, 145.88 sec so far
Iteration 2804: max relative diff=0.000023, 150.91 sec so far
Iteration 2896: max relative diff=0.000023, 155.96 sec so far
Iteration 2988: max relative diff=0.000023, 160.97 sec so far
Iteration 3080: max relative diff=0.000023, 166.00 sec so far
Iteration 3171: max relative diff=0.000023, 171.01 sec so far
Iteration 3262: max relative diff=0.000023, 176.03 sec so far
Iteration 3351: max relative diff=0.000023, 181.04 sec so far
Iteration 3443: max relative diff=0.000023, 186.10 sec so far
Iteration 3535: max relative diff=0.000023, 191.14 sec so far
Iteration 3627: max relative diff=0.000023, 196.15 sec so far
Iteration 3719: max relative diff=0.000023, 201.17 sec so far
Iteration 3811: max relative diff=0.000023, 206.19 sec so far
Iteration 3903: max relative diff=0.000023, 211.24 sec so far
Iteration 3995: max relative diff=0.000023, 216.27 sec so far
Iteration 4087: max relative diff=0.000023, 221.30 sec so far
Iteration 4179: max relative diff=0.000023, 226.33 sec so far
Iteration 4271: max relative diff=0.000023, 231.36 sec so far
Iteration 4363: max relative diff=0.000023, 236.38 sec so far
Iteration 4453: max relative diff=0.000023, 241.41 sec so far
Iteration 4545: max relative diff=0.000023, 246.45 sec so far
Iteration 4637: max relative diff=0.000023, 251.48 sec so far
Iteration 4729: max relative diff=0.000023, 256.51 sec so far
Iteration 4821: max relative diff=0.000023, 261.54 sec so far
Iteration 4913: max relative diff=0.000023, 266.57 sec so far
Iteration 5005: max relative diff=0.000023, 271.60 sec so far
Iteration 5097: max relative diff=0.000023, 276.61 sec so far
Iteration 5189: max relative diff=0.000023, 281.62 sec so far
Iteration 5281: max relative diff=0.000023, 286.65 sec so far
Iteration 5373: max relative diff=0.000023, 291.69 sec so far
Iteration 5465: max relative diff=0.000023, 296.72 sec so far
Iteration 5555: max relative diff=0.000023, 301.76 sec so far
Iteration 5647: max relative diff=0.000023, 306.79 sec so far
Iteration 5739: max relative diff=0.000023, 311.85 sec so far
Iteration 5831: max relative diff=0.000023, 316.88 sec so far
Iteration 5923: max relative diff=0.000023, 321.90 sec so far
Iteration 6015: max relative diff=0.000023, 326.94 sec so far
Iteration 6108: max relative diff=0.000023, 332.00 sec so far
Iteration 6201: max relative diff=0.000023, 337.06 sec so far
Iteration 6293: max relative diff=0.000023, 342.10 sec so far
Iteration 6385: max relative diff=0.000023, 347.13 sec so far
Iteration 6477: max relative diff=0.000023, 352.16 sec so far
Iteration 6569: max relative diff=0.000023, 357.17 sec so far
Iteration 6659: max relative diff=0.000023, 362.20 sec so far
Iteration 6751: max relative diff=0.000023, 367.25 sec so far
Iteration 6843: max relative diff=0.000023, 372.30 sec so far
Iteration 6935: max relative diff=0.000023, 377.33 sec so far
Iteration 7027: max relative diff=0.000023, 382.36 sec so far
Iteration 7119: max relative diff=0.000023, 387.37 sec so far
Iteration 7211: max relative diff=0.000023, 392.42 sec so far
Iteration 7303: max relative diff=0.000023, 397.46 sec so far
Iteration 7395: max relative diff=0.000023, 402.49 sec so far
Iteration 7487: max relative diff=0.000023, 407.51 sec so far
Iteration 7579: max relative diff=0.000023, 412.54 sec so far
Iteration 7671: max relative diff=0.000023, 417.55 sec so far
Iteration 7761: max relative diff=0.000023, 422.61 sec so far
Iteration 7853: max relative diff=0.000023, 427.67 sec so far
Iteration 7945: max relative diff=0.000023, 432.71 sec so far
Iteration 8037: max relative diff=0.000023, 437.73 sec so far
Iteration 8129: max relative diff=0.000023, 442.76 sec so far
Iteration 8221: max relative diff=0.000023, 447.80 sec so far
Iteration 8313: max relative diff=0.000023, 452.85 sec so far
Iteration 8405: max relative diff=0.000023, 457.88 sec so far
Iteration 8497: max relative diff=0.000023, 462.90 sec so far
Iteration 8589: max relative diff=0.000023, 467.92 sec so far
Iteration 8681: max relative diff=0.000023, 472.97 sec so far
Iteration 8773: max relative diff=0.000023, 478.02 sec so far
Iteration 8863: max relative diff=0.000023, 483.07 sec so far
Iteration 8955: max relative diff=0.000023, 488.13 sec so far
Iteration 9047: max relative diff=0.000023, 493.16 sec so far
Iteration 9139: max relative diff=0.000023, 498.18 sec so far
Iteration 9231: max relative diff=0.000023, 503.20 sec so far
Iteration 9323: max relative diff=0.000023, 508.23 sec so far
Iteration 9415: max relative diff=0.000023, 513.26 sec so far
Iteration 9508: max relative diff=0.000023, 518.31 sec so far
Iteration 9601: max relative diff=0.000023, 523.37 sec so far
Iteration 9693: max relative diff=0.000023, 528.41 sec so far
Iteration 9785: max relative diff=0.000023, 533.44 sec so far
Iteration 9876: max relative diff=0.000023, 538.47 sec so far
Iteration 9967: max relative diff=0.000023, 543.50 sec so far

Jacobi: 10000 iterations in 545.61 seconds (average 0.054528, setup 0.33)

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

