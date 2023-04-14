
 

from multiprocessing import  Manager, Process
import threading
from time import sleep
from enum import Enum
import numpy as np
import random 
from datetime import datetime
from nicegui import ui
from nicegui.events import ValueChangeEventArguments

class imp_data:                     #class data for locked sharing
    def __init__(self):
        self.file_name = 'name'
        self.probe_nr = '0'
        self.comments = 'no comment'
        self.u_min = 0.0
        self.u_max = 3.0
        self.delta_u = 0.2
        self.t_meas = 20000.0 #ms
        self.I    = 0.0
        self.U    = 0.0
        self.modus = 0
        self.SMachine = 0
        self.error = 0
        self.sig_sn = "0000"
        self.firmware = "V1.0"
        self.time_p    = 0.0
        self.progress = 0.0
    def server_data(self):
        data=np.array([self.SMachine,self.modus,self.error,self.progress,self.file_name,self.probe_nr,self.comments,self.u_min,self.u_max,self.delta_u,self.t_meas,self.I,self.U,self.time_p, self.sig_sn, self.firmware])
        return data

class SM(Enum):                     #Enum type
    INIT        = 0
    READY       = 1
    RUNNING     = 2
    MEASURING   = 3
    PAUSE       = 4
    STOP        = 5
    CANCEL      = 6

class S_DATA(Enum):                 #Enum type
    STATE_MACHINE   = 0
    MODUS           = 1
    ERROR           = 2
    PROGRESS        = 3
    FILE_NAME       = 4
    PROBE_NR        = 5 
    COMMENTS        = 6
    U_MIN           = 7 
    U_MAX           = 8
    DELTA_U         = 9 
    T_MEAS          = 10
    I               = 11 
    U               = 12
    TIME_P          = 13 
    SIG_SN          = 14
    FIRMWARE        = 15

class classMultiPros:
    def __init__(self):  
        self.init = 0
    
    def th(self, server_data):
        while True:
            SMach = int(server_data[S_DATA.STATE_MACHINE.value])
            if SMach == SM.INIT.value:
                print("vai")
                sleep(10)
                server_data[S_DATA.STATE_MACHINE.value] = SM.READY.value
            elif SMach == SM.RUNNING.value:
                sleep(2)
                server_data[S_DATA.STATE_MACHINE.value] = SM.MEASURING.value
            elif SMach == SM.MEASURING.value:
                sleep(10)
                server_data[S_DATA.STATE_MACHINE.value] = SM.STOP.value
            elif SMach == SM.CANCEL.value:
                sleep(10)
                server_data[S_DATA.STATE_MACHINE.value] = SM.READY.value
            elif SMach == SM.STOP.value:    
                sleep(10)
                server_data[S_DATA.STATE_MACHINE.value] = SM.READY.value
           
            server_data[S_DATA.I.value] = random.randint(0,10)
            server_data[S_DATA.U.value] = random.randint(0,10)
            sleep(1)

#if __name__ in {"__main__", "__mp_main__"}:     
if __name__ == "__main__":
    with Manager() as manager:
        #shared data Manages from intern class
        imp_data2 =imp_data()
        data = imp_data2.server_data()
        shared_list = manager.list(data)
        MultPros = classMultiPros()
        p1 = Process(target = MultPros.th, args=(shared_list,))
        p1.start() 
        sleep(3)
        #######################################SERVER CODE################################################################################################
        
        line_plot = ui.line_plot(n=2, limit=20, figsize=(3, 2), update_every=5) \
        .with_legend(['sin', 'cos'], loc='upper center', ncol=2)

        def btn_click() -> None:
            print("Btn clicked")
            if (shared_list[S_DATA.STATE_MACHINE.value]==SM.READY.value):
                shared_list[S_DATA.STATE_MACHINE.value] = SM.RUNNING.value

        def update_line_plot() -> None:
            now = datetime.now()
            x = now.timestamp()
            y1 = np.sin(x)
            y2 = np.cos(x)
            line_plot.push([now], [[float(shared_list[S_DATA.I.value])], [float(shared_list[S_DATA.U.value])]])
            print("I ",shared_list[S_DATA.I.value]," U ",shared_list[S_DATA.U.value],"SM ",shared_list[S_DATA.STATE_MACHINE.value])


        line_updates = ui.timer(0.1, update_line_plot, active=False)
        line_checkbox = ui.checkbox('active').bind_value(line_updates, 'active')
        ui.button('Start', on_click = btn_click)
        ui.button('Button', on_click= lambda: ui.notify('Click'))

        ui.run(title='Yellow-SiC Development',view='web', width=800, height=800, confirm_close= True)
        p1.join()        
                # while 1:    #JUST A PRINT TO SHOW THE CHANGING OF THE VARIABLES. YOU CAN DELETE IT.
                #     print("I ",shared_list[S_DATA.I.value]," U ",shared_list[S_DATA.U.value],"SM ",shared_list[S_DATA.STATE_MACHINE.value])
                #     sleep(0.1)
            
            ##all examples of the 4 permitted SM changing to SERVER program.
            
            # if (shared_list[S_DATA.STATE_MACHINE.value]==SM.READY.value):         #example for code to check if begin is possible and make it meas
                # shared_list[S_DATA.STATE_MACHINE.value]=SM.RUNNING.value

            
            # if (shared_list[S_DATA.STATE_MACHINE.value]==SM.MEASURING.value):        #example to stop code,
                # shared_list[S_DATA.STATE_MACHINE.value]=SM.STOP.value

                
            # if (shared_list[S_DATA.STATE_MACHINE.value]==SM.MEASURING.value):        #example to cancel code
                # shared_list[S_DATA.STATE_MACHINE.value]=SM.CANCEL.value            

                
            # if (shared_list[S_DATA.STATE_MACHINE.value]==SM.MEASURING.value):        #example to pause code
                # shared_list[S_DATA.STATE_MACHINE.value]=SM.PAUSE.value            
            
            #at the and, just one function should be used. It need to look like below. Just the shred_list as input.
            #server_run(shared_list)
                
            #######################################################################################################################################
            
            #p1.join()
                
