from pyautogui import screenshot
import tkinter as tk

class OverlayWindow:
    def __init__(self):
        # Create a transparent fullscreen window
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        
        # Make transparent
        self.root.wait_visibility(self.root)
        self.root.attributes("-alpha", 0.0)
        
        self.root.bind("<Button-1>", self.on_click)
        self.root.mainloop()

    def on_click(self, event):
        colorpicker = ColorPicker(event.x, event.y)
        colorpicker.get_color(output_to_terminal=True)
        self.close()

    def close(self, event=None):
        self.root.destroy()


class ColorPicker:
    def __init__(self, x: int, y: int) -> None:
        self.screen_pixel = screenshot(region=(x, y, 1, 1)) # 1x1 screenshot at mouse pos

    def get_color(self, output_to_terminal=False) -> tuple[tuple, str]:
        color_rgb = self._get_rgb()
        color_hex = self._get_hex(color_rgb)

        if output_to_terminal:
            print(f"{color_rgb} | {color_hex}")

        return (color_rgb, color_hex)        
    
    def _get_rgb(self) -> tuple:
        return self.screen_pixel.getpixel((0, 0))
    
    def _get_hex(self, rgb: tuple) -> str:
        r, g, b = rgb
        return f"#{r:02x}{g:02x}{b:02x}"


if __name__ == "__main__":
    OverlayWindow()
