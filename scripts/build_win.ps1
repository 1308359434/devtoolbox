# Windows 本地构建脚本：PyInstaller onedir 便携版
# 用法：powershell -ExecutionPolicy Bypass -File scripts/build_win.ps1

$ErrorActionPreference = "Stop"
Set-Location (Split-Path -Parent $PSScriptRoot)

Write-Host "== 1/4 清理旧构建 =="
if (Test-Path dist) { Remove-Item -Recurse -Force dist }
if (Test-Path build) { Remove-Item -Recurse -Force build }

Write-Host "== 2/4 运行测试 =="
pytest
if ($LASTEXITCODE -ne 0) { throw "测试失败，停止构建" }

Write-Host "== 3/4 PyInstaller 打包（onedir，保持 Qt DLL 独立动态链接）=="
pyinstaller --noconfirm --clean --onedir --name DevToolBox `
  --exclude-module tkinter --exclude-module matplotlib --exclude-module numpy `
  src/devtoolbox/__main__.py
if ($LASTEXITCODE -ne 0) { throw "打包失败" }

Write-Host "== 4/4 生成便携 zip =="
Compress-Archive -Path dist/DevToolBox/* -DestinationPath DevToolBox-portable-win.zip -Force
Write-Host "完成：dist/DevToolBox/ 与 DevToolBox-portable-win.zip"
Write-Host "注意：LGPL 合规要求随包附带 THIRD_PARTY_NOTICES.md 与 LICENSE。"
Copy-Item LICENSE dist/DevToolBox/
Copy-Item THIRD_PARTY_NOTICES.md dist/DevToolBox/
