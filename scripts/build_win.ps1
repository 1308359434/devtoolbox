# Windows 本地构建脚本：PyInstaller onefile 单文件版（双击即用，无需解压）
# 用法：powershell -ExecutionPolicy Bypass -File scripts/build_win.ps1

$ErrorActionPreference = "Stop"
Set-Location (Split-Path -Parent $PSScriptRoot)

Write-Host "== 1/4 清理旧构建 =="
if (Test-Path dist) { Remove-Item -Recurse -Force dist }
if (Test-Path build) { Remove-Item -Recurse -Force build }

Write-Host "== 2/4 运行测试 =="
pytest
if ($LASTEXITCODE -ne 0) { throw "测试失败，停止构建" }

Write-Host "== 3/4 PyInstaller 打包（onefile，单文件双击即用）=="
pyinstaller --noconfirm --clean --onefile --name DevToolBox `
  --exclude-module tkinter --exclude-module matplotlib --exclude-module numpy `
  --exclude-module PySide6.WebEngine --exclude-module PySide6.QtWebEngineCore `
  src/devtoolbox/__main__.py
if ($LASTEXITCODE -ne 0) { throw "打包失败" }

Write-Host "== 4/4 生成发布 zip（含单文件 exe 与许可声明）=="
New-Item -ItemType Directory -Force -Path release | Out-Null
Copy-Item dist/DevToolBox.exe release/
Copy-Item LICENSE release/
Copy-Item THIRD_PARTY_NOTICES.md release/
Compress-Archive -Path release/* -DestinationPath DevToolBox-portable-win.zip -Force
Write-Host "完成：dist/DevToolBox.exe（可直接双击）与 DevToolBox-portable-win.zip"
