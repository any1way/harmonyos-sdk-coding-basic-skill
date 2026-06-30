用途：本技能为harmonyos-sdk-coding-basic-skill中的本地知识检索部件，用于鸿蒙APP开发者使用AI Agent编程时候的查询指南和API参考知识。本技能非HarmonyOS SDK场景化技能，场景化技能参见鸿蒙SDK相关技能文档。
用法：把整个目录解压到Agent配置的skills目录下；

## Windows 用户重要提示：长路径支持

本仓库 `references/` 目录含 12000+ 篇鸿蒙官方文档，部分中文 FAQ 问句和 Code Linter 规则目录名较长。克隆到 Windows 深目录（如 `C:\Users\<user>\Documents\projects\<team>\...`）时，完整路径可能超过 Windows 默认 MAX_PATH=260 限制，导致 `git checkout` 报 "Filename too long" 错误。

**克隆前请启用 Git 长路径支持**（任选一种）：

**方式 1：全局配置（推荐，一次配置永久生效）**
```powershell
git config --global core.longpaths true
git clone https://github.com/any1way/harmonyos-sdk-coding-basic-skill.git
```

**方式 2：克隆后单独配置**
```powershell
git clone https://github.com/any1way/harmonyos-sdk-coding-basic-skill.git
cd harmonyos-sdk-coding-basic-skill
git config core.longpaths true
git checkout .
```

**方式 3：启用 Windows 系统级长路径支持**（需管理员权限）
```powershell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" `
  -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```
启用后重启 Git Bash/PowerShell 即可，无需 `core.longpaths` 配置。

> 说明：长路径对 macOS/Linux 无影响，无需任何配置。
