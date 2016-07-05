#!../../bin/linux-x86_64/demo

< envPaths
epicsEnvSet("PREFIX", "SR00DEMO01:")
epicsEnvSet("PORT",   "SIM1")
epicsEnvSet("QSIZE",  "20")
epicsEnvSet("XSIZE",  "500")
epicsEnvSet("YSIZE",  "500")
epicsEnvSet("NCHANS", "2048")
epicsEnvSet("CBUFFS", "500")
epicsEnvSet("EPICS_DB_INCLUDE_PATH", "$(ADCORE)/db")
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES", "20000000")

dbLoadDatabase("$(TOP)/dbd/demo.dbd")
demo_registerRecordDeviceDriver pdbbase

simDetectorConfig("$(PORT)", $(XSIZE), $(YSIZE), 1, 0, 0)
dbLoadRecords("$(ADEXAMPLE)/db/simDetector.template","P=$(PREFIX),R=CAM1:,PORT=$(PORT),ADDR=0,TIMEOUT=1")

ffmpegServerConfigure(8000)
ffmpegStreamConfigure("MPEG1", 2, 0, "$(PORT)", "0", -1)
dbLoadRecords("$(FFMPEGSERVER)/db/ffmpegStream.template", "P=$(PREFIX),R=MPEG1:,PORT=MPEG1,ADDR=0,TIMEOUT=1,NDARRAY_PORT=$(PORT)")

iocInit()

epicsThreadSleep(1)

dbpf("$(PREFIX)CAM1:Acquire", "Acquire")
dbpf("$(PREFIX)CAM1:ArrayCallbacks", 1)
dbpf("$(PREFIX)MPEG1:EnableCallbacks", 1)
