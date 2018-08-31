# Orthanc Watcher

A Python application that watches a local Orthanc-Dicom server. If any images older than a set time period are detected, they are deleted through the Orthanc REST API.

## Releases

Releases are available to download [here](https://github.com/brikwerk/orthanc-watcher/releases)

## Installation
1. Extract the contents of the Orthanc Watcher zip folder to your preferred installation directory.
2. Configure the provided "config.json" to your liking. Currently there is only one setting inside (DeleteDays), which sets the period until deletion.
3. Run the provided "install-task.bat" as administrator. Please review the installation script before running it to ensure integrity and legitimacy. This script adds "OrthancWatcher.exe" to the Windows task scheduler so the exe may run on a daily basis. The user does not have to be logged in for this.