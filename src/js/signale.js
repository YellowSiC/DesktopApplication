const { app, BrowserWindow, Menu, ipcMain } = require('electron');
const path = require('path');





  /* let menu = Menu.buildFromTemplate(menuTemplate);
  Menu.setApplicationMenu(menu);

  ipcMain.on('update-menu', (event, page) => {
    let menuTemplate = [
      {
        label: 'File',
        submenu: [
          {
            label: 'Open Page 1',
            enabled: page !== 'page1',
            click() {
              mainWindow.loadURL('src/pages/index.html');
            }
          },
          {
            label: 'Open Page 2',
            enabled: page !== 'page2',
            click() {
              mainWindow.loadURL('src/pages/main.html');
            }
          },
          {
            label: 'Quit',
            click() {
              app.quit();
            }
          }
        ]
      }
    ];

    menu = Menu.buildFromTemplate(menuTemplate);
    Menu.setApplicationMenu(menu);
  }); */





