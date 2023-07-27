[app]

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.mydomain

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) Package dependencies
requirements = python3,kivy,kivymd

# (str) Application versioning (method 1)
version = 0.1

# (list) Permissions
android.permissions = INTERNET

# (str) Custom activity classname
android.entrypoint = org.kivy.android.PythonActivity

# (bool) Use a black background
android.blacklist_refs = unnecessary

# (list) Additional build options to append
android.build_options = android.permissions=INTERNET

# (list) Png optimization level (0-3)
# 0: no compression
# 1: fast (but low compression)
# 2: default
# 3: high compression (but slow)
android.pngcrush_opt_level = 3

# (bool) Create a source archive (.tar.gz) after building
source.build_dir = .buildozer/android/platform/build-armeabi-v7a
source.include_patterns = assets/*,*.py
source.exclude_patterns = tests/*,venv/*

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command outputs))
log_level = 2

# (str) Android SDK directory path
android.sdk_path = /home/user/android-sdk-linux

# (str) Android NDK directory path
android.ndk_path = /home/user/android-ndk-r20b

# (str) Python-for-android git clone directory (if empty, it will clone from github)
python-for-android.branch = master

# (str) Python-for-android git clone directory (if empty, it will clone from github)
python-for-android.url = https://github.com/kivy/python-for-android.git

# (list) List of custom p4a arguments
p4a.custom_args = --bootstrap=sdl2

# (str) Path to a custom distribution setup script
#p4a.local_recipes = myrecipes/

# (str) Filename of previous built application (for incremental builds)
#p4a.rebuild = myapp

# (bool) Rebuild everything, even if files have been seen before.
# Useful to reset dependencies or build flags used with p4a
#force_build = False

# (str) Path to application source code
# Must be defined if build.py is in a subdirectory
#source_dir = /path/to/your/code/

# (str) External storage directory path (e.g. '/sdcard')
android.storage_dir = /storage/emulated/0
