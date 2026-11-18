v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
C {devices/iopin.sym} -200 -40 0 0 {name=tp lab=tp}
C {devices/iopin.sym} -200 -80 0 0 {name=tn lab=tn}
C {devices/iopin.sym} -200 -120 0 0 {name=vt lab=vt}
C {devices/iopin.sym} -200 -160 0 0 {name=vbp lab=vbp}
C {devices/iopin.sym} -200 -200 0 0 {name=gnd lab=gnd}
C {devices/title.sym} 0 40 0 0 {name=t1 author="HT13G-M P2.7.1"}
C {devices/lab_pin.sym} 200 40 0 0 {name=ttitle lab=vco_var_AC_D11}
C {sg13g2_pr/cap_rfcmim.sym} 0 0 0 0 {name=xcp
model=cap_rfcmim
lvs_model=rfcmim
w=2.129200e-05
l=2.129200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 0 -30 0 -30 {lab=tp}
C {devices/lab_pin.sym} 0 -30 0 0 {name=p1 sig_type=std_logic lab=tp}
N 0 30 0 30 {lab=vgp}
C {devices/lab_pin.sym} 0 30 0 0 {name=p2 sig_type=std_logic lab=vgp}
N -30 0 -30 0 {lab=gnd}
C {devices/lab_pin.sym} -30 0 0 0 {name=p3 sig_type=std_logic lab=gnd}
C {sg13g2_pr/cap_rfcmim.sym} 220 0 0 0 {name=xcn
model=cap_rfcmim
lvs_model=rfcmim
w=2.129200e-05
l=2.129200e-05
wfeed=5.0e-6
m=1
mm_ok=1
spiceprefix=X
}
N 220 -30 220 -30 {lab=tn}
C {devices/lab_pin.sym} 220 -30 0 0 {name=p4 sig_type=std_logic lab=tn}
N 220 30 220 30 {lab=vgn}
C {devices/lab_pin.sym} 220 30 0 0 {name=p5 sig_type=std_logic lab=vgn}
N 190 0 190 0 {lab=gnd}
C {devices/lab_pin.sym} 190 0 0 0 {name=p6 sig_type=std_logic lab=gnd}
C {sg13g2_pr/rhigh.sym} 440 0 0 0 {name=rvp
w=5.000000e-07
l=4.209500e-05
b=16
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 440 -30 440 -30 {lab=vgp}
C {devices/lab_pin.sym} 440 -30 0 0 {name=p7 sig_type=std_logic lab=vgp}
N 440 30 440 30 {lab=vvb}
C {devices/lab_pin.sym} 440 30 0 0 {name=p8 sig_type=std_logic lab=vvb}
C {sg13g2_pr/rhigh.sym} 660 0 0 0 {name=rvn
w=5.000000e-07
l=4.209500e-05
b=16
m=1
model=rhigh
body=gnd
spiceprefix=X
mm_ok=1
}
N 660 -30 660 -30 {lab=vgn}
C {devices/lab_pin.sym} 660 -30 0 0 {name=p9 sig_type=std_logic lab=vgn}
N 660 30 660 30 {lab=vvb}
C {devices/lab_pin.sym} 660 30 0 0 {name=p10 sig_type=std_logic lab=vvb}
C {sg13g2_pr/sg13_svaricap.sym} 880 0 0 0 {name=xv1
model=sg13_hv_svaricap_fx
W=3.740000e-06
L=3.000000e-07
Nx=10
spiceprefix=X
}
N 920 0 920 0 {lab=vgp}
C {devices/lab_pin.sym} 920 0 0 0 {name=p11 sig_type=std_logic lab=vgp}
N 880 -30 880 -30 {lab=vt}
C {devices/lab_pin.sym} 880 -30 0 0 {name=p12 sig_type=std_logic lab=vt}
N 840 0 840 0 {lab=vgn}
C {devices/lab_pin.sym} 840 0 0 0 {name=p13 sig_type=std_logic lab=vgn}
C {sg13g2_pr/sg13_svaricap.sym} 1100 0 0 0 {name=xv2
model=sg13_hv_svaricap_fx
W=3.740000e-06
L=3.000000e-07
Nx=10
spiceprefix=X
}
N 1140 0 1140 0 {lab=vgp}
C {devices/lab_pin.sym} 1140 0 0 0 {name=p14 sig_type=std_logic lab=vgp}
N 1100 -30 1100 -30 {lab=vt}
C {devices/lab_pin.sym} 1100 -30 0 0 {name=p15 sig_type=std_logic lab=vt}
N 1060 0 1060 0 {lab=vgn}
C {devices/lab_pin.sym} 1060 0 0 0 {name=p16 sig_type=std_logic lab=vgn}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 120 0 0 {name=mbp_rvp
w=5u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 90 20 90 {lab=vgp}
C {devices/lab_pin.sym} 20 90 0 0 {name=p17 sig_type=std_logic lab=vgp}
N -20 120 -20 120 {lab=vbp}
C {devices/lab_pin.sym} -20 120 0 1 {name=p18 sig_type=std_logic lab=vbp}
N 20 150 20 150 {lab=vvb}
C {devices/lab_pin.sym} 20 150 0 0 {name=p19 sig_type=std_logic lab=vvb}
N 20 120 20 120 {lab=gnd}
C {devices/lab_pin.sym} 20 120 0 0 {name=p20 sig_type=std_logic lab=gnd}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 120 0 0 {name=mbp_rvn
w=5u
l=0.13u
ng=2
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 90 240 90 {lab=vgn}
C {devices/lab_pin.sym} 240 90 0 0 {name=p21 sig_type=std_logic lab=vgn}
N 200 120 200 120 {lab=vbp}
C {devices/lab_pin.sym} 200 120 0 1 {name=p22 sig_type=std_logic lab=vbp}
N 240 150 240 150 {lab=vvb}
C {devices/lab_pin.sym} 240 150 0 0 {name=p23 sig_type=std_logic lab=vvb}
N 240 120 240 120 {lab=gnd}
C {devices/lab_pin.sym} 240 120 0 0 {name=p24 sig_type=std_logic lab=gnd}
