from nicegui import ui
import datetime
import numpy as np
import globals
from multiprocessing import  Manager, Process
import threading
from time import sleep
from enum import Enum
import numpy as np
import random 
import datetime
from nicegui import ui
from nicegui.events import ValueChangeEventArguments
data = []


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



with ui.tabs() as tabs:
    ui.tab('Home', icon='home').style('color: black')
    ui.tab('Lichtquelle', icon='wb_sunny').style('color: black')
    ui.tab('Siglent', icon='device_hub').style('color: black')
    ui.tab('Settings', icon='settings').style('color: black')
   



with ui.tab_panels(tabs, value='Home'):
    with ui.tab_panel('Home'):
       
        with ui.row():
            with ui.column():
                U_START = ui.input('U-START [V]')
            with ui.column():
                U_STOP = ui.input('U-STOP [V]')
            with ui.column():
                dU = ui.input('dU [V]')
            with ui.column():
                Haltezeit = ui.input('Haltezeit [ms]')

            with ui.column():

                def initialisirung():
                    ui.notify('Secssful', position='top-right',type='positive')
                ui.button('Initialsiren', on_click= initialisirung)

            line_plot = ui.line_plot(n=2, limit=120000, figsize=(15, 5), update_every=5) \
                .with_legend(['sin', 'cos'], loc='upper center', ncol=4).style('margin:10px')

            def update_line_plot() -> None:
                now = datetime.datetime.now()
                x = now.timestamp()
                y1 = np.sin(x)
                y2 = np.cos(x)
                line_plot.push([now], [[y1], [y2]])
            line_updates = ui.timer(0.1, update_line_plot, active=False)
            line_checkbox = ui.checkbox('Start').bind_value(line_updates, 'active') 
            



                
            

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
                        ui.update(siglent_ip)
                        ui.update(siglent_port)
                    
                    with ui.label('Server').classes('top-right'):
                        with ui.row():
                            run_it = ui.input(label='run_it')
                            how_many_times = ui.input(label='how_many_times')
                            modus = ui.input(label='modus')   
                            ui.update(siglent_ip)
                            ui.update(siglent_port)
                            ui.update(siglent_port)
                            

                            

                    with ui.label('Electrolyse'):
                        with ui.row():
                            file_name = ui.input(label='file_name')
                            probe_nr = ui.input(label='probe_nr')
                            comments = ui.input(label='comments')
                            u_min = ui.input(label='u_min')
                        with ui.row():
                            u_max = ui.input(label='u_max')
                            delta_u = ui.input(label='delta_u')
                            t_meas = ui.input(label='t_meas')
                            t_wait = ui.input(label='t_wait')
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


                async def initial():
                            data.append(siglent_ip.value)
                            data.append(siglent_port.value)
                            data.append(run_it.value)
                            data.append(how_many_times.value)
                            data.append(modus.value)
                            data.append(file_name.value)
                            data.append(probe_nr.value)
                            data.append(comments.value)
                            data.append(u_min.value)
                            data.append(u_max.value)
                            data.append(delta_u.value)
                            data.append(t_meas.value)
                            data.append(t_wait.value)
                            data.append(CONNECTED.value)
                            data.append(VOLTAGE.value)
                            data.append(BAUDRATE.value)
                            data.append(PORT.value)
                            data.append(BYTESIZE.value)
                            data.append(PARITY.value)
                            data.append(STOPBITS.value)
                            data.append(TIMEOUT.value)
                            data.append(RES.value)
                            data.append(UPPER_LIMIT.value)
                            array.value = data
                            ui.update(array)

                mybutton = ui.button('initialisiren', on_click=initial).style('margin:10px; margin-left: 358px')
                with ui.card():
                        ui.label('CMD HISTORY')
                        array = ui.textarea().style('width: 900px; height: 200px;')



ui.run(tailwind=True, title='Yellow-SiC', favicon='https://raw.githubusercontent.com/YellowSiC/DesktopApplication/main/public/icon512.png')