import tkinter as tk
import requests

class VirtualMachineGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("ToonToonEMU 0.X")

        self.vm_frame = tk.Frame(self)
        self.vm_frame.pack(side="top", fill="both", expand=True)

        self.vm_display = tk.Canvas(self.vm_frame, bg="gray")
        self.vm_display.pack(side="top", fill="both", expand=True)

        self.control_frame = tk.Frame(self)
        self.control_frame.pack(side="bottom", fill="x")

        self.power_button = tk.Button(self.control_frame, text="Power", command=self.power_vm)
        self.power_button.pack(side="left")

        self.reset_button = tk.Button(self.control_frame, text="Reset", command=self.reset_vm)
        self.reset_button.pack(side="left")

        self.suspend_button = tk.Button(self.control_frame, text="Suspend", command=self.suspend_vm)
        self.suspend_button.pack(side="left")

    def power_vm(self):
        pass

    def reset_vm(self):
        pass

    def suspend_vm(self):
        pass

if __name__ == "__main__":
    app = VirtualMachineGUI()
    app.mainloop()
