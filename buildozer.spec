[app]

# 应用在手机桌面上显示的名字
title = 计算机

# 应用的内部包名（建议保持 com.你的名字.应用名 的格式，请勿包含中文或特殊字符）
package.name = mycalculator
package.domain = org.example

# 项目源码目录
source.dir = .
# 项目包含的文件扩展名
source.include_exts = py,png,jpg,kv,atlas

# 应用版本
version = 0.1

# 打包时需要包含的Python库（核心依赖是kivy）
requirements = python3,kivy

# 安卓相关配置
android.permissions = INTERNET
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30

# 日志级别，打包失败时可开启以查看详细错误
# log_level = 2

# 应用图标（可选，需要一张png图片放在项目文件夹里）
# icon.filename = %(source.dir)s/icon.png

# 预编译一些C库以加快启动速度
presplash.filename = %(source.dir)s/presplash.png