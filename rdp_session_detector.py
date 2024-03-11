import os
import subprocess

def is_user_remoting():
    """
    Checks if the user is currently logged in via Remote Desktop.
    Returns True if a remote session is detected, False otherwise.
    """
    try:
        # Query session information using the qwinsta command
        output = subprocess.check_output('qwinsta', stderr=subprocess.STDOUT, text=True)

        # Look for lines that indicate an active remote session
        for line in output.splitlines():
            if "rdp-tcp#" in line.lower() and "active" in line.lower():
                return True
        return False
    except Exception as e:
        print(f"Error checking remote desktop session: {e}")
        return False

if __name__ == "__main__":
    # Example usage
    if is_user_remoting():
        print("A user is currently remoting in.")
    else:
        print("No active remote desktop sessions.")
