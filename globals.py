from typing import List, Dict, Any




#[siglent]
sig_ip: str = '169.254.1.1'
port: int = 5025

#[data]
path: str = ''

#[server]
#or "server" or "alone"
run_it: str = 'alone'
how_many_times = 3
#modus test or electrolyse
modus = 'electrolyse'

#[electrolyse]
file_name: str = None
probe_nr:str = 'L0001'
comments: str = 'TestMessung_KOH25'
u_min: int = 2
u_max: int = 3
delta_u: float = 0.1
t_meas: int = 1000
t_wait: int =8000

#[Arduino]
CONNECTED: int = 0
VOLTAGE: float = 1.2
BAUDRATE: int = 115200
PORT: str = '/dev/ttyUSB0'
BYTESIZE: int = 8
PARITY: str = 'N'
STOPBITS: str = 1
TIMEOUT: str = 1
RES: float = 0.125
UPPER_LIMIT: float = 1.5