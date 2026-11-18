v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
C {devices/iopin.sym} -200 -40 0 0 {name=tp lab=tp}
C {devices/iopin.sym} -200 -80 0 0 {name=tn lab=tn}
C {devices/iopin.sym} -200 -120 0 0 {name=ct lab=ct}
C {devices/iopin.sym} -200 -160 0 0 {name=vt lab=vt}
C {devices/iopin.sym} -200 -200 0 0 {name=vdd lab=vdd}
C {devices/iopin.sym} -200 -240 0 0 {name=gnd lab=gnd}
C {devices/iopin.sym} -200 -280 0 0 {name=vbp lab=vbp}
C {devices/iopin.sym} -200 -320 0 0 {name=vbp_tail lab=vbp_tail}
C {devices/iopin.sym} -200 -360 0 0 {name=cmp lab=cmp}
C {devices/iopin.sym} -200 -400 0 0 {name=tail lab=tail}
C {devices/iopin.sym} -200 -440 0 0 {name=hold lab=hold}
C {devices/iopin.sym} -200 -480 0 0 {name=rep lab=rep}
C {devices/iopin.sym} -200 -520 0 0 {name=en lab=en}
C {devices/iopin.sym} -200 -560 0 0 {name=vthn lab=vthn}
C {devices/iopin.sym} -200 -600 0 0 {name=g0 lab=g0}
C {devices/iopin.sym} -200 -640 0 0 {name=g1 lab=g1}
C {devices/iopin.sym} -200 -680 0 0 {name=g2 lab=g2}
C {devices/iopin.sym} -200 -720 0 0 {name=g3 lab=g3}
C {devices/iopin.sym} -200 -760 0 0 {name=g4 lab=g4}
C {devices/iopin.sym} -200 -800 0 0 {name=g5 lab=g5}
C {devices/iopin.sym} -200 -840 0 0 {name=g6 lab=g6}
C {devices/iopin.sym} -200 -880 0 0 {name=g7 lab=g7}
C {devices/iopin.sym} -200 -920 0 0 {name=g8 lab=g8}
C {devices/iopin.sym} -200 -960 0 0 {name=g9 lab=g9}
C {devices/iopin.sym} -200 -1000 0 0 {name=g10 lab=g10}
C {devices/iopin.sym} -200 -1040 0 0 {name=g11 lab=g11}
C {devices/iopin.sym} -200 -1080 0 0 {name=code0 lab=code0}
C {devices/iopin.sym} -200 -1120 0 0 {name=code1 lab=code1}
C {devices/iopin.sym} -200 -1160 0 0 {name=code2 lab=code2}
C {devices/iopin.sym} -200 -1200 0 0 {name=code3 lab=code3}
C {devices/iopin.sym} -200 -1240 0 0 {name=code4 lab=code4}
C {devices/title.sym} 0 40 0 0 {name=t1 author="HT13G-M P2.7.1"}
C {devices/lab_pin.sym} 200 40 0 0 {name=ttitle lab=vco_top_P272a_hier}
C {l2n0.sym} 0 0 0 0 {name=xl
p=tp
n=tn
ct=ct
}
N -100 -8 -80 -8 {}
C {devices/lab_pin.sym} -100 -8 0 0 {name=l_xl_p lab=tp}
N -100 0 -80 0 {}
C {devices/lab_pin.sym} -100 0 0 0 {name=l_xl_n lab=tn}
N -100 8 -80 8 {}
C {devices/lab_pin.sym} -100 8 0 0 {name=l_xl_ct lab=ct}
C {vco_core.sym} 220 0 0 0 {name=xcore
tp=tp
tn=tn
tail=tail
ct=ct
vdd=vdd
gnd=gnd
}
N 120 -20 140 -20 {}
C {devices/lab_pin.sym} 120 -20 0 0 {name=l_xcore_tp lab=tp}
N 120 -12 140 -12 {}
C {devices/lab_pin.sym} 120 -12 0 0 {name=l_xcore_tn lab=tn}
N 120 -4 140 -4 {}
C {devices/lab_pin.sym} 120 -4 0 0 {name=l_xcore_tail lab=tail}
N 120 4 140 4 {}
C {devices/lab_pin.sym} 120 4 0 0 {name=l_xcore_ct lab=ct}
N 120 12 140 12 {}
C {devices/lab_pin.sym} 120 12 0 0 {name=l_xcore_vdd lab=vdd}
N 120 20 140 20 {}
C {devices/lab_pin.sym} 120 20 0 0 {name=l_xcore_gnd lab=gnd}
C {vco_bank.sym} 440 0 0 0 {name=xbank
tp=tp
tn=tn
vbp=vbp
gnd=gnd
g0=g0
bb0=bb0
g1=g1
bb1=bb1
g2=g2
bb2=bb2
g3=g3
bb3=bb3
g4=g4
bb4=bb4
g5=g5
bb5=bb5
g6=g6
bb6=bb6
g7=g7
bb7=bb7
g8=g8
bb8=bb8
g9=g9
bb9=bb9
g10=g10
bb10=bb10
g11=g11
bb11=bb11
}
N 340 -108 360 -108 {}
C {devices/lab_pin.sym} 340 -108 0 0 {name=l_xbank_tp lab=tp}
N 340 -100 360 -100 {}
C {devices/lab_pin.sym} 340 -100 0 0 {name=l_xbank_tn lab=tn}
N 340 -92 360 -92 {}
C {devices/lab_pin.sym} 340 -92 0 0 {name=l_xbank_vbp lab=vbp}
N 340 -84 360 -84 {}
C {devices/lab_pin.sym} 340 -84 0 0 {name=l_xbank_gnd lab=gnd}
N 340 -76 360 -76 {}
C {devices/lab_pin.sym} 340 -76 0 0 {name=l_xbank_g0 lab=g0}
N 340 -68 360 -68 {}
C {devices/lab_pin.sym} 340 -68 0 0 {name=l_xbank_bb0 lab=bb0}
N 340 -60 360 -60 {}
C {devices/lab_pin.sym} 340 -60 0 0 {name=l_xbank_g1 lab=g1}
N 340 -52 360 -52 {}
C {devices/lab_pin.sym} 340 -52 0 0 {name=l_xbank_bb1 lab=bb1}
N 340 -44 360 -44 {}
C {devices/lab_pin.sym} 340 -44 0 0 {name=l_xbank_g2 lab=g2}
N 340 -36 360 -36 {}
C {devices/lab_pin.sym} 340 -36 0 0 {name=l_xbank_bb2 lab=bb2}
N 340 -28 360 -28 {}
C {devices/lab_pin.sym} 340 -28 0 0 {name=l_xbank_g3 lab=g3}
N 340 -20 360 -20 {}
C {devices/lab_pin.sym} 340 -20 0 0 {name=l_xbank_bb3 lab=bb3}
N 340 -12 360 -12 {}
C {devices/lab_pin.sym} 340 -12 0 0 {name=l_xbank_g4 lab=g4}
N 340 -4 360 -4 {}
C {devices/lab_pin.sym} 340 -4 0 0 {name=l_xbank_bb4 lab=bb4}
N 340 4 360 4 {}
C {devices/lab_pin.sym} 340 4 0 0 {name=l_xbank_g5 lab=g5}
N 340 12 360 12 {}
C {devices/lab_pin.sym} 340 12 0 0 {name=l_xbank_bb5 lab=bb5}
N 340 20 360 20 {}
C {devices/lab_pin.sym} 340 20 0 0 {name=l_xbank_g6 lab=g6}
N 340 28 360 28 {}
C {devices/lab_pin.sym} 340 28 0 0 {name=l_xbank_bb6 lab=bb6}
N 340 36 360 36 {}
C {devices/lab_pin.sym} 340 36 0 0 {name=l_xbank_g7 lab=g7}
N 340 44 360 44 {}
C {devices/lab_pin.sym} 340 44 0 0 {name=l_xbank_bb7 lab=bb7}
N 340 52 360 52 {}
C {devices/lab_pin.sym} 340 52 0 0 {name=l_xbank_g8 lab=g8}
N 340 60 360 60 {}
C {devices/lab_pin.sym} 340 60 0 0 {name=l_xbank_bb8 lab=bb8}
N 340 68 360 68 {}
C {devices/lab_pin.sym} 340 68 0 0 {name=l_xbank_g9 lab=g9}
N 340 76 360 76 {}
C {devices/lab_pin.sym} 340 76 0 0 {name=l_xbank_bb9 lab=bb9}
N 340 84 360 84 {}
C {devices/lab_pin.sym} 340 84 0 0 {name=l_xbank_g10 lab=g10}
N 340 92 360 92 {}
C {devices/lab_pin.sym} 340 92 0 0 {name=l_xbank_bb10 lab=bb10}
N 340 100 360 100 {}
C {devices/lab_pin.sym} 340 100 0 0 {name=l_xbank_g11 lab=g11}
N 340 108 360 108 {}
C {devices/lab_pin.sym} 340 108 0 0 {name=l_xbank_bb11 lab=bb11}
C {vco_var.sym} 660 0 0 0 {name=xvar
tp=tp
tn=tn
vt=vt
vbp=vbp
gnd=gnd
}
N 560 -16 580 -16 {}
C {devices/lab_pin.sym} 560 -16 0 0 {name=l_xvar_tp lab=tp}
N 560 -8 580 -8 {}
C {devices/lab_pin.sym} 560 -8 0 0 {name=l_xvar_tn lab=tn}
N 560 0 580 0 {}
C {devices/lab_pin.sym} 560 0 0 0 {name=l_xvar_vt lab=vt}
N 560 8 580 8 {}
C {devices/lab_pin.sym} 560 8 0 0 {name=l_xvar_vbp lab=vbp}
N 560 16 580 16 {}
C {devices/lab_pin.sym} 560 16 0 0 {name=l_xvar_gnd lab=gnd}
C {vco_tail_dac.sym} 220 280 0 0 {name=xtail
tail=tail
vdd=vdd
gnd=gnd
vbp_tail=vbp_tail
nb=nb
nbf=nbf
code0=code0
code1=code1
code2=code2
code3=code3
code4=code4
}
N 120 240 140 240 {}
C {devices/lab_pin.sym} 120 240 0 0 {name=l_xtail_tail lab=tail}
N 120 248 140 248 {}
C {devices/lab_pin.sym} 120 248 0 0 {name=l_xtail_vdd lab=vdd}
N 120 256 140 256 {}
C {devices/lab_pin.sym} 120 256 0 0 {name=l_xtail_gnd lab=gnd}
N 120 264 140 264 {}
C {devices/lab_pin.sym} 120 264 0 0 {name=l_xtail_vbp_tail lab=vbp_tail}
N 120 272 140 272 {}
C {devices/lab_pin.sym} 120 272 0 0 {name=l_xtail_nb lab=nb}
N 120 280 140 280 {}
C {devices/lab_pin.sym} 120 280 0 0 {name=l_xtail_nbf lab=nbf}
N 120 288 140 288 {}
C {devices/lab_pin.sym} 120 288 0 0 {name=l_xtail_code0 lab=code0}
N 120 296 140 296 {}
C {devices/lab_pin.sym} 120 296 0 0 {name=l_xtail_code1 lab=code1}
N 120 304 140 304 {}
C {devices/lab_pin.sym} 120 304 0 0 {name=l_xtail_code2 lab=code2}
N 120 312 140 312 {}
C {devices/lab_pin.sym} 120 312 0 0 {name=l_xtail_code3 lab=code3}
N 120 320 140 320 {}
C {devices/lab_pin.sym} 120 320 0 0 {name=l_xtail_code4 lab=code4}
C {ampcal_det.sym} 440 280 0 0 {name=xdet
tp=tp
tn=tn
ct=ct
vdd=vdd
gnd=gnd
cmp=cmp
hold=hold
rep=rep
en=en
vthn=vthn
}
N 340 244 360 244 {}
C {devices/lab_pin.sym} 340 244 0 0 {name=l_xdet_tp lab=tp}
N 340 252 360 252 {}
C {devices/lab_pin.sym} 340 252 0 0 {name=l_xdet_tn lab=tn}
N 340 260 360 260 {}
C {devices/lab_pin.sym} 340 260 0 0 {name=l_xdet_ct lab=ct}
N 340 268 360 268 {}
C {devices/lab_pin.sym} 340 268 0 0 {name=l_xdet_vdd lab=vdd}
N 340 276 360 276 {}
C {devices/lab_pin.sym} 340 276 0 0 {name=l_xdet_gnd lab=gnd}
N 340 284 360 284 {}
C {devices/lab_pin.sym} 340 284 0 0 {name=l_xdet_cmp lab=cmp}
N 340 292 360 292 {}
C {devices/lab_pin.sym} 340 292 0 0 {name=l_xdet_hold lab=hold}
N 340 300 360 300 {}
C {devices/lab_pin.sym} 340 300 0 0 {name=l_xdet_rep lab=rep}
N 340 308 360 308 {}
C {devices/lab_pin.sym} 340 308 0 0 {name=l_xdet_en lab=en}
N 340 316 360 316 {}
C {devices/lab_pin.sym} 340 316 0 0 {name=l_xdet_vthn lab=vthn}
