SET loc=%~dp0OrthancWatcher.exe
schtasks /Create /SC DAILY /RU system /TN "Orthanc Watcher" /TR %loc% 