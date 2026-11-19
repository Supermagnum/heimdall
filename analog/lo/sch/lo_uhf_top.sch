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
C {devices/lab_pin.sym} 200 40 0 0 {name=ttitle lab=lo_uhf_top_hierarchy_P274b}
C {lo_bias.sym} 0 0 0 0 {name=xbias
nbias=nbias
en_lodiv=en_lodiv
nb_lo=nb_lo
vdd=vdd
0=0
}
N -100 -16 -80 -16 {}
C {devices/lab_pin.sym} -100 -16 0 0 {name=l_xbias_nbias lab=nbias}
N -100 -8 -80 -8 {}
C {devices/lab_pin.sym} -100 -8 0 0 {name=l_xbias_en_lodiv lab=en_lodiv}
N -100 0 -80 0 {}
C {devices/lab_pin.sym} -100 0 0 0 {name=l_xbias_nb_lo lab=nb_lo}
N -100 8 -80 8 {}
C {devices/lab_pin.sym} -100 8 0 0 {name=l_xbias_vdd lab=vdd}
N -100 16 -80 16 {}
C {devices/lab_pin.sym} -100 16 0 0 {name=l_xbias_0 lab=0}
C {lo_buffer.sym} 400 0 0 0 {name=xbuf
tp=tp
tn=tn
ckp=ckp
ckn=ckn
vbuf=vbuf
0=0
}
N 300 -20 320 -20 {}
C {devices/lab_pin.sym} 300 -20 0 0 {name=l_xbuf_tp lab=tp}
N 300 -12 320 -12 {}
C {devices/lab_pin.sym} 300 -12 0 0 {name=l_xbuf_tn lab=tn}
N 300 -4 320 -4 {}
C {devices/lab_pin.sym} 300 -4 0 0 {name=l_xbuf_ckp lab=ckp}
N 300 4 320 4 {}
C {devices/lab_pin.sym} 300 4 0 0 {name=l_xbuf_ckn lab=ckn}
N 300 12 320 12 {}
C {devices/lab_pin.sym} 300 12 0 0 {name=l_xbuf_vbuf lab=vbuf}
N 300 20 320 20 {}
C {devices/lab_pin.sym} 300 20 0 0 {name=l_xbuf_0 lab=0}
C {cml_dff_uhf.sym} 800 0 0 0 {name=xdiv
dp=qn
dn=qp
ckp=ckp
ckn=ckn
qp=qp
qn=qn
nb_lo=nb_lo
vdv=vdv
0=0
}
N 700 -32 720 -32 {}
C {devices/lab_pin.sym} 700 -32 0 0 {name=l_xdiv_dp lab=qn}
N 700 -24 720 -24 {}
C {devices/lab_pin.sym} 700 -24 0 0 {name=l_xdiv_dn lab=qp}
N 700 -16 720 -16 {}
C {devices/lab_pin.sym} 700 -16 0 0 {name=l_xdiv_ckp lab=ckp}
N 700 -8 720 -8 {}
C {devices/lab_pin.sym} 700 -8 0 0 {name=l_xdiv_ckn lab=ckn}
N 700 0 720 0 {}
C {devices/lab_pin.sym} 700 0 0 0 {name=l_xdiv_qp lab=qp}
N 700 8 720 8 {}
C {devices/lab_pin.sym} 700 8 0 0 {name=l_xdiv_qn lab=qn}
N 700 16 720 16 {}
C {devices/lab_pin.sym} 700 16 0 0 {name=l_xdiv_nb_lo lab=nb_lo}
N 700 24 720 24 {}
C {devices/lab_pin.sym} 700 24 0 0 {name=l_xdiv_vdv lab=vdv}
N 700 32 720 32 {}
C {devices/lab_pin.sym} 700 32 0 0 {name=l_xdiv_0 lab=0}
C {lo_converter.sym} 1200 0 0 0 {name=xconv
dp=qp
dn=qn
y=x_clk
vcv=vcv
0=0
}
N 1100 -16 1120 -16 {}
C {devices/lab_pin.sym} 1100 -16 0 0 {name=l_xconv_dp lab=qp}
N 1100 -8 1120 -8 {}
C {devices/lab_pin.sym} 1100 -8 0 0 {name=l_xconv_dn lab=qn}
N 1100 0 1120 0 {}
C {devices/lab_pin.sym} 1100 0 0 0 {name=l_xconv_y lab=x_clk}
N 1100 8 1120 8 {}
C {devices/lab_pin.sym} 1100 8 0 0 {name=l_xconv_vcv lab=vcv}
N 1100 16 1120 16 {}
C {devices/lab_pin.sym} 1100 16 0 0 {name=l_xconv_0 lab=0}
C {lo_johnson_uhf.sym} 1600 0 0 0 {name=xjohn
x_clk=x_clk
x_p0=x_p0
x_p1=x_p1
x_p2=x_p2
x_p3=x_p3
vdg=vdg
0=0
}
N 1500 -24 1520 -24 {}
C {devices/lab_pin.sym} 1500 -24 0 0 {name=l_xjohn_x_clk lab=x_clk}
N 1500 -16 1520 -16 {}
C {devices/lab_pin.sym} 1500 -16 0 0 {name=l_xjohn_x_p0 lab=x_p0}
N 1500 -8 1520 -8 {}
C {devices/lab_pin.sym} 1500 -8 0 0 {name=l_xjohn_x_p1 lab=x_p1}
N 1500 0 1520 0 {}
C {devices/lab_pin.sym} 1500 0 0 0 {name=l_xjohn_x_p2 lab=x_p2}
N 1500 8 1520 8 {}
C {devices/lab_pin.sym} 1500 8 0 0 {name=l_xjohn_x_p3 lab=x_p3}
N 1500 16 1520 16 {}
C {devices/lab_pin.sym} 1500 16 0 0 {name=l_xjohn_vdg lab=vdg}
N 1500 24 1520 24 {}
C {devices/lab_pin.sym} 1500 24 0 0 {name=l_xjohn_0 lab=0}
