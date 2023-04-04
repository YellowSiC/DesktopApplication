from nicegui import ui
import datetime
import numpy as np
import globals


with ui.card().style('background: rgba(47, 43, 41, 0.5); align-items: center ; justify-content: center; width: 100%'):
    ui.image('https://raw.githubusercontent.com/YellowSiC/DesktopApplication/main/public/icon512.png').style('display: initial; width: 50px; height: 50px')
    with ui.tabs() as tabs:
        ui.tab('Config', icon='settings').style('color: black')
        ui.tab('Home', icon='home').style('color: black')
        ui.tab('Lichtquelle', icon='wb_sunny').style('color: black')
        ui.tab('Siglent', icon='device_hub').style('color: black')
        ui.image('')



with ui.tab_panels(tabs, value='Home'):
    with ui.tab_panel('Home'):
       
        with ui.row():
            with ui.column():
                ui.input('U-START [V]')
            with ui.column():
                ui.input('U-STOP [V]')
            with ui.column():
                ui.input('dU [V]')
            with ui.column():
                ui.input('Haltezeit [ms]')

            line_plot = ui.line_plot(n=2, limit=120000, figsize=(15, 5), update_every=5) \
                .with_legend(['sin', 'cos'], loc='upper center', ncol=4).style('margin:10px')

            def update_line_plot() -> None:
                now = datetime.datetime.now()
                x = now.timestamp()
                y1 = np.sin(x)
                y2 = np.cos(x)
                #y3 = np.tan(x)
                #y4 = x**2

                #deff = y2 - y1 / x
                line_plot.push([now], [[y1], [y2]])

            line_updates = ui.timer(0.1, update_line_plot, active=False)
            line_checkbox = ui.checkbox('active').bind_value(line_updates, 'active') 
            with ui.row():      
                ui.button('Initialsiren')
                ui.button('Start')
                ui.button('Stop')

async def data():
    ui.notify(str(ini.value), position='right', type='positive')

with ui.tab_panels(tabs, value='Config'):
    with ui.tab_panel('Config'):

        with ui.row():
            
            with ui.card().style('width: 100%; margin-left: 258px'):
                
                with ui.label('Siglent').classes('top-left'):
                    with ui.row():
                        siglent_ip = ui.input(label='Siglent-IP')
                        siglent_port = ui.input(label='Siglent-Port')
                        ui.update(siglent_ip)
                        ui.update(siglent_port)
                    
                    with ui.label('Server').classes('top-right'):
                        with ui.row():
                            ui.input(label='run_it')
                            ui.input(label='how_many_times')
                            ui.input(label='modus')   
                    with ui.label('Electrolyse').classes('center'):
                        with ui.row():
                            ui.input(label='file_name')
                            ui.input(label='probe_nr')
                            ui.input(label='comments')
                            ui.input(label='u_min')
                        with ui.row():
                            ui.input(label='u_max')
                            ui.input(label='delta_u')
                            ui.input(label='t_meas')
                            ui.input(label='t_wait')
                    with ui.label('Arduino').classes('center'):
                        with ui.row():
                            ui.input(label='CONNECTED')
                            ui.input(label='VOLTAGE')
                            ui.input(label='BAUDRATE')
                            ui.input(label='PORT')
                            ui.input(label='BYTESIZE')
                        with ui.row():
                            ui.input(label='PARITY')
                            ui.input(label='STOPBITS')
                            ui.input(label='TIMEOUT')
                            ui.input(label='RES')
                            ui.input(label='UPPER_LIMIT')
        ui.button('initialisiren', on_click=data).style('margin:10px; margin-left: 658px')
                
            


with ui.tab_panels(tabs, value='Lichtquelle'):
    with ui.tab_panel('Lichtquelle'):
        with ui.row():
            with ui.column():
                ui.label('TODO')
                


with ui.tab_panels(tabs, value='Siglent'):
    with ui.tab_panel('Siglent'):
        with ui.row():
            with ui.column():
                ui.label('TODO')
            
                
          




ui.run(native=True,tailwind=True, title='Yellow-SiC', favicon='https://raw.githubusercontent.com/YellowSiC/DesktopApplication/main/public/icon512.png')