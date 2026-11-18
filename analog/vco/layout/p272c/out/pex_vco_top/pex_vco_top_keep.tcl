
crashbackups stop
drc off
gds read /foss/designs/analog/vco/layout/p272c/out/pex_vco_top/vco_top.gds
load vco_top
select top cell
flatten vco_top_flat
load vco_top_flat
cellname delete vco_top
cellname rename vco_top_flat vco_top
select top cell
extract path /foss/designs/analog/vco/layout/p272c/out/pex_vco_top
ext2spice lvs
extresist threshold 100
extresist mindelay 0
extresist minres 50
extract do resistance
extract do unique
extract all
ext2spice extresist on
ext2spice cthresh 0.01
ext2spice -p /foss/designs/analog/vco/layout/p272c/out/pex_vco_top -o /foss/designs/analog/vco/layout/p272c/out/pex_vco_top/vco_top.pex.spice
quit -noprompt
