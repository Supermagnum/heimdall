v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
C {devices/iopin.sym} -200 -40 0 0 {name=tp lab=tp}
C {devices/iopin.sym} -200 -80 0 0 {name=tn lab=tn}
C {devices/iopin.sym} -200 -120 0 0 {name=tail lab=tail}
C {devices/iopin.sym} -200 -160 0 0 {name=ct lab=ct}
C {devices/iopin.sym} -200 -200 0 0 {name=vdd lab=vdd}
C {devices/iopin.sym} -200 -240 0 0 {name=gnd lab=gnd}
C {devices/title.sym} 0 40 0 0 {name=t1 author="HT13G-M P2.7.1"}
C {devices/lab_pin.sym} 200 40 0 0 {name=ttitle lab=vco_core_XC}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 0 0 0 {name=m1
w=32u
l=0.13u
ng=8
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 -30 20 -30 {lab=tp}
C {devices/lab_pin.sym} 20 -30 0 0 {name=p1 sig_type=std_logic lab=tp}
N -20 0 -20 0 {lab=tn}
C {devices/lab_pin.sym} -20 0 0 1 {name=p2 sig_type=std_logic lab=tn}
N 20 30 20 30 {lab=tail}
C {devices/lab_pin.sym} 20 30 0 0 {name=p3 sig_type=std_logic lab=tail}
N 20 0 20 0 {lab=gnd}
C {devices/lab_pin.sym} 20 0 0 0 {name=p4 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 0 0 0 {name=m2
w=32u
l=0.13u
ng=8
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 -30 240 -30 {lab=tn}
C {devices/lab_pin.sym} 240 -30 0 0 {name=p5 sig_type=std_logic lab=tn}
N 200 0 200 0 {lab=tp}
C {devices/lab_pin.sym} 200 0 0 1 {name=p6 sig_type=std_logic lab=tp}
N 240 30 240 30 {lab=tail}
C {devices/lab_pin.sym} 240 30 0 0 {name=p7 sig_type=std_logic lab=tail}
N 240 0 240 0 {lab=gnd}
C {devices/lab_pin.sym} 240 0 0 0 {name=p8 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 0 0 0 {name=mdum
w=9u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 -30 460 -30 {lab=gnd}
C {devices/lab_pin.sym} 460 -30 0 0 {name=p9 sig_type=std_logic lab=gnd}
N 420 0 420 0 {lab=gnd}
C {devices/lab_pin.sym} 420 0 0 1 {name=p10 sig_type=std_logic lab=gnd}
N 460 30 460 30 {lab=gnd}
C {devices/lab_pin.sym} 460 30 0 0 {name=p11 sig_type=std_logic lab=gnd}
N 460 0 460 0 {lab=gnd}
C {devices/lab_pin.sym} 460 0 0 0 {name=p12 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 660 0 0 0 {name=xf1
model=cap_rfcmim
lvs_model=rfcmim
w=1.450000e-05
l=1.450000e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 660 -30 660 -30 {lab=tp}
C {devices/lab_pin.sym} 660 -30 0 0 {name=p13 sig_type=std_logic lab=tp}
N 660 30 660 30 {lab=fx}
C {devices/lab_pin.sym} 660 30 0 0 {name=p14 sig_type=std_logic lab=fx}
N 630 0 630 0 {lab=gnd}
C {devices/lab_pin.sym} 630 0 0 0 {name=p15 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 880 0 0 0 {name=xf2
model=cap_rfcmim
lvs_model=rfcmim
w=1.450000e-05
l=1.450000e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 880 -30 880 -30 {lab=tn}
C {devices/lab_pin.sym} 880 -30 0 0 {name=p16 sig_type=std_logic lab=tn}
N 880 30 880 30 {lab=fx}
C {devices/lab_pin.sym} 880 30 0 0 {name=p17 sig_type=std_logic lab=fx}
N 850 0 850 0 {lab=gnd}
C {devices/lab_pin.sym} 850 0 0 0 {name=p18 sig_type=std_logic lab=gnd}
C {sg13g2_pr/rhigh.sym} 1100 0 0 0 {name=rfx
w=2.000000e-06
l=1.520000e-05
b=0
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 1100 -30 1100 -30 {lab=fx}
C {devices/lab_pin.sym} 1100 -30 0 0 {name=p19 sig_type=std_logic lab=fx}
N 1100 30 1100 30 {lab=gnd}
C {devices/lab_pin.sym} 1100 30 0 0 {name=p20 sig_type=std_logic lab=gnd}
