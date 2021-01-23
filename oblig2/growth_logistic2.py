import sys

N = int(sys.argv[1])
ym1 = float(sys.argv[2]) # This is y(n - 1)
q = float(sys.argv[3])

def osc_eqq(N, ym1, q):
    for n in xrange(N):
        yn = ym1 + q * ym1 * (1 - ym1)
        ym1 = yn
        print yn

osc_eqq(N, ym1, q)


"""
a)
[Linueks@1x-193-157-198-148 oblig2]$ python growth_logistic2.py 50 0.3 1
0.51
0.7599
0.94235199
0.996676706943
0.999988955723
0.999999999878
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
"""

"""
b)
[Linueks@1x-193-157-198-148 oblig2]$ python growth_logistic2.py 50 0.3 2
0.72
1.1232
0.84644352
1.1063972949
0.870961936376
1.0957364199
0.885932655914
1.08804462611
0.896451661513
1.08210382168
0.904414103251
1.07731256943
0.910732963781
1.07332982871
0.915915643735
1.06994399833
0.920271675867
1.06701511279
0.92400283652
1.06444602577
0.92724739376
1.06216672281
0.930103874339
1.0601251889
0.932644734424
1.05828180197
"""

"""
c)
python growth_logistic2.py 1000 0.3 2
0.984148067082
1.01534936536
0.984179428602
1.01531999044
0.984210605347
1.01529078469
0.984241599121
1.01526174648
0.984272411706
1.01523287423
0.984303044859
1.01520416634
0.984333500312
1.01517562126
0.984363779776
1.01514723746
0.984393884936
1.01511901341
0.984423817458
1.01509094762
0.984453578983
1.0150630386
0.984483171132
1.01503528491
0.984512595504
1.0150076851
0.984541853676
1.01498023775
0.984570947205
1.01495294145
0.984599877629
1.01492579483
0.984628646465
1.01489879652
0.984657255208
1.01487194516
0.984685705338
1.01484523942
0.984713998314
1.01481867799
0.984742135574
1.01479225957
0.984770118541
1.01476598288
0.984797948619
1.01473984665
0.984825627193
1.01471384963
0.984853155631
1.01468799058
0.984880535285
1.01466226829
0.984907767489
1.01463668155
0.98493485356
1.01461122917
0.984961794799
1.01458590997
0.984988592491
1.0145607228
0.985015247905
1.0145356665
0.985041762294
1.01451073996
0.985068136897
1.01448594203
0.985094372935
1.01446127163
0.985120471617
1.01443672765
0.985146434136
1.01441230903
0.985172261671
1.01438801468
0.985197955386
1.01436384356
0.985223516432
1.01433979463
0.985248945945
1.01431586686
0.985274245048
1.01429205923
0.985299414852
1.01426837074
0.985324456452
1.01424480039
0.985349370932
1.0142213472
0.985374159364
1.01419801021
0.985398822805
1.01417478844
0.985423362301
1.01415168097
0.985447778886
1.01412868684
0.985472073581
1.01410580513
0.985496247397
1.01408303492
0.98552030133
1.01406037532
0.985544236369
1.01403782543
0.985568053488
1.01401538435
0.985591753651
1.01399305122
0.985615337812
1.01397082518
0.985638806912
1.01394870535
0.985662161884
1.01392669091
0.985685403648
1.01390478101
0.985708533115
1.01388297483
0.985731551186
1.01386127155
0.985754458751
1.01383967036
0.985777256691
1.01381817045
0.985799945876
1.01379677105
0.985822527168
1.01377547136
0.985845001417
1.01375427061
0.985867369467
1.01373316804
0.985889632149
1.01371216289
0.985911790289
1.01369125441
0.9859338447
1.01367044185
0.985955796189
1.01364972449
0.985977645553
1.0136291016
0.985999393581
1.01360857246
0.986021041053
1.01358813636
0.98604258874
1.0135677926
0.986064037406
"""
