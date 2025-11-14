import sys
import os

class Payload:
    @staticmethod
    def find_payloads():
        if getattr(sys, 'frozen', False):
            script_dir = os.path.dirname(sys.executable)
        else:
            script_dir = os.path.dirname(os.path.abspath(__file__))

        project_root = os.path.dirname(script_dir)
        payload_dir = os.path.join(project_root, "..", "public", "payload")

        payloads = []
        if os.path.exists(payload_dir) and os.path.isdir(payload_dir):
            for file in os.listdir(payload_dir):
                if file.endswith('.txt'):
                    payloads.append(os.path.join(payload_dir, file))
        return payloads