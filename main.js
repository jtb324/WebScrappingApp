const electron = require("electron");
const url = require("url");
const path = require("path");

const { app, BrowserWindow, Menu, screen } = electron;

let mainWindow;

app.on("ready", function () {
  const { width, height } = screen.getPrimaryDisplay().workAreaSize;

  mainWindow = new BrowserWindow({ width, height });

  mainWindow.loadURL(
    url.format({
      pathname: path.join(__dirname, "mainWindow.html"),
      protocol: "file",
      slashes: true,
    })
  );
});
