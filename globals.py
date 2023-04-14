from typing import List, Dict, Any
from enum import Enum

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