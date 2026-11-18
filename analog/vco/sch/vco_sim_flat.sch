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
C {devices/lab_pin.sym} 200 40 0 0 {name=ttitle lab=vco_sim_flat_from_sch}
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
w=9u
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
w=19.8u
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
w=39.12u
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
w=0.15u
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
w=0.15u
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
w=77.5u
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
w=0.31u
l=0.13u
ng=1
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
w=0.31u
l=0.13u
ng=1
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
w=154.38u
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
w=0.62u
l=0.13u
ng=1
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
w=0.62u
l=0.13u
ng=1
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
w=308.5u
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
ng=1
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
ng=1
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
w=308.5u
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
ng=1
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
ng=1
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
w=308.5u
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
ng=1
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
ng=1
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
w=308.5u
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
ng=1
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
ng=1
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
w=308.5u
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
ng=1
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
ng=1
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
w=308.5u
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
ng=1
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
ng=1
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
w=308.5u
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
ng=1
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
ng=1
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
w=308.5u
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
ng=1
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
ng=1
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
C {sg13g2_pr/sg13_lv_pmos.sym} 220 2280 0 0 {name=mdb_b0
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 2310 240 2310 {lab=xd_b0}
C {devices/lab_pin.sym} 240 2310 0 0 {name=p345 sig_type=std_logic lab=xd_b0}
N 200 2280 200 2280 {lab=pbias}
C {devices/lab_pin.sym} 200 2280 0 1 {name=p346 sig_type=std_logic lab=pbias}
N 240 2250 240 2250 {lab=vdd}
C {devices/lab_pin.sym} 240 2250 0 0 {name=p347 sig_type=std_logic lab=vdd}
N 240 2280 240 2280 {lab=vdd}
C {devices/lab_pin.sym} 240 2280 0 0 {name=p348 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 2280 0 0 {name=msw_b0
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 2310 460 2310 {lab=xraw}
C {devices/lab_pin.sym} 460 2310 0 0 {name=p349 sig_type=std_logic lab=xraw}
N 420 2280 420 2280 {lab=code_gnd}
C {devices/lab_pin.sym} 420 2280 0 1 {name=p350 sig_type=std_logic lab=code_gnd}
N 460 2250 460 2250 {lab=xd_b0}
C {devices/lab_pin.sym} 460 2250 0 0 {name=p351 sig_type=std_logic lab=xd_b0}
N 460 2280 460 2280 {lab=vdd}
C {devices/lab_pin.sym} 460 2280 0 0 {name=p352 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 2280 0 0 {name=mdb_b1
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 2310 680 2310 {lab=xd_b1}
C {devices/lab_pin.sym} 680 2310 0 0 {name=p353 sig_type=std_logic lab=xd_b1}
N 640 2280 640 2280 {lab=pbias}
C {devices/lab_pin.sym} 640 2280 0 1 {name=p354 sig_type=std_logic lab=pbias}
N 680 2250 680 2250 {lab=vdd}
C {devices/lab_pin.sym} 680 2250 0 0 {name=p355 sig_type=std_logic lab=vdd}
N 680 2280 680 2280 {lab=vdd}
C {devices/lab_pin.sym} 680 2280 0 0 {name=p356 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 2280 0 0 {name=msw_b1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 2310 900 2310 {lab=xraw}
C {devices/lab_pin.sym} 900 2310 0 0 {name=p357 sig_type=std_logic lab=xraw}
N 860 2280 860 2280 {lab=code_gnd}
C {devices/lab_pin.sym} 860 2280 0 1 {name=p358 sig_type=std_logic lab=code_gnd}
N 900 2250 900 2250 {lab=xd_b1}
C {devices/lab_pin.sym} 900 2250 0 0 {name=p359 sig_type=std_logic lab=xd_b1}
N 900 2280 900 2280 {lab=vdd}
C {devices/lab_pin.sym} 900 2280 0 0 {name=p360 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 2280 0 0 {name=mdb_b2
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 2310 1120 2310 {lab=xd_b2}
C {devices/lab_pin.sym} 1120 2310 0 0 {name=p361 sig_type=std_logic lab=xd_b2}
N 1080 2280 1080 2280 {lab=pbias}
C {devices/lab_pin.sym} 1080 2280 0 1 {name=p362 sig_type=std_logic lab=pbias}
N 1120 2250 1120 2250 {lab=vdd}
C {devices/lab_pin.sym} 1120 2250 0 0 {name=p363 sig_type=std_logic lab=vdd}
N 1120 2280 1120 2280 {lab=vdd}
C {devices/lab_pin.sym} 1120 2280 0 0 {name=p364 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 2400 0 0 {name=msw_b2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 2430 20 2430 {lab=xraw}
C {devices/lab_pin.sym} 20 2430 0 0 {name=p365 sig_type=std_logic lab=xraw}
N -20 2400 -20 2400 {lab=code_gnd}
C {devices/lab_pin.sym} -20 2400 0 1 {name=p366 sig_type=std_logic lab=code_gnd}
N 20 2370 20 2370 {lab=xd_b2}
C {devices/lab_pin.sym} 20 2370 0 0 {name=p367 sig_type=std_logic lab=xd_b2}
N 20 2400 20 2400 {lab=vdd}
C {devices/lab_pin.sym} 20 2400 0 0 {name=p368 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 2400 0 0 {name=mdb_b3
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 2430 240 2430 {lab=xd_b3}
C {devices/lab_pin.sym} 240 2430 0 0 {name=p369 sig_type=std_logic lab=xd_b3}
N 200 2400 200 2400 {lab=pbias}
C {devices/lab_pin.sym} 200 2400 0 1 {name=p370 sig_type=std_logic lab=pbias}
N 240 2370 240 2370 {lab=vdd}
C {devices/lab_pin.sym} 240 2370 0 0 {name=p371 sig_type=std_logic lab=vdd}
N 240 2400 240 2400 {lab=vdd}
C {devices/lab_pin.sym} 240 2400 0 0 {name=p372 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 2400 0 0 {name=msw_b3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 2430 460 2430 {lab=xraw}
C {devices/lab_pin.sym} 460 2430 0 0 {name=p373 sig_type=std_logic lab=xraw}
N 420 2400 420 2400 {lab=code_gnd}
C {devices/lab_pin.sym} 420 2400 0 1 {name=p374 sig_type=std_logic lab=code_gnd}
N 460 2370 460 2370 {lab=xd_b3}
C {devices/lab_pin.sym} 460 2370 0 0 {name=p375 sig_type=std_logic lab=xd_b3}
N 460 2400 460 2400 {lab=vdd}
C {devices/lab_pin.sym} 460 2400 0 0 {name=p376 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 2400 0 0 {name=mdb_b4
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 2430 680 2430 {lab=xd_b4}
C {devices/lab_pin.sym} 680 2430 0 0 {name=p377 sig_type=std_logic lab=xd_b4}
N 640 2400 640 2400 {lab=pbias}
C {devices/lab_pin.sym} 640 2400 0 1 {name=p378 sig_type=std_logic lab=pbias}
N 680 2370 680 2370 {lab=vdd}
C {devices/lab_pin.sym} 680 2370 0 0 {name=p379 sig_type=std_logic lab=vdd}
N 680 2400 680 2400 {lab=vdd}
C {devices/lab_pin.sym} 680 2400 0 0 {name=p380 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 2400 0 0 {name=msw_b4
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 2430 900 2430 {lab=xraw}
C {devices/lab_pin.sym} 900 2430 0 0 {name=p381 sig_type=std_logic lab=xraw}
N 860 2400 860 2400 {lab=code_gnd}
C {devices/lab_pin.sym} 860 2400 0 1 {name=p382 sig_type=std_logic lab=code_gnd}
N 900 2370 900 2370 {lab=xd_b4}
C {devices/lab_pin.sym} 900 2370 0 0 {name=p383 sig_type=std_logic lab=xd_b4}
N 900 2400 900 2400 {lab=vdd}
C {devices/lab_pin.sym} 900 2400 0 0 {name=p384 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 2400 0 0 {name=mdb_b5
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 2430 1120 2430 {lab=xd_b5}
C {devices/lab_pin.sym} 1120 2430 0 0 {name=p385 sig_type=std_logic lab=xd_b5}
N 1080 2400 1080 2400 {lab=pbias}
C {devices/lab_pin.sym} 1080 2400 0 1 {name=p386 sig_type=std_logic lab=pbias}
N 1120 2370 1120 2370 {lab=vdd}
C {devices/lab_pin.sym} 1120 2370 0 0 {name=p387 sig_type=std_logic lab=vdd}
N 1120 2400 1120 2400 {lab=vdd}
C {devices/lab_pin.sym} 1120 2400 0 0 {name=p388 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 2520 0 0 {name=msw_b5
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 2550 20 2550 {lab=xraw}
C {devices/lab_pin.sym} 20 2550 0 0 {name=p389 sig_type=std_logic lab=xraw}
N -20 2520 -20 2520 {lab=code_gnd}
C {devices/lab_pin.sym} -20 2520 0 1 {name=p390 sig_type=std_logic lab=code_gnd}
N 20 2490 20 2490 {lab=xd_b5}
C {devices/lab_pin.sym} 20 2490 0 0 {name=p391 sig_type=std_logic lab=xd_b5}
N 20 2520 20 2520 {lab=vdd}
C {devices/lab_pin.sym} 20 2520 0 0 {name=p392 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 2520 0 0 {name=mdb_b6
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 2550 240 2550 {lab=xd_b6}
C {devices/lab_pin.sym} 240 2550 0 0 {name=p393 sig_type=std_logic lab=xd_b6}
N 200 2520 200 2520 {lab=pbias}
C {devices/lab_pin.sym} 200 2520 0 1 {name=p394 sig_type=std_logic lab=pbias}
N 240 2490 240 2490 {lab=vdd}
C {devices/lab_pin.sym} 240 2490 0 0 {name=p395 sig_type=std_logic lab=vdd}
N 240 2520 240 2520 {lab=vdd}
C {devices/lab_pin.sym} 240 2520 0 0 {name=p396 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 2520 0 0 {name=msw_b6
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 2550 460 2550 {lab=xraw}
C {devices/lab_pin.sym} 460 2550 0 0 {name=p397 sig_type=std_logic lab=xraw}
N 420 2520 420 2520 {lab=code_gnd}
C {devices/lab_pin.sym} 420 2520 0 1 {name=p398 sig_type=std_logic lab=code_gnd}
N 460 2490 460 2490 {lab=xd_b6}
C {devices/lab_pin.sym} 460 2490 0 0 {name=p399 sig_type=std_logic lab=xd_b6}
N 460 2520 460 2520 {lab=vdd}
C {devices/lab_pin.sym} 460 2520 0 0 {name=p400 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 2520 0 0 {name=mdb_b7
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 2550 680 2550 {lab=xd_b7}
C {devices/lab_pin.sym} 680 2550 0 0 {name=p401 sig_type=std_logic lab=xd_b7}
N 640 2520 640 2520 {lab=pbias}
C {devices/lab_pin.sym} 640 2520 0 1 {name=p402 sig_type=std_logic lab=pbias}
N 680 2490 680 2490 {lab=vdd}
C {devices/lab_pin.sym} 680 2490 0 0 {name=p403 sig_type=std_logic lab=vdd}
N 680 2520 680 2520 {lab=vdd}
C {devices/lab_pin.sym} 680 2520 0 0 {name=p404 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 2520 0 0 {name=msw_b7
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 2550 900 2550 {lab=xraw}
C {devices/lab_pin.sym} 900 2550 0 0 {name=p405 sig_type=std_logic lab=xraw}
N 860 2520 860 2520 {lab=code_gnd}
C {devices/lab_pin.sym} 860 2520 0 1 {name=p406 sig_type=std_logic lab=code_gnd}
N 900 2490 900 2490 {lab=xd_b7}
C {devices/lab_pin.sym} 900 2490 0 0 {name=p407 sig_type=std_logic lab=xd_b7}
N 900 2520 900 2520 {lab=vdd}
C {devices/lab_pin.sym} 900 2520 0 0 {name=p408 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 2520 0 0 {name=mdb_b8
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 2550 1120 2550 {lab=xd_b8}
C {devices/lab_pin.sym} 1120 2550 0 0 {name=p409 sig_type=std_logic lab=xd_b8}
N 1080 2520 1080 2520 {lab=pbias}
C {devices/lab_pin.sym} 1080 2520 0 1 {name=p410 sig_type=std_logic lab=pbias}
N 1120 2490 1120 2490 {lab=vdd}
C {devices/lab_pin.sym} 1120 2490 0 0 {name=p411 sig_type=std_logic lab=vdd}
N 1120 2520 1120 2520 {lab=vdd}
C {devices/lab_pin.sym} 1120 2520 0 0 {name=p412 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 2640 0 0 {name=msw_b8
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 2670 20 2670 {lab=xraw}
C {devices/lab_pin.sym} 20 2670 0 0 {name=p413 sig_type=std_logic lab=xraw}
N -20 2640 -20 2640 {lab=code_gnd}
C {devices/lab_pin.sym} -20 2640 0 1 {name=p414 sig_type=std_logic lab=code_gnd}
N 20 2610 20 2610 {lab=xd_b8}
C {devices/lab_pin.sym} 20 2610 0 0 {name=p415 sig_type=std_logic lab=xd_b8}
N 20 2640 20 2640 {lab=vdd}
C {devices/lab_pin.sym} 20 2640 0 0 {name=p416 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 2640 0 0 {name=mdb_b9
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 2670 240 2670 {lab=xd_b9}
C {devices/lab_pin.sym} 240 2670 0 0 {name=p417 sig_type=std_logic lab=xd_b9}
N 200 2640 200 2640 {lab=pbias}
C {devices/lab_pin.sym} 200 2640 0 1 {name=p418 sig_type=std_logic lab=pbias}
N 240 2610 240 2610 {lab=vdd}
C {devices/lab_pin.sym} 240 2610 0 0 {name=p419 sig_type=std_logic lab=vdd}
N 240 2640 240 2640 {lab=vdd}
C {devices/lab_pin.sym} 240 2640 0 0 {name=p420 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 2640 0 0 {name=msw_b9
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 2670 460 2670 {lab=xraw}
C {devices/lab_pin.sym} 460 2670 0 0 {name=p421 sig_type=std_logic lab=xraw}
N 420 2640 420 2640 {lab=code_gnd}
C {devices/lab_pin.sym} 420 2640 0 1 {name=p422 sig_type=std_logic lab=code_gnd}
N 460 2610 460 2610 {lab=xd_b9}
C {devices/lab_pin.sym} 460 2610 0 0 {name=p423 sig_type=std_logic lab=xd_b9}
N 460 2640 460 2640 {lab=vdd}
C {devices/lab_pin.sym} 460 2640 0 0 {name=p424 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 2640 0 0 {name=mdb_b10
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 2670 680 2670 {lab=xd_b10}
C {devices/lab_pin.sym} 680 2670 0 0 {name=p425 sig_type=std_logic lab=xd_b10}
N 640 2640 640 2640 {lab=pbias}
C {devices/lab_pin.sym} 640 2640 0 1 {name=p426 sig_type=std_logic lab=pbias}
N 680 2610 680 2610 {lab=vdd}
C {devices/lab_pin.sym} 680 2610 0 0 {name=p427 sig_type=std_logic lab=vdd}
N 680 2640 680 2640 {lab=vdd}
C {devices/lab_pin.sym} 680 2640 0 0 {name=p428 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 2640 0 0 {name=msw_b10
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 2670 900 2670 {lab=xraw}
C {devices/lab_pin.sym} 900 2670 0 0 {name=p429 sig_type=std_logic lab=xraw}
N 860 2640 860 2640 {lab=code_gnd}
C {devices/lab_pin.sym} 860 2640 0 1 {name=p430 sig_type=std_logic lab=code_gnd}
N 900 2610 900 2610 {lab=xd_b10}
C {devices/lab_pin.sym} 900 2610 0 0 {name=p431 sig_type=std_logic lab=xd_b10}
N 900 2640 900 2640 {lab=vdd}
C {devices/lab_pin.sym} 900 2640 0 0 {name=p432 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 2640 0 0 {name=mdb_b11
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 2670 1120 2670 {lab=xd_b11}
C {devices/lab_pin.sym} 1120 2670 0 0 {name=p433 sig_type=std_logic lab=xd_b11}
N 1080 2640 1080 2640 {lab=pbias}
C {devices/lab_pin.sym} 1080 2640 0 1 {name=p434 sig_type=std_logic lab=pbias}
N 1120 2610 1120 2610 {lab=vdd}
C {devices/lab_pin.sym} 1120 2610 0 0 {name=p435 sig_type=std_logic lab=vdd}
N 1120 2640 1120 2640 {lab=vdd}
C {devices/lab_pin.sym} 1120 2640 0 0 {name=p436 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 2760 0 0 {name=msw_b11
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 2790 20 2790 {lab=xraw}
C {devices/lab_pin.sym} 20 2790 0 0 {name=p437 sig_type=std_logic lab=xraw}
N -20 2760 -20 2760 {lab=code_gnd}
C {devices/lab_pin.sym} -20 2760 0 1 {name=p438 sig_type=std_logic lab=code_gnd}
N 20 2730 20 2730 {lab=xd_b11}
C {devices/lab_pin.sym} 20 2730 0 0 {name=p439 sig_type=std_logic lab=xd_b11}
N 20 2760 20 2760 {lab=vdd}
C {devices/lab_pin.sym} 20 2760 0 0 {name=p440 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 2760 0 0 {name=mdb_b12
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 2790 240 2790 {lab=xd_b12}
C {devices/lab_pin.sym} 240 2790 0 0 {name=p441 sig_type=std_logic lab=xd_b12}
N 200 2760 200 2760 {lab=pbias}
C {devices/lab_pin.sym} 200 2760 0 1 {name=p442 sig_type=std_logic lab=pbias}
N 240 2730 240 2730 {lab=vdd}
C {devices/lab_pin.sym} 240 2730 0 0 {name=p443 sig_type=std_logic lab=vdd}
N 240 2760 240 2760 {lab=vdd}
C {devices/lab_pin.sym} 240 2760 0 0 {name=p444 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 2760 0 0 {name=msw_b12
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 2790 460 2790 {lab=xraw}
C {devices/lab_pin.sym} 460 2790 0 0 {name=p445 sig_type=std_logic lab=xraw}
N 420 2760 420 2760 {lab=code_gnd}
C {devices/lab_pin.sym} 420 2760 0 1 {name=p446 sig_type=std_logic lab=code_gnd}
N 460 2730 460 2730 {lab=xd_b12}
C {devices/lab_pin.sym} 460 2730 0 0 {name=p447 sig_type=std_logic lab=xd_b12}
N 460 2760 460 2760 {lab=vdd}
C {devices/lab_pin.sym} 460 2760 0 0 {name=p448 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 2760 0 0 {name=mdb_b13
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 2790 680 2790 {lab=xd_b13}
C {devices/lab_pin.sym} 680 2790 0 0 {name=p449 sig_type=std_logic lab=xd_b13}
N 640 2760 640 2760 {lab=pbias}
C {devices/lab_pin.sym} 640 2760 0 1 {name=p450 sig_type=std_logic lab=pbias}
N 680 2730 680 2730 {lab=vdd}
C {devices/lab_pin.sym} 680 2730 0 0 {name=p451 sig_type=std_logic lab=vdd}
N 680 2760 680 2760 {lab=vdd}
C {devices/lab_pin.sym} 680 2760 0 0 {name=p452 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 2760 0 0 {name=msw_b13
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 2790 900 2790 {lab=xraw}
C {devices/lab_pin.sym} 900 2790 0 0 {name=p453 sig_type=std_logic lab=xraw}
N 860 2760 860 2760 {lab=code_gnd}
C {devices/lab_pin.sym} 860 2760 0 1 {name=p454 sig_type=std_logic lab=code_gnd}
N 900 2730 900 2730 {lab=xd_b13}
C {devices/lab_pin.sym} 900 2730 0 0 {name=p455 sig_type=std_logic lab=xd_b13}
N 900 2760 900 2760 {lab=vdd}
C {devices/lab_pin.sym} 900 2760 0 0 {name=p456 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 2760 0 0 {name=mdb_b14
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 2790 1120 2790 {lab=xd_b14}
C {devices/lab_pin.sym} 1120 2790 0 0 {name=p457 sig_type=std_logic lab=xd_b14}
N 1080 2760 1080 2760 {lab=pbias}
C {devices/lab_pin.sym} 1080 2760 0 1 {name=p458 sig_type=std_logic lab=pbias}
N 1120 2730 1120 2730 {lab=vdd}
C {devices/lab_pin.sym} 1120 2730 0 0 {name=p459 sig_type=std_logic lab=vdd}
N 1120 2760 1120 2760 {lab=vdd}
C {devices/lab_pin.sym} 1120 2760 0 0 {name=p460 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 2880 0 0 {name=msw_b14
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 2910 20 2910 {lab=xraw}
C {devices/lab_pin.sym} 20 2910 0 0 {name=p461 sig_type=std_logic lab=xraw}
N -20 2880 -20 2880 {lab=code_gnd}
C {devices/lab_pin.sym} -20 2880 0 1 {name=p462 sig_type=std_logic lab=code_gnd}
N 20 2850 20 2850 {lab=xd_b14}
C {devices/lab_pin.sym} 20 2850 0 0 {name=p463 sig_type=std_logic lab=xd_b14}
N 20 2880 20 2880 {lab=vdd}
C {devices/lab_pin.sym} 20 2880 0 0 {name=p464 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 2880 0 0 {name=mdb_b15
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 2910 240 2910 {lab=xd_b15}
C {devices/lab_pin.sym} 240 2910 0 0 {name=p465 sig_type=std_logic lab=xd_b15}
N 200 2880 200 2880 {lab=pbias}
C {devices/lab_pin.sym} 200 2880 0 1 {name=p466 sig_type=std_logic lab=pbias}
N 240 2850 240 2850 {lab=vdd}
C {devices/lab_pin.sym} 240 2850 0 0 {name=p467 sig_type=std_logic lab=vdd}
N 240 2880 240 2880 {lab=vdd}
C {devices/lab_pin.sym} 240 2880 0 0 {name=p468 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 2880 0 0 {name=msw_b15
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 2910 460 2910 {lab=xraw}
C {devices/lab_pin.sym} 460 2910 0 0 {name=p469 sig_type=std_logic lab=xraw}
N 420 2880 420 2880 {lab=code_gnd}
C {devices/lab_pin.sym} 420 2880 0 1 {name=p470 sig_type=std_logic lab=code_gnd}
N 460 2850 460 2850 {lab=xd_b15}
C {devices/lab_pin.sym} 460 2850 0 0 {name=p471 sig_type=std_logic lab=xd_b15}
N 460 2880 460 2880 {lab=vdd}
C {devices/lab_pin.sym} 460 2880 0 0 {name=p472 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 2880 0 0 {name=mdb_b16
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 2910 680 2910 {lab=xd_b16}
C {devices/lab_pin.sym} 680 2910 0 0 {name=p473 sig_type=std_logic lab=xd_b16}
N 640 2880 640 2880 {lab=pbias}
C {devices/lab_pin.sym} 640 2880 0 1 {name=p474 sig_type=std_logic lab=pbias}
N 680 2850 680 2850 {lab=vdd}
C {devices/lab_pin.sym} 680 2850 0 0 {name=p475 sig_type=std_logic lab=vdd}
N 680 2880 680 2880 {lab=vdd}
C {devices/lab_pin.sym} 680 2880 0 0 {name=p476 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 2880 0 0 {name=msw_b16
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 2910 900 2910 {lab=xraw}
C {devices/lab_pin.sym} 900 2910 0 0 {name=p477 sig_type=std_logic lab=xraw}
N 860 2880 860 2880 {lab=code_gnd}
C {devices/lab_pin.sym} 860 2880 0 1 {name=p478 sig_type=std_logic lab=code_gnd}
N 900 2850 900 2850 {lab=xd_b16}
C {devices/lab_pin.sym} 900 2850 0 0 {name=p479 sig_type=std_logic lab=xd_b16}
N 900 2880 900 2880 {lab=vdd}
C {devices/lab_pin.sym} 900 2880 0 0 {name=p480 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 2880 0 0 {name=mdb_b17
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 2910 1120 2910 {lab=xd_b17}
C {devices/lab_pin.sym} 1120 2910 0 0 {name=p481 sig_type=std_logic lab=xd_b17}
N 1080 2880 1080 2880 {lab=pbias}
C {devices/lab_pin.sym} 1080 2880 0 1 {name=p482 sig_type=std_logic lab=pbias}
N 1120 2850 1120 2850 {lab=vdd}
C {devices/lab_pin.sym} 1120 2850 0 0 {name=p483 sig_type=std_logic lab=vdd}
N 1120 2880 1120 2880 {lab=vdd}
C {devices/lab_pin.sym} 1120 2880 0 0 {name=p484 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 3000 0 0 {name=msw_b17
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 3030 20 3030 {lab=xraw}
C {devices/lab_pin.sym} 20 3030 0 0 {name=p485 sig_type=std_logic lab=xraw}
N -20 3000 -20 3000 {lab=code_gnd}
C {devices/lab_pin.sym} -20 3000 0 1 {name=p486 sig_type=std_logic lab=code_gnd}
N 20 2970 20 2970 {lab=xd_b17}
C {devices/lab_pin.sym} 20 2970 0 0 {name=p487 sig_type=std_logic lab=xd_b17}
N 20 3000 20 3000 {lab=vdd}
C {devices/lab_pin.sym} 20 3000 0 0 {name=p488 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 3000 0 0 {name=mdb_b18
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 3030 240 3030 {lab=xd_b18}
C {devices/lab_pin.sym} 240 3030 0 0 {name=p489 sig_type=std_logic lab=xd_b18}
N 200 3000 200 3000 {lab=pbias}
C {devices/lab_pin.sym} 200 3000 0 1 {name=p490 sig_type=std_logic lab=pbias}
N 240 2970 240 2970 {lab=vdd}
C {devices/lab_pin.sym} 240 2970 0 0 {name=p491 sig_type=std_logic lab=vdd}
N 240 3000 240 3000 {lab=vdd}
C {devices/lab_pin.sym} 240 3000 0 0 {name=p492 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 3000 0 0 {name=msw_b18
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 3030 460 3030 {lab=xraw}
C {devices/lab_pin.sym} 460 3030 0 0 {name=p493 sig_type=std_logic lab=xraw}
N 420 3000 420 3000 {lab=code_gnd}
C {devices/lab_pin.sym} 420 3000 0 1 {name=p494 sig_type=std_logic lab=code_gnd}
N 460 2970 460 2970 {lab=xd_b18}
C {devices/lab_pin.sym} 460 2970 0 0 {name=p495 sig_type=std_logic lab=xd_b18}
N 460 3000 460 3000 {lab=vdd}
C {devices/lab_pin.sym} 460 3000 0 0 {name=p496 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 3000 0 0 {name=mdb_b4_0
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 3030 680 3030 {lab=xd_b4_0}
C {devices/lab_pin.sym} 680 3030 0 0 {name=p497 sig_type=std_logic lab=xd_b4_0}
N 640 3000 640 3000 {lab=pbias}
C {devices/lab_pin.sym} 640 3000 0 1 {name=p498 sig_type=std_logic lab=pbias}
N 680 2970 680 2970 {lab=vdd}
C {devices/lab_pin.sym} 680 2970 0 0 {name=p499 sig_type=std_logic lab=vdd}
N 680 3000 680 3000 {lab=vdd}
C {devices/lab_pin.sym} 680 3000 0 0 {name=p500 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 3000 0 0 {name=msw_b4_0
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 3030 900 3030 {lab=xraw}
C {devices/lab_pin.sym} 900 3030 0 0 {name=p501 sig_type=std_logic lab=xraw}
N 860 3000 860 3000 {lab=code4}
C {devices/lab_pin.sym} 860 3000 0 1 {name=p502 sig_type=std_logic lab=code4}
N 900 2970 900 2970 {lab=xd_b4_0}
C {devices/lab_pin.sym} 900 2970 0 0 {name=p503 sig_type=std_logic lab=xd_b4_0}
N 900 3000 900 3000 {lab=vdd}
C {devices/lab_pin.sym} 900 3000 0 0 {name=p504 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 3000 0 0 {name=mdb_b3_0
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 3030 1120 3030 {lab=xd_b3_0}
C {devices/lab_pin.sym} 1120 3030 0 0 {name=p505 sig_type=std_logic lab=xd_b3_0}
N 1080 3000 1080 3000 {lab=pbias}
C {devices/lab_pin.sym} 1080 3000 0 1 {name=p506 sig_type=std_logic lab=pbias}
N 1120 2970 1120 2970 {lab=vdd}
C {devices/lab_pin.sym} 1120 2970 0 0 {name=p507 sig_type=std_logic lab=vdd}
N 1120 3000 1120 3000 {lab=vdd}
C {devices/lab_pin.sym} 1120 3000 0 0 {name=p508 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 3120 0 0 {name=msw_b3_0
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 3150 20 3150 {lab=xraw}
C {devices/lab_pin.sym} 20 3150 0 0 {name=p509 sig_type=std_logic lab=xraw}
N -20 3120 -20 3120 {lab=code3}
C {devices/lab_pin.sym} -20 3120 0 1 {name=p510 sig_type=std_logic lab=code3}
N 20 3090 20 3090 {lab=xd_b3_0}
C {devices/lab_pin.sym} 20 3090 0 0 {name=p511 sig_type=std_logic lab=xd_b3_0}
N 20 3120 20 3120 {lab=vdd}
C {devices/lab_pin.sym} 20 3120 0 0 {name=p512 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 3120 0 0 {name=mdb_b2_0
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 3150 240 3150 {lab=xd_b2_0}
C {devices/lab_pin.sym} 240 3150 0 0 {name=p513 sig_type=std_logic lab=xd_b2_0}
N 200 3120 200 3120 {lab=pbias}
C {devices/lab_pin.sym} 200 3120 0 1 {name=p514 sig_type=std_logic lab=pbias}
N 240 3090 240 3090 {lab=vdd}
C {devices/lab_pin.sym} 240 3090 0 0 {name=p515 sig_type=std_logic lab=vdd}
N 240 3120 240 3120 {lab=vdd}
C {devices/lab_pin.sym} 240 3120 0 0 {name=p516 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 3120 0 0 {name=msw_b2_0
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 3150 460 3150 {lab=xraw}
C {devices/lab_pin.sym} 460 3150 0 0 {name=p517 sig_type=std_logic lab=xraw}
N 420 3120 420 3120 {lab=code2}
C {devices/lab_pin.sym} 420 3120 0 1 {name=p518 sig_type=std_logic lab=code2}
N 460 3090 460 3090 {lab=xd_b2_0}
C {devices/lab_pin.sym} 460 3090 0 0 {name=p519 sig_type=std_logic lab=xd_b2_0}
N 460 3120 460 3120 {lab=vdd}
C {devices/lab_pin.sym} 460 3120 0 0 {name=p520 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 3120 0 0 {name=mdb_b4_1
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 3150 680 3150 {lab=xd_b4_1}
C {devices/lab_pin.sym} 680 3150 0 0 {name=p521 sig_type=std_logic lab=xd_b4_1}
N 640 3120 640 3120 {lab=pbias}
C {devices/lab_pin.sym} 640 3120 0 1 {name=p522 sig_type=std_logic lab=pbias}
N 680 3090 680 3090 {lab=vdd}
C {devices/lab_pin.sym} 680 3090 0 0 {name=p523 sig_type=std_logic lab=vdd}
N 680 3120 680 3120 {lab=vdd}
C {devices/lab_pin.sym} 680 3120 0 0 {name=p524 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 3120 0 0 {name=msw_b4_1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 3150 900 3150 {lab=xraw}
C {devices/lab_pin.sym} 900 3150 0 0 {name=p525 sig_type=std_logic lab=xraw}
N 860 3120 860 3120 {lab=code4}
C {devices/lab_pin.sym} 860 3120 0 1 {name=p526 sig_type=std_logic lab=code4}
N 900 3090 900 3090 {lab=xd_b4_1}
C {devices/lab_pin.sym} 900 3090 0 0 {name=p527 sig_type=std_logic lab=xd_b4_1}
N 900 3120 900 3120 {lab=vdd}
C {devices/lab_pin.sym} 900 3120 0 0 {name=p528 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 3120 0 0 {name=mdb_b3_1
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 3150 1120 3150 {lab=xd_b3_1}
C {devices/lab_pin.sym} 1120 3150 0 0 {name=p529 sig_type=std_logic lab=xd_b3_1}
N 1080 3120 1080 3120 {lab=pbias}
C {devices/lab_pin.sym} 1080 3120 0 1 {name=p530 sig_type=std_logic lab=pbias}
N 1120 3090 1120 3090 {lab=vdd}
C {devices/lab_pin.sym} 1120 3090 0 0 {name=p531 sig_type=std_logic lab=vdd}
N 1120 3120 1120 3120 {lab=vdd}
C {devices/lab_pin.sym} 1120 3120 0 0 {name=p532 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 3240 0 0 {name=msw_b3_1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 3270 20 3270 {lab=xraw}
C {devices/lab_pin.sym} 20 3270 0 0 {name=p533 sig_type=std_logic lab=xraw}
N -20 3240 -20 3240 {lab=code3}
C {devices/lab_pin.sym} -20 3240 0 1 {name=p534 sig_type=std_logic lab=code3}
N 20 3210 20 3210 {lab=xd_b3_1}
C {devices/lab_pin.sym} 20 3210 0 0 {name=p535 sig_type=std_logic lab=xd_b3_1}
N 20 3240 20 3240 {lab=vdd}
C {devices/lab_pin.sym} 20 3240 0 0 {name=p536 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 3240 0 0 {name=mdb_b4_2
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 3270 240 3270 {lab=xd_b4_2}
C {devices/lab_pin.sym} 240 3270 0 0 {name=p537 sig_type=std_logic lab=xd_b4_2}
N 200 3240 200 3240 {lab=pbias}
C {devices/lab_pin.sym} 200 3240 0 1 {name=p538 sig_type=std_logic lab=pbias}
N 240 3210 240 3210 {lab=vdd}
C {devices/lab_pin.sym} 240 3210 0 0 {name=p539 sig_type=std_logic lab=vdd}
N 240 3240 240 3240 {lab=vdd}
C {devices/lab_pin.sym} 240 3240 0 0 {name=p540 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 3240 0 0 {name=msw_b4_2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 3270 460 3270 {lab=xraw}
C {devices/lab_pin.sym} 460 3270 0 0 {name=p541 sig_type=std_logic lab=xraw}
N 420 3240 420 3240 {lab=code4}
C {devices/lab_pin.sym} 420 3240 0 1 {name=p542 sig_type=std_logic lab=code4}
N 460 3210 460 3210 {lab=xd_b4_2}
C {devices/lab_pin.sym} 460 3210 0 0 {name=p543 sig_type=std_logic lab=xd_b4_2}
N 460 3240 460 3240 {lab=vdd}
C {devices/lab_pin.sym} 460 3240 0 0 {name=p544 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 3240 0 0 {name=mdb_b1_0
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 3270 680 3270 {lab=xd_b1_0}
C {devices/lab_pin.sym} 680 3270 0 0 {name=p545 sig_type=std_logic lab=xd_b1_0}
N 640 3240 640 3240 {lab=pbias}
C {devices/lab_pin.sym} 640 3240 0 1 {name=p546 sig_type=std_logic lab=pbias}
N 680 3210 680 3210 {lab=vdd}
C {devices/lab_pin.sym} 680 3210 0 0 {name=p547 sig_type=std_logic lab=vdd}
N 680 3240 680 3240 {lab=vdd}
C {devices/lab_pin.sym} 680 3240 0 0 {name=p548 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 3240 0 0 {name=msw_b1_0
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 3270 900 3270 {lab=xraw}
C {devices/lab_pin.sym} 900 3270 0 0 {name=p549 sig_type=std_logic lab=xraw}
N 860 3240 860 3240 {lab=code1}
C {devices/lab_pin.sym} 860 3240 0 1 {name=p550 sig_type=std_logic lab=code1}
N 900 3210 900 3210 {lab=xd_b1_0}
C {devices/lab_pin.sym} 900 3210 0 0 {name=p551 sig_type=std_logic lab=xd_b1_0}
N 900 3240 900 3240 {lab=vdd}
C {devices/lab_pin.sym} 900 3240 0 0 {name=p552 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 3240 0 0 {name=mdb_b4_3
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 3270 1120 3270 {lab=xd_b4_3}
C {devices/lab_pin.sym} 1120 3270 0 0 {name=p553 sig_type=std_logic lab=xd_b4_3}
N 1080 3240 1080 3240 {lab=pbias}
C {devices/lab_pin.sym} 1080 3240 0 1 {name=p554 sig_type=std_logic lab=pbias}
N 1120 3210 1120 3210 {lab=vdd}
C {devices/lab_pin.sym} 1120 3210 0 0 {name=p555 sig_type=std_logic lab=vdd}
N 1120 3240 1120 3240 {lab=vdd}
C {devices/lab_pin.sym} 1120 3240 0 0 {name=p556 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 3360 0 0 {name=msw_b4_3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 3390 20 3390 {lab=xraw}
C {devices/lab_pin.sym} 20 3390 0 0 {name=p557 sig_type=std_logic lab=xraw}
N -20 3360 -20 3360 {lab=code4}
C {devices/lab_pin.sym} -20 3360 0 1 {name=p558 sig_type=std_logic lab=code4}
N 20 3330 20 3330 {lab=xd_b4_3}
C {devices/lab_pin.sym} 20 3330 0 0 {name=p559 sig_type=std_logic lab=xd_b4_3}
N 20 3360 20 3360 {lab=vdd}
C {devices/lab_pin.sym} 20 3360 0 0 {name=p560 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 3360 0 0 {name=mdb_b4_4
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 3390 240 3390 {lab=xd_b4_4}
C {devices/lab_pin.sym} 240 3390 0 0 {name=p561 sig_type=std_logic lab=xd_b4_4}
N 200 3360 200 3360 {lab=pbias}
C {devices/lab_pin.sym} 200 3360 0 1 {name=p562 sig_type=std_logic lab=pbias}
N 240 3330 240 3330 {lab=vdd}
C {devices/lab_pin.sym} 240 3330 0 0 {name=p563 sig_type=std_logic lab=vdd}
N 240 3360 240 3360 {lab=vdd}
C {devices/lab_pin.sym} 240 3360 0 0 {name=p564 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 3360 0 0 {name=msw_b4_4
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 3390 460 3390 {lab=xraw}
C {devices/lab_pin.sym} 460 3390 0 0 {name=p565 sig_type=std_logic lab=xraw}
N 420 3360 420 3360 {lab=code4}
C {devices/lab_pin.sym} 420 3360 0 1 {name=p566 sig_type=std_logic lab=code4}
N 460 3330 460 3330 {lab=xd_b4_4}
C {devices/lab_pin.sym} 460 3330 0 0 {name=p567 sig_type=std_logic lab=xd_b4_4}
N 460 3360 460 3360 {lab=vdd}
C {devices/lab_pin.sym} 460 3360 0 0 {name=p568 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 3360 0 0 {name=mdb_b0_0
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 3390 680 3390 {lab=xd_b0_0}
C {devices/lab_pin.sym} 680 3390 0 0 {name=p569 sig_type=std_logic lab=xd_b0_0}
N 640 3360 640 3360 {lab=pbias}
C {devices/lab_pin.sym} 640 3360 0 1 {name=p570 sig_type=std_logic lab=pbias}
N 680 3330 680 3330 {lab=vdd}
C {devices/lab_pin.sym} 680 3330 0 0 {name=p571 sig_type=std_logic lab=vdd}
N 680 3360 680 3360 {lab=vdd}
C {devices/lab_pin.sym} 680 3360 0 0 {name=p572 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 3360 0 0 {name=msw_b0_0
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 3390 900 3390 {lab=xraw}
C {devices/lab_pin.sym} 900 3390 0 0 {name=p573 sig_type=std_logic lab=xraw}
N 860 3360 860 3360 {lab=code0}
C {devices/lab_pin.sym} 860 3360 0 1 {name=p574 sig_type=std_logic lab=code0}
N 900 3330 900 3330 {lab=xd_b0_0}
C {devices/lab_pin.sym} 900 3330 0 0 {name=p575 sig_type=std_logic lab=xd_b0_0}
N 900 3360 900 3360 {lab=vdd}
C {devices/lab_pin.sym} 900 3360 0 0 {name=p576 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 3360 0 0 {name=mdb_b4_5
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 3390 1120 3390 {lab=xd_b4_5}
C {devices/lab_pin.sym} 1120 3390 0 0 {name=p577 sig_type=std_logic lab=xd_b4_5}
N 1080 3360 1080 3360 {lab=pbias}
C {devices/lab_pin.sym} 1080 3360 0 1 {name=p578 sig_type=std_logic lab=pbias}
N 1120 3330 1120 3330 {lab=vdd}
C {devices/lab_pin.sym} 1120 3330 0 0 {name=p579 sig_type=std_logic lab=vdd}
N 1120 3360 1120 3360 {lab=vdd}
C {devices/lab_pin.sym} 1120 3360 0 0 {name=p580 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 3480 0 0 {name=msw_b4_5
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 3510 20 3510 {lab=xraw}
C {devices/lab_pin.sym} 20 3510 0 0 {name=p581 sig_type=std_logic lab=xraw}
N -20 3480 -20 3480 {lab=code4}
C {devices/lab_pin.sym} -20 3480 0 1 {name=p582 sig_type=std_logic lab=code4}
N 20 3450 20 3450 {lab=xd_b4_5}
C {devices/lab_pin.sym} 20 3450 0 0 {name=p583 sig_type=std_logic lab=xd_b4_5}
N 20 3480 20 3480 {lab=vdd}
C {devices/lab_pin.sym} 20 3480 0 0 {name=p584 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 3480 0 0 {name=mdb_b3_2
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 3510 240 3510 {lab=xd_b3_2}
C {devices/lab_pin.sym} 240 3510 0 0 {name=p585 sig_type=std_logic lab=xd_b3_2}
N 200 3480 200 3480 {lab=pbias}
C {devices/lab_pin.sym} 200 3480 0 1 {name=p586 sig_type=std_logic lab=pbias}
N 240 3450 240 3450 {lab=vdd}
C {devices/lab_pin.sym} 240 3450 0 0 {name=p587 sig_type=std_logic lab=vdd}
N 240 3480 240 3480 {lab=vdd}
C {devices/lab_pin.sym} 240 3480 0 0 {name=p588 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 3480 0 0 {name=msw_b3_2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 3510 460 3510 {lab=xraw}
C {devices/lab_pin.sym} 460 3510 0 0 {name=p589 sig_type=std_logic lab=xraw}
N 420 3480 420 3480 {lab=code3}
C {devices/lab_pin.sym} 420 3480 0 1 {name=p590 sig_type=std_logic lab=code3}
N 460 3450 460 3450 {lab=xd_b3_2}
C {devices/lab_pin.sym} 460 3450 0 0 {name=p591 sig_type=std_logic lab=xd_b3_2}
N 460 3480 460 3480 {lab=vdd}
C {devices/lab_pin.sym} 460 3480 0 0 {name=p592 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 3480 0 0 {name=mdb_b4_6
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 3510 680 3510 {lab=xd_b4_6}
C {devices/lab_pin.sym} 680 3510 0 0 {name=p593 sig_type=std_logic lab=xd_b4_6}
N 640 3480 640 3480 {lab=pbias}
C {devices/lab_pin.sym} 640 3480 0 1 {name=p594 sig_type=std_logic lab=pbias}
N 680 3450 680 3450 {lab=vdd}
C {devices/lab_pin.sym} 680 3450 0 0 {name=p595 sig_type=std_logic lab=vdd}
N 680 3480 680 3480 {lab=vdd}
C {devices/lab_pin.sym} 680 3480 0 0 {name=p596 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 3480 0 0 {name=msw_b4_6
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 3510 900 3510 {lab=xraw}
C {devices/lab_pin.sym} 900 3510 0 0 {name=p597 sig_type=std_logic lab=xraw}
N 860 3480 860 3480 {lab=code4}
C {devices/lab_pin.sym} 860 3480 0 1 {name=p598 sig_type=std_logic lab=code4}
N 900 3450 900 3450 {lab=xd_b4_6}
C {devices/lab_pin.sym} 900 3450 0 0 {name=p599 sig_type=std_logic lab=xd_b4_6}
N 900 3480 900 3480 {lab=vdd}
C {devices/lab_pin.sym} 900 3480 0 0 {name=p600 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 3480 0 0 {name=mdb_b2_1
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 3510 1120 3510 {lab=xd_b2_1}
C {devices/lab_pin.sym} 1120 3510 0 0 {name=p601 sig_type=std_logic lab=xd_b2_1}
N 1080 3480 1080 3480 {lab=pbias}
C {devices/lab_pin.sym} 1080 3480 0 1 {name=p602 sig_type=std_logic lab=pbias}
N 1120 3450 1120 3450 {lab=vdd}
C {devices/lab_pin.sym} 1120 3450 0 0 {name=p603 sig_type=std_logic lab=vdd}
N 1120 3480 1120 3480 {lab=vdd}
C {devices/lab_pin.sym} 1120 3480 0 0 {name=p604 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 3600 0 0 {name=msw_b2_1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 3630 20 3630 {lab=xraw}
C {devices/lab_pin.sym} 20 3630 0 0 {name=p605 sig_type=std_logic lab=xraw}
N -20 3600 -20 3600 {lab=code2}
C {devices/lab_pin.sym} -20 3600 0 1 {name=p606 sig_type=std_logic lab=code2}
N 20 3570 20 3570 {lab=xd_b2_1}
C {devices/lab_pin.sym} 20 3570 0 0 {name=p607 sig_type=std_logic lab=xd_b2_1}
N 20 3600 20 3600 {lab=vdd}
C {devices/lab_pin.sym} 20 3600 0 0 {name=p608 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 3600 0 0 {name=mdb_b3_3
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 3630 240 3630 {lab=xd_b3_3}
C {devices/lab_pin.sym} 240 3630 0 0 {name=p609 sig_type=std_logic lab=xd_b3_3}
N 200 3600 200 3600 {lab=pbias}
C {devices/lab_pin.sym} 200 3600 0 1 {name=p610 sig_type=std_logic lab=pbias}
N 240 3570 240 3570 {lab=vdd}
C {devices/lab_pin.sym} 240 3570 0 0 {name=p611 sig_type=std_logic lab=vdd}
N 240 3600 240 3600 {lab=vdd}
C {devices/lab_pin.sym} 240 3600 0 0 {name=p612 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 3600 0 0 {name=msw_b3_3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 3630 460 3630 {lab=xraw}
C {devices/lab_pin.sym} 460 3630 0 0 {name=p613 sig_type=std_logic lab=xraw}
N 420 3600 420 3600 {lab=code3}
C {devices/lab_pin.sym} 420 3600 0 1 {name=p614 sig_type=std_logic lab=code3}
N 460 3570 460 3570 {lab=xd_b3_3}
C {devices/lab_pin.sym} 460 3570 0 0 {name=p615 sig_type=std_logic lab=xd_b3_3}
N 460 3600 460 3600 {lab=vdd}
C {devices/lab_pin.sym} 460 3600 0 0 {name=p616 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 3600 0 0 {name=mdb_b4_7
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 3630 680 3630 {lab=xd_b4_7}
C {devices/lab_pin.sym} 680 3630 0 0 {name=p617 sig_type=std_logic lab=xd_b4_7}
N 640 3600 640 3600 {lab=pbias}
C {devices/lab_pin.sym} 640 3600 0 1 {name=p618 sig_type=std_logic lab=pbias}
N 680 3570 680 3570 {lab=vdd}
C {devices/lab_pin.sym} 680 3570 0 0 {name=p619 sig_type=std_logic lab=vdd}
N 680 3600 680 3600 {lab=vdd}
C {devices/lab_pin.sym} 680 3600 0 0 {name=p620 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 3600 0 0 {name=msw_b4_7
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 3630 900 3630 {lab=xraw}
C {devices/lab_pin.sym} 900 3630 0 0 {name=p621 sig_type=std_logic lab=xraw}
N 860 3600 860 3600 {lab=code4}
C {devices/lab_pin.sym} 860 3600 0 1 {name=p622 sig_type=std_logic lab=code4}
N 900 3570 900 3570 {lab=xd_b4_7}
C {devices/lab_pin.sym} 900 3570 0 0 {name=p623 sig_type=std_logic lab=xd_b4_7}
N 900 3600 900 3600 {lab=vdd}
C {devices/lab_pin.sym} 900 3600 0 0 {name=p624 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 3600 0 0 {name=mdb_b4_8
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 3630 1120 3630 {lab=xd_b4_8}
C {devices/lab_pin.sym} 1120 3630 0 0 {name=p625 sig_type=std_logic lab=xd_b4_8}
N 1080 3600 1080 3600 {lab=pbias}
C {devices/lab_pin.sym} 1080 3600 0 1 {name=p626 sig_type=std_logic lab=pbias}
N 1120 3570 1120 3570 {lab=vdd}
C {devices/lab_pin.sym} 1120 3570 0 0 {name=p627 sig_type=std_logic lab=vdd}
N 1120 3600 1120 3600 {lab=vdd}
C {devices/lab_pin.sym} 1120 3600 0 0 {name=p628 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 3720 0 0 {name=msw_b4_8
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 3750 20 3750 {lab=xraw}
C {devices/lab_pin.sym} 20 3750 0 0 {name=p629 sig_type=std_logic lab=xraw}
N -20 3720 -20 3720 {lab=code4}
C {devices/lab_pin.sym} -20 3720 0 1 {name=p630 sig_type=std_logic lab=code4}
N 20 3690 20 3690 {lab=xd_b4_8}
C {devices/lab_pin.sym} 20 3690 0 0 {name=p631 sig_type=std_logic lab=xd_b4_8}
N 20 3720 20 3720 {lab=vdd}
C {devices/lab_pin.sym} 20 3720 0 0 {name=p632 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 3720 0 0 {name=mdb_b3_4
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 3750 240 3750 {lab=xd_b3_4}
C {devices/lab_pin.sym} 240 3750 0 0 {name=p633 sig_type=std_logic lab=xd_b3_4}
N 200 3720 200 3720 {lab=pbias}
C {devices/lab_pin.sym} 200 3720 0 1 {name=p634 sig_type=std_logic lab=pbias}
N 240 3690 240 3690 {lab=vdd}
C {devices/lab_pin.sym} 240 3690 0 0 {name=p635 sig_type=std_logic lab=vdd}
N 240 3720 240 3720 {lab=vdd}
C {devices/lab_pin.sym} 240 3720 0 0 {name=p636 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 3720 0 0 {name=msw_b3_4
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 3750 460 3750 {lab=xraw}
C {devices/lab_pin.sym} 460 3750 0 0 {name=p637 sig_type=std_logic lab=xraw}
N 420 3720 420 3720 {lab=code3}
C {devices/lab_pin.sym} 420 3720 0 1 {name=p638 sig_type=std_logic lab=code3}
N 460 3690 460 3690 {lab=xd_b3_4}
C {devices/lab_pin.sym} 460 3690 0 0 {name=p639 sig_type=std_logic lab=xd_b3_4}
N 460 3720 460 3720 {lab=vdd}
C {devices/lab_pin.sym} 460 3720 0 0 {name=p640 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 3720 0 0 {name=mdb_b2_2
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 3750 680 3750 {lab=xd_b2_2}
C {devices/lab_pin.sym} 680 3750 0 0 {name=p641 sig_type=std_logic lab=xd_b2_2}
N 640 3720 640 3720 {lab=pbias}
C {devices/lab_pin.sym} 640 3720 0 1 {name=p642 sig_type=std_logic lab=pbias}
N 680 3690 680 3690 {lab=vdd}
C {devices/lab_pin.sym} 680 3690 0 0 {name=p643 sig_type=std_logic lab=vdd}
N 680 3720 680 3720 {lab=vdd}
C {devices/lab_pin.sym} 680 3720 0 0 {name=p644 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 3720 0 0 {name=msw_b2_2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 3750 900 3750 {lab=xraw}
C {devices/lab_pin.sym} 900 3750 0 0 {name=p645 sig_type=std_logic lab=xraw}
N 860 3720 860 3720 {lab=code2}
C {devices/lab_pin.sym} 860 3720 0 1 {name=p646 sig_type=std_logic lab=code2}
N 900 3690 900 3690 {lab=xd_b2_2}
C {devices/lab_pin.sym} 900 3690 0 0 {name=p647 sig_type=std_logic lab=xd_b2_2}
N 900 3720 900 3720 {lab=vdd}
C {devices/lab_pin.sym} 900 3720 0 0 {name=p648 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 3720 0 0 {name=mdb_b4_9
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 3750 1120 3750 {lab=xd_b4_9}
C {devices/lab_pin.sym} 1120 3750 0 0 {name=p649 sig_type=std_logic lab=xd_b4_9}
N 1080 3720 1080 3720 {lab=pbias}
C {devices/lab_pin.sym} 1080 3720 0 1 {name=p650 sig_type=std_logic lab=pbias}
N 1120 3690 1120 3690 {lab=vdd}
C {devices/lab_pin.sym} 1120 3690 0 0 {name=p651 sig_type=std_logic lab=vdd}
N 1120 3720 1120 3720 {lab=vdd}
C {devices/lab_pin.sym} 1120 3720 0 0 {name=p652 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 3840 0 0 {name=msw_b4_9
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 3870 20 3870 {lab=xraw}
C {devices/lab_pin.sym} 20 3870 0 0 {name=p653 sig_type=std_logic lab=xraw}
N -20 3840 -20 3840 {lab=code4}
C {devices/lab_pin.sym} -20 3840 0 1 {name=p654 sig_type=std_logic lab=code4}
N 20 3810 20 3810 {lab=xd_b4_9}
C {devices/lab_pin.sym} 20 3810 0 0 {name=p655 sig_type=std_logic lab=xd_b4_9}
N 20 3840 20 3840 {lab=vdd}
C {devices/lab_pin.sym} 20 3840 0 0 {name=p656 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 3840 0 0 {name=mdb_b3_5
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 3870 240 3870 {lab=xd_b3_5}
C {devices/lab_pin.sym} 240 3870 0 0 {name=p657 sig_type=std_logic lab=xd_b3_5}
N 200 3840 200 3840 {lab=pbias}
C {devices/lab_pin.sym} 200 3840 0 1 {name=p658 sig_type=std_logic lab=pbias}
N 240 3810 240 3810 {lab=vdd}
C {devices/lab_pin.sym} 240 3810 0 0 {name=p659 sig_type=std_logic lab=vdd}
N 240 3840 240 3840 {lab=vdd}
C {devices/lab_pin.sym} 240 3840 0 0 {name=p660 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 3840 0 0 {name=msw_b3_5
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 3870 460 3870 {lab=xraw}
C {devices/lab_pin.sym} 460 3870 0 0 {name=p661 sig_type=std_logic lab=xraw}
N 420 3840 420 3840 {lab=code3}
C {devices/lab_pin.sym} 420 3840 0 1 {name=p662 sig_type=std_logic lab=code3}
N 460 3810 460 3810 {lab=xd_b3_5}
C {devices/lab_pin.sym} 460 3810 0 0 {name=p663 sig_type=std_logic lab=xd_b3_5}
N 460 3840 460 3840 {lab=vdd}
C {devices/lab_pin.sym} 460 3840 0 0 {name=p664 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 3840 0 0 {name=mdb_b4_10
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 3870 680 3870 {lab=xd_b4_10}
C {devices/lab_pin.sym} 680 3870 0 0 {name=p665 sig_type=std_logic lab=xd_b4_10}
N 640 3840 640 3840 {lab=pbias}
C {devices/lab_pin.sym} 640 3840 0 1 {name=p666 sig_type=std_logic lab=pbias}
N 680 3810 680 3810 {lab=vdd}
C {devices/lab_pin.sym} 680 3810 0 0 {name=p667 sig_type=std_logic lab=vdd}
N 680 3840 680 3840 {lab=vdd}
C {devices/lab_pin.sym} 680 3840 0 0 {name=p668 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 3840 0 0 {name=msw_b4_10
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 3870 900 3870 {lab=xraw}
C {devices/lab_pin.sym} 900 3870 0 0 {name=p669 sig_type=std_logic lab=xraw}
N 860 3840 860 3840 {lab=code4}
C {devices/lab_pin.sym} 860 3840 0 1 {name=p670 sig_type=std_logic lab=code4}
N 900 3810 900 3810 {lab=xd_b4_10}
C {devices/lab_pin.sym} 900 3810 0 0 {name=p671 sig_type=std_logic lab=xd_b4_10}
N 900 3840 900 3840 {lab=vdd}
C {devices/lab_pin.sym} 900 3840 0 0 {name=p672 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 3840 0 0 {name=mdb_b1_1
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 3870 1120 3870 {lab=xd_b1_1}
C {devices/lab_pin.sym} 1120 3870 0 0 {name=p673 sig_type=std_logic lab=xd_b1_1}
N 1080 3840 1080 3840 {lab=pbias}
C {devices/lab_pin.sym} 1080 3840 0 1 {name=p674 sig_type=std_logic lab=pbias}
N 1120 3810 1120 3810 {lab=vdd}
C {devices/lab_pin.sym} 1120 3810 0 0 {name=p675 sig_type=std_logic lab=vdd}
N 1120 3840 1120 3840 {lab=vdd}
C {devices/lab_pin.sym} 1120 3840 0 0 {name=p676 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 3960 0 0 {name=msw_b1_1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 3990 20 3990 {lab=xraw}
C {devices/lab_pin.sym} 20 3990 0 0 {name=p677 sig_type=std_logic lab=xraw}
N -20 3960 -20 3960 {lab=code1}
C {devices/lab_pin.sym} -20 3960 0 1 {name=p678 sig_type=std_logic lab=code1}
N 20 3930 20 3930 {lab=xd_b1_1}
C {devices/lab_pin.sym} 20 3930 0 0 {name=p679 sig_type=std_logic lab=xd_b1_1}
N 20 3960 20 3960 {lab=vdd}
C {devices/lab_pin.sym} 20 3960 0 0 {name=p680 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 3960 0 0 {name=mdb_b4_11
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 3990 240 3990 {lab=xd_b4_11}
C {devices/lab_pin.sym} 240 3990 0 0 {name=p681 sig_type=std_logic lab=xd_b4_11}
N 200 3960 200 3960 {lab=pbias}
C {devices/lab_pin.sym} 200 3960 0 1 {name=p682 sig_type=std_logic lab=pbias}
N 240 3930 240 3930 {lab=vdd}
C {devices/lab_pin.sym} 240 3930 0 0 {name=p683 sig_type=std_logic lab=vdd}
N 240 3960 240 3960 {lab=vdd}
C {devices/lab_pin.sym} 240 3960 0 0 {name=p684 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 3960 0 0 {name=msw_b4_11
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 3990 460 3990 {lab=xraw}
C {devices/lab_pin.sym} 460 3990 0 0 {name=p685 sig_type=std_logic lab=xraw}
N 420 3960 420 3960 {lab=code4}
C {devices/lab_pin.sym} 420 3960 0 1 {name=p686 sig_type=std_logic lab=code4}
N 460 3930 460 3930 {lab=xd_b4_11}
C {devices/lab_pin.sym} 460 3930 0 0 {name=p687 sig_type=std_logic lab=xd_b4_11}
N 460 3960 460 3960 {lab=vdd}
C {devices/lab_pin.sym} 460 3960 0 0 {name=p688 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 3960 0 0 {name=mdb_b4_12
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 3990 680 3990 {lab=xd_b4_12}
C {devices/lab_pin.sym} 680 3990 0 0 {name=p689 sig_type=std_logic lab=xd_b4_12}
N 640 3960 640 3960 {lab=pbias}
C {devices/lab_pin.sym} 640 3960 0 1 {name=p690 sig_type=std_logic lab=pbias}
N 680 3930 680 3930 {lab=vdd}
C {devices/lab_pin.sym} 680 3930 0 0 {name=p691 sig_type=std_logic lab=vdd}
N 680 3960 680 3960 {lab=vdd}
C {devices/lab_pin.sym} 680 3960 0 0 {name=p692 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 3960 0 0 {name=msw_b4_12
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 3990 900 3990 {lab=xraw}
C {devices/lab_pin.sym} 900 3990 0 0 {name=p693 sig_type=std_logic lab=xraw}
N 860 3960 860 3960 {lab=code4}
C {devices/lab_pin.sym} 860 3960 0 1 {name=p694 sig_type=std_logic lab=code4}
N 900 3930 900 3930 {lab=xd_b4_12}
C {devices/lab_pin.sym} 900 3930 0 0 {name=p695 sig_type=std_logic lab=xd_b4_12}
N 900 3960 900 3960 {lab=vdd}
C {devices/lab_pin.sym} 900 3960 0 0 {name=p696 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 3960 0 0 {name=mdb_dmy
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 3990 1120 3990 {lab=xd_dmy}
C {devices/lab_pin.sym} 1120 3990 0 0 {name=p697 sig_type=std_logic lab=xd_dmy}
N 1080 3960 1080 3960 {lab=pbias}
C {devices/lab_pin.sym} 1080 3960 0 1 {name=p698 sig_type=std_logic lab=pbias}
N 1120 3930 1120 3930 {lab=vdd}
C {devices/lab_pin.sym} 1120 3930 0 0 {name=p699 sig_type=std_logic lab=vdd}
N 1120 3960 1120 3960 {lab=vdd}
C {devices/lab_pin.sym} 1120 3960 0 0 {name=p700 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 4080 0 0 {name=msw_dmy
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 4110 20 4110 {lab=xraw}
C {devices/lab_pin.sym} 20 4110 0 0 {name=p701 sig_type=std_logic lab=xraw}
N -20 4080 -20 4080 {lab=code_vdd}
C {devices/lab_pin.sym} -20 4080 0 1 {name=p702 sig_type=std_logic lab=code_vdd}
N 20 4050 20 4050 {lab=xd_dmy}
C {devices/lab_pin.sym} 20 4050 0 0 {name=p703 sig_type=std_logic lab=xd_dmy}
N 20 4080 20 4080 {lab=vdd}
C {devices/lab_pin.sym} 20 4080 0 0 {name=p704 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 4080 0 0 {name=mdb_b3_6
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 4110 240 4110 {lab=xd_b3_6}
C {devices/lab_pin.sym} 240 4110 0 0 {name=p705 sig_type=std_logic lab=xd_b3_6}
N 200 4080 200 4080 {lab=pbias}
C {devices/lab_pin.sym} 200 4080 0 1 {name=p706 sig_type=std_logic lab=pbias}
N 240 4050 240 4050 {lab=vdd}
C {devices/lab_pin.sym} 240 4050 0 0 {name=p707 sig_type=std_logic lab=vdd}
N 240 4080 240 4080 {lab=vdd}
C {devices/lab_pin.sym} 240 4080 0 0 {name=p708 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 4080 0 0 {name=msw_b3_6
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 4110 460 4110 {lab=xraw}
C {devices/lab_pin.sym} 460 4110 0 0 {name=p709 sig_type=std_logic lab=xraw}
N 420 4080 420 4080 {lab=code3}
C {devices/lab_pin.sym} 420 4080 0 1 {name=p710 sig_type=std_logic lab=code3}
N 460 4050 460 4050 {lab=xd_b3_6}
C {devices/lab_pin.sym} 460 4050 0 0 {name=p711 sig_type=std_logic lab=xd_b3_6}
N 460 4080 460 4080 {lab=vdd}
C {devices/lab_pin.sym} 460 4080 0 0 {name=p712 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 4080 0 0 {name=mdb_b4_13
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 4110 680 4110 {lab=xd_b4_13}
C {devices/lab_pin.sym} 680 4110 0 0 {name=p713 sig_type=std_logic lab=xd_b4_13}
N 640 4080 640 4080 {lab=pbias}
C {devices/lab_pin.sym} 640 4080 0 1 {name=p714 sig_type=std_logic lab=pbias}
N 680 4050 680 4050 {lab=vdd}
C {devices/lab_pin.sym} 680 4050 0 0 {name=p715 sig_type=std_logic lab=vdd}
N 680 4080 680 4080 {lab=vdd}
C {devices/lab_pin.sym} 680 4080 0 0 {name=p716 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 4080 0 0 {name=msw_b4_13
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 4110 900 4110 {lab=xraw}
C {devices/lab_pin.sym} 900 4110 0 0 {name=p717 sig_type=std_logic lab=xraw}
N 860 4080 860 4080 {lab=code4}
C {devices/lab_pin.sym} 860 4080 0 1 {name=p718 sig_type=std_logic lab=code4}
N 900 4050 900 4050 {lab=xd_b4_13}
C {devices/lab_pin.sym} 900 4050 0 0 {name=p719 sig_type=std_logic lab=xd_b4_13}
N 900 4080 900 4080 {lab=vdd}
C {devices/lab_pin.sym} 900 4080 0 0 {name=p720 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 4080 0 0 {name=mdb_b4_14
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 4110 1120 4110 {lab=xd_b4_14}
C {devices/lab_pin.sym} 1120 4110 0 0 {name=p721 sig_type=std_logic lab=xd_b4_14}
N 1080 4080 1080 4080 {lab=pbias}
C {devices/lab_pin.sym} 1080 4080 0 1 {name=p722 sig_type=std_logic lab=pbias}
N 1120 4050 1120 4050 {lab=vdd}
C {devices/lab_pin.sym} 1120 4050 0 0 {name=p723 sig_type=std_logic lab=vdd}
N 1120 4080 1120 4080 {lab=vdd}
C {devices/lab_pin.sym} 1120 4080 0 0 {name=p724 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 4200 0 0 {name=msw_b4_14
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 4230 20 4230 {lab=xraw}
C {devices/lab_pin.sym} 20 4230 0 0 {name=p725 sig_type=std_logic lab=xraw}
N -20 4200 -20 4200 {lab=code4}
C {devices/lab_pin.sym} -20 4200 0 1 {name=p726 sig_type=std_logic lab=code4}
N 20 4170 20 4170 {lab=xd_b4_14}
C {devices/lab_pin.sym} 20 4170 0 0 {name=p727 sig_type=std_logic lab=xd_b4_14}
N 20 4200 20 4200 {lab=vdd}
C {devices/lab_pin.sym} 20 4200 0 0 {name=p728 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 4200 0 0 {name=mdb_b2_3
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 4230 240 4230 {lab=xd_b2_3}
C {devices/lab_pin.sym} 240 4230 0 0 {name=p729 sig_type=std_logic lab=xd_b2_3}
N 200 4200 200 4200 {lab=pbias}
C {devices/lab_pin.sym} 200 4200 0 1 {name=p730 sig_type=std_logic lab=pbias}
N 240 4170 240 4170 {lab=vdd}
C {devices/lab_pin.sym} 240 4170 0 0 {name=p731 sig_type=std_logic lab=vdd}
N 240 4200 240 4200 {lab=vdd}
C {devices/lab_pin.sym} 240 4200 0 0 {name=p732 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 4200 0 0 {name=msw_b2_3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 4230 460 4230 {lab=xraw}
C {devices/lab_pin.sym} 460 4230 0 0 {name=p733 sig_type=std_logic lab=xraw}
N 420 4200 420 4200 {lab=code2}
C {devices/lab_pin.sym} 420 4200 0 1 {name=p734 sig_type=std_logic lab=code2}
N 460 4170 460 4170 {lab=xd_b2_3}
C {devices/lab_pin.sym} 460 4170 0 0 {name=p735 sig_type=std_logic lab=xd_b2_3}
N 460 4200 460 4200 {lab=vdd}
C {devices/lab_pin.sym} 460 4200 0 0 {name=p736 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 4200 0 0 {name=mdb_b3_7
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 4230 680 4230 {lab=xd_b3_7}
C {devices/lab_pin.sym} 680 4230 0 0 {name=p737 sig_type=std_logic lab=xd_b3_7}
N 640 4200 640 4200 {lab=pbias}
C {devices/lab_pin.sym} 640 4200 0 1 {name=p738 sig_type=std_logic lab=pbias}
N 680 4170 680 4170 {lab=vdd}
C {devices/lab_pin.sym} 680 4170 0 0 {name=p739 sig_type=std_logic lab=vdd}
N 680 4200 680 4200 {lab=vdd}
C {devices/lab_pin.sym} 680 4200 0 0 {name=p740 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 4200 0 0 {name=msw_b3_7
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 4230 900 4230 {lab=xraw}
C {devices/lab_pin.sym} 900 4230 0 0 {name=p741 sig_type=std_logic lab=xraw}
N 860 4200 860 4200 {lab=code3}
C {devices/lab_pin.sym} 860 4200 0 1 {name=p742 sig_type=std_logic lab=code3}
N 900 4170 900 4170 {lab=xd_b3_7}
C {devices/lab_pin.sym} 900 4170 0 0 {name=p743 sig_type=std_logic lab=xd_b3_7}
N 900 4200 900 4200 {lab=vdd}
C {devices/lab_pin.sym} 900 4200 0 0 {name=p744 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 4200 0 0 {name=mdb_b4_15
w=2u
l=2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 4230 1120 4230 {lab=xd_b4_15}
C {devices/lab_pin.sym} 1120 4230 0 0 {name=p745 sig_type=std_logic lab=xd_b4_15}
N 1080 4200 1080 4200 {lab=pbias}
C {devices/lab_pin.sym} 1080 4200 0 1 {name=p746 sig_type=std_logic lab=pbias}
N 1120 4170 1120 4170 {lab=vdd}
C {devices/lab_pin.sym} 1120 4170 0 0 {name=p747 sig_type=std_logic lab=vdd}
N 1120 4200 1120 4200 {lab=vdd}
C {devices/lab_pin.sym} 1120 4200 0 0 {name=p748 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 4320 0 0 {name=msw_b4_15
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 4350 20 4350 {lab=xraw}
C {devices/lab_pin.sym} 20 4350 0 0 {name=p749 sig_type=std_logic lab=xraw}
N -20 4320 -20 4320 {lab=code4}
C {devices/lab_pin.sym} -20 4320 0 1 {name=p750 sig_type=std_logic lab=code4}
N 20 4290 20 4290 {lab=xd_b4_15}
C {devices/lab_pin.sym} 20 4290 0 0 {name=p751 sig_type=std_logic lab=xd_b4_15}
N 20 4320 20 4320 {lab=vdd}
C {devices/lab_pin.sym} 20 4320 0 0 {name=p752 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 4320 0 0 {name=mt
w=480u
l=4u
ng=96
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 4290 240 4290 {lab=tail}
C {devices/lab_pin.sym} 240 4290 0 0 {name=p753 sig_type=std_logic lab=tail}
N 200 4320 200 4320 {lab=nbf}
C {devices/lab_pin.sym} 200 4320 0 1 {name=p754 sig_type=std_logic lab=nbf}
N 240 4350 240 4350 {lab=gnd}
C {devices/lab_pin.sym} 240 4350 0 0 {name=p755 sig_type=std_logic lab=gnd}
N 240 4320 240 4320 {lab=gnd}
C {devices/lab_pin.sym} 240 4320 0 0 {name=p756 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 4320 0 0 {name=mo1
w=8u
l=2u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 4290 460 4290 {lab=d1}
C {devices/lab_pin.sym} 460 4290 0 0 {name=p757 sig_type=std_logic lab=d1}
N 420 4320 420 4320 {lab=xraw}
C {devices/lab_pin.sym} 420 4320 0 1 {name=p758 sig_type=std_logic lab=xraw}
N 460 4350 460 4350 {lab=ss}
C {devices/lab_pin.sym} 460 4350 0 0 {name=p759 sig_type=std_logic lab=ss}
N 460 4320 460 4320 {lab=gnd}
C {devices/lab_pin.sym} 460 4320 0 0 {name=p760 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 4320 0 0 {name=mo2
w=8u
l=2u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 4290 680 4290 {lab=nb}
C {devices/lab_pin.sym} 680 4290 0 0 {name=p761 sig_type=std_logic lab=nb}
N 640 4320 640 4320 {lab=tail_f}
C {devices/lab_pin.sym} 640 4320 0 1 {name=p762 sig_type=std_logic lab=tail_f}
N 680 4350 680 4350 {lab=ss}
C {devices/lab_pin.sym} 680 4350 0 0 {name=p763 sig_type=std_logic lab=ss}
N 680 4320 680 4320 {lab=gnd}
C {devices/lab_pin.sym} 680 4320 0 0 {name=p764 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 4320 0 0 {name=mp1
w=4u
l=2u
ng=2
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 4350 900 4350 {lab=d1}
C {devices/lab_pin.sym} 900 4350 0 0 {name=p765 sig_type=std_logic lab=d1}
N 860 4320 860 4320 {lab=d1}
C {devices/lab_pin.sym} 860 4320 0 1 {name=p766 sig_type=std_logic lab=d1}
N 900 4290 900 4290 {lab=vdd}
C {devices/lab_pin.sym} 900 4290 0 0 {name=p767 sig_type=std_logic lab=vdd}
N 900 4320 900 4320 {lab=vdd}
C {devices/lab_pin.sym} 900 4320 0 0 {name=p768 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 4320 0 0 {name=mp2
w=4u
l=2u
ng=2
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 4350 1120 4350 {lab=nb}
C {devices/lab_pin.sym} 1120 4350 0 0 {name=p769 sig_type=std_logic lab=nb}
N 1080 4320 1080 4320 {lab=d1}
C {devices/lab_pin.sym} 1080 4320 0 1 {name=p770 sig_type=std_logic lab=d1}
N 1120 4290 1120 4290 {lab=vdd}
C {devices/lab_pin.sym} 1120 4290 0 0 {name=p771 sig_type=std_logic lab=vdd}
N 1120 4320 1120 4320 {lab=vdd}
C {devices/lab_pin.sym} 1120 4320 0 0 {name=p772 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 4440 0 0 {name=mdum_ota
w=8u
l=2u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 4410 20 4410 {lab=gnd}
C {devices/lab_pin.sym} 20 4410 0 0 {name=p773 sig_type=std_logic lab=gnd}
N -20 4440 -20 4440 {lab=gnd}
C {devices/lab_pin.sym} -20 4440 0 1 {name=p774 sig_type=std_logic lab=gnd}
N 20 4470 20 4470 {lab=gnd}
C {devices/lab_pin.sym} 20 4470 0 0 {name=p775 sig_type=std_logic lab=gnd}
N 20 4440 20 4440 {lab=gnd}
C {devices/lab_pin.sym} 20 4440 0 0 {name=p776 sig_type=std_logic lab=gnd}
C {sg13g2_pr/rhigh.sym} 220 4440 0 0 {name=rbf
w=5.000000e-07
l=2.128500e-05
b=16
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 220 4410 220 4410 {lab=nb}
C {devices/lab_pin.sym} 220 4410 0 0 {name=p777 sig_type=std_logic lab=nb}
N 220 4470 220 4470 {lab=nbf}
C {devices/lab_pin.sym} 220 4470 0 0 {name=p778 sig_type=std_logic lab=nbf}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 4440 0 0 {name=mbp_rbf
w=20u
l=0.13u
ng=4
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 4410 460 4410 {lab=nb}
C {devices/lab_pin.sym} 460 4410 0 0 {name=p779 sig_type=std_logic lab=nb}
N 420 4440 420 4440 {lab=vbp_tail}
C {devices/lab_pin.sym} 420 4440 0 1 {name=p780 sig_type=std_logic lab=vbp_tail}
N 460 4470 460 4470 {lab=nbf}
C {devices/lab_pin.sym} 460 4470 0 0 {name=p781 sig_type=std_logic lab=nbf}
N 460 4440 460 4440 {lab=gnd}
C {devices/lab_pin.sym} 460 4440 0 0 {name=p782 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_cmim.sym} 660 4440 0 0 {name=cbf0
model=cap_cmim
lvs_model=cmim
w=6.894000e-05
l=6.894000e-05
m=1
mm_ok=1
spiceprefix=X
}
N 660 4410 660 4410 {lab=nbf}
C {devices/lab_pin.sym} 660 4410 0 0 {name=p783 sig_type=std_logic lab=nbf}
N 660 4470 660 4470 {lab=gnd}
C {devices/lab_pin.sym} 660 4470 0 0 {name=p784 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_cmim.sym} 880 4440 0 0 {name=cbf1
model=cap_cmim
lvs_model=cmim
w=6.894000e-05
l=6.894000e-05
m=1
mm_ok=1
spiceprefix=X
}
N 880 4410 880 4410 {lab=nbf}
C {devices/lab_pin.sym} 880 4410 0 0 {name=p785 sig_type=std_logic lab=nbf}
N 880 4470 880 4470 {lab=gnd}
C {devices/lab_pin.sym} 880 4470 0 0 {name=p786 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_cmim.sym} 1100 4440 0 0 {name=cbf2
model=cap_cmim
lvs_model=cmim
w=6.894000e-05
l=6.894000e-05
m=1
mm_ok=1
spiceprefix=X
}
N 1100 4410 1100 4410 {lab=nbf}
C {devices/lab_pin.sym} 1100 4410 0 0 {name=p787 sig_type=std_logic lab=nbf}
N 1100 4470 1100 4470 {lab=gnd}
C {devices/lab_pin.sym} 1100 4470 0 0 {name=p788 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_cmim.sym} 0 4560 0 0 {name=cbf3
model=cap_cmim
lvs_model=cmim
w=6.894000e-05
l=6.894000e-05
m=1
mm_ok=1
spiceprefix=X
}
N 0 4530 0 4530 {lab=nbf}
C {devices/lab_pin.sym} 0 4530 0 0 {name=p789 sig_type=std_logic lab=nbf}
N 0 4590 0 4590 {lab=gnd}
C {devices/lab_pin.sym} 0 4590 0 0 {name=p790 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_cmim.sym} 220 4560 0 0 {name=cbf4
model=cap_cmim
lvs_model=cmim
w=6.894000e-05
l=6.894000e-05
m=1
mm_ok=1
spiceprefix=X
}
N 220 4530 220 4530 {lab=nbf}
C {devices/lab_pin.sym} 220 4530 0 0 {name=p791 sig_type=std_logic lab=nbf}
N 220 4590 220 4590 {lab=gnd}
C {devices/lab_pin.sym} 220 4590 0 0 {name=p792 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_cmim.sym} 440 4560 0 0 {name=cbf5
model=cap_cmim
lvs_model=cmim
w=6.894000e-05
l=6.894000e-05
m=1
mm_ok=1
spiceprefix=X
}
N 440 4530 440 4530 {lab=nbf}
C {devices/lab_pin.sym} 440 4530 0 0 {name=p793 sig_type=std_logic lab=nbf}
N 440 4590 440 4590 {lab=gnd}
C {devices/lab_pin.sym} 440 4590 0 0 {name=p794 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_cmim.sym} 660 4560 0 0 {name=cbf6
model=cap_cmim
lvs_model=cmim
w=6.894000e-05
l=6.894000e-05
m=1
mm_ok=1
spiceprefix=X
}
N 660 4530 660 4530 {lab=nbf}
C {devices/lab_pin.sym} 660 4530 0 0 {name=p795 sig_type=std_logic lab=nbf}
N 660 4590 660 4590 {lab=gnd}
C {devices/lab_pin.sym} 660 4590 0 0 {name=p796 sig_type=std_logic lab=gnd}
C {devices/isource.sym} 880 4560 0 0 {name=iref_pbias value=1.05e-05}
N 880 4530 880 4530 {lab=vdd}
C {devices/lab_pin.sym} 880 4530 0 0 {name=p797 sig_type=std_logic lab=vdd}
N 880 4590 880 4590 {lab=pbias}
C {devices/lab_pin.sym} 880 4590 0 0 {name=p798 sig_type=std_logic lab=pbias}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 4560 0 0 {name=mb1
w=10u
l=0.13u
ng=4
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 4530 1120 4530 {lab=op}
C {devices/lab_pin.sym} 1120 4530 0 0 {name=p799 sig_type=std_logic lab=op}
N 1080 4560 1080 4560 {lab=tp}
C {devices/lab_pin.sym} 1080 4560 0 1 {name=p800 sig_type=std_logic lab=tp}
N 1120 4590 1120 4590 {lab=tb}
C {devices/lab_pin.sym} 1120 4590 0 0 {name=p801 sig_type=std_logic lab=tb}
N 1120 4560 1120 4560 {lab=gnd}
C {devices/lab_pin.sym} 1120 4560 0 0 {name=p802 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 4680 0 0 {name=mb2
w=10u
l=0.13u
ng=4
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 4650 20 4650 {lab=on}
C {devices/lab_pin.sym} 20 4650 0 0 {name=p803 sig_type=std_logic lab=on}
N -20 4680 -20 4680 {lab=tn}
C {devices/lab_pin.sym} -20 4680 0 1 {name=p804 sig_type=std_logic lab=tn}
N 20 4710 20 4710 {lab=tb}
C {devices/lab_pin.sym} 20 4710 0 0 {name=p805 sig_type=std_logic lab=tb}
N 20 4680 20 4680 {lab=gnd}
C {devices/lab_pin.sym} 20 4680 0 0 {name=p806 sig_type=std_logic lab=gnd}
C {devices/res.sym} 220 4680 0 0 {name=rl1
value=400
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 4650 220 4650 {lab=vdd}
C {devices/lab_pin.sym} 220 4650 0 0 {name=p807 sig_type=std_logic lab=vdd}
N 220 4710 220 4710 {lab=op}
C {devices/lab_pin.sym} 220 4710 0 0 {name=p808 sig_type=std_logic lab=op}
C {devices/res.sym} 440 4680 0 0 {name=rl2
value=400
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 440 4650 440 4650 {lab=vdd}
C {devices/lab_pin.sym} 440 4650 0 0 {name=p809 sig_type=std_logic lab=vdd}
N 440 4710 440 4710 {lab=on}
C {devices/lab_pin.sym} 440 4710 0 0 {name=p810 sig_type=std_logic lab=on}
C {devices/isource.sym} 660 4680 0 0 {name=ib value=0.001}
N 660 4650 660 4650 {lab=tb}
C {devices/lab_pin.sym} 660 4650 0 0 {name=p811 sig_type=std_logic lab=tb}
N 660 4710 660 4710 {lab=gnd}
C {devices/lab_pin.sym} 660 4710 0 0 {name=p812 sig_type=std_logic lab=gnd}
C {devices/capa.sym} 880 4680 0 0 {name=ctb
value=2e-12
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 880 4650 880 4650 {lab=tb}
C {devices/lab_pin.sym} 880 4650 0 0 {name=p813 sig_type=std_logic lab=tb}
N 880 4710 880 4710 {lab=gnd}
C {devices/lab_pin.sym} 880 4710 0 0 {name=p814 sig_type=std_logic lab=gnd}
C {devices/capa.sym} 1100 4680 0 0 {name=cl1
value=2e-14
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 1100 4650 1100 4650 {lab=op}
C {devices/lab_pin.sym} 1100 4650 0 0 {name=p815 sig_type=std_logic lab=op}
N 1100 4710 1100 4710 {lab=gnd}
C {devices/lab_pin.sym} 1100 4710 0 0 {name=p816 sig_type=std_logic lab=gnd}
C {devices/capa.sym} 0 4800 0 0 {name=cl2
value=2e-14
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 0 4770 0 4770 {lab=on}
C {devices/lab_pin.sym} 0 4770 0 0 {name=p817 sig_type=std_logic lab=on}
N 0 4830 0 4830 {lab=gnd}
C {devices/lab_pin.sym} 0 4830 0 0 {name=p818 sig_type=std_logic lab=gnd}
