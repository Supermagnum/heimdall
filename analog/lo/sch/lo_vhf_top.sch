v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
C {devices/iopin.sym} -200 -40 0 0 {name=tp lab=tp}
C {devices/iopin.sym} -200 -80 0 0 {name=tn lab=tn}
C {devices/iopin.sym} -200 -120 0 0 {name=nbias lab=nbias}
C {devices/iopin.sym} -200 -160 0 0 {name=en_lodiv lab=en_lodiv}
C {devices/iopin.sym} -200 -200 0 0 {name=vref lab=vref}
C {devices/iopin.sym} -200 -240 0 0 {name=x_r1 lab=x_r1}
C {devices/iopin.sym} -200 -280 0 0 {name=x_r2 lab=x_r2}
C {devices/iopin.sym} -200 -320 0 0 {name=x_r3 lab=x_r3}
C {devices/iopin.sym} -200 -360 0 0 {name=x_r4 lab=x_r4}
C {devices/iopin.sym} -200 -400 0 0 {name=x_r1b lab=x_r1b}
C {devices/iopin.sym} -200 -440 0 0 {name=x_r2b lab=x_r2b}
C {devices/iopin.sym} -200 -480 0 0 {name=x_r3b lab=x_r3b}
C {devices/iopin.sym} -200 -520 0 0 {name=x_r4b lab=x_r4b}
C {devices/iopin.sym} -200 -560 0 0 {name=vbuf lab=vbuf}
C {devices/iopin.sym} -200 -600 0 0 {name=vdv lab=vdv}
C {devices/iopin.sym} -200 -640 0 0 {name=vcv lab=vcv}
C {devices/iopin.sym} -200 -680 0 0 {name=vdg lab=vdg}
C {devices/iopin.sym} -200 -720 0 0 {name=vdd lab=vdd}
C {devices/iopin.sym} -200 -760 0 0 {name=0 lab=0}
C {devices/title.sym} 0 40 0 0 {name=t1 author="HT13G-M P2.7.1"}
C {devices/lab_pin.sym} 200 40 0 0 {name=ttitle lab=lo_vhf_top_flat}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 0 0 0 {name=xenb_p
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 30 20 30 {lab=en_n}
C {devices/lab_pin.sym} 20 30 0 0 {name=p1 sig_type=std_logic lab=en_n}
N -20 0 -20 0 {lab=en_lodiv}
C {devices/lab_pin.sym} -20 0 0 1 {name=p2 sig_type=std_logic lab=en_lodiv}
N 20 -30 20 -30 {lab=vdd}
C {devices/lab_pin.sym} 20 -30 0 0 {name=p3 sig_type=std_logic lab=vdd}
N 20 0 20 0 {lab=vdd}
C {devices/lab_pin.sym} 20 0 0 0 {name=p4 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 0 0 0 {name=xenb_n
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 -30 240 -30 {lab=en_n}
C {devices/lab_pin.sym} 240 -30 0 0 {name=p5 sig_type=std_logic lab=en_n}
N 200 0 200 0 {lab=en_lodiv}
C {devices/lab_pin.sym} 200 0 0 1 {name=p6 sig_type=std_logic lab=en_lodiv}
N 240 30 240 30 {lab=0}
C {devices/lab_pin.sym} 240 30 0 0 {name=p7 sig_type=std_logic lab=0}
N 240 0 240 0 {lab=0}
C {devices/lab_pin.sym} 240 0 0 0 {name=p8 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 0 0 0 {name=tgn
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 -30 460 -30 {lab=nb_lo}
C {devices/lab_pin.sym} 460 -30 0 0 {name=p9 sig_type=std_logic lab=nb_lo}
N 420 0 420 0 {lab=en_lodiv}
C {devices/lab_pin.sym} 420 0 0 1 {name=p10 sig_type=std_logic lab=en_lodiv}
N 460 30 460 30 {lab=nbias}
C {devices/lab_pin.sym} 460 30 0 0 {name=p11 sig_type=std_logic lab=nbias}
N 460 0 460 0 {lab=0}
C {devices/lab_pin.sym} 460 0 0 0 {name=p12 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 0 0 0 {name=tgp
w=8u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 30 680 30 {lab=nb_lo}
C {devices/lab_pin.sym} 680 30 0 0 {name=p13 sig_type=std_logic lab=nb_lo}
N 640 0 640 0 {lab=en_n}
C {devices/lab_pin.sym} 640 0 0 1 {name=p14 sig_type=std_logic lab=en_n}
N 680 -30 680 -30 {lab=nbias}
C {devices/lab_pin.sym} 680 -30 0 0 {name=p15 sig_type=std_logic lab=nbias}
N 680 0 680 0 {lab=vdd}
C {devices/lab_pin.sym} 680 0 0 0 {name=p16 sig_type=std_logic lab=vdd}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 0 0 0 {name=mpd
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 -30 900 -30 {lab=nb_lo}
C {devices/lab_pin.sym} 900 -30 0 0 {name=p17 sig_type=std_logic lab=nb_lo}
N 860 0 860 0 {lab=en_n}
C {devices/lab_pin.sym} 860 0 0 1 {name=p18 sig_type=std_logic lab=en_n}
N 900 30 900 30 {lab=0}
C {devices/lab_pin.sym} 900 30 0 0 {name=p19 sig_type=std_logic lab=0}
N 900 0 900 0 {lab=0}
C {devices/lab_pin.sym} 900 0 0 0 {name=p20 sig_type=std_logic lab=0}
C {devices/capa.sym} 1100 0 0 0 {name=ccp
value=100f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 1100 -30 1100 -30 {lab=tp}
C {devices/lab_pin.sym} 1100 -30 0 0 {name=p21 sig_type=std_logic lab=tp}
N 1100 30 1100 30 {lab=x_bip}
C {devices/lab_pin.sym} 1100 30 0 0 {name=p22 sig_type=std_logic lab=x_bip}
C {devices/res.sym} 0 120 0 0 {name=rfp
value=50k
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 0 90 0 90 {lab=x_bip}
C {devices/lab_pin.sym} 0 90 0 0 {name=p23 sig_type=std_logic lab=x_bip}
N 0 150 0 150 {lab=x_bop}
C {devices/lab_pin.sym} 0 150 0 0 {name=p24 sig_type=std_logic lab=x_bop}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 120 0 0 {name=xb1pp
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 150 240 150 {lab=x_bop}
C {devices/lab_pin.sym} 240 150 0 0 {name=p25 sig_type=std_logic lab=x_bop}
N 200 120 200 120 {lab=x_bip}
C {devices/lab_pin.sym} 200 120 0 1 {name=p26 sig_type=std_logic lab=x_bip}
N 240 90 240 90 {lab=vbuf}
C {devices/lab_pin.sym} 240 90 0 0 {name=p27 sig_type=std_logic lab=vbuf}
N 240 120 240 120 {lab=vbuf}
C {devices/lab_pin.sym} 240 120 0 0 {name=p28 sig_type=std_logic lab=vbuf}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 120 0 0 {name=xb1pn
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 90 460 90 {lab=x_bop}
C {devices/lab_pin.sym} 460 90 0 0 {name=p29 sig_type=std_logic lab=x_bop}
N 420 120 420 120 {lab=x_bip}
C {devices/lab_pin.sym} 420 120 0 1 {name=p30 sig_type=std_logic lab=x_bip}
N 460 150 460 150 {lab=0}
C {devices/lab_pin.sym} 460 150 0 0 {name=p31 sig_type=std_logic lab=0}
N 460 120 460 120 {lab=0}
C {devices/lab_pin.sym} 460 120 0 0 {name=p32 sig_type=std_logic lab=0}
C {devices/capa.sym} 660 120 0 0 {name=ccmp
value=50f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 660 90 660 90 {lab=x_bop}
C {devices/lab_pin.sym} 660 90 0 0 {name=p33 sig_type=std_logic lab=x_bop}
N 660 150 660 150 {lab=x_mip}
C {devices/lab_pin.sym} 660 150 0 0 {name=p34 sig_type=std_logic lab=x_mip}
C {devices/res.sym} 880 120 0 0 {name=rfmp
value=50k
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 90 880 90 {lab=x_mip}
C {devices/lab_pin.sym} 880 90 0 0 {name=p35 sig_type=std_logic lab=x_mip}
N 880 150 880 150 {lab=x_bmp}
C {devices/lab_pin.sym} 880 150 0 0 {name=p36 sig_type=std_logic lab=x_bmp}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 120 0 0 {name=xbmpp
w=6u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 150 1120 150 {lab=x_bmp}
C {devices/lab_pin.sym} 1120 150 0 0 {name=p37 sig_type=std_logic lab=x_bmp}
N 1080 120 1080 120 {lab=x_mip}
C {devices/lab_pin.sym} 1080 120 0 1 {name=p38 sig_type=std_logic lab=x_mip}
N 1120 90 1120 90 {lab=vbuf}
C {devices/lab_pin.sym} 1120 90 0 0 {name=p39 sig_type=std_logic lab=vbuf}
N 1120 120 1120 120 {lab=vbuf}
C {devices/lab_pin.sym} 1120 120 0 0 {name=p40 sig_type=std_logic lab=vbuf}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 240 0 0 {name=xbmpn
w=3u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 210 20 210 {lab=x_bmp}
C {devices/lab_pin.sym} 20 210 0 0 {name=p41 sig_type=std_logic lab=x_bmp}
N -20 240 -20 240 {lab=x_mip}
C {devices/lab_pin.sym} -20 240 0 1 {name=p42 sig_type=std_logic lab=x_mip}
N 20 270 20 270 {lab=0}
C {devices/lab_pin.sym} 20 270 0 0 {name=p43 sig_type=std_logic lab=0}
N 20 240 20 240 {lab=0}
C {devices/lab_pin.sym} 20 240 0 0 {name=p44 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 240 0 0 {name=xb2pp
w=8.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 270 240 270 {lab=ckp}
C {devices/lab_pin.sym} 240 270 0 0 {name=p45 sig_type=std_logic lab=ckp}
N 200 240 200 240 {lab=x_bmp}
C {devices/lab_pin.sym} 200 240 0 1 {name=p46 sig_type=std_logic lab=x_bmp}
N 240 210 240 210 {lab=vbuf}
C {devices/lab_pin.sym} 240 210 0 0 {name=p47 sig_type=std_logic lab=vbuf}
N 240 240 240 240 {lab=vbuf}
C {devices/lab_pin.sym} 240 240 0 0 {name=p48 sig_type=std_logic lab=vbuf}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 240 0 0 {name=xb2pn
w=4.0u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 210 460 210 {lab=ckp}
C {devices/lab_pin.sym} 460 210 0 0 {name=p49 sig_type=std_logic lab=ckp}
N 420 240 420 240 {lab=x_bmp}
C {devices/lab_pin.sym} 420 240 0 1 {name=p50 sig_type=std_logic lab=x_bmp}
N 460 270 460 270 {lab=0}
C {devices/lab_pin.sym} 460 270 0 0 {name=p51 sig_type=std_logic lab=0}
N 460 240 460 240 {lab=0}
C {devices/lab_pin.sym} 460 240 0 0 {name=p52 sig_type=std_logic lab=0}
C {devices/capa.sym} 660 240 0 0 {name=ccn
value=100f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 660 210 660 210 {lab=tn}
C {devices/lab_pin.sym} 660 210 0 0 {name=p53 sig_type=std_logic lab=tn}
N 660 270 660 270 {lab=x_bin}
C {devices/lab_pin.sym} 660 270 0 0 {name=p54 sig_type=std_logic lab=x_bin}
C {devices/res.sym} 880 240 0 0 {name=rfn
value=50k
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 210 880 210 {lab=x_bin}
C {devices/lab_pin.sym} 880 210 0 0 {name=p55 sig_type=std_logic lab=x_bin}
N 880 270 880 270 {lab=x_bon}
C {devices/lab_pin.sym} 880 270 0 0 {name=p56 sig_type=std_logic lab=x_bon}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 240 0 0 {name=xb1np
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 270 1120 270 {lab=x_bon}
C {devices/lab_pin.sym} 1120 270 0 0 {name=p57 sig_type=std_logic lab=x_bon}
N 1080 240 1080 240 {lab=x_bin}
C {devices/lab_pin.sym} 1080 240 0 1 {name=p58 sig_type=std_logic lab=x_bin}
N 1120 210 1120 210 {lab=vbuf}
C {devices/lab_pin.sym} 1120 210 0 0 {name=p59 sig_type=std_logic lab=vbuf}
N 1120 240 1120 240 {lab=vbuf}
C {devices/lab_pin.sym} 1120 240 0 0 {name=p60 sig_type=std_logic lab=vbuf}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 360 0 0 {name=xb1nn
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 330 20 330 {lab=x_bon}
C {devices/lab_pin.sym} 20 330 0 0 {name=p61 sig_type=std_logic lab=x_bon}
N -20 360 -20 360 {lab=x_bin}
C {devices/lab_pin.sym} -20 360 0 1 {name=p62 sig_type=std_logic lab=x_bin}
N 20 390 20 390 {lab=0}
C {devices/lab_pin.sym} 20 390 0 0 {name=p63 sig_type=std_logic lab=0}
N 20 360 20 360 {lab=0}
C {devices/lab_pin.sym} 20 360 0 0 {name=p64 sig_type=std_logic lab=0}
C {devices/capa.sym} 220 360 0 0 {name=ccmn
value=50f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 220 330 220 330 {lab=x_bon}
C {devices/lab_pin.sym} 220 330 0 0 {name=p65 sig_type=std_logic lab=x_bon}
N 220 390 220 390 {lab=x_min}
C {devices/lab_pin.sym} 220 390 0 0 {name=p66 sig_type=std_logic lab=x_min}
C {devices/res.sym} 440 360 0 0 {name=rfmn
value=50k
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 440 330 440 330 {lab=x_min}
C {devices/lab_pin.sym} 440 330 0 0 {name=p67 sig_type=std_logic lab=x_min}
N 440 390 440 390 {lab=x_bmn}
C {devices/lab_pin.sym} 440 390 0 0 {name=p68 sig_type=std_logic lab=x_bmn}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 360 0 0 {name=xbmnp
w=6u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 390 680 390 {lab=x_bmn}
C {devices/lab_pin.sym} 680 390 0 0 {name=p69 sig_type=std_logic lab=x_bmn}
N 640 360 640 360 {lab=x_min}
C {devices/lab_pin.sym} 640 360 0 1 {name=p70 sig_type=std_logic lab=x_min}
N 680 330 680 330 {lab=vbuf}
C {devices/lab_pin.sym} 680 330 0 0 {name=p71 sig_type=std_logic lab=vbuf}
N 680 360 680 360 {lab=vbuf}
C {devices/lab_pin.sym} 680 360 0 0 {name=p72 sig_type=std_logic lab=vbuf}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 360 0 0 {name=xbmnn
w=3u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 330 900 330 {lab=x_bmn}
C {devices/lab_pin.sym} 900 330 0 0 {name=p73 sig_type=std_logic lab=x_bmn}
N 860 360 860 360 {lab=x_min}
C {devices/lab_pin.sym} 860 360 0 1 {name=p74 sig_type=std_logic lab=x_min}
N 900 390 900 390 {lab=0}
C {devices/lab_pin.sym} 900 390 0 0 {name=p75 sig_type=std_logic lab=0}
N 900 360 900 360 {lab=0}
C {devices/lab_pin.sym} 900 360 0 0 {name=p76 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 360 0 0 {name=xb2np
w=8.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 390 1120 390 {lab=ckn}
C {devices/lab_pin.sym} 1120 390 0 0 {name=p77 sig_type=std_logic lab=ckn}
N 1080 360 1080 360 {lab=x_bmn}
C {devices/lab_pin.sym} 1080 360 0 1 {name=p78 sig_type=std_logic lab=x_bmn}
N 1120 330 1120 330 {lab=vbuf}
C {devices/lab_pin.sym} 1120 330 0 0 {name=p79 sig_type=std_logic lab=vbuf}
N 1120 360 1120 360 {lab=vbuf}
C {devices/lab_pin.sym} 1120 360 0 0 {name=p80 sig_type=std_logic lab=vbuf}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 480 0 0 {name=xb2nn
w=4.0u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 450 20 450 {lab=ckn}
C {devices/lab_pin.sym} 20 450 0 0 {name=p81 sig_type=std_logic lab=ckn}
N -20 480 -20 480 {lab=x_bmn}
C {devices/lab_pin.sym} -20 480 0 1 {name=p82 sig_type=std_logic lab=x_bmn}
N 20 510 20 510 {lab=0}
C {devices/lab_pin.sym} 20 510 0 0 {name=p83 sig_type=std_logic lab=0}
N 20 480 20 480 {lab=0}
C {devices/lab_pin.sym} 20 480 0 0 {name=p84 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 480 0 0 {name=xbxpp
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 510 240 510 {lab=x_bon}
C {devices/lab_pin.sym} 240 510 0 0 {name=p85 sig_type=std_logic lab=x_bon}
N 200 480 200 480 {lab=x_bop}
C {devices/lab_pin.sym} 200 480 0 1 {name=p86 sig_type=std_logic lab=x_bop}
N 240 450 240 450 {lab=vbuf}
C {devices/lab_pin.sym} 240 450 0 0 {name=p87 sig_type=std_logic lab=vbuf}
N 240 480 240 480 {lab=vbuf}
C {devices/lab_pin.sym} 240 480 0 0 {name=p88 sig_type=std_logic lab=vbuf}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 480 0 0 {name=xbxpn
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 450 460 450 {lab=x_bon}
C {devices/lab_pin.sym} 460 450 0 0 {name=p89 sig_type=std_logic lab=x_bon}
N 420 480 420 480 {lab=x_bop}
C {devices/lab_pin.sym} 420 480 0 1 {name=p90 sig_type=std_logic lab=x_bop}
N 460 510 460 510 {lab=0}
C {devices/lab_pin.sym} 460 510 0 0 {name=p91 sig_type=std_logic lab=0}
N 460 480 460 480 {lab=0}
C {devices/lab_pin.sym} 460 480 0 0 {name=p92 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 480 0 0 {name=xbxnp
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 510 680 510 {lab=x_bop}
C {devices/lab_pin.sym} 680 510 0 0 {name=p93 sig_type=std_logic lab=x_bop}
N 640 480 640 480 {lab=x_bon}
C {devices/lab_pin.sym} 640 480 0 1 {name=p94 sig_type=std_logic lab=x_bon}
N 680 450 680 450 {lab=vbuf}
C {devices/lab_pin.sym} 680 450 0 0 {name=p95 sig_type=std_logic lab=vbuf}
N 680 480 680 480 {lab=vbuf}
C {devices/lab_pin.sym} 680 480 0 0 {name=p96 sig_type=std_logic lab=vbuf}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 480 0 0 {name=xbxnn
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 450 900 450 {lab=x_bop}
C {devices/lab_pin.sym} 900 450 0 0 {name=p97 sig_type=std_logic lab=x_bop}
N 860 480 860 480 {lab=x_bon}
C {devices/lab_pin.sym} 860 480 0 1 {name=p98 sig_type=std_logic lab=x_bon}
N 900 510 900 510 {lab=0}
C {devices/lab_pin.sym} 900 510 0 0 {name=p99 sig_type=std_logic lab=0}
N 900 480 900 480 {lab=0}
C {devices/lab_pin.sym} 900 480 0 0 {name=p100 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 480 0 0 {name=xbopp
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 510 1120 510 {lab=ckn}
C {devices/lab_pin.sym} 1120 510 0 0 {name=p101 sig_type=std_logic lab=ckn}
N 1080 480 1080 480 {lab=ckp}
C {devices/lab_pin.sym} 1080 480 0 1 {name=p102 sig_type=std_logic lab=ckp}
N 1120 450 1120 450 {lab=vbuf}
C {devices/lab_pin.sym} 1120 450 0 0 {name=p103 sig_type=std_logic lab=vbuf}
N 1120 480 1120 480 {lab=vbuf}
C {devices/lab_pin.sym} 1120 480 0 0 {name=p104 sig_type=std_logic lab=vbuf}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 600 0 0 {name=xbopn
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 570 20 570 {lab=ckn}
C {devices/lab_pin.sym} 20 570 0 0 {name=p105 sig_type=std_logic lab=ckn}
N -20 600 -20 600 {lab=ckp}
C {devices/lab_pin.sym} -20 600 0 1 {name=p106 sig_type=std_logic lab=ckp}
N 20 630 20 630 {lab=0}
C {devices/lab_pin.sym} 20 630 0 0 {name=p107 sig_type=std_logic lab=0}
N 20 600 20 600 {lab=0}
C {devices/lab_pin.sym} 20 600 0 0 {name=p108 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 600 0 0 {name=xbonp
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 630 240 630 {lab=ckp}
C {devices/lab_pin.sym} 240 630 0 0 {name=p109 sig_type=std_logic lab=ckp}
N 200 600 200 600 {lab=ckn}
C {devices/lab_pin.sym} 200 600 0 1 {name=p110 sig_type=std_logic lab=ckn}
N 240 570 240 570 {lab=vbuf}
C {devices/lab_pin.sym} 240 570 0 0 {name=p111 sig_type=std_logic lab=vbuf}
N 240 600 240 600 {lab=vbuf}
C {devices/lab_pin.sym} 240 600 0 0 {name=p112 sig_type=std_logic lab=vbuf}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 600 0 0 {name=xbonn
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 570 460 570 {lab=ckp}
C {devices/lab_pin.sym} 460 570 0 0 {name=p113 sig_type=std_logic lab=ckp}
N 420 600 420 600 {lab=ckn}
C {devices/lab_pin.sym} 420 600 0 1 {name=p114 sig_type=std_logic lab=ckn}
N 460 630 460 630 {lab=0}
C {devices/lab_pin.sym} 460 630 0 0 {name=p115 sig_type=std_logic lab=0}
N 460 600 460 600 {lab=0}
C {devices/lab_pin.sym} 460 600 0 0 {name=p116 sig_type=std_logic lab=0}
C {devices/res.sym} 660 600 0 0 {name=rgp
value=1000.0
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 660 570 660 570 {lab=vdv}
C {devices/lab_pin.sym} 660 570 0 0 {name=p117 sig_type=std_logic lab=vdv}
N 660 630 660 630 {lab=orp}
C {devices/lab_pin.sym} 660 630 0 0 {name=p118 sig_type=std_logic lab=orp}
C {devices/res.sym} 880 600 0 0 {name=rgn
value=1000.0
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 570 880 570 {lab=vdv}
C {devices/lab_pin.sym} 880 570 0 0 {name=p119 sig_type=std_logic lab=vdv}
N 880 630 880 630 {lab=orn}
C {devices/lab_pin.sym} 880 630 0 0 {name=p120 sig_type=std_logic lab=orn}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 600 0 0 {name=mga
w=5.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 570 1120 570 {lab=orn}
C {devices/lab_pin.sym} 1120 570 0 0 {name=p121 sig_type=std_logic lab=orn}
N 1080 600 1080 600 {lab=q1p}
C {devices/lab_pin.sym} 1080 600 0 1 {name=p122 sig_type=std_logic lab=q1p}
N 1120 630 1120 630 {lab=tg}
C {devices/lab_pin.sym} 1120 630 0 0 {name=p123 sig_type=std_logic lab=tg}
N 1120 600 1120 600 {lab=0}
C {devices/lab_pin.sym} 1120 600 0 0 {name=p124 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 720 0 0 {name=mgb
w=5.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 690 20 690 {lab=orn}
C {devices/lab_pin.sym} 20 690 0 0 {name=p125 sig_type=std_logic lab=orn}
N -20 720 -20 720 {lab=q2p}
C {devices/lab_pin.sym} -20 720 0 1 {name=p126 sig_type=std_logic lab=q2p}
N 20 750 20 750 {lab=tg}
C {devices/lab_pin.sym} 20 750 0 0 {name=p127 sig_type=std_logic lab=tg}
N 20 720 20 720 {lab=0}
C {devices/lab_pin.sym} 20 720 0 0 {name=p128 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 720 0 0 {name=mgr
w=5.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 690 240 690 {lab=orp}
C {devices/lab_pin.sym} 240 690 0 0 {name=p129 sig_type=std_logic lab=orp}
N 200 720 200 720 {lab=vref}
C {devices/lab_pin.sym} 200 720 0 1 {name=p130 sig_type=std_logic lab=vref}
N 240 750 240 750 {lab=tg}
C {devices/lab_pin.sym} 240 750 0 0 {name=p131 sig_type=std_logic lab=tg}
N 240 720 240 720 {lab=0}
C {devices/lab_pin.sym} 240 720 0 0 {name=p132 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 720 0 0 {name=mtg
w=15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 690 460 690 {lab=tg}
C {devices/lab_pin.sym} 460 690 0 0 {name=p133 sig_type=std_logic lab=tg}
N 420 720 420 720 {lab=nb_lo}
C {devices/lab_pin.sym} 420 720 0 1 {name=p134 sig_type=std_logic lab=nb_lo}
N 460 750 460 750 {lab=0}
C {devices/lab_pin.sym} 460 750 0 0 {name=p135 sig_type=std_logic lab=0}
N 460 720 460 720 {lab=0}
C {devices/lab_pin.sym} 460 720 0 0 {name=p136 sig_type=std_logic lab=0}
C {devices/res.sym} 660 720 0 0 {name=rlamp
value=1000.0
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 660 690 660 690 {lab=vdv}
C {devices/lab_pin.sym} 660 690 0 0 {name=p137 sig_type=std_logic lab=vdv}
N 660 750 660 750 {lab=map}
C {devices/lab_pin.sym} 660 750 0 0 {name=p138 sig_type=std_logic lab=map}
C {devices/res.sym} 880 720 0 0 {name=rlamn
value=1000.0
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 690 880 690 {lab=vdv}
C {devices/lab_pin.sym} 880 690 0 0 {name=p139 sig_type=std_logic lab=vdv}
N 880 750 880 750 {lab=man}
C {devices/lab_pin.sym} 880 750 0 0 {name=p140 sig_type=std_logic lab=man}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 720 0 0 {name=mam1
w=5.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 690 1120 690 {lab=man}
C {devices/lab_pin.sym} 1120 690 0 0 {name=p141 sig_type=std_logic lab=man}
N 1080 720 1080 720 {lab=orn}
C {devices/lab_pin.sym} 1080 720 0 1 {name=p142 sig_type=std_logic lab=orn}
N 1120 750 1120 750 {lab=s1am}
C {devices/lab_pin.sym} 1120 750 0 0 {name=p143 sig_type=std_logic lab=s1am}
N 1120 720 1120 720 {lab=0}
C {devices/lab_pin.sym} 1120 720 0 0 {name=p144 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 840 0 0 {name=mam2
w=5.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 810 20 810 {lab=map}
C {devices/lab_pin.sym} 20 810 0 0 {name=p145 sig_type=std_logic lab=map}
N -20 840 -20 840 {lab=orp}
C {devices/lab_pin.sym} -20 840 0 1 {name=p146 sig_type=std_logic lab=orp}
N 20 870 20 870 {lab=s1am}
C {devices/lab_pin.sym} 20 870 0 0 {name=p147 sig_type=std_logic lab=s1am}
N 20 840 20 840 {lab=0}
C {devices/lab_pin.sym} 20 840 0 0 {name=p148 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 840 0 0 {name=mam3
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 810 240 810 {lab=man}
C {devices/lab_pin.sym} 240 810 0 0 {name=p149 sig_type=std_logic lab=man}
N 200 840 200 840 {lab=map}
C {devices/lab_pin.sym} 200 840 0 1 {name=p150 sig_type=std_logic lab=map}
N 240 870 240 870 {lab=s2am}
C {devices/lab_pin.sym} 240 870 0 0 {name=p151 sig_type=std_logic lab=s2am}
N 240 840 240 840 {lab=0}
C {devices/lab_pin.sym} 240 840 0 0 {name=p152 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 840 0 0 {name=mam4
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 810 460 810 {lab=map}
C {devices/lab_pin.sym} 460 810 0 0 {name=p153 sig_type=std_logic lab=map}
N 420 840 420 840 {lab=man}
C {devices/lab_pin.sym} 420 840 0 1 {name=p154 sig_type=std_logic lab=man}
N 460 870 460 870 {lab=s2am}
C {devices/lab_pin.sym} 460 870 0 0 {name=p155 sig_type=std_logic lab=s2am}
N 460 840 460 840 {lab=0}
C {devices/lab_pin.sym} 460 840 0 0 {name=p156 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 840 0 0 {name=mam5
w=5.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 810 680 810 {lab=s1am}
C {devices/lab_pin.sym} 680 810 0 0 {name=p157 sig_type=std_logic lab=s1am}
N 640 840 640 840 {lab=ckp}
C {devices/lab_pin.sym} 640 840 0 1 {name=p158 sig_type=std_logic lab=ckp}
N 680 870 680 870 {lab=tam}
C {devices/lab_pin.sym} 680 870 0 0 {name=p159 sig_type=std_logic lab=tam}
N 680 840 680 840 {lab=0}
C {devices/lab_pin.sym} 680 840 0 0 {name=p160 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 840 0 0 {name=mam6
w=5.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 810 900 810 {lab=s2am}
C {devices/lab_pin.sym} 900 810 0 0 {name=p161 sig_type=std_logic lab=s2am}
N 860 840 860 840 {lab=ckn}
C {devices/lab_pin.sym} 860 840 0 1 {name=p162 sig_type=std_logic lab=ckn}
N 900 870 900 870 {lab=tam}
C {devices/lab_pin.sym} 900 870 0 0 {name=p163 sig_type=std_logic lab=tam}
N 900 840 900 840 {lab=0}
C {devices/lab_pin.sym} 900 840 0 0 {name=p164 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 840 0 0 {name=mtam
w=15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 810 1120 810 {lab=tam}
C {devices/lab_pin.sym} 1120 810 0 0 {name=p165 sig_type=std_logic lab=tam}
N 1080 840 1080 840 {lab=nb_lo}
C {devices/lab_pin.sym} 1080 840 0 1 {name=p166 sig_type=std_logic lab=nb_lo}
N 1120 870 1120 870 {lab=0}
C {devices/lab_pin.sym} 1120 870 0 0 {name=p167 sig_type=std_logic lab=0}
N 1120 840 1120 840 {lab=0}
C {devices/lab_pin.sym} 1120 840 0 0 {name=p168 sig_type=std_logic lab=0}
C {devices/res.sym} 0 960 0 0 {name=rlasp
value=1000.0
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 0 930 0 930 {lab=vdv}
C {devices/lab_pin.sym} 0 930 0 0 {name=p169 sig_type=std_logic lab=vdv}
N 0 990 0 990 {lab=q1p}
C {devices/lab_pin.sym} 0 990 0 0 {name=p170 sig_type=std_logic lab=q1p}
C {devices/res.sym} 220 960 0 0 {name=rlasn
value=1000.0
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 930 220 930 {lab=vdv}
C {devices/lab_pin.sym} 220 930 0 0 {name=p171 sig_type=std_logic lab=vdv}
N 220 990 220 990 {lab=q1n}
C {devices/lab_pin.sym} 220 990 0 0 {name=p172 sig_type=std_logic lab=q1n}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 960 0 0 {name=mas1
w=5.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 930 460 930 {lab=q1n}
C {devices/lab_pin.sym} 460 930 0 0 {name=p173 sig_type=std_logic lab=q1n}
N 420 960 420 960 {lab=map}
C {devices/lab_pin.sym} 420 960 0 1 {name=p174 sig_type=std_logic lab=map}
N 460 990 460 990 {lab=s1as}
C {devices/lab_pin.sym} 460 990 0 0 {name=p175 sig_type=std_logic lab=s1as}
N 460 960 460 960 {lab=0}
C {devices/lab_pin.sym} 460 960 0 0 {name=p176 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 960 0 0 {name=mas2
w=5.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 930 680 930 {lab=q1p}
C {devices/lab_pin.sym} 680 930 0 0 {name=p177 sig_type=std_logic lab=q1p}
N 640 960 640 960 {lab=man}
C {devices/lab_pin.sym} 640 960 0 1 {name=p178 sig_type=std_logic lab=man}
N 680 990 680 990 {lab=s1as}
C {devices/lab_pin.sym} 680 990 0 0 {name=p179 sig_type=std_logic lab=s1as}
N 680 960 680 960 {lab=0}
C {devices/lab_pin.sym} 680 960 0 0 {name=p180 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 960 0 0 {name=mas3
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 930 900 930 {lab=q1n}
C {devices/lab_pin.sym} 900 930 0 0 {name=p181 sig_type=std_logic lab=q1n}
N 860 960 860 960 {lab=q1p}
C {devices/lab_pin.sym} 860 960 0 1 {name=p182 sig_type=std_logic lab=q1p}
N 900 990 900 990 {lab=s2as}
C {devices/lab_pin.sym} 900 990 0 0 {name=p183 sig_type=std_logic lab=s2as}
N 900 960 900 960 {lab=0}
C {devices/lab_pin.sym} 900 960 0 0 {name=p184 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 960 0 0 {name=mas4
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 930 1120 930 {lab=q1p}
C {devices/lab_pin.sym} 1120 930 0 0 {name=p185 sig_type=std_logic lab=q1p}
N 1080 960 1080 960 {lab=q1n}
C {devices/lab_pin.sym} 1080 960 0 1 {name=p186 sig_type=std_logic lab=q1n}
N 1120 990 1120 990 {lab=s2as}
C {devices/lab_pin.sym} 1120 990 0 0 {name=p187 sig_type=std_logic lab=s2as}
N 1120 960 1120 960 {lab=0}
C {devices/lab_pin.sym} 1120 960 0 0 {name=p188 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 1080 0 0 {name=mas5
w=5.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 1050 20 1050 {lab=s1as}
C {devices/lab_pin.sym} 20 1050 0 0 {name=p189 sig_type=std_logic lab=s1as}
N -20 1080 -20 1080 {lab=ckn}
C {devices/lab_pin.sym} -20 1080 0 1 {name=p190 sig_type=std_logic lab=ckn}
N 20 1110 20 1110 {lab=tas}
C {devices/lab_pin.sym} 20 1110 0 0 {name=p191 sig_type=std_logic lab=tas}
N 20 1080 20 1080 {lab=0}
C {devices/lab_pin.sym} 20 1080 0 0 {name=p192 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 1080 0 0 {name=mas6
w=5.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 1050 240 1050 {lab=s2as}
C {devices/lab_pin.sym} 240 1050 0 0 {name=p193 sig_type=std_logic lab=s2as}
N 200 1080 200 1080 {lab=ckp}
C {devices/lab_pin.sym} 200 1080 0 1 {name=p194 sig_type=std_logic lab=ckp}
N 240 1110 240 1110 {lab=tas}
C {devices/lab_pin.sym} 240 1110 0 0 {name=p195 sig_type=std_logic lab=tas}
N 240 1080 240 1080 {lab=0}
C {devices/lab_pin.sym} 240 1080 0 0 {name=p196 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 1080 0 0 {name=mtas
w=15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 1050 460 1050 {lab=tas}
C {devices/lab_pin.sym} 460 1050 0 0 {name=p197 sig_type=std_logic lab=tas}
N 420 1080 420 1080 {lab=nb_lo}
C {devices/lab_pin.sym} 420 1080 0 1 {name=p198 sig_type=std_logic lab=nb_lo}
N 460 1110 460 1110 {lab=0}
C {devices/lab_pin.sym} 460 1110 0 0 {name=p199 sig_type=std_logic lab=0}
N 460 1080 460 1080 {lab=0}
C {devices/lab_pin.sym} 460 1080 0 0 {name=p200 sig_type=std_logic lab=0}
C {devices/res.sym} 660 1080 0 0 {name=rlbmp
value=1000.0
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 660 1050 660 1050 {lab=vdv}
C {devices/lab_pin.sym} 660 1050 0 0 {name=p201 sig_type=std_logic lab=vdv}
N 660 1110 660 1110 {lab=mbp}
C {devices/lab_pin.sym} 660 1110 0 0 {name=p202 sig_type=std_logic lab=mbp}
C {devices/res.sym} 880 1080 0 0 {name=rlbmn
value=1000.0
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 1050 880 1050 {lab=vdv}
C {devices/lab_pin.sym} 880 1050 0 0 {name=p203 sig_type=std_logic lab=vdv}
N 880 1110 880 1110 {lab=mbn}
C {devices/lab_pin.sym} 880 1110 0 0 {name=p204 sig_type=std_logic lab=mbn}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 1080 0 0 {name=mbm1
w=5.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 1050 1120 1050 {lab=mbn}
C {devices/lab_pin.sym} 1120 1050 0 0 {name=p205 sig_type=std_logic lab=mbn}
N 1080 1080 1080 1080 {lab=q1p}
C {devices/lab_pin.sym} 1080 1080 0 1 {name=p206 sig_type=std_logic lab=q1p}
N 1120 1110 1120 1110 {lab=s1bm}
C {devices/lab_pin.sym} 1120 1110 0 0 {name=p207 sig_type=std_logic lab=s1bm}
N 1120 1080 1120 1080 {lab=0}
C {devices/lab_pin.sym} 1120 1080 0 0 {name=p208 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 1200 0 0 {name=mbm2
w=5.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 1170 20 1170 {lab=mbp}
C {devices/lab_pin.sym} 20 1170 0 0 {name=p209 sig_type=std_logic lab=mbp}
N -20 1200 -20 1200 {lab=q1n}
C {devices/lab_pin.sym} -20 1200 0 1 {name=p210 sig_type=std_logic lab=q1n}
N 20 1230 20 1230 {lab=s1bm}
C {devices/lab_pin.sym} 20 1230 0 0 {name=p211 sig_type=std_logic lab=s1bm}
N 20 1200 20 1200 {lab=0}
C {devices/lab_pin.sym} 20 1200 0 0 {name=p212 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 1200 0 0 {name=mbm3
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 1170 240 1170 {lab=mbn}
C {devices/lab_pin.sym} 240 1170 0 0 {name=p213 sig_type=std_logic lab=mbn}
N 200 1200 200 1200 {lab=mbp}
C {devices/lab_pin.sym} 200 1200 0 1 {name=p214 sig_type=std_logic lab=mbp}
N 240 1230 240 1230 {lab=s2bm}
C {devices/lab_pin.sym} 240 1230 0 0 {name=p215 sig_type=std_logic lab=s2bm}
N 240 1200 240 1200 {lab=0}
C {devices/lab_pin.sym} 240 1200 0 0 {name=p216 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 1200 0 0 {name=mbm4
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 1170 460 1170 {lab=mbp}
C {devices/lab_pin.sym} 460 1170 0 0 {name=p217 sig_type=std_logic lab=mbp}
N 420 1200 420 1200 {lab=mbn}
C {devices/lab_pin.sym} 420 1200 0 1 {name=p218 sig_type=std_logic lab=mbn}
N 460 1230 460 1230 {lab=s2bm}
C {devices/lab_pin.sym} 460 1230 0 0 {name=p219 sig_type=std_logic lab=s2bm}
N 460 1200 460 1200 {lab=0}
C {devices/lab_pin.sym} 460 1200 0 0 {name=p220 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 1200 0 0 {name=mbm5
w=5.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 1170 680 1170 {lab=s1bm}
C {devices/lab_pin.sym} 680 1170 0 0 {name=p221 sig_type=std_logic lab=s1bm}
N 640 1200 640 1200 {lab=ckp}
C {devices/lab_pin.sym} 640 1200 0 1 {name=p222 sig_type=std_logic lab=ckp}
N 680 1230 680 1230 {lab=tbm}
C {devices/lab_pin.sym} 680 1230 0 0 {name=p223 sig_type=std_logic lab=tbm}
N 680 1200 680 1200 {lab=0}
C {devices/lab_pin.sym} 680 1200 0 0 {name=p224 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 1200 0 0 {name=mbm6
w=5.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 1170 900 1170 {lab=s2bm}
C {devices/lab_pin.sym} 900 1170 0 0 {name=p225 sig_type=std_logic lab=s2bm}
N 860 1200 860 1200 {lab=ckn}
C {devices/lab_pin.sym} 860 1200 0 1 {name=p226 sig_type=std_logic lab=ckn}
N 900 1230 900 1230 {lab=tbm}
C {devices/lab_pin.sym} 900 1230 0 0 {name=p227 sig_type=std_logic lab=tbm}
N 900 1200 900 1200 {lab=0}
C {devices/lab_pin.sym} 900 1200 0 0 {name=p228 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 1200 0 0 {name=mtbm
w=15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 1170 1120 1170 {lab=tbm}
C {devices/lab_pin.sym} 1120 1170 0 0 {name=p229 sig_type=std_logic lab=tbm}
N 1080 1200 1080 1200 {lab=nb_lo}
C {devices/lab_pin.sym} 1080 1200 0 1 {name=p230 sig_type=std_logic lab=nb_lo}
N 1120 1230 1120 1230 {lab=0}
C {devices/lab_pin.sym} 1120 1230 0 0 {name=p231 sig_type=std_logic lab=0}
N 1120 1200 1120 1200 {lab=0}
C {devices/lab_pin.sym} 1120 1200 0 0 {name=p232 sig_type=std_logic lab=0}
C {devices/res.sym} 0 1320 0 0 {name=rlbsp
value=1000.0
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 0 1290 0 1290 {lab=vdv}
C {devices/lab_pin.sym} 0 1290 0 0 {name=p233 sig_type=std_logic lab=vdv}
N 0 1350 0 1350 {lab=q2p}
C {devices/lab_pin.sym} 0 1350 0 0 {name=p234 sig_type=std_logic lab=q2p}
C {devices/res.sym} 220 1320 0 0 {name=rlbsn
value=1000.0
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 1290 220 1290 {lab=vdv}
C {devices/lab_pin.sym} 220 1290 0 0 {name=p235 sig_type=std_logic lab=vdv}
N 220 1350 220 1350 {lab=q2n}
C {devices/lab_pin.sym} 220 1350 0 0 {name=p236 sig_type=std_logic lab=q2n}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 1320 0 0 {name=mbs1
w=5.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 1290 460 1290 {lab=q2n}
C {devices/lab_pin.sym} 460 1290 0 0 {name=p237 sig_type=std_logic lab=q2n}
N 420 1320 420 1320 {lab=mbp}
C {devices/lab_pin.sym} 420 1320 0 1 {name=p238 sig_type=std_logic lab=mbp}
N 460 1350 460 1350 {lab=s1bs}
C {devices/lab_pin.sym} 460 1350 0 0 {name=p239 sig_type=std_logic lab=s1bs}
N 460 1320 460 1320 {lab=0}
C {devices/lab_pin.sym} 460 1320 0 0 {name=p240 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 1320 0 0 {name=mbs2
w=5.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 1290 680 1290 {lab=q2p}
C {devices/lab_pin.sym} 680 1290 0 0 {name=p241 sig_type=std_logic lab=q2p}
N 640 1320 640 1320 {lab=mbn}
C {devices/lab_pin.sym} 640 1320 0 1 {name=p242 sig_type=std_logic lab=mbn}
N 680 1350 680 1350 {lab=s1bs}
C {devices/lab_pin.sym} 680 1350 0 0 {name=p243 sig_type=std_logic lab=s1bs}
N 680 1320 680 1320 {lab=0}
C {devices/lab_pin.sym} 680 1320 0 0 {name=p244 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 1320 0 0 {name=mbs3
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 1290 900 1290 {lab=q2n}
C {devices/lab_pin.sym} 900 1290 0 0 {name=p245 sig_type=std_logic lab=q2n}
N 860 1320 860 1320 {lab=q2p}
C {devices/lab_pin.sym} 860 1320 0 1 {name=p246 sig_type=std_logic lab=q2p}
N 900 1350 900 1350 {lab=s2bs}
C {devices/lab_pin.sym} 900 1350 0 0 {name=p247 sig_type=std_logic lab=s2bs}
N 900 1320 900 1320 {lab=0}
C {devices/lab_pin.sym} 900 1320 0 0 {name=p248 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 1320 0 0 {name=mbs4
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 1290 1120 1290 {lab=q2p}
C {devices/lab_pin.sym} 1120 1290 0 0 {name=p249 sig_type=std_logic lab=q2p}
N 1080 1320 1080 1320 {lab=q2n}
C {devices/lab_pin.sym} 1080 1320 0 1 {name=p250 sig_type=std_logic lab=q2n}
N 1120 1350 1120 1350 {lab=s2bs}
C {devices/lab_pin.sym} 1120 1350 0 0 {name=p251 sig_type=std_logic lab=s2bs}
N 1120 1320 1120 1320 {lab=0}
C {devices/lab_pin.sym} 1120 1320 0 0 {name=p252 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 1440 0 0 {name=mbs5
w=5.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 1410 20 1410 {lab=s1bs}
C {devices/lab_pin.sym} 20 1410 0 0 {name=p253 sig_type=std_logic lab=s1bs}
N -20 1440 -20 1440 {lab=ckn}
C {devices/lab_pin.sym} -20 1440 0 1 {name=p254 sig_type=std_logic lab=ckn}
N 20 1470 20 1470 {lab=tbs}
C {devices/lab_pin.sym} 20 1470 0 0 {name=p255 sig_type=std_logic lab=tbs}
N 20 1440 20 1440 {lab=0}
C {devices/lab_pin.sym} 20 1440 0 0 {name=p256 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 1440 0 0 {name=mbs6
w=5.00u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 1410 240 1410 {lab=s2bs}
C {devices/lab_pin.sym} 240 1410 0 0 {name=p257 sig_type=std_logic lab=s2bs}
N 200 1440 200 1440 {lab=ckp}
C {devices/lab_pin.sym} 200 1440 0 1 {name=p258 sig_type=std_logic lab=ckp}
N 240 1470 240 1470 {lab=tbs}
C {devices/lab_pin.sym} 240 1470 0 0 {name=p259 sig_type=std_logic lab=tbs}
N 240 1440 240 1440 {lab=0}
C {devices/lab_pin.sym} 240 1440 0 0 {name=p260 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 1440 0 0 {name=mtbs
w=15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 1410 460 1410 {lab=tbs}
C {devices/lab_pin.sym} 460 1410 0 0 {name=p261 sig_type=std_logic lab=tbs}
N 420 1440 420 1440 {lab=nb_lo}
C {devices/lab_pin.sym} 420 1440 0 1 {name=p262 sig_type=std_logic lab=nb_lo}
N 460 1470 460 1470 {lab=0}
C {devices/lab_pin.sym} 460 1470 0 0 {name=p263 sig_type=std_logic lab=0}
N 460 1440 460 1440 {lab=0}
C {devices/lab_pin.sym} 460 1440 0 0 {name=p264 sig_type=std_logic lab=0}
C {devices/capa.sym} 660 1440 0 0 {name=ccap
value=50f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 660 1410 660 1410 {lab=q2p}
C {devices/lab_pin.sym} 660 1410 0 0 {name=p265 sig_type=std_logic lab=q2p}
N 660 1470 660 1470 {lab=x_cip}
C {devices/lab_pin.sym} 660 1470 0 0 {name=p266 sig_type=std_logic lab=x_cip}
C {devices/res.sym} 880 1440 0 0 {name=rcap
value=50k
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 1410 880 1410 {lab=x_cip}
C {devices/lab_pin.sym} 880 1410 0 0 {name=p267 sig_type=std_logic lab=x_cip}
N 880 1470 880 1470 {lab=x_o2p}
C {devices/lab_pin.sym} 880 1470 0 0 {name=p268 sig_type=std_logic lab=x_o2p}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 1440 0 0 {name=xcapp
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 1470 1120 1470 {lab=x_o2p}
C {devices/lab_pin.sym} 1120 1470 0 0 {name=p269 sig_type=std_logic lab=x_o2p}
N 1080 1440 1080 1440 {lab=x_cip}
C {devices/lab_pin.sym} 1080 1440 0 1 {name=p270 sig_type=std_logic lab=x_cip}
N 1120 1410 1120 1410 {lab=vcv}
C {devices/lab_pin.sym} 1120 1410 0 0 {name=p271 sig_type=std_logic lab=vcv}
N 1120 1440 1120 1440 {lab=vcv}
C {devices/lab_pin.sym} 1120 1440 0 0 {name=p272 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 1560 0 0 {name=xcapn
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 1530 20 1530 {lab=x_o2p}
C {devices/lab_pin.sym} 20 1530 0 0 {name=p273 sig_type=std_logic lab=x_o2p}
N -20 1560 -20 1560 {lab=x_cip}
C {devices/lab_pin.sym} -20 1560 0 1 {name=p274 sig_type=std_logic lab=x_cip}
N 20 1590 20 1590 {lab=0}
C {devices/lab_pin.sym} 20 1590 0 0 {name=p275 sig_type=std_logic lab=0}
N 20 1560 20 1560 {lab=0}
C {devices/lab_pin.sym} 20 1560 0 0 {name=p276 sig_type=std_logic lab=0}
C {devices/capa.sym} 220 1560 0 0 {name=ccan
value=50f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 220 1530 220 1530 {lab=q2n}
C {devices/lab_pin.sym} 220 1530 0 0 {name=p277 sig_type=std_logic lab=q2n}
N 220 1590 220 1590 {lab=x_cin}
C {devices/lab_pin.sym} 220 1590 0 0 {name=p278 sig_type=std_logic lab=x_cin}
C {devices/res.sym} 440 1560 0 0 {name=rcan
value=50k
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 440 1530 440 1530 {lab=x_cin}
C {devices/lab_pin.sym} 440 1530 0 0 {name=p279 sig_type=std_logic lab=x_cin}
N 440 1590 440 1590 {lab=x_o2n}
C {devices/lab_pin.sym} 440 1590 0 0 {name=p280 sig_type=std_logic lab=x_o2n}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 1560 0 0 {name=xcanp
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 1590 680 1590 {lab=x_o2n}
C {devices/lab_pin.sym} 680 1590 0 0 {name=p281 sig_type=std_logic lab=x_o2n}
N 640 1560 640 1560 {lab=x_cin}
C {devices/lab_pin.sym} 640 1560 0 1 {name=p282 sig_type=std_logic lab=x_cin}
N 680 1530 680 1530 {lab=vcv}
C {devices/lab_pin.sym} 680 1530 0 0 {name=p283 sig_type=std_logic lab=vcv}
N 680 1560 680 1560 {lab=vcv}
C {devices/lab_pin.sym} 680 1560 0 0 {name=p284 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 1560 0 0 {name=xcann
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 1530 900 1530 {lab=x_o2n}
C {devices/lab_pin.sym} 900 1530 0 0 {name=p285 sig_type=std_logic lab=x_o2n}
N 860 1560 860 1560 {lab=x_cin}
C {devices/lab_pin.sym} 860 1560 0 1 {name=p286 sig_type=std_logic lab=x_cin}
N 900 1590 900 1590 {lab=0}
C {devices/lab_pin.sym} 900 1590 0 0 {name=p287 sig_type=std_logic lab=0}
N 900 1560 900 1560 {lab=0}
C {devices/lab_pin.sym} 900 1560 0 0 {name=p288 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 1560 0 0 {name=xcxpp
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 1590 1120 1590 {lab=x_o2n}
C {devices/lab_pin.sym} 1120 1590 0 0 {name=p289 sig_type=std_logic lab=x_o2n}
N 1080 1560 1080 1560 {lab=x_o2p}
C {devices/lab_pin.sym} 1080 1560 0 1 {name=p290 sig_type=std_logic lab=x_o2p}
N 1120 1530 1120 1530 {lab=vcv}
C {devices/lab_pin.sym} 1120 1530 0 0 {name=p291 sig_type=std_logic lab=vcv}
N 1120 1560 1120 1560 {lab=vcv}
C {devices/lab_pin.sym} 1120 1560 0 0 {name=p292 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 1680 0 0 {name=xcxpn
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 1650 20 1650 {lab=x_o2n}
C {devices/lab_pin.sym} 20 1650 0 0 {name=p293 sig_type=std_logic lab=x_o2n}
N -20 1680 -20 1680 {lab=x_o2p}
C {devices/lab_pin.sym} -20 1680 0 1 {name=p294 sig_type=std_logic lab=x_o2p}
N 20 1710 20 1710 {lab=0}
C {devices/lab_pin.sym} 20 1710 0 0 {name=p295 sig_type=std_logic lab=0}
N 20 1680 20 1680 {lab=0}
C {devices/lab_pin.sym} 20 1680 0 0 {name=p296 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 1680 0 0 {name=xcxnp
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 1710 240 1710 {lab=x_o2p}
C {devices/lab_pin.sym} 240 1710 0 0 {name=p297 sig_type=std_logic lab=x_o2p}
N 200 1680 200 1680 {lab=x_o2n}
C {devices/lab_pin.sym} 200 1680 0 1 {name=p298 sig_type=std_logic lab=x_o2n}
N 240 1650 240 1650 {lab=vcv}
C {devices/lab_pin.sym} 240 1650 0 0 {name=p299 sig_type=std_logic lab=vcv}
N 240 1680 240 1680 {lab=vcv}
C {devices/lab_pin.sym} 240 1680 0 0 {name=p300 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 1680 0 0 {name=xcxnn
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 1650 460 1650 {lab=x_o2p}
C {devices/lab_pin.sym} 460 1650 0 0 {name=p301 sig_type=std_logic lab=x_o2p}
N 420 1680 420 1680 {lab=x_o2n}
C {devices/lab_pin.sym} 420 1680 0 1 {name=p302 sig_type=std_logic lab=x_o2n}
N 460 1710 460 1710 {lab=0}
C {devices/lab_pin.sym} 460 1710 0 0 {name=p303 sig_type=std_logic lab=0}
N 460 1680 460 1680 {lab=0}
C {devices/lab_pin.sym} 460 1680 0 0 {name=p304 sig_type=std_logic lab=0}
C {devices/capa.sym} 660 1680 0 0 {name=ccb
value=50f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 660 1650 660 1650 {lab=x_o2p}
C {devices/lab_pin.sym} 660 1650 0 0 {name=p305 sig_type=std_logic lab=x_o2p}
N 660 1710 660 1710 {lab=x_cbi}
C {devices/lab_pin.sym} 660 1710 0 0 {name=p306 sig_type=std_logic lab=x_cbi}
C {devices/res.sym} 880 1680 0 0 {name=rcb
value=50k
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 1650 880 1650 {lab=x_cbi}
C {devices/lab_pin.sym} 880 1650 0 0 {name=p307 sig_type=std_logic lab=x_cbi}
N 880 1710 880 1710 {lab=x_cy}
C {devices/lab_pin.sym} 880 1710 0 0 {name=p308 sig_type=std_logic lab=x_cy}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 1680 0 0 {name=xcbp
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 1710 1120 1710 {lab=x_cy}
C {devices/lab_pin.sym} 1120 1710 0 0 {name=p309 sig_type=std_logic lab=x_cy}
N 1080 1680 1080 1680 {lab=x_cbi}
C {devices/lab_pin.sym} 1080 1680 0 1 {name=p310 sig_type=std_logic lab=x_cbi}
N 1120 1650 1120 1650 {lab=vcv}
C {devices/lab_pin.sym} 1120 1650 0 0 {name=p311 sig_type=std_logic lab=vcv}
N 1120 1680 1120 1680 {lab=vcv}
C {devices/lab_pin.sym} 1120 1680 0 0 {name=p312 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 1800 0 0 {name=xcbn
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 1770 20 1770 {lab=x_cy}
C {devices/lab_pin.sym} 20 1770 0 0 {name=p313 sig_type=std_logic lab=x_cy}
N -20 1800 -20 1800 {lab=x_cbi}
C {devices/lab_pin.sym} -20 1800 0 1 {name=p314 sig_type=std_logic lab=x_cbi}
N 20 1830 20 1830 {lab=0}
C {devices/lab_pin.sym} 20 1830 0 0 {name=p315 sig_type=std_logic lab=0}
N 20 1800 20 1800 {lab=0}
C {devices/lab_pin.sym} 20 1800 0 0 {name=p316 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 1800 0 0 {name=xcv3p
w=6.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 1830 240 1830 {lab=x_cz}
C {devices/lab_pin.sym} 240 1830 0 0 {name=p317 sig_type=std_logic lab=x_cz}
N 200 1800 200 1800 {lab=x_cy}
C {devices/lab_pin.sym} 200 1800 0 1 {name=p318 sig_type=std_logic lab=x_cy}
N 240 1770 240 1770 {lab=vcv}
C {devices/lab_pin.sym} 240 1770 0 0 {name=p319 sig_type=std_logic lab=vcv}
N 240 1800 240 1800 {lab=vcv}
C {devices/lab_pin.sym} 240 1800 0 0 {name=p320 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 1800 0 0 {name=xcv3n
w=3.0u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 1770 460 1770 {lab=x_cz}
C {devices/lab_pin.sym} 460 1770 0 0 {name=p321 sig_type=std_logic lab=x_cz}
N 420 1800 420 1800 {lab=x_cy}
C {devices/lab_pin.sym} 420 1800 0 1 {name=p322 sig_type=std_logic lab=x_cy}
N 460 1830 460 1830 {lab=0}
C {devices/lab_pin.sym} 460 1830 0 0 {name=p323 sig_type=std_logic lab=0}
N 460 1800 460 1800 {lab=0}
C {devices/lab_pin.sym} 460 1800 0 0 {name=p324 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 1800 0 0 {name=xcv4p
w=18.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 1830 680 1830 {lab=x_clk}
C {devices/lab_pin.sym} 680 1830 0 0 {name=p325 sig_type=std_logic lab=x_clk}
N 640 1800 640 1800 {lab=x_cz}
C {devices/lab_pin.sym} 640 1800 0 1 {name=p326 sig_type=std_logic lab=x_cz}
N 680 1770 680 1770 {lab=vcv}
C {devices/lab_pin.sym} 680 1770 0 0 {name=p327 sig_type=std_logic lab=vcv}
N 680 1800 680 1800 {lab=vcv}
C {devices/lab_pin.sym} 680 1800 0 0 {name=p328 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 1800 0 0 {name=xcv4n
w=9.0u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 1770 900 1770 {lab=x_clk}
C {devices/lab_pin.sym} 900 1770 0 0 {name=p329 sig_type=std_logic lab=x_clk}
N 860 1800 860 1800 {lab=x_cz}
C {devices/lab_pin.sym} 860 1800 0 1 {name=p330 sig_type=std_logic lab=x_cz}
N 900 1830 900 1830 {lab=0}
C {devices/lab_pin.sym} 900 1830 0 0 {name=p331 sig_type=std_logic lab=0}
N 900 1800 900 1800 {lab=0}
C {devices/lab_pin.sym} 900 1800 0 0 {name=p332 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 1800 0 0 {name=xf1p1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 1830 1120 1830 {lab=x_f1_x1}
C {devices/lab_pin.sym} 1120 1830 0 0 {name=p333 sig_type=std_logic lab=x_f1_x1}
N 1080 1800 1080 1800 {lab=x_q4}
C {devices/lab_pin.sym} 1080 1800 0 1 {name=p334 sig_type=std_logic lab=x_q4}
N 1120 1770 1120 1770 {lab=vdg}
C {devices/lab_pin.sym} 1120 1770 0 0 {name=p335 sig_type=std_logic lab=vdg}
N 1120 1800 1120 1800 {lab=vdg}
C {devices/lab_pin.sym} 1120 1800 0 0 {name=p336 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 1920 0 0 {name=xf1p2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 1950 20 1950 {lab=x_f1_a}
C {devices/lab_pin.sym} 20 1950 0 0 {name=p337 sig_type=std_logic lab=x_f1_a}
N -20 1920 -20 1920 {lab=x_clk}
C {devices/lab_pin.sym} -20 1920 0 1 {name=p338 sig_type=std_logic lab=x_clk}
N 20 1890 20 1890 {lab=x_f1_x1}
C {devices/lab_pin.sym} 20 1890 0 0 {name=p339 sig_type=std_logic lab=x_f1_x1}
N 20 1920 20 1920 {lab=vdg}
C {devices/lab_pin.sym} 20 1920 0 0 {name=p340 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 1920 0 0 {name=xf1n1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 1890 240 1890 {lab=x_f1_a}
C {devices/lab_pin.sym} 240 1890 0 0 {name=p341 sig_type=std_logic lab=x_f1_a}
N 200 1920 200 1920 {lab=x_q4}
C {devices/lab_pin.sym} 200 1920 0 1 {name=p342 sig_type=std_logic lab=x_q4}
N 240 1950 240 1950 {lab=0}
C {devices/lab_pin.sym} 240 1950 0 0 {name=p343 sig_type=std_logic lab=0}
N 240 1920 240 1920 {lab=0}
C {devices/lab_pin.sym} 240 1920 0 0 {name=p344 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 1920 0 0 {name=xf1p3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 1950 460 1950 {lab=x_f1_b}
C {devices/lab_pin.sym} 460 1950 0 0 {name=p345 sig_type=std_logic lab=x_f1_b}
N 420 1920 420 1920 {lab=x_clk}
C {devices/lab_pin.sym} 420 1920 0 1 {name=p346 sig_type=std_logic lab=x_clk}
N 460 1890 460 1890 {lab=vdg}
C {devices/lab_pin.sym} 460 1890 0 0 {name=p347 sig_type=std_logic lab=vdg}
N 460 1920 460 1920 {lab=vdg}
C {devices/lab_pin.sym} 460 1920 0 0 {name=p348 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 1920 0 0 {name=xf1n2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 1890 680 1890 {lab=x_f1_b}
C {devices/lab_pin.sym} 680 1890 0 0 {name=p349 sig_type=std_logic lab=x_f1_b}
N 640 1920 640 1920 {lab=x_f1_a}
C {devices/lab_pin.sym} 640 1920 0 1 {name=p350 sig_type=std_logic lab=x_f1_a}
N 680 1950 680 1950 {lab=x_f1_x2}
C {devices/lab_pin.sym} 680 1950 0 0 {name=p351 sig_type=std_logic lab=x_f1_x2}
N 680 1920 680 1920 {lab=0}
C {devices/lab_pin.sym} 680 1920 0 0 {name=p352 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 1920 0 0 {name=xf1n3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 1890 900 1890 {lab=x_f1_x2}
C {devices/lab_pin.sym} 900 1890 0 0 {name=p353 sig_type=std_logic lab=x_f1_x2}
N 860 1920 860 1920 {lab=x_clk}
C {devices/lab_pin.sym} 860 1920 0 1 {name=p354 sig_type=std_logic lab=x_clk}
N 900 1950 900 1950 {lab=0}
C {devices/lab_pin.sym} 900 1950 0 0 {name=p355 sig_type=std_logic lab=0}
N 900 1920 900 1920 {lab=0}
C {devices/lab_pin.sym} 900 1920 0 0 {name=p356 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 1920 0 0 {name=xf1p4
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 1950 1120 1950 {lab=x_q1}
C {devices/lab_pin.sym} 1120 1950 0 0 {name=p357 sig_type=std_logic lab=x_q1}
N 1080 1920 1080 1920 {lab=x_f1_b}
C {devices/lab_pin.sym} 1080 1920 0 1 {name=p358 sig_type=std_logic lab=x_f1_b}
N 1120 1890 1120 1890 {lab=vdg}
C {devices/lab_pin.sym} 1120 1890 0 0 {name=p359 sig_type=std_logic lab=vdg}
N 1120 1920 1120 1920 {lab=vdg}
C {devices/lab_pin.sym} 1120 1920 0 0 {name=p360 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 2040 0 0 {name=xf1n4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 2010 20 2010 {lab=x_q1}
C {devices/lab_pin.sym} 20 2010 0 0 {name=p361 sig_type=std_logic lab=x_q1}
N -20 2040 -20 2040 {lab=x_clk}
C {devices/lab_pin.sym} -20 2040 0 1 {name=p362 sig_type=std_logic lab=x_clk}
N 20 2070 20 2070 {lab=x_f1_x3}
C {devices/lab_pin.sym} 20 2070 0 0 {name=p363 sig_type=std_logic lab=x_f1_x3}
N 20 2040 20 2040 {lab=0}
C {devices/lab_pin.sym} 20 2040 0 0 {name=p364 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 2040 0 0 {name=xf1n5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 2010 240 2010 {lab=x_f1_x3}
C {devices/lab_pin.sym} 240 2010 0 0 {name=p365 sig_type=std_logic lab=x_f1_x3}
N 200 2040 200 2040 {lab=x_f1_b}
C {devices/lab_pin.sym} 200 2040 0 1 {name=p366 sig_type=std_logic lab=x_f1_b}
N 240 2070 240 2070 {lab=0}
C {devices/lab_pin.sym} 240 2070 0 0 {name=p367 sig_type=std_logic lab=0}
N 240 2040 240 2040 {lab=0}
C {devices/lab_pin.sym} 240 2040 0 0 {name=p368 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 2040 0 0 {name=xi2p
w=1.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 2070 460 2070 {lab=x_d2}
C {devices/lab_pin.sym} 460 2070 0 0 {name=p369 sig_type=std_logic lab=x_d2}
N 420 2040 420 2040 {lab=x_q1}
C {devices/lab_pin.sym} 420 2040 0 1 {name=p370 sig_type=std_logic lab=x_q1}
N 460 2010 460 2010 {lab=vdg}
C {devices/lab_pin.sym} 460 2010 0 0 {name=p371 sig_type=std_logic lab=vdg}
N 460 2040 460 2040 {lab=vdg}
C {devices/lab_pin.sym} 460 2040 0 0 {name=p372 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 2040 0 0 {name=xi2n
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 2010 680 2010 {lab=x_d2}
C {devices/lab_pin.sym} 680 2010 0 0 {name=p373 sig_type=std_logic lab=x_d2}
N 640 2040 640 2040 {lab=x_q1}
C {devices/lab_pin.sym} 640 2040 0 1 {name=p374 sig_type=std_logic lab=x_q1}
N 680 2070 680 2070 {lab=0}
C {devices/lab_pin.sym} 680 2070 0 0 {name=p375 sig_type=std_logic lab=0}
N 680 2040 680 2040 {lab=0}
C {devices/lab_pin.sym} 680 2040 0 0 {name=p376 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 2040 0 0 {name=xf2p1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 2070 900 2070 {lab=x_f2_x1}
C {devices/lab_pin.sym} 900 2070 0 0 {name=p377 sig_type=std_logic lab=x_f2_x1}
N 860 2040 860 2040 {lab=x_d2}
C {devices/lab_pin.sym} 860 2040 0 1 {name=p378 sig_type=std_logic lab=x_d2}
N 900 2010 900 2010 {lab=vdg}
C {devices/lab_pin.sym} 900 2010 0 0 {name=p379 sig_type=std_logic lab=vdg}
N 900 2040 900 2040 {lab=vdg}
C {devices/lab_pin.sym} 900 2040 0 0 {name=p380 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 2040 0 0 {name=xf2p2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 2070 1120 2070 {lab=x_f2_a}
C {devices/lab_pin.sym} 1120 2070 0 0 {name=p381 sig_type=std_logic lab=x_f2_a}
N 1080 2040 1080 2040 {lab=x_clk}
C {devices/lab_pin.sym} 1080 2040 0 1 {name=p382 sig_type=std_logic lab=x_clk}
N 1120 2010 1120 2010 {lab=x_f2_x1}
C {devices/lab_pin.sym} 1120 2010 0 0 {name=p383 sig_type=std_logic lab=x_f2_x1}
N 1120 2040 1120 2040 {lab=vdg}
C {devices/lab_pin.sym} 1120 2040 0 0 {name=p384 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 2160 0 0 {name=xf2n1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 2130 20 2130 {lab=x_f2_a}
C {devices/lab_pin.sym} 20 2130 0 0 {name=p385 sig_type=std_logic lab=x_f2_a}
N -20 2160 -20 2160 {lab=x_d2}
C {devices/lab_pin.sym} -20 2160 0 1 {name=p386 sig_type=std_logic lab=x_d2}
N 20 2190 20 2190 {lab=0}
C {devices/lab_pin.sym} 20 2190 0 0 {name=p387 sig_type=std_logic lab=0}
N 20 2160 20 2160 {lab=0}
C {devices/lab_pin.sym} 20 2160 0 0 {name=p388 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 2160 0 0 {name=xf2p3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 2190 240 2190 {lab=x_f2_b}
C {devices/lab_pin.sym} 240 2190 0 0 {name=p389 sig_type=std_logic lab=x_f2_b}
N 200 2160 200 2160 {lab=x_clk}
C {devices/lab_pin.sym} 200 2160 0 1 {name=p390 sig_type=std_logic lab=x_clk}
N 240 2130 240 2130 {lab=vdg}
C {devices/lab_pin.sym} 240 2130 0 0 {name=p391 sig_type=std_logic lab=vdg}
N 240 2160 240 2160 {lab=vdg}
C {devices/lab_pin.sym} 240 2160 0 0 {name=p392 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 2160 0 0 {name=xf2n2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 2130 460 2130 {lab=x_f2_b}
C {devices/lab_pin.sym} 460 2130 0 0 {name=p393 sig_type=std_logic lab=x_f2_b}
N 420 2160 420 2160 {lab=x_f2_a}
C {devices/lab_pin.sym} 420 2160 0 1 {name=p394 sig_type=std_logic lab=x_f2_a}
N 460 2190 460 2190 {lab=x_f2_x2}
C {devices/lab_pin.sym} 460 2190 0 0 {name=p395 sig_type=std_logic lab=x_f2_x2}
N 460 2160 460 2160 {lab=0}
C {devices/lab_pin.sym} 460 2160 0 0 {name=p396 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 2160 0 0 {name=xf2n3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 2130 680 2130 {lab=x_f2_x2}
C {devices/lab_pin.sym} 680 2130 0 0 {name=p397 sig_type=std_logic lab=x_f2_x2}
N 640 2160 640 2160 {lab=x_clk}
C {devices/lab_pin.sym} 640 2160 0 1 {name=p398 sig_type=std_logic lab=x_clk}
N 680 2190 680 2190 {lab=0}
C {devices/lab_pin.sym} 680 2190 0 0 {name=p399 sig_type=std_logic lab=0}
N 680 2160 680 2160 {lab=0}
C {devices/lab_pin.sym} 680 2160 0 0 {name=p400 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 2160 0 0 {name=xf2p4
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 2190 900 2190 {lab=x_q2}
C {devices/lab_pin.sym} 900 2190 0 0 {name=p401 sig_type=std_logic lab=x_q2}
N 860 2160 860 2160 {lab=x_f2_b}
C {devices/lab_pin.sym} 860 2160 0 1 {name=p402 sig_type=std_logic lab=x_f2_b}
N 900 2130 900 2130 {lab=vdg}
C {devices/lab_pin.sym} 900 2130 0 0 {name=p403 sig_type=std_logic lab=vdg}
N 900 2160 900 2160 {lab=vdg}
C {devices/lab_pin.sym} 900 2160 0 0 {name=p404 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 2160 0 0 {name=xf2n4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 2130 1120 2130 {lab=x_q2}
C {devices/lab_pin.sym} 1120 2130 0 0 {name=p405 sig_type=std_logic lab=x_q2}
N 1080 2160 1080 2160 {lab=x_clk}
C {devices/lab_pin.sym} 1080 2160 0 1 {name=p406 sig_type=std_logic lab=x_clk}
N 1120 2190 1120 2190 {lab=x_f2_x3}
C {devices/lab_pin.sym} 1120 2190 0 0 {name=p407 sig_type=std_logic lab=x_f2_x3}
N 1120 2160 1120 2160 {lab=0}
C {devices/lab_pin.sym} 1120 2160 0 0 {name=p408 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 2280 0 0 {name=xf2n5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 2250 20 2250 {lab=x_f2_x3}
C {devices/lab_pin.sym} 20 2250 0 0 {name=p409 sig_type=std_logic lab=x_f2_x3}
N -20 2280 -20 2280 {lab=x_f2_b}
C {devices/lab_pin.sym} -20 2280 0 1 {name=p410 sig_type=std_logic lab=x_f2_b}
N 20 2310 20 2310 {lab=0}
C {devices/lab_pin.sym} 20 2310 0 0 {name=p411 sig_type=std_logic lab=0}
N 20 2280 20 2280 {lab=0}
C {devices/lab_pin.sym} 20 2280 0 0 {name=p412 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 2280 0 0 {name=xi3p
w=1.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 2310 240 2310 {lab=x_d3}
C {devices/lab_pin.sym} 240 2310 0 0 {name=p413 sig_type=std_logic lab=x_d3}
N 200 2280 200 2280 {lab=x_q2}
C {devices/lab_pin.sym} 200 2280 0 1 {name=p414 sig_type=std_logic lab=x_q2}
N 240 2250 240 2250 {lab=vdg}
C {devices/lab_pin.sym} 240 2250 0 0 {name=p415 sig_type=std_logic lab=vdg}
N 240 2280 240 2280 {lab=vdg}
C {devices/lab_pin.sym} 240 2280 0 0 {name=p416 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 2280 0 0 {name=xi3n
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 2250 460 2250 {lab=x_d3}
C {devices/lab_pin.sym} 460 2250 0 0 {name=p417 sig_type=std_logic lab=x_d3}
N 420 2280 420 2280 {lab=x_q2}
C {devices/lab_pin.sym} 420 2280 0 1 {name=p418 sig_type=std_logic lab=x_q2}
N 460 2310 460 2310 {lab=0}
C {devices/lab_pin.sym} 460 2310 0 0 {name=p419 sig_type=std_logic lab=0}
N 460 2280 460 2280 {lab=0}
C {devices/lab_pin.sym} 460 2280 0 0 {name=p420 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 2280 0 0 {name=xf3p1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 2310 680 2310 {lab=x_f3_x1}
C {devices/lab_pin.sym} 680 2310 0 0 {name=p421 sig_type=std_logic lab=x_f3_x1}
N 640 2280 640 2280 {lab=x_d3}
C {devices/lab_pin.sym} 640 2280 0 1 {name=p422 sig_type=std_logic lab=x_d3}
N 680 2250 680 2250 {lab=vdg}
C {devices/lab_pin.sym} 680 2250 0 0 {name=p423 sig_type=std_logic lab=vdg}
N 680 2280 680 2280 {lab=vdg}
C {devices/lab_pin.sym} 680 2280 0 0 {name=p424 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 2280 0 0 {name=xf3p2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 2310 900 2310 {lab=x_f3_a}
C {devices/lab_pin.sym} 900 2310 0 0 {name=p425 sig_type=std_logic lab=x_f3_a}
N 860 2280 860 2280 {lab=x_clk}
C {devices/lab_pin.sym} 860 2280 0 1 {name=p426 sig_type=std_logic lab=x_clk}
N 900 2250 900 2250 {lab=x_f3_x1}
C {devices/lab_pin.sym} 900 2250 0 0 {name=p427 sig_type=std_logic lab=x_f3_x1}
N 900 2280 900 2280 {lab=vdg}
C {devices/lab_pin.sym} 900 2280 0 0 {name=p428 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 2280 0 0 {name=xf3n1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 2250 1120 2250 {lab=x_f3_a}
C {devices/lab_pin.sym} 1120 2250 0 0 {name=p429 sig_type=std_logic lab=x_f3_a}
N 1080 2280 1080 2280 {lab=x_d3}
C {devices/lab_pin.sym} 1080 2280 0 1 {name=p430 sig_type=std_logic lab=x_d3}
N 1120 2310 1120 2310 {lab=0}
C {devices/lab_pin.sym} 1120 2310 0 0 {name=p431 sig_type=std_logic lab=0}
N 1120 2280 1120 2280 {lab=0}
C {devices/lab_pin.sym} 1120 2280 0 0 {name=p432 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 2400 0 0 {name=xf3p3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 2430 20 2430 {lab=x_f3_b}
C {devices/lab_pin.sym} 20 2430 0 0 {name=p433 sig_type=std_logic lab=x_f3_b}
N -20 2400 -20 2400 {lab=x_clk}
C {devices/lab_pin.sym} -20 2400 0 1 {name=p434 sig_type=std_logic lab=x_clk}
N 20 2370 20 2370 {lab=vdg}
C {devices/lab_pin.sym} 20 2370 0 0 {name=p435 sig_type=std_logic lab=vdg}
N 20 2400 20 2400 {lab=vdg}
C {devices/lab_pin.sym} 20 2400 0 0 {name=p436 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 2400 0 0 {name=xf3n2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 2370 240 2370 {lab=x_f3_b}
C {devices/lab_pin.sym} 240 2370 0 0 {name=p437 sig_type=std_logic lab=x_f3_b}
N 200 2400 200 2400 {lab=x_f3_a}
C {devices/lab_pin.sym} 200 2400 0 1 {name=p438 sig_type=std_logic lab=x_f3_a}
N 240 2430 240 2430 {lab=x_f3_x2}
C {devices/lab_pin.sym} 240 2430 0 0 {name=p439 sig_type=std_logic lab=x_f3_x2}
N 240 2400 240 2400 {lab=0}
C {devices/lab_pin.sym} 240 2400 0 0 {name=p440 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 2400 0 0 {name=xf3n3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 2370 460 2370 {lab=x_f3_x2}
C {devices/lab_pin.sym} 460 2370 0 0 {name=p441 sig_type=std_logic lab=x_f3_x2}
N 420 2400 420 2400 {lab=x_clk}
C {devices/lab_pin.sym} 420 2400 0 1 {name=p442 sig_type=std_logic lab=x_clk}
N 460 2430 460 2430 {lab=0}
C {devices/lab_pin.sym} 460 2430 0 0 {name=p443 sig_type=std_logic lab=0}
N 460 2400 460 2400 {lab=0}
C {devices/lab_pin.sym} 460 2400 0 0 {name=p444 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 2400 0 0 {name=xf3p4
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 2430 680 2430 {lab=x_q3}
C {devices/lab_pin.sym} 680 2430 0 0 {name=p445 sig_type=std_logic lab=x_q3}
N 640 2400 640 2400 {lab=x_f3_b}
C {devices/lab_pin.sym} 640 2400 0 1 {name=p446 sig_type=std_logic lab=x_f3_b}
N 680 2370 680 2370 {lab=vdg}
C {devices/lab_pin.sym} 680 2370 0 0 {name=p447 sig_type=std_logic lab=vdg}
N 680 2400 680 2400 {lab=vdg}
C {devices/lab_pin.sym} 680 2400 0 0 {name=p448 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 2400 0 0 {name=xf3n4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 2370 900 2370 {lab=x_q3}
C {devices/lab_pin.sym} 900 2370 0 0 {name=p449 sig_type=std_logic lab=x_q3}
N 860 2400 860 2400 {lab=x_clk}
C {devices/lab_pin.sym} 860 2400 0 1 {name=p450 sig_type=std_logic lab=x_clk}
N 900 2430 900 2430 {lab=x_f3_x3}
C {devices/lab_pin.sym} 900 2430 0 0 {name=p451 sig_type=std_logic lab=x_f3_x3}
N 900 2400 900 2400 {lab=0}
C {devices/lab_pin.sym} 900 2400 0 0 {name=p452 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 2400 0 0 {name=xf3n5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 2370 1120 2370 {lab=x_f3_x3}
C {devices/lab_pin.sym} 1120 2370 0 0 {name=p453 sig_type=std_logic lab=x_f3_x3}
N 1080 2400 1080 2400 {lab=x_f3_b}
C {devices/lab_pin.sym} 1080 2400 0 1 {name=p454 sig_type=std_logic lab=x_f3_b}
N 1120 2430 1120 2430 {lab=0}
C {devices/lab_pin.sym} 1120 2430 0 0 {name=p455 sig_type=std_logic lab=0}
N 1120 2400 1120 2400 {lab=0}
C {devices/lab_pin.sym} 1120 2400 0 0 {name=p456 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 2520 0 0 {name=xi4p
w=1.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 2550 20 2550 {lab=x_d4}
C {devices/lab_pin.sym} 20 2550 0 0 {name=p457 sig_type=std_logic lab=x_d4}
N -20 2520 -20 2520 {lab=x_q3}
C {devices/lab_pin.sym} -20 2520 0 1 {name=p458 sig_type=std_logic lab=x_q3}
N 20 2490 20 2490 {lab=vdg}
C {devices/lab_pin.sym} 20 2490 0 0 {name=p459 sig_type=std_logic lab=vdg}
N 20 2520 20 2520 {lab=vdg}
C {devices/lab_pin.sym} 20 2520 0 0 {name=p460 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 2520 0 0 {name=xi4n
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 2490 240 2490 {lab=x_d4}
C {devices/lab_pin.sym} 240 2490 0 0 {name=p461 sig_type=std_logic lab=x_d4}
N 200 2520 200 2520 {lab=x_q3}
C {devices/lab_pin.sym} 200 2520 0 1 {name=p462 sig_type=std_logic lab=x_q3}
N 240 2550 240 2550 {lab=0}
C {devices/lab_pin.sym} 240 2550 0 0 {name=p463 sig_type=std_logic lab=0}
N 240 2520 240 2520 {lab=0}
C {devices/lab_pin.sym} 240 2520 0 0 {name=p464 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 2520 0 0 {name=xf4p1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 2550 460 2550 {lab=x_f4_x1}
C {devices/lab_pin.sym} 460 2550 0 0 {name=p465 sig_type=std_logic lab=x_f4_x1}
N 420 2520 420 2520 {lab=x_d4}
C {devices/lab_pin.sym} 420 2520 0 1 {name=p466 sig_type=std_logic lab=x_d4}
N 460 2490 460 2490 {lab=vdg}
C {devices/lab_pin.sym} 460 2490 0 0 {name=p467 sig_type=std_logic lab=vdg}
N 460 2520 460 2520 {lab=vdg}
C {devices/lab_pin.sym} 460 2520 0 0 {name=p468 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 2520 0 0 {name=xf4p2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 2550 680 2550 {lab=x_f4_a}
C {devices/lab_pin.sym} 680 2550 0 0 {name=p469 sig_type=std_logic lab=x_f4_a}
N 640 2520 640 2520 {lab=x_clk}
C {devices/lab_pin.sym} 640 2520 0 1 {name=p470 sig_type=std_logic lab=x_clk}
N 680 2490 680 2490 {lab=x_f4_x1}
C {devices/lab_pin.sym} 680 2490 0 0 {name=p471 sig_type=std_logic lab=x_f4_x1}
N 680 2520 680 2520 {lab=vdg}
C {devices/lab_pin.sym} 680 2520 0 0 {name=p472 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 2520 0 0 {name=xf4n1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 2490 900 2490 {lab=x_f4_a}
C {devices/lab_pin.sym} 900 2490 0 0 {name=p473 sig_type=std_logic lab=x_f4_a}
N 860 2520 860 2520 {lab=x_d4}
C {devices/lab_pin.sym} 860 2520 0 1 {name=p474 sig_type=std_logic lab=x_d4}
N 900 2550 900 2550 {lab=0}
C {devices/lab_pin.sym} 900 2550 0 0 {name=p475 sig_type=std_logic lab=0}
N 900 2520 900 2520 {lab=0}
C {devices/lab_pin.sym} 900 2520 0 0 {name=p476 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 2520 0 0 {name=xf4p3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 2550 1120 2550 {lab=x_f4_b}
C {devices/lab_pin.sym} 1120 2550 0 0 {name=p477 sig_type=std_logic lab=x_f4_b}
N 1080 2520 1080 2520 {lab=x_clk}
C {devices/lab_pin.sym} 1080 2520 0 1 {name=p478 sig_type=std_logic lab=x_clk}
N 1120 2490 1120 2490 {lab=vdg}
C {devices/lab_pin.sym} 1120 2490 0 0 {name=p479 sig_type=std_logic lab=vdg}
N 1120 2520 1120 2520 {lab=vdg}
C {devices/lab_pin.sym} 1120 2520 0 0 {name=p480 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 2640 0 0 {name=xf4n2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 2610 20 2610 {lab=x_f4_b}
C {devices/lab_pin.sym} 20 2610 0 0 {name=p481 sig_type=std_logic lab=x_f4_b}
N -20 2640 -20 2640 {lab=x_f4_a}
C {devices/lab_pin.sym} -20 2640 0 1 {name=p482 sig_type=std_logic lab=x_f4_a}
N 20 2670 20 2670 {lab=x_f4_x2}
C {devices/lab_pin.sym} 20 2670 0 0 {name=p483 sig_type=std_logic lab=x_f4_x2}
N 20 2640 20 2640 {lab=0}
C {devices/lab_pin.sym} 20 2640 0 0 {name=p484 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 2640 0 0 {name=xf4n3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 2610 240 2610 {lab=x_f4_x2}
C {devices/lab_pin.sym} 240 2610 0 0 {name=p485 sig_type=std_logic lab=x_f4_x2}
N 200 2640 200 2640 {lab=x_clk}
C {devices/lab_pin.sym} 200 2640 0 1 {name=p486 sig_type=std_logic lab=x_clk}
N 240 2670 240 2670 {lab=0}
C {devices/lab_pin.sym} 240 2670 0 0 {name=p487 sig_type=std_logic lab=0}
N 240 2640 240 2640 {lab=0}
C {devices/lab_pin.sym} 240 2640 0 0 {name=p488 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 2640 0 0 {name=xf4p4
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 2670 460 2670 {lab=x_q4}
C {devices/lab_pin.sym} 460 2670 0 0 {name=p489 sig_type=std_logic lab=x_q4}
N 420 2640 420 2640 {lab=x_f4_b}
C {devices/lab_pin.sym} 420 2640 0 1 {name=p490 sig_type=std_logic lab=x_f4_b}
N 460 2610 460 2610 {lab=vdg}
C {devices/lab_pin.sym} 460 2610 0 0 {name=p491 sig_type=std_logic lab=vdg}
N 460 2640 460 2640 {lab=vdg}
C {devices/lab_pin.sym} 460 2640 0 0 {name=p492 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 2640 0 0 {name=xf4n4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 2610 680 2610 {lab=x_q4}
C {devices/lab_pin.sym} 680 2610 0 0 {name=p493 sig_type=std_logic lab=x_q4}
N 640 2640 640 2640 {lab=x_clk}
C {devices/lab_pin.sym} 640 2640 0 1 {name=p494 sig_type=std_logic lab=x_clk}
N 680 2670 680 2670 {lab=x_f4_x3}
C {devices/lab_pin.sym} 680 2670 0 0 {name=p495 sig_type=std_logic lab=x_f4_x3}
N 680 2640 680 2640 {lab=0}
C {devices/lab_pin.sym} 680 2640 0 0 {name=p496 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 2640 0 0 {name=xf4n5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 2610 900 2610 {lab=x_f4_x3}
C {devices/lab_pin.sym} 900 2610 0 0 {name=p497 sig_type=std_logic lab=x_f4_x3}
N 860 2640 860 2640 {lab=x_f4_b}
C {devices/lab_pin.sym} 860 2640 0 1 {name=p498 sig_type=std_logic lab=x_f4_b}
N 900 2670 900 2670 {lab=0}
C {devices/lab_pin.sym} 900 2670 0 0 {name=p499 sig_type=std_logic lab=0}
N 900 2640 900 2640 {lab=0}
C {devices/lab_pin.sym} 900 2640 0 0 {name=p500 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 2640 0 0 {name=xo1p
w=1.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 2670 1120 2670 {lab=x_q1b}
C {devices/lab_pin.sym} 1120 2670 0 0 {name=p501 sig_type=std_logic lab=x_q1b}
N 1080 2640 1080 2640 {lab=x_q1}
C {devices/lab_pin.sym} 1080 2640 0 1 {name=p502 sig_type=std_logic lab=x_q1}
N 1120 2610 1120 2610 {lab=vdg}
C {devices/lab_pin.sym} 1120 2610 0 0 {name=p503 sig_type=std_logic lab=vdg}
N 1120 2640 1120 2640 {lab=vdg}
C {devices/lab_pin.sym} 1120 2640 0 0 {name=p504 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 2760 0 0 {name=xo1n
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 2730 20 2730 {lab=x_q1b}
C {devices/lab_pin.sym} 20 2730 0 0 {name=p505 sig_type=std_logic lab=x_q1b}
N -20 2760 -20 2760 {lab=x_q1}
C {devices/lab_pin.sym} -20 2760 0 1 {name=p506 sig_type=std_logic lab=x_q1}
N 20 2790 20 2790 {lab=0}
C {devices/lab_pin.sym} 20 2790 0 0 {name=p507 sig_type=std_logic lab=0}
N 20 2760 20 2760 {lab=0}
C {devices/lab_pin.sym} 20 2760 0 0 {name=p508 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 2760 0 0 {name=xr1ap1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 2790 240 2790 {lab=x_r1a_x1}
C {devices/lab_pin.sym} 240 2790 0 0 {name=p509 sig_type=std_logic lab=x_r1a_x1}
N 200 2760 200 2760 {lab=x_q1b}
C {devices/lab_pin.sym} 200 2760 0 1 {name=p510 sig_type=std_logic lab=x_q1b}
N 240 2730 240 2730 {lab=vdg}
C {devices/lab_pin.sym} 240 2730 0 0 {name=p511 sig_type=std_logic lab=vdg}
N 240 2760 240 2760 {lab=vdg}
C {devices/lab_pin.sym} 240 2760 0 0 {name=p512 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 2760 0 0 {name=xr1ap2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 2790 460 2790 {lab=x_r1a_a}
C {devices/lab_pin.sym} 460 2790 0 0 {name=p513 sig_type=std_logic lab=x_r1a_a}
N 420 2760 420 2760 {lab=x_clk}
C {devices/lab_pin.sym} 420 2760 0 1 {name=p514 sig_type=std_logic lab=x_clk}
N 460 2730 460 2730 {lab=x_r1a_x1}
C {devices/lab_pin.sym} 460 2730 0 0 {name=p515 sig_type=std_logic lab=x_r1a_x1}
N 460 2760 460 2760 {lab=vdg}
C {devices/lab_pin.sym} 460 2760 0 0 {name=p516 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 2760 0 0 {name=xr1an1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 2730 680 2730 {lab=x_r1a_a}
C {devices/lab_pin.sym} 680 2730 0 0 {name=p517 sig_type=std_logic lab=x_r1a_a}
N 640 2760 640 2760 {lab=x_q1b}
C {devices/lab_pin.sym} 640 2760 0 1 {name=p518 sig_type=std_logic lab=x_q1b}
N 680 2790 680 2790 {lab=0}
C {devices/lab_pin.sym} 680 2790 0 0 {name=p519 sig_type=std_logic lab=0}
N 680 2760 680 2760 {lab=0}
C {devices/lab_pin.sym} 680 2760 0 0 {name=p520 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 2760 0 0 {name=xr1ap3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 2790 900 2790 {lab=x_r1a_b}
C {devices/lab_pin.sym} 900 2790 0 0 {name=p521 sig_type=std_logic lab=x_r1a_b}
N 860 2760 860 2760 {lab=x_clk}
C {devices/lab_pin.sym} 860 2760 0 1 {name=p522 sig_type=std_logic lab=x_clk}
N 900 2730 900 2730 {lab=vdg}
C {devices/lab_pin.sym} 900 2730 0 0 {name=p523 sig_type=std_logic lab=vdg}
N 900 2760 900 2760 {lab=vdg}
C {devices/lab_pin.sym} 900 2760 0 0 {name=p524 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 2760 0 0 {name=xr1an2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 2730 1120 2730 {lab=x_r1a_b}
C {devices/lab_pin.sym} 1120 2730 0 0 {name=p525 sig_type=std_logic lab=x_r1a_b}
N 1080 2760 1080 2760 {lab=x_r1a_a}
C {devices/lab_pin.sym} 1080 2760 0 1 {name=p526 sig_type=std_logic lab=x_r1a_a}
N 1120 2790 1120 2790 {lab=x_r1a_x2}
C {devices/lab_pin.sym} 1120 2790 0 0 {name=p527 sig_type=std_logic lab=x_r1a_x2}
N 1120 2760 1120 2760 {lab=0}
C {devices/lab_pin.sym} 1120 2760 0 0 {name=p528 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 2880 0 0 {name=xr1an3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 2850 20 2850 {lab=x_r1a_x2}
C {devices/lab_pin.sym} 20 2850 0 0 {name=p529 sig_type=std_logic lab=x_r1a_x2}
N -20 2880 -20 2880 {lab=x_clk}
C {devices/lab_pin.sym} -20 2880 0 1 {name=p530 sig_type=std_logic lab=x_clk}
N 20 2910 20 2910 {lab=0}
C {devices/lab_pin.sym} 20 2910 0 0 {name=p531 sig_type=std_logic lab=0}
N 20 2880 20 2880 {lab=0}
C {devices/lab_pin.sym} 20 2880 0 0 {name=p532 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 2880 0 0 {name=xr1ap4
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 2910 240 2910 {lab=x_r1}
C {devices/lab_pin.sym} 240 2910 0 0 {name=p533 sig_type=std_logic lab=x_r1}
N 200 2880 200 2880 {lab=x_r1a_b}
C {devices/lab_pin.sym} 200 2880 0 1 {name=p534 sig_type=std_logic lab=x_r1a_b}
N 240 2850 240 2850 {lab=vdg}
C {devices/lab_pin.sym} 240 2850 0 0 {name=p535 sig_type=std_logic lab=vdg}
N 240 2880 240 2880 {lab=vdg}
C {devices/lab_pin.sym} 240 2880 0 0 {name=p536 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 2880 0 0 {name=xr1an4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 2850 460 2850 {lab=x_r1}
C {devices/lab_pin.sym} 460 2850 0 0 {name=p537 sig_type=std_logic lab=x_r1}
N 420 2880 420 2880 {lab=x_clk}
C {devices/lab_pin.sym} 420 2880 0 1 {name=p538 sig_type=std_logic lab=x_clk}
N 460 2910 460 2910 {lab=x_r1a_x3}
C {devices/lab_pin.sym} 460 2910 0 0 {name=p539 sig_type=std_logic lab=x_r1a_x3}
N 460 2880 460 2880 {lab=0}
C {devices/lab_pin.sym} 460 2880 0 0 {name=p540 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 2880 0 0 {name=xr1an5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 2850 680 2850 {lab=x_r1a_x3}
C {devices/lab_pin.sym} 680 2850 0 0 {name=p541 sig_type=std_logic lab=x_r1a_x3}
N 640 2880 640 2880 {lab=x_r1a_b}
C {devices/lab_pin.sym} 640 2880 0 1 {name=p542 sig_type=std_logic lab=x_r1a_b}
N 680 2910 680 2910 {lab=0}
C {devices/lab_pin.sym} 680 2910 0 0 {name=p543 sig_type=std_logic lab=0}
N 680 2880 680 2880 {lab=0}
C {devices/lab_pin.sym} 680 2880 0 0 {name=p544 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 2880 0 0 {name=xr1bp1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 2910 900 2910 {lab=x_r1b_x1}
C {devices/lab_pin.sym} 900 2910 0 0 {name=p545 sig_type=std_logic lab=x_r1b_x1}
N 860 2880 860 2880 {lab=x_q1}
C {devices/lab_pin.sym} 860 2880 0 1 {name=p546 sig_type=std_logic lab=x_q1}
N 900 2850 900 2850 {lab=vdg}
C {devices/lab_pin.sym} 900 2850 0 0 {name=p547 sig_type=std_logic lab=vdg}
N 900 2880 900 2880 {lab=vdg}
C {devices/lab_pin.sym} 900 2880 0 0 {name=p548 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 2880 0 0 {name=xr1bp2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 2910 1120 2910 {lab=x_r1b_a}
C {devices/lab_pin.sym} 1120 2910 0 0 {name=p549 sig_type=std_logic lab=x_r1b_a}
N 1080 2880 1080 2880 {lab=x_clk}
C {devices/lab_pin.sym} 1080 2880 0 1 {name=p550 sig_type=std_logic lab=x_clk}
N 1120 2850 1120 2850 {lab=x_r1b_x1}
C {devices/lab_pin.sym} 1120 2850 0 0 {name=p551 sig_type=std_logic lab=x_r1b_x1}
N 1120 2880 1120 2880 {lab=vdg}
C {devices/lab_pin.sym} 1120 2880 0 0 {name=p552 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 3000 0 0 {name=xr1bn1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 2970 20 2970 {lab=x_r1b_a}
C {devices/lab_pin.sym} 20 2970 0 0 {name=p553 sig_type=std_logic lab=x_r1b_a}
N -20 3000 -20 3000 {lab=x_q1}
C {devices/lab_pin.sym} -20 3000 0 1 {name=p554 sig_type=std_logic lab=x_q1}
N 20 3030 20 3030 {lab=0}
C {devices/lab_pin.sym} 20 3030 0 0 {name=p555 sig_type=std_logic lab=0}
N 20 3000 20 3000 {lab=0}
C {devices/lab_pin.sym} 20 3000 0 0 {name=p556 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 3000 0 0 {name=xr1bp3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 3030 240 3030 {lab=x_r1b_b}
C {devices/lab_pin.sym} 240 3030 0 0 {name=p557 sig_type=std_logic lab=x_r1b_b}
N 200 3000 200 3000 {lab=x_clk}
C {devices/lab_pin.sym} 200 3000 0 1 {name=p558 sig_type=std_logic lab=x_clk}
N 240 2970 240 2970 {lab=vdg}
C {devices/lab_pin.sym} 240 2970 0 0 {name=p559 sig_type=std_logic lab=vdg}
N 240 3000 240 3000 {lab=vdg}
C {devices/lab_pin.sym} 240 3000 0 0 {name=p560 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 3000 0 0 {name=xr1bn2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 2970 460 2970 {lab=x_r1b_b}
C {devices/lab_pin.sym} 460 2970 0 0 {name=p561 sig_type=std_logic lab=x_r1b_b}
N 420 3000 420 3000 {lab=x_r1b_a}
C {devices/lab_pin.sym} 420 3000 0 1 {name=p562 sig_type=std_logic lab=x_r1b_a}
N 460 3030 460 3030 {lab=x_r1b_x2}
C {devices/lab_pin.sym} 460 3030 0 0 {name=p563 sig_type=std_logic lab=x_r1b_x2}
N 460 3000 460 3000 {lab=0}
C {devices/lab_pin.sym} 460 3000 0 0 {name=p564 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 3000 0 0 {name=xr1bn3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 2970 680 2970 {lab=x_r1b_x2}
C {devices/lab_pin.sym} 680 2970 0 0 {name=p565 sig_type=std_logic lab=x_r1b_x2}
N 640 3000 640 3000 {lab=x_clk}
C {devices/lab_pin.sym} 640 3000 0 1 {name=p566 sig_type=std_logic lab=x_clk}
N 680 3030 680 3030 {lab=0}
C {devices/lab_pin.sym} 680 3030 0 0 {name=p567 sig_type=std_logic lab=0}
N 680 3000 680 3000 {lab=0}
C {devices/lab_pin.sym} 680 3000 0 0 {name=p568 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 3000 0 0 {name=xr1bp4
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 3030 900 3030 {lab=x_r1b}
C {devices/lab_pin.sym} 900 3030 0 0 {name=p569 sig_type=std_logic lab=x_r1b}
N 860 3000 860 3000 {lab=x_r1b_b}
C {devices/lab_pin.sym} 860 3000 0 1 {name=p570 sig_type=std_logic lab=x_r1b_b}
N 900 2970 900 2970 {lab=vdg}
C {devices/lab_pin.sym} 900 2970 0 0 {name=p571 sig_type=std_logic lab=vdg}
N 900 3000 900 3000 {lab=vdg}
C {devices/lab_pin.sym} 900 3000 0 0 {name=p572 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 3000 0 0 {name=xr1bn4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 2970 1120 2970 {lab=x_r1b}
C {devices/lab_pin.sym} 1120 2970 0 0 {name=p573 sig_type=std_logic lab=x_r1b}
N 1080 3000 1080 3000 {lab=x_clk}
C {devices/lab_pin.sym} 1080 3000 0 1 {name=p574 sig_type=std_logic lab=x_clk}
N 1120 3030 1120 3030 {lab=x_r1b_x3}
C {devices/lab_pin.sym} 1120 3030 0 0 {name=p575 sig_type=std_logic lab=x_r1b_x3}
N 1120 3000 1120 3000 {lab=0}
C {devices/lab_pin.sym} 1120 3000 0 0 {name=p576 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 3120 0 0 {name=xr1bn5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 3090 20 3090 {lab=x_r1b_x3}
C {devices/lab_pin.sym} 20 3090 0 0 {name=p577 sig_type=std_logic lab=x_r1b_x3}
N -20 3120 -20 3120 {lab=x_r1b_b}
C {devices/lab_pin.sym} -20 3120 0 1 {name=p578 sig_type=std_logic lab=x_r1b_b}
N 20 3150 20 3150 {lab=0}
C {devices/lab_pin.sym} 20 3150 0 0 {name=p579 sig_type=std_logic lab=0}
N 20 3120 20 3120 {lab=0}
C {devices/lab_pin.sym} 20 3120 0 0 {name=p580 sig_type=std_logic lab=0}
C {devices/capa.sym} 220 3120 0 0 {name=cr1
value=10f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 220 3090 220 3090 {lab=x_r1}
C {devices/lab_pin.sym} 220 3090 0 0 {name=p581 sig_type=std_logic lab=x_r1}
N 220 3150 220 3150 {lab=0}
C {devices/lab_pin.sym} 220 3150 0 0 {name=p582 sig_type=std_logic lab=0}
C {devices/capa.sym} 440 3120 0 0 {name=crb1
value=10f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 440 3090 440 3090 {lab=x_r1b}
C {devices/lab_pin.sym} 440 3090 0 0 {name=p583 sig_type=std_logic lab=x_r1b}
N 440 3150 440 3150 {lab=0}
C {devices/lab_pin.sym} 440 3150 0 0 {name=p584 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 3120 0 0 {name=xo2p
w=1.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 3150 680 3150 {lab=x_q2b}
C {devices/lab_pin.sym} 680 3150 0 0 {name=p585 sig_type=std_logic lab=x_q2b}
N 640 3120 640 3120 {lab=x_q2}
C {devices/lab_pin.sym} 640 3120 0 1 {name=p586 sig_type=std_logic lab=x_q2}
N 680 3090 680 3090 {lab=vdg}
C {devices/lab_pin.sym} 680 3090 0 0 {name=p587 sig_type=std_logic lab=vdg}
N 680 3120 680 3120 {lab=vdg}
C {devices/lab_pin.sym} 680 3120 0 0 {name=p588 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 3120 0 0 {name=xo2n
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 3090 900 3090 {lab=x_q2b}
C {devices/lab_pin.sym} 900 3090 0 0 {name=p589 sig_type=std_logic lab=x_q2b}
N 860 3120 860 3120 {lab=x_q2}
C {devices/lab_pin.sym} 860 3120 0 1 {name=p590 sig_type=std_logic lab=x_q2}
N 900 3150 900 3150 {lab=0}
C {devices/lab_pin.sym} 900 3150 0 0 {name=p591 sig_type=std_logic lab=0}
N 900 3120 900 3120 {lab=0}
C {devices/lab_pin.sym} 900 3120 0 0 {name=p592 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 3120 0 0 {name=xr2ap1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 3150 1120 3150 {lab=x_r2a_x1}
C {devices/lab_pin.sym} 1120 3150 0 0 {name=p593 sig_type=std_logic lab=x_r2a_x1}
N 1080 3120 1080 3120 {lab=x_q2b}
C {devices/lab_pin.sym} 1080 3120 0 1 {name=p594 sig_type=std_logic lab=x_q2b}
N 1120 3090 1120 3090 {lab=vdg}
C {devices/lab_pin.sym} 1120 3090 0 0 {name=p595 sig_type=std_logic lab=vdg}
N 1120 3120 1120 3120 {lab=vdg}
C {devices/lab_pin.sym} 1120 3120 0 0 {name=p596 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 3240 0 0 {name=xr2ap2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 3270 20 3270 {lab=x_r2a_a}
C {devices/lab_pin.sym} 20 3270 0 0 {name=p597 sig_type=std_logic lab=x_r2a_a}
N -20 3240 -20 3240 {lab=x_clk}
C {devices/lab_pin.sym} -20 3240 0 1 {name=p598 sig_type=std_logic lab=x_clk}
N 20 3210 20 3210 {lab=x_r2a_x1}
C {devices/lab_pin.sym} 20 3210 0 0 {name=p599 sig_type=std_logic lab=x_r2a_x1}
N 20 3240 20 3240 {lab=vdg}
C {devices/lab_pin.sym} 20 3240 0 0 {name=p600 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 3240 0 0 {name=xr2an1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 3210 240 3210 {lab=x_r2a_a}
C {devices/lab_pin.sym} 240 3210 0 0 {name=p601 sig_type=std_logic lab=x_r2a_a}
N 200 3240 200 3240 {lab=x_q2b}
C {devices/lab_pin.sym} 200 3240 0 1 {name=p602 sig_type=std_logic lab=x_q2b}
N 240 3270 240 3270 {lab=0}
C {devices/lab_pin.sym} 240 3270 0 0 {name=p603 sig_type=std_logic lab=0}
N 240 3240 240 3240 {lab=0}
C {devices/lab_pin.sym} 240 3240 0 0 {name=p604 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 3240 0 0 {name=xr2ap3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 3270 460 3270 {lab=x_r2a_b}
C {devices/lab_pin.sym} 460 3270 0 0 {name=p605 sig_type=std_logic lab=x_r2a_b}
N 420 3240 420 3240 {lab=x_clk}
C {devices/lab_pin.sym} 420 3240 0 1 {name=p606 sig_type=std_logic lab=x_clk}
N 460 3210 460 3210 {lab=vdg}
C {devices/lab_pin.sym} 460 3210 0 0 {name=p607 sig_type=std_logic lab=vdg}
N 460 3240 460 3240 {lab=vdg}
C {devices/lab_pin.sym} 460 3240 0 0 {name=p608 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 3240 0 0 {name=xr2an2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 3210 680 3210 {lab=x_r2a_b}
C {devices/lab_pin.sym} 680 3210 0 0 {name=p609 sig_type=std_logic lab=x_r2a_b}
N 640 3240 640 3240 {lab=x_r2a_a}
C {devices/lab_pin.sym} 640 3240 0 1 {name=p610 sig_type=std_logic lab=x_r2a_a}
N 680 3270 680 3270 {lab=x_r2a_x2}
C {devices/lab_pin.sym} 680 3270 0 0 {name=p611 sig_type=std_logic lab=x_r2a_x2}
N 680 3240 680 3240 {lab=0}
C {devices/lab_pin.sym} 680 3240 0 0 {name=p612 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 3240 0 0 {name=xr2an3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 3210 900 3210 {lab=x_r2a_x2}
C {devices/lab_pin.sym} 900 3210 0 0 {name=p613 sig_type=std_logic lab=x_r2a_x2}
N 860 3240 860 3240 {lab=x_clk}
C {devices/lab_pin.sym} 860 3240 0 1 {name=p614 sig_type=std_logic lab=x_clk}
N 900 3270 900 3270 {lab=0}
C {devices/lab_pin.sym} 900 3270 0 0 {name=p615 sig_type=std_logic lab=0}
N 900 3240 900 3240 {lab=0}
C {devices/lab_pin.sym} 900 3240 0 0 {name=p616 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 3240 0 0 {name=xr2ap4
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 3270 1120 3270 {lab=x_r2}
C {devices/lab_pin.sym} 1120 3270 0 0 {name=p617 sig_type=std_logic lab=x_r2}
N 1080 3240 1080 3240 {lab=x_r2a_b}
C {devices/lab_pin.sym} 1080 3240 0 1 {name=p618 sig_type=std_logic lab=x_r2a_b}
N 1120 3210 1120 3210 {lab=vdg}
C {devices/lab_pin.sym} 1120 3210 0 0 {name=p619 sig_type=std_logic lab=vdg}
N 1120 3240 1120 3240 {lab=vdg}
C {devices/lab_pin.sym} 1120 3240 0 0 {name=p620 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 3360 0 0 {name=xr2an4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 3330 20 3330 {lab=x_r2}
C {devices/lab_pin.sym} 20 3330 0 0 {name=p621 sig_type=std_logic lab=x_r2}
N -20 3360 -20 3360 {lab=x_clk}
C {devices/lab_pin.sym} -20 3360 0 1 {name=p622 sig_type=std_logic lab=x_clk}
N 20 3390 20 3390 {lab=x_r2a_x3}
C {devices/lab_pin.sym} 20 3390 0 0 {name=p623 sig_type=std_logic lab=x_r2a_x3}
N 20 3360 20 3360 {lab=0}
C {devices/lab_pin.sym} 20 3360 0 0 {name=p624 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 3360 0 0 {name=xr2an5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 3330 240 3330 {lab=x_r2a_x3}
C {devices/lab_pin.sym} 240 3330 0 0 {name=p625 sig_type=std_logic lab=x_r2a_x3}
N 200 3360 200 3360 {lab=x_r2a_b}
C {devices/lab_pin.sym} 200 3360 0 1 {name=p626 sig_type=std_logic lab=x_r2a_b}
N 240 3390 240 3390 {lab=0}
C {devices/lab_pin.sym} 240 3390 0 0 {name=p627 sig_type=std_logic lab=0}
N 240 3360 240 3360 {lab=0}
C {devices/lab_pin.sym} 240 3360 0 0 {name=p628 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 3360 0 0 {name=xr2bp1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 3390 460 3390 {lab=x_r2b_x1}
C {devices/lab_pin.sym} 460 3390 0 0 {name=p629 sig_type=std_logic lab=x_r2b_x1}
N 420 3360 420 3360 {lab=x_q2}
C {devices/lab_pin.sym} 420 3360 0 1 {name=p630 sig_type=std_logic lab=x_q2}
N 460 3330 460 3330 {lab=vdg}
C {devices/lab_pin.sym} 460 3330 0 0 {name=p631 sig_type=std_logic lab=vdg}
N 460 3360 460 3360 {lab=vdg}
C {devices/lab_pin.sym} 460 3360 0 0 {name=p632 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 3360 0 0 {name=xr2bp2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 3390 680 3390 {lab=x_r2b_a}
C {devices/lab_pin.sym} 680 3390 0 0 {name=p633 sig_type=std_logic lab=x_r2b_a}
N 640 3360 640 3360 {lab=x_clk}
C {devices/lab_pin.sym} 640 3360 0 1 {name=p634 sig_type=std_logic lab=x_clk}
N 680 3330 680 3330 {lab=x_r2b_x1}
C {devices/lab_pin.sym} 680 3330 0 0 {name=p635 sig_type=std_logic lab=x_r2b_x1}
N 680 3360 680 3360 {lab=vdg}
C {devices/lab_pin.sym} 680 3360 0 0 {name=p636 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 3360 0 0 {name=xr2bn1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 3330 900 3330 {lab=x_r2b_a}
C {devices/lab_pin.sym} 900 3330 0 0 {name=p637 sig_type=std_logic lab=x_r2b_a}
N 860 3360 860 3360 {lab=x_q2}
C {devices/lab_pin.sym} 860 3360 0 1 {name=p638 sig_type=std_logic lab=x_q2}
N 900 3390 900 3390 {lab=0}
C {devices/lab_pin.sym} 900 3390 0 0 {name=p639 sig_type=std_logic lab=0}
N 900 3360 900 3360 {lab=0}
C {devices/lab_pin.sym} 900 3360 0 0 {name=p640 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 3360 0 0 {name=xr2bp3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 3390 1120 3390 {lab=x_r2b_b}
C {devices/lab_pin.sym} 1120 3390 0 0 {name=p641 sig_type=std_logic lab=x_r2b_b}
N 1080 3360 1080 3360 {lab=x_clk}
C {devices/lab_pin.sym} 1080 3360 0 1 {name=p642 sig_type=std_logic lab=x_clk}
N 1120 3330 1120 3330 {lab=vdg}
C {devices/lab_pin.sym} 1120 3330 0 0 {name=p643 sig_type=std_logic lab=vdg}
N 1120 3360 1120 3360 {lab=vdg}
C {devices/lab_pin.sym} 1120 3360 0 0 {name=p644 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 3480 0 0 {name=xr2bn2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 3450 20 3450 {lab=x_r2b_b}
C {devices/lab_pin.sym} 20 3450 0 0 {name=p645 sig_type=std_logic lab=x_r2b_b}
N -20 3480 -20 3480 {lab=x_r2b_a}
C {devices/lab_pin.sym} -20 3480 0 1 {name=p646 sig_type=std_logic lab=x_r2b_a}
N 20 3510 20 3510 {lab=x_r2b_x2}
C {devices/lab_pin.sym} 20 3510 0 0 {name=p647 sig_type=std_logic lab=x_r2b_x2}
N 20 3480 20 3480 {lab=0}
C {devices/lab_pin.sym} 20 3480 0 0 {name=p648 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 3480 0 0 {name=xr2bn3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 3450 240 3450 {lab=x_r2b_x2}
C {devices/lab_pin.sym} 240 3450 0 0 {name=p649 sig_type=std_logic lab=x_r2b_x2}
N 200 3480 200 3480 {lab=x_clk}
C {devices/lab_pin.sym} 200 3480 0 1 {name=p650 sig_type=std_logic lab=x_clk}
N 240 3510 240 3510 {lab=0}
C {devices/lab_pin.sym} 240 3510 0 0 {name=p651 sig_type=std_logic lab=0}
N 240 3480 240 3480 {lab=0}
C {devices/lab_pin.sym} 240 3480 0 0 {name=p652 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 3480 0 0 {name=xr2bp4
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 3510 460 3510 {lab=x_r2b}
C {devices/lab_pin.sym} 460 3510 0 0 {name=p653 sig_type=std_logic lab=x_r2b}
N 420 3480 420 3480 {lab=x_r2b_b}
C {devices/lab_pin.sym} 420 3480 0 1 {name=p654 sig_type=std_logic lab=x_r2b_b}
N 460 3450 460 3450 {lab=vdg}
C {devices/lab_pin.sym} 460 3450 0 0 {name=p655 sig_type=std_logic lab=vdg}
N 460 3480 460 3480 {lab=vdg}
C {devices/lab_pin.sym} 460 3480 0 0 {name=p656 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 3480 0 0 {name=xr2bn4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 3450 680 3450 {lab=x_r2b}
C {devices/lab_pin.sym} 680 3450 0 0 {name=p657 sig_type=std_logic lab=x_r2b}
N 640 3480 640 3480 {lab=x_clk}
C {devices/lab_pin.sym} 640 3480 0 1 {name=p658 sig_type=std_logic lab=x_clk}
N 680 3510 680 3510 {lab=x_r2b_x3}
C {devices/lab_pin.sym} 680 3510 0 0 {name=p659 sig_type=std_logic lab=x_r2b_x3}
N 680 3480 680 3480 {lab=0}
C {devices/lab_pin.sym} 680 3480 0 0 {name=p660 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 3480 0 0 {name=xr2bn5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 3450 900 3450 {lab=x_r2b_x3}
C {devices/lab_pin.sym} 900 3450 0 0 {name=p661 sig_type=std_logic lab=x_r2b_x3}
N 860 3480 860 3480 {lab=x_r2b_b}
C {devices/lab_pin.sym} 860 3480 0 1 {name=p662 sig_type=std_logic lab=x_r2b_b}
N 900 3510 900 3510 {lab=0}
C {devices/lab_pin.sym} 900 3510 0 0 {name=p663 sig_type=std_logic lab=0}
N 900 3480 900 3480 {lab=0}
C {devices/lab_pin.sym} 900 3480 0 0 {name=p664 sig_type=std_logic lab=0}
C {devices/capa.sym} 1100 3480 0 0 {name=cr2
value=10f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 1100 3450 1100 3450 {lab=x_r2}
C {devices/lab_pin.sym} 1100 3450 0 0 {name=p665 sig_type=std_logic lab=x_r2}
N 1100 3510 1100 3510 {lab=0}
C {devices/lab_pin.sym} 1100 3510 0 0 {name=p666 sig_type=std_logic lab=0}
C {devices/capa.sym} 0 3600 0 0 {name=crb2
value=10f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 0 3570 0 3570 {lab=x_r2b}
C {devices/lab_pin.sym} 0 3570 0 0 {name=p667 sig_type=std_logic lab=x_r2b}
N 0 3630 0 3630 {lab=0}
C {devices/lab_pin.sym} 0 3630 0 0 {name=p668 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 3600 0 0 {name=xo3p
w=1.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 3630 240 3630 {lab=x_q3b}
C {devices/lab_pin.sym} 240 3630 0 0 {name=p669 sig_type=std_logic lab=x_q3b}
N 200 3600 200 3600 {lab=x_q3}
C {devices/lab_pin.sym} 200 3600 0 1 {name=p670 sig_type=std_logic lab=x_q3}
N 240 3570 240 3570 {lab=vdg}
C {devices/lab_pin.sym} 240 3570 0 0 {name=p671 sig_type=std_logic lab=vdg}
N 240 3600 240 3600 {lab=vdg}
C {devices/lab_pin.sym} 240 3600 0 0 {name=p672 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 3600 0 0 {name=xo3n
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 3570 460 3570 {lab=x_q3b}
C {devices/lab_pin.sym} 460 3570 0 0 {name=p673 sig_type=std_logic lab=x_q3b}
N 420 3600 420 3600 {lab=x_q3}
C {devices/lab_pin.sym} 420 3600 0 1 {name=p674 sig_type=std_logic lab=x_q3}
N 460 3630 460 3630 {lab=0}
C {devices/lab_pin.sym} 460 3630 0 0 {name=p675 sig_type=std_logic lab=0}
N 460 3600 460 3600 {lab=0}
C {devices/lab_pin.sym} 460 3600 0 0 {name=p676 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 3600 0 0 {name=xr3ap1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 3630 680 3630 {lab=x_r3a_x1}
C {devices/lab_pin.sym} 680 3630 0 0 {name=p677 sig_type=std_logic lab=x_r3a_x1}
N 640 3600 640 3600 {lab=x_q3b}
C {devices/lab_pin.sym} 640 3600 0 1 {name=p678 sig_type=std_logic lab=x_q3b}
N 680 3570 680 3570 {lab=vdg}
C {devices/lab_pin.sym} 680 3570 0 0 {name=p679 sig_type=std_logic lab=vdg}
N 680 3600 680 3600 {lab=vdg}
C {devices/lab_pin.sym} 680 3600 0 0 {name=p680 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 3600 0 0 {name=xr3ap2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 3630 900 3630 {lab=x_r3a_a}
C {devices/lab_pin.sym} 900 3630 0 0 {name=p681 sig_type=std_logic lab=x_r3a_a}
N 860 3600 860 3600 {lab=x_clk}
C {devices/lab_pin.sym} 860 3600 0 1 {name=p682 sig_type=std_logic lab=x_clk}
N 900 3570 900 3570 {lab=x_r3a_x1}
C {devices/lab_pin.sym} 900 3570 0 0 {name=p683 sig_type=std_logic lab=x_r3a_x1}
N 900 3600 900 3600 {lab=vdg}
C {devices/lab_pin.sym} 900 3600 0 0 {name=p684 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 3600 0 0 {name=xr3an1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 3570 1120 3570 {lab=x_r3a_a}
C {devices/lab_pin.sym} 1120 3570 0 0 {name=p685 sig_type=std_logic lab=x_r3a_a}
N 1080 3600 1080 3600 {lab=x_q3b}
C {devices/lab_pin.sym} 1080 3600 0 1 {name=p686 sig_type=std_logic lab=x_q3b}
N 1120 3630 1120 3630 {lab=0}
C {devices/lab_pin.sym} 1120 3630 0 0 {name=p687 sig_type=std_logic lab=0}
N 1120 3600 1120 3600 {lab=0}
C {devices/lab_pin.sym} 1120 3600 0 0 {name=p688 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 3720 0 0 {name=xr3ap3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 3750 20 3750 {lab=x_r3a_b}
C {devices/lab_pin.sym} 20 3750 0 0 {name=p689 sig_type=std_logic lab=x_r3a_b}
N -20 3720 -20 3720 {lab=x_clk}
C {devices/lab_pin.sym} -20 3720 0 1 {name=p690 sig_type=std_logic lab=x_clk}
N 20 3690 20 3690 {lab=vdg}
C {devices/lab_pin.sym} 20 3690 0 0 {name=p691 sig_type=std_logic lab=vdg}
N 20 3720 20 3720 {lab=vdg}
C {devices/lab_pin.sym} 20 3720 0 0 {name=p692 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 3720 0 0 {name=xr3an2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 3690 240 3690 {lab=x_r3a_b}
C {devices/lab_pin.sym} 240 3690 0 0 {name=p693 sig_type=std_logic lab=x_r3a_b}
N 200 3720 200 3720 {lab=x_r3a_a}
C {devices/lab_pin.sym} 200 3720 0 1 {name=p694 sig_type=std_logic lab=x_r3a_a}
N 240 3750 240 3750 {lab=x_r3a_x2}
C {devices/lab_pin.sym} 240 3750 0 0 {name=p695 sig_type=std_logic lab=x_r3a_x2}
N 240 3720 240 3720 {lab=0}
C {devices/lab_pin.sym} 240 3720 0 0 {name=p696 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 3720 0 0 {name=xr3an3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 3690 460 3690 {lab=x_r3a_x2}
C {devices/lab_pin.sym} 460 3690 0 0 {name=p697 sig_type=std_logic lab=x_r3a_x2}
N 420 3720 420 3720 {lab=x_clk}
C {devices/lab_pin.sym} 420 3720 0 1 {name=p698 sig_type=std_logic lab=x_clk}
N 460 3750 460 3750 {lab=0}
C {devices/lab_pin.sym} 460 3750 0 0 {name=p699 sig_type=std_logic lab=0}
N 460 3720 460 3720 {lab=0}
C {devices/lab_pin.sym} 460 3720 0 0 {name=p700 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 3720 0 0 {name=xr3ap4
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 3750 680 3750 {lab=x_r3}
C {devices/lab_pin.sym} 680 3750 0 0 {name=p701 sig_type=std_logic lab=x_r3}
N 640 3720 640 3720 {lab=x_r3a_b}
C {devices/lab_pin.sym} 640 3720 0 1 {name=p702 sig_type=std_logic lab=x_r3a_b}
N 680 3690 680 3690 {lab=vdg}
C {devices/lab_pin.sym} 680 3690 0 0 {name=p703 sig_type=std_logic lab=vdg}
N 680 3720 680 3720 {lab=vdg}
C {devices/lab_pin.sym} 680 3720 0 0 {name=p704 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 3720 0 0 {name=xr3an4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 3690 900 3690 {lab=x_r3}
C {devices/lab_pin.sym} 900 3690 0 0 {name=p705 sig_type=std_logic lab=x_r3}
N 860 3720 860 3720 {lab=x_clk}
C {devices/lab_pin.sym} 860 3720 0 1 {name=p706 sig_type=std_logic lab=x_clk}
N 900 3750 900 3750 {lab=x_r3a_x3}
C {devices/lab_pin.sym} 900 3750 0 0 {name=p707 sig_type=std_logic lab=x_r3a_x3}
N 900 3720 900 3720 {lab=0}
C {devices/lab_pin.sym} 900 3720 0 0 {name=p708 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 3720 0 0 {name=xr3an5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 3690 1120 3690 {lab=x_r3a_x3}
C {devices/lab_pin.sym} 1120 3690 0 0 {name=p709 sig_type=std_logic lab=x_r3a_x3}
N 1080 3720 1080 3720 {lab=x_r3a_b}
C {devices/lab_pin.sym} 1080 3720 0 1 {name=p710 sig_type=std_logic lab=x_r3a_b}
N 1120 3750 1120 3750 {lab=0}
C {devices/lab_pin.sym} 1120 3750 0 0 {name=p711 sig_type=std_logic lab=0}
N 1120 3720 1120 3720 {lab=0}
C {devices/lab_pin.sym} 1120 3720 0 0 {name=p712 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 3840 0 0 {name=xr3bp1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 3870 20 3870 {lab=x_r3b_x1}
C {devices/lab_pin.sym} 20 3870 0 0 {name=p713 sig_type=std_logic lab=x_r3b_x1}
N -20 3840 -20 3840 {lab=x_q3}
C {devices/lab_pin.sym} -20 3840 0 1 {name=p714 sig_type=std_logic lab=x_q3}
N 20 3810 20 3810 {lab=vdg}
C {devices/lab_pin.sym} 20 3810 0 0 {name=p715 sig_type=std_logic lab=vdg}
N 20 3840 20 3840 {lab=vdg}
C {devices/lab_pin.sym} 20 3840 0 0 {name=p716 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 3840 0 0 {name=xr3bp2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 3870 240 3870 {lab=x_r3b_a}
C {devices/lab_pin.sym} 240 3870 0 0 {name=p717 sig_type=std_logic lab=x_r3b_a}
N 200 3840 200 3840 {lab=x_clk}
C {devices/lab_pin.sym} 200 3840 0 1 {name=p718 sig_type=std_logic lab=x_clk}
N 240 3810 240 3810 {lab=x_r3b_x1}
C {devices/lab_pin.sym} 240 3810 0 0 {name=p719 sig_type=std_logic lab=x_r3b_x1}
N 240 3840 240 3840 {lab=vdg}
C {devices/lab_pin.sym} 240 3840 0 0 {name=p720 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 3840 0 0 {name=xr3bn1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 3810 460 3810 {lab=x_r3b_a}
C {devices/lab_pin.sym} 460 3810 0 0 {name=p721 sig_type=std_logic lab=x_r3b_a}
N 420 3840 420 3840 {lab=x_q3}
C {devices/lab_pin.sym} 420 3840 0 1 {name=p722 sig_type=std_logic lab=x_q3}
N 460 3870 460 3870 {lab=0}
C {devices/lab_pin.sym} 460 3870 0 0 {name=p723 sig_type=std_logic lab=0}
N 460 3840 460 3840 {lab=0}
C {devices/lab_pin.sym} 460 3840 0 0 {name=p724 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 3840 0 0 {name=xr3bp3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 3870 680 3870 {lab=x_r3b_b}
C {devices/lab_pin.sym} 680 3870 0 0 {name=p725 sig_type=std_logic lab=x_r3b_b}
N 640 3840 640 3840 {lab=x_clk}
C {devices/lab_pin.sym} 640 3840 0 1 {name=p726 sig_type=std_logic lab=x_clk}
N 680 3810 680 3810 {lab=vdg}
C {devices/lab_pin.sym} 680 3810 0 0 {name=p727 sig_type=std_logic lab=vdg}
N 680 3840 680 3840 {lab=vdg}
C {devices/lab_pin.sym} 680 3840 0 0 {name=p728 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 3840 0 0 {name=xr3bn2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 3810 900 3810 {lab=x_r3b_b}
C {devices/lab_pin.sym} 900 3810 0 0 {name=p729 sig_type=std_logic lab=x_r3b_b}
N 860 3840 860 3840 {lab=x_r3b_a}
C {devices/lab_pin.sym} 860 3840 0 1 {name=p730 sig_type=std_logic lab=x_r3b_a}
N 900 3870 900 3870 {lab=x_r3b_x2}
C {devices/lab_pin.sym} 900 3870 0 0 {name=p731 sig_type=std_logic lab=x_r3b_x2}
N 900 3840 900 3840 {lab=0}
C {devices/lab_pin.sym} 900 3840 0 0 {name=p732 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 3840 0 0 {name=xr3bn3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 3810 1120 3810 {lab=x_r3b_x2}
C {devices/lab_pin.sym} 1120 3810 0 0 {name=p733 sig_type=std_logic lab=x_r3b_x2}
N 1080 3840 1080 3840 {lab=x_clk}
C {devices/lab_pin.sym} 1080 3840 0 1 {name=p734 sig_type=std_logic lab=x_clk}
N 1120 3870 1120 3870 {lab=0}
C {devices/lab_pin.sym} 1120 3870 0 0 {name=p735 sig_type=std_logic lab=0}
N 1120 3840 1120 3840 {lab=0}
C {devices/lab_pin.sym} 1120 3840 0 0 {name=p736 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 3960 0 0 {name=xr3bp4
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 3990 20 3990 {lab=x_r3b}
C {devices/lab_pin.sym} 20 3990 0 0 {name=p737 sig_type=std_logic lab=x_r3b}
N -20 3960 -20 3960 {lab=x_r3b_b}
C {devices/lab_pin.sym} -20 3960 0 1 {name=p738 sig_type=std_logic lab=x_r3b_b}
N 20 3930 20 3930 {lab=vdg}
C {devices/lab_pin.sym} 20 3930 0 0 {name=p739 sig_type=std_logic lab=vdg}
N 20 3960 20 3960 {lab=vdg}
C {devices/lab_pin.sym} 20 3960 0 0 {name=p740 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 3960 0 0 {name=xr3bn4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 3930 240 3930 {lab=x_r3b}
C {devices/lab_pin.sym} 240 3930 0 0 {name=p741 sig_type=std_logic lab=x_r3b}
N 200 3960 200 3960 {lab=x_clk}
C {devices/lab_pin.sym} 200 3960 0 1 {name=p742 sig_type=std_logic lab=x_clk}
N 240 3990 240 3990 {lab=x_r3b_x3}
C {devices/lab_pin.sym} 240 3990 0 0 {name=p743 sig_type=std_logic lab=x_r3b_x3}
N 240 3960 240 3960 {lab=0}
C {devices/lab_pin.sym} 240 3960 0 0 {name=p744 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 3960 0 0 {name=xr3bn5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 3930 460 3930 {lab=x_r3b_x3}
C {devices/lab_pin.sym} 460 3930 0 0 {name=p745 sig_type=std_logic lab=x_r3b_x3}
N 420 3960 420 3960 {lab=x_r3b_b}
C {devices/lab_pin.sym} 420 3960 0 1 {name=p746 sig_type=std_logic lab=x_r3b_b}
N 460 3990 460 3990 {lab=0}
C {devices/lab_pin.sym} 460 3990 0 0 {name=p747 sig_type=std_logic lab=0}
N 460 3960 460 3960 {lab=0}
C {devices/lab_pin.sym} 460 3960 0 0 {name=p748 sig_type=std_logic lab=0}
C {devices/capa.sym} 660 3960 0 0 {name=cr3
value=10f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 660 3930 660 3930 {lab=x_r3}
C {devices/lab_pin.sym} 660 3930 0 0 {name=p749 sig_type=std_logic lab=x_r3}
N 660 3990 660 3990 {lab=0}
C {devices/lab_pin.sym} 660 3990 0 0 {name=p750 sig_type=std_logic lab=0}
C {devices/capa.sym} 880 3960 0 0 {name=crb3
value=10f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 880 3930 880 3930 {lab=x_r3b}
C {devices/lab_pin.sym} 880 3930 0 0 {name=p751 sig_type=std_logic lab=x_r3b}
N 880 3990 880 3990 {lab=0}
C {devices/lab_pin.sym} 880 3990 0 0 {name=p752 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 3960 0 0 {name=xo4p
w=1.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 3990 1120 3990 {lab=x_q4b}
C {devices/lab_pin.sym} 1120 3990 0 0 {name=p753 sig_type=std_logic lab=x_q4b}
N 1080 3960 1080 3960 {lab=x_q4}
C {devices/lab_pin.sym} 1080 3960 0 1 {name=p754 sig_type=std_logic lab=x_q4}
N 1120 3930 1120 3930 {lab=vdg}
C {devices/lab_pin.sym} 1120 3930 0 0 {name=p755 sig_type=std_logic lab=vdg}
N 1120 3960 1120 3960 {lab=vdg}
C {devices/lab_pin.sym} 1120 3960 0 0 {name=p756 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 4080 0 0 {name=xo4n
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 4050 20 4050 {lab=x_q4b}
C {devices/lab_pin.sym} 20 4050 0 0 {name=p757 sig_type=std_logic lab=x_q4b}
N -20 4080 -20 4080 {lab=x_q4}
C {devices/lab_pin.sym} -20 4080 0 1 {name=p758 sig_type=std_logic lab=x_q4}
N 20 4110 20 4110 {lab=0}
C {devices/lab_pin.sym} 20 4110 0 0 {name=p759 sig_type=std_logic lab=0}
N 20 4080 20 4080 {lab=0}
C {devices/lab_pin.sym} 20 4080 0 0 {name=p760 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 4080 0 0 {name=xr4ap1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 4110 240 4110 {lab=x_r4a_x1}
C {devices/lab_pin.sym} 240 4110 0 0 {name=p761 sig_type=std_logic lab=x_r4a_x1}
N 200 4080 200 4080 {lab=x_q4b}
C {devices/lab_pin.sym} 200 4080 0 1 {name=p762 sig_type=std_logic lab=x_q4b}
N 240 4050 240 4050 {lab=vdg}
C {devices/lab_pin.sym} 240 4050 0 0 {name=p763 sig_type=std_logic lab=vdg}
N 240 4080 240 4080 {lab=vdg}
C {devices/lab_pin.sym} 240 4080 0 0 {name=p764 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 4080 0 0 {name=xr4ap2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 4110 460 4110 {lab=x_r4a_a}
C {devices/lab_pin.sym} 460 4110 0 0 {name=p765 sig_type=std_logic lab=x_r4a_a}
N 420 4080 420 4080 {lab=x_clk}
C {devices/lab_pin.sym} 420 4080 0 1 {name=p766 sig_type=std_logic lab=x_clk}
N 460 4050 460 4050 {lab=x_r4a_x1}
C {devices/lab_pin.sym} 460 4050 0 0 {name=p767 sig_type=std_logic lab=x_r4a_x1}
N 460 4080 460 4080 {lab=vdg}
C {devices/lab_pin.sym} 460 4080 0 0 {name=p768 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 4080 0 0 {name=xr4an1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 4050 680 4050 {lab=x_r4a_a}
C {devices/lab_pin.sym} 680 4050 0 0 {name=p769 sig_type=std_logic lab=x_r4a_a}
N 640 4080 640 4080 {lab=x_q4b}
C {devices/lab_pin.sym} 640 4080 0 1 {name=p770 sig_type=std_logic lab=x_q4b}
N 680 4110 680 4110 {lab=0}
C {devices/lab_pin.sym} 680 4110 0 0 {name=p771 sig_type=std_logic lab=0}
N 680 4080 680 4080 {lab=0}
C {devices/lab_pin.sym} 680 4080 0 0 {name=p772 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 4080 0 0 {name=xr4ap3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 4110 900 4110 {lab=x_r4a_b}
C {devices/lab_pin.sym} 900 4110 0 0 {name=p773 sig_type=std_logic lab=x_r4a_b}
N 860 4080 860 4080 {lab=x_clk}
C {devices/lab_pin.sym} 860 4080 0 1 {name=p774 sig_type=std_logic lab=x_clk}
N 900 4050 900 4050 {lab=vdg}
C {devices/lab_pin.sym} 900 4050 0 0 {name=p775 sig_type=std_logic lab=vdg}
N 900 4080 900 4080 {lab=vdg}
C {devices/lab_pin.sym} 900 4080 0 0 {name=p776 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 4080 0 0 {name=xr4an2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 4050 1120 4050 {lab=x_r4a_b}
C {devices/lab_pin.sym} 1120 4050 0 0 {name=p777 sig_type=std_logic lab=x_r4a_b}
N 1080 4080 1080 4080 {lab=x_r4a_a}
C {devices/lab_pin.sym} 1080 4080 0 1 {name=p778 sig_type=std_logic lab=x_r4a_a}
N 1120 4110 1120 4110 {lab=x_r4a_x2}
C {devices/lab_pin.sym} 1120 4110 0 0 {name=p779 sig_type=std_logic lab=x_r4a_x2}
N 1120 4080 1120 4080 {lab=0}
C {devices/lab_pin.sym} 1120 4080 0 0 {name=p780 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 4200 0 0 {name=xr4an3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 4170 20 4170 {lab=x_r4a_x2}
C {devices/lab_pin.sym} 20 4170 0 0 {name=p781 sig_type=std_logic lab=x_r4a_x2}
N -20 4200 -20 4200 {lab=x_clk}
C {devices/lab_pin.sym} -20 4200 0 1 {name=p782 sig_type=std_logic lab=x_clk}
N 20 4230 20 4230 {lab=0}
C {devices/lab_pin.sym} 20 4230 0 0 {name=p783 sig_type=std_logic lab=0}
N 20 4200 20 4200 {lab=0}
C {devices/lab_pin.sym} 20 4200 0 0 {name=p784 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 4200 0 0 {name=xr4ap4
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 4230 240 4230 {lab=x_r4}
C {devices/lab_pin.sym} 240 4230 0 0 {name=p785 sig_type=std_logic lab=x_r4}
N 200 4200 200 4200 {lab=x_r4a_b}
C {devices/lab_pin.sym} 200 4200 0 1 {name=p786 sig_type=std_logic lab=x_r4a_b}
N 240 4170 240 4170 {lab=vdg}
C {devices/lab_pin.sym} 240 4170 0 0 {name=p787 sig_type=std_logic lab=vdg}
N 240 4200 240 4200 {lab=vdg}
C {devices/lab_pin.sym} 240 4200 0 0 {name=p788 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 4200 0 0 {name=xr4an4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 4170 460 4170 {lab=x_r4}
C {devices/lab_pin.sym} 460 4170 0 0 {name=p789 sig_type=std_logic lab=x_r4}
N 420 4200 420 4200 {lab=x_clk}
C {devices/lab_pin.sym} 420 4200 0 1 {name=p790 sig_type=std_logic lab=x_clk}
N 460 4230 460 4230 {lab=x_r4a_x3}
C {devices/lab_pin.sym} 460 4230 0 0 {name=p791 sig_type=std_logic lab=x_r4a_x3}
N 460 4200 460 4200 {lab=0}
C {devices/lab_pin.sym} 460 4200 0 0 {name=p792 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 4200 0 0 {name=xr4an5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 4170 680 4170 {lab=x_r4a_x3}
C {devices/lab_pin.sym} 680 4170 0 0 {name=p793 sig_type=std_logic lab=x_r4a_x3}
N 640 4200 640 4200 {lab=x_r4a_b}
C {devices/lab_pin.sym} 640 4200 0 1 {name=p794 sig_type=std_logic lab=x_r4a_b}
N 680 4230 680 4230 {lab=0}
C {devices/lab_pin.sym} 680 4230 0 0 {name=p795 sig_type=std_logic lab=0}
N 680 4200 680 4200 {lab=0}
C {devices/lab_pin.sym} 680 4200 0 0 {name=p796 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 4200 0 0 {name=xr4bp1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 4230 900 4230 {lab=x_r4b_x1}
C {devices/lab_pin.sym} 900 4230 0 0 {name=p797 sig_type=std_logic lab=x_r4b_x1}
N 860 4200 860 4200 {lab=x_q4}
C {devices/lab_pin.sym} 860 4200 0 1 {name=p798 sig_type=std_logic lab=x_q4}
N 900 4170 900 4170 {lab=vdg}
C {devices/lab_pin.sym} 900 4170 0 0 {name=p799 sig_type=std_logic lab=vdg}
N 900 4200 900 4200 {lab=vdg}
C {devices/lab_pin.sym} 900 4200 0 0 {name=p800 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 4200 0 0 {name=xr4bp2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 4230 1120 4230 {lab=x_r4b_a}
C {devices/lab_pin.sym} 1120 4230 0 0 {name=p801 sig_type=std_logic lab=x_r4b_a}
N 1080 4200 1080 4200 {lab=x_clk}
C {devices/lab_pin.sym} 1080 4200 0 1 {name=p802 sig_type=std_logic lab=x_clk}
N 1120 4170 1120 4170 {lab=x_r4b_x1}
C {devices/lab_pin.sym} 1120 4170 0 0 {name=p803 sig_type=std_logic lab=x_r4b_x1}
N 1120 4200 1120 4200 {lab=vdg}
C {devices/lab_pin.sym} 1120 4200 0 0 {name=p804 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 4320 0 0 {name=xr4bn1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 4290 20 4290 {lab=x_r4b_a}
C {devices/lab_pin.sym} 20 4290 0 0 {name=p805 sig_type=std_logic lab=x_r4b_a}
N -20 4320 -20 4320 {lab=x_q4}
C {devices/lab_pin.sym} -20 4320 0 1 {name=p806 sig_type=std_logic lab=x_q4}
N 20 4350 20 4350 {lab=0}
C {devices/lab_pin.sym} 20 4350 0 0 {name=p807 sig_type=std_logic lab=0}
N 20 4320 20 4320 {lab=0}
C {devices/lab_pin.sym} 20 4320 0 0 {name=p808 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 4320 0 0 {name=xr4bp3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 4350 240 4350 {lab=x_r4b_b}
C {devices/lab_pin.sym} 240 4350 0 0 {name=p809 sig_type=std_logic lab=x_r4b_b}
N 200 4320 200 4320 {lab=x_clk}
C {devices/lab_pin.sym} 200 4320 0 1 {name=p810 sig_type=std_logic lab=x_clk}
N 240 4290 240 4290 {lab=vdg}
C {devices/lab_pin.sym} 240 4290 0 0 {name=p811 sig_type=std_logic lab=vdg}
N 240 4320 240 4320 {lab=vdg}
C {devices/lab_pin.sym} 240 4320 0 0 {name=p812 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 4320 0 0 {name=xr4bn2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 4290 460 4290 {lab=x_r4b_b}
C {devices/lab_pin.sym} 460 4290 0 0 {name=p813 sig_type=std_logic lab=x_r4b_b}
N 420 4320 420 4320 {lab=x_r4b_a}
C {devices/lab_pin.sym} 420 4320 0 1 {name=p814 sig_type=std_logic lab=x_r4b_a}
N 460 4350 460 4350 {lab=x_r4b_x2}
C {devices/lab_pin.sym} 460 4350 0 0 {name=p815 sig_type=std_logic lab=x_r4b_x2}
N 460 4320 460 4320 {lab=0}
C {devices/lab_pin.sym} 460 4320 0 0 {name=p816 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 4320 0 0 {name=xr4bn3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 4290 680 4290 {lab=x_r4b_x2}
C {devices/lab_pin.sym} 680 4290 0 0 {name=p817 sig_type=std_logic lab=x_r4b_x2}
N 640 4320 640 4320 {lab=x_clk}
C {devices/lab_pin.sym} 640 4320 0 1 {name=p818 sig_type=std_logic lab=x_clk}
N 680 4350 680 4350 {lab=0}
C {devices/lab_pin.sym} 680 4350 0 0 {name=p819 sig_type=std_logic lab=0}
N 680 4320 680 4320 {lab=0}
C {devices/lab_pin.sym} 680 4320 0 0 {name=p820 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 4320 0 0 {name=xr4bp4
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 4350 900 4350 {lab=x_r4b}
C {devices/lab_pin.sym} 900 4350 0 0 {name=p821 sig_type=std_logic lab=x_r4b}
N 860 4320 860 4320 {lab=x_r4b_b}
C {devices/lab_pin.sym} 860 4320 0 1 {name=p822 sig_type=std_logic lab=x_r4b_b}
N 900 4290 900 4290 {lab=vdg}
C {devices/lab_pin.sym} 900 4290 0 0 {name=p823 sig_type=std_logic lab=vdg}
N 900 4320 900 4320 {lab=vdg}
C {devices/lab_pin.sym} 900 4320 0 0 {name=p824 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 4320 0 0 {name=xr4bn4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 4290 1120 4290 {lab=x_r4b}
C {devices/lab_pin.sym} 1120 4290 0 0 {name=p825 sig_type=std_logic lab=x_r4b}
N 1080 4320 1080 4320 {lab=x_clk}
C {devices/lab_pin.sym} 1080 4320 0 1 {name=p826 sig_type=std_logic lab=x_clk}
N 1120 4350 1120 4350 {lab=x_r4b_x3}
C {devices/lab_pin.sym} 1120 4350 0 0 {name=p827 sig_type=std_logic lab=x_r4b_x3}
N 1120 4320 1120 4320 {lab=0}
C {devices/lab_pin.sym} 1120 4320 0 0 {name=p828 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 4440 0 0 {name=xr4bn5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 4410 20 4410 {lab=x_r4b_x3}
C {devices/lab_pin.sym} 20 4410 0 0 {name=p829 sig_type=std_logic lab=x_r4b_x3}
N -20 4440 -20 4440 {lab=x_r4b_b}
C {devices/lab_pin.sym} -20 4440 0 1 {name=p830 sig_type=std_logic lab=x_r4b_b}
N 20 4470 20 4470 {lab=0}
C {devices/lab_pin.sym} 20 4470 0 0 {name=p831 sig_type=std_logic lab=0}
N 20 4440 20 4440 {lab=0}
C {devices/lab_pin.sym} 20 4440 0 0 {name=p832 sig_type=std_logic lab=0}
C {devices/capa.sym} 220 4440 0 0 {name=cr4
value=10f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 220 4410 220 4410 {lab=x_r4}
C {devices/lab_pin.sym} 220 4410 0 0 {name=p833 sig_type=std_logic lab=x_r4}
N 220 4470 220 4470 {lab=0}
C {devices/lab_pin.sym} 220 4470 0 0 {name=p834 sig_type=std_logic lab=0}
C {devices/capa.sym} 440 4440 0 0 {name=crb4
value=10f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 440 4410 440 4410 {lab=x_r4b}
C {devices/lab_pin.sym} 440 4410 0 0 {name=p835 sig_type=std_logic lab=x_r4b}
N 440 4470 440 4470 {lab=0}
C {devices/lab_pin.sym} 440 4470 0 0 {name=p836 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 4440 0 0 {name=xf1kq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 4470 680 4470 {lab=x_f1_kq}
C {devices/lab_pin.sym} 680 4470 0 0 {name=p837 sig_type=std_logic lab=x_f1_kq}
N 640 4440 640 4440 {lab=x_q1}
C {devices/lab_pin.sym} 640 4440 0 1 {name=p838 sig_type=std_logic lab=x_q1}
N 680 4410 680 4410 {lab=vdg}
C {devices/lab_pin.sym} 680 4410 0 0 {name=p839 sig_type=std_logic lab=vdg}
N 680 4440 680 4440 {lab=vdg}
C {devices/lab_pin.sym} 680 4440 0 0 {name=p840 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 4440 0 0 {name=xf1kq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 4410 900 4410 {lab=x_f1_kq}
C {devices/lab_pin.sym} 900 4410 0 0 {name=p841 sig_type=std_logic lab=x_f1_kq}
N 860 4440 860 4440 {lab=x_q1}
C {devices/lab_pin.sym} 860 4440 0 1 {name=p842 sig_type=std_logic lab=x_q1}
N 900 4470 900 4470 {lab=0}
C {devices/lab_pin.sym} 900 4470 0 0 {name=p843 sig_type=std_logic lab=0}
N 900 4440 900 4440 {lab=0}
C {devices/lab_pin.sym} 900 4440 0 0 {name=p844 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 4440 0 0 {name=xf1kq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 4470 1120 4470 {lab=x_q1}
C {devices/lab_pin.sym} 1120 4470 0 0 {name=p845 sig_type=std_logic lab=x_q1}
N 1080 4440 1080 4440 {lab=x_f1_kq}
C {devices/lab_pin.sym} 1080 4440 0 1 {name=p846 sig_type=std_logic lab=x_f1_kq}
N 1120 4410 1120 4410 {lab=vdg}
C {devices/lab_pin.sym} 1120 4410 0 0 {name=p847 sig_type=std_logic lab=vdg}
N 1120 4440 1120 4440 {lab=vdg}
C {devices/lab_pin.sym} 1120 4440 0 0 {name=p848 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 4560 0 0 {name=xf1kq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 4530 20 4530 {lab=x_q1}
C {devices/lab_pin.sym} 20 4530 0 0 {name=p849 sig_type=std_logic lab=x_q1}
N -20 4560 -20 4560 {lab=x_f1_kq}
C {devices/lab_pin.sym} -20 4560 0 1 {name=p850 sig_type=std_logic lab=x_f1_kq}
N 20 4590 20 4590 {lab=0}
C {devices/lab_pin.sym} 20 4590 0 0 {name=p851 sig_type=std_logic lab=0}
N 20 4560 20 4560 {lab=0}
C {devices/lab_pin.sym} 20 4560 0 0 {name=p852 sig_type=std_logic lab=0}
C {devices/res.sym} 220 4560 0 0 {name=rkf11
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 4530 220 4530 {lab=x_f1_a}
C {devices/lab_pin.sym} 220 4530 0 0 {name=p853 sig_type=std_logic lab=x_f1_a}
N 220 4590 220 4590 {lab=0}
C {devices/lab_pin.sym} 220 4590 0 0 {name=p854 sig_type=std_logic lab=0}
C {devices/res.sym} 440 4560 0 0 {name=rkf12
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 440 4530 440 4530 {lab=x_f1_b}
C {devices/lab_pin.sym} 440 4530 0 0 {name=p855 sig_type=std_logic lab=x_f1_b}
N 440 4590 440 4590 {lab=0}
C {devices/lab_pin.sym} 440 4590 0 0 {name=p856 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 4560 0 0 {name=xf2kq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 4590 680 4590 {lab=x_f2_kq}
C {devices/lab_pin.sym} 680 4590 0 0 {name=p857 sig_type=std_logic lab=x_f2_kq}
N 640 4560 640 4560 {lab=x_q2}
C {devices/lab_pin.sym} 640 4560 0 1 {name=p858 sig_type=std_logic lab=x_q2}
N 680 4530 680 4530 {lab=vdg}
C {devices/lab_pin.sym} 680 4530 0 0 {name=p859 sig_type=std_logic lab=vdg}
N 680 4560 680 4560 {lab=vdg}
C {devices/lab_pin.sym} 680 4560 0 0 {name=p860 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 4560 0 0 {name=xf2kq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 4530 900 4530 {lab=x_f2_kq}
C {devices/lab_pin.sym} 900 4530 0 0 {name=p861 sig_type=std_logic lab=x_f2_kq}
N 860 4560 860 4560 {lab=x_q2}
C {devices/lab_pin.sym} 860 4560 0 1 {name=p862 sig_type=std_logic lab=x_q2}
N 900 4590 900 4590 {lab=0}
C {devices/lab_pin.sym} 900 4590 0 0 {name=p863 sig_type=std_logic lab=0}
N 900 4560 900 4560 {lab=0}
C {devices/lab_pin.sym} 900 4560 0 0 {name=p864 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 4560 0 0 {name=xf2kq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 4590 1120 4590 {lab=x_q2}
C {devices/lab_pin.sym} 1120 4590 0 0 {name=p865 sig_type=std_logic lab=x_q2}
N 1080 4560 1080 4560 {lab=x_f2_kq}
C {devices/lab_pin.sym} 1080 4560 0 1 {name=p866 sig_type=std_logic lab=x_f2_kq}
N 1120 4530 1120 4530 {lab=vdg}
C {devices/lab_pin.sym} 1120 4530 0 0 {name=p867 sig_type=std_logic lab=vdg}
N 1120 4560 1120 4560 {lab=vdg}
C {devices/lab_pin.sym} 1120 4560 0 0 {name=p868 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 4680 0 0 {name=xf2kq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 4650 20 4650 {lab=x_q2}
C {devices/lab_pin.sym} 20 4650 0 0 {name=p869 sig_type=std_logic lab=x_q2}
N -20 4680 -20 4680 {lab=x_f2_kq}
C {devices/lab_pin.sym} -20 4680 0 1 {name=p870 sig_type=std_logic lab=x_f2_kq}
N 20 4710 20 4710 {lab=0}
C {devices/lab_pin.sym} 20 4710 0 0 {name=p871 sig_type=std_logic lab=0}
N 20 4680 20 4680 {lab=0}
C {devices/lab_pin.sym} 20 4680 0 0 {name=p872 sig_type=std_logic lab=0}
C {devices/res.sym} 220 4680 0 0 {name=rkf21
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 4650 220 4650 {lab=x_f2_a}
C {devices/lab_pin.sym} 220 4650 0 0 {name=p873 sig_type=std_logic lab=x_f2_a}
N 220 4710 220 4710 {lab=0}
C {devices/lab_pin.sym} 220 4710 0 0 {name=p874 sig_type=std_logic lab=0}
C {devices/res.sym} 440 4680 0 0 {name=rkf22
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 440 4650 440 4650 {lab=x_f2_b}
C {devices/lab_pin.sym} 440 4650 0 0 {name=p875 sig_type=std_logic lab=x_f2_b}
N 440 4710 440 4710 {lab=0}
C {devices/lab_pin.sym} 440 4710 0 0 {name=p876 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 4680 0 0 {name=xf3kq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 4710 680 4710 {lab=x_f3_kq}
C {devices/lab_pin.sym} 680 4710 0 0 {name=p877 sig_type=std_logic lab=x_f3_kq}
N 640 4680 640 4680 {lab=x_q3}
C {devices/lab_pin.sym} 640 4680 0 1 {name=p878 sig_type=std_logic lab=x_q3}
N 680 4650 680 4650 {lab=vdg}
C {devices/lab_pin.sym} 680 4650 0 0 {name=p879 sig_type=std_logic lab=vdg}
N 680 4680 680 4680 {lab=vdg}
C {devices/lab_pin.sym} 680 4680 0 0 {name=p880 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 4680 0 0 {name=xf3kq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 4650 900 4650 {lab=x_f3_kq}
C {devices/lab_pin.sym} 900 4650 0 0 {name=p881 sig_type=std_logic lab=x_f3_kq}
N 860 4680 860 4680 {lab=x_q3}
C {devices/lab_pin.sym} 860 4680 0 1 {name=p882 sig_type=std_logic lab=x_q3}
N 900 4710 900 4710 {lab=0}
C {devices/lab_pin.sym} 900 4710 0 0 {name=p883 sig_type=std_logic lab=0}
N 900 4680 900 4680 {lab=0}
C {devices/lab_pin.sym} 900 4680 0 0 {name=p884 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 4680 0 0 {name=xf3kq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 4710 1120 4710 {lab=x_q3}
C {devices/lab_pin.sym} 1120 4710 0 0 {name=p885 sig_type=std_logic lab=x_q3}
N 1080 4680 1080 4680 {lab=x_f3_kq}
C {devices/lab_pin.sym} 1080 4680 0 1 {name=p886 sig_type=std_logic lab=x_f3_kq}
N 1120 4650 1120 4650 {lab=vdg}
C {devices/lab_pin.sym} 1120 4650 0 0 {name=p887 sig_type=std_logic lab=vdg}
N 1120 4680 1120 4680 {lab=vdg}
C {devices/lab_pin.sym} 1120 4680 0 0 {name=p888 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 4800 0 0 {name=xf3kq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 4770 20 4770 {lab=x_q3}
C {devices/lab_pin.sym} 20 4770 0 0 {name=p889 sig_type=std_logic lab=x_q3}
N -20 4800 -20 4800 {lab=x_f3_kq}
C {devices/lab_pin.sym} -20 4800 0 1 {name=p890 sig_type=std_logic lab=x_f3_kq}
N 20 4830 20 4830 {lab=0}
C {devices/lab_pin.sym} 20 4830 0 0 {name=p891 sig_type=std_logic lab=0}
N 20 4800 20 4800 {lab=0}
C {devices/lab_pin.sym} 20 4800 0 0 {name=p892 sig_type=std_logic lab=0}
C {devices/res.sym} 220 4800 0 0 {name=rkf31
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 4770 220 4770 {lab=x_f3_a}
C {devices/lab_pin.sym} 220 4770 0 0 {name=p893 sig_type=std_logic lab=x_f3_a}
N 220 4830 220 4830 {lab=0}
C {devices/lab_pin.sym} 220 4830 0 0 {name=p894 sig_type=std_logic lab=0}
C {devices/res.sym} 440 4800 0 0 {name=rkf32
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 440 4770 440 4770 {lab=x_f3_b}
C {devices/lab_pin.sym} 440 4770 0 0 {name=p895 sig_type=std_logic lab=x_f3_b}
N 440 4830 440 4830 {lab=0}
C {devices/lab_pin.sym} 440 4830 0 0 {name=p896 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 4800 0 0 {name=xf4kq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 4830 680 4830 {lab=x_f4_kq}
C {devices/lab_pin.sym} 680 4830 0 0 {name=p897 sig_type=std_logic lab=x_f4_kq}
N 640 4800 640 4800 {lab=x_q4}
C {devices/lab_pin.sym} 640 4800 0 1 {name=p898 sig_type=std_logic lab=x_q4}
N 680 4770 680 4770 {lab=vdg}
C {devices/lab_pin.sym} 680 4770 0 0 {name=p899 sig_type=std_logic lab=vdg}
N 680 4800 680 4800 {lab=vdg}
C {devices/lab_pin.sym} 680 4800 0 0 {name=p900 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 4800 0 0 {name=xf4kq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 4770 900 4770 {lab=x_f4_kq}
C {devices/lab_pin.sym} 900 4770 0 0 {name=p901 sig_type=std_logic lab=x_f4_kq}
N 860 4800 860 4800 {lab=x_q4}
C {devices/lab_pin.sym} 860 4800 0 1 {name=p902 sig_type=std_logic lab=x_q4}
N 900 4830 900 4830 {lab=0}
C {devices/lab_pin.sym} 900 4830 0 0 {name=p903 sig_type=std_logic lab=0}
N 900 4800 900 4800 {lab=0}
C {devices/lab_pin.sym} 900 4800 0 0 {name=p904 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 4800 0 0 {name=xf4kq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 4830 1120 4830 {lab=x_q4}
C {devices/lab_pin.sym} 1120 4830 0 0 {name=p905 sig_type=std_logic lab=x_q4}
N 1080 4800 1080 4800 {lab=x_f4_kq}
C {devices/lab_pin.sym} 1080 4800 0 1 {name=p906 sig_type=std_logic lab=x_f4_kq}
N 1120 4770 1120 4770 {lab=vdg}
C {devices/lab_pin.sym} 1120 4770 0 0 {name=p907 sig_type=std_logic lab=vdg}
N 1120 4800 1120 4800 {lab=vdg}
C {devices/lab_pin.sym} 1120 4800 0 0 {name=p908 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 4920 0 0 {name=xf4kq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 4890 20 4890 {lab=x_q4}
C {devices/lab_pin.sym} 20 4890 0 0 {name=p909 sig_type=std_logic lab=x_q4}
N -20 4920 -20 4920 {lab=x_f4_kq}
C {devices/lab_pin.sym} -20 4920 0 1 {name=p910 sig_type=std_logic lab=x_f4_kq}
N 20 4950 20 4950 {lab=0}
C {devices/lab_pin.sym} 20 4950 0 0 {name=p911 sig_type=std_logic lab=0}
N 20 4920 20 4920 {lab=0}
C {devices/lab_pin.sym} 20 4920 0 0 {name=p912 sig_type=std_logic lab=0}
C {devices/res.sym} 220 4920 0 0 {name=rkf41
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 4890 220 4890 {lab=x_f4_a}
C {devices/lab_pin.sym} 220 4890 0 0 {name=p913 sig_type=std_logic lab=x_f4_a}
N 220 4950 220 4950 {lab=0}
C {devices/lab_pin.sym} 220 4950 0 0 {name=p914 sig_type=std_logic lab=0}
C {devices/res.sym} 440 4920 0 0 {name=rkf42
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 440 4890 440 4890 {lab=x_f4_b}
C {devices/lab_pin.sym} 440 4890 0 0 {name=p915 sig_type=std_logic lab=x_f4_b}
N 440 4950 440 4950 {lab=0}
C {devices/lab_pin.sym} 440 4950 0 0 {name=p916 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 4920 0 0 {name=xr1akq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 4950 680 4950 {lab=x_r1a_kq}
C {devices/lab_pin.sym} 680 4950 0 0 {name=p917 sig_type=std_logic lab=x_r1a_kq}
N 640 4920 640 4920 {lab=x_r1}
C {devices/lab_pin.sym} 640 4920 0 1 {name=p918 sig_type=std_logic lab=x_r1}
N 680 4890 680 4890 {lab=vdg}
C {devices/lab_pin.sym} 680 4890 0 0 {name=p919 sig_type=std_logic lab=vdg}
N 680 4920 680 4920 {lab=vdg}
C {devices/lab_pin.sym} 680 4920 0 0 {name=p920 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 4920 0 0 {name=xr1akq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 4890 900 4890 {lab=x_r1a_kq}
C {devices/lab_pin.sym} 900 4890 0 0 {name=p921 sig_type=std_logic lab=x_r1a_kq}
N 860 4920 860 4920 {lab=x_r1}
C {devices/lab_pin.sym} 860 4920 0 1 {name=p922 sig_type=std_logic lab=x_r1}
N 900 4950 900 4950 {lab=0}
C {devices/lab_pin.sym} 900 4950 0 0 {name=p923 sig_type=std_logic lab=0}
N 900 4920 900 4920 {lab=0}
C {devices/lab_pin.sym} 900 4920 0 0 {name=p924 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 4920 0 0 {name=xr1akq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 4950 1120 4950 {lab=x_r1}
C {devices/lab_pin.sym} 1120 4950 0 0 {name=p925 sig_type=std_logic lab=x_r1}
N 1080 4920 1080 4920 {lab=x_r1a_kq}
C {devices/lab_pin.sym} 1080 4920 0 1 {name=p926 sig_type=std_logic lab=x_r1a_kq}
N 1120 4890 1120 4890 {lab=vdg}
C {devices/lab_pin.sym} 1120 4890 0 0 {name=p927 sig_type=std_logic lab=vdg}
N 1120 4920 1120 4920 {lab=vdg}
C {devices/lab_pin.sym} 1120 4920 0 0 {name=p928 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 5040 0 0 {name=xr1akq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 5010 20 5010 {lab=x_r1}
C {devices/lab_pin.sym} 20 5010 0 0 {name=p929 sig_type=std_logic lab=x_r1}
N -20 5040 -20 5040 {lab=x_r1a_kq}
C {devices/lab_pin.sym} -20 5040 0 1 {name=p930 sig_type=std_logic lab=x_r1a_kq}
N 20 5070 20 5070 {lab=0}
C {devices/lab_pin.sym} 20 5070 0 0 {name=p931 sig_type=std_logic lab=0}
N 20 5040 20 5040 {lab=0}
C {devices/lab_pin.sym} 20 5040 0 0 {name=p932 sig_type=std_logic lab=0}
C {devices/res.sym} 220 5040 0 0 {name=rkr1a1
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 5010 220 5010 {lab=x_r1a_a}
C {devices/lab_pin.sym} 220 5010 0 0 {name=p933 sig_type=std_logic lab=x_r1a_a}
N 220 5070 220 5070 {lab=0}
C {devices/lab_pin.sym} 220 5070 0 0 {name=p934 sig_type=std_logic lab=0}
C {devices/res.sym} 440 5040 0 0 {name=rkr1a2
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 440 5010 440 5010 {lab=x_r1a_b}
C {devices/lab_pin.sym} 440 5010 0 0 {name=p935 sig_type=std_logic lab=x_r1a_b}
N 440 5070 440 5070 {lab=0}
C {devices/lab_pin.sym} 440 5070 0 0 {name=p936 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 5040 0 0 {name=xr1bkq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 5070 680 5070 {lab=x_r1b_kq}
C {devices/lab_pin.sym} 680 5070 0 0 {name=p937 sig_type=std_logic lab=x_r1b_kq}
N 640 5040 640 5040 {lab=x_r1b}
C {devices/lab_pin.sym} 640 5040 0 1 {name=p938 sig_type=std_logic lab=x_r1b}
N 680 5010 680 5010 {lab=vdg}
C {devices/lab_pin.sym} 680 5010 0 0 {name=p939 sig_type=std_logic lab=vdg}
N 680 5040 680 5040 {lab=vdg}
C {devices/lab_pin.sym} 680 5040 0 0 {name=p940 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 5040 0 0 {name=xr1bkq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 5010 900 5010 {lab=x_r1b_kq}
C {devices/lab_pin.sym} 900 5010 0 0 {name=p941 sig_type=std_logic lab=x_r1b_kq}
N 860 5040 860 5040 {lab=x_r1b}
C {devices/lab_pin.sym} 860 5040 0 1 {name=p942 sig_type=std_logic lab=x_r1b}
N 900 5070 900 5070 {lab=0}
C {devices/lab_pin.sym} 900 5070 0 0 {name=p943 sig_type=std_logic lab=0}
N 900 5040 900 5040 {lab=0}
C {devices/lab_pin.sym} 900 5040 0 0 {name=p944 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 5040 0 0 {name=xr1bkq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 5070 1120 5070 {lab=x_r1b}
C {devices/lab_pin.sym} 1120 5070 0 0 {name=p945 sig_type=std_logic lab=x_r1b}
N 1080 5040 1080 5040 {lab=x_r1b_kq}
C {devices/lab_pin.sym} 1080 5040 0 1 {name=p946 sig_type=std_logic lab=x_r1b_kq}
N 1120 5010 1120 5010 {lab=vdg}
C {devices/lab_pin.sym} 1120 5010 0 0 {name=p947 sig_type=std_logic lab=vdg}
N 1120 5040 1120 5040 {lab=vdg}
C {devices/lab_pin.sym} 1120 5040 0 0 {name=p948 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 5160 0 0 {name=xr1bkq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 5130 20 5130 {lab=x_r1b}
C {devices/lab_pin.sym} 20 5130 0 0 {name=p949 sig_type=std_logic lab=x_r1b}
N -20 5160 -20 5160 {lab=x_r1b_kq}
C {devices/lab_pin.sym} -20 5160 0 1 {name=p950 sig_type=std_logic lab=x_r1b_kq}
N 20 5190 20 5190 {lab=0}
C {devices/lab_pin.sym} 20 5190 0 0 {name=p951 sig_type=std_logic lab=0}
N 20 5160 20 5160 {lab=0}
C {devices/lab_pin.sym} 20 5160 0 0 {name=p952 sig_type=std_logic lab=0}
C {devices/res.sym} 220 5160 0 0 {name=rkr1b1
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 5130 220 5130 {lab=x_r1b_a}
C {devices/lab_pin.sym} 220 5130 0 0 {name=p953 sig_type=std_logic lab=x_r1b_a}
N 220 5190 220 5190 {lab=0}
C {devices/lab_pin.sym} 220 5190 0 0 {name=p954 sig_type=std_logic lab=0}
C {devices/res.sym} 440 5160 0 0 {name=rkr1b2
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 440 5130 440 5130 {lab=x_r1b_b}
C {devices/lab_pin.sym} 440 5130 0 0 {name=p955 sig_type=std_logic lab=x_r1b_b}
N 440 5190 440 5190 {lab=0}
C {devices/lab_pin.sym} 440 5190 0 0 {name=p956 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 5160 0 0 {name=xr2akq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 5190 680 5190 {lab=x_r2a_kq}
C {devices/lab_pin.sym} 680 5190 0 0 {name=p957 sig_type=std_logic lab=x_r2a_kq}
N 640 5160 640 5160 {lab=x_r2}
C {devices/lab_pin.sym} 640 5160 0 1 {name=p958 sig_type=std_logic lab=x_r2}
N 680 5130 680 5130 {lab=vdg}
C {devices/lab_pin.sym} 680 5130 0 0 {name=p959 sig_type=std_logic lab=vdg}
N 680 5160 680 5160 {lab=vdg}
C {devices/lab_pin.sym} 680 5160 0 0 {name=p960 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 5160 0 0 {name=xr2akq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 5130 900 5130 {lab=x_r2a_kq}
C {devices/lab_pin.sym} 900 5130 0 0 {name=p961 sig_type=std_logic lab=x_r2a_kq}
N 860 5160 860 5160 {lab=x_r2}
C {devices/lab_pin.sym} 860 5160 0 1 {name=p962 sig_type=std_logic lab=x_r2}
N 900 5190 900 5190 {lab=0}
C {devices/lab_pin.sym} 900 5190 0 0 {name=p963 sig_type=std_logic lab=0}
N 900 5160 900 5160 {lab=0}
C {devices/lab_pin.sym} 900 5160 0 0 {name=p964 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 5160 0 0 {name=xr2akq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 5190 1120 5190 {lab=x_r2}
C {devices/lab_pin.sym} 1120 5190 0 0 {name=p965 sig_type=std_logic lab=x_r2}
N 1080 5160 1080 5160 {lab=x_r2a_kq}
C {devices/lab_pin.sym} 1080 5160 0 1 {name=p966 sig_type=std_logic lab=x_r2a_kq}
N 1120 5130 1120 5130 {lab=vdg}
C {devices/lab_pin.sym} 1120 5130 0 0 {name=p967 sig_type=std_logic lab=vdg}
N 1120 5160 1120 5160 {lab=vdg}
C {devices/lab_pin.sym} 1120 5160 0 0 {name=p968 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 5280 0 0 {name=xr2akq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 5250 20 5250 {lab=x_r2}
C {devices/lab_pin.sym} 20 5250 0 0 {name=p969 sig_type=std_logic lab=x_r2}
N -20 5280 -20 5280 {lab=x_r2a_kq}
C {devices/lab_pin.sym} -20 5280 0 1 {name=p970 sig_type=std_logic lab=x_r2a_kq}
N 20 5310 20 5310 {lab=0}
C {devices/lab_pin.sym} 20 5310 0 0 {name=p971 sig_type=std_logic lab=0}
N 20 5280 20 5280 {lab=0}
C {devices/lab_pin.sym} 20 5280 0 0 {name=p972 sig_type=std_logic lab=0}
C {devices/res.sym} 220 5280 0 0 {name=rkr2a1
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 5250 220 5250 {lab=x_r2a_a}
C {devices/lab_pin.sym} 220 5250 0 0 {name=p973 sig_type=std_logic lab=x_r2a_a}
N 220 5310 220 5310 {lab=0}
C {devices/lab_pin.sym} 220 5310 0 0 {name=p974 sig_type=std_logic lab=0}
C {devices/res.sym} 440 5280 0 0 {name=rkr2a2
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 440 5250 440 5250 {lab=x_r2a_b}
C {devices/lab_pin.sym} 440 5250 0 0 {name=p975 sig_type=std_logic lab=x_r2a_b}
N 440 5310 440 5310 {lab=0}
C {devices/lab_pin.sym} 440 5310 0 0 {name=p976 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 5280 0 0 {name=xr2bkq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 5310 680 5310 {lab=x_r2b_kq}
C {devices/lab_pin.sym} 680 5310 0 0 {name=p977 sig_type=std_logic lab=x_r2b_kq}
N 640 5280 640 5280 {lab=x_r2b}
C {devices/lab_pin.sym} 640 5280 0 1 {name=p978 sig_type=std_logic lab=x_r2b}
N 680 5250 680 5250 {lab=vdg}
C {devices/lab_pin.sym} 680 5250 0 0 {name=p979 sig_type=std_logic lab=vdg}
N 680 5280 680 5280 {lab=vdg}
C {devices/lab_pin.sym} 680 5280 0 0 {name=p980 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 5280 0 0 {name=xr2bkq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 5250 900 5250 {lab=x_r2b_kq}
C {devices/lab_pin.sym} 900 5250 0 0 {name=p981 sig_type=std_logic lab=x_r2b_kq}
N 860 5280 860 5280 {lab=x_r2b}
C {devices/lab_pin.sym} 860 5280 0 1 {name=p982 sig_type=std_logic lab=x_r2b}
N 900 5310 900 5310 {lab=0}
C {devices/lab_pin.sym} 900 5310 0 0 {name=p983 sig_type=std_logic lab=0}
N 900 5280 900 5280 {lab=0}
C {devices/lab_pin.sym} 900 5280 0 0 {name=p984 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 5280 0 0 {name=xr2bkq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 5310 1120 5310 {lab=x_r2b}
C {devices/lab_pin.sym} 1120 5310 0 0 {name=p985 sig_type=std_logic lab=x_r2b}
N 1080 5280 1080 5280 {lab=x_r2b_kq}
C {devices/lab_pin.sym} 1080 5280 0 1 {name=p986 sig_type=std_logic lab=x_r2b_kq}
N 1120 5250 1120 5250 {lab=vdg}
C {devices/lab_pin.sym} 1120 5250 0 0 {name=p987 sig_type=std_logic lab=vdg}
N 1120 5280 1120 5280 {lab=vdg}
C {devices/lab_pin.sym} 1120 5280 0 0 {name=p988 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 5400 0 0 {name=xr2bkq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 5370 20 5370 {lab=x_r2b}
C {devices/lab_pin.sym} 20 5370 0 0 {name=p989 sig_type=std_logic lab=x_r2b}
N -20 5400 -20 5400 {lab=x_r2b_kq}
C {devices/lab_pin.sym} -20 5400 0 1 {name=p990 sig_type=std_logic lab=x_r2b_kq}
N 20 5430 20 5430 {lab=0}
C {devices/lab_pin.sym} 20 5430 0 0 {name=p991 sig_type=std_logic lab=0}
N 20 5400 20 5400 {lab=0}
C {devices/lab_pin.sym} 20 5400 0 0 {name=p992 sig_type=std_logic lab=0}
C {devices/res.sym} 220 5400 0 0 {name=rkr2b1
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 5370 220 5370 {lab=x_r2b_a}
C {devices/lab_pin.sym} 220 5370 0 0 {name=p993 sig_type=std_logic lab=x_r2b_a}
N 220 5430 220 5430 {lab=0}
C {devices/lab_pin.sym} 220 5430 0 0 {name=p994 sig_type=std_logic lab=0}
C {devices/res.sym} 440 5400 0 0 {name=rkr2b2
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 440 5370 440 5370 {lab=x_r2b_b}
C {devices/lab_pin.sym} 440 5370 0 0 {name=p995 sig_type=std_logic lab=x_r2b_b}
N 440 5430 440 5430 {lab=0}
C {devices/lab_pin.sym} 440 5430 0 0 {name=p996 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 5400 0 0 {name=xr3akq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 5430 680 5430 {lab=x_r3a_kq}
C {devices/lab_pin.sym} 680 5430 0 0 {name=p997 sig_type=std_logic lab=x_r3a_kq}
N 640 5400 640 5400 {lab=x_r3}
C {devices/lab_pin.sym} 640 5400 0 1 {name=p998 sig_type=std_logic lab=x_r3}
N 680 5370 680 5370 {lab=vdg}
C {devices/lab_pin.sym} 680 5370 0 0 {name=p999 sig_type=std_logic lab=vdg}
N 680 5400 680 5400 {lab=vdg}
C {devices/lab_pin.sym} 680 5400 0 0 {name=p1000 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 5400 0 0 {name=xr3akq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 5370 900 5370 {lab=x_r3a_kq}
C {devices/lab_pin.sym} 900 5370 0 0 {name=p1001 sig_type=std_logic lab=x_r3a_kq}
N 860 5400 860 5400 {lab=x_r3}
C {devices/lab_pin.sym} 860 5400 0 1 {name=p1002 sig_type=std_logic lab=x_r3}
N 900 5430 900 5430 {lab=0}
C {devices/lab_pin.sym} 900 5430 0 0 {name=p1003 sig_type=std_logic lab=0}
N 900 5400 900 5400 {lab=0}
C {devices/lab_pin.sym} 900 5400 0 0 {name=p1004 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 5400 0 0 {name=xr3akq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 5430 1120 5430 {lab=x_r3}
C {devices/lab_pin.sym} 1120 5430 0 0 {name=p1005 sig_type=std_logic lab=x_r3}
N 1080 5400 1080 5400 {lab=x_r3a_kq}
C {devices/lab_pin.sym} 1080 5400 0 1 {name=p1006 sig_type=std_logic lab=x_r3a_kq}
N 1120 5370 1120 5370 {lab=vdg}
C {devices/lab_pin.sym} 1120 5370 0 0 {name=p1007 sig_type=std_logic lab=vdg}
N 1120 5400 1120 5400 {lab=vdg}
C {devices/lab_pin.sym} 1120 5400 0 0 {name=p1008 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 5520 0 0 {name=xr3akq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 5490 20 5490 {lab=x_r3}
C {devices/lab_pin.sym} 20 5490 0 0 {name=p1009 sig_type=std_logic lab=x_r3}
N -20 5520 -20 5520 {lab=x_r3a_kq}
C {devices/lab_pin.sym} -20 5520 0 1 {name=p1010 sig_type=std_logic lab=x_r3a_kq}
N 20 5550 20 5550 {lab=0}
C {devices/lab_pin.sym} 20 5550 0 0 {name=p1011 sig_type=std_logic lab=0}
N 20 5520 20 5520 {lab=0}
C {devices/lab_pin.sym} 20 5520 0 0 {name=p1012 sig_type=std_logic lab=0}
C {devices/res.sym} 220 5520 0 0 {name=rkr3a1
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 5490 220 5490 {lab=x_r3a_a}
C {devices/lab_pin.sym} 220 5490 0 0 {name=p1013 sig_type=std_logic lab=x_r3a_a}
N 220 5550 220 5550 {lab=0}
C {devices/lab_pin.sym} 220 5550 0 0 {name=p1014 sig_type=std_logic lab=0}
C {devices/res.sym} 440 5520 0 0 {name=rkr3a2
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 440 5490 440 5490 {lab=x_r3a_b}
C {devices/lab_pin.sym} 440 5490 0 0 {name=p1015 sig_type=std_logic lab=x_r3a_b}
N 440 5550 440 5550 {lab=0}
C {devices/lab_pin.sym} 440 5550 0 0 {name=p1016 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 5520 0 0 {name=xr3bkq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 5550 680 5550 {lab=x_r3b_kq}
C {devices/lab_pin.sym} 680 5550 0 0 {name=p1017 sig_type=std_logic lab=x_r3b_kq}
N 640 5520 640 5520 {lab=x_r3b}
C {devices/lab_pin.sym} 640 5520 0 1 {name=p1018 sig_type=std_logic lab=x_r3b}
N 680 5490 680 5490 {lab=vdg}
C {devices/lab_pin.sym} 680 5490 0 0 {name=p1019 sig_type=std_logic lab=vdg}
N 680 5520 680 5520 {lab=vdg}
C {devices/lab_pin.sym} 680 5520 0 0 {name=p1020 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 5520 0 0 {name=xr3bkq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 5490 900 5490 {lab=x_r3b_kq}
C {devices/lab_pin.sym} 900 5490 0 0 {name=p1021 sig_type=std_logic lab=x_r3b_kq}
N 860 5520 860 5520 {lab=x_r3b}
C {devices/lab_pin.sym} 860 5520 0 1 {name=p1022 sig_type=std_logic lab=x_r3b}
N 900 5550 900 5550 {lab=0}
C {devices/lab_pin.sym} 900 5550 0 0 {name=p1023 sig_type=std_logic lab=0}
N 900 5520 900 5520 {lab=0}
C {devices/lab_pin.sym} 900 5520 0 0 {name=p1024 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 5520 0 0 {name=xr3bkq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 5550 1120 5550 {lab=x_r3b}
C {devices/lab_pin.sym} 1120 5550 0 0 {name=p1025 sig_type=std_logic lab=x_r3b}
N 1080 5520 1080 5520 {lab=x_r3b_kq}
C {devices/lab_pin.sym} 1080 5520 0 1 {name=p1026 sig_type=std_logic lab=x_r3b_kq}
N 1120 5490 1120 5490 {lab=vdg}
C {devices/lab_pin.sym} 1120 5490 0 0 {name=p1027 sig_type=std_logic lab=vdg}
N 1120 5520 1120 5520 {lab=vdg}
C {devices/lab_pin.sym} 1120 5520 0 0 {name=p1028 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 5640 0 0 {name=xr3bkq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 5610 20 5610 {lab=x_r3b}
C {devices/lab_pin.sym} 20 5610 0 0 {name=p1029 sig_type=std_logic lab=x_r3b}
N -20 5640 -20 5640 {lab=x_r3b_kq}
C {devices/lab_pin.sym} -20 5640 0 1 {name=p1030 sig_type=std_logic lab=x_r3b_kq}
N 20 5670 20 5670 {lab=0}
C {devices/lab_pin.sym} 20 5670 0 0 {name=p1031 sig_type=std_logic lab=0}
N 20 5640 20 5640 {lab=0}
C {devices/lab_pin.sym} 20 5640 0 0 {name=p1032 sig_type=std_logic lab=0}
C {devices/res.sym} 220 5640 0 0 {name=rkr3b1
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 5610 220 5610 {lab=x_r3b_a}
C {devices/lab_pin.sym} 220 5610 0 0 {name=p1033 sig_type=std_logic lab=x_r3b_a}
N 220 5670 220 5670 {lab=0}
C {devices/lab_pin.sym} 220 5670 0 0 {name=p1034 sig_type=std_logic lab=0}
C {devices/res.sym} 440 5640 0 0 {name=rkr3b2
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 440 5610 440 5610 {lab=x_r3b_b}
C {devices/lab_pin.sym} 440 5610 0 0 {name=p1035 sig_type=std_logic lab=x_r3b_b}
N 440 5670 440 5670 {lab=0}
C {devices/lab_pin.sym} 440 5670 0 0 {name=p1036 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 5640 0 0 {name=xr4akq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 5670 680 5670 {lab=x_r4a_kq}
C {devices/lab_pin.sym} 680 5670 0 0 {name=p1037 sig_type=std_logic lab=x_r4a_kq}
N 640 5640 640 5640 {lab=x_r4}
C {devices/lab_pin.sym} 640 5640 0 1 {name=p1038 sig_type=std_logic lab=x_r4}
N 680 5610 680 5610 {lab=vdg}
C {devices/lab_pin.sym} 680 5610 0 0 {name=p1039 sig_type=std_logic lab=vdg}
N 680 5640 680 5640 {lab=vdg}
C {devices/lab_pin.sym} 680 5640 0 0 {name=p1040 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 5640 0 0 {name=xr4akq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 5610 900 5610 {lab=x_r4a_kq}
C {devices/lab_pin.sym} 900 5610 0 0 {name=p1041 sig_type=std_logic lab=x_r4a_kq}
N 860 5640 860 5640 {lab=x_r4}
C {devices/lab_pin.sym} 860 5640 0 1 {name=p1042 sig_type=std_logic lab=x_r4}
N 900 5670 900 5670 {lab=0}
C {devices/lab_pin.sym} 900 5670 0 0 {name=p1043 sig_type=std_logic lab=0}
N 900 5640 900 5640 {lab=0}
C {devices/lab_pin.sym} 900 5640 0 0 {name=p1044 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 5640 0 0 {name=xr4akq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 5670 1120 5670 {lab=x_r4}
C {devices/lab_pin.sym} 1120 5670 0 0 {name=p1045 sig_type=std_logic lab=x_r4}
N 1080 5640 1080 5640 {lab=x_r4a_kq}
C {devices/lab_pin.sym} 1080 5640 0 1 {name=p1046 sig_type=std_logic lab=x_r4a_kq}
N 1120 5610 1120 5610 {lab=vdg}
C {devices/lab_pin.sym} 1120 5610 0 0 {name=p1047 sig_type=std_logic lab=vdg}
N 1120 5640 1120 5640 {lab=vdg}
C {devices/lab_pin.sym} 1120 5640 0 0 {name=p1048 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 5760 0 0 {name=xr4akq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 5730 20 5730 {lab=x_r4}
C {devices/lab_pin.sym} 20 5730 0 0 {name=p1049 sig_type=std_logic lab=x_r4}
N -20 5760 -20 5760 {lab=x_r4a_kq}
C {devices/lab_pin.sym} -20 5760 0 1 {name=p1050 sig_type=std_logic lab=x_r4a_kq}
N 20 5790 20 5790 {lab=0}
C {devices/lab_pin.sym} 20 5790 0 0 {name=p1051 sig_type=std_logic lab=0}
N 20 5760 20 5760 {lab=0}
C {devices/lab_pin.sym} 20 5760 0 0 {name=p1052 sig_type=std_logic lab=0}
C {devices/res.sym} 220 5760 0 0 {name=rkr4a1
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 5730 220 5730 {lab=x_r4a_a}
C {devices/lab_pin.sym} 220 5730 0 0 {name=p1053 sig_type=std_logic lab=x_r4a_a}
N 220 5790 220 5790 {lab=0}
C {devices/lab_pin.sym} 220 5790 0 0 {name=p1054 sig_type=std_logic lab=0}
C {devices/res.sym} 440 5760 0 0 {name=rkr4a2
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 440 5730 440 5730 {lab=x_r4a_b}
C {devices/lab_pin.sym} 440 5730 0 0 {name=p1055 sig_type=std_logic lab=x_r4a_b}
N 440 5790 440 5790 {lab=0}
C {devices/lab_pin.sym} 440 5790 0 0 {name=p1056 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 5760 0 0 {name=xr4bkq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 5790 680 5790 {lab=x_r4b_kq}
C {devices/lab_pin.sym} 680 5790 0 0 {name=p1057 sig_type=std_logic lab=x_r4b_kq}
N 640 5760 640 5760 {lab=x_r4b}
C {devices/lab_pin.sym} 640 5760 0 1 {name=p1058 sig_type=std_logic lab=x_r4b}
N 680 5730 680 5730 {lab=vdg}
C {devices/lab_pin.sym} 680 5730 0 0 {name=p1059 sig_type=std_logic lab=vdg}
N 680 5760 680 5760 {lab=vdg}
C {devices/lab_pin.sym} 680 5760 0 0 {name=p1060 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 5760 0 0 {name=xr4bkq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 5730 900 5730 {lab=x_r4b_kq}
C {devices/lab_pin.sym} 900 5730 0 0 {name=p1061 sig_type=std_logic lab=x_r4b_kq}
N 860 5760 860 5760 {lab=x_r4b}
C {devices/lab_pin.sym} 860 5760 0 1 {name=p1062 sig_type=std_logic lab=x_r4b}
N 900 5790 900 5790 {lab=0}
C {devices/lab_pin.sym} 900 5790 0 0 {name=p1063 sig_type=std_logic lab=0}
N 900 5760 900 5760 {lab=0}
C {devices/lab_pin.sym} 900 5760 0 0 {name=p1064 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 5760 0 0 {name=xr4bkq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 5790 1120 5790 {lab=x_r4b}
C {devices/lab_pin.sym} 1120 5790 0 0 {name=p1065 sig_type=std_logic lab=x_r4b}
N 1080 5760 1080 5760 {lab=x_r4b_kq}
C {devices/lab_pin.sym} 1080 5760 0 1 {name=p1066 sig_type=std_logic lab=x_r4b_kq}
N 1120 5730 1120 5730 {lab=vdg}
C {devices/lab_pin.sym} 1120 5730 0 0 {name=p1067 sig_type=std_logic lab=vdg}
N 1120 5760 1120 5760 {lab=vdg}
C {devices/lab_pin.sym} 1120 5760 0 0 {name=p1068 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 5880 0 0 {name=xr4bkq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 5850 20 5850 {lab=x_r4b}
C {devices/lab_pin.sym} 20 5850 0 0 {name=p1069 sig_type=std_logic lab=x_r4b}
N -20 5880 -20 5880 {lab=x_r4b_kq}
C {devices/lab_pin.sym} -20 5880 0 1 {name=p1070 sig_type=std_logic lab=x_r4b_kq}
N 20 5910 20 5910 {lab=0}
C {devices/lab_pin.sym} 20 5910 0 0 {name=p1071 sig_type=std_logic lab=0}
N 20 5880 20 5880 {lab=0}
C {devices/lab_pin.sym} 20 5880 0 0 {name=p1072 sig_type=std_logic lab=0}
C {devices/res.sym} 220 5880 0 0 {name=rkr4b1
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 5850 220 5850 {lab=x_r4b_a}
C {devices/lab_pin.sym} 220 5850 0 0 {name=p1073 sig_type=std_logic lab=x_r4b_a}
N 220 5910 220 5910 {lab=0}
C {devices/lab_pin.sym} 220 5910 0 0 {name=p1074 sig_type=std_logic lab=0}
C {devices/res.sym} 440 5880 0 0 {name=rkr4b2
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 440 5850 440 5850 {lab=x_r4b_b}
C {devices/lab_pin.sym} 440 5850 0 0 {name=p1075 sig_type=std_logic lab=x_r4b_b}
N 440 5910 440 5910 {lab=0}
C {devices/lab_pin.sym} 440 5910 0 0 {name=p1076 sig_type=std_logic lab=0}
