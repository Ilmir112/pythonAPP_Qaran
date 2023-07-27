[app]

# (str) Title of your application
title = KivyMD App

# (str) Package name
package.name = kivymdapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.kivymd

# (str) Source code directory
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,ttf,txt

# (list) Dependencies to include
requirements = kivy==2.0.0, kivymd, requests

# (str) Application version
version = 0.1

# (str) Application icon
icon.filename = icon.png

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

# (list) Services to declare
services =

# (str) The version of Android API to use
android.api = 29

# (str) The version of Android NDK to use
android.ndk = 19c

# (str) The version of Python for android to use
python-for-android.version = 0.9.0

# (str) Comma separated list of Java packages and classes to add to the project
android.add_jars =

# (str) Comma separated list of Java .jar files to add to the libs/ directory
android.add_libs =

# (str) Deprecated, use android.add_libs instead.
android.add_external_libs =

# (str) Gradle dependencies to add (eg. 'implementation com.android.support:appcompat-v7:27.1.1')
android.gradle_dependencies =

# (list) Add an other custom buildozer command (append in the command line)
android.additional_commands =

# (bool) If you need specific Android uses-library
android.uses_library =

# (str) Name of the application project
android.project_title = KivyMD App

# (str) Package name
android.package_name = org.kivymd

# (str) Gradle filename (Yaml format)
android.gradle_filename =

# (list) source patterns to exclude
exclude_patterns = *.pyc, *.pyo, __pycache__, .git, .svn, CVS, .DS_Store, buildozer.spec, *.egg-info, .idea

# (list) Application requirements
requirements = python3,kivy==2.0.0, kivymd, requests

# (str) Presplash of the application
presplash.filename = presplash.png

# (str) Icon of the application
icon.filename = icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (bool) Turn on the debug mode
android.debug = False

# (bool) Logcat output
logcat_filters = *:S python:D

