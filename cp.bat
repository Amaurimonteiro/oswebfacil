@echo off
chcp 1252 > Nul

copy *.png c:\os_system\dist\os
copy *.ui c:\os_system\dist\os
copy *.ico c:\os_system\dist\os


:: Especifique aqui o caminho para on rar.exe:
set "Rar=%programfiles%\winrar\rar.exe"

:: Especifique aqui onde estão os arquivos que deverão ser incluidos no arquivo sfx:
set Fonte=C:\os_system\dist\os\*

:: Especifique aqui o caminho para onde os arquivos devem ser extraídos:
set CExtracao=c:\oswebfacil\

:: Especifique aqui o arquivo de instalação:
set CInstalacao=c:\oswebfacil\os.exe

:: Especifique o arquivo sfx que devera ser criado:
set SFX=C:\Users\Public\Desktop\oswebfacil_install.exe

:: Especifique aqui o icone do Arquivo SFX:
set Icone=C:\os_system\logo_oswebfacil.ico

echo Path=%CExtracao%>"%temp%\opcoes.txt"
echo Silent=^1>>"%temp%\opcoes.txt"
echo Setup=%CInstalacao%>>%temp%\opcoes.txt

"%Rar%" a -c -cfg- -ep1 -s -r -sfx -iicon"%Icone%" -y "-z%TEMP%\opcoes.txt" "%SFX%" "%Fonte%"

del "%temp%\opcoes.txt"





:: Especifique aqui o caminho para on rar.exe:
set "Rar=%programfiles%\winrar\rar.exe"

:: Especifique aqui onde estão os arquivos que deverão ser incluidos no arquivo sfx:
set Fonte=C:\Users\Public\Desktop\oswebfacil*.*

:: Especifique aqui o caminho para onde os arquivos devem ser extraídos:
set CExtracao=C:\Users\Public\Desktop\

:: Especifique aqui o arquivo de instalação:
set CInstalacao=C:\Users\Public\Desktop\oswebfacil

:: Especifique o arquivo sfx que devera ser criado:
set SFX=c:\Users\Administrador\desktop\oswebfacil_inst.exe
set SFX=C:\Users\Public\Desktop\oswebfacil_install.exe

:: Especifique aqui o icone do Arquivo SFX:
set Icone=C:\os_system\logo_oswebfacil.ico

echo Path=%CExtracao%>"%temp%\opcoes.txt"
echo Silent=^1>>"%temp%\opcoes.txt"
echo Setup=%CInstalacao%>>%temp%\opcoes.txt

"%Rar%" a -c -cfg- -ep1 -s -r -sfx -iicon"%Icone%" -y "-z%TEMP%\opcoes.txt" "%SFX%" "%Fonte%"

del "%temp%\opcoes.txt"




