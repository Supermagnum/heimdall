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
C {devices/iopin.sym} -200 -200 0 0 {name=x_p0 lab=x_p0}
C {devices/iopin.sym} -200 -240 0 0 {name=x_p1 lab=x_p1}
C {devices/iopin.sym} -200 -280 0 0 {name=x_p2 lab=x_p2}
C {devices/iopin.sym} -200 -320 0 0 {name=x_p3 lab=x_p3}
C {devices/iopin.sym} -200 -360 0 0 {name=vbuf lab=vbuf}
C {devices/iopin.sym} -200 -400 0 0 {name=vdv lab=vdv}
C {devices/iopin.sym} -200 -440 0 0 {name=vcv lab=vcv}
C {devices/iopin.sym} -200 -480 0 0 {name=vdg lab=vdg}
C {devices/iopin.sym} -200 -520 0 0 {name=vdd lab=vdd}
C {devices/iopin.sym} -200 -560 0 0 {name=0 lab=0}
C {devices/title.sym} 0 40 0 0 {name=t1 author="HT13G-M P2.7.1"}
C {devices/lab_pin.sym} 200 40 0 0 {name=ttitle lab=lo_uhf_top_flat}
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
C {devices/res.sym} 660 600 0 0 {name=rlamp
value=666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 660 570 660 570 {lab=vdv}
C {devices/lab_pin.sym} 660 570 0 0 {name=p117 sig_type=std_logic lab=vdv}
N 660 630 660 630 {lab=map}
C {devices/lab_pin.sym} 660 630 0 0 {name=p118 sig_type=std_logic lab=map}
C {devices/res.sym} 880 600 0 0 {name=rlamn
value=666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 570 880 570 {lab=vdv}
C {devices/lab_pin.sym} 880 570 0 0 {name=p119 sig_type=std_logic lab=vdv}
N 880 630 880 630 {lab=man}
C {devices/lab_pin.sym} 880 630 0 0 {name=p120 sig_type=std_logic lab=man}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 600 0 0 {name=mam1
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 570 1120 570 {lab=man}
C {devices/lab_pin.sym} 1120 570 0 0 {name=p121 sig_type=std_logic lab=man}
N 1080 600 1080 600 {lab=qn}
C {devices/lab_pin.sym} 1080 600 0 1 {name=p122 sig_type=std_logic lab=qn}
N 1120 630 1120 630 {lab=s1am}
C {devices/lab_pin.sym} 1120 630 0 0 {name=p123 sig_type=std_logic lab=s1am}
N 1120 600 1120 600 {lab=0}
C {devices/lab_pin.sym} 1120 600 0 0 {name=p124 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 720 0 0 {name=mam2
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 690 20 690 {lab=map}
C {devices/lab_pin.sym} 20 690 0 0 {name=p125 sig_type=std_logic lab=map}
N -20 720 -20 720 {lab=qp}
C {devices/lab_pin.sym} -20 720 0 1 {name=p126 sig_type=std_logic lab=qp}
N 20 750 20 750 {lab=s1am}
C {devices/lab_pin.sym} 20 750 0 0 {name=p127 sig_type=std_logic lab=s1am}
N 20 720 20 720 {lab=0}
C {devices/lab_pin.sym} 20 720 0 0 {name=p128 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 720 0 0 {name=mam3
w=11.25u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 690 240 690 {lab=man}
C {devices/lab_pin.sym} 240 690 0 0 {name=p129 sig_type=std_logic lab=man}
N 200 720 200 720 {lab=map}
C {devices/lab_pin.sym} 200 720 0 1 {name=p130 sig_type=std_logic lab=map}
N 240 750 240 750 {lab=s2am}
C {devices/lab_pin.sym} 240 750 0 0 {name=p131 sig_type=std_logic lab=s2am}
N 240 720 240 720 {lab=0}
C {devices/lab_pin.sym} 240 720 0 0 {name=p132 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 720 0 0 {name=mam4
w=11.25u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 690 460 690 {lab=map}
C {devices/lab_pin.sym} 460 690 0 0 {name=p133 sig_type=std_logic lab=map}
N 420 720 420 720 {lab=man}
C {devices/lab_pin.sym} 420 720 0 1 {name=p134 sig_type=std_logic lab=man}
N 460 750 460 750 {lab=s2am}
C {devices/lab_pin.sym} 460 750 0 0 {name=p135 sig_type=std_logic lab=s2am}
N 460 720 460 720 {lab=0}
C {devices/lab_pin.sym} 460 720 0 0 {name=p136 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 720 0 0 {name=mam5
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 690 680 690 {lab=s1am}
C {devices/lab_pin.sym} 680 690 0 0 {name=p137 sig_type=std_logic lab=s1am}
N 640 720 640 720 {lab=ckp}
C {devices/lab_pin.sym} 640 720 0 1 {name=p138 sig_type=std_logic lab=ckp}
N 680 750 680 750 {lab=tam}
C {devices/lab_pin.sym} 680 750 0 0 {name=p139 sig_type=std_logic lab=tam}
N 680 720 680 720 {lab=0}
C {devices/lab_pin.sym} 680 720 0 0 {name=p140 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 720 0 0 {name=mam6
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 690 900 690 {lab=s2am}
C {devices/lab_pin.sym} 900 690 0 0 {name=p141 sig_type=std_logic lab=s2am}
N 860 720 860 720 {lab=ckn}
C {devices/lab_pin.sym} 860 720 0 1 {name=p142 sig_type=std_logic lab=ckn}
N 900 750 900 750 {lab=tam}
C {devices/lab_pin.sym} 900 750 0 0 {name=p143 sig_type=std_logic lab=tam}
N 900 720 900 720 {lab=0}
C {devices/lab_pin.sym} 900 720 0 0 {name=p144 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 720 0 0 {name=mtam
w=15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 690 1120 690 {lab=tam}
C {devices/lab_pin.sym} 1120 690 0 0 {name=p145 sig_type=std_logic lab=tam}
N 1080 720 1080 720 {lab=nb_lo}
C {devices/lab_pin.sym} 1080 720 0 1 {name=p146 sig_type=std_logic lab=nb_lo}
N 1120 750 1120 750 {lab=0}
C {devices/lab_pin.sym} 1120 750 0 0 {name=p147 sig_type=std_logic lab=0}
N 1120 720 1120 720 {lab=0}
C {devices/lab_pin.sym} 1120 720 0 0 {name=p148 sig_type=std_logic lab=0}
C {devices/res.sym} 0 840 0 0 {name=rlasp
value=666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 0 810 0 810 {lab=vdv}
C {devices/lab_pin.sym} 0 810 0 0 {name=p149 sig_type=std_logic lab=vdv}
N 0 870 0 870 {lab=qp}
C {devices/lab_pin.sym} 0 870 0 0 {name=p150 sig_type=std_logic lab=qp}
C {devices/res.sym} 220 840 0 0 {name=rlasn
value=666.7
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 220 810 220 810 {lab=vdv}
C {devices/lab_pin.sym} 220 810 0 0 {name=p151 sig_type=std_logic lab=vdv}
N 220 870 220 870 {lab=qn}
C {devices/lab_pin.sym} 220 870 0 0 {name=p152 sig_type=std_logic lab=qn}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 840 0 0 {name=mas1
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 810 460 810 {lab=qn}
C {devices/lab_pin.sym} 460 810 0 0 {name=p153 sig_type=std_logic lab=qn}
N 420 840 420 840 {lab=map}
C {devices/lab_pin.sym} 420 840 0 1 {name=p154 sig_type=std_logic lab=map}
N 460 870 460 870 {lab=s1as}
C {devices/lab_pin.sym} 460 870 0 0 {name=p155 sig_type=std_logic lab=s1as}
N 460 840 460 840 {lab=0}
C {devices/lab_pin.sym} 460 840 0 0 {name=p156 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 840 0 0 {name=mas2
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 810 680 810 {lab=qp}
C {devices/lab_pin.sym} 680 810 0 0 {name=p157 sig_type=std_logic lab=qp}
N 640 840 640 840 {lab=man}
C {devices/lab_pin.sym} 640 840 0 1 {name=p158 sig_type=std_logic lab=man}
N 680 870 680 870 {lab=s1as}
C {devices/lab_pin.sym} 680 870 0 0 {name=p159 sig_type=std_logic lab=s1as}
N 680 840 680 840 {lab=0}
C {devices/lab_pin.sym} 680 840 0 0 {name=p160 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 840 0 0 {name=mas3
w=11.25u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 810 900 810 {lab=qn}
C {devices/lab_pin.sym} 900 810 0 0 {name=p161 sig_type=std_logic lab=qn}
N 860 840 860 840 {lab=qp}
C {devices/lab_pin.sym} 860 840 0 1 {name=p162 sig_type=std_logic lab=qp}
N 900 870 900 870 {lab=s2as}
C {devices/lab_pin.sym} 900 870 0 0 {name=p163 sig_type=std_logic lab=s2as}
N 900 840 900 840 {lab=0}
C {devices/lab_pin.sym} 900 840 0 0 {name=p164 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 840 0 0 {name=mas4
w=11.25u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 810 1120 810 {lab=qp}
C {devices/lab_pin.sym} 1120 810 0 0 {name=p165 sig_type=std_logic lab=qp}
N 1080 840 1080 840 {lab=qn}
C {devices/lab_pin.sym} 1080 840 0 1 {name=p166 sig_type=std_logic lab=qn}
N 1120 870 1120 870 {lab=s2as}
C {devices/lab_pin.sym} 1120 870 0 0 {name=p167 sig_type=std_logic lab=s2as}
N 1120 840 1120 840 {lab=0}
C {devices/lab_pin.sym} 1120 840 0 0 {name=p168 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 960 0 0 {name=mas5
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 930 20 930 {lab=s1as}
C {devices/lab_pin.sym} 20 930 0 0 {name=p169 sig_type=std_logic lab=s1as}
N -20 960 -20 960 {lab=ckn}
C {devices/lab_pin.sym} -20 960 0 1 {name=p170 sig_type=std_logic lab=ckn}
N 20 990 20 990 {lab=tas}
C {devices/lab_pin.sym} 20 990 0 0 {name=p171 sig_type=std_logic lab=tas}
N 20 960 20 960 {lab=0}
C {devices/lab_pin.sym} 20 960 0 0 {name=p172 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 960 0 0 {name=mas6
w=7.50u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 930 240 930 {lab=s2as}
C {devices/lab_pin.sym} 240 930 0 0 {name=p173 sig_type=std_logic lab=s2as}
N 200 960 200 960 {lab=ckp}
C {devices/lab_pin.sym} 200 960 0 1 {name=p174 sig_type=std_logic lab=ckp}
N 240 990 240 990 {lab=tas}
C {devices/lab_pin.sym} 240 990 0 0 {name=p175 sig_type=std_logic lab=tas}
N 240 960 240 960 {lab=0}
C {devices/lab_pin.sym} 240 960 0 0 {name=p176 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 960 0 0 {name=mtas
w=15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 930 460 930 {lab=tas}
C {devices/lab_pin.sym} 460 930 0 0 {name=p177 sig_type=std_logic lab=tas}
N 420 960 420 960 {lab=nb_lo}
C {devices/lab_pin.sym} 420 960 0 1 {name=p178 sig_type=std_logic lab=nb_lo}
N 460 990 460 990 {lab=0}
C {devices/lab_pin.sym} 460 990 0 0 {name=p179 sig_type=std_logic lab=0}
N 460 960 460 960 {lab=0}
C {devices/lab_pin.sym} 460 960 0 0 {name=p180 sig_type=std_logic lab=0}
C {devices/capa.sym} 660 960 0 0 {name=ccap
value=50f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 660 930 660 930 {lab=qp}
C {devices/lab_pin.sym} 660 930 0 0 {name=p181 sig_type=std_logic lab=qp}
N 660 990 660 990 {lab=x_cip}
C {devices/lab_pin.sym} 660 990 0 0 {name=p182 sig_type=std_logic lab=x_cip}
C {devices/res.sym} 880 960 0 0 {name=rcap
value=50k
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 930 880 930 {lab=x_cip}
C {devices/lab_pin.sym} 880 930 0 0 {name=p183 sig_type=std_logic lab=x_cip}
N 880 990 880 990 {lab=x_o2p}
C {devices/lab_pin.sym} 880 990 0 0 {name=p184 sig_type=std_logic lab=x_o2p}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 960 0 0 {name=xcapp
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 990 1120 990 {lab=x_o2p}
C {devices/lab_pin.sym} 1120 990 0 0 {name=p185 sig_type=std_logic lab=x_o2p}
N 1080 960 1080 960 {lab=x_cip}
C {devices/lab_pin.sym} 1080 960 0 1 {name=p186 sig_type=std_logic lab=x_cip}
N 1120 930 1120 930 {lab=vcv}
C {devices/lab_pin.sym} 1120 930 0 0 {name=p187 sig_type=std_logic lab=vcv}
N 1120 960 1120 960 {lab=vcv}
C {devices/lab_pin.sym} 1120 960 0 0 {name=p188 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 1080 0 0 {name=xcapn
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 1050 20 1050 {lab=x_o2p}
C {devices/lab_pin.sym} 20 1050 0 0 {name=p189 sig_type=std_logic lab=x_o2p}
N -20 1080 -20 1080 {lab=x_cip}
C {devices/lab_pin.sym} -20 1080 0 1 {name=p190 sig_type=std_logic lab=x_cip}
N 20 1110 20 1110 {lab=0}
C {devices/lab_pin.sym} 20 1110 0 0 {name=p191 sig_type=std_logic lab=0}
N 20 1080 20 1080 {lab=0}
C {devices/lab_pin.sym} 20 1080 0 0 {name=p192 sig_type=std_logic lab=0}
C {devices/capa.sym} 220 1080 0 0 {name=ccan
value=50f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 220 1050 220 1050 {lab=qn}
C {devices/lab_pin.sym} 220 1050 0 0 {name=p193 sig_type=std_logic lab=qn}
N 220 1110 220 1110 {lab=x_cin}
C {devices/lab_pin.sym} 220 1110 0 0 {name=p194 sig_type=std_logic lab=x_cin}
C {devices/res.sym} 440 1080 0 0 {name=rcan
value=50k
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 440 1050 440 1050 {lab=x_cin}
C {devices/lab_pin.sym} 440 1050 0 0 {name=p195 sig_type=std_logic lab=x_cin}
N 440 1110 440 1110 {lab=x_o2n}
C {devices/lab_pin.sym} 440 1110 0 0 {name=p196 sig_type=std_logic lab=x_o2n}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 1080 0 0 {name=xcanp
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 1110 680 1110 {lab=x_o2n}
C {devices/lab_pin.sym} 680 1110 0 0 {name=p197 sig_type=std_logic lab=x_o2n}
N 640 1080 640 1080 {lab=x_cin}
C {devices/lab_pin.sym} 640 1080 0 1 {name=p198 sig_type=std_logic lab=x_cin}
N 680 1050 680 1050 {lab=vcv}
C {devices/lab_pin.sym} 680 1050 0 0 {name=p199 sig_type=std_logic lab=vcv}
N 680 1080 680 1080 {lab=vcv}
C {devices/lab_pin.sym} 680 1080 0 0 {name=p200 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 1080 0 0 {name=xcann
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 1050 900 1050 {lab=x_o2n}
C {devices/lab_pin.sym} 900 1050 0 0 {name=p201 sig_type=std_logic lab=x_o2n}
N 860 1080 860 1080 {lab=x_cin}
C {devices/lab_pin.sym} 860 1080 0 1 {name=p202 sig_type=std_logic lab=x_cin}
N 900 1110 900 1110 {lab=0}
C {devices/lab_pin.sym} 900 1110 0 0 {name=p203 sig_type=std_logic lab=0}
N 900 1080 900 1080 {lab=0}
C {devices/lab_pin.sym} 900 1080 0 0 {name=p204 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 1080 0 0 {name=xcxpp
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 1110 1120 1110 {lab=x_o2n}
C {devices/lab_pin.sym} 1120 1110 0 0 {name=p205 sig_type=std_logic lab=x_o2n}
N 1080 1080 1080 1080 {lab=x_o2p}
C {devices/lab_pin.sym} 1080 1080 0 1 {name=p206 sig_type=std_logic lab=x_o2p}
N 1120 1050 1120 1050 {lab=vcv}
C {devices/lab_pin.sym} 1120 1050 0 0 {name=p207 sig_type=std_logic lab=vcv}
N 1120 1080 1120 1080 {lab=vcv}
C {devices/lab_pin.sym} 1120 1080 0 0 {name=p208 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 1200 0 0 {name=xcxpn
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 1170 20 1170 {lab=x_o2n}
C {devices/lab_pin.sym} 20 1170 0 0 {name=p209 sig_type=std_logic lab=x_o2n}
N -20 1200 -20 1200 {lab=x_o2p}
C {devices/lab_pin.sym} -20 1200 0 1 {name=p210 sig_type=std_logic lab=x_o2p}
N 20 1230 20 1230 {lab=0}
C {devices/lab_pin.sym} 20 1230 0 0 {name=p211 sig_type=std_logic lab=0}
N 20 1200 20 1200 {lab=0}
C {devices/lab_pin.sym} 20 1200 0 0 {name=p212 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 1200 0 0 {name=xcxnp
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 1230 240 1230 {lab=x_o2p}
C {devices/lab_pin.sym} 240 1230 0 0 {name=p213 sig_type=std_logic lab=x_o2p}
N 200 1200 200 1200 {lab=x_o2n}
C {devices/lab_pin.sym} 200 1200 0 1 {name=p214 sig_type=std_logic lab=x_o2n}
N 240 1170 240 1170 {lab=vcv}
C {devices/lab_pin.sym} 240 1170 0 0 {name=p215 sig_type=std_logic lab=vcv}
N 240 1200 240 1200 {lab=vcv}
C {devices/lab_pin.sym} 240 1200 0 0 {name=p216 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 1200 0 0 {name=xcxnn
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 1170 460 1170 {lab=x_o2p}
C {devices/lab_pin.sym} 460 1170 0 0 {name=p217 sig_type=std_logic lab=x_o2p}
N 420 1200 420 1200 {lab=x_o2n}
C {devices/lab_pin.sym} 420 1200 0 1 {name=p218 sig_type=std_logic lab=x_o2n}
N 460 1230 460 1230 {lab=0}
C {devices/lab_pin.sym} 460 1230 0 0 {name=p219 sig_type=std_logic lab=0}
N 460 1200 460 1200 {lab=0}
C {devices/lab_pin.sym} 460 1200 0 0 {name=p220 sig_type=std_logic lab=0}
C {devices/capa.sym} 660 1200 0 0 {name=ccb
value=50f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 660 1170 660 1170 {lab=x_o2p}
C {devices/lab_pin.sym} 660 1170 0 0 {name=p221 sig_type=std_logic lab=x_o2p}
N 660 1230 660 1230 {lab=x_cbi}
C {devices/lab_pin.sym} 660 1230 0 0 {name=p222 sig_type=std_logic lab=x_cbi}
C {devices/res.sym} 880 1200 0 0 {name=rcb
value=50k
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 1170 880 1170 {lab=x_cbi}
C {devices/lab_pin.sym} 880 1170 0 0 {name=p223 sig_type=std_logic lab=x_cbi}
N 880 1230 880 1230 {lab=x_cy}
C {devices/lab_pin.sym} 880 1230 0 0 {name=p224 sig_type=std_logic lab=x_cy}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 1200 0 0 {name=xcbp
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 1230 1120 1230 {lab=x_cy}
C {devices/lab_pin.sym} 1120 1230 0 0 {name=p225 sig_type=std_logic lab=x_cy}
N 1080 1200 1080 1200 {lab=x_cbi}
C {devices/lab_pin.sym} 1080 1200 0 1 {name=p226 sig_type=std_logic lab=x_cbi}
N 1120 1170 1120 1170 {lab=vcv}
C {devices/lab_pin.sym} 1120 1170 0 0 {name=p227 sig_type=std_logic lab=vcv}
N 1120 1200 1120 1200 {lab=vcv}
C {devices/lab_pin.sym} 1120 1200 0 0 {name=p228 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 1320 0 0 {name=xcbn
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 1290 20 1290 {lab=x_cy}
C {devices/lab_pin.sym} 20 1290 0 0 {name=p229 sig_type=std_logic lab=x_cy}
N -20 1320 -20 1320 {lab=x_cbi}
C {devices/lab_pin.sym} -20 1320 0 1 {name=p230 sig_type=std_logic lab=x_cbi}
N 20 1350 20 1350 {lab=0}
C {devices/lab_pin.sym} 20 1350 0 0 {name=p231 sig_type=std_logic lab=0}
N 20 1320 20 1320 {lab=0}
C {devices/lab_pin.sym} 20 1320 0 0 {name=p232 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 1320 0 0 {name=xcv3p
w=6.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 1350 240 1350 {lab=x_cz}
C {devices/lab_pin.sym} 240 1350 0 0 {name=p233 sig_type=std_logic lab=x_cz}
N 200 1320 200 1320 {lab=x_cy}
C {devices/lab_pin.sym} 200 1320 0 1 {name=p234 sig_type=std_logic lab=x_cy}
N 240 1290 240 1290 {lab=vcv}
C {devices/lab_pin.sym} 240 1290 0 0 {name=p235 sig_type=std_logic lab=vcv}
N 240 1320 240 1320 {lab=vcv}
C {devices/lab_pin.sym} 240 1320 0 0 {name=p236 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 1320 0 0 {name=xcv3n
w=3.0u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 1290 460 1290 {lab=x_cz}
C {devices/lab_pin.sym} 460 1290 0 0 {name=p237 sig_type=std_logic lab=x_cz}
N 420 1320 420 1320 {lab=x_cy}
C {devices/lab_pin.sym} 420 1320 0 1 {name=p238 sig_type=std_logic lab=x_cy}
N 460 1350 460 1350 {lab=0}
C {devices/lab_pin.sym} 460 1350 0 0 {name=p239 sig_type=std_logic lab=0}
N 460 1320 460 1320 {lab=0}
C {devices/lab_pin.sym} 460 1320 0 0 {name=p240 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 1320 0 0 {name=xcv4p
w=18.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 1350 680 1350 {lab=x_clk}
C {devices/lab_pin.sym} 680 1350 0 0 {name=p241 sig_type=std_logic lab=x_clk}
N 640 1320 640 1320 {lab=x_cz}
C {devices/lab_pin.sym} 640 1320 0 1 {name=p242 sig_type=std_logic lab=x_cz}
N 680 1290 680 1290 {lab=vcv}
C {devices/lab_pin.sym} 680 1290 0 0 {name=p243 sig_type=std_logic lab=vcv}
N 680 1320 680 1320 {lab=vcv}
C {devices/lab_pin.sym} 680 1320 0 0 {name=p244 sig_type=std_logic lab=vcv}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 1320 0 0 {name=xcv4n
w=9.0u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 1290 900 1290 {lab=x_clk}
C {devices/lab_pin.sym} 900 1290 0 0 {name=p245 sig_type=std_logic lab=x_clk}
N 860 1320 860 1320 {lab=x_cz}
C {devices/lab_pin.sym} 860 1320 0 1 {name=p246 sig_type=std_logic lab=x_cz}
N 900 1350 900 1350 {lab=0}
C {devices/lab_pin.sym} 900 1350 0 0 {name=p247 sig_type=std_logic lab=0}
N 900 1320 900 1320 {lab=0}
C {devices/lab_pin.sym} 900 1320 0 0 {name=p248 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 1320 0 0 {name=xf1p1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 1350 1120 1350 {lab=x_f1_x1}
C {devices/lab_pin.sym} 1120 1350 0 0 {name=p249 sig_type=std_logic lab=x_f1_x1}
N 1080 1320 1080 1320 {lab=x_q2}
C {devices/lab_pin.sym} 1080 1320 0 1 {name=p250 sig_type=std_logic lab=x_q2}
N 1120 1290 1120 1290 {lab=vdg}
C {devices/lab_pin.sym} 1120 1290 0 0 {name=p251 sig_type=std_logic lab=vdg}
N 1120 1320 1120 1320 {lab=vdg}
C {devices/lab_pin.sym} 1120 1320 0 0 {name=p252 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 1440 0 0 {name=xf1p2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 1470 20 1470 {lab=x_f1_a}
C {devices/lab_pin.sym} 20 1470 0 0 {name=p253 sig_type=std_logic lab=x_f1_a}
N -20 1440 -20 1440 {lab=x_clk}
C {devices/lab_pin.sym} -20 1440 0 1 {name=p254 sig_type=std_logic lab=x_clk}
N 20 1410 20 1410 {lab=x_f1_x1}
C {devices/lab_pin.sym} 20 1410 0 0 {name=p255 sig_type=std_logic lab=x_f1_x1}
N 20 1440 20 1440 {lab=vdg}
C {devices/lab_pin.sym} 20 1440 0 0 {name=p256 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 1440 0 0 {name=xf1n1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 1410 240 1410 {lab=x_f1_a}
C {devices/lab_pin.sym} 240 1410 0 0 {name=p257 sig_type=std_logic lab=x_f1_a}
N 200 1440 200 1440 {lab=x_q2}
C {devices/lab_pin.sym} 200 1440 0 1 {name=p258 sig_type=std_logic lab=x_q2}
N 240 1470 240 1470 {lab=0}
C {devices/lab_pin.sym} 240 1470 0 0 {name=p259 sig_type=std_logic lab=0}
N 240 1440 240 1440 {lab=0}
C {devices/lab_pin.sym} 240 1440 0 0 {name=p260 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 1440 0 0 {name=xf1p3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 1470 460 1470 {lab=x_f1_b}
C {devices/lab_pin.sym} 460 1470 0 0 {name=p261 sig_type=std_logic lab=x_f1_b}
N 420 1440 420 1440 {lab=x_clk}
C {devices/lab_pin.sym} 420 1440 0 1 {name=p262 sig_type=std_logic lab=x_clk}
N 460 1410 460 1410 {lab=vdg}
C {devices/lab_pin.sym} 460 1410 0 0 {name=p263 sig_type=std_logic lab=vdg}
N 460 1440 460 1440 {lab=vdg}
C {devices/lab_pin.sym} 460 1440 0 0 {name=p264 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 1440 0 0 {name=xf1n2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 1410 680 1410 {lab=x_f1_b}
C {devices/lab_pin.sym} 680 1410 0 0 {name=p265 sig_type=std_logic lab=x_f1_b}
N 640 1440 640 1440 {lab=x_f1_a}
C {devices/lab_pin.sym} 640 1440 0 1 {name=p266 sig_type=std_logic lab=x_f1_a}
N 680 1470 680 1470 {lab=x_f1_x2}
C {devices/lab_pin.sym} 680 1470 0 0 {name=p267 sig_type=std_logic lab=x_f1_x2}
N 680 1440 680 1440 {lab=0}
C {devices/lab_pin.sym} 680 1440 0 0 {name=p268 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 1440 0 0 {name=xf1n3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 1410 900 1410 {lab=x_f1_x2}
C {devices/lab_pin.sym} 900 1410 0 0 {name=p269 sig_type=std_logic lab=x_f1_x2}
N 860 1440 860 1440 {lab=x_clk}
C {devices/lab_pin.sym} 860 1440 0 1 {name=p270 sig_type=std_logic lab=x_clk}
N 900 1470 900 1470 {lab=0}
C {devices/lab_pin.sym} 900 1470 0 0 {name=p271 sig_type=std_logic lab=0}
N 900 1440 900 1440 {lab=0}
C {devices/lab_pin.sym} 900 1440 0 0 {name=p272 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 1440 0 0 {name=xf1p4
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 1470 1120 1470 {lab=x_q1}
C {devices/lab_pin.sym} 1120 1470 0 0 {name=p273 sig_type=std_logic lab=x_q1}
N 1080 1440 1080 1440 {lab=x_f1_b}
C {devices/lab_pin.sym} 1080 1440 0 1 {name=p274 sig_type=std_logic lab=x_f1_b}
N 1120 1410 1120 1410 {lab=vdg}
C {devices/lab_pin.sym} 1120 1410 0 0 {name=p275 sig_type=std_logic lab=vdg}
N 1120 1440 1120 1440 {lab=vdg}
C {devices/lab_pin.sym} 1120 1440 0 0 {name=p276 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 1560 0 0 {name=xf1n4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 1530 20 1530 {lab=x_q1}
C {devices/lab_pin.sym} 20 1530 0 0 {name=p277 sig_type=std_logic lab=x_q1}
N -20 1560 -20 1560 {lab=x_clk}
C {devices/lab_pin.sym} -20 1560 0 1 {name=p278 sig_type=std_logic lab=x_clk}
N 20 1590 20 1590 {lab=x_f1_x3}
C {devices/lab_pin.sym} 20 1590 0 0 {name=p279 sig_type=std_logic lab=x_f1_x3}
N 20 1560 20 1560 {lab=0}
C {devices/lab_pin.sym} 20 1560 0 0 {name=p280 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 1560 0 0 {name=xf1n5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 1530 240 1530 {lab=x_f1_x3}
C {devices/lab_pin.sym} 240 1530 0 0 {name=p281 sig_type=std_logic lab=x_f1_x3}
N 200 1560 200 1560 {lab=x_f1_b}
C {devices/lab_pin.sym} 200 1560 0 1 {name=p282 sig_type=std_logic lab=x_f1_b}
N 240 1590 240 1590 {lab=0}
C {devices/lab_pin.sym} 240 1590 0 0 {name=p283 sig_type=std_logic lab=0}
N 240 1560 240 1560 {lab=0}
C {devices/lab_pin.sym} 240 1560 0 0 {name=p284 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 1560 0 0 {name=xi1p
w=1.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 1590 460 1590 {lab=x_q1b}
C {devices/lab_pin.sym} 460 1590 0 0 {name=p285 sig_type=std_logic lab=x_q1b}
N 420 1560 420 1560 {lab=x_q1}
C {devices/lab_pin.sym} 420 1560 0 1 {name=p286 sig_type=std_logic lab=x_q1}
N 460 1530 460 1530 {lab=vdg}
C {devices/lab_pin.sym} 460 1530 0 0 {name=p287 sig_type=std_logic lab=vdg}
N 460 1560 460 1560 {lab=vdg}
C {devices/lab_pin.sym} 460 1560 0 0 {name=p288 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 1560 0 0 {name=xi1n
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 1530 680 1530 {lab=x_q1b}
C {devices/lab_pin.sym} 680 1530 0 0 {name=p289 sig_type=std_logic lab=x_q1b}
N 640 1560 640 1560 {lab=x_q1}
C {devices/lab_pin.sym} 640 1560 0 1 {name=p290 sig_type=std_logic lab=x_q1}
N 680 1590 680 1590 {lab=0}
C {devices/lab_pin.sym} 680 1590 0 0 {name=p291 sig_type=std_logic lab=0}
N 680 1560 680 1560 {lab=0}
C {devices/lab_pin.sym} 680 1560 0 0 {name=p292 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 1560 0 0 {name=xf2p1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 1590 900 1590 {lab=x_f2_x1}
C {devices/lab_pin.sym} 900 1590 0 0 {name=p293 sig_type=std_logic lab=x_f2_x1}
N 860 1560 860 1560 {lab=x_q1b}
C {devices/lab_pin.sym} 860 1560 0 1 {name=p294 sig_type=std_logic lab=x_q1b}
N 900 1530 900 1530 {lab=vdg}
C {devices/lab_pin.sym} 900 1530 0 0 {name=p295 sig_type=std_logic lab=vdg}
N 900 1560 900 1560 {lab=vdg}
C {devices/lab_pin.sym} 900 1560 0 0 {name=p296 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 1560 0 0 {name=xf2p2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 1590 1120 1590 {lab=x_f2_a}
C {devices/lab_pin.sym} 1120 1590 0 0 {name=p297 sig_type=std_logic lab=x_f2_a}
N 1080 1560 1080 1560 {lab=x_clk}
C {devices/lab_pin.sym} 1080 1560 0 1 {name=p298 sig_type=std_logic lab=x_clk}
N 1120 1530 1120 1530 {lab=x_f2_x1}
C {devices/lab_pin.sym} 1120 1530 0 0 {name=p299 sig_type=std_logic lab=x_f2_x1}
N 1120 1560 1120 1560 {lab=vdg}
C {devices/lab_pin.sym} 1120 1560 0 0 {name=p300 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 1680 0 0 {name=xf2n1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 1650 20 1650 {lab=x_f2_a}
C {devices/lab_pin.sym} 20 1650 0 0 {name=p301 sig_type=std_logic lab=x_f2_a}
N -20 1680 -20 1680 {lab=x_q1b}
C {devices/lab_pin.sym} -20 1680 0 1 {name=p302 sig_type=std_logic lab=x_q1b}
N 20 1710 20 1710 {lab=0}
C {devices/lab_pin.sym} 20 1710 0 0 {name=p303 sig_type=std_logic lab=0}
N 20 1680 20 1680 {lab=0}
C {devices/lab_pin.sym} 20 1680 0 0 {name=p304 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 1680 0 0 {name=xf2p3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 1710 240 1710 {lab=x_f2_b}
C {devices/lab_pin.sym} 240 1710 0 0 {name=p305 sig_type=std_logic lab=x_f2_b}
N 200 1680 200 1680 {lab=x_clk}
C {devices/lab_pin.sym} 200 1680 0 1 {name=p306 sig_type=std_logic lab=x_clk}
N 240 1650 240 1650 {lab=vdg}
C {devices/lab_pin.sym} 240 1650 0 0 {name=p307 sig_type=std_logic lab=vdg}
N 240 1680 240 1680 {lab=vdg}
C {devices/lab_pin.sym} 240 1680 0 0 {name=p308 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 1680 0 0 {name=xf2n2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 1650 460 1650 {lab=x_f2_b}
C {devices/lab_pin.sym} 460 1650 0 0 {name=p309 sig_type=std_logic lab=x_f2_b}
N 420 1680 420 1680 {lab=x_f2_a}
C {devices/lab_pin.sym} 420 1680 0 1 {name=p310 sig_type=std_logic lab=x_f2_a}
N 460 1710 460 1710 {lab=x_f2_x2}
C {devices/lab_pin.sym} 460 1710 0 0 {name=p311 sig_type=std_logic lab=x_f2_x2}
N 460 1680 460 1680 {lab=0}
C {devices/lab_pin.sym} 460 1680 0 0 {name=p312 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 1680 0 0 {name=xf2n3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 1650 680 1650 {lab=x_f2_x2}
C {devices/lab_pin.sym} 680 1650 0 0 {name=p313 sig_type=std_logic lab=x_f2_x2}
N 640 1680 640 1680 {lab=x_clk}
C {devices/lab_pin.sym} 640 1680 0 1 {name=p314 sig_type=std_logic lab=x_clk}
N 680 1710 680 1710 {lab=0}
C {devices/lab_pin.sym} 680 1710 0 0 {name=p315 sig_type=std_logic lab=0}
N 680 1680 680 1680 {lab=0}
C {devices/lab_pin.sym} 680 1680 0 0 {name=p316 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 1680 0 0 {name=xf2p4
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 1710 900 1710 {lab=x_q2}
C {devices/lab_pin.sym} 900 1710 0 0 {name=p317 sig_type=std_logic lab=x_q2}
N 860 1680 860 1680 {lab=x_f2_b}
C {devices/lab_pin.sym} 860 1680 0 1 {name=p318 sig_type=std_logic lab=x_f2_b}
N 900 1650 900 1650 {lab=vdg}
C {devices/lab_pin.sym} 900 1650 0 0 {name=p319 sig_type=std_logic lab=vdg}
N 900 1680 900 1680 {lab=vdg}
C {devices/lab_pin.sym} 900 1680 0 0 {name=p320 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 1680 0 0 {name=xf2n4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 1650 1120 1650 {lab=x_q2}
C {devices/lab_pin.sym} 1120 1650 0 0 {name=p321 sig_type=std_logic lab=x_q2}
N 1080 1680 1080 1680 {lab=x_clk}
C {devices/lab_pin.sym} 1080 1680 0 1 {name=p322 sig_type=std_logic lab=x_clk}
N 1120 1710 1120 1710 {lab=x_f2_x3}
C {devices/lab_pin.sym} 1120 1710 0 0 {name=p323 sig_type=std_logic lab=x_f2_x3}
N 1120 1680 1120 1680 {lab=0}
C {devices/lab_pin.sym} 1120 1680 0 0 {name=p324 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 1800 0 0 {name=xf2n5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 1770 20 1770 {lab=x_f2_x3}
C {devices/lab_pin.sym} 20 1770 0 0 {name=p325 sig_type=std_logic lab=x_f2_x3}
N -20 1800 -20 1800 {lab=x_f2_b}
C {devices/lab_pin.sym} -20 1800 0 1 {name=p326 sig_type=std_logic lab=x_f2_b}
N 20 1830 20 1830 {lab=0}
C {devices/lab_pin.sym} 20 1830 0 0 {name=p327 sig_type=std_logic lab=0}
N 20 1800 20 1800 {lab=0}
C {devices/lab_pin.sym} 20 1800 0 0 {name=p328 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 1800 0 0 {name=xi2p
w=1.0u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 1830 240 1830 {lab=x_q2b}
C {devices/lab_pin.sym} 240 1830 0 0 {name=p329 sig_type=std_logic lab=x_q2b}
N 200 1800 200 1800 {lab=x_q2}
C {devices/lab_pin.sym} 200 1800 0 1 {name=p330 sig_type=std_logic lab=x_q2}
N 240 1770 240 1770 {lab=vdg}
C {devices/lab_pin.sym} 240 1770 0 0 {name=p331 sig_type=std_logic lab=vdg}
N 240 1800 240 1800 {lab=vdg}
C {devices/lab_pin.sym} 240 1800 0 0 {name=p332 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 1800 0 0 {name=xi2n
w=0.5u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 1770 460 1770 {lab=x_q2b}
C {devices/lab_pin.sym} 460 1770 0 0 {name=p333 sig_type=std_logic lab=x_q2b}
N 420 1800 420 1800 {lab=x_q2}
C {devices/lab_pin.sym} 420 1800 0 1 {name=p334 sig_type=std_logic lab=x_q2}
N 460 1830 460 1830 {lab=0}
C {devices/lab_pin.sym} 460 1830 0 0 {name=p335 sig_type=std_logic lab=0}
N 460 1800 460 1800 {lab=0}
C {devices/lab_pin.sym} 460 1800 0 0 {name=p336 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 1800 0 0 {name=xg0pa
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 1830 680 1830 {lab=x_n0}
C {devices/lab_pin.sym} 680 1830 0 0 {name=p337 sig_type=std_logic lab=x_n0}
N 640 1800 640 1800 {lab=x_q1}
C {devices/lab_pin.sym} 640 1800 0 1 {name=p338 sig_type=std_logic lab=x_q1}
N 680 1770 680 1770 {lab=vdg}
C {devices/lab_pin.sym} 680 1770 0 0 {name=p339 sig_type=std_logic lab=vdg}
N 680 1800 680 1800 {lab=vdg}
C {devices/lab_pin.sym} 680 1800 0 0 {name=p340 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 1800 0 0 {name=xg0pb
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 1830 900 1830 {lab=x_n0}
C {devices/lab_pin.sym} 900 1830 0 0 {name=p341 sig_type=std_logic lab=x_n0}
N 860 1800 860 1800 {lab=x_q2b}
C {devices/lab_pin.sym} 860 1800 0 1 {name=p342 sig_type=std_logic lab=x_q2b}
N 900 1770 900 1770 {lab=vdg}
C {devices/lab_pin.sym} 900 1770 0 0 {name=p343 sig_type=std_logic lab=vdg}
N 900 1800 900 1800 {lab=vdg}
C {devices/lab_pin.sym} 900 1800 0 0 {name=p344 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 1800 0 0 {name=xg0na
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 1770 1120 1770 {lab=x_n0}
C {devices/lab_pin.sym} 1120 1770 0 0 {name=p345 sig_type=std_logic lab=x_n0}
N 1080 1800 1080 1800 {lab=x_q1}
C {devices/lab_pin.sym} 1080 1800 0 1 {name=p346 sig_type=std_logic lab=x_q1}
N 1120 1830 1120 1830 {lab=x_g0m}
C {devices/lab_pin.sym} 1120 1830 0 0 {name=p347 sig_type=std_logic lab=x_g0m}
N 1120 1800 1120 1800 {lab=0}
C {devices/lab_pin.sym} 1120 1800 0 0 {name=p348 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 1920 0 0 {name=xg0nb
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 1890 20 1890 {lab=x_g0m}
C {devices/lab_pin.sym} 20 1890 0 0 {name=p349 sig_type=std_logic lab=x_g0m}
N -20 1920 -20 1920 {lab=x_q2b}
C {devices/lab_pin.sym} -20 1920 0 1 {name=p350 sig_type=std_logic lab=x_q2b}
N 20 1950 20 1950 {lab=0}
C {devices/lab_pin.sym} 20 1950 0 0 {name=p351 sig_type=std_logic lab=0}
N 20 1920 20 1920 {lab=0}
C {devices/lab_pin.sym} 20 1920 0 0 {name=p352 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 1920 0 0 {name=xr0p1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 1950 240 1950 {lab=x_r0_x1}
C {devices/lab_pin.sym} 240 1950 0 0 {name=p353 sig_type=std_logic lab=x_r0_x1}
N 200 1920 200 1920 {lab=x_n0}
C {devices/lab_pin.sym} 200 1920 0 1 {name=p354 sig_type=std_logic lab=x_n0}
N 240 1890 240 1890 {lab=vdg}
C {devices/lab_pin.sym} 240 1890 0 0 {name=p355 sig_type=std_logic lab=vdg}
N 240 1920 240 1920 {lab=vdg}
C {devices/lab_pin.sym} 240 1920 0 0 {name=p356 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 1920 0 0 {name=xr0p2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 1950 460 1950 {lab=x_r0_a}
C {devices/lab_pin.sym} 460 1950 0 0 {name=p357 sig_type=std_logic lab=x_r0_a}
N 420 1920 420 1920 {lab=x_clk}
C {devices/lab_pin.sym} 420 1920 0 1 {name=p358 sig_type=std_logic lab=x_clk}
N 460 1890 460 1890 {lab=x_r0_x1}
C {devices/lab_pin.sym} 460 1890 0 0 {name=p359 sig_type=std_logic lab=x_r0_x1}
N 460 1920 460 1920 {lab=vdg}
C {devices/lab_pin.sym} 460 1920 0 0 {name=p360 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 1920 0 0 {name=xr0n1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 1890 680 1890 {lab=x_r0_a}
C {devices/lab_pin.sym} 680 1890 0 0 {name=p361 sig_type=std_logic lab=x_r0_a}
N 640 1920 640 1920 {lab=x_n0}
C {devices/lab_pin.sym} 640 1920 0 1 {name=p362 sig_type=std_logic lab=x_n0}
N 680 1950 680 1950 {lab=0}
C {devices/lab_pin.sym} 680 1950 0 0 {name=p363 sig_type=std_logic lab=0}
N 680 1920 680 1920 {lab=0}
C {devices/lab_pin.sym} 680 1920 0 0 {name=p364 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 1920 0 0 {name=xr0p3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 1950 900 1950 {lab=x_r0_b}
C {devices/lab_pin.sym} 900 1950 0 0 {name=p365 sig_type=std_logic lab=x_r0_b}
N 860 1920 860 1920 {lab=x_clk}
C {devices/lab_pin.sym} 860 1920 0 1 {name=p366 sig_type=std_logic lab=x_clk}
N 900 1890 900 1890 {lab=vdg}
C {devices/lab_pin.sym} 900 1890 0 0 {name=p367 sig_type=std_logic lab=vdg}
N 900 1920 900 1920 {lab=vdg}
C {devices/lab_pin.sym} 900 1920 0 0 {name=p368 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 1920 0 0 {name=xr0n2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 1890 1120 1890 {lab=x_r0_b}
C {devices/lab_pin.sym} 1120 1890 0 0 {name=p369 sig_type=std_logic lab=x_r0_b}
N 1080 1920 1080 1920 {lab=x_r0_a}
C {devices/lab_pin.sym} 1080 1920 0 1 {name=p370 sig_type=std_logic lab=x_r0_a}
N 1120 1950 1120 1950 {lab=x_r0_x2}
C {devices/lab_pin.sym} 1120 1950 0 0 {name=p371 sig_type=std_logic lab=x_r0_x2}
N 1120 1920 1120 1920 {lab=0}
C {devices/lab_pin.sym} 1120 1920 0 0 {name=p372 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 2040 0 0 {name=xr0n3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 2010 20 2010 {lab=x_r0_x2}
C {devices/lab_pin.sym} 20 2010 0 0 {name=p373 sig_type=std_logic lab=x_r0_x2}
N -20 2040 -20 2040 {lab=x_clk}
C {devices/lab_pin.sym} -20 2040 0 1 {name=p374 sig_type=std_logic lab=x_clk}
N 20 2070 20 2070 {lab=0}
C {devices/lab_pin.sym} 20 2070 0 0 {name=p375 sig_type=std_logic lab=0}
N 20 2040 20 2040 {lab=0}
C {devices/lab_pin.sym} 20 2040 0 0 {name=p376 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 2040 0 0 {name=xr0p4
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 2070 240 2070 {lab=x_p0}
C {devices/lab_pin.sym} 240 2070 0 0 {name=p377 sig_type=std_logic lab=x_p0}
N 200 2040 200 2040 {lab=x_r0_b}
C {devices/lab_pin.sym} 200 2040 0 1 {name=p378 sig_type=std_logic lab=x_r0_b}
N 240 2010 240 2010 {lab=vdg}
C {devices/lab_pin.sym} 240 2010 0 0 {name=p379 sig_type=std_logic lab=vdg}
N 240 2040 240 2040 {lab=vdg}
C {devices/lab_pin.sym} 240 2040 0 0 {name=p380 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 2040 0 0 {name=xr0n4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 2010 460 2010 {lab=x_p0}
C {devices/lab_pin.sym} 460 2010 0 0 {name=p381 sig_type=std_logic lab=x_p0}
N 420 2040 420 2040 {lab=x_clk}
C {devices/lab_pin.sym} 420 2040 0 1 {name=p382 sig_type=std_logic lab=x_clk}
N 460 2070 460 2070 {lab=x_r0_x3}
C {devices/lab_pin.sym} 460 2070 0 0 {name=p383 sig_type=std_logic lab=x_r0_x3}
N 460 2040 460 2040 {lab=0}
C {devices/lab_pin.sym} 460 2040 0 0 {name=p384 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 2040 0 0 {name=xr0n5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 2010 680 2010 {lab=x_r0_x3}
C {devices/lab_pin.sym} 680 2010 0 0 {name=p385 sig_type=std_logic lab=x_r0_x3}
N 640 2040 640 2040 {lab=x_r0_b}
C {devices/lab_pin.sym} 640 2040 0 1 {name=p386 sig_type=std_logic lab=x_r0_b}
N 680 2070 680 2070 {lab=0}
C {devices/lab_pin.sym} 680 2070 0 0 {name=p387 sig_type=std_logic lab=0}
N 680 2040 680 2040 {lab=0}
C {devices/lab_pin.sym} 680 2040 0 0 {name=p388 sig_type=std_logic lab=0}
C {devices/capa.sym} 880 2040 0 0 {name=cpl0
value=20f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 880 2010 880 2010 {lab=x_p0}
C {devices/lab_pin.sym} 880 2010 0 0 {name=p389 sig_type=std_logic lab=x_p0}
N 880 2070 880 2070 {lab=0}
C {devices/lab_pin.sym} 880 2070 0 0 {name=p390 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 2040 0 0 {name=xg1pa
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 2070 1120 2070 {lab=x_n1}
C {devices/lab_pin.sym} 1120 2070 0 0 {name=p391 sig_type=std_logic lab=x_n1}
N 1080 2040 1080 2040 {lab=x_q1}
C {devices/lab_pin.sym} 1080 2040 0 1 {name=p392 sig_type=std_logic lab=x_q1}
N 1120 2010 1120 2010 {lab=vdg}
C {devices/lab_pin.sym} 1120 2010 0 0 {name=p393 sig_type=std_logic lab=vdg}
N 1120 2040 1120 2040 {lab=vdg}
C {devices/lab_pin.sym} 1120 2040 0 0 {name=p394 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 2160 0 0 {name=xg1pb
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 2190 20 2190 {lab=x_n1}
C {devices/lab_pin.sym} 20 2190 0 0 {name=p395 sig_type=std_logic lab=x_n1}
N -20 2160 -20 2160 {lab=x_q2}
C {devices/lab_pin.sym} -20 2160 0 1 {name=p396 sig_type=std_logic lab=x_q2}
N 20 2130 20 2130 {lab=vdg}
C {devices/lab_pin.sym} 20 2130 0 0 {name=p397 sig_type=std_logic lab=vdg}
N 20 2160 20 2160 {lab=vdg}
C {devices/lab_pin.sym} 20 2160 0 0 {name=p398 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 2160 0 0 {name=xg1na
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 2130 240 2130 {lab=x_n1}
C {devices/lab_pin.sym} 240 2130 0 0 {name=p399 sig_type=std_logic lab=x_n1}
N 200 2160 200 2160 {lab=x_q1}
C {devices/lab_pin.sym} 200 2160 0 1 {name=p400 sig_type=std_logic lab=x_q1}
N 240 2190 240 2190 {lab=x_g1m}
C {devices/lab_pin.sym} 240 2190 0 0 {name=p401 sig_type=std_logic lab=x_g1m}
N 240 2160 240 2160 {lab=0}
C {devices/lab_pin.sym} 240 2160 0 0 {name=p402 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 2160 0 0 {name=xg1nb
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 2130 460 2130 {lab=x_g1m}
C {devices/lab_pin.sym} 460 2130 0 0 {name=p403 sig_type=std_logic lab=x_g1m}
N 420 2160 420 2160 {lab=x_q2}
C {devices/lab_pin.sym} 420 2160 0 1 {name=p404 sig_type=std_logic lab=x_q2}
N 460 2190 460 2190 {lab=0}
C {devices/lab_pin.sym} 460 2190 0 0 {name=p405 sig_type=std_logic lab=0}
N 460 2160 460 2160 {lab=0}
C {devices/lab_pin.sym} 460 2160 0 0 {name=p406 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 2160 0 0 {name=xr1p1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 2190 680 2190 {lab=x_r1_x1}
C {devices/lab_pin.sym} 680 2190 0 0 {name=p407 sig_type=std_logic lab=x_r1_x1}
N 640 2160 640 2160 {lab=x_n1}
C {devices/lab_pin.sym} 640 2160 0 1 {name=p408 sig_type=std_logic lab=x_n1}
N 680 2130 680 2130 {lab=vdg}
C {devices/lab_pin.sym} 680 2130 0 0 {name=p409 sig_type=std_logic lab=vdg}
N 680 2160 680 2160 {lab=vdg}
C {devices/lab_pin.sym} 680 2160 0 0 {name=p410 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 2160 0 0 {name=xr1p2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 2190 900 2190 {lab=x_r1_a}
C {devices/lab_pin.sym} 900 2190 0 0 {name=p411 sig_type=std_logic lab=x_r1_a}
N 860 2160 860 2160 {lab=x_clk}
C {devices/lab_pin.sym} 860 2160 0 1 {name=p412 sig_type=std_logic lab=x_clk}
N 900 2130 900 2130 {lab=x_r1_x1}
C {devices/lab_pin.sym} 900 2130 0 0 {name=p413 sig_type=std_logic lab=x_r1_x1}
N 900 2160 900 2160 {lab=vdg}
C {devices/lab_pin.sym} 900 2160 0 0 {name=p414 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 2160 0 0 {name=xr1n1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 2130 1120 2130 {lab=x_r1_a}
C {devices/lab_pin.sym} 1120 2130 0 0 {name=p415 sig_type=std_logic lab=x_r1_a}
N 1080 2160 1080 2160 {lab=x_n1}
C {devices/lab_pin.sym} 1080 2160 0 1 {name=p416 sig_type=std_logic lab=x_n1}
N 1120 2190 1120 2190 {lab=0}
C {devices/lab_pin.sym} 1120 2190 0 0 {name=p417 sig_type=std_logic lab=0}
N 1120 2160 1120 2160 {lab=0}
C {devices/lab_pin.sym} 1120 2160 0 0 {name=p418 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 2280 0 0 {name=xr1p3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 2310 20 2310 {lab=x_r1_b}
C {devices/lab_pin.sym} 20 2310 0 0 {name=p419 sig_type=std_logic lab=x_r1_b}
N -20 2280 -20 2280 {lab=x_clk}
C {devices/lab_pin.sym} -20 2280 0 1 {name=p420 sig_type=std_logic lab=x_clk}
N 20 2250 20 2250 {lab=vdg}
C {devices/lab_pin.sym} 20 2250 0 0 {name=p421 sig_type=std_logic lab=vdg}
N 20 2280 20 2280 {lab=vdg}
C {devices/lab_pin.sym} 20 2280 0 0 {name=p422 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 2280 0 0 {name=xr1n2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 2250 240 2250 {lab=x_r1_b}
C {devices/lab_pin.sym} 240 2250 0 0 {name=p423 sig_type=std_logic lab=x_r1_b}
N 200 2280 200 2280 {lab=x_r1_a}
C {devices/lab_pin.sym} 200 2280 0 1 {name=p424 sig_type=std_logic lab=x_r1_a}
N 240 2310 240 2310 {lab=x_r1_x2}
C {devices/lab_pin.sym} 240 2310 0 0 {name=p425 sig_type=std_logic lab=x_r1_x2}
N 240 2280 240 2280 {lab=0}
C {devices/lab_pin.sym} 240 2280 0 0 {name=p426 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 2280 0 0 {name=xr1n3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 2250 460 2250 {lab=x_r1_x2}
C {devices/lab_pin.sym} 460 2250 0 0 {name=p427 sig_type=std_logic lab=x_r1_x2}
N 420 2280 420 2280 {lab=x_clk}
C {devices/lab_pin.sym} 420 2280 0 1 {name=p428 sig_type=std_logic lab=x_clk}
N 460 2310 460 2310 {lab=0}
C {devices/lab_pin.sym} 460 2310 0 0 {name=p429 sig_type=std_logic lab=0}
N 460 2280 460 2280 {lab=0}
C {devices/lab_pin.sym} 460 2280 0 0 {name=p430 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 2280 0 0 {name=xr1p4
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 2310 680 2310 {lab=x_p1}
C {devices/lab_pin.sym} 680 2310 0 0 {name=p431 sig_type=std_logic lab=x_p1}
N 640 2280 640 2280 {lab=x_r1_b}
C {devices/lab_pin.sym} 640 2280 0 1 {name=p432 sig_type=std_logic lab=x_r1_b}
N 680 2250 680 2250 {lab=vdg}
C {devices/lab_pin.sym} 680 2250 0 0 {name=p433 sig_type=std_logic lab=vdg}
N 680 2280 680 2280 {lab=vdg}
C {devices/lab_pin.sym} 680 2280 0 0 {name=p434 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 2280 0 0 {name=xr1n4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 2250 900 2250 {lab=x_p1}
C {devices/lab_pin.sym} 900 2250 0 0 {name=p435 sig_type=std_logic lab=x_p1}
N 860 2280 860 2280 {lab=x_clk}
C {devices/lab_pin.sym} 860 2280 0 1 {name=p436 sig_type=std_logic lab=x_clk}
N 900 2310 900 2310 {lab=x_r1_x3}
C {devices/lab_pin.sym} 900 2310 0 0 {name=p437 sig_type=std_logic lab=x_r1_x3}
N 900 2280 900 2280 {lab=0}
C {devices/lab_pin.sym} 900 2280 0 0 {name=p438 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 2280 0 0 {name=xr1n5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 2250 1120 2250 {lab=x_r1_x3}
C {devices/lab_pin.sym} 1120 2250 0 0 {name=p439 sig_type=std_logic lab=x_r1_x3}
N 1080 2280 1080 2280 {lab=x_r1_b}
C {devices/lab_pin.sym} 1080 2280 0 1 {name=p440 sig_type=std_logic lab=x_r1_b}
N 1120 2310 1120 2310 {lab=0}
C {devices/lab_pin.sym} 1120 2310 0 0 {name=p441 sig_type=std_logic lab=0}
N 1120 2280 1120 2280 {lab=0}
C {devices/lab_pin.sym} 1120 2280 0 0 {name=p442 sig_type=std_logic lab=0}
C {devices/capa.sym} 0 2400 0 0 {name=cpl1
value=20f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 0 2370 0 2370 {lab=x_p1}
C {devices/lab_pin.sym} 0 2370 0 0 {name=p443 sig_type=std_logic lab=x_p1}
N 0 2430 0 2430 {lab=0}
C {devices/lab_pin.sym} 0 2430 0 0 {name=p444 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 2400 0 0 {name=xg2pa
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 2430 240 2430 {lab=x_n2}
C {devices/lab_pin.sym} 240 2430 0 0 {name=p445 sig_type=std_logic lab=x_n2}
N 200 2400 200 2400 {lab=x_q1b}
C {devices/lab_pin.sym} 200 2400 0 1 {name=p446 sig_type=std_logic lab=x_q1b}
N 240 2370 240 2370 {lab=vdg}
C {devices/lab_pin.sym} 240 2370 0 0 {name=p447 sig_type=std_logic lab=vdg}
N 240 2400 240 2400 {lab=vdg}
C {devices/lab_pin.sym} 240 2400 0 0 {name=p448 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 2400 0 0 {name=xg2pb
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 2430 460 2430 {lab=x_n2}
C {devices/lab_pin.sym} 460 2430 0 0 {name=p449 sig_type=std_logic lab=x_n2}
N 420 2400 420 2400 {lab=x_q2}
C {devices/lab_pin.sym} 420 2400 0 1 {name=p450 sig_type=std_logic lab=x_q2}
N 460 2370 460 2370 {lab=vdg}
C {devices/lab_pin.sym} 460 2370 0 0 {name=p451 sig_type=std_logic lab=vdg}
N 460 2400 460 2400 {lab=vdg}
C {devices/lab_pin.sym} 460 2400 0 0 {name=p452 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 2400 0 0 {name=xg2na
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 2370 680 2370 {lab=x_n2}
C {devices/lab_pin.sym} 680 2370 0 0 {name=p453 sig_type=std_logic lab=x_n2}
N 640 2400 640 2400 {lab=x_q1b}
C {devices/lab_pin.sym} 640 2400 0 1 {name=p454 sig_type=std_logic lab=x_q1b}
N 680 2430 680 2430 {lab=x_g2m}
C {devices/lab_pin.sym} 680 2430 0 0 {name=p455 sig_type=std_logic lab=x_g2m}
N 680 2400 680 2400 {lab=0}
C {devices/lab_pin.sym} 680 2400 0 0 {name=p456 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 2400 0 0 {name=xg2nb
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 2370 900 2370 {lab=x_g2m}
C {devices/lab_pin.sym} 900 2370 0 0 {name=p457 sig_type=std_logic lab=x_g2m}
N 860 2400 860 2400 {lab=x_q2}
C {devices/lab_pin.sym} 860 2400 0 1 {name=p458 sig_type=std_logic lab=x_q2}
N 900 2430 900 2430 {lab=0}
C {devices/lab_pin.sym} 900 2430 0 0 {name=p459 sig_type=std_logic lab=0}
N 900 2400 900 2400 {lab=0}
C {devices/lab_pin.sym} 900 2400 0 0 {name=p460 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 2400 0 0 {name=xr2p1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 2430 1120 2430 {lab=x_r2_x1}
C {devices/lab_pin.sym} 1120 2430 0 0 {name=p461 sig_type=std_logic lab=x_r2_x1}
N 1080 2400 1080 2400 {lab=x_n2}
C {devices/lab_pin.sym} 1080 2400 0 1 {name=p462 sig_type=std_logic lab=x_n2}
N 1120 2370 1120 2370 {lab=vdg}
C {devices/lab_pin.sym} 1120 2370 0 0 {name=p463 sig_type=std_logic lab=vdg}
N 1120 2400 1120 2400 {lab=vdg}
C {devices/lab_pin.sym} 1120 2400 0 0 {name=p464 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 0 2520 0 0 {name=xr2p2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 20 2550 20 2550 {lab=x_r2_a}
C {devices/lab_pin.sym} 20 2550 0 0 {name=p465 sig_type=std_logic lab=x_r2_a}
N -20 2520 -20 2520 {lab=x_clk}
C {devices/lab_pin.sym} -20 2520 0 1 {name=p466 sig_type=std_logic lab=x_clk}
N 20 2490 20 2490 {lab=x_r2_x1}
C {devices/lab_pin.sym} 20 2490 0 0 {name=p467 sig_type=std_logic lab=x_r2_x1}
N 20 2520 20 2520 {lab=vdg}
C {devices/lab_pin.sym} 20 2520 0 0 {name=p468 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 2520 0 0 {name=xr2n1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 2490 240 2490 {lab=x_r2_a}
C {devices/lab_pin.sym} 240 2490 0 0 {name=p469 sig_type=std_logic lab=x_r2_a}
N 200 2520 200 2520 {lab=x_n2}
C {devices/lab_pin.sym} 200 2520 0 1 {name=p470 sig_type=std_logic lab=x_n2}
N 240 2550 240 2550 {lab=0}
C {devices/lab_pin.sym} 240 2550 0 0 {name=p471 sig_type=std_logic lab=0}
N 240 2520 240 2520 {lab=0}
C {devices/lab_pin.sym} 240 2520 0 0 {name=p472 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 2520 0 0 {name=xr2p3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 2550 460 2550 {lab=x_r2_b}
C {devices/lab_pin.sym} 460 2550 0 0 {name=p473 sig_type=std_logic lab=x_r2_b}
N 420 2520 420 2520 {lab=x_clk}
C {devices/lab_pin.sym} 420 2520 0 1 {name=p474 sig_type=std_logic lab=x_clk}
N 460 2490 460 2490 {lab=vdg}
C {devices/lab_pin.sym} 460 2490 0 0 {name=p475 sig_type=std_logic lab=vdg}
N 460 2520 460 2520 {lab=vdg}
C {devices/lab_pin.sym} 460 2520 0 0 {name=p476 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 2520 0 0 {name=xr2n2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 2490 680 2490 {lab=x_r2_b}
C {devices/lab_pin.sym} 680 2490 0 0 {name=p477 sig_type=std_logic lab=x_r2_b}
N 640 2520 640 2520 {lab=x_r2_a}
C {devices/lab_pin.sym} 640 2520 0 1 {name=p478 sig_type=std_logic lab=x_r2_a}
N 680 2550 680 2550 {lab=x_r2_x2}
C {devices/lab_pin.sym} 680 2550 0 0 {name=p479 sig_type=std_logic lab=x_r2_x2}
N 680 2520 680 2520 {lab=0}
C {devices/lab_pin.sym} 680 2520 0 0 {name=p480 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 880 2520 0 0 {name=xr2n3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 900 2490 900 2490 {lab=x_r2_x2}
C {devices/lab_pin.sym} 900 2490 0 0 {name=p481 sig_type=std_logic lab=x_r2_x2}
N 860 2520 860 2520 {lab=x_clk}
C {devices/lab_pin.sym} 860 2520 0 1 {name=p482 sig_type=std_logic lab=x_clk}
N 900 2550 900 2550 {lab=0}
C {devices/lab_pin.sym} 900 2550 0 0 {name=p483 sig_type=std_logic lab=0}
N 900 2520 900 2520 {lab=0}
C {devices/lab_pin.sym} 900 2520 0 0 {name=p484 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 2520 0 0 {name=xr2p4
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 2550 1120 2550 {lab=x_p2}
C {devices/lab_pin.sym} 1120 2550 0 0 {name=p485 sig_type=std_logic lab=x_p2}
N 1080 2520 1080 2520 {lab=x_r2_b}
C {devices/lab_pin.sym} 1080 2520 0 1 {name=p486 sig_type=std_logic lab=x_r2_b}
N 1120 2490 1120 2490 {lab=vdg}
C {devices/lab_pin.sym} 1120 2490 0 0 {name=p487 sig_type=std_logic lab=vdg}
N 1120 2520 1120 2520 {lab=vdg}
C {devices/lab_pin.sym} 1120 2520 0 0 {name=p488 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 2640 0 0 {name=xr2n4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 2610 20 2610 {lab=x_p2}
C {devices/lab_pin.sym} 20 2610 0 0 {name=p489 sig_type=std_logic lab=x_p2}
N -20 2640 -20 2640 {lab=x_clk}
C {devices/lab_pin.sym} -20 2640 0 1 {name=p490 sig_type=std_logic lab=x_clk}
N 20 2670 20 2670 {lab=x_r2_x3}
C {devices/lab_pin.sym} 20 2670 0 0 {name=p491 sig_type=std_logic lab=x_r2_x3}
N 20 2640 20 2640 {lab=0}
C {devices/lab_pin.sym} 20 2640 0 0 {name=p492 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 220 2640 0 0 {name=xr2n5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 240 2610 240 2610 {lab=x_r2_x3}
C {devices/lab_pin.sym} 240 2610 0 0 {name=p493 sig_type=std_logic lab=x_r2_x3}
N 200 2640 200 2640 {lab=x_r2_b}
C {devices/lab_pin.sym} 200 2640 0 1 {name=p494 sig_type=std_logic lab=x_r2_b}
N 240 2670 240 2670 {lab=0}
C {devices/lab_pin.sym} 240 2670 0 0 {name=p495 sig_type=std_logic lab=0}
N 240 2640 240 2640 {lab=0}
C {devices/lab_pin.sym} 240 2640 0 0 {name=p496 sig_type=std_logic lab=0}
C {devices/capa.sym} 440 2640 0 0 {name=cpl2
value=20f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 440 2610 440 2610 {lab=x_p2}
C {devices/lab_pin.sym} 440 2610 0 0 {name=p497 sig_type=std_logic lab=x_p2}
N 440 2670 440 2670 {lab=0}
C {devices/lab_pin.sym} 440 2670 0 0 {name=p498 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 2640 0 0 {name=xg3pa
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 680 2670 680 2670 {lab=x_n3}
C {devices/lab_pin.sym} 680 2670 0 0 {name=p499 sig_type=std_logic lab=x_n3}
N 640 2640 640 2640 {lab=x_q1b}
C {devices/lab_pin.sym} 640 2640 0 1 {name=p500 sig_type=std_logic lab=x_q1b}
N 680 2610 680 2610 {lab=vdg}
C {devices/lab_pin.sym} 680 2610 0 0 {name=p501 sig_type=std_logic lab=vdg}
N 680 2640 680 2640 {lab=vdg}
C {devices/lab_pin.sym} 680 2640 0 0 {name=p502 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 2640 0 0 {name=xg3pb
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 2670 900 2670 {lab=x_n3}
C {devices/lab_pin.sym} 900 2670 0 0 {name=p503 sig_type=std_logic lab=x_n3}
N 860 2640 860 2640 {lab=x_q2b}
C {devices/lab_pin.sym} 860 2640 0 1 {name=p504 sig_type=std_logic lab=x_q2b}
N 900 2610 900 2610 {lab=vdg}
C {devices/lab_pin.sym} 900 2610 0 0 {name=p505 sig_type=std_logic lab=vdg}
N 900 2640 900 2640 {lab=vdg}
C {devices/lab_pin.sym} 900 2640 0 0 {name=p506 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 2640 0 0 {name=xg3na
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 2610 1120 2610 {lab=x_n3}
C {devices/lab_pin.sym} 1120 2610 0 0 {name=p507 sig_type=std_logic lab=x_n3}
N 1080 2640 1080 2640 {lab=x_q1b}
C {devices/lab_pin.sym} 1080 2640 0 1 {name=p508 sig_type=std_logic lab=x_q1b}
N 1120 2670 1120 2670 {lab=x_g3m}
C {devices/lab_pin.sym} 1120 2670 0 0 {name=p509 sig_type=std_logic lab=x_g3m}
N 1120 2640 1120 2640 {lab=0}
C {devices/lab_pin.sym} 1120 2640 0 0 {name=p510 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 2760 0 0 {name=xg3nb
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 2730 20 2730 {lab=x_g3m}
C {devices/lab_pin.sym} 20 2730 0 0 {name=p511 sig_type=std_logic lab=x_g3m}
N -20 2760 -20 2760 {lab=x_q2b}
C {devices/lab_pin.sym} -20 2760 0 1 {name=p512 sig_type=std_logic lab=x_q2b}
N 20 2790 20 2790 {lab=0}
C {devices/lab_pin.sym} 20 2790 0 0 {name=p513 sig_type=std_logic lab=0}
N 20 2760 20 2760 {lab=0}
C {devices/lab_pin.sym} 20 2760 0 0 {name=p514 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 2760 0 0 {name=xr3p1
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 2790 240 2790 {lab=x_r3_x1}
C {devices/lab_pin.sym} 240 2790 0 0 {name=p515 sig_type=std_logic lab=x_r3_x1}
N 200 2760 200 2760 {lab=x_n3}
C {devices/lab_pin.sym} 200 2760 0 1 {name=p516 sig_type=std_logic lab=x_n3}
N 240 2730 240 2730 {lab=vdg}
C {devices/lab_pin.sym} 240 2730 0 0 {name=p517 sig_type=std_logic lab=vdg}
N 240 2760 240 2760 {lab=vdg}
C {devices/lab_pin.sym} 240 2760 0 0 {name=p518 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_pmos.sym} 440 2760 0 0 {name=xr3p2
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 460 2790 460 2790 {lab=x_r3_a}
C {devices/lab_pin.sym} 460 2790 0 0 {name=p519 sig_type=std_logic lab=x_r3_a}
N 420 2760 420 2760 {lab=x_clk}
C {devices/lab_pin.sym} 420 2760 0 1 {name=p520 sig_type=std_logic lab=x_clk}
N 460 2730 460 2730 {lab=x_r3_x1}
C {devices/lab_pin.sym} 460 2730 0 0 {name=p521 sig_type=std_logic lab=x_r3_x1}
N 460 2760 460 2760 {lab=vdg}
C {devices/lab_pin.sym} 460 2760 0 0 {name=p522 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 2760 0 0 {name=xr3n1
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 2730 680 2730 {lab=x_r3_a}
C {devices/lab_pin.sym} 680 2730 0 0 {name=p523 sig_type=std_logic lab=x_r3_a}
N 640 2760 640 2760 {lab=x_n3}
C {devices/lab_pin.sym} 640 2760 0 1 {name=p524 sig_type=std_logic lab=x_n3}
N 680 2790 680 2790 {lab=0}
C {devices/lab_pin.sym} 680 2790 0 0 {name=p525 sig_type=std_logic lab=0}
N 680 2760 680 2760 {lab=0}
C {devices/lab_pin.sym} 680 2760 0 0 {name=p526 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 880 2760 0 0 {name=xr3p3
w=2u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 900 2790 900 2790 {lab=x_r3_b}
C {devices/lab_pin.sym} 900 2790 0 0 {name=p527 sig_type=std_logic lab=x_r3_b}
N 860 2760 860 2760 {lab=x_clk}
C {devices/lab_pin.sym} 860 2760 0 1 {name=p528 sig_type=std_logic lab=x_clk}
N 900 2730 900 2730 {lab=vdg}
C {devices/lab_pin.sym} 900 2730 0 0 {name=p529 sig_type=std_logic lab=vdg}
N 900 2760 900 2760 {lab=vdg}
C {devices/lab_pin.sym} 900 2760 0 0 {name=p530 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 1100 2760 0 0 {name=xr3n2
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 1120 2730 1120 2730 {lab=x_r3_b}
C {devices/lab_pin.sym} 1120 2730 0 0 {name=p531 sig_type=std_logic lab=x_r3_b}
N 1080 2760 1080 2760 {lab=x_r3_a}
C {devices/lab_pin.sym} 1080 2760 0 1 {name=p532 sig_type=std_logic lab=x_r3_a}
N 1120 2790 1120 2790 {lab=x_r3_x2}
C {devices/lab_pin.sym} 1120 2790 0 0 {name=p533 sig_type=std_logic lab=x_r3_x2}
N 1120 2760 1120 2760 {lab=0}
C {devices/lab_pin.sym} 1120 2760 0 0 {name=p534 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 2880 0 0 {name=xr3n3
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 2850 20 2850 {lab=x_r3_x2}
C {devices/lab_pin.sym} 20 2850 0 0 {name=p535 sig_type=std_logic lab=x_r3_x2}
N -20 2880 -20 2880 {lab=x_clk}
C {devices/lab_pin.sym} -20 2880 0 1 {name=p536 sig_type=std_logic lab=x_clk}
N 20 2910 20 2910 {lab=0}
C {devices/lab_pin.sym} 20 2910 0 0 {name=p537 sig_type=std_logic lab=0}
N 20 2880 20 2880 {lab=0}
C {devices/lab_pin.sym} 20 2880 0 0 {name=p538 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 2880 0 0 {name=xr3p4
w=4u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 2910 240 2910 {lab=x_p3}
C {devices/lab_pin.sym} 240 2910 0 0 {name=p539 sig_type=std_logic lab=x_p3}
N 200 2880 200 2880 {lab=x_r3_b}
C {devices/lab_pin.sym} 200 2880 0 1 {name=p540 sig_type=std_logic lab=x_r3_b}
N 240 2850 240 2850 {lab=vdg}
C {devices/lab_pin.sym} 240 2850 0 0 {name=p541 sig_type=std_logic lab=vdg}
N 240 2880 240 2880 {lab=vdg}
C {devices/lab_pin.sym} 240 2880 0 0 {name=p542 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 2880 0 0 {name=xr3n4
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 2850 460 2850 {lab=x_p3}
C {devices/lab_pin.sym} 460 2850 0 0 {name=p543 sig_type=std_logic lab=x_p3}
N 420 2880 420 2880 {lab=x_clk}
C {devices/lab_pin.sym} 420 2880 0 1 {name=p544 sig_type=std_logic lab=x_clk}
N 460 2910 460 2910 {lab=x_r3_x3}
C {devices/lab_pin.sym} 460 2910 0 0 {name=p545 sig_type=std_logic lab=x_r3_x3}
N 460 2880 460 2880 {lab=0}
C {devices/lab_pin.sym} 460 2880 0 0 {name=p546 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 2880 0 0 {name=xr3n5
w=1u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 680 2850 680 2850 {lab=x_r3_x3}
C {devices/lab_pin.sym} 680 2850 0 0 {name=p547 sig_type=std_logic lab=x_r3_x3}
N 640 2880 640 2880 {lab=x_r3_b}
C {devices/lab_pin.sym} 640 2880 0 1 {name=p548 sig_type=std_logic lab=x_r3_b}
N 680 2910 680 2910 {lab=0}
C {devices/lab_pin.sym} 680 2910 0 0 {name=p549 sig_type=std_logic lab=0}
N 680 2880 680 2880 {lab=0}
C {devices/lab_pin.sym} 680 2880 0 0 {name=p550 sig_type=std_logic lab=0}
C {devices/capa.sym} 880 2880 0 0 {name=cpl3
value=20f
m=1
footprint=1206
device=capacitor
sim_device=capacitor
}
N 880 2850 880 2850 {lab=x_p3}
C {devices/lab_pin.sym} 880 2850 0 0 {name=p551 sig_type=std_logic lab=x_p3}
N 880 2910 880 2910 {lab=0}
C {devices/lab_pin.sym} 880 2910 0 0 {name=p552 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 2880 0 0 {name=xf1kq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 2910 1120 2910 {lab=x_f1_kq}
C {devices/lab_pin.sym} 1120 2910 0 0 {name=p553 sig_type=std_logic lab=x_f1_kq}
N 1080 2880 1080 2880 {lab=x_q1}
C {devices/lab_pin.sym} 1080 2880 0 1 {name=p554 sig_type=std_logic lab=x_q1}
N 1120 2850 1120 2850 {lab=vdg}
C {devices/lab_pin.sym} 1120 2850 0 0 {name=p555 sig_type=std_logic lab=vdg}
N 1120 2880 1120 2880 {lab=vdg}
C {devices/lab_pin.sym} 1120 2880 0 0 {name=p556 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 3000 0 0 {name=xf1kq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 2970 20 2970 {lab=x_f1_kq}
C {devices/lab_pin.sym} 20 2970 0 0 {name=p557 sig_type=std_logic lab=x_f1_kq}
N -20 3000 -20 3000 {lab=x_q1}
C {devices/lab_pin.sym} -20 3000 0 1 {name=p558 sig_type=std_logic lab=x_q1}
N 20 3030 20 3030 {lab=0}
C {devices/lab_pin.sym} 20 3030 0 0 {name=p559 sig_type=std_logic lab=0}
N 20 3000 20 3000 {lab=0}
C {devices/lab_pin.sym} 20 3000 0 0 {name=p560 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 3000 0 0 {name=xf1kq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 3030 240 3030 {lab=x_q1}
C {devices/lab_pin.sym} 240 3030 0 0 {name=p561 sig_type=std_logic lab=x_q1}
N 200 3000 200 3000 {lab=x_f1_kq}
C {devices/lab_pin.sym} 200 3000 0 1 {name=p562 sig_type=std_logic lab=x_f1_kq}
N 240 2970 240 2970 {lab=vdg}
C {devices/lab_pin.sym} 240 2970 0 0 {name=p563 sig_type=std_logic lab=vdg}
N 240 3000 240 3000 {lab=vdg}
C {devices/lab_pin.sym} 240 3000 0 0 {name=p564 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 3000 0 0 {name=xf1kq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 2970 460 2970 {lab=x_q1}
C {devices/lab_pin.sym} 460 2970 0 0 {name=p565 sig_type=std_logic lab=x_q1}
N 420 3000 420 3000 {lab=x_f1_kq}
C {devices/lab_pin.sym} 420 3000 0 1 {name=p566 sig_type=std_logic lab=x_f1_kq}
N 460 3030 460 3030 {lab=0}
C {devices/lab_pin.sym} 460 3030 0 0 {name=p567 sig_type=std_logic lab=0}
N 460 3000 460 3000 {lab=0}
C {devices/lab_pin.sym} 460 3000 0 0 {name=p568 sig_type=std_logic lab=0}
C {devices/res.sym} 660 3000 0 0 {name=rkf11
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 660 2970 660 2970 {lab=x_f1_a}
C {devices/lab_pin.sym} 660 2970 0 0 {name=p569 sig_type=std_logic lab=x_f1_a}
N 660 3030 660 3030 {lab=0}
C {devices/lab_pin.sym} 660 3030 0 0 {name=p570 sig_type=std_logic lab=0}
C {devices/res.sym} 880 3000 0 0 {name=rkf12
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 2970 880 2970 {lab=x_f1_b}
C {devices/lab_pin.sym} 880 2970 0 0 {name=p571 sig_type=std_logic lab=x_f1_b}
N 880 3030 880 3030 {lab=0}
C {devices/lab_pin.sym} 880 3030 0 0 {name=p572 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 3000 0 0 {name=xf2kq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 3030 1120 3030 {lab=x_f2_kq}
C {devices/lab_pin.sym} 1120 3030 0 0 {name=p573 sig_type=std_logic lab=x_f2_kq}
N 1080 3000 1080 3000 {lab=x_q2}
C {devices/lab_pin.sym} 1080 3000 0 1 {name=p574 sig_type=std_logic lab=x_q2}
N 1120 2970 1120 2970 {lab=vdg}
C {devices/lab_pin.sym} 1120 2970 0 0 {name=p575 sig_type=std_logic lab=vdg}
N 1120 3000 1120 3000 {lab=vdg}
C {devices/lab_pin.sym} 1120 3000 0 0 {name=p576 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 3120 0 0 {name=xf2kq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 3090 20 3090 {lab=x_f2_kq}
C {devices/lab_pin.sym} 20 3090 0 0 {name=p577 sig_type=std_logic lab=x_f2_kq}
N -20 3120 -20 3120 {lab=x_q2}
C {devices/lab_pin.sym} -20 3120 0 1 {name=p578 sig_type=std_logic lab=x_q2}
N 20 3150 20 3150 {lab=0}
C {devices/lab_pin.sym} 20 3150 0 0 {name=p579 sig_type=std_logic lab=0}
N 20 3120 20 3120 {lab=0}
C {devices/lab_pin.sym} 20 3120 0 0 {name=p580 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 3120 0 0 {name=xf2kq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 3150 240 3150 {lab=x_q2}
C {devices/lab_pin.sym} 240 3150 0 0 {name=p581 sig_type=std_logic lab=x_q2}
N 200 3120 200 3120 {lab=x_f2_kq}
C {devices/lab_pin.sym} 200 3120 0 1 {name=p582 sig_type=std_logic lab=x_f2_kq}
N 240 3090 240 3090 {lab=vdg}
C {devices/lab_pin.sym} 240 3090 0 0 {name=p583 sig_type=std_logic lab=vdg}
N 240 3120 240 3120 {lab=vdg}
C {devices/lab_pin.sym} 240 3120 0 0 {name=p584 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 3120 0 0 {name=xf2kq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 3090 460 3090 {lab=x_q2}
C {devices/lab_pin.sym} 460 3090 0 0 {name=p585 sig_type=std_logic lab=x_q2}
N 420 3120 420 3120 {lab=x_f2_kq}
C {devices/lab_pin.sym} 420 3120 0 1 {name=p586 sig_type=std_logic lab=x_f2_kq}
N 460 3150 460 3150 {lab=0}
C {devices/lab_pin.sym} 460 3150 0 0 {name=p587 sig_type=std_logic lab=0}
N 460 3120 460 3120 {lab=0}
C {devices/lab_pin.sym} 460 3120 0 0 {name=p588 sig_type=std_logic lab=0}
C {devices/res.sym} 660 3120 0 0 {name=rkf21
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 660 3090 660 3090 {lab=x_f2_a}
C {devices/lab_pin.sym} 660 3090 0 0 {name=p589 sig_type=std_logic lab=x_f2_a}
N 660 3150 660 3150 {lab=0}
C {devices/lab_pin.sym} 660 3150 0 0 {name=p590 sig_type=std_logic lab=0}
C {devices/res.sym} 880 3120 0 0 {name=rkf22
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 3090 880 3090 {lab=x_f2_b}
C {devices/lab_pin.sym} 880 3090 0 0 {name=p591 sig_type=std_logic lab=x_f2_b}
N 880 3150 880 3150 {lab=0}
C {devices/lab_pin.sym} 880 3150 0 0 {name=p592 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 3120 0 0 {name=xr0kq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 3150 1120 3150 {lab=x_r0_kq}
C {devices/lab_pin.sym} 1120 3150 0 0 {name=p593 sig_type=std_logic lab=x_r0_kq}
N 1080 3120 1080 3120 {lab=x_p0}
C {devices/lab_pin.sym} 1080 3120 0 1 {name=p594 sig_type=std_logic lab=x_p0}
N 1120 3090 1120 3090 {lab=vdg}
C {devices/lab_pin.sym} 1120 3090 0 0 {name=p595 sig_type=std_logic lab=vdg}
N 1120 3120 1120 3120 {lab=vdg}
C {devices/lab_pin.sym} 1120 3120 0 0 {name=p596 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 3240 0 0 {name=xr0kq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 3210 20 3210 {lab=x_r0_kq}
C {devices/lab_pin.sym} 20 3210 0 0 {name=p597 sig_type=std_logic lab=x_r0_kq}
N -20 3240 -20 3240 {lab=x_p0}
C {devices/lab_pin.sym} -20 3240 0 1 {name=p598 sig_type=std_logic lab=x_p0}
N 20 3270 20 3270 {lab=0}
C {devices/lab_pin.sym} 20 3270 0 0 {name=p599 sig_type=std_logic lab=0}
N 20 3240 20 3240 {lab=0}
C {devices/lab_pin.sym} 20 3240 0 0 {name=p600 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 3240 0 0 {name=xr0kq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 3270 240 3270 {lab=x_p0}
C {devices/lab_pin.sym} 240 3270 0 0 {name=p601 sig_type=std_logic lab=x_p0}
N 200 3240 200 3240 {lab=x_r0_kq}
C {devices/lab_pin.sym} 200 3240 0 1 {name=p602 sig_type=std_logic lab=x_r0_kq}
N 240 3210 240 3210 {lab=vdg}
C {devices/lab_pin.sym} 240 3210 0 0 {name=p603 sig_type=std_logic lab=vdg}
N 240 3240 240 3240 {lab=vdg}
C {devices/lab_pin.sym} 240 3240 0 0 {name=p604 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 3240 0 0 {name=xr0kq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 3210 460 3210 {lab=x_p0}
C {devices/lab_pin.sym} 460 3210 0 0 {name=p605 sig_type=std_logic lab=x_p0}
N 420 3240 420 3240 {lab=x_r0_kq}
C {devices/lab_pin.sym} 420 3240 0 1 {name=p606 sig_type=std_logic lab=x_r0_kq}
N 460 3270 460 3270 {lab=0}
C {devices/lab_pin.sym} 460 3270 0 0 {name=p607 sig_type=std_logic lab=0}
N 460 3240 460 3240 {lab=0}
C {devices/lab_pin.sym} 460 3240 0 0 {name=p608 sig_type=std_logic lab=0}
C {devices/res.sym} 660 3240 0 0 {name=rkr01
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 660 3210 660 3210 {lab=x_r0_a}
C {devices/lab_pin.sym} 660 3210 0 0 {name=p609 sig_type=std_logic lab=x_r0_a}
N 660 3270 660 3270 {lab=0}
C {devices/lab_pin.sym} 660 3270 0 0 {name=p610 sig_type=std_logic lab=0}
C {devices/res.sym} 880 3240 0 0 {name=rkr02
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 3210 880 3210 {lab=x_r0_b}
C {devices/lab_pin.sym} 880 3210 0 0 {name=p611 sig_type=std_logic lab=x_r0_b}
N 880 3270 880 3270 {lab=0}
C {devices/lab_pin.sym} 880 3270 0 0 {name=p612 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 3240 0 0 {name=xr1kq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 3270 1120 3270 {lab=x_r1_kq}
C {devices/lab_pin.sym} 1120 3270 0 0 {name=p613 sig_type=std_logic lab=x_r1_kq}
N 1080 3240 1080 3240 {lab=x_p1}
C {devices/lab_pin.sym} 1080 3240 0 1 {name=p614 sig_type=std_logic lab=x_p1}
N 1120 3210 1120 3210 {lab=vdg}
C {devices/lab_pin.sym} 1120 3210 0 0 {name=p615 sig_type=std_logic lab=vdg}
N 1120 3240 1120 3240 {lab=vdg}
C {devices/lab_pin.sym} 1120 3240 0 0 {name=p616 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 3360 0 0 {name=xr1kq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 3330 20 3330 {lab=x_r1_kq}
C {devices/lab_pin.sym} 20 3330 0 0 {name=p617 sig_type=std_logic lab=x_r1_kq}
N -20 3360 -20 3360 {lab=x_p1}
C {devices/lab_pin.sym} -20 3360 0 1 {name=p618 sig_type=std_logic lab=x_p1}
N 20 3390 20 3390 {lab=0}
C {devices/lab_pin.sym} 20 3390 0 0 {name=p619 sig_type=std_logic lab=0}
N 20 3360 20 3360 {lab=0}
C {devices/lab_pin.sym} 20 3360 0 0 {name=p620 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 3360 0 0 {name=xr1kq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 3390 240 3390 {lab=x_p1}
C {devices/lab_pin.sym} 240 3390 0 0 {name=p621 sig_type=std_logic lab=x_p1}
N 200 3360 200 3360 {lab=x_r1_kq}
C {devices/lab_pin.sym} 200 3360 0 1 {name=p622 sig_type=std_logic lab=x_r1_kq}
N 240 3330 240 3330 {lab=vdg}
C {devices/lab_pin.sym} 240 3330 0 0 {name=p623 sig_type=std_logic lab=vdg}
N 240 3360 240 3360 {lab=vdg}
C {devices/lab_pin.sym} 240 3360 0 0 {name=p624 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 3360 0 0 {name=xr1kq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 3330 460 3330 {lab=x_p1}
C {devices/lab_pin.sym} 460 3330 0 0 {name=p625 sig_type=std_logic lab=x_p1}
N 420 3360 420 3360 {lab=x_r1_kq}
C {devices/lab_pin.sym} 420 3360 0 1 {name=p626 sig_type=std_logic lab=x_r1_kq}
N 460 3390 460 3390 {lab=0}
C {devices/lab_pin.sym} 460 3390 0 0 {name=p627 sig_type=std_logic lab=0}
N 460 3360 460 3360 {lab=0}
C {devices/lab_pin.sym} 460 3360 0 0 {name=p628 sig_type=std_logic lab=0}
C {devices/res.sym} 660 3360 0 0 {name=rkr11
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 660 3330 660 3330 {lab=x_r1_a}
C {devices/lab_pin.sym} 660 3330 0 0 {name=p629 sig_type=std_logic lab=x_r1_a}
N 660 3390 660 3390 {lab=0}
C {devices/lab_pin.sym} 660 3390 0 0 {name=p630 sig_type=std_logic lab=0}
C {devices/res.sym} 880 3360 0 0 {name=rkr12
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 3330 880 3330 {lab=x_r1_b}
C {devices/lab_pin.sym} 880 3330 0 0 {name=p631 sig_type=std_logic lab=x_r1_b}
N 880 3390 880 3390 {lab=0}
C {devices/lab_pin.sym} 880 3390 0 0 {name=p632 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 3360 0 0 {name=xr2kq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 3390 1120 3390 {lab=x_r2_kq}
C {devices/lab_pin.sym} 1120 3390 0 0 {name=p633 sig_type=std_logic lab=x_r2_kq}
N 1080 3360 1080 3360 {lab=x_p2}
C {devices/lab_pin.sym} 1080 3360 0 1 {name=p634 sig_type=std_logic lab=x_p2}
N 1120 3330 1120 3330 {lab=vdg}
C {devices/lab_pin.sym} 1120 3330 0 0 {name=p635 sig_type=std_logic lab=vdg}
N 1120 3360 1120 3360 {lab=vdg}
C {devices/lab_pin.sym} 1120 3360 0 0 {name=p636 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 3480 0 0 {name=xr2kq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 3450 20 3450 {lab=x_r2_kq}
C {devices/lab_pin.sym} 20 3450 0 0 {name=p637 sig_type=std_logic lab=x_r2_kq}
N -20 3480 -20 3480 {lab=x_p2}
C {devices/lab_pin.sym} -20 3480 0 1 {name=p638 sig_type=std_logic lab=x_p2}
N 20 3510 20 3510 {lab=0}
C {devices/lab_pin.sym} 20 3510 0 0 {name=p639 sig_type=std_logic lab=0}
N 20 3480 20 3480 {lab=0}
C {devices/lab_pin.sym} 20 3480 0 0 {name=p640 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 3480 0 0 {name=xr2kq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 3510 240 3510 {lab=x_p2}
C {devices/lab_pin.sym} 240 3510 0 0 {name=p641 sig_type=std_logic lab=x_p2}
N 200 3480 200 3480 {lab=x_r2_kq}
C {devices/lab_pin.sym} 200 3480 0 1 {name=p642 sig_type=std_logic lab=x_r2_kq}
N 240 3450 240 3450 {lab=vdg}
C {devices/lab_pin.sym} 240 3450 0 0 {name=p643 sig_type=std_logic lab=vdg}
N 240 3480 240 3480 {lab=vdg}
C {devices/lab_pin.sym} 240 3480 0 0 {name=p644 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 3480 0 0 {name=xr2kq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 3450 460 3450 {lab=x_p2}
C {devices/lab_pin.sym} 460 3450 0 0 {name=p645 sig_type=std_logic lab=x_p2}
N 420 3480 420 3480 {lab=x_r2_kq}
C {devices/lab_pin.sym} 420 3480 0 1 {name=p646 sig_type=std_logic lab=x_r2_kq}
N 460 3510 460 3510 {lab=0}
C {devices/lab_pin.sym} 460 3510 0 0 {name=p647 sig_type=std_logic lab=0}
N 460 3480 460 3480 {lab=0}
C {devices/lab_pin.sym} 460 3480 0 0 {name=p648 sig_type=std_logic lab=0}
C {devices/res.sym} 660 3480 0 0 {name=rkr21
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 660 3450 660 3450 {lab=x_r2_a}
C {devices/lab_pin.sym} 660 3450 0 0 {name=p649 sig_type=std_logic lab=x_r2_a}
N 660 3510 660 3510 {lab=0}
C {devices/lab_pin.sym} 660 3510 0 0 {name=p650 sig_type=std_logic lab=0}
C {devices/res.sym} 880 3480 0 0 {name=rkr22
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 3450 880 3450 {lab=x_r2_b}
C {devices/lab_pin.sym} 880 3450 0 0 {name=p651 sig_type=std_logic lab=x_r2_b}
N 880 3510 880 3510 {lab=0}
C {devices/lab_pin.sym} 880 3510 0 0 {name=p652 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 1100 3480 0 0 {name=xr3kq1p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 1120 3510 1120 3510 {lab=x_r3_kq}
C {devices/lab_pin.sym} 1120 3510 0 0 {name=p653 sig_type=std_logic lab=x_r3_kq}
N 1080 3480 1080 3480 {lab=x_p3}
C {devices/lab_pin.sym} 1080 3480 0 1 {name=p654 sig_type=std_logic lab=x_p3}
N 1120 3450 1120 3450 {lab=vdg}
C {devices/lab_pin.sym} 1120 3450 0 0 {name=p655 sig_type=std_logic lab=vdg}
N 1120 3480 1120 3480 {lab=vdg}
C {devices/lab_pin.sym} 1120 3480 0 0 {name=p656 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 0 3600 0 0 {name=xr3kq1n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 20 3570 20 3570 {lab=x_r3_kq}
C {devices/lab_pin.sym} 20 3570 0 0 {name=p657 sig_type=std_logic lab=x_r3_kq}
N -20 3600 -20 3600 {lab=x_p3}
C {devices/lab_pin.sym} -20 3600 0 1 {name=p658 sig_type=std_logic lab=x_p3}
N 20 3630 20 3630 {lab=0}
C {devices/lab_pin.sym} 20 3630 0 0 {name=p659 sig_type=std_logic lab=0}
N 20 3600 20 3600 {lab=0}
C {devices/lab_pin.sym} 20 3600 0 0 {name=p660 sig_type=std_logic lab=0}
C {sg13g2_pr/sg13_lv_pmos.sym} 220 3600 0 0 {name=xr3kq2p
w=0.3u
l=0.13u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
N 240 3630 240 3630 {lab=x_p3}
C {devices/lab_pin.sym} 240 3630 0 0 {name=p661 sig_type=std_logic lab=x_p3}
N 200 3600 200 3600 {lab=x_r3_kq}
C {devices/lab_pin.sym} 200 3600 0 1 {name=p662 sig_type=std_logic lab=x_r3_kq}
N 240 3570 240 3570 {lab=vdg}
C {devices/lab_pin.sym} 240 3570 0 0 {name=p663 sig_type=std_logic lab=vdg}
N 240 3600 240 3600 {lab=vdg}
C {devices/lab_pin.sym} 240 3600 0 0 {name=p664 sig_type=std_logic lab=vdg}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 3600 0 0 {name=xr3kq2n
w=0.15u
l=0.13u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
N 460 3570 460 3570 {lab=x_p3}
C {devices/lab_pin.sym} 460 3570 0 0 {name=p665 sig_type=std_logic lab=x_p3}
N 420 3600 420 3600 {lab=x_r3_kq}
C {devices/lab_pin.sym} 420 3600 0 1 {name=p666 sig_type=std_logic lab=x_r3_kq}
N 460 3630 460 3630 {lab=0}
C {devices/lab_pin.sym} 460 3630 0 0 {name=p667 sig_type=std_logic lab=0}
N 460 3600 460 3600 {lab=0}
C {devices/lab_pin.sym} 460 3600 0 0 {name=p668 sig_type=std_logic lab=0}
C {devices/res.sym} 660 3600 0 0 {name=rkr31
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 660 3570 660 3570 {lab=x_r3_a}
C {devices/lab_pin.sym} 660 3570 0 0 {name=p669 sig_type=std_logic lab=x_r3_a}
N 660 3630 660 3630 {lab=0}
C {devices/lab_pin.sym} 660 3630 0 0 {name=p670 sig_type=std_logic lab=0}
C {devices/res.sym} 880 3600 0 0 {name=rkr32
value=100Meg
m=1
footprint=1206
device=resistor
sim_device=resistor
}
N 880 3570 880 3570 {lab=x_r3_b}
C {devices/lab_pin.sym} 880 3570 0 0 {name=p671 sig_type=std_logic lab=x_r3_b}
N 880 3630 880 3630 {lab=0}
C {devices/lab_pin.sym} 880 3630 0 0 {name=p672 sig_type=std_logic lab=0}
