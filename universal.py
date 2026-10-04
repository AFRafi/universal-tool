import platform
import sys
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
system = platform.system().lower()
machine = platform.machine().lower()

# Comprehensive Android detection (Termux, Pydroid 3, QPython, Generic Android)
is_android = (
    hasattr(sys, "getandroidapilevel")
    or "android" in os.environ.get("ANDROID_ROOT", "").lower()
    or "termux" in os.environ.get("PREFIX", "").lower()
    or "pydroid" in sys.executable.lower()
    or "android" in platform.platform().lower()
)

target_folder = None
if is_android:
    target_folder = "android_aarch64"
elif system == "linux":
    target_folder = "linux_x86_64"
elif system == "windows":
    target_folder = "windows_amd64"
elif system == "darwin":
    target_folder = "darwin_arm64"
else:
    print(f"[-] Unsupported OS: {system}")
    sys.exit(1)

binary_path = os.path.join(base_dir, "binaries", target_folder)
sys.path.insert(0, binary_path)

try:
    import universal_core as core
    core.check_force_update()
    core.authenticate()
    core.main()
except ImportError as e:
    print(f"[-] Compatible engine binary not found for your system: {e}")
    sys.exit(1)
