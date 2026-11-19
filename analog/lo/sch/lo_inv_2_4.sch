v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
C {devices/iopin.sym} -200 -40 0 0 {name=a lab=a}
C {devices/iopin.sym} -200 -80 0 0 {name=y lab=y}
C {devices/iopin.sym} -200 -120 0 0 {name=vdd lab=vdd}
C {devices/iopin.sym} -200 -160 0 0 {name=0 lab=0}
C {devices/title.sym} 0 40 0 0 {name=t1 author="HT13G-M P2.7.1"}
C {devices/lab_pin.sym} 200 40 0 0 {name=ttitle lab=lo_inv_wn2_wp4}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 0 0 0 {name=xp
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 30 20 30 {lab=y}
C {devices/lab_pin.sym} 20 30 0 0 {name=p1 sig_type=std_logic lab=y}
N -20 0 -20 0 {lab=a}
C {devices/lab_pin.sym} -20 0 0 1 {name=p2 sig_type=std_logic lab=a}
N 20 -30 20 -30 {lab=vdd}
C {devices/lab_pin.sym} 20 -30 0 0 {name=p3 sig_type=std_logic lab=vdd}
N 20 0 20 0 {lab=vdd}
C {devices/lab_pin.sym} 20 0 0 0 {name=p4 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 0 0 0 {name=xn
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 -30 240 -30 {lab=y}
C {devices/lab_pin.sym} 240 -30 0 0 {name=p5 sig_type=std_logic lab=y}
N 200 0 200 0 {lab=a}
C {devices/lab_pin.sym} 200 0 0 1 {name=p6 sig_type=std_logic lab=a}
N 240 30 240 30 {lab=0}
C {devices/lab_pin.sym} 240 30 0 0 {name=p7 sig_type=std_logic lab=0}
N 240 0 240 0 {lab=0}
C {devices/lab_pin.sym} 240 0 0 0 {name=p8 sig_type=std_logic lab=0}
