v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
C {devices/iopin.sym} -200 -40 0 0 {name=tp lab=tp}
C {devices/iopin.sym} -200 -80 0 0 {name=tn lab=tn}
C {devices/iopin.sym} -200 -120 0 0 {name=ckp lab=ckp}
C {devices/iopin.sym} -200 -160 0 0 {name=ckn lab=ckn}
C {devices/iopin.sym} -200 -200 0 0 {name=vbuf lab=vbuf}
C {devices/iopin.sym} -200 -240 0 0 {name=0 lab=0}
C {devices/title.sym} 0 40 0 0 {name=t1 author="HT13G-M P2.7.1"}
C {devices/lab_pin.sym} 200 40 0 0 {name=ttitle lab=lo_buffer_B2_4}
C {devices/capa.sym} 0 0 0 0 {name=ccp
value=100f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 0 -30 0 -30 {lab=tp}
C {devices/lab_pin.sym} 0 -30 0 0 {name=p1 sig_type=std_logic lab=tp}
N 0 30 0 30 {lab=x_bip}
C {devices/lab_pin.sym} 0 30 0 0 {name=p2 sig_type=std_logic lab=x_bip}
C {devices/res.sym} 220 0 0 0 {name=rfp
value=50k
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 -30 220 -30 {lab=x_bip}
C {devices/lab_pin.sym} 220 -30 0 0 {name=p3 sig_type=std_logic lab=x_bip}
N 220 30 220 30 {lab=x_bop}
C {devices/lab_pin.sym} 220 30 0 0 {name=p4 sig_type=std_logic lab=x_bop}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 0 0 0 {name=xb1pp
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 30 460 30 {lab=x_bop}
C {devices/lab_pin.sym} 460 30 0 0 {name=p5 sig_type=std_logic lab=x_bop}
N 420 0 420 0 {lab=x_bip}
C {devices/lab_pin.sym} 420 0 0 1 {name=p6 sig_type=std_logic lab=x_bip}
N 460 -30 460 -30 {lab=vbuf}
C {devices/lab_pin.sym} 460 -30 0 0 {name=p7 sig_type=std_logic lab=vbuf}
N 460 0 460 0 {lab=vbuf}
C {devices/lab_pin.sym} 460 0 0 0 {name=p8 sig_type=std_logic lab=vbuf}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 0 0 0 {name=xb1pn
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 -30 680 -30 {lab=x_bop}
C {devices/lab_pin.sym} 680 -30 0 0 {name=p9 sig_type=std_logic lab=x_bop}
N 640 0 640 0 {lab=x_bip}
C {devices/lab_pin.sym} 640 0 0 1 {name=p10 sig_type=std_logic lab=x_bip}
N 680 30 680 30 {lab=0}
C {devices/lab_pin.sym} 680 30 0 0 {name=p11 sig_type=std_logic lab=0}
N 680 0 680 0 {lab=0}
C {devices/lab_pin.sym} 680 0 0 0 {name=p12 sig_type=std_logic lab=0}
C {devices/capa.sym} 880 0 0 0 {name=ccmp
value=50f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 880 -30 880 -30 {lab=x_bop}
C {devices/lab_pin.sym} 880 -30 0 0 {name=p13 sig_type=std_logic lab=x_bop}
N 880 30 880 30 {lab=x_mip}
C {devices/lab_pin.sym} 880 30 0 0 {name=p14 sig_type=std_logic lab=x_mip}
C {devices/res.sym} 1100 0 0 0 {name=rfmp
value=50k
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 1100 -30 1100 -30 {lab=x_mip}
C {devices/lab_pin.sym} 1100 -30 0 0 {name=p15 sig_type=std_logic lab=x_mip}
N 1100 30 1100 30 {lab=x_bmp}
C {devices/lab_pin.sym} 1100 30 0 0 {name=p16 sig_type=std_logic lab=x_bmp}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 120 0 0 {name=xbmpp
w=6u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 150 20 150 {lab=x_bmp}
C {devices/lab_pin.sym} 20 150 0 0 {name=p17 sig_type=std_logic lab=x_bmp}
N -20 120 -20 120 {lab=x_mip}
C {devices/lab_pin.sym} -20 120 0 1 {name=p18 sig_type=std_logic lab=x_mip}
N 20 90 20 90 {lab=vbuf}
C {devices/lab_pin.sym} 20 90 0 0 {name=p19 sig_type=std_logic lab=vbuf}
N 20 120 20 120 {lab=vbuf}
C {devices/lab_pin.sym} 20 120 0 0 {name=p20 sig_type=std_logic lab=vbuf}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 120 0 0 {name=xbmpn
w=3u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 90 240 90 {lab=x_bmp}
C {devices/lab_pin.sym} 240 90 0 0 {name=p21 sig_type=std_logic lab=x_bmp}
N 200 120 200 120 {lab=x_mip}
C {devices/lab_pin.sym} 200 120 0 1 {name=p22 sig_type=std_logic lab=x_mip}
N 240 150 240 150 {lab=0}
C {devices/lab_pin.sym} 240 150 0 0 {name=p23 sig_type=std_logic lab=0}
N 240 120 240 120 {lab=0}
C {devices/lab_pin.sym} 240 120 0 0 {name=p24 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 120 0 0 {name=xb2pp
w=8.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 150 460 150 {lab=ckp}
C {devices/lab_pin.sym} 460 150 0 0 {name=p25 sig_type=std_logic lab=ckp}
N 420 120 420 120 {lab=x_bmp}
C {devices/lab_pin.sym} 420 120 0 1 {name=p26 sig_type=std_logic lab=x_bmp}
N 460 90 460 90 {lab=vbuf}
C {devices/lab_pin.sym} 460 90 0 0 {name=p27 sig_type=std_logic lab=vbuf}
N 460 120 460 120 {lab=vbuf}
C {devices/lab_pin.sym} 460 120 0 0 {name=p28 sig_type=std_logic lab=vbuf}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 120 0 0 {name=xb2pn
w=4.0u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 90 680 90 {lab=ckp}
C {devices/lab_pin.sym} 680 90 0 0 {name=p29 sig_type=std_logic lab=ckp}
N 640 120 640 120 {lab=x_bmp}
C {devices/lab_pin.sym} 640 120 0 1 {name=p30 sig_type=std_logic lab=x_bmp}
N 680 150 680 150 {lab=0}
C {devices/lab_pin.sym} 680 150 0 0 {name=p31 sig_type=std_logic lab=0}
N 680 120 680 120 {lab=0}
C {devices/lab_pin.sym} 680 120 0 0 {name=p32 sig_type=std_logic lab=0}
C {devices/capa.sym} 880 120 0 0 {name=ccn
value=100f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 880 90 880 90 {lab=tn}
C {devices/lab_pin.sym} 880 90 0 0 {name=p33 sig_type=std_logic lab=tn}
N 880 150 880 150 {lab=x_bin}
C {devices/lab_pin.sym} 880 150 0 0 {name=p34 sig_type=std_logic lab=x_bin}
C {devices/res.sym} 1100 120 0 0 {name=rfn
value=50k
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 1100 90 1100 90 {lab=x_bin}
C {devices/lab_pin.sym} 1100 90 0 0 {name=p35 sig_type=std_logic lab=x_bin}
N 1100 150 1100 150 {lab=x_bon}
C {devices/lab_pin.sym} 1100 150 0 0 {name=p36 sig_type=std_logic lab=x_bon}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 240 0 0 {name=xb1np
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 270 20 270 {lab=x_bon}
C {devices/lab_pin.sym} 20 270 0 0 {name=p37 sig_type=std_logic lab=x_bon}
N -20 240 -20 240 {lab=x_bin}
C {devices/lab_pin.sym} -20 240 0 1 {name=p38 sig_type=std_logic lab=x_bin}
N 20 210 20 210 {lab=vbuf}
C {devices/lab_pin.sym} 20 210 0 0 {name=p39 sig_type=std_logic lab=vbuf}
N 20 240 20 240 {lab=vbuf}
C {devices/lab_pin.sym} 20 240 0 0 {name=p40 sig_type=std_logic lab=vbuf}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 240 0 0 {name=xb1nn
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 210 240 210 {lab=x_bon}
C {devices/lab_pin.sym} 240 210 0 0 {name=p41 sig_type=std_logic lab=x_bon}
N 200 240 200 240 {lab=x_bin}
C {devices/lab_pin.sym} 200 240 0 1 {name=p42 sig_type=std_logic lab=x_bin}
N 240 270 240 270 {lab=0}
C {devices/lab_pin.sym} 240 270 0 0 {name=p43 sig_type=std_logic lab=0}
N 240 240 240 240 {lab=0}
C {devices/lab_pin.sym} 240 240 0 0 {name=p44 sig_type=std_logic lab=0}
C {devices/capa.sym} 440 240 0 0 {name=ccmn
value=50f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 440 210 440 210 {lab=x_bon}
C {devices/lab_pin.sym} 440 210 0 0 {name=p45 sig_type=std_logic lab=x_bon}
N 440 270 440 270 {lab=x_min}
C {devices/lab_pin.sym} 440 270 0 0 {name=p46 sig_type=std_logic lab=x_min}
C {devices/res.sym} 660 240 0 0 {name=rfmn
value=50k
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 660 210 660 210 {lab=x_min}
C {devices/lab_pin.sym} 660 210 0 0 {name=p47 sig_type=std_logic lab=x_min}
N 660 270 660 270 {lab=x_bmn}
C {devices/lab_pin.sym} 660 270 0 0 {name=p48 sig_type=std_logic lab=x_bmn}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 240 0 0 {name=xbmnp
w=6u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 270 900 270 {lab=x_bmn}
C {devices/lab_pin.sym} 900 270 0 0 {name=p49 sig_type=std_logic lab=x_bmn}
N 860 240 860 240 {lab=x_min}
C {devices/lab_pin.sym} 860 240 0 1 {name=p50 sig_type=std_logic lab=x_min}
N 900 210 900 210 {lab=vbuf}
C {devices/lab_pin.sym} 900 210 0 0 {name=p51 sig_type=std_logic lab=vbuf}
N 900 240 900 240 {lab=vbuf}
C {devices/lab_pin.sym} 900 240 0 0 {name=p52 sig_type=std_logic lab=vbuf}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 240 0 0 {name=xbmnn
w=3u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 210 1120 210 {lab=x_bmn}
C {devices/lab_pin.sym} 1120 210 0 0 {name=p53 sig_type=std_logic lab=x_bmn}
N 1080 240 1080 240 {lab=x_min}
C {devices/lab_pin.sym} 1080 240 0 1 {name=p54 sig_type=std_logic lab=x_min}
N 1120 270 1120 270 {lab=0}
C {devices/lab_pin.sym} 1120 270 0 0 {name=p55 sig_type=std_logic lab=0}
N 1120 240 1120 240 {lab=0}
C {devices/lab_pin.sym} 1120 240 0 0 {name=p56 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 360 0 0 {name=xb2np
w=8.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 390 20 390 {lab=ckn}
C {devices/lab_pin.sym} 20 390 0 0 {name=p57 sig_type=std_logic lab=ckn}
N -20 360 -20 360 {lab=x_bmn}
C {devices/lab_pin.sym} -20 360 0 1 {name=p58 sig_type=std_logic lab=x_bmn}
N 20 330 20 330 {lab=vbuf}
C {devices/lab_pin.sym} 20 330 0 0 {name=p59 sig_type=std_logic lab=vbuf}
N 20 360 20 360 {lab=vbuf}
C {devices/lab_pin.sym} 20 360 0 0 {name=p60 sig_type=std_logic lab=vbuf}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 360 0 0 {name=xb2nn
w=4.0u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 330 240 330 {lab=ckn}
C {devices/lab_pin.sym} 240 330 0 0 {name=p61 sig_type=std_logic lab=ckn}
N 200 360 200 360 {lab=x_bmn}
C {devices/lab_pin.sym} 200 360 0 1 {name=p62 sig_type=std_logic lab=x_bmn}
N 240 390 240 390 {lab=0}
C {devices/lab_pin.sym} 240 390 0 0 {name=p63 sig_type=std_logic lab=0}
N 240 360 240 360 {lab=0}
C {devices/lab_pin.sym} 240 360 0 0 {name=p64 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 360 0 0 {name=xbxpp
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 390 460 390 {lab=x_bon}
C {devices/lab_pin.sym} 460 390 0 0 {name=p65 sig_type=std_logic lab=x_bon}
N 420 360 420 360 {lab=x_bop}
C {devices/lab_pin.sym} 420 360 0 1 {name=p66 sig_type=std_logic lab=x_bop}
N 460 330 460 330 {lab=vbuf}
C {devices/lab_pin.sym} 460 330 0 0 {name=p67 sig_type=std_logic lab=vbuf}
N 460 360 460 360 {lab=vbuf}
C {devices/lab_pin.sym} 460 360 0 0 {name=p68 sig_type=std_logic lab=vbuf}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 360 0 0 {name=xbxpn
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 330 680 330 {lab=x_bon}
C {devices/lab_pin.sym} 680 330 0 0 {name=p69 sig_type=std_logic lab=x_bon}
N 640 360 640 360 {lab=x_bop}
C {devices/lab_pin.sym} 640 360 0 1 {name=p70 sig_type=std_logic lab=x_bop}
N 680 390 680 390 {lab=0}
C {devices/lab_pin.sym} 680 390 0 0 {name=p71 sig_type=std_logic lab=0}
N 680 360 680 360 {lab=0}
C {devices/lab_pin.sym} 680 360 0 0 {name=p72 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 360 0 0 {name=xbxnp
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 390 900 390 {lab=x_bop}
C {devices/lab_pin.sym} 900 390 0 0 {name=p73 sig_type=std_logic lab=x_bop}
N 860 360 860 360 {lab=x_bon}
C {devices/lab_pin.sym} 860 360 0 1 {name=p74 sig_type=std_logic lab=x_bon}
N 900 330 900 330 {lab=vbuf}
C {devices/lab_pin.sym} 900 330 0 0 {name=p75 sig_type=std_logic lab=vbuf}
N 900 360 900 360 {lab=vbuf}
C {devices/lab_pin.sym} 900 360 0 0 {name=p76 sig_type=std_logic lab=vbuf}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 360 0 0 {name=xbxnn
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 330 1120 330 {lab=x_bop}
C {devices/lab_pin.sym} 1120 330 0 0 {name=p77 sig_type=std_logic lab=x_bop}
N 1080 360 1080 360 {lab=x_bon}
C {devices/lab_pin.sym} 1080 360 0 1 {name=p78 sig_type=std_logic lab=x_bon}
N 1120 390 1120 390 {lab=0}
C {devices/lab_pin.sym} 1120 390 0 0 {name=p79 sig_type=std_logic lab=0}
N 1120 360 1120 360 {lab=0}
C {devices/lab_pin.sym} 1120 360 0 0 {name=p80 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 480 0 0 {name=xbopp
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 510 20 510 {lab=ckn}
C {devices/lab_pin.sym} 20 510 0 0 {name=p81 sig_type=std_logic lab=ckn}
N -20 480 -20 480 {lab=ckp}
C {devices/lab_pin.sym} -20 480 0 1 {name=p82 sig_type=std_logic lab=ckp}
N 20 450 20 450 {lab=vbuf}
C {devices/lab_pin.sym} 20 450 0 0 {name=p83 sig_type=std_logic lab=vbuf}
N 20 480 20 480 {lab=vbuf}
C {devices/lab_pin.sym} 20 480 0 0 {name=p84 sig_type=std_logic lab=vbuf}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 480 0 0 {name=xbopn
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 450 240 450 {lab=ckn}
C {devices/lab_pin.sym} 240 450 0 0 {name=p85 sig_type=std_logic lab=ckn}
N 200 480 200 480 {lab=ckp}
C {devices/lab_pin.sym} 200 480 0 1 {name=p86 sig_type=std_logic lab=ckp}
N 240 510 240 510 {lab=0}
C {devices/lab_pin.sym} 240 510 0 0 {name=p87 sig_type=std_logic lab=0}
N 240 480 240 480 {lab=0}
C {devices/lab_pin.sym} 240 480 0 0 {name=p88 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 480 0 0 {name=xbonp
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 510 460 510 {lab=ckp}
C {devices/lab_pin.sym} 460 510 0 0 {name=p89 sig_type=std_logic lab=ckp}
N 420 480 420 480 {lab=ckn}
C {devices/lab_pin.sym} 420 480 0 1 {name=p90 sig_type=std_logic lab=ckn}
N 460 450 460 450 {lab=vbuf}
C {devices/lab_pin.sym} 460 450 0 0 {name=p91 sig_type=std_logic lab=vbuf}
N 460 480 460 480 {lab=vbuf}
C {devices/lab_pin.sym} 460 480 0 0 {name=p92 sig_type=std_logic lab=vbuf}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 480 0 0 {name=xbonn
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 450 680 450 {lab=ckp}
C {devices/lab_pin.sym} 680 450 0 0 {name=p93 sig_type=std_logic lab=ckp}
N 640 480 640 480 {lab=ckn}
C {devices/lab_pin.sym} 640 480 0 1 {name=p94 sig_type=std_logic lab=ckn}
N 680 510 680 510 {lab=0}
C {devices/lab_pin.sym} 680 510 0 0 {name=p95 sig_type=std_logic lab=0}
N 680 480 680 480 {lab=0}
C {devices/lab_pin.sym} 680 480 0 0 {name=p96 sig_type=std_logic lab=0}
