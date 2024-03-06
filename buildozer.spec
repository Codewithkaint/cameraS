[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy==2.0.0, kivymd==0.104.2, opencv-python==4.5.3, pillow

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning
version = 0.1

# (str) Supported orientations
orientation = portrait

# (list) Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (bool) Enable AndroidX support
android.enable_androidx = True

# (int) Target Android API
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (bool) Skip trying to update the Android SDK
android.skip_update = False

# (bool) Automatically accept SDK license agreements
android.accept_sdk_license = True

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Permissions
android.permissions = CAMERA, WRITE_EXTERNAL_STORAGE

# (str) OUYA Console category
#android.ouya.category = GAME

# (bool) Allow backup
android.allow_backup = True

# (str) XML file for custom backup rules
# android.backup_rules =

# (bool) Copy library instead of making a libpymodules.so
# android.copy_libs = 1


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
