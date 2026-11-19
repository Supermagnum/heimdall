v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
C {devices/iopin.sym} -200 -40 0 0 {name=d lab=d}
C {devices/iopin.sym} -200 -80 0 0 {name=ck lab=ck}
C {devices/iopin.sym} -200 -120 0 0 {name=q lab=q}
C {devices/iopin.sym} -200 -160 0 0 {name=vdg lab=vdg}
C {devices/iopin.sym} -200 -200 0 0 {name=0 lab=0}
C {devices/title.sym} 0 40 0 0 {name=t1 author="HT13G-M P2.7.1"}
C {devices/lab_pin.sym} 200 40 0 0 {name=ttitle lab=lo_tspc_sz2_keepers}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 0 0 0 {name=xp1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 30 20 30 {lab=nx1}
C {devices/lab_pin.sym} 20 30 0 0 {name=p1 sig_type=std_logic lab=nx1}
N -20 0 -20 0 {lab=d}
C {devices/lab_pin.sym} -20 0 0 1 {name=p2 sig_type=std_logic lab=d}
N 20 -30 20 -30 {lab=vdg}
C {devices/lab_pin.sym} 20 -30 0 0 {name=p3 sig_type=std_logic lab=vdg}
N 20 0 20 0 {lab=vdg}
C {devices/lab_pin.sym} 20 0 0 0 {name=p4 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 0 0 0 {name=xp2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 30 240 30 {lab=na}
C {devices/lab_pin.sym} 240 30 0 0 {name=p5 sig_type=std_logic lab=na}
N 200 0 200 0 {lab=ck}
C {devices/lab_pin.sym} 200 0 0 1 {name=p6 sig_type=std_logic lab=ck}
N 240 -30 240 -30 {lab=nx1}
C {devices/lab_pin.sym} 240 -30 0 0 {name=p7 sig_type=std_logic lab=nx1}
N 240 0 240 0 {lab=vdg}
C {devices/lab_pin.sym} 240 0 0 0 {name=p8 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 0 0 0 {name=xn1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 -30 460 -30 {lab=na}
C {devices/lab_pin.sym} 460 -30 0 0 {name=p9 sig_type=std_logic lab=na}
N 420 0 420 0 {lab=d}
C {devices/lab_pin.sym} 420 0 0 1 {name=p10 sig_type=std_logic lab=d}
N 460 30 460 30 {lab=0}
C {devices/lab_pin.sym} 460 30 0 0 {name=p11 sig_type=std_logic lab=0}
N 460 0 460 0 {lab=0}
C {devices/lab_pin.sym} 460 0 0 0 {name=p12 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 0 0 0 {name=xp3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 30 680 30 {lab=nb}
C {devices/lab_pin.sym} 680 30 0 0 {name=p13 sig_type=std_logic lab=nb}
N 640 0 640 0 {lab=ck}
C {devices/lab_pin.sym} 640 0 0 1 {name=p14 sig_type=std_logic lab=ck}
N 680 -30 680 -30 {lab=vdg}
C {devices/lab_pin.sym} 680 -30 0 0 {name=p15 sig_type=std_logic lab=vdg}
N 680 0 680 0 {lab=vdg}
C {devices/lab_pin.sym} 680 0 0 0 {name=p16 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 0 0 0 {name=xn2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 -30 900 -30 {lab=nb}
C {devices/lab_pin.sym} 900 -30 0 0 {name=p17 sig_type=std_logic lab=nb}
N 860 0 860 0 {lab=na}
C {devices/lab_pin.sym} 860 0 0 1 {name=p18 sig_type=std_logic lab=na}
N 900 30 900 30 {lab=nx2}
C {devices/lab_pin.sym} 900 30 0 0 {name=p19 sig_type=std_logic lab=nx2}
N 900 0 900 0 {lab=0}
C {devices/lab_pin.sym} 900 0 0 0 {name=p20 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 0 0 0 {name=xn3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 -30 1120 -30 {lab=nx2}
C {devices/lab_pin.sym} 1120 -30 0 0 {name=p21 sig_type=std_logic lab=nx2}
N 1080 0 1080 0 {lab=ck}
C {devices/lab_pin.sym} 1080 0 0 1 {name=p22 sig_type=std_logic lab=ck}
N 1120 30 1120 30 {lab=0}
C {devices/lab_pin.sym} 1120 30 0 0 {name=p23 sig_type=std_logic lab=0}
N 1120 0 1120 0 {lab=0}
C {devices/lab_pin.sym} 1120 0 0 0 {name=p24 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 120 0 0 {name=xp4
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 150 20 150 {lab=q}
C {devices/lab_pin.sym} 20 150 0 0 {name=p25 sig_type=std_logic lab=q}
N -20 120 -20 120 {lab=nb}
C {devices/lab_pin.sym} -20 120 0 1 {name=p26 sig_type=std_logic lab=nb}
N 20 90 20 90 {lab=vdg}
C {devices/lab_pin.sym} 20 90 0 0 {name=p27 sig_type=std_logic lab=vdg}
N 20 120 20 120 {lab=vdg}
C {devices/lab_pin.sym} 20 120 0 0 {name=p28 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 120 0 0 {name=xn4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 90 240 90 {lab=q}
C {devices/lab_pin.sym} 240 90 0 0 {name=p29 sig_type=std_logic lab=q}
N 200 120 200 120 {lab=ck}
C {devices/lab_pin.sym} 200 120 0 1 {name=p30 sig_type=std_logic lab=ck}
N 240 150 240 150 {lab=nx3}
C {devices/lab_pin.sym} 240 150 0 0 {name=p31 sig_type=std_logic lab=nx3}
N 240 120 240 120 {lab=0}
C {devices/lab_pin.sym} 240 120 0 0 {name=p32 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 120 0 0 {name=xn5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 90 460 90 {lab=nx3}
C {devices/lab_pin.sym} 460 90 0 0 {name=p33 sig_type=std_logic lab=nx3}
N 420 120 420 120 {lab=nb}
C {devices/lab_pin.sym} 420 120 0 1 {name=p34 sig_type=std_logic lab=nb}
N 460 150 460 150 {lab=0}
C {devices/lab_pin.sym} 460 150 0 0 {name=p35 sig_type=std_logic lab=0}
N 460 120 460 120 {lab=0}
C {devices/lab_pin.sym} 460 120 0 0 {name=p36 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 120 0 0 {name=xkq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 150 680 150 {lab=nkq}
C {devices/lab_pin.sym} 680 150 0 0 {name=p37 sig_type=std_logic lab=nkq}
N 640 120 640 120 {lab=q}
C {devices/lab_pin.sym} 640 120 0 1 {name=p38 sig_type=std_logic lab=q}
N 680 90 680 90 {lab=vdg}
C {devices/lab_pin.sym} 680 90 0 0 {name=p39 sig_type=std_logic lab=vdg}
N 680 120 680 120 {lab=vdg}
C {devices/lab_pin.sym} 680 120 0 0 {name=p40 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 120 0 0 {name=xkq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 90 900 90 {lab=nkq}
C {devices/lab_pin.sym} 900 90 0 0 {name=p41 sig_type=std_logic lab=nkq}
N 860 120 860 120 {lab=q}
C {devices/lab_pin.sym} 860 120 0 1 {name=p42 sig_type=std_logic lab=q}
N 900 150 900 150 {lab=0}
C {devices/lab_pin.sym} 900 150 0 0 {name=p43 sig_type=std_logic lab=0}
N 900 120 900 120 {lab=0}
C {devices/lab_pin.sym} 900 120 0 0 {name=p44 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 120 0 0 {name=xkq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 150 1120 150 {lab=q}
C {devices/lab_pin.sym} 1120 150 0 0 {name=p45 sig_type=std_logic lab=q}
N 1080 120 1080 120 {lab=nkq}
C {devices/lab_pin.sym} 1080 120 0 1 {name=p46 sig_type=std_logic lab=nkq}
N 1120 90 1120 90 {lab=vdg}
C {devices/lab_pin.sym} 1120 90 0 0 {name=p47 sig_type=std_logic lab=vdg}
N 1120 120 1120 120 {lab=vdg}
C {devices/lab_pin.sym} 1120 120 0 0 {name=p48 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 240 0 0 {name=xkq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 210 20 210 {lab=q}
C {devices/lab_pin.sym} 20 210 0 0 {name=p49 sig_type=std_logic lab=q}
N -20 240 -20 240 {lab=nkq}
C {devices/lab_pin.sym} -20 240 0 1 {name=p50 sig_type=std_logic lab=nkq}
N 20 270 20 270 {lab=0}
C {devices/lab_pin.sym} 20 270 0 0 {name=p51 sig_type=std_logic lab=0}
N 20 240 20 240 {lab=0}
C {devices/lab_pin.sym} 20 240 0 0 {name=p52 sig_type=std_logic lab=0}
C {devices/res.sym} 220 240 0 0 {name=rka
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 210 220 210 {lab=na}
C {devices/lab_pin.sym} 220 210 0 0 {name=p53 sig_type=std_logic lab=na}
N 220 270 220 270 {lab=0}
C {devices/lab_pin.sym} 220 270 0 0 {name=p54 sig_type=std_logic lab=0}
C {devices/res.sym} 440 240 0 0 {name=rkb
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 440 210 440 210 {lab=nb}
C {devices/lab_pin.sym} 440 210 0 0 {name=p55 sig_type=std_logic lab=nb}
N 440 270 440 270 {lab=0}
C {devices/lab_pin.sym} 440 270 0 0 {name=p56 sig_type=std_logic lab=0}
