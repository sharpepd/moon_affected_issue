@echo off
setlocal
set SCRIPT_DIR=%~dp0
if not exist %SCRIPT_DIR%\em.exe powershell -Command "Invoke-WebRequest https://repo-manager.azure.zf-world.com/artifactory/AZP-001-platform-tools_generic_prod_local_azr/enviromate/enviromate-1.1.0-windows.exe -OutFile em.exe"
em setup -cf %~dp0em_config.yml
