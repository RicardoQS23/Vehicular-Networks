#!/usr/bin/env python
# #####################################################################################################
# rsu_control comamnds: output test only with: single pin (led) and set of pind (traffic light)
#   Note: modifications required, for complex traffic light systems (with more than one semaphore)
#######################################################################################################
import application.app_config as app_conf

def start_rsu(rsu_control_txd_queue):
    if (app_conf.debug_app) or (app_conf.debug_rsu):
        print ('rsu_application: start_rsu')

    rsu_control_msg="s"
    rsu_control_txd_queue.put(rsu_control_msg)
    return 


def exit_rsu(rsu_control_txd_queue):
    if (app_conf.debug_app) or (app_conf.debug_rsu):
        print ('rsu_application: exit_rsu')
    rsu_control_msg="x"
    rsu_control_txd_queue.put(rsu_control_msg)
    return 

def turn_on(rsu_control_txd_queue):
    if (app_conf.debug_app) or (app_conf.debug_rsu):
        print ('rsu_application: turn_on')
    rsu_control_msg="1"
    rsu_control_txd_queue.put(rsu_control_msg)
    return 

def turn_off(rsu_control_txd_queue):
    if (app_conf.debug_app) or (app_conf.debug_rsu):
        print ('rsu_application: turn_off')
    rsu_control_msg="0"
    rsu_control_txd_queue.put(rsu_control_msg)
    return 

def green_tls(rsu_control_txd_queue):
    if (app_conf.debug_app) or (app_conf.debug_rsu):
        print ('rsu_application: green_tls')
    rsu_control_msg="s_green"
    rsu_control_txd_queue.put(rsu_control_msg)
    return 

def yellow_tls(rsu_control_txd_queue):
    if (app_conf.debug_app) or (app_conf.debug_rsu):
        print ('rsu_application: yellow_tls')
    rsu_control_msg="s_yellow"
    rsu_control_txd_queue.put(rsu_control_msg)
    return 

def red_tls(rsu_control_txd_queue):
    if (app_conf.debug_app) or (app_conf.debug_rsu):
        print ('rsu_application: red_tls')
    rsu_control_msg="s_red"
    rsu_control_txd_queue.put(rsu_control_msg)
    return 


