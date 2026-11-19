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
C {devices/iopin.sym} -200 -280 0 0 {name=nb_lo lab=nb_lo}
C {devices/iopin.sym} -200 -320 0 0 {name=vdv lab=vdv}
C {devices/iopin.sym} -200 -360 0 0 {name=0 lab=0}
C {devices/title.sym} 0 40 0 0 {name=t1 author="HT13G-M P2.7.1"}
C {devices/lab_pin.sym} 200 40 0 0 {name=ttitle lab=cml_dff_uhf_0p75}
C {devices/res.sym} 0 0 0 0 {name=rlamp
value=666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 0 -30 0 -30 {lab=vdv}
C {devices/lab_pin.sym} 0 -30 0 0 {name=p1 sig_type=std_logic lab=vdv}
N 0 30 0 30 {lab=map}
C {devices/lab_pin.sym} 0 30 0 0 {name=p2 sig_type=std_logic lab=map}
C {devices/res.sym} 220 0 0 0 {name=rlamn
value=666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 -30 220 -30 {lab=vdv}
C {devices/lab_pin.sym} 220 -30 0 0 {name=p3 sig_type=std_logic lab=vdv}
N 220 30 220 30 {lab=man}
C {devices/lab_pin.sym} 220 30 0 0 {name=p4 sig_type=std_logic lab=man}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 0 0 0 {name=mam1
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 -30 460 -30 {lab=man}
C {devices/lab_pin.sym} 460 -30 0 0 {name=p5 sig_type=std_logic lab=man}
N 420 0 420 0 {lab=dp}
C {devices/lab_pin.sym} 420 0 0 1 {name=p6 sig_type=std_logic lab=dp}
N 460 30 460 30 {lab=s1am}
C {devices/lab_pin.sym} 460 30 0 0 {name=p7 sig_type=std_logic lab=s1am}
N 460 0 460 0 {lab=0}
C {devices/lab_pin.sym} 460 0 0 0 {name=p8 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 0 0 0 {name=mam2
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 -30 680 -30 {lab=map}
C {devices/lab_pin.sym} 680 -30 0 0 {name=p9 sig_type=std_logic lab=map}
N 640 0 640 0 {lab=dn}
C {devices/lab_pin.sym} 640 0 0 1 {name=p10 sig_type=std_logic lab=dn}
N 680 30 680 30 {lab=s1am}
C {devices/lab_pin.sym} 680 30 0 0 {name=p11 sig_type=std_logic lab=s1am}
N 680 0 680 0 {lab=0}
C {devices/lab_pin.sym} 680 0 0 0 {name=p12 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 0 0 0 {name=mam3
w=11.25u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 -30 900 -30 {lab=man}
C {devices/lab_pin.sym} 900 -30 0 0 {name=p13 sig_type=std_logic lab=man}
N 860 0 860 0 {lab=map}
C {devices/lab_pin.sym} 860 0 0 1 {name=p14 sig_type=std_logic lab=map}
N 900 30 900 30 {lab=s2am}
C {devices/lab_pin.sym} 900 30 0 0 {name=p15 sig_type=std_logic lab=s2am}
N 900 0 900 0 {lab=0}
C {devices/lab_pin.sym} 900 0 0 0 {name=p16 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 0 0 0 {name=mam4
w=11.25u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 -30 1120 -30 {lab=map}
C {devices/lab_pin.sym} 1120 -30 0 0 {name=p17 sig_type=std_logic lab=map}
N 1080 0 1080 0 {lab=man}
C {devices/lab_pin.sym} 1080 0 0 1 {name=p18 sig_type=std_logic lab=man}
N 1120 30 1120 30 {lab=s2am}
C {devices/lab_pin.sym} 1120 30 0 0 {name=p19 sig_type=std_logic lab=s2am}
N 1120 0 1120 0 {lab=0}
C {devices/lab_pin.sym} 1120 0 0 0 {name=p20 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 120 0 0 {name=mam5
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 90 20 90 {lab=s1am}
C {devices/lab_pin.sym} 20 90 0 0 {name=p21 sig_type=std_logic lab=s1am}
N -20 120 -20 120 {lab=ckp}
C {devices/lab_pin.sym} -20 120 0 1 {name=p22 sig_type=std_logic lab=ckp}
N 20 150 20 150 {lab=tam}
C {devices/lab_pin.sym} 20 150 0 0 {name=p23 sig_type=std_logic lab=tam}
N 20 120 20 120 {lab=0}
C {devices/lab_pin.sym} 20 120 0 0 {name=p24 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 120 0 0 {name=mam6
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 90 240 90 {lab=s2am}
C {devices/lab_pin.sym} 240 90 0 0 {name=p25 sig_type=std_logic lab=s2am}
N 200 120 200 120 {lab=ckn}
C {devices/lab_pin.sym} 200 120 0 1 {name=p26 sig_type=std_logic lab=ckn}
N 240 150 240 150 {lab=tam}
C {devices/lab_pin.sym} 240 150 0 0 {name=p27 sig_type=std_logic lab=tam}
N 240 120 240 120 {lab=0}
C {devices/lab_pin.sym} 240 120 0 0 {name=p28 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 120 0 0 {name=mtam
w=15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 90 460 90 {lab=tam}
C {devices/lab_pin.sym} 460 90 0 0 {name=p29 sig_type=std_logic lab=tam}
N 420 120 420 120 {lab=nb_lo}
C {devices/lab_pin.sym} 420 120 0 1 {name=p30 sig_type=std_logic lab=nb_lo}
N 460 150 460 150 {lab=0}
C {devices/lab_pin.sym} 460 150 0 0 {name=p31 sig_type=std_logic lab=0}
N 460 120 460 120 {lab=0}
C {devices/lab_pin.sym} 460 120 0 0 {name=p32 sig_type=std_logic lab=0}
C {devices/res.sym} 660 120 0 0 {name=rlasp
value=666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 660 90 660 90 {lab=vdv}
C {devices/lab_pin.sym} 660 90 0 0 {name=p33 sig_type=std_logic lab=vdv}
N 660 150 660 150 {lab=qp}
C {devices/lab_pin.sym} 660 150 0 0 {name=p34 sig_type=std_logic lab=qp}
C {devices/res.sym} 880 120 0 0 {name=rlasn
value=666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 90 880 90 {lab=vdv}
C {devices/lab_pin.sym} 880 90 0 0 {name=p35 sig_type=std_logic lab=vdv}
N 880 150 880 150 {lab=qn}
C {devices/lab_pin.sym} 880 150 0 0 {name=p36 sig_type=std_logic lab=qn}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 120 0 0 {name=mas1
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 90 1120 90 {lab=qn}
C {devices/lab_pin.sym} 1120 90 0 0 {name=p37 sig_type=std_logic lab=qn}
N 1080 120 1080 120 {lab=map}
C {devices/lab_pin.sym} 1080 120 0 1 {name=p38 sig_type=std_logic lab=map}
N 1120 150 1120 150 {lab=s1as}
C {devices/lab_pin.sym} 1120 150 0 0 {name=p39 sig_type=std_logic lab=s1as}
N 1120 120 1120 120 {lab=0}
C {devices/lab_pin.sym} 1120 120 0 0 {name=p40 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 240 0 0 {name=mas2
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 210 20 210 {lab=qp}
C {devices/lab_pin.sym} 20 210 0 0 {name=p41 sig_type=std_logic lab=qp}
N -20 240 -20 240 {lab=man}
C {devices/lab_pin.sym} -20 240 0 1 {name=p42 sig_type=std_logic lab=man}
N 20 270 20 270 {lab=s1as}
C {devices/lab_pin.sym} 20 270 0 0 {name=p43 sig_type=std_logic lab=s1as}
N 20 240 20 240 {lab=0}
C {devices/lab_pin.sym} 20 240 0 0 {name=p44 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 240 0 0 {name=mas3
w=11.25u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 210 240 210 {lab=qn}
C {devices/lab_pin.sym} 240 210 0 0 {name=p45 sig_type=std_logic lab=qn}
N 200 240 200 240 {lab=qp}
C {devices/lab_pin.sym} 200 240 0 1 {name=p46 sig_type=std_logic lab=qp}
N 240 270 240 270 {lab=s2as}
C {devices/lab_pin.sym} 240 270 0 0 {name=p47 sig_type=std_logic lab=s2as}
N 240 240 240 240 {lab=0}
C {devices/lab_pin.sym} 240 240 0 0 {name=p48 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 240 0 0 {name=mas4
w=11.25u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 210 460 210 {lab=qp}
C {devices/lab_pin.sym} 460 210 0 0 {name=p49 sig_type=std_logic lab=qp}
N 420 240 420 240 {lab=qn}
C {devices/lab_pin.sym} 420 240 0 1 {name=p50 sig_type=std_logic lab=qn}
N 460 270 460 270 {lab=s2as}
C {devices/lab_pin.sym} 460 270 0 0 {name=p51 sig_type=std_logic lab=s2as}
N 460 240 460 240 {lab=0}
C {devices/lab_pin.sym} 460 240 0 0 {name=p52 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 240 0 0 {name=mas5
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 210 680 210 {lab=s1as}
C {devices/lab_pin.sym} 680 210 0 0 {name=p53 sig_type=std_logic lab=s1as}
N 640 240 640 240 {lab=ckn}
C {devices/lab_pin.sym} 640 240 0 1 {name=p54 sig_type=std_logic lab=ckn}
N 680 270 680 270 {lab=tas}
C {devices/lab_pin.sym} 680 270 0 0 {name=p55 sig_type=std_logic lab=tas}
N 680 240 680 240 {lab=0}
C {devices/lab_pin.sym} 680 240 0 0 {name=p56 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 240 0 0 {name=mas6
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 210 900 210 {lab=s2as}
C {devices/lab_pin.sym} 900 210 0 0 {name=p57 sig_type=std_logic lab=s2as}
N 860 240 860 240 {lab=ckp}
C {devices/lab_pin.sym} 860 240 0 1 {name=p58 sig_type=std_logic lab=ckp}
N 900 270 900 270 {lab=tas}
C {devices/lab_pin.sym} 900 270 0 0 {name=p59 sig_type=std_logic lab=tas}
N 900 240 900 240 {lab=0}
C {devices/lab_pin.sym} 900 240 0 0 {name=p60 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 240 0 0 {name=mtas
w=15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 210 1120 210 {lab=tas}
C {devices/lab_pin.sym} 1120 210 0 0 {name=p61 sig_type=std_logic lab=tas}
N 1080 240 1080 240 {lab=nb_lo}
C {devices/lab_pin.sym} 1080 240 0 1 {name=p62 sig_type=std_logic lab=nb_lo}
N 1120 270 1120 270 {lab=0}
C {devices/lab_pin.sym} 1120 270 0 0 {name=p63 sig_type=std_logic lab=0}
N 1120 240 1120 240 {lab=0}
C {devices/lab_pin.sym} 1120 240 0 0 {name=p64 sig_type=std_logic lab=0}
