from nicegui import ui



with ui.card().style('background: rgba(47, 43, 41, 0.5); align-items: center ; justify-content: center; width: 100%'):
    ui.image('https://raw.githubusercontent.com/YellowSiC/DesktopApplication/main/public/icon512.png').style('display: initial; width: 50px; height: 50px')
    with ui.tabs() as tabs:
        ui.tab('Config', icon='settings').style('color: black')
        ui.tab('Main', icon='home').style('color: black')
        ui.tab('Lichtquelle', icon='wb_sunny').style('color: black')
        ui.tab('Siglent', icon='device_hub').style('color: black')
        ui.image('')



with ui.tab_panels(tabs, value='Main'):
    with ui.tab_panel('Main'):
        with ui.card():
            with ui.row():
                with ui.column():
                    ui.input('U-START [V]')
                with ui.column():
                    ui.input('U-STOP [V]')
                with ui.column():
                    ui.input('dU [V]')
                with ui.column():
                    ui.input('Haltezeit [ms]')
                    
            ui.button('START').style('background-color: rgb(0, 26, 255')


with ui.tab_panels(tabs, value='Config'):
    with ui.tab_panel('Config'):
        #Haupt DIV(CARD)

        with ui.card().style('width: 1470px;'):

            with ui.row():
                with ui.row():
                    #Siglent DIV(CARD)
                    with ui.card().style('margin: 36px;'):
                        with ui.label('Siglent'):
                            ui.input(label='Siglent-IP')
                            ui.input(label='Siglent-Port')

                #Server DIV(CARD)
                with ui.column():
                    with ui.card().style('margin: 36px;'):
                        with ui.label('Server'):
                            ui.input(label='run_it')
                            ui.input(label='how_many_times')
                            ui.input(label='modus')   

               #Electrolyse DIV(CARD)
                with ui.column():
                    with ui.card().style('margin: 36px;'):
                        with ui.label('Electrolyse'):
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




            #Aduino DIV(CARD)
            with ui.row():
                with ui.column():
                    with ui.card().style('margin: 36px; width: 1300px'):
                        with ui.label('Arduino'):
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
            
                
          




ui.run(native=True, tailwind=True, title='Yellow-SiC', favicon='https://raw.githubusercontent.com/YellowSiC/DesktopApplication/main/public/icon512.png')