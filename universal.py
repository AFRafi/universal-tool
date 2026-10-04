import platform
import sys
import os

# Insert binaries folder into system path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "binaries"))

system = platform.system().lower()
is_android = "android" in os.popen("uname -o 2>/dev/null").read().lower() or "termux" in os.environ.get("PREFIX", "").lower()

try:
    if is_android:
        import universal_android_aarch64 as core
    elif system == "windows":
        import universal_windows_amd64 as core
    elif system == "linux":
        import universal_linux_x86_64 as core
    elif system == "darwin":
        import universal_darwin_arm64 as core
    else:
        print(f"[-] Unsupported OS: {system}")
        sys.exit(1)

    # Initialize routines
    core.check_force_update()
    core.authenticate()
    core.main()

except ImportError as e:
    print(f"[-] Compatible engine binary not found for your system: {e}")
    sys.exit(1)
