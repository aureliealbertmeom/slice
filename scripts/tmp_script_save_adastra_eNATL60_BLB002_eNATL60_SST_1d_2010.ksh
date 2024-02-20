#!/bin/bash

CONFIG=eNATL60
CASE=BLB002
REG=eNATL60
SREG=
VAR=SST
FREQ=1d
YYYY=2010

TDIR=/lus/scratch/CT1/hmg2840/aalbert/TMPEXTRACT/${CONFIG}/${CONFIG}-${CASE}/${REG}/${FREQ}
STDIR=/lus/store/CT1/hmg2840/aalbert//${CONFIG}/${CONFIG}-${CASE}/${REG}/${FREQ}

mkdir -p $STDIR

cd $TDIR

echo "We are in " $TDIR

ulimit -s unlimited

if [ ! -f ${STDIR}/eNATL60-BLB002_y2010.1d_SST.tar ]; then
	tar -cvf eNATL60-BLB002_y2010.1d_SST.tar ${CONFIG}${SREG}-${CASE}_y${YYYY}*.${FREQ}_${VAR}.nc
	dd if=eNATL60-BLB002_y2010.1d_SST.tar of=${STDIR}/eNATL60-BLB002_y2010.1d_SST.tar bs=20M
else
	echo "be careful, archive already exists, erase it first if you want to replace it"
fi

