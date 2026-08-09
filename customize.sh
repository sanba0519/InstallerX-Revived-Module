# This ensures Magisk extracts the module files automatically
SKIPUNZIP=0

# UI print command to show status in the flashing console
ui_print "- Installing PackageInstaller Replacement..."

# Define permissions
# Syntax: set_perm_recursive <directory> <owner> <group> <dir_permission> <file_permission>
# 0 0 corresponds to root:root
# 0755 is rwxr-xr-x (required for directories)
# 0644 is rw-r--r-- (required for system apks)

ui_print "- Setting permissions..."
set_perm_recursive "$MODPATH/system" 0 0 0755 0644