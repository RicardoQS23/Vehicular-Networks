#!/usr/bin/env python
# #####################################################################################################
# SENDING/RECEIVING APPLICATION THREADS - add your business logic here!
# Note: you can use a single thread, if you prefer, but be carefully when dealing with concurrency.
#######################################################################################################
from socket import MsgFlag
import time
from application.message_handler import *
import application.app_config_rsu as app_rsu_conf
from application.rsu_commands import *

#-----------------------------------------------------------------------------------------
# Thread: rsu application transmission. To be completed
#-----------------------------------------------------------------------------------------
def rsu_application_txd(node, start_flag, my_system_rxd_queue, ca_service_txd_queue, den_service_txd_queue):
     
     while not start_flag.isSet():
          time.sleep (1)
     if (app_conf.debug_sys):
          print('STATUS: Ready to start - THREAD: application_txd - NODE: {}'.format(node),'\n')
     time.sleep(app_rsu_conf.warm_up_time)
	# to be completed


#-----------------------------------------------------------------------------------------
# Thread: rsu application reception.  To be completed
#-----------------------------------------------------------------------------------------
def rsu_application_rxd(node, start_flag, services_rxd_queue, my_system_rxd_queue):
     
     while not start_flag.isSet():
           time.sleep (1)
     if (app_conf.debug_sys):
          print('STATUS: Ready to start - THREAD: application_rxd - NODE: {}'.format(node),'\n')
     
  	# to be completed


#-----------------------------------------------------------------------------------------
# Thread: my_system -  implements the business logic of your system. To be completed
#-----------------------------------------------------------------------------------------
def rsu_system(node, start_flag, coordinates, my_system_rxd_queue, rsu_control_txd_queue):
    
     while not start_flag.isSet():
         time.sleep (1)
     if (app_conf.debug_sys):
         print('STATUS: Ready to start - THREAD: my_system - NODE: {}'.format(node),'\n')
  
     
	# to be completed
     
