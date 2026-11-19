v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
C {devices/iopin.sym} -200 -40 0 0 {name=a lab=a}
C {devices/iopin.sym} -200 -80 0 0 {name=b lab=b}
C {devices/iopin.sym} -200 -120 0 0 {name=y lab=y}
C {devices/iopin.sym} -200 -160 0 0 {name=vdg lab=vdg}
C {devices/iopin.sym} -200 -200 0 0 {name=0 lab=0}
C {devices/title.sym} 0 40 0 0 {name=t1 author="HT13G-M P2.7.1"}
C {devices/lab_pin.sym} 200 40 0 0 {name=ttitle lab=lo_nand2}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 0 0 0 {name=xpa
w=1u
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
N 20 -30 20 -30 {lab=vdg}
C {devices/lab_pin.sym} 20 -30 0 0 {name=p3 sig_type=std_logic lab=vdg}
N 20 0 20 0 {lab=vdg}
C {devices/lab_pin.sym} 20 0 0 0 {name=p4 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 0 0 0 {name=xpb
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 30 240 30 {lab=y}
C {devices/lab_pin.sym} 240 30 0 0 {name=p5 sig_type=std_logic lab=y}
N 200 0 200 0 {lab=b}
C {devices/lab_pin.sym} 200 0 0 1 {name=p6 sig_type=std_logic lab=b}
N 240 -30 240 -30 {lab=vdg}
C {devices/lab_pin.sym} 240 -30 0 0 {name=p7 sig_type=std_logic lab=vdg}
N 240 0 240 0 {lab=vdg}
C {devices/lab_pin.sym} 240 0 0 0 {name=p8 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 0 0 0 {name=xna
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 -30 460 -30 {lab=y}
C {devices/lab_pin.sym} 460 -30 0 0 {name=p9 sig_type=std_logic lab=y}
N 420 0 420 0 {lab=a}
C {devices/lab_pin.sym} 420 0 0 1 {name=p10 sig_type=std_logic lab=a}
N 460 30 460 30 {lab=mid}
C {devices/lab_pin.sym} 460 30 0 0 {name=p11 sig_type=std_logic lab=mid}
N 460 0 460 0 {lab=0}
C {devices/lab_pin.sym} 460 0 0 0 {name=p12 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 0 0 0 {name=xnb
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 -30 680 -30 {lab=mid}
C {devices/lab_pin.sym} 680 -30 0 0 {name=p13 sig_type=std_logic lab=mid}
N 640 0 640 0 {lab=b}
C {devices/lab_pin.sym} 640 0 0 1 {name=p14 sig_type=std_logic lab=b}
N 680 30 680 30 {lab=0}
C {devices/lab_pin.sym} 680 30 0 0 {name=p15 sig_type=std_logic lab=0}
N 680 0 680 0 {lab=0}
C {devices/lab_pin.sym} 680 0 0 0 {name=p16 sig_type=std_logic lab=0}
