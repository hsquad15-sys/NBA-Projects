import tkinter as tk
from tkinter import scrolledtext
from Yahoo_Grab import sites, grab_headlines

def run_gui():
    def on_grab():
        output_box.config(state='normal')
        output_box.delete(1.0, tk.END)
        for site in sites:
            # Bold website name using Tkinter tags
            output_box.insert(tk.END, f"\nTop headlines from ")
            start = output_box.index(tk.END)
            output_box.insert(tk.END, f"{site['name']}", 'bold')
            output_box.insert(tk.END, ":\n")
            try:
                headlines = grab_headlines(site)
                for i, h in enumerate(headlines):
                    output_box.insert(tk.END, f"  • {h['title']}\n    {h['link']}\n")
            except Exception as e:
                output_box.insert(tk.END, f"Error fetching {site['name']}: {e}\n")
        output_box.config(state='disabled')

    root = tk.Tk()
    root.title("Headline Grabber")
    root.geometry("700x500")

    grab_btn = tk.Button(root, text="Grab Headlines", command=on_grab, font=("Arial", 14))
    grab_btn.pack(pady=10)

    output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
    output_box.pack(expand=True, fill='both', padx=10, pady=10)
    output_box.tag_configure('bold', font=("Arial", 12, "bold"))
    output_box.config(state='disabled')

    root.mainloop()

if __name__ == "__main__":
    run_gui()
