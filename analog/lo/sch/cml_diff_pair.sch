v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
C {devices/iopin.sym} -200 -40 0 0 {name=d1 lab=d1}
C {devices/iopin.sym} -200 -80 0 0 {name=d2 lab=d2}
C {devices/iopin.sym} -200 -120 0 0 {name=g1 lab=g1}
C {devices/iopin.sym} -200 -160 0 0 {name=g2 lab=g2}
C {devices/iopin.sym} -200 -200 0 0 {name=s lab=s}
C {devices/iopin.sym} -200 -240 0 0 {name=0 lab=0}
C {devices/title.sym} 0 40 0 0 {name=t1 author="HT13G-M P2.7.1"}
C {devices/lab_pin.sym} 200 40 0 0 {name=ttitle lab=cml_diff_pair_W7p5}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 0 0 0 {name=mm1
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 -30 20 -30 {lab=d1}
C {devices/lab_pin.sym} 20 -30 0 0 {name=p1 sig_type=std_logic lab=d1}
N -20 0 -20 0 {lab=g1}
C {devices/lab_pin.sym} -20 0 0 1 {name=p2 sig_type=std_logic lab=g1}
N 20 30 20 30 {lab=s}
C {devices/lab_pin.sym} 20 30 0 0 {name=p3 sig_type=std_logic lab=s}
N 20 0 20 0 {lab=0}
C {devices/lab_pin.sym} 20 0 0 0 {name=p4 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 0 0 0 {name=mm2
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 -30 240 -30 {lab=d2}
C {devices/lab_pin.sym} 240 -30 0 0 {name=p5 sig_type=std_logic lab=d2}
N 200 0 200 0 {lab=g2}
C {devices/lab_pin.sym} 200 0 0 1 {name=p6 sig_type=std_logic lab=g2}
N 240 30 240 30 {lab=s}
C {devices/lab_pin.sym} 240 30 0 0 {name=p7 sig_type=std_logic lab=s}
N 240 0 240 0 {lab=0}
C {devices/lab_pin.sym} 240 0 0 0 {name=p8 sig_type=std_logic lab=0}
