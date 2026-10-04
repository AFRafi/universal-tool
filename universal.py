import platform
import sys
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
system = platform.system().lower()
is_android = "android" in os.popen("uname -o 2>/dev/null").read().lower() or "termux" in os.environ.get("PREFIX", "").lower()

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
