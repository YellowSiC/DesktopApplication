import numpy as np
import globals
from multiprocessing import  Manager, Process
import threading
from time import sleep
from enum import Enum
import random 
from datetime import datetime
from nicegui import ui
from nicegui.events import ValueChangeEventArguments
import globals as glob


class imp_data:                     #class data for locked sharing
    def __init__(self):
        self.file_name= 'name'
        self.probe_nr = '0'
        self.comments = 'no comment'
        #________ Erste Feld______
        self.u_min = 0.0
        self.u_max = 3.0
        self.delta_u = 0.2
        self.t_meas = glob.t_meas[0]
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


""" def initial():
        run_it.value              = S_DATA.STATE_MACHINE.value
        run_it.value              = S_DATA.STATE_MACHINE.value
        how_many_times.value      = S_DATA.STATE_MACHINE.value
        modus.value               = S_DATA.STATE_MACHINE.value
        CONNECTED.value           = S_DATA.STATE_MACHINE.value
        VOLTAGE.value             = S_DATA.STATE_MACHINE.value
        BAUDRATE.value            = S_DATA.STATE_MACHINE.value
        PORT.value                = S_DATA.STATE_MACHINE.value
        BYTESIZE.value            = S_DATA.STATE_MACHINE.value
        PARITY.value              = S_DATA.STATE_MACHINE.value
        STOPBITS.value            = S_DATA.STATE_MACHINE.value
        TIMEOUT.value             = S_DATA.STATE_MACHINE.value
        RES.value                 = S_DATA.STATE_MACHINE.value
        UPPER_LIMIT.value         = S_DATA.STATE_MACHINE.value
 """




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


                server_data[S_DATA.STATE_MACHINE.value] = SM.READY.value
            elif SMach == SM.RUNNING.value:


                server_data[S_DATA.STATE_MACHINE.value] = SM.MEASURING.value


            elif SMach == SM.CANCEL.value:
                server_data[S_DATA.STATE_MACHINE.value] = SM.READY.value

            elif SMach == SM.STOP.value:    


                server_data[S_DATA.STATE_MACHINE.value] = SM.READY.value


           
            server_data[S_DATA.I.value] = random.randint(0,10)

            server_data[S_DATA.U.value] = random.randint(0,10)


    
if __name__ == "__main__":
    with Manager() as manager:

        imp_data2 =imp_data()
        data = imp_data2.server_data()
        shared_list = manager.list(data)
        MultPros = classMultiPros()
        p1 = Process(target = MultPros.th, args=(shared_list,))
        p1.start() 
        sleep(3)

        with ui.tabs() as tabs:
            ui.tab('Home', icon='home').style('color: black')
            ui.tab('Lichtquelle', icon='wb_sunny').style('color: black')
            ui.tab('Siglent', icon='device_hub').style('color: black')
            ui.tab('Settings', icon='settings').style('color: black')
            ui.tab('User-Settings', icon='webhook').style('color: black')
        

        with ui.tab_panels(tabs, value='Home'):
            with ui.tab_panel('Home'):
                with ui.card():
                    with ui.row():
                        
                        with ui.row():
                            with ui.row():
                                U_START = ui.input('U-START [V]')
                                
                                
                                U_STOP = ui.input('U-STOP [V]')
                                u_max = ui.input(label='u_max')
                            with ui.row():
                                dU = ui.input('dU [V]')
                                Haltezeit = ui.input('Haltezeit [ms]')
                                file_name = ui.input(label='file_name')
                        
                        with ui.row():
                            with ui.row():
                                probe_nr = ui.input(label='probe_nr')
                                comments = ui.input(label='comments')
                                u_min = ui.input(label='u_min')

                            
                            with ui.row():
                                delta_u = ui.input(label='delta_u')
                                t_meas = ui.input(label='t_meas')
                                t_wait = ui.input(label='t_wait')
                                    
                        

                        with ui.column():

                            def initialisirung():
                                ui.notify('Secssful', position='top-right',type='positive')
                            ui.button('Initialsiren', on_click= initialisirung)
              
                with ui.row():
                    line_plot_strom = ui.line_plot(n=1, limit=120000, figsize=(8, 6), update_every=5).with_legend(['Strom'], loc='upper center', ncol=4)
                    line_plot_spannung = ui.line_plot(n=1, limit=120000, figsize=(8, 6), update_every=5).with_legend(['Spannung'], loc='upper center', ncol=4)

                    def btn_click() -> None:
                            if (shared_list[S_DATA.STATE_MACHINE.value]==SM.READY.value):
                                shared_list[S_DATA.STATE_MACHINE.value] = SM.RUNNING.value

                    def update_line_plot() -> None:
                        now = datetime.now()
                        x = now.timestamp()
                        y1 = np.sin(x)
                        y2 = np.cos(x)

                        line_plot_strom.push([now], [[float(shared_list[S_DATA.I.value])]])
                        line_plot_spannung.push([now], [[float(shared_list[S_DATA.U.value])]])
                        #print("I ",shared_list[S_DATA.I.value]," U ",shared_list[S_DATA.U.value],"SM ",shared_list[S_DATA.STATE_MACHINE.value])
                        
                    line_updates = ui.timer(0.1, update_line_plot, active=False)

                    def update_start(): 
                        if (shared_list[S_DATA.STATE_MACHINE.value] is not SM.READY.value):
                                shared_list[S_DATA.STATE_MACHINE.value] = SM.RUNNING.value 

                        elif (shared_list[S_DATA.STATE_MACHINE.value] is not SM.PAUSE.value):
                                shared_list[S_DATA.STATE_MACHINE.value] = SM.RUNNING.value 


                        line_updates.active = True


                    def update_pause():
                            if (shared_list[S_DATA.STATE_MACHINE.value]==SM.MEASURING.value):
                                shared_list[S_DATA.STATE_MACHINE.value] = SM.PAUSE.value
                                line_updates.active = False
                    
                    def update_stop():
                            if (shared_list[S_DATA.STATE_MACHINE.value]==SM.MEASURING.value):
                                shared_list[S_DATA.STATE_MACHINE.value] = SM.STOP.value
                                line_updates.active = False
                    
                    def update_cancel():
                            if (shared_list[S_DATA.STATE_MACHINE.value]==SM.MEASURING.value):
                                shared_list[S_DATA.STATE_MACHINE.value] = SM.CANCEL.value
                                line_updates.active = False

                start_button = ui.button('START', on_click=update_start).style('margin: 10px')
                pause_button = ui.button('Pause', on_click=update_pause).style('margin: 10px')
                stop_button = ui.button('STOP', on_click=update_stop).style('margin: 10px')
                cancel_button = ui.button('cancel', on_click=update_cancel).style('margin: 10px')
                
                      



                            
                        

        #______________________________Lichtquelle__________________________



        with ui.tab_panels(tabs, value='Lichtquelle'):
            with ui.tab_panel('Lichtquelle'):
                with ui.card().style('margin-left: 450px; margin-top: 45px'):
                    with ui.column():
                        with ui.row():
                            Command = ui.input('Command')
                            Parameter1 = ui.input('Parameter 1 ')
                            Parameter2 = ui.input('Parameter 2 ')
                            ui.button('SendLQ').style('margin: 20px')
                        with ui.column():
                            ui.label('Ansower')
                            array = ui.textarea().style('width: 900px; height: 200px;')
                            Strom = ui.input('Strom: Volt(0.1V)/µA')
                            with ui.row():
                                h2 = ui.input('H2 [ml/min]')
                                Spannung = ui.input('Spannung [V]')
                        

        #_____________________________________Siglent______________________________________



        with ui.tab_panels(tabs, value='Siglent'):
            with ui.tab_panel('Siglent'):
                with ui.card().style('margin-left: 300px'):
                    with ui.column():
                        with ui.row():
                        
                            with ui.card().style('margin:50px'):
                                
                                slider1 = ui.slider(min=0, max=100, value=0).style('width: 800px')
                                with ui.label('Spannung [V]'):
                                    ui.label().bind_text_from(slider1, 'value')
                                    
                            ui.button('Senden').style('margin:50px')
                            
                            
                                
                        with ui.row():
                            
                            with ui.card().style('margin:50px'):
                                slider2 = ui.slider(min=0, max=100, value=0).style('width: 800px')
                                with ui.label('Strom [A]'):
                                    ui.label().bind_text_from(slider2, 'value')
                                    
                            ui.button('Lesen').style('margin:50px')
                            
                        with ui.row():
                            with ui.card().style('margin:50px'):
                                with ui.row():
                                    
                                    ui.input(label='Aktueller Strom [A]')
                                    ui.input(label='Spannung [U]')  
                                ui.switch(text='An/Aus')      



        #___________________________________Settings_____________________________________



        with ui.tab_panels(tabs, value='Settings'):
            with ui.tab_panel('Settings'):

                with ui.row():
                    
                    with ui.card().style('width: 100%; margin-left: 450px'):
                        
                        with ui.label('Siglent').classes('top-left'):
                            with ui.row():
                                siglent_ip = ui.input(label='Siglent-IP')
                                siglent_port = ui.input(label='Siglent-Port')
                                
                              
                            
                            with ui.label('Server').classes('top-right'):
                                with ui.row():
                                    run_it = ui.input(label='run_it')
                                    how_many_times = ui.input(label='how_many_times')
                                    modus = ui.input(label='modus')
                                     
                               
                                    

                                    

                            
                            with ui.label('Arduino'):
                                with ui.row():
                                    CONNECTED = ui.input(label='CONNECTED') 
                                    VOLTAGE = ui.input(label='VOLTAGE')                                     
                                    BAUDRATE = ui.input(label='BAUDRATE')                                     
                                    PORT = ui.input(label='PORT')                                     
                                    BYTESIZE = ui.input(label='BYTESIZE')
                                     
                                with ui.row():
                                    PARITY = ui.input(label='PARITY')
                                    STOPBITS = ui.input(label='STOPBITS')
                                    TIMEOUT = ui.input(label='TIMEOUT')
                                    RES = ui.input(label='RES')
                                    UPPER_LIMIT = ui.input(label='UPPER_LIMIT')
                                    

                        def initial():
                            pass
                            """ siglent_ip.value          = S_DATA.STATE_MACHINE.value
                            siglent_port.value        = S_DATA.STATE_MACHINE.value
                            run_it.value              = S_DATA.STATE_MACHINE.value
                            run_it.value              = S_DATA.STATE_MACHINE.value
                            how_many_times.value      = S_DATA.STATE_MACHINE.value
                            modus.value               = S_DATA.STATE_MACHINE.value
                            CONNECTED.value           = S_DATA.STATE_MACHINE.value
                            VOLTAGE.value             = S_DATA.STATE_MACHINE.value
                            BAUDRATE.value            = S_DATA.STATE_MACHINE.value
                            PORT.value                = S_DATA.STATE_MACHINE.value
                            BYTESIZE.value            = S_DATA.STATE_MACHINE.value
                            PARITY.value              = S_DATA.STATE_MACHINE.value
                            STOPBITS.value            = S_DATA.STATE_MACHINE.value
                            TIMEOUT.value             = S_DATA.STATE_MACHINE.value
                            RES.value                 = S_DATA.STATE_MACHINE.value
                            UPPER_LIMIT.value         = S_DATA.STATE_MACHINE.value
 """


                       

                        mybutton = ui.button('initialisiren', on_click= initial)
                        with ui.card():
                                ui.label('CMD HISTORY')
                                array = ui.textarea().style('width: 900px; height: 200px;')

        with ui.tab_panels(tabs, value='User-Settings'):
            with ui.tab_panel('User-Settings'):
                with ui.card():
                    with ui.column():
                        with ui.row():
                            STATE_MACHINE   = ui.input(label='STATE_MACHINE') 
                            MODUS           = ui.input(label='MODUS') 
                            ERROR           = ui.input(label='ERROR') 
                            PROGRESS        = ui.input(label='PROGRESS') 
                            FILE_NAME       = ui.input(label='FILE_NAME') 
                            PROBE_NR        = ui.input(label='PROBE_NR') 
                            COMMENTS        = ui.input(label='COMMENTS') 
                            U_MIN           = ui.input(label='U_MIN') 
                            U_MAX           = ui.input(label='U_MAX') 
                            DELTA_U         = ui.input(label='DELTA_U') 
                            T_MEAS          = ui.input(label='T_MEAS') 
                            I               = ui.input(label='I') 
                            U               = ui.input(label='U') 
                            TIME_P          = ui.input(label='TIME_P') 
                            SIG_SN          = ui.input(label='SIG_SN') 
                            FIRMWARE        = ui.input(label='FIRMWARE') 


                            def initial_a():
                                shared_list[S_DATA.STATE_MACHINE.value] =STATE_MACHINE.value
                                shared_list[S_DATA.MODUS.value] = MODUS.value 
                                shared_list[S_DATA.ERROR.value] = ERROR.value
                                shared_list[S_DATA.PROGRESS.value] = PROGRESS.value
                                shared_list[S_DATA.FILE_NAME.value]  = str(FILE_NAME.value) 
                                shared_list[S_DATA.COMMENTS.value] = COMMENTS.value
                                shared_list[S_DATA.U_MIN.value] = U_MIN.value 
                                shared_list[S_DATA.U_MAX.value] = U_MAX.value 
                                shared_list[S_DATA.DELTA_U.value] = DELTA_U.value 
                                shared_list[S_DATA.T_MEAS.value] = T_MEAS.value
                                shared_list[S_DATA.I.value] = I.value 
                                shared_list[S_DATA.U.value] = U.value  
                                shared_list[S_DATA.TIME_P.value] = TIME_P.value 
                                shared_list[S_DATA.SIG_SN.value] =SIG_SN.value 
                                shared_list[S_DATA.FIRMWARE.value]=FIRMWARE.value 
                          
                        my_button = ui.button('SAVE', on_click= initial_a)


        ui.run(title='Yellow-SiC Development',view='app', width=800, height=800, confirm_close= True)
        p1.join()     
