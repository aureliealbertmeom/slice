
# Machines list

machine_list=['adastra','jean-zay','irene']

# Directories on each machine

script_path={}
script_path['adastra']='/lus/home/CT1/ige2071/aalbert/git/extractions-MEOM'

nco_path={}
nco_path['adastra']='/lus/home/CT1/ige2071/aalbert/.conda/envs/nco/bin'

cdf_path={}
cdf_path['adastra']='/lus/work/CT1/ige2071/aalbert/git/CDFTOOLS/bin'

scratch_path={}
scratch_path['adastra']='/lus/scratch/CT1/hmg2840/aalbert/TMPEXTRACT'

store_path={}
store_path['adastra']='/lus/store/CT1/hmg2840/aalbert/'

# All the configurations available on each machine

configuration_list={}
configuration_list['adastra']=['CALEDO60','eNATL60']

# All the simulations run with each configuration on each machine

simulation_list={}
simulation_list['adastra']={}
simulation_list['adastra']['CALEDO60']=['TRPC12NT0','TRPC12N00']
simulation_list['adastra']['eNATL60']=['BLBT02','BLB002']

# Where to find the -S directory for a given simulation of a configuration on a machine and how it is organized

directory={}
directory['adastra']={}
directory['adastra']['CALEDO60']={}
directory['adastra']['CALEDO60']['TRPC12NT0']='/lus/store/CT1/ige2071/brodeau/TROPICO12/TROPICO12_NST-TRPC12NT0-S'
directory['adastra']['eNATL60']['BLBT02']='/lus/store/CT1/hmg2840/brodeau/eNATL60'
directory['adastra']['eNATL60']['BLB002']='/lus/store/CT1/hmg2840/brodeau/eNATL60'

stylenom={}
stylenom['adastra']={}
stylenom['adastra']['CALEDO60']={}
stylenom['adastra']['CALEDO60']['TRPC12NT0']='brodeau_nst'
for sim in ['BLBT02','BLB002']:
    stylenom['adastra']['eNATL60'][sim]='brodeau_enatl'

# All the regions we can extract in a configuration and the associated parameters

regions_list={}
regions_list['CALEDO60']=['CALEDO60']
regions_list['eNATL60']=['eNATL60']

xy={}
xy['CALEDO60']={}
xy['CALEDO60']['CALEDO60']=''
xy['eNATL60']={}
xy['eNATL60']['eNATL60']=''

ex={}
ex['CALEDO60']={}
ex['CALEDO60']['CALEDO60']=''
ex['eNATL60']={}
ex['eNATL60']['eNATL60']=''

# All the variables we can extract and the associated name and filetyp for each simulations

variable_list=['SSH','SSU','SSV','SST','SSS','T','S','U','V','W','TAUM','TAUBOT','QTOCE','QSROCE','QSBOCE','QNSOCE','QLWOCE','QLAOCE','PRECIP','EVAPOCE','EMPMR','WINDSP','RHOAIR','MLD','SBU','TAUUO','SBV','TAUVO']

vars_name={}
for sim in ['TRPC12NT0','TRPC12N00']:
    vars_name[sim]={'SSH':'z s','SSU':'uos','SSV':'vos'}
for sim in ['BLBT02','BLB002']:
    vars_name[sim]={'SSH':'sossheig','SSU':'sozocrtx','SSV':'somecrty','SST':'sosstsst','SSS':'sosaline','MLD':'somxl010','BOTU':'bozocrtx','BOTV':'bomecrty'}

filetyp={}
for sim in ['TRPC12NT0','TRPC12N00']:
    filetyp[sim]={'SSH':'gridT-2D','SSU':'gridU-2D','SSV':'gridV-2D'}
for sim in ['BLBT02','BLB002']:
    filetyp[sim]={'SSH':'gridT-2D','SSS':'gridT-2D','SST':'gridT-2D','MLD':'gridT-2D','SSU':'gridU-2D','SSV':'gridV-2D'}

vars_dim={'SSH':'2D','SST':'2D','SSS':'2D','SSU':'2D','SSV':'2D','T':'3D','S':'3D','U':'3D','V':'3D','W':'3D','TAUM':'2D','TAUBOT':'2D','QTOCE':'2D','QSROCE':'2D','QSBOCE':'2D','QNSOCE':'2D','QLWOCE':'2D','QLAOCE':'2D','PRECIP':'2D','EVAPOCE':'2D','EMPMR':'2D','WINDSP':'2D','RHOAIR':'2D','MLD':'2D','BOTU':'2D','TAUUO':'2D','BOTV':'2D','TAUVO':'2D'}
# The time frequency available for a given variable and simulation

frequencies={}
for sim in ['TRPC12NT0','TRPC12N00']:
    frequencies[sim]={'SSH':'1h','SSU':'1h','SSV':'1h'}
for sim in ['BLBT02','BLB002']:
    frequencies[sim]={'SSH':'1h','SSS':'1h','SST':'1h','SSU':'1h','SSV':'1h'}

# The period of time covered by a simulation
sim_date_init={}
for sim in ['TRPC12NT0','TRPC12N00']:
    sim_date_init[sim]='2012-01-01'
    sim_date_end[sim]='2018-12-31'
for sim in ['BLBT02','BLB002']:
    sim_date_init[sim]='2009-07-01'
    sim_date_end[sim]='2010-06-30'




