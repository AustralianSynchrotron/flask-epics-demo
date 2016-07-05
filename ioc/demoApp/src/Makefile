TOP=../..

include $(TOP)/configure/CONFIG
PROD_NAME = demo
PROD_IOC = $(PROD_NAME)
DBD += $(PROD_NAME).dbd

$(PROD_NAME)_DBD += base.dbd

$(PROD_NAME)_DBD += commonDriverSupport.dbd

PROD_LIBS               += NDPlugin ADBase netCDF
PROD_LIBS               += asyn calc busy sscan autosave
PROD_LIBS               += $(EPICS_BASE_IOC_LIBS)

$(PROD_NAME)_DBD += simDetectorSupport.dbd
PROD_LIBS += simDetector

$(PROD_NAME)_DBD += ffmpegServer.dbd
PROD_LIBS += ffmpegServer

$(PROD_NAME)_SRCS += $(PROD_NAME)_registerRecordDeviceDriver.cpp
$(PROD_NAME)_SRCS_DEFAULT += $(PROD_NAME)Main.cpp

$(PROD_NAME)_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
