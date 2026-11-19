v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
C {devices/iopin.sym} -200 -40 0 0 {name=dp lab=dp}
C {devices/iopin.sym} -200 -80 0 0 {name=dn lab=dn}
C {devices/iopin.sym} -200 -120 0 0 {name=ckp lab=ckp}
C {devices/iopin.sym} -200 -160 0 0 {name=ckn lab=ckn}
C {devices/iopin.sym} -200 -200 0 0 {name=qp lab=qp}
C {devices/iopin.sym} -200 -240 0 0 {name=qn lab=qn}
C {devices/iopin.sym} -200 -280 0 0 {name=vdd lab=vdd}
C {devices/iopin.sym} -200 -320 0 0 {name=0 lab=0}
C {devices/title.sym} 0 40 0 0 {name=t1 author="HT13G-M P2.7.1"}
C {devices/lab_pin.sym} 200 40 0 0 {name=ttitle lab=cml_latch_vhf_tl_0p30mA}
C {devices/res.sym} 0 0 0 0 {name=rlap
value=666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 0 -30 0 -30 {lab=vdd}
C {devices/lab_pin.sym} 0 -30 0 0 {name=p1 sig_type=std_logic lab=vdd}
N 0 30 0 30 {lab=qp}
C {devices/lab_pin.sym} 0 30 0 0 {name=p2 sig_type=std_logic lab=qp}
C {devices/res.sym} 220 0 0 0 {name=rlan
value=666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 -30 220 -30 {lab=vdd}
C {devices/lab_pin.sym} 220 -30 0 0 {name=p3 sig_type=std_logic lab=vdd}
N 220 30 220 30 {lab=qn}
C {devices/lab_pin.sym} 220 30 0 0 {name=p4 sig_type=std_logic lab=qn}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 0 0 0 {name=ma1
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 -30 460 -30 {lab=qn}
C {devices/lab_pin.sym} 460 -30 0 0 {name=p5 sig_type=std_logic lab=qn}
N 420 0 420 0 {lab=dp}
C {devices/lab_pin.sym} 420 0 0 1 {name=p6 sig_type=std_logic lab=dp}
N 460 30 460 30 {lab=s1a}
C {devices/lab_pin.sym} 460 30 0 0 {name=p7 sig_type=std_logic lab=s1a}
N 460 0 460 0 {lab=0}
C {devices/lab_pin.sym} 460 0 0 0 {name=p8 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 0 0 0 {name=ma2
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 -30 680 -30 {lab=qp}
C {devices/lab_pin.sym} 680 -30 0 0 {name=p9 sig_type=std_logic lab=qp}
N 640 0 640 0 {lab=dn}
C {devices/lab_pin.sym} 640 0 0 1 {name=p10 sig_type=std_logic lab=dn}
N 680 30 680 30 {lab=s1a}
C {devices/lab_pin.sym} 680 30 0 0 {name=p11 sig_type=std_logic lab=s1a}
N 680 0 680 0 {lab=0}
C {devices/lab_pin.sym} 680 0 0 0 {name=p12 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 0 0 0 {name=ma3
w=11.25u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 -30 900 -30 {lab=qn}
C {devices/lab_pin.sym} 900 -30 0 0 {name=p13 sig_type=std_logic lab=qn}
N 860 0 860 0 {lab=qp}
C {devices/lab_pin.sym} 860 0 0 1 {name=p14 sig_type=std_logic lab=qp}
N 900 30 900 30 {lab=s2a}
C {devices/lab_pin.sym} 900 30 0 0 {name=p15 sig_type=std_logic lab=s2a}
N 900 0 900 0 {lab=0}
C {devices/lab_pin.sym} 900 0 0 0 {name=p16 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 0 0 0 {name=ma4
w=11.25u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 -30 1120 -30 {lab=qp}
C {devices/lab_pin.sym} 1120 -30 0 0 {name=p17 sig_type=std_logic lab=qp}
N 1080 0 1080 0 {lab=qn}
C {devices/lab_pin.sym} 1080 0 0 1 {name=p18 sig_type=std_logic lab=qn}
N 1120 30 1120 30 {lab=s2a}
C {devices/lab_pin.sym} 1120 30 0 0 {name=p19 sig_type=std_logic lab=s2a}
N 1120 0 1120 0 {lab=0}
C {devices/lab_pin.sym} 1120 0 0 0 {name=p20 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 120 0 0 {name=ma5
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 90 20 90 {lab=s1a}
C {devices/lab_pin.sym} 20 90 0 0 {name=p21 sig_type=std_logic lab=s1a}
N -20 120 -20 120 {lab=ckp}
C {devices/lab_pin.sym} -20 120 0 1 {name=p22 sig_type=std_logic lab=ckp}
N 20 150 20 150 {lab=0}
C {devices/lab_pin.sym} 20 150 0 0 {name=p23 sig_type=std_logic lab=0}
N 20 120 20 120 {lab=0}
C {devices/lab_pin.sym} 20 120 0 0 {name=p24 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 120 0 0 {name=ma6
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 90 240 90 {lab=s2a}
C {devices/lab_pin.sym} 240 90 0 0 {name=p25 sig_type=std_logic lab=s2a}
N 200 120 200 120 {lab=ckn}
C {devices/lab_pin.sym} 200 120 0 1 {name=p26 sig_type=std_logic lab=ckn}
N 240 150 240 150 {lab=0}
C {devices/lab_pin.sym} 240 150 0 0 {name=p27 sig_type=std_logic lab=0}
N 240 120 240 120 {lab=0}
C {devices/lab_pin.sym} 240 120 0 0 {name=p28 sig_type=std_logic lab=0}
