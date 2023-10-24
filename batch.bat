@echo off
chcp 1252 > Nul

:: Especifique aqui o caminho para on rar.exe:
set "Rar=%programfiles%\winrar\rar.exe"

:: Especifique aqui onde estão os arquivos que deverão ser incluidos no arquivo sfx:
set Fonte=%userprofile%\desktop\Teste\*

:: Especifique aqui o caminho para onde os arquivos devem ser extraídos:
set CExtracao=%Programfiles%\TesteCCleaner

:: Especifique aqui o arquivo de instalação:
set CInstalacao=%userprofile%\desktop\Teste\ccsetup566.exe

:: Especifique o arquivo sfx que devera ser criado:
set SFX=%userprofile%\desktop\setup.exe

:: Especifique aqui o icone do Arquivo SFX:
set Icone=%userprofile%\desktop\Teste\drinking.ico

echo Path=%CExtracao%>"%temp%\opcoes.txt"
echo Silent=^1>>"%temp%\opcoes.txt"
echo Setup=%CInstalacao%>>%temp%\opcoes.txt

"%Rar%" a -c -cfg- -ep1 -s -r -sfx -iicon"%Icone%" -y "-z%TEMP%\opcoes.txt" "%SFX%" "%Fonte%"

del "%temp%\opcoes.txt"