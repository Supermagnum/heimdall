v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
C {devices/iopin.sym} -200 -40 0 0 {name=tp lab=tp}
C {devices/iopin.sym} -200 -80 0 0 {name=tn lab=tn}
C {devices/iopin.sym} -200 -120 0 0 {name=ct lab=ct}
C {devices/iopin.sym} -200 -160 0 0 {name=vt lab=vt}
C {devices/iopin.sym} -200 -200 0 0 {name=vdd lab=vdd}
C {devices/iopin.sym} -200 -240 0 0 {name=gnd lab=gnd}
C {devices/iopin.sym} -200 -280 0 0 {name=vbp lab=vbp}
C {devices/iopin.sym} -200 -320 0 0 {name=vbp_tail lab=vbp_tail}
C {devices/title.sym} 0 40 0 0 {name=t1 author="HT13G-M P2.7.1"}
C {devices/lab_pin.sym} 200 40 0 0 {name=ttitle lab=vco_sim_flat_step2}
C {devices/res.sym} 0 0 0 0 {name=r1p
value=0.814837
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 0 -30 0 -30 {lab=p}
C {devices/lab_pin.sym} 0 -30 0 0 {name=p1 sig_type=std_logic lab=p}
N 0 30 0 30 {lab=p1}
C {devices/lab_pin.sym} 0 30 0 0 {name=p2 sig_type=std_logic lab=p1}
C {devices/ind.sym} 220 0 0 0 {name=l1p
value=8.05663e-10
m=1
footprint=1206
device=inductor
sim_device=inductor
}
N 220 -30 220 -30 {lab=p1}
C {devices/lab_pin.sym} 220 -30 0 0 {name=p3 sig_type=std_logic lab=p1}
N 220 30 220 30 {lab=p2}
C {devices/lab_pin.sym} 220 30 0 0 {name=p4 sig_type=std_logic lab=p2}
C {devices/res.sym} 440 0 0 0 {name=r2p
value=0.827877
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 440 -30 440 -30 {lab=p2}
C {devices/lab_pin.sym} 440 -30 0 0 {name=p5 sig_type=std_logic lab=p2}
N 440 30 440 30 {lab=ct}
C {devices/lab_pin.sym} 440 30 0 0 {name=p6 sig_type=std_logic lab=ct}
C {devices/ind.sym} 660 0 0 0 {name=l2p
value=3.196e-11
m=1
footprint=1206
device=inductor
sim_device=inductor
}
N 660 -30 660 -30 {lab=p2}
C {devices/lab_pin.sym} 660 -30 0 0 {name=p7 sig_type=std_logic lab=p2}
N 660 30 660 30 {lab=ct}
C {devices/lab_pin.sym} 660 30 0 0 {name=p8 sig_type=std_logic lab=ct}
C {devices/res.sym} 880 0 0 0 {name=r1n
value=0.814837
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 -30 880 -30 {lab=n}
C {devices/lab_pin.sym} 880 -30 0 0 {name=p9 sig_type=std_logic lab=n}
N 880 30 880 30 {lab=n1}
C {devices/lab_pin.sym} 880 30 0 0 {name=p10 sig_type=std_logic lab=n1}
C {devices/ind.sym} 1100 0 0 0 {name=l1n
value=8.05663e-10
m=1
footprint=1206
device=inductor
sim_device=inductor
}
N 1100 -30 1100 -30 {lab=n1}
C {devices/lab_pin.sym} 1100 -30 0 0 {name=p11 sig_type=std_logic lab=n1}
N 1100 30 1100 30 {lab=n2}
C {devices/lab_pin.sym} 1100 30 0 0 {name=p12 sig_type=std_logic lab=n2}
C {devices/res.sym} 0 120 0 0 {name=r2n
value=0.827877
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 0 90 0 90 {lab=n2}
C {devices/lab_pin.sym} 0 90 0 0 {name=p13 sig_type=std_logic lab=n2}
N 0 150 0 150 {lab=ct}
C {devices/lab_pin.sym} 0 150 0 0 {name=p14 sig_type=std_logic lab=ct}
C {devices/ind.sym} 220 120 0 0 {name=l2n
value=3.196e-11
m=1
footprint=1206
device=inductor
sim_device=inductor
}
N 220 90 220 90 {lab=n2}
C {devices/lab_pin.sym} 220 90 0 0 {name=p15 sig_type=std_logic lab=n2}
N 220 150 220 150 {lab=ct}
C {devices/lab_pin.sym} 220 150 0 0 {name=p16 sig_type=std_logic lab=ct}
C {devices/capa.sym} 440 120 0 0 {name=cp
value=2.98589e-14
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 440 90 440 90 {lab=p}
C {devices/lab_pin.sym} 440 90 0 0 {name=p17 sig_type=std_logic lab=p}
N 440 150 440 150 {lab=n}
C {devices/lab_pin.sym} 440 150 0 0 {name=p18 sig_type=std_logic lab=n}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 120 0 0 {name=m1
w=32u
l=0.13u
ng=8
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 90 680 90 {lab=tp}
C {devices/lab_pin.sym} 680 90 0 0 {name=p19 sig_type=std_logic lab=tp}
N 640 120 640 120 {lab=tn}
C {devices/lab_pin.sym} 640 120 0 1 {name=p20 sig_type=std_logic lab=tn}
N 680 150 680 150 {lab=tail}
C {devices/lab_pin.sym} 680 150 0 0 {name=p21 sig_type=std_logic lab=tail}
N 680 120 680 120 {lab=gnd}
C {devices/lab_pin.sym} 680 120 0 0 {name=p22 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 120 0 0 {name=m2
w=32u
l=0.13u
ng=8
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 90 900 90 {lab=tn}
C {devices/lab_pin.sym} 900 90 0 0 {name=p23 sig_type=std_logic lab=tn}
N 860 120 860 120 {lab=tp}
C {devices/lab_pin.sym} 860 120 0 1 {name=p24 sig_type=std_logic lab=tp}
N 900 150 900 150 {lab=tail}
C {devices/lab_pin.sym} 900 150 0 0 {name=p25 sig_type=std_logic lab=tail}
N 900 120 900 120 {lab=gnd}
C {devices/lab_pin.sym} 900 120 0 0 {name=p26 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 120 0 0 {name=mdum
w=8u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 90 1120 90 {lab=gnd}
C {devices/lab_pin.sym} 1120 90 0 0 {name=p27 sig_type=std_logic lab=gnd}
N 1080 120 1080 120 {lab=gnd}
C {devices/lab_pin.sym} 1080 120 0 1 {name=p28 sig_type=std_logic lab=gnd}
N 1120 150 1120 150 {lab=gnd}
C {devices/lab_pin.sym} 1120 150 0 0 {name=p29 sig_type=std_logic lab=gnd}
N 1120 120 1120 120 {lab=gnd}
C {devices/lab_pin.sym} 1120 120 0 0 {name=p30 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 0 240 0 0 {name=xf1
model=cap_rfcmim
lvs_model=rfcmim
w=1.450000e-05
l=1.450000e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 0 210 0 210 {lab=tp}
C {devices/lab_pin.sym} 0 210 0 0 {name=p31 sig_type=std_logic lab=tp}
N 0 270 0 270 {lab=fx}
C {devices/lab_pin.sym} 0 270 0 0 {name=p32 sig_type=std_logic lab=fx}
N -30 240 -30 240 {lab=gnd}
C {devices/lab_pin.sym} -30 240 0 0 {name=p33 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 220 240 0 0 {name=xf2
model=cap_rfcmim
lvs_model=rfcmim
w=1.450000e-05
l=1.450000e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 220 210 220 210 {lab=tn}
C {devices/lab_pin.sym} 220 210 0 0 {name=p34 sig_type=std_logic lab=tn}
N 220 270 220 270 {lab=fx}
C {devices/lab_pin.sym} 220 270 0 0 {name=p35 sig_type=std_logic lab=fx}
N 190 240 190 240 {lab=gnd}
C {devices/lab_pin.sym} 190 240 0 0 {name=p36 sig_type=std_logic lab=gnd}
C {sg13g2_pr/rhigh.sym} 440 240 0 0 {name=rfx
w=2.000000e-06
l=1.520000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 440 210 440 210 {lab=fx}
C {devices/lab_pin.sym} 440 210 0 0 {name=p37 sig_type=std_logic lab=fx}
N 440 270 440 270 {lab=gnd}
C {devices/lab_pin.sym} 440 270 0 0 {name=p38 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_cmim.sym} 660 240 0 0 {name=xb0p
model=cap_cmim
lvs_model=cmim
w=2.810000e-06
l=2.810000e-06
m=1
mm_ok=1
spiceprefix=X
}
N 660 210 660 210 {lab=tp}
C {devices/lab_pin.sym} 660 210 0 0 {name=p39 sig_type=std_logic lab=tp}
N 660 270 660 270 {lab=a0}
C {devices/lab_pin.sym} 660 270 0 0 {name=p40 sig_type=std_logic lab=a0}
C {sg13g2_pr/cap_cmim.sym} 880 240 0 0 {name=xb0n
model=cap_cmim
lvs_model=cmim
w=2.810000e-06
l=2.810000e-06
m=1
mm_ok=1
spiceprefix=X
}
N 880 210 880 210 {lab=tn}
C {devices/lab_pin.sym} 880 210 0 0 {name=p41 sig_type=std_logic lab=tn}
N 880 270 880 270 {lab=b0}
C {devices/lab_pin.sym} 880 270 0 0 {name=p42 sig_type=std_logic lab=b0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 240 0 0 {name=ms0
w=10.32u
l=0.13u
ng=4
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 210 1120 210 {lab=a0}
C {devices/lab_pin.sym} 1120 210 0 0 {name=p43 sig_type=std_logic lab=a0}
N 1080 240 1080 240 {lab=g0}
C {devices/lab_pin.sym} 1080 240 0 1 {name=p44 sig_type=std_logic lab=g0}
N 1120 270 1120 270 {lab=b0}
C {devices/lab_pin.sym} 1120 270 0 0 {name=p45 sig_type=std_logic lab=b0}
N 1120 240 1120 240 {lab=gnd}
C {devices/lab_pin.sym} 1120 240 0 0 {name=p46 sig_type=std_logic lab=gnd}
C {sg13g2_pr/rhigh.sym} 0 360 0 0 {name=rba0
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 0 330 0 330 {lab=a0}
C {devices/lab_pin.sym} 0 330 0 0 {name=p47 sig_type=std_logic lab=a0}
N 0 390 0 390 {lab=bb0}
C {devices/lab_pin.sym} 0 390 0 0 {name=p48 sig_type=std_logic lab=bb0}
C {sg13g2_pr/rhigh.sym} 220 360 0 0 {name=rbb0
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 220 330 220 330 {lab=b0}
C {devices/lab_pin.sym} 220 330 0 0 {name=p49 sig_type=std_logic lab=b0}
N 220 390 220 390 {lab=bb0}
C {devices/lab_pin.sym} 220 390 0 0 {name=p50 sig_type=std_logic lab=bb0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 360 0 0 {name=mbp_rba0
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 330 460 330 {lab=a0}
C {devices/lab_pin.sym} 460 330 0 0 {name=p51 sig_type=std_logic lab=a0}
N 420 360 420 360 {lab=vbp}
C {devices/lab_pin.sym} 420 360 0 1 {name=p52 sig_type=std_logic lab=vbp}
N 460 390 460 390 {lab=bb0}
C {devices/lab_pin.sym} 460 390 0 0 {name=p53 sig_type=std_logic lab=bb0}
N 460 360 460 360 {lab=gnd}
C {devices/lab_pin.sym} 460 360 0 0 {name=p54 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 360 0 0 {name=mbp_rbb0
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 330 680 330 {lab=b0}
C {devices/lab_pin.sym} 680 330 0 0 {name=p55 sig_type=std_logic lab=b0}
N 640 360 640 360 {lab=vbp}
C {devices/lab_pin.sym} 640 360 0 1 {name=p56 sig_type=std_logic lab=vbp}
N 680 390 680 390 {lab=bb0}
C {devices/lab_pin.sym} 680 390 0 0 {name=p57 sig_type=std_logic lab=bb0}
N 680 360 680 360 {lab=gnd}
C {devices/lab_pin.sym} 680 360 0 0 {name=p58 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_cmim.sym} 880 360 0 0 {name=xb1p
model=cap_cmim
lvs_model=cmim
w=3.920000e-06
l=3.920000e-06
m=1
mm_ok=1
spiceprefix=X
}
N 880 330 880 330 {lab=tp}
C {devices/lab_pin.sym} 880 330 0 0 {name=p59 sig_type=std_logic lab=tp}
N 880 390 880 390 {lab=a1}
C {devices/lab_pin.sym} 880 390 0 0 {name=p60 sig_type=std_logic lab=a1}
C {sg13g2_pr/cap_cmim.sym} 1100 360 0 0 {name=xb1n
model=cap_cmim
lvs_model=cmim
w=3.920000e-06
l=3.920000e-06
m=1
mm_ok=1
spiceprefix=X
}
N 1100 330 1100 330 {lab=tn}
C {devices/lab_pin.sym} 1100 330 0 0 {name=p61 sig_type=std_logic lab=tn}
N 1100 390 1100 390 {lab=b1}
C {devices/lab_pin.sym} 1100 390 0 0 {name=p62 sig_type=std_logic lab=b1}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 480 0 0 {name=ms1
w=19.82u
l=0.13u
ng=8
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 450 20 450 {lab=a1}
C {devices/lab_pin.sym} 20 450 0 0 {name=p63 sig_type=std_logic lab=a1}
N -20 480 -20 480 {lab=g1}
C {devices/lab_pin.sym} -20 480 0 1 {name=p64 sig_type=std_logic lab=g1}
N 20 510 20 510 {lab=b1}
C {devices/lab_pin.sym} 20 510 0 0 {name=p65 sig_type=std_logic lab=b1}
N 20 480 20 480 {lab=gnd}
C {devices/lab_pin.sym} 20 480 0 0 {name=p66 sig_type=std_logic lab=gnd}
C {sg13g2_pr/rhigh.sym} 220 480 0 0 {name=rba1
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 220 450 220 450 {lab=a1}
C {devices/lab_pin.sym} 220 450 0 0 {name=p67 sig_type=std_logic lab=a1}
N 220 510 220 510 {lab=bb1}
C {devices/lab_pin.sym} 220 510 0 0 {name=p68 sig_type=std_logic lab=bb1}
C {sg13g2_pr/rhigh.sym} 440 480 0 0 {name=rbb1
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 440 450 440 450 {lab=b1}
C {devices/lab_pin.sym} 440 450 0 0 {name=p69 sig_type=std_logic lab=b1}
N 440 510 440 510 {lab=bb1}
C {devices/lab_pin.sym} 440 510 0 0 {name=p70 sig_type=std_logic lab=bb1}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 480 0 0 {name=mbp_rba1
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 450 680 450 {lab=a1}
C {devices/lab_pin.sym} 680 450 0 0 {name=p71 sig_type=std_logic lab=a1}
N 640 480 640 480 {lab=vbp}
C {devices/lab_pin.sym} 640 480 0 1 {name=p72 sig_type=std_logic lab=vbp}
N 680 510 680 510 {lab=bb1}
C {devices/lab_pin.sym} 680 510 0 0 {name=p73 sig_type=std_logic lab=bb1}
N 680 480 680 480 {lab=gnd}
C {devices/lab_pin.sym} 680 480 0 0 {name=p74 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 480 0 0 {name=mbp_rbb1
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 450 900 450 {lab=b1}
C {devices/lab_pin.sym} 900 450 0 0 {name=p75 sig_type=std_logic lab=b1}
N 860 480 860 480 {lab=vbp}
C {devices/lab_pin.sym} 860 480 0 1 {name=p76 sig_type=std_logic lab=vbp}
N 900 510 900 510 {lab=bb1}
C {devices/lab_pin.sym} 900 510 0 0 {name=p77 sig_type=std_logic lab=bb1}
N 900 480 900 480 {lab=gnd}
C {devices/lab_pin.sym} 900 480 0 0 {name=p78 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_cmim.sym} 1100 480 0 0 {name=xb2p
model=cap_cmim
lvs_model=cmim
w=5.530000e-06
l=5.530000e-06
m=1
mm_ok=1
spiceprefix=X
}
N 1100 450 1100 450 {lab=tp}
C {devices/lab_pin.sym} 1100 450 0 0 {name=p79 sig_type=std_logic lab=tp}
N 1100 510 1100 510 {lab=a2}
C {devices/lab_pin.sym} 1100 510 0 0 {name=p80 sig_type=std_logic lab=a2}
C {sg13g2_pr/cap_cmim.sym} 0 600 0 0 {name=xb2n
model=cap_cmim
lvs_model=cmim
w=5.530000e-06
l=5.530000e-06
m=1
mm_ok=1
spiceprefix=X
}
N 0 570 0 570 {lab=tn}
C {devices/lab_pin.sym} 0 570 0 0 {name=p81 sig_type=std_logic lab=tn}
N 0 630 0 630 {lab=b2}
C {devices/lab_pin.sym} 0 630 0 0 {name=p82 sig_type=std_logic lab=b2}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 600 0 0 {name=ms2
w=39.15u
l=0.13u
ng=16
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 570 240 570 {lab=a2}
C {devices/lab_pin.sym} 240 570 0 0 {name=p83 sig_type=std_logic lab=a2}
N 200 600 200 600 {lab=g2}
C {devices/lab_pin.sym} 200 600 0 1 {name=p84 sig_type=std_logic lab=g2}
N 240 630 240 630 {lab=b2}
C {devices/lab_pin.sym} 240 630 0 0 {name=p85 sig_type=std_logic lab=b2}
N 240 600 240 600 {lab=gnd}
C {devices/lab_pin.sym} 240 600 0 0 {name=p86 sig_type=std_logic lab=gnd}
C {sg13g2_pr/rhigh.sym} 440 600 0 0 {name=rba2
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 440 570 440 570 {lab=a2}
C {devices/lab_pin.sym} 440 570 0 0 {name=p87 sig_type=std_logic lab=a2}
N 440 630 440 630 {lab=bb2}
C {devices/lab_pin.sym} 440 630 0 0 {name=p88 sig_type=std_logic lab=bb2}
C {sg13g2_pr/rhigh.sym} 660 600 0 0 {name=rbb2
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 660 570 660 570 {lab=b2}
C {devices/lab_pin.sym} 660 570 0 0 {name=p89 sig_type=std_logic lab=b2}
N 660 630 660 630 {lab=bb2}
C {devices/lab_pin.sym} 660 630 0 0 {name=p90 sig_type=std_logic lab=bb2}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 600 0 0 {name=mbp_rba2
w=0.1562u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 570 900 570 {lab=a2}
C {devices/lab_pin.sym} 900 570 0 0 {name=p91 sig_type=std_logic lab=a2}
N 860 600 860 600 {lab=vbp}
C {devices/lab_pin.sym} 860 600 0 1 {name=p92 sig_type=std_logic lab=vbp}
N 900 630 900 630 {lab=bb2}
C {devices/lab_pin.sym} 900 630 0 0 {name=p93 sig_type=std_logic lab=bb2}
N 900 600 900 600 {lab=gnd}
C {devices/lab_pin.sym} 900 600 0 0 {name=p94 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 600 0 0 {name=mbp_rbb2
w=0.1562u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 570 1120 570 {lab=b2}
C {devices/lab_pin.sym} 1120 570 0 0 {name=p95 sig_type=std_logic lab=b2}
N 1080 600 1080 600 {lab=vbp}
C {devices/lab_pin.sym} 1080 600 0 1 {name=p96 sig_type=std_logic lab=vbp}
N 1120 630 1120 630 {lab=bb2}
C {devices/lab_pin.sym} 1120 630 0 0 {name=p97 sig_type=std_logic lab=bb2}
N 1120 600 1120 600 {lab=gnd}
C {devices/lab_pin.sym} 1120 600 0 0 {name=p98 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 0 720 0 0 {name=xb3p
model=cap_rfcmim
lvs_model=rfcmim
w=7.874000e-06
l=7.874000e-06
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 0 690 0 690 {lab=tp}
C {devices/lab_pin.sym} 0 690 0 0 {name=p99 sig_type=std_logic lab=tp}
N 0 750 0 750 {lab=a3}
C {devices/lab_pin.sym} 0 750 0 0 {name=p100 sig_type=std_logic lab=a3}
N -30 720 -30 720 {lab=gnd}
C {devices/lab_pin.sym} -30 720 0 0 {name=p101 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 220 720 0 0 {name=xb3n
model=cap_rfcmim
lvs_model=rfcmim
w=7.874000e-06
l=7.874000e-06
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 220 690 220 690 {lab=tn}
C {devices/lab_pin.sym} 220 690 0 0 {name=p102 sig_type=std_logic lab=tn}
N 220 750 220 750 {lab=b3}
C {devices/lab_pin.sym} 220 750 0 0 {name=p103 sig_type=std_logic lab=b3}
N 190 720 190 720 {lab=gnd}
C {devices/lab_pin.sym} 190 720 0 0 {name=p104 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 720 0 0 {name=ms3
w=77.50u
l=0.13u
ng=31
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 690 460 690 {lab=a3}
C {devices/lab_pin.sym} 460 690 0 0 {name=p105 sig_type=std_logic lab=a3}
N 420 720 420 720 {lab=g3}
C {devices/lab_pin.sym} 420 720 0 1 {name=p106 sig_type=std_logic lab=g3}
N 460 750 460 750 {lab=b3}
C {devices/lab_pin.sym} 460 750 0 0 {name=p107 sig_type=std_logic lab=b3}
N 460 720 460 720 {lab=gnd}
C {devices/lab_pin.sym} 460 720 0 0 {name=p108 sig_type=std_logic lab=gnd}
C {sg13g2_pr/rhigh.sym} 660 720 0 0 {name=rba3
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 660 690 660 690 {lab=a3}
C {devices/lab_pin.sym} 660 690 0 0 {name=p109 sig_type=std_logic lab=a3}
N 660 750 660 750 {lab=bb3}
C {devices/lab_pin.sym} 660 750 0 0 {name=p110 sig_type=std_logic lab=bb3}
C {sg13g2_pr/rhigh.sym} 880 720 0 0 {name=rbb3
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 880 690 880 690 {lab=b3}
C {devices/lab_pin.sym} 880 690 0 0 {name=p111 sig_type=std_logic lab=b3}
N 880 750 880 750 {lab=bb3}
C {devices/lab_pin.sym} 880 750 0 0 {name=p112 sig_type=std_logic lab=bb3}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 720 0 0 {name=mbp_rba3
w=0.3125u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 690 1120 690 {lab=a3}
C {devices/lab_pin.sym} 1120 690 0 0 {name=p113 sig_type=std_logic lab=a3}
N 1080 720 1080 720 {lab=vbp}
C {devices/lab_pin.sym} 1080 720 0 1 {name=p114 sig_type=std_logic lab=vbp}
N 1120 750 1120 750 {lab=bb3}
C {devices/lab_pin.sym} 1120 750 0 0 {name=p115 sig_type=std_logic lab=bb3}
N 1120 720 1120 720 {lab=gnd}
C {devices/lab_pin.sym} 1120 720 0 0 {name=p116 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 840 0 0 {name=mbp_rbb3
w=0.3125u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 810 20 810 {lab=b3}
C {devices/lab_pin.sym} 20 810 0 0 {name=p117 sig_type=std_logic lab=b3}
N -20 840 -20 840 {lab=vbp}
C {devices/lab_pin.sym} -20 840 0 1 {name=p118 sig_type=std_logic lab=vbp}
N 20 870 20 870 {lab=bb3}
C {devices/lab_pin.sym} 20 870 0 0 {name=p119 sig_type=std_logic lab=bb3}
N 20 840 20 840 {lab=gnd}
C {devices/lab_pin.sym} 20 840 0 0 {name=p120 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 220 840 0 0 {name=xb4p
model=cap_rfcmim
lvs_model=rfcmim
w=1.112200e-05
l=1.112200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 220 810 220 810 {lab=tp}
C {devices/lab_pin.sym} 220 810 0 0 {name=p121 sig_type=std_logic lab=tp}
N 220 870 220 870 {lab=a4}
C {devices/lab_pin.sym} 220 870 0 0 {name=p122 sig_type=std_logic lab=a4}
N 190 840 190 840 {lab=gnd}
C {devices/lab_pin.sym} 190 840 0 0 {name=p123 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 440 840 0 0 {name=xb4n
model=cap_rfcmim
lvs_model=rfcmim
w=1.112200e-05
l=1.112200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 440 810 440 810 {lab=tn}
C {devices/lab_pin.sym} 440 810 0 0 {name=p124 sig_type=std_logic lab=tn}
N 440 870 440 870 {lab=b4}
C {devices/lab_pin.sym} 440 870 0 0 {name=p125 sig_type=std_logic lab=b4}
N 410 840 410 840 {lab=gnd}
C {devices/lab_pin.sym} 410 840 0 0 {name=p126 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 840 0 0 {name=ms4
w=154.63u
l=0.13u
ng=62
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 810 680 810 {lab=a4}
C {devices/lab_pin.sym} 680 810 0 0 {name=p127 sig_type=std_logic lab=a4}
N 640 840 640 840 {lab=g4}
C {devices/lab_pin.sym} 640 840 0 1 {name=p128 sig_type=std_logic lab=g4}
N 680 870 680 870 {lab=b4}
C {devices/lab_pin.sym} 680 870 0 0 {name=p129 sig_type=std_logic lab=b4}
N 680 840 680 840 {lab=gnd}
C {devices/lab_pin.sym} 680 840 0 0 {name=p130 sig_type=std_logic lab=gnd}
C {sg13g2_pr/rhigh.sym} 880 840 0 0 {name=rba4
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 880 810 880 810 {lab=a4}
C {devices/lab_pin.sym} 880 810 0 0 {name=p131 sig_type=std_logic lab=a4}
N 880 870 880 870 {lab=bb4}
C {devices/lab_pin.sym} 880 870 0 0 {name=p132 sig_type=std_logic lab=bb4}
C {sg13g2_pr/rhigh.sym} 1100 840 0 0 {name=rbb4
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 1100 810 1100 810 {lab=b4}
C {devices/lab_pin.sym} 1100 810 0 0 {name=p133 sig_type=std_logic lab=b4}
N 1100 870 1100 870 {lab=bb4}
C {devices/lab_pin.sym} 1100 870 0 0 {name=p134 sig_type=std_logic lab=bb4}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 960 0 0 {name=mbp_rba4
w=0.625u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 930 20 930 {lab=a4}
C {devices/lab_pin.sym} 20 930 0 0 {name=p135 sig_type=std_logic lab=a4}
N -20 960 -20 960 {lab=vbp}
C {devices/lab_pin.sym} -20 960 0 1 {name=p136 sig_type=std_logic lab=vbp}
N 20 990 20 990 {lab=bb4}
C {devices/lab_pin.sym} 20 990 0 0 {name=p137 sig_type=std_logic lab=bb4}
N 20 960 20 960 {lab=gnd}
C {devices/lab_pin.sym} 20 960 0 0 {name=p138 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 960 0 0 {name=mbp_rbb4
w=0.625u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 930 240 930 {lab=b4}
C {devices/lab_pin.sym} 240 930 0 0 {name=p139 sig_type=std_logic lab=b4}
N 200 960 200 960 {lab=vbp}
C {devices/lab_pin.sym} 200 960 0 1 {name=p140 sig_type=std_logic lab=vbp}
N 240 990 240 990 {lab=bb4}
C {devices/lab_pin.sym} 240 990 0 0 {name=p141 sig_type=std_logic lab=bb4}
N 240 960 240 960 {lab=gnd}
C {devices/lab_pin.sym} 240 960 0 0 {name=p142 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 440 960 0 0 {name=xb5p
model=cap_rfcmim
lvs_model=rfcmim
w=1.571200e-05
l=1.571200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 440 930 440 930 {lab=tp}
C {devices/lab_pin.sym} 440 930 0 0 {name=p143 sig_type=std_logic lab=tp}
N 440 990 440 990 {lab=a5}
C {devices/lab_pin.sym} 440 990 0 0 {name=p144 sig_type=std_logic lab=a5}
N 410 960 410 960 {lab=gnd}
C {devices/lab_pin.sym} 410 960 0 0 {name=p145 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 660 960 0 0 {name=xb5n
model=cap_rfcmim
lvs_model=rfcmim
w=1.571200e-05
l=1.571200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 660 930 660 930 {lab=tn}
C {devices/lab_pin.sym} 660 930 0 0 {name=p146 sig_type=std_logic lab=tn}
N 660 990 660 990 {lab=b5}
C {devices/lab_pin.sym} 660 990 0 0 {name=p147 sig_type=std_logic lab=b5}
N 630 960 630 960 {lab=gnd}
C {devices/lab_pin.sym} 630 960 0 0 {name=p148 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 960 0 0 {name=ms5
w=308.58u
l=0.13u
ng=100
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 930 900 930 {lab=a5}
C {devices/lab_pin.sym} 900 930 0 0 {name=p149 sig_type=std_logic lab=a5}
N 860 960 860 960 {lab=g5}
C {devices/lab_pin.sym} 860 960 0 1 {name=p150 sig_type=std_logic lab=g5}
N 900 990 900 990 {lab=b5}
C {devices/lab_pin.sym} 900 990 0 0 {name=p151 sig_type=std_logic lab=b5}
N 900 960 900 960 {lab=gnd}
C {devices/lab_pin.sym} 900 960 0 0 {name=p152 sig_type=std_logic lab=gnd}
C {sg13g2_pr/rhigh.sym} 1100 960 0 0 {name=rba5
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 1100 930 1100 930 {lab=a5}
C {devices/lab_pin.sym} 1100 930 0 0 {name=p153 sig_type=std_logic lab=a5}
N 1100 990 1100 990 {lab=bb5}
C {devices/lab_pin.sym} 1100 990 0 0 {name=p154 sig_type=std_logic lab=bb5}
C {sg13g2_pr/rhigh.sym} 0 1080 0 0 {name=rbb5
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 0 1050 0 1050 {lab=b5}
C {devices/lab_pin.sym} 0 1050 0 0 {name=p155 sig_type=std_logic lab=b5}
N 0 1110 0 1110 {lab=bb5}
C {devices/lab_pin.sym} 0 1110 0 0 {name=p156 sig_type=std_logic lab=bb5}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 1080 0 0 {name=mbp_rba5
w=1.25u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 1050 240 1050 {lab=a5}
C {devices/lab_pin.sym} 240 1050 0 0 {name=p157 sig_type=std_logic lab=a5}
N 200 1080 200 1080 {lab=vbp}
C {devices/lab_pin.sym} 200 1080 0 1 {name=p158 sig_type=std_logic lab=vbp}
N 240 1110 240 1110 {lab=bb5}
C {devices/lab_pin.sym} 240 1110 0 0 {name=p159 sig_type=std_logic lab=bb5}
N 240 1080 240 1080 {lab=gnd}
C {devices/lab_pin.sym} 240 1080 0 0 {name=p160 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 1080 0 0 {name=mbp_rbb5
w=1.25u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 1050 460 1050 {lab=b5}
C {devices/lab_pin.sym} 460 1050 0 0 {name=p161 sig_type=std_logic lab=b5}
N 420 1080 420 1080 {lab=vbp}
C {devices/lab_pin.sym} 420 1080 0 1 {name=p162 sig_type=std_logic lab=vbp}
N 460 1110 460 1110 {lab=bb5}
C {devices/lab_pin.sym} 460 1110 0 0 {name=p163 sig_type=std_logic lab=bb5}
N 460 1080 460 1080 {lab=gnd}
C {devices/lab_pin.sym} 460 1080 0 0 {name=p164 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 660 1080 0 0 {name=xb6p
model=cap_rfcmim
lvs_model=rfcmim
w=1.571200e-05
l=1.571200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 660 1050 660 1050 {lab=tp}
C {devices/lab_pin.sym} 660 1050 0 0 {name=p165 sig_type=std_logic lab=tp}
N 660 1110 660 1110 {lab=a6}
C {devices/lab_pin.sym} 660 1110 0 0 {name=p166 sig_type=std_logic lab=a6}
N 630 1080 630 1080 {lab=gnd}
C {devices/lab_pin.sym} 630 1080 0 0 {name=p167 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 880 1080 0 0 {name=xb6n
model=cap_rfcmim
lvs_model=rfcmim
w=1.571200e-05
l=1.571200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 880 1050 880 1050 {lab=tn}
C {devices/lab_pin.sym} 880 1050 0 0 {name=p168 sig_type=std_logic lab=tn}
N 880 1110 880 1110 {lab=b6}
C {devices/lab_pin.sym} 880 1110 0 0 {name=p169 sig_type=std_logic lab=b6}
N 850 1080 850 1080 {lab=gnd}
C {devices/lab_pin.sym} 850 1080 0 0 {name=p170 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 1080 0 0 {name=ms6
w=308.58u
l=0.13u
ng=100
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 1050 1120 1050 {lab=a6}
C {devices/lab_pin.sym} 1120 1050 0 0 {name=p171 sig_type=std_logic lab=a6}
N 1080 1080 1080 1080 {lab=g6}
C {devices/lab_pin.sym} 1080 1080 0 1 {name=p172 sig_type=std_logic lab=g6}
N 1120 1110 1120 1110 {lab=b6}
C {devices/lab_pin.sym} 1120 1110 0 0 {name=p173 sig_type=std_logic lab=b6}
N 1120 1080 1120 1080 {lab=gnd}
C {devices/lab_pin.sym} 1120 1080 0 0 {name=p174 sig_type=std_logic lab=gnd}
C {sg13g2_pr/rhigh.sym} 0 1200 0 0 {name=rba6
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 0 1170 0 1170 {lab=a6}
C {devices/lab_pin.sym} 0 1170 0 0 {name=p175 sig_type=std_logic lab=a6}
N 0 1230 0 1230 {lab=bb6}
C {devices/lab_pin.sym} 0 1230 0 0 {name=p176 sig_type=std_logic lab=bb6}
C {sg13g2_pr/rhigh.sym} 220 1200 0 0 {name=rbb6
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 220 1170 220 1170 {lab=b6}
C {devices/lab_pin.sym} 220 1170 0 0 {name=p177 sig_type=std_logic lab=b6}
N 220 1230 220 1230 {lab=bb6}
C {devices/lab_pin.sym} 220 1230 0 0 {name=p178 sig_type=std_logic lab=bb6}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 1200 0 0 {name=mbp_rba6
w=1.25u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 1170 460 1170 {lab=a6}
C {devices/lab_pin.sym} 460 1170 0 0 {name=p179 sig_type=std_logic lab=a6}
N 420 1200 420 1200 {lab=vbp}
C {devices/lab_pin.sym} 420 1200 0 1 {name=p180 sig_type=std_logic lab=vbp}
N 460 1230 460 1230 {lab=bb6}
C {devices/lab_pin.sym} 460 1230 0 0 {name=p181 sig_type=std_logic lab=bb6}
N 460 1200 460 1200 {lab=gnd}
C {devices/lab_pin.sym} 460 1200 0 0 {name=p182 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 1200 0 0 {name=mbp_rbb6
w=1.25u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 1170 680 1170 {lab=b6}
C {devices/lab_pin.sym} 680 1170 0 0 {name=p183 sig_type=std_logic lab=b6}
N 640 1200 640 1200 {lab=vbp}
C {devices/lab_pin.sym} 640 1200 0 1 {name=p184 sig_type=std_logic lab=vbp}
N 680 1230 680 1230 {lab=bb6}
C {devices/lab_pin.sym} 680 1230 0 0 {name=p185 sig_type=std_logic lab=bb6}
N 680 1200 680 1200 {lab=gnd}
C {devices/lab_pin.sym} 680 1200 0 0 {name=p186 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 880 1200 0 0 {name=xb7p
model=cap_rfcmim
lvs_model=rfcmim
w=1.571200e-05
l=1.571200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 880 1170 880 1170 {lab=tp}
C {devices/lab_pin.sym} 880 1170 0 0 {name=p187 sig_type=std_logic lab=tp}
N 880 1230 880 1230 {lab=a7}
C {devices/lab_pin.sym} 880 1230 0 0 {name=p188 sig_type=std_logic lab=a7}
N 850 1200 850 1200 {lab=gnd}
C {devices/lab_pin.sym} 850 1200 0 0 {name=p189 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 1100 1200 0 0 {name=xb7n
model=cap_rfcmim
lvs_model=rfcmim
w=1.571200e-05
l=1.571200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 1100 1170 1100 1170 {lab=tn}
C {devices/lab_pin.sym} 1100 1170 0 0 {name=p190 sig_type=std_logic lab=tn}
N 1100 1230 1100 1230 {lab=b7}
C {devices/lab_pin.sym} 1100 1230 0 0 {name=p191 sig_type=std_logic lab=b7}
N 1070 1200 1070 1200 {lab=gnd}
C {devices/lab_pin.sym} 1070 1200 0 0 {name=p192 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 1320 0 0 {name=ms7
w=308.58u
l=0.13u
ng=100
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 1290 20 1290 {lab=a7}
C {devices/lab_pin.sym} 20 1290 0 0 {name=p193 sig_type=std_logic lab=a7}
N -20 1320 -20 1320 {lab=g7}
C {devices/lab_pin.sym} -20 1320 0 1 {name=p194 sig_type=std_logic lab=g7}
N 20 1350 20 1350 {lab=b7}
C {devices/lab_pin.sym} 20 1350 0 0 {name=p195 sig_type=std_logic lab=b7}
N 20 1320 20 1320 {lab=gnd}
C {devices/lab_pin.sym} 20 1320 0 0 {name=p196 sig_type=std_logic lab=gnd}
C {sg13g2_pr/rhigh.sym} 220 1320 0 0 {name=rba7
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 220 1290 220 1290 {lab=a7}
C {devices/lab_pin.sym} 220 1290 0 0 {name=p197 sig_type=std_logic lab=a7}
N 220 1350 220 1350 {lab=bb7}
C {devices/lab_pin.sym} 220 1350 0 0 {name=p198 sig_type=std_logic lab=bb7}
C {sg13g2_pr/rhigh.sym} 440 1320 0 0 {name=rbb7
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 440 1290 440 1290 {lab=b7}
C {devices/lab_pin.sym} 440 1290 0 0 {name=p199 sig_type=std_logic lab=b7}
N 440 1350 440 1350 {lab=bb7}
C {devices/lab_pin.sym} 440 1350 0 0 {name=p200 sig_type=std_logic lab=bb7}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 1320 0 0 {name=mbp_rba7
w=1.25u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 1290 680 1290 {lab=a7}
C {devices/lab_pin.sym} 680 1290 0 0 {name=p201 sig_type=std_logic lab=a7}
N 640 1320 640 1320 {lab=vbp}
C {devices/lab_pin.sym} 640 1320 0 1 {name=p202 sig_type=std_logic lab=vbp}
N 680 1350 680 1350 {lab=bb7}
C {devices/lab_pin.sym} 680 1350 0 0 {name=p203 sig_type=std_logic lab=bb7}
N 680 1320 680 1320 {lab=gnd}
C {devices/lab_pin.sym} 680 1320 0 0 {name=p204 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 1320 0 0 {name=mbp_rbb7
w=1.25u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 1290 900 1290 {lab=b7}
C {devices/lab_pin.sym} 900 1290 0 0 {name=p205 sig_type=std_logic lab=b7}
N 860 1320 860 1320 {lab=vbp}
C {devices/lab_pin.sym} 860 1320 0 1 {name=p206 sig_type=std_logic lab=vbp}
N 900 1350 900 1350 {lab=bb7}
C {devices/lab_pin.sym} 900 1350 0 0 {name=p207 sig_type=std_logic lab=bb7}
N 900 1320 900 1320 {lab=gnd}
C {devices/lab_pin.sym} 900 1320 0 0 {name=p208 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 1100 1320 0 0 {name=xb8p
model=cap_rfcmim
lvs_model=rfcmim
w=1.571200e-05
l=1.571200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 1100 1290 1100 1290 {lab=tp}
C {devices/lab_pin.sym} 1100 1290 0 0 {name=p209 sig_type=std_logic lab=tp}
N 1100 1350 1100 1350 {lab=a8}
C {devices/lab_pin.sym} 1100 1350 0 0 {name=p210 sig_type=std_logic lab=a8}
N 1070 1320 1070 1320 {lab=gnd}
C {devices/lab_pin.sym} 1070 1320 0 0 {name=p211 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 0 1440 0 0 {name=xb8n
model=cap_rfcmim
lvs_model=rfcmim
w=1.571200e-05
l=1.571200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 0 1410 0 1410 {lab=tn}
C {devices/lab_pin.sym} 0 1410 0 0 {name=p212 sig_type=std_logic lab=tn}
N 0 1470 0 1470 {lab=b8}
C {devices/lab_pin.sym} 0 1470 0 0 {name=p213 sig_type=std_logic lab=b8}
N -30 1440 -30 1440 {lab=gnd}
C {devices/lab_pin.sym} -30 1440 0 0 {name=p214 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 1440 0 0 {name=ms8
w=308.58u
l=0.13u
ng=100
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 1410 240 1410 {lab=a8}
C {devices/lab_pin.sym} 240 1410 0 0 {name=p215 sig_type=std_logic lab=a8}
N 200 1440 200 1440 {lab=g8}
C {devices/lab_pin.sym} 200 1440 0 1 {name=p216 sig_type=std_logic lab=g8}
N 240 1470 240 1470 {lab=b8}
C {devices/lab_pin.sym} 240 1470 0 0 {name=p217 sig_type=std_logic lab=b8}
N 240 1440 240 1440 {lab=gnd}
C {devices/lab_pin.sym} 240 1440 0 0 {name=p218 sig_type=std_logic lab=gnd}
C {sg13g2_pr/rhigh.sym} 440 1440 0 0 {name=rba8
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 440 1410 440 1410 {lab=a8}
C {devices/lab_pin.sym} 440 1410 0 0 {name=p219 sig_type=std_logic lab=a8}
N 440 1470 440 1470 {lab=bb8}
C {devices/lab_pin.sym} 440 1470 0 0 {name=p220 sig_type=std_logic lab=bb8}
C {sg13g2_pr/rhigh.sym} 660 1440 0 0 {name=rbb8
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 660 1410 660 1410 {lab=b8}
C {devices/lab_pin.sym} 660 1410 0 0 {name=p221 sig_type=std_logic lab=b8}
N 660 1470 660 1470 {lab=bb8}
C {devices/lab_pin.sym} 660 1470 0 0 {name=p222 sig_type=std_logic lab=bb8}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 1440 0 0 {name=mbp_rba8
w=1.25u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 1410 900 1410 {lab=a8}
C {devices/lab_pin.sym} 900 1410 0 0 {name=p223 sig_type=std_logic lab=a8}
N 860 1440 860 1440 {lab=vbp}
C {devices/lab_pin.sym} 860 1440 0 1 {name=p224 sig_type=std_logic lab=vbp}
N 900 1470 900 1470 {lab=bb8}
C {devices/lab_pin.sym} 900 1470 0 0 {name=p225 sig_type=std_logic lab=bb8}
N 900 1440 900 1440 {lab=gnd}
C {devices/lab_pin.sym} 900 1440 0 0 {name=p226 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 1440 0 0 {name=mbp_rbb8
w=1.25u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 1410 1120 1410 {lab=b8}
C {devices/lab_pin.sym} 1120 1410 0 0 {name=p227 sig_type=std_logic lab=b8}
N 1080 1440 1080 1440 {lab=vbp}
C {devices/lab_pin.sym} 1080 1440 0 1 {name=p228 sig_type=std_logic lab=vbp}
N 1120 1470 1120 1470 {lab=bb8}
C {devices/lab_pin.sym} 1120 1470 0 0 {name=p229 sig_type=std_logic lab=bb8}
N 1120 1440 1120 1440 {lab=gnd}
C {devices/lab_pin.sym} 1120 1440 0 0 {name=p230 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 0 1560 0 0 {name=xb9p
model=cap_rfcmim
lvs_model=rfcmim
w=1.571200e-05
l=1.571200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 0 1530 0 1530 {lab=tp}
C {devices/lab_pin.sym} 0 1530 0 0 {name=p231 sig_type=std_logic lab=tp}
N 0 1590 0 1590 {lab=a9}
C {devices/lab_pin.sym} 0 1590 0 0 {name=p232 sig_type=std_logic lab=a9}
N -30 1560 -30 1560 {lab=gnd}
C {devices/lab_pin.sym} -30 1560 0 0 {name=p233 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 220 1560 0 0 {name=xb9n
model=cap_rfcmim
lvs_model=rfcmim
w=1.571200e-05
l=1.571200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 220 1530 220 1530 {lab=tn}
C {devices/lab_pin.sym} 220 1530 0 0 {name=p234 sig_type=std_logic lab=tn}
N 220 1590 220 1590 {lab=b9}
C {devices/lab_pin.sym} 220 1590 0 0 {name=p235 sig_type=std_logic lab=b9}
N 190 1560 190 1560 {lab=gnd}
C {devices/lab_pin.sym} 190 1560 0 0 {name=p236 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 1560 0 0 {name=ms9
w=308.58u
l=0.13u
ng=100
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 1530 460 1530 {lab=a9}
C {devices/lab_pin.sym} 460 1530 0 0 {name=p237 sig_type=std_logic lab=a9}
N 420 1560 420 1560 {lab=g9}
C {devices/lab_pin.sym} 420 1560 0 1 {name=p238 sig_type=std_logic lab=g9}
N 460 1590 460 1590 {lab=b9}
C {devices/lab_pin.sym} 460 1590 0 0 {name=p239 sig_type=std_logic lab=b9}
N 460 1560 460 1560 {lab=gnd}
C {devices/lab_pin.sym} 460 1560 0 0 {name=p240 sig_type=std_logic lab=gnd}
C {sg13g2_pr/rhigh.sym} 660 1560 0 0 {name=rba9
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 660 1530 660 1530 {lab=a9}
C {devices/lab_pin.sym} 660 1530 0 0 {name=p241 sig_type=std_logic lab=a9}
N 660 1590 660 1590 {lab=bb9}
C {devices/lab_pin.sym} 660 1590 0 0 {name=p242 sig_type=std_logic lab=bb9}
C {sg13g2_pr/rhigh.sym} 880 1560 0 0 {name=rbb9
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 880 1530 880 1530 {lab=b9}
C {devices/lab_pin.sym} 880 1530 0 0 {name=p243 sig_type=std_logic lab=b9}
N 880 1590 880 1590 {lab=bb9}
C {devices/lab_pin.sym} 880 1590 0 0 {name=p244 sig_type=std_logic lab=bb9}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 1560 0 0 {name=mbp_rba9
w=1.25u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 1530 1120 1530 {lab=a9}
C {devices/lab_pin.sym} 1120 1530 0 0 {name=p245 sig_type=std_logic lab=a9}
N 1080 1560 1080 1560 {lab=vbp}
C {devices/lab_pin.sym} 1080 1560 0 1 {name=p246 sig_type=std_logic lab=vbp}
N 1120 1590 1120 1590 {lab=bb9}
C {devices/lab_pin.sym} 1120 1590 0 0 {name=p247 sig_type=std_logic lab=bb9}
N 1120 1560 1120 1560 {lab=gnd}
C {devices/lab_pin.sym} 1120 1560 0 0 {name=p248 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 1680 0 0 {name=mbp_rbb9
w=1.25u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 1650 20 1650 {lab=b9}
C {devices/lab_pin.sym} 20 1650 0 0 {name=p249 sig_type=std_logic lab=b9}
N -20 1680 -20 1680 {lab=vbp}
C {devices/lab_pin.sym} -20 1680 0 1 {name=p250 sig_type=std_logic lab=vbp}
N 20 1710 20 1710 {lab=bb9}
C {devices/lab_pin.sym} 20 1710 0 0 {name=p251 sig_type=std_logic lab=bb9}
N 20 1680 20 1680 {lab=gnd}
C {devices/lab_pin.sym} 20 1680 0 0 {name=p252 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 220 1680 0 0 {name=xb10p
model=cap_rfcmim
lvs_model=rfcmim
w=1.571200e-05
l=1.571200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 220 1650 220 1650 {lab=tp}
C {devices/lab_pin.sym} 220 1650 0 0 {name=p253 sig_type=std_logic lab=tp}
N 220 1710 220 1710 {lab=a10}
C {devices/lab_pin.sym} 220 1710 0 0 {name=p254 sig_type=std_logic lab=a10}
N 190 1680 190 1680 {lab=gnd}
C {devices/lab_pin.sym} 190 1680 0 0 {name=p255 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 440 1680 0 0 {name=xb10n
model=cap_rfcmim
lvs_model=rfcmim
w=1.571200e-05
l=1.571200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 440 1650 440 1650 {lab=tn}
C {devices/lab_pin.sym} 440 1650 0 0 {name=p256 sig_type=std_logic lab=tn}
N 440 1710 440 1710 {lab=b10}
C {devices/lab_pin.sym} 440 1710 0 0 {name=p257 sig_type=std_logic lab=b10}
N 410 1680 410 1680 {lab=gnd}
C {devices/lab_pin.sym} 410 1680 0 0 {name=p258 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 1680 0 0 {name=ms10
w=308.58u
l=0.13u
ng=100
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 1650 680 1650 {lab=a10}
C {devices/lab_pin.sym} 680 1650 0 0 {name=p259 sig_type=std_logic lab=a10}
N 640 1680 640 1680 {lab=g10}
C {devices/lab_pin.sym} 640 1680 0 1 {name=p260 sig_type=std_logic lab=g10}
N 680 1710 680 1710 {lab=b10}
C {devices/lab_pin.sym} 680 1710 0 0 {name=p261 sig_type=std_logic lab=b10}
N 680 1680 680 1680 {lab=gnd}
C {devices/lab_pin.sym} 680 1680 0 0 {name=p262 sig_type=std_logic lab=gnd}
C {sg13g2_pr/rhigh.sym} 880 1680 0 0 {name=rba10
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 880 1650 880 1650 {lab=a10}
C {devices/lab_pin.sym} 880 1650 0 0 {name=p263 sig_type=std_logic lab=a10}
N 880 1710 880 1710 {lab=bb10}
C {devices/lab_pin.sym} 880 1710 0 0 {name=p264 sig_type=std_logic lab=bb10}
C {sg13g2_pr/rhigh.sym} 1100 1680 0 0 {name=rbb10
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 1100 1650 1100 1650 {lab=b10}
C {devices/lab_pin.sym} 1100 1650 0 0 {name=p265 sig_type=std_logic lab=b10}
N 1100 1710 1100 1710 {lab=bb10}
C {devices/lab_pin.sym} 1100 1710 0 0 {name=p266 sig_type=std_logic lab=bb10}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 1800 0 0 {name=mbp_rba10
w=1.25u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 1770 20 1770 {lab=a10}
C {devices/lab_pin.sym} 20 1770 0 0 {name=p267 sig_type=std_logic lab=a10}
N -20 1800 -20 1800 {lab=vbp}
C {devices/lab_pin.sym} -20 1800 0 1 {name=p268 sig_type=std_logic lab=vbp}
N 20 1830 20 1830 {lab=bb10}
C {devices/lab_pin.sym} 20 1830 0 0 {name=p269 sig_type=std_logic lab=bb10}
N 20 1800 20 1800 {lab=gnd}
C {devices/lab_pin.sym} 20 1800 0 0 {name=p270 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 1800 0 0 {name=mbp_rbb10
w=1.25u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 1770 240 1770 {lab=b10}
C {devices/lab_pin.sym} 240 1770 0 0 {name=p271 sig_type=std_logic lab=b10}
N 200 1800 200 1800 {lab=vbp}
C {devices/lab_pin.sym} 200 1800 0 1 {name=p272 sig_type=std_logic lab=vbp}
N 240 1830 240 1830 {lab=bb10}
C {devices/lab_pin.sym} 240 1830 0 0 {name=p273 sig_type=std_logic lab=bb10}
N 240 1800 240 1800 {lab=gnd}
C {devices/lab_pin.sym} 240 1800 0 0 {name=p274 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 440 1800 0 0 {name=xb11p
model=cap_rfcmim
lvs_model=rfcmim
w=1.571200e-05
l=1.571200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 440 1770 440 1770 {lab=tp}
C {devices/lab_pin.sym} 440 1770 0 0 {name=p275 sig_type=std_logic lab=tp}
N 440 1830 440 1830 {lab=a11}
C {devices/lab_pin.sym} 440 1830 0 0 {name=p276 sig_type=std_logic lab=a11}
N 410 1800 410 1800 {lab=gnd}
C {devices/lab_pin.sym} 410 1800 0 0 {name=p277 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 660 1800 0 0 {name=xb11n
model=cap_rfcmim
lvs_model=rfcmim
w=1.571200e-05
l=1.571200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 660 1770 660 1770 {lab=tn}
C {devices/lab_pin.sym} 660 1770 0 0 {name=p278 sig_type=std_logic lab=tn}
N 660 1830 660 1830 {lab=b11}
C {devices/lab_pin.sym} 660 1830 0 0 {name=p279 sig_type=std_logic lab=b11}
N 630 1800 630 1800 {lab=gnd}
C {devices/lab_pin.sym} 630 1800 0 0 {name=p280 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 1800 0 0 {name=ms11
w=308.58u
l=0.13u
ng=100
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 1770 900 1770 {lab=a11}
C {devices/lab_pin.sym} 900 1770 0 0 {name=p281 sig_type=std_logic lab=a11}
N 860 1800 860 1800 {lab=g11}
C {devices/lab_pin.sym} 860 1800 0 1 {name=p282 sig_type=std_logic lab=g11}
N 900 1830 900 1830 {lab=b11}
C {devices/lab_pin.sym} 900 1830 0 0 {name=p283 sig_type=std_logic lab=b11}
N 900 1800 900 1800 {lab=gnd}
C {devices/lab_pin.sym} 900 1800 0 0 {name=p284 sig_type=std_logic lab=gnd}
C {sg13g2_pr/rhigh.sym} 1100 1800 0 0 {name=rba11
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 1100 1770 1100 1770 {lab=a11}
C {devices/lab_pin.sym} 1100 1770 0 0 {name=p285 sig_type=std_logic lab=a11}
N 1100 1830 1100 1830 {lab=bb11}
C {devices/lab_pin.sym} 1100 1830 0 0 {name=p286 sig_type=std_logic lab=bb11}
C {sg13g2_pr/rhigh.sym} 0 1920 0 0 {name=rbb11
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 0 1890 0 1890 {lab=b11}
C {devices/lab_pin.sym} 0 1890 0 0 {name=p287 sig_type=std_logic lab=b11}
N 0 1950 0 1950 {lab=bb11}
C {devices/lab_pin.sym} 0 1950 0 0 {name=p288 sig_type=std_logic lab=bb11}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 1920 0 0 {name=mbp_rba11
w=1.25u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 1890 240 1890 {lab=a11}
C {devices/lab_pin.sym} 240 1890 0 0 {name=p289 sig_type=std_logic lab=a11}
N 200 1920 200 1920 {lab=vbp}
C {devices/lab_pin.sym} 200 1920 0 1 {name=p290 sig_type=std_logic lab=vbp}
N 240 1950 240 1950 {lab=bb11}
C {devices/lab_pin.sym} 240 1950 0 0 {name=p291 sig_type=std_logic lab=bb11}
N 240 1920 240 1920 {lab=gnd}
C {devices/lab_pin.sym} 240 1920 0 0 {name=p292 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 1920 0 0 {name=mbp_rbb11
w=1.25u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 1890 460 1890 {lab=b11}
C {devices/lab_pin.sym} 460 1890 0 0 {name=p293 sig_type=std_logic lab=b11}
N 420 1920 420 1920 {lab=vbp}
C {devices/lab_pin.sym} 420 1920 0 1 {name=p294 sig_type=std_logic lab=vbp}
N 460 1950 460 1950 {lab=bb11}
C {devices/lab_pin.sym} 460 1950 0 0 {name=p295 sig_type=std_logic lab=bb11}
N 460 1920 460 1920 {lab=gnd}
C {devices/lab_pin.sym} 460 1920 0 0 {name=p296 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 660 1920 0 0 {name=xbdump
model=cap_rfcmim
lvs_model=rfcmim
w=1.571200e-05
l=1.571200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 660 1890 660 1890 {lab=gnd}
C {devices/lab_pin.sym} 660 1890 0 0 {name=p297 sig_type=std_logic lab=gnd}
N 660 1950 660 1950 {lab=adum}
C {devices/lab_pin.sym} 660 1950 0 0 {name=p298 sig_type=std_logic lab=adum}
N 630 1920 630 1920 {lab=gnd}
C {devices/lab_pin.sym} 630 1920 0 0 {name=p299 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 880 1920 0 0 {name=xbdumn
model=cap_rfcmim
lvs_model=rfcmim
w=1.571200e-05
l=1.571200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 880 1890 880 1890 {lab=gnd}
C {devices/lab_pin.sym} 880 1890 0 0 {name=p300 sig_type=std_logic lab=gnd}
N 880 1950 880 1950 {lab=bdum}
C {devices/lab_pin.sym} 880 1950 0 0 {name=p301 sig_type=std_logic lab=bdum}
N 850 1920 850 1920 {lab=gnd}
C {devices/lab_pin.sym} 850 1920 0 0 {name=p302 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 1920 0 0 {name=msdum
w=308.58u
l=0.13u
ng=100
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 1890 1120 1890 {lab=adum}
C {devices/lab_pin.sym} 1120 1890 0 0 {name=p303 sig_type=std_logic lab=adum}
N 1080 1920 1080 1920 {lab=gnd}
C {devices/lab_pin.sym} 1080 1920 0 1 {name=p304 sig_type=std_logic lab=gnd}
N 1120 1950 1120 1950 {lab=bdum}
C {devices/lab_pin.sym} 1120 1950 0 0 {name=p305 sig_type=std_logic lab=bdum}
N 1120 1920 1120 1920 {lab=gnd}
C {devices/lab_pin.sym} 1120 1920 0 0 {name=p306 sig_type=std_logic lab=gnd}
C {sg13g2_pr/rhigh.sym} 0 2040 0 0 {name=rbadum
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 0 2010 0 2010 {lab=adum}
C {devices/lab_pin.sym} 0 2010 0 0 {name=p307 sig_type=std_logic lab=adum}
N 0 2070 0 2070 {lab=gnd}
C {devices/lab_pin.sym} 0 2070 0 0 {name=p308 sig_type=std_logic lab=gnd}
C {sg13g2_pr/rhigh.sym} 220 2040 0 0 {name=rbbdum
w=5.000000e-06
l=6.080000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 220 2010 220 2010 {lab=bdum}
C {devices/lab_pin.sym} 220 2010 0 0 {name=p309 sig_type=std_logic lab=bdum}
N 220 2070 220 2070 {lab=gnd}
C {devices/lab_pin.sym} 220 2070 0 0 {name=p310 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 2040 0 0 {name=mbp_rbadum
w=1.25u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 2010 460 2010 {lab=adum}
C {devices/lab_pin.sym} 460 2010 0 0 {name=p311 sig_type=std_logic lab=adum}
N 420 2040 420 2040 {lab=gnd}
C {devices/lab_pin.sym} 420 2040 0 1 {name=p312 sig_type=std_logic lab=gnd}
N 460 2070 460 2070 {lab=gnd}
C {devices/lab_pin.sym} 460 2070 0 0 {name=p313 sig_type=std_logic lab=gnd}
N 460 2040 460 2040 {lab=gnd}
C {devices/lab_pin.sym} 460 2040 0 0 {name=p314 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 2040 0 0 {name=mbp_rbbdum
w=1.25u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 2010 680 2010 {lab=bdum}
C {devices/lab_pin.sym} 680 2010 0 0 {name=p315 sig_type=std_logic lab=bdum}
N 640 2040 640 2040 {lab=gnd}
C {devices/lab_pin.sym} 640 2040 0 1 {name=p316 sig_type=std_logic lab=gnd}
N 680 2070 680 2070 {lab=gnd}
C {devices/lab_pin.sym} 680 2070 0 0 {name=p317 sig_type=std_logic lab=gnd}
N 680 2040 680 2040 {lab=gnd}
C {devices/lab_pin.sym} 680 2040 0 0 {name=p318 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 880 2040 0 0 {name=xcp
model=cap_rfcmim
lvs_model=rfcmim
w=2.129200e-05
l=2.129200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 880 2010 880 2010 {lab=tp}
C {devices/lab_pin.sym} 880 2010 0 0 {name=p319 sig_type=std_logic lab=tp}
N 880 2070 880 2070 {lab=vgp}
C {devices/lab_pin.sym} 880 2070 0 0 {name=p320 sig_type=std_logic lab=vgp}
N 850 2040 850 2040 {lab=gnd}
C {devices/lab_pin.sym} 850 2040 0 0 {name=p321 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 1100 2040 0 0 {name=xcn
model=cap_rfcmim
lvs_model=rfcmim
w=2.129200e-05
l=2.129200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 1100 2010 1100 2010 {lab=tn}
C {devices/lab_pin.sym} 1100 2010 0 0 {name=p322 sig_type=std_logic lab=tn}
N 1100 2070 1100 2070 {lab=vgn}
C {devices/lab_pin.sym} 1100 2070 0 0 {name=p323 sig_type=std_logic lab=vgn}
N 1070 2040 1070 2040 {lab=gnd}
C {devices/lab_pin.sym} 1070 2040 0 0 {name=p324 sig_type=std_logic lab=gnd}
C {sg13g2_pr/rhigh.sym} 0 2160 0 0 {name=rvp
w=5.000000e-07
l=4.209500e-05
b=16
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 0 2130 0 2130 {lab=vgp}
C {devices/lab_pin.sym} 0 2130 0 0 {name=p325 sig_type=std_logic lab=vgp}
N 0 2190 0 2190 {lab=vvb}
C {devices/lab_pin.sym} 0 2190 0 0 {name=p326 sig_type=std_logic lab=vvb}
C {sg13g2_pr/rhigh.sym} 220 2160 0 0 {name=rvn
w=5.000000e-07
l=4.209500e-05
b=16
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 220 2130 220 2130 {lab=vgn}
C {devices/lab_pin.sym} 220 2130 0 0 {name=p327 sig_type=std_logic lab=vgn}
N 220 2190 220 2190 {lab=vvb}
C {devices/lab_pin.sym} 220 2190 0 0 {name=p328 sig_type=std_logic lab=vvb}
C {sg13g2_pr/sg13_svaricap.sym} 440 2160 0 0 {name=xv1
model=sg13_hv_svaricap_fx
W=3.740000e-06
L=3.000000e-07
Nx=10
spiceprefix=X
}
N 480 2160 480 2160 {lab=vgp}
C {devices/lab_pin.sym} 480 2160 0 0 {name=p329 sig_type=std_logic lab=vgp}
N 440 2130 440 2130 {lab=vt}
C {devices/lab_pin.sym} 440 2130 0 0 {name=p330 sig_type=std_logic lab=vt}
N 400 2160 400 2160 {lab=vgn}
C {devices/lab_pin.sym} 400 2160 0 0 {name=p331 sig_type=std_logic lab=vgn}
C {sg13g2_pr/sg13_svaricap.sym} 660 2160 0 0 {name=xv2
model=sg13_hv_svaricap_fx
W=3.740000e-06
L=3.000000e-07
Nx=10
spiceprefix=X
}
N 700 2160 700 2160 {lab=vgp}
C {devices/lab_pin.sym} 700 2160 0 0 {name=p332 sig_type=std_logic lab=vgp}
N 660 2130 660 2130 {lab=vt}
C {devices/lab_pin.sym} 660 2130 0 0 {name=p333 sig_type=std_logic lab=vt}
N 620 2160 620 2160 {lab=vgn}
C {devices/lab_pin.sym} 620 2160 0 0 {name=p334 sig_type=std_logic lab=vgn}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 2160 0 0 {name=mbp_rvp
w=5u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 2130 900 2130 {lab=vgp}
C {devices/lab_pin.sym} 900 2130 0 0 {name=p335 sig_type=std_logic lab=vgp}
N 860 2160 860 2160 {lab=vbp}
C {devices/lab_pin.sym} 860 2160 0 1 {name=p336 sig_type=std_logic lab=vbp}
N 900 2190 900 2190 {lab=vvb}
C {devices/lab_pin.sym} 900 2190 0 0 {name=p337 sig_type=std_logic lab=vvb}
N 900 2160 900 2160 {lab=gnd}
C {devices/lab_pin.sym} 900 2160 0 0 {name=p338 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 2160 0 0 {name=mbp_rvn
w=5u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 2130 1120 2130 {lab=vgn}
C {devices/lab_pin.sym} 1120 2130 0 0 {name=p339 sig_type=std_logic lab=vgn}
N 1080 2160 1080 2160 {lab=vbp}
C {devices/lab_pin.sym} 1080 2160 0 1 {name=p340 sig_type=std_logic lab=vbp}
N 1120 2190 1120 2190 {lab=vvb}
C {devices/lab_pin.sym} 1120 2190 0 0 {name=p341 sig_type=std_logic lab=vvb}
N 1120 2160 1120 2160 {lab=gnd}
C {devices/lab_pin.sym} 1120 2160 0 0 {name=p342 sig_type=std_logic lab=gnd}
C {devices/vsource.sym} 0 2280 0 0 {name=vvb_bias value=0.3}
N 0 2250 0 2250 {lab=vvb}
C {devices/lab_pin.sym} 0 2250 0 0 {name=p343 sig_type=std_logic lab=vvb}
N 0 2310 0 2310 {lab=gnd}
C {devices/lab_pin.sym} 0 2310 0 0 {name=p344 sig_type=std_logic lab=gnd}
C {devices/capa.sym} 220 2280 0 0 {name=ctail
value=8e-12
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 220 2250 220 2250 {lab=tail}
C {devices/lab_pin.sym} 220 2250 0 0 {name=p345 sig_type=std_logic lab=tail}
N 220 2310 220 2310 {lab=gnd}
C {devices/lab_pin.sym} 220 2310 0 0 {name=p346 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 2280 0 0 {name=mt
w=160u
l=4u
ng=32
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 2250 460 2250 {lab=tail}
C {devices/lab_pin.sym} 460 2250 0 0 {name=p347 sig_type=std_logic lab=tail}
N 420 2280 420 2280 {lab=nbf}
C {devices/lab_pin.sym} 420 2280 0 1 {name=p348 sig_type=std_logic lab=nbf}
N 460 2310 460 2310 {lab=gnd}
C {devices/lab_pin.sym} 460 2310 0 0 {name=p349 sig_type=std_logic lab=gnd}
N 460 2280 460 2280 {lab=gnd}
C {devices/lab_pin.sym} 460 2280 0 0 {name=p350 sig_type=std_logic lab=gnd}
C {devices/res.sym} 660 2280 0 0 {name=rbf
value=1000000.0
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 660 2250 660 2250 {lab=nb}
C {devices/lab_pin.sym} 660 2250 0 0 {name=p351 sig_type=std_logic lab=nb}
N 660 2310 660 2310 {lab=nbf}
C {devices/lab_pin.sym} 660 2310 0 0 {name=p352 sig_type=std_logic lab=nbf}
C {sg13g2_pr/cap_cmim.sym} 880 2280 0 0 {name=cbf0
model=cap_cmim
lvs_model=cmim
w=6.900700e-05
l=6.900700e-05
m=1
mm_ok=1
spiceprefix=X
}
N 880 2250 880 2250 {lab=nbf}
C {devices/lab_pin.sym} 880 2250 0 0 {name=p353 sig_type=std_logic lab=nbf}
N 880 2310 880 2310 {lab=gnd}
C {devices/lab_pin.sym} 880 2310 0 0 {name=p354 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_cmim.sym} 1100 2280 0 0 {name=cbf1
model=cap_cmim
lvs_model=cmim
w=6.900700e-05
l=6.900700e-05
m=1
mm_ok=1
spiceprefix=X
}
N 1100 2250 1100 2250 {lab=nbf}
C {devices/lab_pin.sym} 1100 2250 0 0 {name=p355 sig_type=std_logic lab=nbf}
N 1100 2310 1100 2310 {lab=gnd}
C {devices/lab_pin.sym} 1100 2310 0 0 {name=p356 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_cmim.sym} 0 2400 0 0 {name=cbf2
model=cap_cmim
lvs_model=cmim
w=6.900700e-05
l=6.900700e-05
m=1
mm_ok=1
spiceprefix=X
}
N 0 2370 0 2370 {lab=nbf}
C {devices/lab_pin.sym} 0 2370 0 0 {name=p357 sig_type=std_logic lab=nbf}
N 0 2430 0 2430 {lab=gnd}
C {devices/lab_pin.sym} 0 2430 0 0 {name=p358 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_cmim.sym} 220 2400 0 0 {name=cbf3
model=cap_cmim
lvs_model=cmim
w=6.900700e-05
l=6.900700e-05
m=1
mm_ok=1
spiceprefix=X
}
N 220 2370 220 2370 {lab=nbf}
C {devices/lab_pin.sym} 220 2370 0 0 {name=p359 sig_type=std_logic lab=nbf}
N 220 2430 220 2430 {lab=gnd}
C {devices/lab_pin.sym} 220 2430 0 0 {name=p360 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_cmim.sym} 440 2400 0 0 {name=cbf4
model=cap_cmim
lvs_model=cmim
w=6.900700e-05
l=6.900700e-05
m=1
mm_ok=1
spiceprefix=X
}
N 440 2370 440 2370 {lab=nbf}
C {devices/lab_pin.sym} 440 2370 0 0 {name=p361 sig_type=std_logic lab=nbf}
N 440 2430 440 2430 {lab=gnd}
C {devices/lab_pin.sym} 440 2430 0 0 {name=p362 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_cmim.sym} 660 2400 0 0 {name=cbf5
model=cap_cmim
lvs_model=cmim
w=6.900700e-05
l=6.900700e-05
m=1
mm_ok=1
spiceprefix=X
}
N 660 2370 660 2370 {lab=nbf}
C {devices/lab_pin.sym} 660 2370 0 0 {name=p363 sig_type=std_logic lab=nbf}
N 660 2430 660 2430 {lab=gnd}
C {devices/lab_pin.sym} 660 2430 0 0 {name=p364 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_cmim.sym} 880 2400 0 0 {name=cbf6
model=cap_cmim
lvs_model=cmim
w=6.900700e-05
l=6.900700e-05
m=1
mm_ok=1
spiceprefix=X
}
N 880 2370 880 2370 {lab=nbf}
C {devices/lab_pin.sym} 880 2370 0 0 {name=p365 sig_type=std_logic lab=nbf}
N 880 2430 880 2430 {lab=gnd}
C {devices/lab_pin.sym} 880 2430 0 0 {name=p366 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 2400 0 0 {name=mr
w=20u
l=4u
ng=4
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 2370 1120 2370 {lab=nb}
C {devices/lab_pin.sym} 1120 2370 0 0 {name=p367 sig_type=std_logic lab=nb}
N 1080 2400 1080 2400 {lab=nb}
C {devices/lab_pin.sym} 1080 2400 0 1 {name=p368 sig_type=std_logic lab=nb}
N 1120 2430 1120 2430 {lab=gnd}
C {devices/lab_pin.sym} 1120 2430 0 0 {name=p369 sig_type=std_logic lab=gnd}
N 1120 2400 1120 2400 {lab=gnd}
C {devices/lab_pin.sym} 1120 2400 0 0 {name=p370 sig_type=std_logic lab=gnd}
C {devices/isource.sym} 0 2520 0 0 {name=iref value=0.0005}
N 0 2490 0 2490 {lab=vdd}
C {devices/lab_pin.sym} 0 2490 0 0 {name=p371 sig_type=std_logic lab=vdd}
N 0 2550 0 2550 {lab=nb}
C {devices/lab_pin.sym} 0 2550 0 0 {name=p372 sig_type=std_logic lab=nb}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 2520 0 0 {name=mbp_rbf
w=20u
l=0.13u
ng=4
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 2490 240 2490 {lab=nb}
C {devices/lab_pin.sym} 240 2490 0 0 {name=p373 sig_type=std_logic lab=nb}
N 200 2520 200 2520 {lab=vbp_tail}
C {devices/lab_pin.sym} 200 2520 0 1 {name=p374 sig_type=std_logic lab=vbp_tail}
N 240 2550 240 2550 {lab=nbf}
C {devices/lab_pin.sym} 240 2550 0 0 {name=p375 sig_type=std_logic lab=nbf}
N 240 2520 240 2520 {lab=gnd}
C {devices/lab_pin.sym} 240 2520 0 0 {name=p376 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 2520 0 0 {name=mb1
w=10u
l=0.13u
ng=4
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 2490 460 2490 {lab=op}
C {devices/lab_pin.sym} 460 2490 0 0 {name=p377 sig_type=std_logic lab=op}
N 420 2520 420 2520 {lab=tp}
C {devices/lab_pin.sym} 420 2520 0 1 {name=p378 sig_type=std_logic lab=tp}
N 460 2550 460 2550 {lab=tb}
C {devices/lab_pin.sym} 460 2550 0 0 {name=p379 sig_type=std_logic lab=tb}
N 460 2520 460 2520 {lab=gnd}
C {devices/lab_pin.sym} 460 2520 0 0 {name=p380 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 2520 0 0 {name=mb2
w=10u
l=0.13u
ng=4
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 2490 680 2490 {lab=on}
C {devices/lab_pin.sym} 680 2490 0 0 {name=p381 sig_type=std_logic lab=on}
N 640 2520 640 2520 {lab=tn}
C {devices/lab_pin.sym} 640 2520 0 1 {name=p382 sig_type=std_logic lab=tn}
N 680 2550 680 2550 {lab=tb}
C {devices/lab_pin.sym} 680 2550 0 0 {name=p383 sig_type=std_logic lab=tb}
N 680 2520 680 2520 {lab=gnd}
C {devices/lab_pin.sym} 680 2520 0 0 {name=p384 sig_type=std_logic lab=gnd}
C {devices/res.sym} 880 2520 0 0 {name=rl1
value=400
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 2490 880 2490 {lab=vdd}
C {devices/lab_pin.sym} 880 2490 0 0 {name=p385 sig_type=std_logic lab=vdd}
N 880 2550 880 2550 {lab=op}
C {devices/lab_pin.sym} 880 2550 0 0 {name=p386 sig_type=std_logic lab=op}
C {devices/res.sym} 1100 2520 0 0 {name=rl2
value=400
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 1100 2490 1100 2490 {lab=vdd}
C {devices/lab_pin.sym} 1100 2490 0 0 {name=p387 sig_type=std_logic lab=vdd}
N 1100 2550 1100 2550 {lab=on}
C {devices/lab_pin.sym} 1100 2550 0 0 {name=p388 sig_type=std_logic lab=on}
C {devices/isource.sym} 0 2640 0 0 {name=ib value=0.001}
N 0 2610 0 2610 {lab=tb}
C {devices/lab_pin.sym} 0 2610 0 0 {name=p389 sig_type=std_logic lab=tb}
N 0 2670 0 2670 {lab=gnd}
C {devices/lab_pin.sym} 0 2670 0 0 {name=p390 sig_type=std_logic lab=gnd}
C {devices/capa.sym} 220 2640 0 0 {name=ctb
value=2e-12
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 220 2610 220 2610 {lab=tb}
C {devices/lab_pin.sym} 220 2610 0 0 {name=p391 sig_type=std_logic lab=tb}
N 220 2670 220 2670 {lab=gnd}
C {devices/lab_pin.sym} 220 2670 0 0 {name=p392 sig_type=std_logic lab=gnd}
C {devices/capa.sym} 440 2640 0 0 {name=cl1
value=2e-14
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 440 2610 440 2610 {lab=op}
C {devices/lab_pin.sym} 440 2610 0 0 {name=p393 sig_type=std_logic lab=op}
N 440 2670 440 2670 {lab=gnd}
C {devices/lab_pin.sym} 440 2670 0 0 {name=p394 sig_type=std_logic lab=gnd}
C {devices/capa.sym} 660 2640 0 0 {name=cl2
value=2e-14
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 660 2610 660 2610 {lab=on}
C {devices/lab_pin.sym} 660 2610 0 0 {name=p395 sig_type=std_logic lab=on}
N 660 2670 660 2670 {lab=gnd}
C {devices/lab_pin.sym} 660 2670 0 0 {name=p396 sig_type=std_logic lab=gnd}
