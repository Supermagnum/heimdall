v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
C {devices/iopin.sym} -200 -40 0 0 {name=x_clk lab=x_clk}
C {devices/iopin.sym} -200 -80 0 0 {name=x_p0 lab=x_p0}
C {devices/iopin.sym} -200 -120 0 0 {name=x_p1 lab=x_p1}
C {devices/iopin.sym} -200 -160 0 0 {name=x_p2 lab=x_p2}
C {devices/iopin.sym} -200 -200 0 0 {name=x_p3 lab=x_p3}
C {devices/iopin.sym} -200 -240 0 0 {name=vdg lab=vdg}
C {devices/iopin.sym} -200 -280 0 0 {name=0 lab=0}
C {devices/title.sym} 0 40 0 0 {name=t1 author="HT13G-M P2.7.1"}
C {devices/lab_pin.sym} 200 40 0 0 {name=ttitle lab=lo_johnson_uhf_div4_25pct}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 0 0 0 {name=xf1p1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 30 20 30 {lab=x_f1_x1}
C {devices/lab_pin.sym} 20 30 0 0 {name=p1 sig_type=std_logic lab=x_f1_x1}
N -20 0 -20 0 {lab=x_q2}
C {devices/lab_pin.sym} -20 0 0 1 {name=p2 sig_type=std_logic lab=x_q2}
N 20 -30 20 -30 {lab=vdg}
C {devices/lab_pin.sym} 20 -30 0 0 {name=p3 sig_type=std_logic lab=vdg}
N 20 0 20 0 {lab=vdg}
C {devices/lab_pin.sym} 20 0 0 0 {name=p4 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 0 0 0 {name=xf1p2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 30 240 30 {lab=x_f1_a}
C {devices/lab_pin.sym} 240 30 0 0 {name=p5 sig_type=std_logic lab=x_f1_a}
N 200 0 200 0 {lab=x_clk}
C {devices/lab_pin.sym} 200 0 0 1 {name=p6 sig_type=std_logic lab=x_clk}
N 240 -30 240 -30 {lab=x_f1_x1}
C {devices/lab_pin.sym} 240 -30 0 0 {name=p7 sig_type=std_logic lab=x_f1_x1}
N 240 0 240 0 {lab=vdg}
C {devices/lab_pin.sym} 240 0 0 0 {name=p8 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 0 0 0 {name=xf1n1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 -30 460 -30 {lab=x_f1_a}
C {devices/lab_pin.sym} 460 -30 0 0 {name=p9 sig_type=std_logic lab=x_f1_a}
N 420 0 420 0 {lab=x_q2}
C {devices/lab_pin.sym} 420 0 0 1 {name=p10 sig_type=std_logic lab=x_q2}
N 460 30 460 30 {lab=0}
C {devices/lab_pin.sym} 460 30 0 0 {name=p11 sig_type=std_logic lab=0}
N 460 0 460 0 {lab=0}
C {devices/lab_pin.sym} 460 0 0 0 {name=p12 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 0 0 0 {name=xf1p3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 30 680 30 {lab=x_f1_b}
C {devices/lab_pin.sym} 680 30 0 0 {name=p13 sig_type=std_logic lab=x_f1_b}
N 640 0 640 0 {lab=x_clk}
C {devices/lab_pin.sym} 640 0 0 1 {name=p14 sig_type=std_logic lab=x_clk}
N 680 -30 680 -30 {lab=vdg}
C {devices/lab_pin.sym} 680 -30 0 0 {name=p15 sig_type=std_logic lab=vdg}
N 680 0 680 0 {lab=vdg}
C {devices/lab_pin.sym} 680 0 0 0 {name=p16 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 0 0 0 {name=xf1n2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 -30 900 -30 {lab=x_f1_b}
C {devices/lab_pin.sym} 900 -30 0 0 {name=p17 sig_type=std_logic lab=x_f1_b}
N 860 0 860 0 {lab=x_f1_a}
C {devices/lab_pin.sym} 860 0 0 1 {name=p18 sig_type=std_logic lab=x_f1_a}
N 900 30 900 30 {lab=x_f1_x2}
C {devices/lab_pin.sym} 900 30 0 0 {name=p19 sig_type=std_logic lab=x_f1_x2}
N 900 0 900 0 {lab=0}
C {devices/lab_pin.sym} 900 0 0 0 {name=p20 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 0 0 0 {name=xf1n3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 -30 1120 -30 {lab=x_f1_x2}
C {devices/lab_pin.sym} 1120 -30 0 0 {name=p21 sig_type=std_logic lab=x_f1_x2}
N 1080 0 1080 0 {lab=x_clk}
C {devices/lab_pin.sym} 1080 0 0 1 {name=p22 sig_type=std_logic lab=x_clk}
N 1120 30 1120 30 {lab=0}
C {devices/lab_pin.sym} 1120 30 0 0 {name=p23 sig_type=std_logic lab=0}
N 1120 0 1120 0 {lab=0}
C {devices/lab_pin.sym} 1120 0 0 0 {name=p24 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 120 0 0 {name=xf1p4
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 150 20 150 {lab=x_q1}
C {devices/lab_pin.sym} 20 150 0 0 {name=p25 sig_type=std_logic lab=x_q1}
N -20 120 -20 120 {lab=x_f1_b}
C {devices/lab_pin.sym} -20 120 0 1 {name=p26 sig_type=std_logic lab=x_f1_b}
N 20 90 20 90 {lab=vdg}
C {devices/lab_pin.sym} 20 90 0 0 {name=p27 sig_type=std_logic lab=vdg}
N 20 120 20 120 {lab=vdg}
C {devices/lab_pin.sym} 20 120 0 0 {name=p28 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 120 0 0 {name=xf1n4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 90 240 90 {lab=x_q1}
C {devices/lab_pin.sym} 240 90 0 0 {name=p29 sig_type=std_logic lab=x_q1}
N 200 120 200 120 {lab=x_clk}
C {devices/lab_pin.sym} 200 120 0 1 {name=p30 sig_type=std_logic lab=x_clk}
N 240 150 240 150 {lab=x_f1_x3}
C {devices/lab_pin.sym} 240 150 0 0 {name=p31 sig_type=std_logic lab=x_f1_x3}
N 240 120 240 120 {lab=0}
C {devices/lab_pin.sym} 240 120 0 0 {name=p32 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 120 0 0 {name=xf1n5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 90 460 90 {lab=x_f1_x3}
C {devices/lab_pin.sym} 460 90 0 0 {name=p33 sig_type=std_logic lab=x_f1_x3}
N 420 120 420 120 {lab=x_f1_b}
C {devices/lab_pin.sym} 420 120 0 1 {name=p34 sig_type=std_logic lab=x_f1_b}
N 460 150 460 150 {lab=0}
C {devices/lab_pin.sym} 460 150 0 0 {name=p35 sig_type=std_logic lab=0}
N 460 120 460 120 {lab=0}
C {devices/lab_pin.sym} 460 120 0 0 {name=p36 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 120 0 0 {name=xi1p
w=1.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 150 680 150 {lab=x_q1b}
C {devices/lab_pin.sym} 680 150 0 0 {name=p37 sig_type=std_logic lab=x_q1b}
N 640 120 640 120 {lab=x_q1}
C {devices/lab_pin.sym} 640 120 0 1 {name=p38 sig_type=std_logic lab=x_q1}
N 680 90 680 90 {lab=vdg}
C {devices/lab_pin.sym} 680 90 0 0 {name=p39 sig_type=std_logic lab=vdg}
N 680 120 680 120 {lab=vdg}
C {devices/lab_pin.sym} 680 120 0 0 {name=p40 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 120 0 0 {name=xi1n
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 90 900 90 {lab=x_q1b}
C {devices/lab_pin.sym} 900 90 0 0 {name=p41 sig_type=std_logic lab=x_q1b}
N 860 120 860 120 {lab=x_q1}
C {devices/lab_pin.sym} 860 120 0 1 {name=p42 sig_type=std_logic lab=x_q1}
N 900 150 900 150 {lab=0}
C {devices/lab_pin.sym} 900 150 0 0 {name=p43 sig_type=std_logic lab=0}
N 900 120 900 120 {lab=0}
C {devices/lab_pin.sym} 900 120 0 0 {name=p44 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 120 0 0 {name=xf2p1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 150 1120 150 {lab=x_f2_x1}
C {devices/lab_pin.sym} 1120 150 0 0 {name=p45 sig_type=std_logic lab=x_f2_x1}
N 1080 120 1080 120 {lab=x_q1b}
C {devices/lab_pin.sym} 1080 120 0 1 {name=p46 sig_type=std_logic lab=x_q1b}
N 1120 90 1120 90 {lab=vdg}
C {devices/lab_pin.sym} 1120 90 0 0 {name=p47 sig_type=std_logic lab=vdg}
N 1120 120 1120 120 {lab=vdg}
C {devices/lab_pin.sym} 1120 120 0 0 {name=p48 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 240 0 0 {name=xf2p2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 270 20 270 {lab=x_f2_a}
C {devices/lab_pin.sym} 20 270 0 0 {name=p49 sig_type=std_logic lab=x_f2_a}
N -20 240 -20 240 {lab=x_clk}
C {devices/lab_pin.sym} -20 240 0 1 {name=p50 sig_type=std_logic lab=x_clk}
N 20 210 20 210 {lab=x_f2_x1}
C {devices/lab_pin.sym} 20 210 0 0 {name=p51 sig_type=std_logic lab=x_f2_x1}
N 20 240 20 240 {lab=vdg}
C {devices/lab_pin.sym} 20 240 0 0 {name=p52 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 240 0 0 {name=xf2n1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 210 240 210 {lab=x_f2_a}
C {devices/lab_pin.sym} 240 210 0 0 {name=p53 sig_type=std_logic lab=x_f2_a}
N 200 240 200 240 {lab=x_q1b}
C {devices/lab_pin.sym} 200 240 0 1 {name=p54 sig_type=std_logic lab=x_q1b}
N 240 270 240 270 {lab=0}
C {devices/lab_pin.sym} 240 270 0 0 {name=p55 sig_type=std_logic lab=0}
N 240 240 240 240 {lab=0}
C {devices/lab_pin.sym} 240 240 0 0 {name=p56 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 240 0 0 {name=xf2p3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 270 460 270 {lab=x_f2_b}
C {devices/lab_pin.sym} 460 270 0 0 {name=p57 sig_type=std_logic lab=x_f2_b}
N 420 240 420 240 {lab=x_clk}
C {devices/lab_pin.sym} 420 240 0 1 {name=p58 sig_type=std_logic lab=x_clk}
N 460 210 460 210 {lab=vdg}
C {devices/lab_pin.sym} 460 210 0 0 {name=p59 sig_type=std_logic lab=vdg}
N 460 240 460 240 {lab=vdg}
C {devices/lab_pin.sym} 460 240 0 0 {name=p60 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 240 0 0 {name=xf2n2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 210 680 210 {lab=x_f2_b}
C {devices/lab_pin.sym} 680 210 0 0 {name=p61 sig_type=std_logic lab=x_f2_b}
N 640 240 640 240 {lab=x_f2_a}
C {devices/lab_pin.sym} 640 240 0 1 {name=p62 sig_type=std_logic lab=x_f2_a}
N 680 270 680 270 {lab=x_f2_x2}
C {devices/lab_pin.sym} 680 270 0 0 {name=p63 sig_type=std_logic lab=x_f2_x2}
N 680 240 680 240 {lab=0}
C {devices/lab_pin.sym} 680 240 0 0 {name=p64 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 240 0 0 {name=xf2n3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 210 900 210 {lab=x_f2_x2}
C {devices/lab_pin.sym} 900 210 0 0 {name=p65 sig_type=std_logic lab=x_f2_x2}
N 860 240 860 240 {lab=x_clk}
C {devices/lab_pin.sym} 860 240 0 1 {name=p66 sig_type=std_logic lab=x_clk}
N 900 270 900 270 {lab=0}
C {devices/lab_pin.sym} 900 270 0 0 {name=p67 sig_type=std_logic lab=0}
N 900 240 900 240 {lab=0}
C {devices/lab_pin.sym} 900 240 0 0 {name=p68 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 240 0 0 {name=xf2p4
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 270 1120 270 {lab=x_q2}
C {devices/lab_pin.sym} 1120 270 0 0 {name=p69 sig_type=std_logic lab=x_q2}
N 1080 240 1080 240 {lab=x_f2_b}
C {devices/lab_pin.sym} 1080 240 0 1 {name=p70 sig_type=std_logic lab=x_f2_b}
N 1120 210 1120 210 {lab=vdg}
C {devices/lab_pin.sym} 1120 210 0 0 {name=p71 sig_type=std_logic lab=vdg}
N 1120 240 1120 240 {lab=vdg}
C {devices/lab_pin.sym} 1120 240 0 0 {name=p72 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 360 0 0 {name=xf2n4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 330 20 330 {lab=x_q2}
C {devices/lab_pin.sym} 20 330 0 0 {name=p73 sig_type=std_logic lab=x_q2}
N -20 360 -20 360 {lab=x_clk}
C {devices/lab_pin.sym} -20 360 0 1 {name=p74 sig_type=std_logic lab=x_clk}
N 20 390 20 390 {lab=x_f2_x3}
C {devices/lab_pin.sym} 20 390 0 0 {name=p75 sig_type=std_logic lab=x_f2_x3}
N 20 360 20 360 {lab=0}
C {devices/lab_pin.sym} 20 360 0 0 {name=p76 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 360 0 0 {name=xf2n5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 330 240 330 {lab=x_f2_x3}
C {devices/lab_pin.sym} 240 330 0 0 {name=p77 sig_type=std_logic lab=x_f2_x3}
N 200 360 200 360 {lab=x_f2_b}
C {devices/lab_pin.sym} 200 360 0 1 {name=p78 sig_type=std_logic lab=x_f2_b}
N 240 390 240 390 {lab=0}
C {devices/lab_pin.sym} 240 390 0 0 {name=p79 sig_type=std_logic lab=0}
N 240 360 240 360 {lab=0}
C {devices/lab_pin.sym} 240 360 0 0 {name=p80 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 360 0 0 {name=xi2p
w=1.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 390 460 390 {lab=x_q2b}
C {devices/lab_pin.sym} 460 390 0 0 {name=p81 sig_type=std_logic lab=x_q2b}
N 420 360 420 360 {lab=x_q2}
C {devices/lab_pin.sym} 420 360 0 1 {name=p82 sig_type=std_logic lab=x_q2}
N 460 330 460 330 {lab=vdg}
C {devices/lab_pin.sym} 460 330 0 0 {name=p83 sig_type=std_logic lab=vdg}
N 460 360 460 360 {lab=vdg}
C {devices/lab_pin.sym} 460 360 0 0 {name=p84 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 360 0 0 {name=xi2n
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 330 680 330 {lab=x_q2b}
C {devices/lab_pin.sym} 680 330 0 0 {name=p85 sig_type=std_logic lab=x_q2b}
N 640 360 640 360 {lab=x_q2}
C {devices/lab_pin.sym} 640 360 0 1 {name=p86 sig_type=std_logic lab=x_q2}
N 680 390 680 390 {lab=0}
C {devices/lab_pin.sym} 680 390 0 0 {name=p87 sig_type=std_logic lab=0}
N 680 360 680 360 {lab=0}
C {devices/lab_pin.sym} 680 360 0 0 {name=p88 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 360 0 0 {name=xg0pa
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 390 900 390 {lab=x_n0}
C {devices/lab_pin.sym} 900 390 0 0 {name=p89 sig_type=std_logic lab=x_n0}
N 860 360 860 360 {lab=x_q1}
C {devices/lab_pin.sym} 860 360 0 1 {name=p90 sig_type=std_logic lab=x_q1}
N 900 330 900 330 {lab=vdg}
C {devices/lab_pin.sym} 900 330 0 0 {name=p91 sig_type=std_logic lab=vdg}
N 900 360 900 360 {lab=vdg}
C {devices/lab_pin.sym} 900 360 0 0 {name=p92 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 360 0 0 {name=xg0pb
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 390 1120 390 {lab=x_n0}
C {devices/lab_pin.sym} 1120 390 0 0 {name=p93 sig_type=std_logic lab=x_n0}
N 1080 360 1080 360 {lab=x_q2b}
C {devices/lab_pin.sym} 1080 360 0 1 {name=p94 sig_type=std_logic lab=x_q2b}
N 1120 330 1120 330 {lab=vdg}
C {devices/lab_pin.sym} 1120 330 0 0 {name=p95 sig_type=std_logic lab=vdg}
N 1120 360 1120 360 {lab=vdg}
C {devices/lab_pin.sym} 1120 360 0 0 {name=p96 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 480 0 0 {name=xg0na
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 450 20 450 {lab=x_n0}
C {devices/lab_pin.sym} 20 450 0 0 {name=p97 sig_type=std_logic lab=x_n0}
N -20 480 -20 480 {lab=x_q1}
C {devices/lab_pin.sym} -20 480 0 1 {name=p98 sig_type=std_logic lab=x_q1}
N 20 510 20 510 {lab=x_g0m}
C {devices/lab_pin.sym} 20 510 0 0 {name=p99 sig_type=std_logic lab=x_g0m}
N 20 480 20 480 {lab=0}
C {devices/lab_pin.sym} 20 480 0 0 {name=p100 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 480 0 0 {name=xg0nb
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 450 240 450 {lab=x_g0m}
C {devices/lab_pin.sym} 240 450 0 0 {name=p101 sig_type=std_logic lab=x_g0m}
N 200 480 200 480 {lab=x_q2b}
C {devices/lab_pin.sym} 200 480 0 1 {name=p102 sig_type=std_logic lab=x_q2b}
N 240 510 240 510 {lab=0}
C {devices/lab_pin.sym} 240 510 0 0 {name=p103 sig_type=std_logic lab=0}
N 240 480 240 480 {lab=0}
C {devices/lab_pin.sym} 240 480 0 0 {name=p104 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 480 0 0 {name=xr0p1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 510 460 510 {lab=x_r0_x1}
C {devices/lab_pin.sym} 460 510 0 0 {name=p105 sig_type=std_logic lab=x_r0_x1}
N 420 480 420 480 {lab=x_n0}
C {devices/lab_pin.sym} 420 480 0 1 {name=p106 sig_type=std_logic lab=x_n0}
N 460 450 460 450 {lab=vdg}
C {devices/lab_pin.sym} 460 450 0 0 {name=p107 sig_type=std_logic lab=vdg}
N 460 480 460 480 {lab=vdg}
C {devices/lab_pin.sym} 460 480 0 0 {name=p108 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 480 0 0 {name=xr0p2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 510 680 510 {lab=x_r0_a}
C {devices/lab_pin.sym} 680 510 0 0 {name=p109 sig_type=std_logic lab=x_r0_a}
N 640 480 640 480 {lab=x_clk}
C {devices/lab_pin.sym} 640 480 0 1 {name=p110 sig_type=std_logic lab=x_clk}
N 680 450 680 450 {lab=x_r0_x1}
C {devices/lab_pin.sym} 680 450 0 0 {name=p111 sig_type=std_logic lab=x_r0_x1}
N 680 480 680 480 {lab=vdg}
C {devices/lab_pin.sym} 680 480 0 0 {name=p112 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 480 0 0 {name=xr0n1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 450 900 450 {lab=x_r0_a}
C {devices/lab_pin.sym} 900 450 0 0 {name=p113 sig_type=std_logic lab=x_r0_a}
N 860 480 860 480 {lab=x_n0}
C {devices/lab_pin.sym} 860 480 0 1 {name=p114 sig_type=std_logic lab=x_n0}
N 900 510 900 510 {lab=0}
C {devices/lab_pin.sym} 900 510 0 0 {name=p115 sig_type=std_logic lab=0}
N 900 480 900 480 {lab=0}
C {devices/lab_pin.sym} 900 480 0 0 {name=p116 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 480 0 0 {name=xr0p3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 510 1120 510 {lab=x_r0_b}
C {devices/lab_pin.sym} 1120 510 0 0 {name=p117 sig_type=std_logic lab=x_r0_b}
N 1080 480 1080 480 {lab=x_clk}
C {devices/lab_pin.sym} 1080 480 0 1 {name=p118 sig_type=std_logic lab=x_clk}
N 1120 450 1120 450 {lab=vdg}
C {devices/lab_pin.sym} 1120 450 0 0 {name=p119 sig_type=std_logic lab=vdg}
N 1120 480 1120 480 {lab=vdg}
C {devices/lab_pin.sym} 1120 480 0 0 {name=p120 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 600 0 0 {name=xr0n2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 570 20 570 {lab=x_r0_b}
C {devices/lab_pin.sym} 20 570 0 0 {name=p121 sig_type=std_logic lab=x_r0_b}
N -20 600 -20 600 {lab=x_r0_a}
C {devices/lab_pin.sym} -20 600 0 1 {name=p122 sig_type=std_logic lab=x_r0_a}
N 20 630 20 630 {lab=x_r0_x2}
C {devices/lab_pin.sym} 20 630 0 0 {name=p123 sig_type=std_logic lab=x_r0_x2}
N 20 600 20 600 {lab=0}
C {devices/lab_pin.sym} 20 600 0 0 {name=p124 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 600 0 0 {name=xr0n3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 570 240 570 {lab=x_r0_x2}
C {devices/lab_pin.sym} 240 570 0 0 {name=p125 sig_type=std_logic lab=x_r0_x2}
N 200 600 200 600 {lab=x_clk}
C {devices/lab_pin.sym} 200 600 0 1 {name=p126 sig_type=std_logic lab=x_clk}
N 240 630 240 630 {lab=0}
C {devices/lab_pin.sym} 240 630 0 0 {name=p127 sig_type=std_logic lab=0}
N 240 600 240 600 {lab=0}
C {devices/lab_pin.sym} 240 600 0 0 {name=p128 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 600 0 0 {name=xr0p4
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 630 460 630 {lab=x_p0}
C {devices/lab_pin.sym} 460 630 0 0 {name=p129 sig_type=std_logic lab=x_p0}
N 420 600 420 600 {lab=x_r0_b}
C {devices/lab_pin.sym} 420 600 0 1 {name=p130 sig_type=std_logic lab=x_r0_b}
N 460 570 460 570 {lab=vdg}
C {devices/lab_pin.sym} 460 570 0 0 {name=p131 sig_type=std_logic lab=vdg}
N 460 600 460 600 {lab=vdg}
C {devices/lab_pin.sym} 460 600 0 0 {name=p132 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 600 0 0 {name=xr0n4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 570 680 570 {lab=x_p0}
C {devices/lab_pin.sym} 680 570 0 0 {name=p133 sig_type=std_logic lab=x_p0}
N 640 600 640 600 {lab=x_clk}
C {devices/lab_pin.sym} 640 600 0 1 {name=p134 sig_type=std_logic lab=x_clk}
N 680 630 680 630 {lab=x_r0_x3}
C {devices/lab_pin.sym} 680 630 0 0 {name=p135 sig_type=std_logic lab=x_r0_x3}
N 680 600 680 600 {lab=0}
C {devices/lab_pin.sym} 680 600 0 0 {name=p136 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 600 0 0 {name=xr0n5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 570 900 570 {lab=x_r0_x3}
C {devices/lab_pin.sym} 900 570 0 0 {name=p137 sig_type=std_logic lab=x_r0_x3}
N 860 600 860 600 {lab=x_r0_b}
C {devices/lab_pin.sym} 860 600 0 1 {name=p138 sig_type=std_logic lab=x_r0_b}
N 900 630 900 630 {lab=0}
C {devices/lab_pin.sym} 900 630 0 0 {name=p139 sig_type=std_logic lab=0}
N 900 600 900 600 {lab=0}
C {devices/lab_pin.sym} 900 600 0 0 {name=p140 sig_type=std_logic lab=0}
C {devices/capa.sym} 1100 600 0 0 {name=cpl0
value=20f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 1100 570 1100 570 {lab=x_p0}
C {devices/lab_pin.sym} 1100 570 0 0 {name=p141 sig_type=std_logic lab=x_p0}
N 1100 630 1100 630 {lab=0}
C {devices/lab_pin.sym} 1100 630 0 0 {name=p142 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 720 0 0 {name=xg1pa
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 750 20 750 {lab=x_n1}
C {devices/lab_pin.sym} 20 750 0 0 {name=p143 sig_type=std_logic lab=x_n1}
N -20 720 -20 720 {lab=x_q1}
C {devices/lab_pin.sym} -20 720 0 1 {name=p144 sig_type=std_logic lab=x_q1}
N 20 690 20 690 {lab=vdg}
C {devices/lab_pin.sym} 20 690 0 0 {name=p145 sig_type=std_logic lab=vdg}
N 20 720 20 720 {lab=vdg}
C {devices/lab_pin.sym} 20 720 0 0 {name=p146 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 720 0 0 {name=xg1pb
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 750 240 750 {lab=x_n1}
C {devices/lab_pin.sym} 240 750 0 0 {name=p147 sig_type=std_logic lab=x_n1}
N 200 720 200 720 {lab=x_q2}
C {devices/lab_pin.sym} 200 720 0 1 {name=p148 sig_type=std_logic lab=x_q2}
N 240 690 240 690 {lab=vdg}
C {devices/lab_pin.sym} 240 690 0 0 {name=p149 sig_type=std_logic lab=vdg}
N 240 720 240 720 {lab=vdg}
C {devices/lab_pin.sym} 240 720 0 0 {name=p150 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 720 0 0 {name=xg1na
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 690 460 690 {lab=x_n1}
C {devices/lab_pin.sym} 460 690 0 0 {name=p151 sig_type=std_logic lab=x_n1}
N 420 720 420 720 {lab=x_q1}
C {devices/lab_pin.sym} 420 720 0 1 {name=p152 sig_type=std_logic lab=x_q1}
N 460 750 460 750 {lab=x_g1m}
C {devices/lab_pin.sym} 460 750 0 0 {name=p153 sig_type=std_logic lab=x_g1m}
N 460 720 460 720 {lab=0}
C {devices/lab_pin.sym} 460 720 0 0 {name=p154 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 720 0 0 {name=xg1nb
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 690 680 690 {lab=x_g1m}
C {devices/lab_pin.sym} 680 690 0 0 {name=p155 sig_type=std_logic lab=x_g1m}
N 640 720 640 720 {lab=x_q2}
C {devices/lab_pin.sym} 640 720 0 1 {name=p156 sig_type=std_logic lab=x_q2}
N 680 750 680 750 {lab=0}
C {devices/lab_pin.sym} 680 750 0 0 {name=p157 sig_type=std_logic lab=0}
N 680 720 680 720 {lab=0}
C {devices/lab_pin.sym} 680 720 0 0 {name=p158 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 720 0 0 {name=xr1p1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 750 900 750 {lab=x_r1_x1}
C {devices/lab_pin.sym} 900 750 0 0 {name=p159 sig_type=std_logic lab=x_r1_x1}
N 860 720 860 720 {lab=x_n1}
C {devices/lab_pin.sym} 860 720 0 1 {name=p160 sig_type=std_logic lab=x_n1}
N 900 690 900 690 {lab=vdg}
C {devices/lab_pin.sym} 900 690 0 0 {name=p161 sig_type=std_logic lab=vdg}
N 900 720 900 720 {lab=vdg}
C {devices/lab_pin.sym} 900 720 0 0 {name=p162 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 720 0 0 {name=xr1p2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 750 1120 750 {lab=x_r1_a}
C {devices/lab_pin.sym} 1120 750 0 0 {name=p163 sig_type=std_logic lab=x_r1_a}
N 1080 720 1080 720 {lab=x_clk}
C {devices/lab_pin.sym} 1080 720 0 1 {name=p164 sig_type=std_logic lab=x_clk}
N 1120 690 1120 690 {lab=x_r1_x1}
C {devices/lab_pin.sym} 1120 690 0 0 {name=p165 sig_type=std_logic lab=x_r1_x1}
N 1120 720 1120 720 {lab=vdg}
C {devices/lab_pin.sym} 1120 720 0 0 {name=p166 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 840 0 0 {name=xr1n1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 810 20 810 {lab=x_r1_a}
C {devices/lab_pin.sym} 20 810 0 0 {name=p167 sig_type=std_logic lab=x_r1_a}
N -20 840 -20 840 {lab=x_n1}
C {devices/lab_pin.sym} -20 840 0 1 {name=p168 sig_type=std_logic lab=x_n1}
N 20 870 20 870 {lab=0}
C {devices/lab_pin.sym} 20 870 0 0 {name=p169 sig_type=std_logic lab=0}
N 20 840 20 840 {lab=0}
C {devices/lab_pin.sym} 20 840 0 0 {name=p170 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 840 0 0 {name=xr1p3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 870 240 870 {lab=x_r1_b}
C {devices/lab_pin.sym} 240 870 0 0 {name=p171 sig_type=std_logic lab=x_r1_b}
N 200 840 200 840 {lab=x_clk}
C {devices/lab_pin.sym} 200 840 0 1 {name=p172 sig_type=std_logic lab=x_clk}
N 240 810 240 810 {lab=vdg}
C {devices/lab_pin.sym} 240 810 0 0 {name=p173 sig_type=std_logic lab=vdg}
N 240 840 240 840 {lab=vdg}
C {devices/lab_pin.sym} 240 840 0 0 {name=p174 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 840 0 0 {name=xr1n2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 810 460 810 {lab=x_r1_b}
C {devices/lab_pin.sym} 460 810 0 0 {name=p175 sig_type=std_logic lab=x_r1_b}
N 420 840 420 840 {lab=x_r1_a}
C {devices/lab_pin.sym} 420 840 0 1 {name=p176 sig_type=std_logic lab=x_r1_a}
N 460 870 460 870 {lab=x_r1_x2}
C {devices/lab_pin.sym} 460 870 0 0 {name=p177 sig_type=std_logic lab=x_r1_x2}
N 460 840 460 840 {lab=0}
C {devices/lab_pin.sym} 460 840 0 0 {name=p178 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 840 0 0 {name=xr1n3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 810 680 810 {lab=x_r1_x2}
C {devices/lab_pin.sym} 680 810 0 0 {name=p179 sig_type=std_logic lab=x_r1_x2}
N 640 840 640 840 {lab=x_clk}
C {devices/lab_pin.sym} 640 840 0 1 {name=p180 sig_type=std_logic lab=x_clk}
N 680 870 680 870 {lab=0}
C {devices/lab_pin.sym} 680 870 0 0 {name=p181 sig_type=std_logic lab=0}
N 680 840 680 840 {lab=0}
C {devices/lab_pin.sym} 680 840 0 0 {name=p182 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 840 0 0 {name=xr1p4
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 870 900 870 {lab=x_p1}
C {devices/lab_pin.sym} 900 870 0 0 {name=p183 sig_type=std_logic lab=x_p1}
N 860 840 860 840 {lab=x_r1_b}
C {devices/lab_pin.sym} 860 840 0 1 {name=p184 sig_type=std_logic lab=x_r1_b}
N 900 810 900 810 {lab=vdg}
C {devices/lab_pin.sym} 900 810 0 0 {name=p185 sig_type=std_logic lab=vdg}
N 900 840 900 840 {lab=vdg}
C {devices/lab_pin.sym} 900 840 0 0 {name=p186 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 840 0 0 {name=xr1n4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 810 1120 810 {lab=x_p1}
C {devices/lab_pin.sym} 1120 810 0 0 {name=p187 sig_type=std_logic lab=x_p1}
N 1080 840 1080 840 {lab=x_clk}
C {devices/lab_pin.sym} 1080 840 0 1 {name=p188 sig_type=std_logic lab=x_clk}
N 1120 870 1120 870 {lab=x_r1_x3}
C {devices/lab_pin.sym} 1120 870 0 0 {name=p189 sig_type=std_logic lab=x_r1_x3}
N 1120 840 1120 840 {lab=0}
C {devices/lab_pin.sym} 1120 840 0 0 {name=p190 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 960 0 0 {name=xr1n5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 930 20 930 {lab=x_r1_x3}
C {devices/lab_pin.sym} 20 930 0 0 {name=p191 sig_type=std_logic lab=x_r1_x3}
N -20 960 -20 960 {lab=x_r1_b}
C {devices/lab_pin.sym} -20 960 0 1 {name=p192 sig_type=std_logic lab=x_r1_b}
N 20 990 20 990 {lab=0}
C {devices/lab_pin.sym} 20 990 0 0 {name=p193 sig_type=std_logic lab=0}
N 20 960 20 960 {lab=0}
C {devices/lab_pin.sym} 20 960 0 0 {name=p194 sig_type=std_logic lab=0}
C {devices/capa.sym} 220 960 0 0 {name=cpl1
value=20f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 220 930 220 930 {lab=x_p1}
C {devices/lab_pin.sym} 220 930 0 0 {name=p195 sig_type=std_logic lab=x_p1}
N 220 990 220 990 {lab=0}
C {devices/lab_pin.sym} 220 990 0 0 {name=p196 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 960 0 0 {name=xg2pa
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 990 460 990 {lab=x_n2}
C {devices/lab_pin.sym} 460 990 0 0 {name=p197 sig_type=std_logic lab=x_n2}
N 420 960 420 960 {lab=x_q1b}
C {devices/lab_pin.sym} 420 960 0 1 {name=p198 sig_type=std_logic lab=x_q1b}
N 460 930 460 930 {lab=vdg}
C {devices/lab_pin.sym} 460 930 0 0 {name=p199 sig_type=std_logic lab=vdg}
N 460 960 460 960 {lab=vdg}
C {devices/lab_pin.sym} 460 960 0 0 {name=p200 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 960 0 0 {name=xg2pb
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 990 680 990 {lab=x_n2}
C {devices/lab_pin.sym} 680 990 0 0 {name=p201 sig_type=std_logic lab=x_n2}
N 640 960 640 960 {lab=x_q2}
C {devices/lab_pin.sym} 640 960 0 1 {name=p202 sig_type=std_logic lab=x_q2}
N 680 930 680 930 {lab=vdg}
C {devices/lab_pin.sym} 680 930 0 0 {name=p203 sig_type=std_logic lab=vdg}
N 680 960 680 960 {lab=vdg}
C {devices/lab_pin.sym} 680 960 0 0 {name=p204 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 960 0 0 {name=xg2na
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 930 900 930 {lab=x_n2}
C {devices/lab_pin.sym} 900 930 0 0 {name=p205 sig_type=std_logic lab=x_n2}
N 860 960 860 960 {lab=x_q1b}
C {devices/lab_pin.sym} 860 960 0 1 {name=p206 sig_type=std_logic lab=x_q1b}
N 900 990 900 990 {lab=x_g2m}
C {devices/lab_pin.sym} 900 990 0 0 {name=p207 sig_type=std_logic lab=x_g2m}
N 900 960 900 960 {lab=0}
C {devices/lab_pin.sym} 900 960 0 0 {name=p208 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 960 0 0 {name=xg2nb
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 930 1120 930 {lab=x_g2m}
C {devices/lab_pin.sym} 1120 930 0 0 {name=p209 sig_type=std_logic lab=x_g2m}
N 1080 960 1080 960 {lab=x_q2}
C {devices/lab_pin.sym} 1080 960 0 1 {name=p210 sig_type=std_logic lab=x_q2}
N 1120 990 1120 990 {lab=0}
C {devices/lab_pin.sym} 1120 990 0 0 {name=p211 sig_type=std_logic lab=0}
N 1120 960 1120 960 {lab=0}
C {devices/lab_pin.sym} 1120 960 0 0 {name=p212 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 1080 0 0 {name=xr2p1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 1110 20 1110 {lab=x_r2_x1}
C {devices/lab_pin.sym} 20 1110 0 0 {name=p213 sig_type=std_logic lab=x_r2_x1}
N -20 1080 -20 1080 {lab=x_n2}
C {devices/lab_pin.sym} -20 1080 0 1 {name=p214 sig_type=std_logic lab=x_n2}
N 20 1050 20 1050 {lab=vdg}
C {devices/lab_pin.sym} 20 1050 0 0 {name=p215 sig_type=std_logic lab=vdg}
N 20 1080 20 1080 {lab=vdg}
C {devices/lab_pin.sym} 20 1080 0 0 {name=p216 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 1080 0 0 {name=xr2p2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 1110 240 1110 {lab=x_r2_a}
C {devices/lab_pin.sym} 240 1110 0 0 {name=p217 sig_type=std_logic lab=x_r2_a}
N 200 1080 200 1080 {lab=x_clk}
C {devices/lab_pin.sym} 200 1080 0 1 {name=p218 sig_type=std_logic lab=x_clk}
N 240 1050 240 1050 {lab=x_r2_x1}
C {devices/lab_pin.sym} 240 1050 0 0 {name=p219 sig_type=std_logic lab=x_r2_x1}
N 240 1080 240 1080 {lab=vdg}
C {devices/lab_pin.sym} 240 1080 0 0 {name=p220 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 1080 0 0 {name=xr2n1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 1050 460 1050 {lab=x_r2_a}
C {devices/lab_pin.sym} 460 1050 0 0 {name=p221 sig_type=std_logic lab=x_r2_a}
N 420 1080 420 1080 {lab=x_n2}
C {devices/lab_pin.sym} 420 1080 0 1 {name=p222 sig_type=std_logic lab=x_n2}
N 460 1110 460 1110 {lab=0}
C {devices/lab_pin.sym} 460 1110 0 0 {name=p223 sig_type=std_logic lab=0}
N 460 1080 460 1080 {lab=0}
C {devices/lab_pin.sym} 460 1080 0 0 {name=p224 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 1080 0 0 {name=xr2p3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 1110 680 1110 {lab=x_r2_b}
C {devices/lab_pin.sym} 680 1110 0 0 {name=p225 sig_type=std_logic lab=x_r2_b}
N 640 1080 640 1080 {lab=x_clk}
C {devices/lab_pin.sym} 640 1080 0 1 {name=p226 sig_type=std_logic lab=x_clk}
N 680 1050 680 1050 {lab=vdg}
C {devices/lab_pin.sym} 680 1050 0 0 {name=p227 sig_type=std_logic lab=vdg}
N 680 1080 680 1080 {lab=vdg}
C {devices/lab_pin.sym} 680 1080 0 0 {name=p228 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 1080 0 0 {name=xr2n2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 1050 900 1050 {lab=x_r2_b}
C {devices/lab_pin.sym} 900 1050 0 0 {name=p229 sig_type=std_logic lab=x_r2_b}
N 860 1080 860 1080 {lab=x_r2_a}
C {devices/lab_pin.sym} 860 1080 0 1 {name=p230 sig_type=std_logic lab=x_r2_a}
N 900 1110 900 1110 {lab=x_r2_x2}
C {devices/lab_pin.sym} 900 1110 0 0 {name=p231 sig_type=std_logic lab=x_r2_x2}
N 900 1080 900 1080 {lab=0}
C {devices/lab_pin.sym} 900 1080 0 0 {name=p232 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 1080 0 0 {name=xr2n3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 1050 1120 1050 {lab=x_r2_x2}
C {devices/lab_pin.sym} 1120 1050 0 0 {name=p233 sig_type=std_logic lab=x_r2_x2}
N 1080 1080 1080 1080 {lab=x_clk}
C {devices/lab_pin.sym} 1080 1080 0 1 {name=p234 sig_type=std_logic lab=x_clk}
N 1120 1110 1120 1110 {lab=0}
C {devices/lab_pin.sym} 1120 1110 0 0 {name=p235 sig_type=std_logic lab=0}
N 1120 1080 1120 1080 {lab=0}
C {devices/lab_pin.sym} 1120 1080 0 0 {name=p236 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 1200 0 0 {name=xr2p4
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 1230 20 1230 {lab=x_p2}
C {devices/lab_pin.sym} 20 1230 0 0 {name=p237 sig_type=std_logic lab=x_p2}
N -20 1200 -20 1200 {lab=x_r2_b}
C {devices/lab_pin.sym} -20 1200 0 1 {name=p238 sig_type=std_logic lab=x_r2_b}
N 20 1170 20 1170 {lab=vdg}
C {devices/lab_pin.sym} 20 1170 0 0 {name=p239 sig_type=std_logic lab=vdg}
N 20 1200 20 1200 {lab=vdg}
C {devices/lab_pin.sym} 20 1200 0 0 {name=p240 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 1200 0 0 {name=xr2n4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 1170 240 1170 {lab=x_p2}
C {devices/lab_pin.sym} 240 1170 0 0 {name=p241 sig_type=std_logic lab=x_p2}
N 200 1200 200 1200 {lab=x_clk}
C {devices/lab_pin.sym} 200 1200 0 1 {name=p242 sig_type=std_logic lab=x_clk}
N 240 1230 240 1230 {lab=x_r2_x3}
C {devices/lab_pin.sym} 240 1230 0 0 {name=p243 sig_type=std_logic lab=x_r2_x3}
N 240 1200 240 1200 {lab=0}
C {devices/lab_pin.sym} 240 1200 0 0 {name=p244 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 1200 0 0 {name=xr2n5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 1170 460 1170 {lab=x_r2_x3}
C {devices/lab_pin.sym} 460 1170 0 0 {name=p245 sig_type=std_logic lab=x_r2_x3}
N 420 1200 420 1200 {lab=x_r2_b}
C {devices/lab_pin.sym} 420 1200 0 1 {name=p246 sig_type=std_logic lab=x_r2_b}
N 460 1230 460 1230 {lab=0}
C {devices/lab_pin.sym} 460 1230 0 0 {name=p247 sig_type=std_logic lab=0}
N 460 1200 460 1200 {lab=0}
C {devices/lab_pin.sym} 460 1200 0 0 {name=p248 sig_type=std_logic lab=0}
C {devices/capa.sym} 660 1200 0 0 {name=cpl2
value=20f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 660 1170 660 1170 {lab=x_p2}
C {devices/lab_pin.sym} 660 1170 0 0 {name=p249 sig_type=std_logic lab=x_p2}
N 660 1230 660 1230 {lab=0}
C {devices/lab_pin.sym} 660 1230 0 0 {name=p250 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 1200 0 0 {name=xg3pa
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 1230 900 1230 {lab=x_n3}
C {devices/lab_pin.sym} 900 1230 0 0 {name=p251 sig_type=std_logic lab=x_n3}
N 860 1200 860 1200 {lab=x_q1b}
C {devices/lab_pin.sym} 860 1200 0 1 {name=p252 sig_type=std_logic lab=x_q1b}
N 900 1170 900 1170 {lab=vdg}
C {devices/lab_pin.sym} 900 1170 0 0 {name=p253 sig_type=std_logic lab=vdg}
N 900 1200 900 1200 {lab=vdg}
C {devices/lab_pin.sym} 900 1200 0 0 {name=p254 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 1200 0 0 {name=xg3pb
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 1230 1120 1230 {lab=x_n3}
C {devices/lab_pin.sym} 1120 1230 0 0 {name=p255 sig_type=std_logic lab=x_n3}
N 1080 1200 1080 1200 {lab=x_q2b}
C {devices/lab_pin.sym} 1080 1200 0 1 {name=p256 sig_type=std_logic lab=x_q2b}
N 1120 1170 1120 1170 {lab=vdg}
C {devices/lab_pin.sym} 1120 1170 0 0 {name=p257 sig_type=std_logic lab=vdg}
N 1120 1200 1120 1200 {lab=vdg}
C {devices/lab_pin.sym} 1120 1200 0 0 {name=p258 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 1320 0 0 {name=xg3na
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 1290 20 1290 {lab=x_n3}
C {devices/lab_pin.sym} 20 1290 0 0 {name=p259 sig_type=std_logic lab=x_n3}
N -20 1320 -20 1320 {lab=x_q1b}
C {devices/lab_pin.sym} -20 1320 0 1 {name=p260 sig_type=std_logic lab=x_q1b}
N 20 1350 20 1350 {lab=x_g3m}
C {devices/lab_pin.sym} 20 1350 0 0 {name=p261 sig_type=std_logic lab=x_g3m}
N 20 1320 20 1320 {lab=0}
C {devices/lab_pin.sym} 20 1320 0 0 {name=p262 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 1320 0 0 {name=xg3nb
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 1290 240 1290 {lab=x_g3m}
C {devices/lab_pin.sym} 240 1290 0 0 {name=p263 sig_type=std_logic lab=x_g3m}
N 200 1320 200 1320 {lab=x_q2b}
C {devices/lab_pin.sym} 200 1320 0 1 {name=p264 sig_type=std_logic lab=x_q2b}
N 240 1350 240 1350 {lab=0}
C {devices/lab_pin.sym} 240 1350 0 0 {name=p265 sig_type=std_logic lab=0}
N 240 1320 240 1320 {lab=0}
C {devices/lab_pin.sym} 240 1320 0 0 {name=p266 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 1320 0 0 {name=xr3p1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 1350 460 1350 {lab=x_r3_x1}
C {devices/lab_pin.sym} 460 1350 0 0 {name=p267 sig_type=std_logic lab=x_r3_x1}
N 420 1320 420 1320 {lab=x_n3}
C {devices/lab_pin.sym} 420 1320 0 1 {name=p268 sig_type=std_logic lab=x_n3}
N 460 1290 460 1290 {lab=vdg}
C {devices/lab_pin.sym} 460 1290 0 0 {name=p269 sig_type=std_logic lab=vdg}
N 460 1320 460 1320 {lab=vdg}
C {devices/lab_pin.sym} 460 1320 0 0 {name=p270 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 1320 0 0 {name=xr3p2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 1350 680 1350 {lab=x_r3_a}
C {devices/lab_pin.sym} 680 1350 0 0 {name=p271 sig_type=std_logic lab=x_r3_a}
N 640 1320 640 1320 {lab=x_clk}
C {devices/lab_pin.sym} 640 1320 0 1 {name=p272 sig_type=std_logic lab=x_clk}
N 680 1290 680 1290 {lab=x_r3_x1}
C {devices/lab_pin.sym} 680 1290 0 0 {name=p273 sig_type=std_logic lab=x_r3_x1}
N 680 1320 680 1320 {lab=vdg}
C {devices/lab_pin.sym} 680 1320 0 0 {name=p274 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 1320 0 0 {name=xr3n1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 1290 900 1290 {lab=x_r3_a}
C {devices/lab_pin.sym} 900 1290 0 0 {name=p275 sig_type=std_logic lab=x_r3_a}
N 860 1320 860 1320 {lab=x_n3}
C {devices/lab_pin.sym} 860 1320 0 1 {name=p276 sig_type=std_logic lab=x_n3}
N 900 1350 900 1350 {lab=0}
C {devices/lab_pin.sym} 900 1350 0 0 {name=p277 sig_type=std_logic lab=0}
N 900 1320 900 1320 {lab=0}
C {devices/lab_pin.sym} 900 1320 0 0 {name=p278 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 1320 0 0 {name=xr3p3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 1350 1120 1350 {lab=x_r3_b}
C {devices/lab_pin.sym} 1120 1350 0 0 {name=p279 sig_type=std_logic lab=x_r3_b}
N 1080 1320 1080 1320 {lab=x_clk}
C {devices/lab_pin.sym} 1080 1320 0 1 {name=p280 sig_type=std_logic lab=x_clk}
N 1120 1290 1120 1290 {lab=vdg}
C {devices/lab_pin.sym} 1120 1290 0 0 {name=p281 sig_type=std_logic lab=vdg}
N 1120 1320 1120 1320 {lab=vdg}
C {devices/lab_pin.sym} 1120 1320 0 0 {name=p282 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 1440 0 0 {name=xr3n2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 1410 20 1410 {lab=x_r3_b}
C {devices/lab_pin.sym} 20 1410 0 0 {name=p283 sig_type=std_logic lab=x_r3_b}
N -20 1440 -20 1440 {lab=x_r3_a}
C {devices/lab_pin.sym} -20 1440 0 1 {name=p284 sig_type=std_logic lab=x_r3_a}
N 20 1470 20 1470 {lab=x_r3_x2}
C {devices/lab_pin.sym} 20 1470 0 0 {name=p285 sig_type=std_logic lab=x_r3_x2}
N 20 1440 20 1440 {lab=0}
C {devices/lab_pin.sym} 20 1440 0 0 {name=p286 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 1440 0 0 {name=xr3n3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 1410 240 1410 {lab=x_r3_x2}
C {devices/lab_pin.sym} 240 1410 0 0 {name=p287 sig_type=std_logic lab=x_r3_x2}
N 200 1440 200 1440 {lab=x_clk}
C {devices/lab_pin.sym} 200 1440 0 1 {name=p288 sig_type=std_logic lab=x_clk}
N 240 1470 240 1470 {lab=0}
C {devices/lab_pin.sym} 240 1470 0 0 {name=p289 sig_type=std_logic lab=0}
N 240 1440 240 1440 {lab=0}
C {devices/lab_pin.sym} 240 1440 0 0 {name=p290 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 1440 0 0 {name=xr3p4
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 1470 460 1470 {lab=x_p3}
C {devices/lab_pin.sym} 460 1470 0 0 {name=p291 sig_type=std_logic lab=x_p3}
N 420 1440 420 1440 {lab=x_r3_b}
C {devices/lab_pin.sym} 420 1440 0 1 {name=p292 sig_type=std_logic lab=x_r3_b}
N 460 1410 460 1410 {lab=vdg}
C {devices/lab_pin.sym} 460 1410 0 0 {name=p293 sig_type=std_logic lab=vdg}
N 460 1440 460 1440 {lab=vdg}
C {devices/lab_pin.sym} 460 1440 0 0 {name=p294 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 1440 0 0 {name=xr3n4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 1410 680 1410 {lab=x_p3}
C {devices/lab_pin.sym} 680 1410 0 0 {name=p295 sig_type=std_logic lab=x_p3}
N 640 1440 640 1440 {lab=x_clk}
C {devices/lab_pin.sym} 640 1440 0 1 {name=p296 sig_type=std_logic lab=x_clk}
N 680 1470 680 1470 {lab=x_r3_x3}
C {devices/lab_pin.sym} 680 1470 0 0 {name=p297 sig_type=std_logic lab=x_r3_x3}
N 680 1440 680 1440 {lab=0}
C {devices/lab_pin.sym} 680 1440 0 0 {name=p298 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 1440 0 0 {name=xr3n5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 1410 900 1410 {lab=x_r3_x3}
C {devices/lab_pin.sym} 900 1410 0 0 {name=p299 sig_type=std_logic lab=x_r3_x3}
N 860 1440 860 1440 {lab=x_r3_b}
C {devices/lab_pin.sym} 860 1440 0 1 {name=p300 sig_type=std_logic lab=x_r3_b}
N 900 1470 900 1470 {lab=0}
C {devices/lab_pin.sym} 900 1470 0 0 {name=p301 sig_type=std_logic lab=0}
N 900 1440 900 1440 {lab=0}
C {devices/lab_pin.sym} 900 1440 0 0 {name=p302 sig_type=std_logic lab=0}
C {devices/capa.sym} 1100 1440 0 0 {name=cpl3
value=20f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 1100 1410 1100 1410 {lab=x_p3}
C {devices/lab_pin.sym} 1100 1410 0 0 {name=p303 sig_type=std_logic lab=x_p3}
N 1100 1470 1100 1470 {lab=0}
C {devices/lab_pin.sym} 1100 1470 0 0 {name=p304 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 1560 0 0 {name=xf1kq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 1590 20 1590 {lab=x_f1_kq}
C {devices/lab_pin.sym} 20 1590 0 0 {name=p305 sig_type=std_logic lab=x_f1_kq}
N -20 1560 -20 1560 {lab=x_q1}
C {devices/lab_pin.sym} -20 1560 0 1 {name=p306 sig_type=std_logic lab=x_q1}
N 20 1530 20 1530 {lab=vdg}
C {devices/lab_pin.sym} 20 1530 0 0 {name=p307 sig_type=std_logic lab=vdg}
N 20 1560 20 1560 {lab=vdg}
C {devices/lab_pin.sym} 20 1560 0 0 {name=p308 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 1560 0 0 {name=xf1kq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 1530 240 1530 {lab=x_f1_kq}
C {devices/lab_pin.sym} 240 1530 0 0 {name=p309 sig_type=std_logic lab=x_f1_kq}
N 200 1560 200 1560 {lab=x_q1}
C {devices/lab_pin.sym} 200 1560 0 1 {name=p310 sig_type=std_logic lab=x_q1}
N 240 1590 240 1590 {lab=0}
C {devices/lab_pin.sym} 240 1590 0 0 {name=p311 sig_type=std_logic lab=0}
N 240 1560 240 1560 {lab=0}
C {devices/lab_pin.sym} 240 1560 0 0 {name=p312 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 1560 0 0 {name=xf1kq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 1590 460 1590 {lab=x_q1}
C {devices/lab_pin.sym} 460 1590 0 0 {name=p313 sig_type=std_logic lab=x_q1}
N 420 1560 420 1560 {lab=x_f1_kq}
C {devices/lab_pin.sym} 420 1560 0 1 {name=p314 sig_type=std_logic lab=x_f1_kq}
N 460 1530 460 1530 {lab=vdg}
C {devices/lab_pin.sym} 460 1530 0 0 {name=p315 sig_type=std_logic lab=vdg}
N 460 1560 460 1560 {lab=vdg}
C {devices/lab_pin.sym} 460 1560 0 0 {name=p316 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 1560 0 0 {name=xf1kq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 1530 680 1530 {lab=x_q1}
C {devices/lab_pin.sym} 680 1530 0 0 {name=p317 sig_type=std_logic lab=x_q1}
N 640 1560 640 1560 {lab=x_f1_kq}
C {devices/lab_pin.sym} 640 1560 0 1 {name=p318 sig_type=std_logic lab=x_f1_kq}
N 680 1590 680 1590 {lab=0}
C {devices/lab_pin.sym} 680 1590 0 0 {name=p319 sig_type=std_logic lab=0}
N 680 1560 680 1560 {lab=0}
C {devices/lab_pin.sym} 680 1560 0 0 {name=p320 sig_type=std_logic lab=0}
C {devices/res.sym} 880 1560 0 0 {name=rkf11
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 1530 880 1530 {lab=x_f1_a}
C {devices/lab_pin.sym} 880 1530 0 0 {name=p321 sig_type=std_logic lab=x_f1_a}
N 880 1590 880 1590 {lab=0}
C {devices/lab_pin.sym} 880 1590 0 0 {name=p322 sig_type=std_logic lab=0}
C {devices/res.sym} 1100 1560 0 0 {name=rkf12
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 1100 1530 1100 1530 {lab=x_f1_b}
C {devices/lab_pin.sym} 1100 1530 0 0 {name=p323 sig_type=std_logic lab=x_f1_b}
N 1100 1590 1100 1590 {lab=0}
C {devices/lab_pin.sym} 1100 1590 0 0 {name=p324 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 1680 0 0 {name=xf2kq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 1710 20 1710 {lab=x_f2_kq}
C {devices/lab_pin.sym} 20 1710 0 0 {name=p325 sig_type=std_logic lab=x_f2_kq}
N -20 1680 -20 1680 {lab=x_q2}
C {devices/lab_pin.sym} -20 1680 0 1 {name=p326 sig_type=std_logic lab=x_q2}
N 20 1650 20 1650 {lab=vdg}
C {devices/lab_pin.sym} 20 1650 0 0 {name=p327 sig_type=std_logic lab=vdg}
N 20 1680 20 1680 {lab=vdg}
C {devices/lab_pin.sym} 20 1680 0 0 {name=p328 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 1680 0 0 {name=xf2kq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 1650 240 1650 {lab=x_f2_kq}
C {devices/lab_pin.sym} 240 1650 0 0 {name=p329 sig_type=std_logic lab=x_f2_kq}
N 200 1680 200 1680 {lab=x_q2}
C {devices/lab_pin.sym} 200 1680 0 1 {name=p330 sig_type=std_logic lab=x_q2}
N 240 1710 240 1710 {lab=0}
C {devices/lab_pin.sym} 240 1710 0 0 {name=p331 sig_type=std_logic lab=0}
N 240 1680 240 1680 {lab=0}
C {devices/lab_pin.sym} 240 1680 0 0 {name=p332 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 1680 0 0 {name=xf2kq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 1710 460 1710 {lab=x_q2}
C {devices/lab_pin.sym} 460 1710 0 0 {name=p333 sig_type=std_logic lab=x_q2}
N 420 1680 420 1680 {lab=x_f2_kq}
C {devices/lab_pin.sym} 420 1680 0 1 {name=p334 sig_type=std_logic lab=x_f2_kq}
N 460 1650 460 1650 {lab=vdg}
C {devices/lab_pin.sym} 460 1650 0 0 {name=p335 sig_type=std_logic lab=vdg}
N 460 1680 460 1680 {lab=vdg}
C {devices/lab_pin.sym} 460 1680 0 0 {name=p336 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 1680 0 0 {name=xf2kq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 1650 680 1650 {lab=x_q2}
C {devices/lab_pin.sym} 680 1650 0 0 {name=p337 sig_type=std_logic lab=x_q2}
N 640 1680 640 1680 {lab=x_f2_kq}
C {devices/lab_pin.sym} 640 1680 0 1 {name=p338 sig_type=std_logic lab=x_f2_kq}
N 680 1710 680 1710 {lab=0}
C {devices/lab_pin.sym} 680 1710 0 0 {name=p339 sig_type=std_logic lab=0}
N 680 1680 680 1680 {lab=0}
C {devices/lab_pin.sym} 680 1680 0 0 {name=p340 sig_type=std_logic lab=0}
C {devices/res.sym} 880 1680 0 0 {name=rkf21
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 1650 880 1650 {lab=x_f2_a}
C {devices/lab_pin.sym} 880 1650 0 0 {name=p341 sig_type=std_logic lab=x_f2_a}
N 880 1710 880 1710 {lab=0}
C {devices/lab_pin.sym} 880 1710 0 0 {name=p342 sig_type=std_logic lab=0}
C {devices/res.sym} 1100 1680 0 0 {name=rkf22
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 1100 1650 1100 1650 {lab=x_f2_b}
C {devices/lab_pin.sym} 1100 1650 0 0 {name=p343 sig_type=std_logic lab=x_f2_b}
N 1100 1710 1100 1710 {lab=0}
C {devices/lab_pin.sym} 1100 1710 0 0 {name=p344 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 1800 0 0 {name=xr0kq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 1830 20 1830 {lab=x_r0_kq}
C {devices/lab_pin.sym} 20 1830 0 0 {name=p345 sig_type=std_logic lab=x_r0_kq}
N -20 1800 -20 1800 {lab=x_p0}
C {devices/lab_pin.sym} -20 1800 0 1 {name=p346 sig_type=std_logic lab=x_p0}
N 20 1770 20 1770 {lab=vdg}
C {devices/lab_pin.sym} 20 1770 0 0 {name=p347 sig_type=std_logic lab=vdg}
N 20 1800 20 1800 {lab=vdg}
C {devices/lab_pin.sym} 20 1800 0 0 {name=p348 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 1800 0 0 {name=xr0kq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 1770 240 1770 {lab=x_r0_kq}
C {devices/lab_pin.sym} 240 1770 0 0 {name=p349 sig_type=std_logic lab=x_r0_kq}
N 200 1800 200 1800 {lab=x_p0}
C {devices/lab_pin.sym} 200 1800 0 1 {name=p350 sig_type=std_logic lab=x_p0}
N 240 1830 240 1830 {lab=0}
C {devices/lab_pin.sym} 240 1830 0 0 {name=p351 sig_type=std_logic lab=0}
N 240 1800 240 1800 {lab=0}
C {devices/lab_pin.sym} 240 1800 0 0 {name=p352 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 1800 0 0 {name=xr0kq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 1830 460 1830 {lab=x_p0}
C {devices/lab_pin.sym} 460 1830 0 0 {name=p353 sig_type=std_logic lab=x_p0}
N 420 1800 420 1800 {lab=x_r0_kq}
C {devices/lab_pin.sym} 420 1800 0 1 {name=p354 sig_type=std_logic lab=x_r0_kq}
N 460 1770 460 1770 {lab=vdg}
C {devices/lab_pin.sym} 460 1770 0 0 {name=p355 sig_type=std_logic lab=vdg}
N 460 1800 460 1800 {lab=vdg}
C {devices/lab_pin.sym} 460 1800 0 0 {name=p356 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 1800 0 0 {name=xr0kq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 1770 680 1770 {lab=x_p0}
C {devices/lab_pin.sym} 680 1770 0 0 {name=p357 sig_type=std_logic lab=x_p0}
N 640 1800 640 1800 {lab=x_r0_kq}
C {devices/lab_pin.sym} 640 1800 0 1 {name=p358 sig_type=std_logic lab=x_r0_kq}
N 680 1830 680 1830 {lab=0}
C {devices/lab_pin.sym} 680 1830 0 0 {name=p359 sig_type=std_logic lab=0}
N 680 1800 680 1800 {lab=0}
C {devices/lab_pin.sym} 680 1800 0 0 {name=p360 sig_type=std_logic lab=0}
C {devices/res.sym} 880 1800 0 0 {name=rkr01
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 1770 880 1770 {lab=x_r0_a}
C {devices/lab_pin.sym} 880 1770 0 0 {name=p361 sig_type=std_logic lab=x_r0_a}
N 880 1830 880 1830 {lab=0}
C {devices/lab_pin.sym} 880 1830 0 0 {name=p362 sig_type=std_logic lab=0}
C {devices/res.sym} 1100 1800 0 0 {name=rkr02
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 1100 1770 1100 1770 {lab=x_r0_b}
C {devices/lab_pin.sym} 1100 1770 0 0 {name=p363 sig_type=std_logic lab=x_r0_b}
N 1100 1830 1100 1830 {lab=0}
C {devices/lab_pin.sym} 1100 1830 0 0 {name=p364 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 1920 0 0 {name=xr1kq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 1950 20 1950 {lab=x_r1_kq}
C {devices/lab_pin.sym} 20 1950 0 0 {name=p365 sig_type=std_logic lab=x_r1_kq}
N -20 1920 -20 1920 {lab=x_p1}
C {devices/lab_pin.sym} -20 1920 0 1 {name=p366 sig_type=std_logic lab=x_p1}
N 20 1890 20 1890 {lab=vdg}
C {devices/lab_pin.sym} 20 1890 0 0 {name=p367 sig_type=std_logic lab=vdg}
N 20 1920 20 1920 {lab=vdg}
C {devices/lab_pin.sym} 20 1920 0 0 {name=p368 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 1920 0 0 {name=xr1kq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 1890 240 1890 {lab=x_r1_kq}
C {devices/lab_pin.sym} 240 1890 0 0 {name=p369 sig_type=std_logic lab=x_r1_kq}
N 200 1920 200 1920 {lab=x_p1}
C {devices/lab_pin.sym} 200 1920 0 1 {name=p370 sig_type=std_logic lab=x_p1}
N 240 1950 240 1950 {lab=0}
C {devices/lab_pin.sym} 240 1950 0 0 {name=p371 sig_type=std_logic lab=0}
N 240 1920 240 1920 {lab=0}
C {devices/lab_pin.sym} 240 1920 0 0 {name=p372 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 1920 0 0 {name=xr1kq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 1950 460 1950 {lab=x_p1}
C {devices/lab_pin.sym} 460 1950 0 0 {name=p373 sig_type=std_logic lab=x_p1}
N 420 1920 420 1920 {lab=x_r1_kq}
C {devices/lab_pin.sym} 420 1920 0 1 {name=p374 sig_type=std_logic lab=x_r1_kq}
N 460 1890 460 1890 {lab=vdg}
C {devices/lab_pin.sym} 460 1890 0 0 {name=p375 sig_type=std_logic lab=vdg}
N 460 1920 460 1920 {lab=vdg}
C {devices/lab_pin.sym} 460 1920 0 0 {name=p376 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 1920 0 0 {name=xr1kq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 1890 680 1890 {lab=x_p1}
C {devices/lab_pin.sym} 680 1890 0 0 {name=p377 sig_type=std_logic lab=x_p1}
N 640 1920 640 1920 {lab=x_r1_kq}
C {devices/lab_pin.sym} 640 1920 0 1 {name=p378 sig_type=std_logic lab=x_r1_kq}
N 680 1950 680 1950 {lab=0}
C {devices/lab_pin.sym} 680 1950 0 0 {name=p379 sig_type=std_logic lab=0}
N 680 1920 680 1920 {lab=0}
C {devices/lab_pin.sym} 680 1920 0 0 {name=p380 sig_type=std_logic lab=0}
C {devices/res.sym} 880 1920 0 0 {name=rkr11
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 1890 880 1890 {lab=x_r1_a}
C {devices/lab_pin.sym} 880 1890 0 0 {name=p381 sig_type=std_logic lab=x_r1_a}
N 880 1950 880 1950 {lab=0}
C {devices/lab_pin.sym} 880 1950 0 0 {name=p382 sig_type=std_logic lab=0}
C {devices/res.sym} 1100 1920 0 0 {name=rkr12
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 1100 1890 1100 1890 {lab=x_r1_b}
C {devices/lab_pin.sym} 1100 1890 0 0 {name=p383 sig_type=std_logic lab=x_r1_b}
N 1100 1950 1100 1950 {lab=0}
C {devices/lab_pin.sym} 1100 1950 0 0 {name=p384 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 2040 0 0 {name=xr2kq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 2070 20 2070 {lab=x_r2_kq}
C {devices/lab_pin.sym} 20 2070 0 0 {name=p385 sig_type=std_logic lab=x_r2_kq}
N -20 2040 -20 2040 {lab=x_p2}
C {devices/lab_pin.sym} -20 2040 0 1 {name=p386 sig_type=std_logic lab=x_p2}
N 20 2010 20 2010 {lab=vdg}
C {devices/lab_pin.sym} 20 2010 0 0 {name=p387 sig_type=std_logic lab=vdg}
N 20 2040 20 2040 {lab=vdg}
C {devices/lab_pin.sym} 20 2040 0 0 {name=p388 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 2040 0 0 {name=xr2kq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 2010 240 2010 {lab=x_r2_kq}
C {devices/lab_pin.sym} 240 2010 0 0 {name=p389 sig_type=std_logic lab=x_r2_kq}
N 200 2040 200 2040 {lab=x_p2}
C {devices/lab_pin.sym} 200 2040 0 1 {name=p390 sig_type=std_logic lab=x_p2}
N 240 2070 240 2070 {lab=0}
C {devices/lab_pin.sym} 240 2070 0 0 {name=p391 sig_type=std_logic lab=0}
N 240 2040 240 2040 {lab=0}
C {devices/lab_pin.sym} 240 2040 0 0 {name=p392 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 2040 0 0 {name=xr2kq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 2070 460 2070 {lab=x_p2}
C {devices/lab_pin.sym} 460 2070 0 0 {name=p393 sig_type=std_logic lab=x_p2}
N 420 2040 420 2040 {lab=x_r2_kq}
C {devices/lab_pin.sym} 420 2040 0 1 {name=p394 sig_type=std_logic lab=x_r2_kq}
N 460 2010 460 2010 {lab=vdg}
C {devices/lab_pin.sym} 460 2010 0 0 {name=p395 sig_type=std_logic lab=vdg}
N 460 2040 460 2040 {lab=vdg}
C {devices/lab_pin.sym} 460 2040 0 0 {name=p396 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 2040 0 0 {name=xr2kq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 2010 680 2010 {lab=x_p2}
C {devices/lab_pin.sym} 680 2010 0 0 {name=p397 sig_type=std_logic lab=x_p2}
N 640 2040 640 2040 {lab=x_r2_kq}
C {devices/lab_pin.sym} 640 2040 0 1 {name=p398 sig_type=std_logic lab=x_r2_kq}
N 680 2070 680 2070 {lab=0}
C {devices/lab_pin.sym} 680 2070 0 0 {name=p399 sig_type=std_logic lab=0}
N 680 2040 680 2040 {lab=0}
C {devices/lab_pin.sym} 680 2040 0 0 {name=p400 sig_type=std_logic lab=0}
C {devices/res.sym} 880 2040 0 0 {name=rkr21
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 2010 880 2010 {lab=x_r2_a}
C {devices/lab_pin.sym} 880 2010 0 0 {name=p401 sig_type=std_logic lab=x_r2_a}
N 880 2070 880 2070 {lab=0}
C {devices/lab_pin.sym} 880 2070 0 0 {name=p402 sig_type=std_logic lab=0}
C {devices/res.sym} 1100 2040 0 0 {name=rkr22
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 1100 2010 1100 2010 {lab=x_r2_b}
C {devices/lab_pin.sym} 1100 2010 0 0 {name=p403 sig_type=std_logic lab=x_r2_b}
N 1100 2070 1100 2070 {lab=0}
C {devices/lab_pin.sym} 1100 2070 0 0 {name=p404 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 2160 0 0 {name=xr3kq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 2190 20 2190 {lab=x_r3_kq}
C {devices/lab_pin.sym} 20 2190 0 0 {name=p405 sig_type=std_logic lab=x_r3_kq}
N -20 2160 -20 2160 {lab=x_p3}
C {devices/lab_pin.sym} -20 2160 0 1 {name=p406 sig_type=std_logic lab=x_p3}
N 20 2130 20 2130 {lab=vdg}
C {devices/lab_pin.sym} 20 2130 0 0 {name=p407 sig_type=std_logic lab=vdg}
N 20 2160 20 2160 {lab=vdg}
C {devices/lab_pin.sym} 20 2160 0 0 {name=p408 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 2160 0 0 {name=xr3kq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 2130 240 2130 {lab=x_r3_kq}
C {devices/lab_pin.sym} 240 2130 0 0 {name=p409 sig_type=std_logic lab=x_r3_kq}
N 200 2160 200 2160 {lab=x_p3}
C {devices/lab_pin.sym} 200 2160 0 1 {name=p410 sig_type=std_logic lab=x_p3}
N 240 2190 240 2190 {lab=0}
C {devices/lab_pin.sym} 240 2190 0 0 {name=p411 sig_type=std_logic lab=0}
N 240 2160 240 2160 {lab=0}
C {devices/lab_pin.sym} 240 2160 0 0 {name=p412 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 2160 0 0 {name=xr3kq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 2190 460 2190 {lab=x_p3}
C {devices/lab_pin.sym} 460 2190 0 0 {name=p413 sig_type=std_logic lab=x_p3}
N 420 2160 420 2160 {lab=x_r3_kq}
C {devices/lab_pin.sym} 420 2160 0 1 {name=p414 sig_type=std_logic lab=x_r3_kq}
N 460 2130 460 2130 {lab=vdg}
C {devices/lab_pin.sym} 460 2130 0 0 {name=p415 sig_type=std_logic lab=vdg}
N 460 2160 460 2160 {lab=vdg}
C {devices/lab_pin.sym} 460 2160 0 0 {name=p416 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 2160 0 0 {name=xr3kq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 2130 680 2130 {lab=x_p3}
C {devices/lab_pin.sym} 680 2130 0 0 {name=p417 sig_type=std_logic lab=x_p3}
N 640 2160 640 2160 {lab=x_r3_kq}
C {devices/lab_pin.sym} 640 2160 0 1 {name=p418 sig_type=std_logic lab=x_r3_kq}
N 680 2190 680 2190 {lab=0}
C {devices/lab_pin.sym} 680 2190 0 0 {name=p419 sig_type=std_logic lab=0}
N 680 2160 680 2160 {lab=0}
C {devices/lab_pin.sym} 680 2160 0 0 {name=p420 sig_type=std_logic lab=0}
C {devices/res.sym} 880 2160 0 0 {name=rkr31
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 2130 880 2130 {lab=x_r3_a}
C {devices/lab_pin.sym} 880 2130 0 0 {name=p421 sig_type=std_logic lab=x_r3_a}
N 880 2190 880 2190 {lab=0}
C {devices/lab_pin.sym} 880 2190 0 0 {name=p422 sig_type=std_logic lab=0}
C {devices/res.sym} 1100 2160 0 0 {name=rkr32
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 1100 2130 1100 2130 {lab=x_r3_b}
C {devices/lab_pin.sym} 1100 2130 0 0 {name=p423 sig_type=std_logic lab=x_r3_b}
N 1100 2190 1100 2190 {lab=0}
C {devices/lab_pin.sym} 1100 2190 0 0 {name=p424 sig_type=std_logic lab=0}
