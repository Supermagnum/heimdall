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
C {devices/lab_pin.sym} 200 40 0 0 {name=ttitle lab=lo_uhf_hier_leaf_symbols}
C {cml_latch_uhf.sym} 0 0 0 0 {name=xlat0
dp=dp
dn=dn
ckp=ckp
ckn=ckn
qp=qp
qn=qn
nb_lo=nb_lo
vdd=vdd
0=0
}
N -100 -32 -80 -32 {}
C {devices/lab_pin.sym} -100 -32 0 0 {name=l_xlat0_dp lab=dp}
N -100 -24 -80 -24 {}
C {devices/lab_pin.sym} -100 -24 0 0 {name=l_xlat0_dn lab=dn}
N -100 -16 -80 -16 {}
C {devices/lab_pin.sym} -100 -16 0 0 {name=l_xlat0_ckp lab=ckp}
N -100 -8 -80 -8 {}
C {devices/lab_pin.sym} -100 -8 0 0 {name=l_xlat0_ckn lab=ckn}
N -100 0 -80 0 {}
C {devices/lab_pin.sym} -100 0 0 0 {name=l_xlat0_qp lab=qp}
N -100 8 -80 8 {}
C {devices/lab_pin.sym} -100 8 0 0 {name=l_xlat0_qn lab=qn}
N -100 16 -80 16 {}
C {devices/lab_pin.sym} -100 16 0 0 {name=l_xlat0_nb_lo lab=nb_lo}
N -100 24 -80 24 {}
C {devices/lab_pin.sym} -100 24 0 0 {name=l_xlat0_vdd lab=vdd}
N -100 32 -80 32 {}
C {devices/lab_pin.sym} -100 32 0 0 {name=l_xlat0_0 lab=0}
C {cml_diff_pair.sym} 400 0 0 0 {name=xpair0
d1=d1
d2=d2
g1=g1
g2=g2
s=s
0=0
}
N 300 -20 320 -20 {}
C {devices/lab_pin.sym} 300 -20 0 0 {name=l_xpair0_d1 lab=d1}
N 300 -12 320 -12 {}
C {devices/lab_pin.sym} 300 -12 0 0 {name=l_xpair0_d2 lab=d2}
N 300 -4 320 -4 {}
C {devices/lab_pin.sym} 300 -4 0 0 {name=l_xpair0_g1 lab=g1}
N 300 4 320 4 {}
C {devices/lab_pin.sym} 300 4 0 0 {name=l_xpair0_g2 lab=g2}
N 300 12 320 12 {}
C {devices/lab_pin.sym} 300 12 0 0 {name=l_xpair0_s lab=s}
N 300 20 320 20 {}
C {devices/lab_pin.sym} 300 20 0 0 {name=l_xpair0_0 lab=0}
C {lo_bias.sym} 800 0 0 0 {name=xbias
nbias=nbias
en_lodiv=en_lodiv
nb_lo=nb_lo
vdd=vdd
0=0
}
N 700 -16 720 -16 {}
C {devices/lab_pin.sym} 700 -16 0 0 {name=l_xbias_nbias lab=nbias}
N 700 -8 720 -8 {}
C {devices/lab_pin.sym} 700 -8 0 0 {name=l_xbias_en_lodiv lab=en_lodiv}
N 700 0 720 0 {}
C {devices/lab_pin.sym} 700 0 0 0 {name=l_xbias_nb_lo lab=nb_lo}
N 700 8 720 8 {}
C {devices/lab_pin.sym} 700 8 0 0 {name=l_xbias_vdd lab=vdd}
N 700 16 720 16 {}
C {devices/lab_pin.sym} 700 16 0 0 {name=l_xbias_0 lab=0}
