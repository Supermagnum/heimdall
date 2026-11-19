v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
C {devices/iopin.sym} -200 -40 0 0 {name=ckp lab=ckp}
C {devices/iopin.sym} -200 -80 0 0 {name=ckn lab=ckn}
C {devices/iopin.sym} -200 -120 0 0 {name=q2p lab=q2p}
C {devices/iopin.sym} -200 -160 0 0 {name=q2n lab=q2n}
C {devices/iopin.sym} -200 -200 0 0 {name=vref lab=vref}
C {devices/iopin.sym} -200 -240 0 0 {name=nb_lo lab=nb_lo}
C {devices/iopin.sym} -200 -280 0 0 {name=vdv lab=vdv}
C {devices/iopin.sym} -200 -320 0 0 {name=0 lab=0}
C {devices/title.sym} 0 40 0 0 {name=t1 author="HT13G-M P2.7.1"}
C {devices/lab_pin.sym} 200 40 0 0 {name=ttitle lab=cml_div3_vhf_tl_0p30}
C {devices/res.sym} 0 0 0 0 {name=rgp
value=1666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 0 -30 0 -30 {lab=vdv}
C {devices/lab_pin.sym} 0 -30 0 0 {name=p1 sig_type=std_logic lab=vdv}
N 0 30 0 30 {lab=orp}
C {devices/lab_pin.sym} 0 30 0 0 {name=p2 sig_type=std_logic lab=orp}
C {devices/res.sym} 220 0 0 0 {name=rgn
value=1666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 -30 220 -30 {lab=vdv}
C {devices/lab_pin.sym} 220 -30 0 0 {name=p3 sig_type=std_logic lab=vdv}
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
C {devices/res.sym} 0 120 0 0 {name=rlamp
value=1666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 0 90 0 90 {lab=vdv}
C {devices/lab_pin.sym} 0 90 0 0 {name=p21 sig_type=std_logic lab=vdv}
N 0 150 0 150 {lab=map}
C {devices/lab_pin.sym} 0 150 0 0 {name=p22 sig_type=std_logic lab=map}
C {devices/res.sym} 220 120 0 0 {name=rlamn
value=1666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 90 220 90 {lab=vdv}
C {devices/lab_pin.sym} 220 90 0 0 {name=p23 sig_type=std_logic lab=vdv}
N 220 150 220 150 {lab=man}
C {devices/lab_pin.sym} 220 150 0 0 {name=p24 sig_type=std_logic lab=man}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 120 0 0 {name=mam1
w=3.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 90 460 90 {lab=man}
C {devices/lab_pin.sym} 460 90 0 0 {name=p25 sig_type=std_logic lab=man}
N 420 120 420 120 {lab=orn}
C {devices/lab_pin.sym} 420 120 0 1 {name=p26 sig_type=std_logic lab=orn}
N 460 150 460 150 {lab=s1am}
C {devices/lab_pin.sym} 460 150 0 0 {name=p27 sig_type=std_logic lab=s1am}
N 460 120 460 120 {lab=0}
C {devices/lab_pin.sym} 460 120 0 0 {name=p28 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 120 0 0 {name=mam2
w=3.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 90 680 90 {lab=map}
C {devices/lab_pin.sym} 680 90 0 0 {name=p29 sig_type=std_logic lab=map}
N 640 120 640 120 {lab=orp}
C {devices/lab_pin.sym} 640 120 0 1 {name=p30 sig_type=std_logic lab=orp}
N 680 150 680 150 {lab=s1am}
C {devices/lab_pin.sym} 680 150 0 0 {name=p31 sig_type=std_logic lab=s1am}
N 680 120 680 120 {lab=0}
C {devices/lab_pin.sym} 680 120 0 0 {name=p32 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 120 0 0 {name=mam3
w=4.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 90 900 90 {lab=man}
C {devices/lab_pin.sym} 900 90 0 0 {name=p33 sig_type=std_logic lab=man}
N 860 120 860 120 {lab=map}
C {devices/lab_pin.sym} 860 120 0 1 {name=p34 sig_type=std_logic lab=map}
N 900 150 900 150 {lab=s2am}
C {devices/lab_pin.sym} 900 150 0 0 {name=p35 sig_type=std_logic lab=s2am}
N 900 120 900 120 {lab=0}
C {devices/lab_pin.sym} 900 120 0 0 {name=p36 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 120 0 0 {name=mam4
w=4.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 90 1120 90 {lab=map}
C {devices/lab_pin.sym} 1120 90 0 0 {name=p37 sig_type=std_logic lab=map}
N 1080 120 1080 120 {lab=man}
C {devices/lab_pin.sym} 1080 120 0 1 {name=p38 sig_type=std_logic lab=man}
N 1120 150 1120 150 {lab=s2am}
C {devices/lab_pin.sym} 1120 150 0 0 {name=p39 sig_type=std_logic lab=s2am}
N 1120 120 1120 120 {lab=0}
C {devices/lab_pin.sym} 1120 120 0 0 {name=p40 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 240 0 0 {name=mam5
w=3.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 210 20 210 {lab=s1am}
C {devices/lab_pin.sym} 20 210 0 0 {name=p41 sig_type=std_logic lab=s1am}
N -20 240 -20 240 {lab=ckp}
C {devices/lab_pin.sym} -20 240 0 1 {name=p42 sig_type=std_logic lab=ckp}
N 20 270 20 270 {lab=0}
C {devices/lab_pin.sym} 20 270 0 0 {name=p43 sig_type=std_logic lab=0}
N 20 240 20 240 {lab=0}
C {devices/lab_pin.sym} 20 240 0 0 {name=p44 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 240 0 0 {name=mam6
w=3.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 210 240 210 {lab=s2am}
C {devices/lab_pin.sym} 240 210 0 0 {name=p45 sig_type=std_logic lab=s2am}
N 200 240 200 240 {lab=ckn}
C {devices/lab_pin.sym} 200 240 0 1 {name=p46 sig_type=std_logic lab=ckn}
N 240 270 240 270 {lab=0}
C {devices/lab_pin.sym} 240 270 0 0 {name=p47 sig_type=std_logic lab=0}
N 240 240 240 240 {lab=0}
C {devices/lab_pin.sym} 240 240 0 0 {name=p48 sig_type=std_logic lab=0}
C {devices/res.sym} 440 240 0 0 {name=rlasp
value=1666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 440 210 440 210 {lab=vdv}
C {devices/lab_pin.sym} 440 210 0 0 {name=p49 sig_type=std_logic lab=vdv}
N 440 270 440 270 {lab=q1p}
C {devices/lab_pin.sym} 440 270 0 0 {name=p50 sig_type=std_logic lab=q1p}
C {devices/res.sym} 660 240 0 0 {name=rlasn
value=1666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 660 210 660 210 {lab=vdv}
C {devices/lab_pin.sym} 660 210 0 0 {name=p51 sig_type=std_logic lab=vdv}
N 660 270 660 270 {lab=q1n}
C {devices/lab_pin.sym} 660 270 0 0 {name=p52 sig_type=std_logic lab=q1n}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 240 0 0 {name=mas1
w=3.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 210 900 210 {lab=q1n}
C {devices/lab_pin.sym} 900 210 0 0 {name=p53 sig_type=std_logic lab=q1n}
N 860 240 860 240 {lab=map}
C {devices/lab_pin.sym} 860 240 0 1 {name=p54 sig_type=std_logic lab=map}
N 900 270 900 270 {lab=s1as}
C {devices/lab_pin.sym} 900 270 0 0 {name=p55 sig_type=std_logic lab=s1as}
N 900 240 900 240 {lab=0}
C {devices/lab_pin.sym} 900 240 0 0 {name=p56 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 240 0 0 {name=mas2
w=3.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 210 1120 210 {lab=q1p}
C {devices/lab_pin.sym} 1120 210 0 0 {name=p57 sig_type=std_logic lab=q1p}
N 1080 240 1080 240 {lab=man}
C {devices/lab_pin.sym} 1080 240 0 1 {name=p58 sig_type=std_logic lab=man}
N 1120 270 1120 270 {lab=s1as}
C {devices/lab_pin.sym} 1120 270 0 0 {name=p59 sig_type=std_logic lab=s1as}
N 1120 240 1120 240 {lab=0}
C {devices/lab_pin.sym} 1120 240 0 0 {name=p60 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 360 0 0 {name=mas3
w=4.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 330 20 330 {lab=q1n}
C {devices/lab_pin.sym} 20 330 0 0 {name=p61 sig_type=std_logic lab=q1n}
N -20 360 -20 360 {lab=q1p}
C {devices/lab_pin.sym} -20 360 0 1 {name=p62 sig_type=std_logic lab=q1p}
N 20 390 20 390 {lab=s2as}
C {devices/lab_pin.sym} 20 390 0 0 {name=p63 sig_type=std_logic lab=s2as}
N 20 360 20 360 {lab=0}
C {devices/lab_pin.sym} 20 360 0 0 {name=p64 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 360 0 0 {name=mas4
w=4.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 330 240 330 {lab=q1p}
C {devices/lab_pin.sym} 240 330 0 0 {name=p65 sig_type=std_logic lab=q1p}
N 200 360 200 360 {lab=q1n}
C {devices/lab_pin.sym} 200 360 0 1 {name=p66 sig_type=std_logic lab=q1n}
N 240 390 240 390 {lab=s2as}
C {devices/lab_pin.sym} 240 390 0 0 {name=p67 sig_type=std_logic lab=s2as}
N 240 360 240 360 {lab=0}
C {devices/lab_pin.sym} 240 360 0 0 {name=p68 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 360 0 0 {name=mas5
w=3.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 330 460 330 {lab=s1as}
C {devices/lab_pin.sym} 460 330 0 0 {name=p69 sig_type=std_logic lab=s1as}
N 420 360 420 360 {lab=ckn}
C {devices/lab_pin.sym} 420 360 0 1 {name=p70 sig_type=std_logic lab=ckn}
N 460 390 460 390 {lab=0}
C {devices/lab_pin.sym} 460 390 0 0 {name=p71 sig_type=std_logic lab=0}
N 460 360 460 360 {lab=0}
C {devices/lab_pin.sym} 460 360 0 0 {name=p72 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 360 0 0 {name=mas6
w=3.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 330 680 330 {lab=s2as}
C {devices/lab_pin.sym} 680 330 0 0 {name=p73 sig_type=std_logic lab=s2as}
N 640 360 640 360 {lab=ckp}
C {devices/lab_pin.sym} 640 360 0 1 {name=p74 sig_type=std_logic lab=ckp}
N 680 390 680 390 {lab=0}
C {devices/lab_pin.sym} 680 390 0 0 {name=p75 sig_type=std_logic lab=0}
N 680 360 680 360 {lab=0}
C {devices/lab_pin.sym} 680 360 0 0 {name=p76 sig_type=std_logic lab=0}
C {devices/res.sym} 880 360 0 0 {name=rlbmp
value=1666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 330 880 330 {lab=vdv}
C {devices/lab_pin.sym} 880 330 0 0 {name=p77 sig_type=std_logic lab=vdv}
N 880 390 880 390 {lab=mbp}
C {devices/lab_pin.sym} 880 390 0 0 {name=p78 sig_type=std_logic lab=mbp}
C {devices/res.sym} 1100 360 0 0 {name=rlbmn
value=1666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 1100 330 1100 330 {lab=vdv}
C {devices/lab_pin.sym} 1100 330 0 0 {name=p79 sig_type=std_logic lab=vdv}
N 1100 390 1100 390 {lab=mbn}
C {devices/lab_pin.sym} 1100 390 0 0 {name=p80 sig_type=std_logic lab=mbn}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 480 0 0 {name=mbm1
w=3.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 450 20 450 {lab=mbn}
C {devices/lab_pin.sym} 20 450 0 0 {name=p81 sig_type=std_logic lab=mbn}
N -20 480 -20 480 {lab=q1p}
C {devices/lab_pin.sym} -20 480 0 1 {name=p82 sig_type=std_logic lab=q1p}
N 20 510 20 510 {lab=s1bm}
C {devices/lab_pin.sym} 20 510 0 0 {name=p83 sig_type=std_logic lab=s1bm}
N 20 480 20 480 {lab=0}
C {devices/lab_pin.sym} 20 480 0 0 {name=p84 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 480 0 0 {name=mbm2
w=3.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 450 240 450 {lab=mbp}
C {devices/lab_pin.sym} 240 450 0 0 {name=p85 sig_type=std_logic lab=mbp}
N 200 480 200 480 {lab=q1n}
C {devices/lab_pin.sym} 200 480 0 1 {name=p86 sig_type=std_logic lab=q1n}
N 240 510 240 510 {lab=s1bm}
C {devices/lab_pin.sym} 240 510 0 0 {name=p87 sig_type=std_logic lab=s1bm}
N 240 480 240 480 {lab=0}
C {devices/lab_pin.sym} 240 480 0 0 {name=p88 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 480 0 0 {name=mbm3
w=4.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 450 460 450 {lab=mbn}
C {devices/lab_pin.sym} 460 450 0 0 {name=p89 sig_type=std_logic lab=mbn}
N 420 480 420 480 {lab=mbp}
C {devices/lab_pin.sym} 420 480 0 1 {name=p90 sig_type=std_logic lab=mbp}
N 460 510 460 510 {lab=s2bm}
C {devices/lab_pin.sym} 460 510 0 0 {name=p91 sig_type=std_logic lab=s2bm}
N 460 480 460 480 {lab=0}
C {devices/lab_pin.sym} 460 480 0 0 {name=p92 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 480 0 0 {name=mbm4
w=4.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 450 680 450 {lab=mbp}
C {devices/lab_pin.sym} 680 450 0 0 {name=p93 sig_type=std_logic lab=mbp}
N 640 480 640 480 {lab=mbn}
C {devices/lab_pin.sym} 640 480 0 1 {name=p94 sig_type=std_logic lab=mbn}
N 680 510 680 510 {lab=s2bm}
C {devices/lab_pin.sym} 680 510 0 0 {name=p95 sig_type=std_logic lab=s2bm}
N 680 480 680 480 {lab=0}
C {devices/lab_pin.sym} 680 480 0 0 {name=p96 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 480 0 0 {name=mbm5
w=3.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 450 900 450 {lab=s1bm}
C {devices/lab_pin.sym} 900 450 0 0 {name=p97 sig_type=std_logic lab=s1bm}
N 860 480 860 480 {lab=ckp}
C {devices/lab_pin.sym} 860 480 0 1 {name=p98 sig_type=std_logic lab=ckp}
N 900 510 900 510 {lab=0}
C {devices/lab_pin.sym} 900 510 0 0 {name=p99 sig_type=std_logic lab=0}
N 900 480 900 480 {lab=0}
C {devices/lab_pin.sym} 900 480 0 0 {name=p100 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 480 0 0 {name=mbm6
w=3.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 450 1120 450 {lab=s2bm}
C {devices/lab_pin.sym} 1120 450 0 0 {name=p101 sig_type=std_logic lab=s2bm}
N 1080 480 1080 480 {lab=ckn}
C {devices/lab_pin.sym} 1080 480 0 1 {name=p102 sig_type=std_logic lab=ckn}
N 1120 510 1120 510 {lab=0}
C {devices/lab_pin.sym} 1120 510 0 0 {name=p103 sig_type=std_logic lab=0}
N 1120 480 1120 480 {lab=0}
C {devices/lab_pin.sym} 1120 480 0 0 {name=p104 sig_type=std_logic lab=0}
C {devices/res.sym} 0 600 0 0 {name=rlbsp
value=1666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 0 570 0 570 {lab=vdv}
C {devices/lab_pin.sym} 0 570 0 0 {name=p105 sig_type=std_logic lab=vdv}
N 0 630 0 630 {lab=q2p}
C {devices/lab_pin.sym} 0 630 0 0 {name=p106 sig_type=std_logic lab=q2p}
C {devices/res.sym} 220 600 0 0 {name=rlbsn
value=1666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 570 220 570 {lab=vdv}
C {devices/lab_pin.sym} 220 570 0 0 {name=p107 sig_type=std_logic lab=vdv}
N 220 630 220 630 {lab=q2n}
C {devices/lab_pin.sym} 220 630 0 0 {name=p108 sig_type=std_logic lab=q2n}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 600 0 0 {name=mbs1
w=3.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 570 460 570 {lab=q2n}
C {devices/lab_pin.sym} 460 570 0 0 {name=p109 sig_type=std_logic lab=q2n}
N 420 600 420 600 {lab=mbp}
C {devices/lab_pin.sym} 420 600 0 1 {name=p110 sig_type=std_logic lab=mbp}
N 460 630 460 630 {lab=s1bs}
C {devices/lab_pin.sym} 460 630 0 0 {name=p111 sig_type=std_logic lab=s1bs}
N 460 600 460 600 {lab=0}
C {devices/lab_pin.sym} 460 600 0 0 {name=p112 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 600 0 0 {name=mbs2
w=3.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 570 680 570 {lab=q2p}
C {devices/lab_pin.sym} 680 570 0 0 {name=p113 sig_type=std_logic lab=q2p}
N 640 600 640 600 {lab=mbn}
C {devices/lab_pin.sym} 640 600 0 1 {name=p114 sig_type=std_logic lab=mbn}
N 680 630 680 630 {lab=s1bs}
C {devices/lab_pin.sym} 680 630 0 0 {name=p115 sig_type=std_logic lab=s1bs}
N 680 600 680 600 {lab=0}
C {devices/lab_pin.sym} 680 600 0 0 {name=p116 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 600 0 0 {name=mbs3
w=4.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 570 900 570 {lab=q2n}
C {devices/lab_pin.sym} 900 570 0 0 {name=p117 sig_type=std_logic lab=q2n}
N 860 600 860 600 {lab=q2p}
C {devices/lab_pin.sym} 860 600 0 1 {name=p118 sig_type=std_logic lab=q2p}
N 900 630 900 630 {lab=s2bs}
C {devices/lab_pin.sym} 900 630 0 0 {name=p119 sig_type=std_logic lab=s2bs}
N 900 600 900 600 {lab=0}
C {devices/lab_pin.sym} 900 600 0 0 {name=p120 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 600 0 0 {name=mbs4
w=4.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 570 1120 570 {lab=q2p}
C {devices/lab_pin.sym} 1120 570 0 0 {name=p121 sig_type=std_logic lab=q2p}
N 1080 600 1080 600 {lab=q2n}
C {devices/lab_pin.sym} 1080 600 0 1 {name=p122 sig_type=std_logic lab=q2n}
N 1120 630 1120 630 {lab=s2bs}
C {devices/lab_pin.sym} 1120 630 0 0 {name=p123 sig_type=std_logic lab=s2bs}
N 1120 600 1120 600 {lab=0}
C {devices/lab_pin.sym} 1120 600 0 0 {name=p124 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 720 0 0 {name=mbs5
w=3.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 690 20 690 {lab=s1bs}
C {devices/lab_pin.sym} 20 690 0 0 {name=p125 sig_type=std_logic lab=s1bs}
N -20 720 -20 720 {lab=ckn}
C {devices/lab_pin.sym} -20 720 0 1 {name=p126 sig_type=std_logic lab=ckn}
N 20 750 20 750 {lab=0}
C {devices/lab_pin.sym} 20 750 0 0 {name=p127 sig_type=std_logic lab=0}
N 20 720 20 720 {lab=0}
C {devices/lab_pin.sym} 20 720 0 0 {name=p128 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 720 0 0 {name=mbs6
w=3.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 690 240 690 {lab=s2bs}
C {devices/lab_pin.sym} 240 690 0 0 {name=p129 sig_type=std_logic lab=s2bs}
N 200 720 200 720 {lab=ckp}
C {devices/lab_pin.sym} 200 720 0 1 {name=p130 sig_type=std_logic lab=ckp}
N 240 750 240 750 {lab=0}
C {devices/lab_pin.sym} 240 750 0 0 {name=p131 sig_type=std_logic lab=0}
N 240 720 240 720 {lab=0}
C {devices/lab_pin.sym} 240 720 0 0 {name=p132 sig_type=std_logic lab=0}
