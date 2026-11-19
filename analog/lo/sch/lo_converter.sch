v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
C {devices/iopin.sym} -200 -40 0 0 {name=dp lab=dp}
C {devices/iopin.sym} -200 -80 0 0 {name=dn lab=dn}
C {devices/iopin.sym} -200 -120 0 0 {name=y lab=y}
C {devices/iopin.sym} -200 -160 0 0 {name=vcv lab=vcv}
C {devices/iopin.sym} -200 -200 0 0 {name=0 lab=0}
C {devices/title.sym} 0 40 0 0 {name=t1 author="HT13G-M P2.7.1"}
C {devices/lab_pin.sym} 200 40 0 0 {name=ttitle lab=lo_converter_acconv}
C {devices/capa.sym} 0 0 0 0 {name=ccap
value=50f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 0 -30 0 -30 {lab=dp}
C {devices/lab_pin.sym} 0 -30 0 0 {name=p1 sig_type=std_logic lab=dp}
N 0 30 0 30 {lab=x_cip}
C {devices/lab_pin.sym} 0 30 0 0 {name=p2 sig_type=std_logic lab=x_cip}
C {devices/res.sym} 220 0 0 0 {name=rcap
value=50k
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 -30 220 -30 {lab=x_cip}
C {devices/lab_pin.sym} 220 -30 0 0 {name=p3 sig_type=std_logic lab=x_cip}
N 220 30 220 30 {lab=x_o2p}
C {devices/lab_pin.sym} 220 30 0 0 {name=p4 sig_type=std_logic lab=x_o2p}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 0 0 0 {name=xcapp
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 30 460 30 {lab=x_o2p}
C {devices/lab_pin.sym} 460 30 0 0 {name=p5 sig_type=std_logic lab=x_o2p}
N 420 0 420 0 {lab=x_cip}
C {devices/lab_pin.sym} 420 0 0 1 {name=p6 sig_type=std_logic lab=x_cip}
N 460 -30 460 -30 {lab=vcv}
C {devices/lab_pin.sym} 460 -30 0 0 {name=p7 sig_type=std_logic lab=vcv}
N 460 0 460 0 {lab=vcv}
C {devices/lab_pin.sym} 460 0 0 0 {name=p8 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 0 0 0 {name=xcapn
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 -30 680 -30 {lab=x_o2p}
C {devices/lab_pin.sym} 680 -30 0 0 {name=p9 sig_type=std_logic lab=x_o2p}
N 640 0 640 0 {lab=x_cip}
C {devices/lab_pin.sym} 640 0 0 1 {name=p10 sig_type=std_logic lab=x_cip}
N 680 30 680 30 {lab=0}
C {devices/lab_pin.sym} 680 30 0 0 {name=p11 sig_type=std_logic lab=0}
N 680 0 680 0 {lab=0}
C {devices/lab_pin.sym} 680 0 0 0 {name=p12 sig_type=std_logic lab=0}
C {devices/capa.sym} 880 0 0 0 {name=ccan
value=50f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 880 -30 880 -30 {lab=dn}
C {devices/lab_pin.sym} 880 -30 0 0 {name=p13 sig_type=std_logic lab=dn}
N 880 30 880 30 {lab=x_cin}
C {devices/lab_pin.sym} 880 30 0 0 {name=p14 sig_type=std_logic lab=x_cin}
C {devices/res.sym} 1100 0 0 0 {name=rcan
value=50k
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 1100 -30 1100 -30 {lab=x_cin}
C {devices/lab_pin.sym} 1100 -30 0 0 {name=p15 sig_type=std_logic lab=x_cin}
N 1100 30 1100 30 {lab=x_o2n}
C {devices/lab_pin.sym} 1100 30 0 0 {name=p16 sig_type=std_logic lab=x_o2n}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 120 0 0 {name=xcanp
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 150 20 150 {lab=x_o2n}
C {devices/lab_pin.sym} 20 150 0 0 {name=p17 sig_type=std_logic lab=x_o2n}
N -20 120 -20 120 {lab=x_cin}
C {devices/lab_pin.sym} -20 120 0 1 {name=p18 sig_type=std_logic lab=x_cin}
N 20 90 20 90 {lab=vcv}
C {devices/lab_pin.sym} 20 90 0 0 {name=p19 sig_type=std_logic lab=vcv}
N 20 120 20 120 {lab=vcv}
C {devices/lab_pin.sym} 20 120 0 0 {name=p20 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 120 0 0 {name=xcann
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 90 240 90 {lab=x_o2n}
C {devices/lab_pin.sym} 240 90 0 0 {name=p21 sig_type=std_logic lab=x_o2n}
N 200 120 200 120 {lab=x_cin}
C {devices/lab_pin.sym} 200 120 0 1 {name=p22 sig_type=std_logic lab=x_cin}
N 240 150 240 150 {lab=0}
C {devices/lab_pin.sym} 240 150 0 0 {name=p23 sig_type=std_logic lab=0}
N 240 120 240 120 {lab=0}
C {devices/lab_pin.sym} 240 120 0 0 {name=p24 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 120 0 0 {name=xcxpp
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 150 460 150 {lab=x_o2n}
C {devices/lab_pin.sym} 460 150 0 0 {name=p25 sig_type=std_logic lab=x_o2n}
N 420 120 420 120 {lab=x_o2p}
C {devices/lab_pin.sym} 420 120 0 1 {name=p26 sig_type=std_logic lab=x_o2p}
N 460 90 460 90 {lab=vcv}
C {devices/lab_pin.sym} 460 90 0 0 {name=p27 sig_type=std_logic lab=vcv}
N 460 120 460 120 {lab=vcv}
C {devices/lab_pin.sym} 460 120 0 0 {name=p28 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 120 0 0 {name=xcxpn
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 90 680 90 {lab=x_o2n}
C {devices/lab_pin.sym} 680 90 0 0 {name=p29 sig_type=std_logic lab=x_o2n}
N 640 120 640 120 {lab=x_o2p}
C {devices/lab_pin.sym} 640 120 0 1 {name=p30 sig_type=std_logic lab=x_o2p}
N 680 150 680 150 {lab=0}
C {devices/lab_pin.sym} 680 150 0 0 {name=p31 sig_type=std_logic lab=0}
N 680 120 680 120 {lab=0}
C {devices/lab_pin.sym} 680 120 0 0 {name=p32 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 120 0 0 {name=xcxnp
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 150 900 150 {lab=x_o2p}
C {devices/lab_pin.sym} 900 150 0 0 {name=p33 sig_type=std_logic lab=x_o2p}
N 860 120 860 120 {lab=x_o2n}
C {devices/lab_pin.sym} 860 120 0 1 {name=p34 sig_type=std_logic lab=x_o2n}
N 900 90 900 90 {lab=vcv}
C {devices/lab_pin.sym} 900 90 0 0 {name=p35 sig_type=std_logic lab=vcv}
N 900 120 900 120 {lab=vcv}
C {devices/lab_pin.sym} 900 120 0 0 {name=p36 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 120 0 0 {name=xcxnn
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 90 1120 90 {lab=x_o2p}
C {devices/lab_pin.sym} 1120 90 0 0 {name=p37 sig_type=std_logic lab=x_o2p}
N 1080 120 1080 120 {lab=x_o2n}
C {devices/lab_pin.sym} 1080 120 0 1 {name=p38 sig_type=std_logic lab=x_o2n}
N 1120 150 1120 150 {lab=0}
C {devices/lab_pin.sym} 1120 150 0 0 {name=p39 sig_type=std_logic lab=0}
N 1120 120 1120 120 {lab=0}
C {devices/lab_pin.sym} 1120 120 0 0 {name=p40 sig_type=std_logic lab=0}
C {devices/capa.sym} 0 240 0 0 {name=ccb
value=50f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 0 210 0 210 {lab=x_o2p}
C {devices/lab_pin.sym} 0 210 0 0 {name=p41 sig_type=std_logic lab=x_o2p}
N 0 270 0 270 {lab=x_cbi}
C {devices/lab_pin.sym} 0 270 0 0 {name=p42 sig_type=std_logic lab=x_cbi}
C {devices/res.sym} 220 240 0 0 {name=rcb
value=50k
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 210 220 210 {lab=x_cbi}
C {devices/lab_pin.sym} 220 210 0 0 {name=p43 sig_type=std_logic lab=x_cbi}
N 220 270 220 270 {lab=x_cy}
C {devices/lab_pin.sym} 220 270 0 0 {name=p44 sig_type=std_logic lab=x_cy}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 240 0 0 {name=xcbp
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 270 460 270 {lab=x_cy}
C {devices/lab_pin.sym} 460 270 0 0 {name=p45 sig_type=std_logic lab=x_cy}
N 420 240 420 240 {lab=x_cbi}
C {devices/lab_pin.sym} 420 240 0 1 {name=p46 sig_type=std_logic lab=x_cbi}
N 460 210 460 210 {lab=vcv}
C {devices/lab_pin.sym} 460 210 0 0 {name=p47 sig_type=std_logic lab=vcv}
N 460 240 460 240 {lab=vcv}
C {devices/lab_pin.sym} 460 240 0 0 {name=p48 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 240 0 0 {name=xcbn
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 210 680 210 {lab=x_cy}
C {devices/lab_pin.sym} 680 210 0 0 {name=p49 sig_type=std_logic lab=x_cy}
N 640 240 640 240 {lab=x_cbi}
C {devices/lab_pin.sym} 640 240 0 1 {name=p50 sig_type=std_logic lab=x_cbi}
N 680 270 680 270 {lab=0}
C {devices/lab_pin.sym} 680 270 0 0 {name=p51 sig_type=std_logic lab=0}
N 680 240 680 240 {lab=0}
C {devices/lab_pin.sym} 680 240 0 0 {name=p52 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 240 0 0 {name=xcv3p
w=6.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 270 900 270 {lab=x_cz}
C {devices/lab_pin.sym} 900 270 0 0 {name=p53 sig_type=std_logic lab=x_cz}
N 860 240 860 240 {lab=x_cy}
C {devices/lab_pin.sym} 860 240 0 1 {name=p54 sig_type=std_logic lab=x_cy}
N 900 210 900 210 {lab=vcv}
C {devices/lab_pin.sym} 900 210 0 0 {name=p55 sig_type=std_logic lab=vcv}
N 900 240 900 240 {lab=vcv}
C {devices/lab_pin.sym} 900 240 0 0 {name=p56 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 240 0 0 {name=xcv3n
w=3.0u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 210 1120 210 {lab=x_cz}
C {devices/lab_pin.sym} 1120 210 0 0 {name=p57 sig_type=std_logic lab=x_cz}
N 1080 240 1080 240 {lab=x_cy}
C {devices/lab_pin.sym} 1080 240 0 1 {name=p58 sig_type=std_logic lab=x_cy}
N 1120 270 1120 270 {lab=0}
C {devices/lab_pin.sym} 1120 270 0 0 {name=p59 sig_type=std_logic lab=0}
N 1120 240 1120 240 {lab=0}
C {devices/lab_pin.sym} 1120 240 0 0 {name=p60 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 360 0 0 {name=xcv4p
w=18.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 390 20 390 {lab=y}
C {devices/lab_pin.sym} 20 390 0 0 {name=p61 sig_type=std_logic lab=y}
N -20 360 -20 360 {lab=x_cz}
C {devices/lab_pin.sym} -20 360 0 1 {name=p62 sig_type=std_logic lab=x_cz}
N 20 330 20 330 {lab=vcv}
C {devices/lab_pin.sym} 20 330 0 0 {name=p63 sig_type=std_logic lab=vcv}
N 20 360 20 360 {lab=vcv}
C {devices/lab_pin.sym} 20 360 0 0 {name=p64 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 360 0 0 {name=xcv4n
w=9.0u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 330 240 330 {lab=y}
C {devices/lab_pin.sym} 240 330 0 0 {name=p65 sig_type=std_logic lab=y}
N 200 360 200 360 {lab=x_cz}
C {devices/lab_pin.sym} 200 360 0 1 {name=p66 sig_type=std_logic lab=x_cz}
N 240 390 240 390 {lab=0}
C {devices/lab_pin.sym} 240 390 0 0 {name=p67 sig_type=std_logic lab=0}
N 240 360 240 360 {lab=0}
C {devices/lab_pin.sym} 240 360 0 0 {name=p68 sig_type=std_logic lab=0}
