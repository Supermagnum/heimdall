v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
C {devices/iopin.sym} -200 -40 0 0 {name=q1p lab=q1p}
C {devices/iopin.sym} -200 -80 0 0 {name=q2p lab=q2p}
C {devices/iopin.sym} -200 -120 0 0 {name=vref lab=vref}
C {devices/iopin.sym} -200 -160 0 0 {name=orp lab=orp}
C {devices/iopin.sym} -200 -200 0 0 {name=orn lab=orn}
C {devices/iopin.sym} -200 -240 0 0 {name=nb_lo lab=nb_lo}
C {devices/iopin.sym} -200 -280 0 0 {name=vdd lab=vdd}
C {devices/iopin.sym} -200 -320 0 0 {name=0 lab=0}
C {devices/title.sym} 0 40 0 0 {name=t1 author="HT13G-M P2.7.1"}
C {devices/lab_pin.sym} 200 40 0 0 {name=ttitle lab=cml_nor_vhf_0p30mA}
C {devices/res.sym} 0 0 0 0 {name=rgp
value=1666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 0 -30 0 -30 {lab=vdd}
C {devices/lab_pin.sym} 0 -30 0 0 {name=p1 sig_type=std_logic lab=vdd}
N 0 30 0 30 {lab=orp}
C {devices/lab_pin.sym} 0 30 0 0 {name=p2 sig_type=std_logic lab=orp}
C {devices/res.sym} 220 0 0 0 {name=rgn
value=1666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 -30 220 -30 {lab=vdd}
C {devices/lab_pin.sym} 220 -30 0 0 {name=p3 sig_type=std_logic lab=vdd}
N 220 30 220 30 {lab=orn}
C {devices/lab_pin.sym} 220 30 0 0 {name=p4 sig_type=std_logic lab=orn}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 0 0 0 {name=mga
w=3.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 -30 460 -30 {lab=orn}
C {devices/lab_pin.sym} 460 -30 0 0 {name=p5 sig_type=std_logic lab=orn}
N 420 0 420 0 {lab=q1p}
C {devices/lab_pin.sym} 420 0 0 1 {name=p6 sig_type=std_logic lab=q1p}
N 460 30 460 30 {lab=tg}
C {devices/lab_pin.sym} 460 30 0 0 {name=p7 sig_type=std_logic lab=tg}
N 460 0 460 0 {lab=0}
C {devices/lab_pin.sym} 460 0 0 0 {name=p8 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 0 0 0 {name=mgb
w=3.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 -30 680 -30 {lab=orn}
C {devices/lab_pin.sym} 680 -30 0 0 {name=p9 sig_type=std_logic lab=orn}
N 640 0 640 0 {lab=q2p}
C {devices/lab_pin.sym} 640 0 0 1 {name=p10 sig_type=std_logic lab=q2p}
N 680 30 680 30 {lab=tg}
C {devices/lab_pin.sym} 680 30 0 0 {name=p11 sig_type=std_logic lab=tg}
N 680 0 680 0 {lab=0}
C {devices/lab_pin.sym} 680 0 0 0 {name=p12 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 0 0 0 {name=mgr
w=3.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 -30 900 -30 {lab=orp}
C {devices/lab_pin.sym} 900 -30 0 0 {name=p13 sig_type=std_logic lab=orp}
N 860 0 860 0 {lab=vref}
C {devices/lab_pin.sym} 860 0 0 1 {name=p14 sig_type=std_logic lab=vref}
N 900 30 900 30 {lab=tg}
C {devices/lab_pin.sym} 900 30 0 0 {name=p15 sig_type=std_logic lab=tg}
N 900 0 900 0 {lab=0}
C {devices/lab_pin.sym} 900 0 0 0 {name=p16 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 0 0 0 {name=mtg
w=6u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 -30 1120 -30 {lab=tg}
C {devices/lab_pin.sym} 1120 -30 0 0 {name=p17 sig_type=std_logic lab=tg}
N 1080 0 1080 0 {lab=nb_lo}
C {devices/lab_pin.sym} 1080 0 0 1 {name=p18 sig_type=std_logic lab=nb_lo}
N 1120 30 1120 30 {lab=0}
C {devices/lab_pin.sym} 1120 30 0 0 {name=p19 sig_type=std_logic lab=0}
N 1120 0 1120 0 {lab=0}
C {devices/lab_pin.sym} 1120 0 0 0 {name=p20 sig_type=std_logic lab=0}
