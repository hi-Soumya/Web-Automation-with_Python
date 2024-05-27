from bs4 import BeautifulSoup
import requests
import tkinter as tktr
from tkinter import Text, messagebox

def download_pdf():
    try:
        pdf_name = input_text.get("1.0", "end-1c").strip()
        if not pdf_name:
            messagebox.showwarning("Input Required", "Please enter a PDF file name or a part of the name.")
            return
        
        url = requests.get('https://www.bluecrossma.org/myblue/fast-forms')
        soup = BeautifulSoup(url.text, "html.parser")

        links = soup.find_all('a', title=True)
        found = False
        for link in links:
            if('.pdf' in link.get('href', []) and pdf_name.lower() in link.get('title', '').lower()):
                response = requests.get(link.get('href'))
                pdf_filename = pdf_name + ".pdf"
                with open(pdf_filename, 'wb') as pdf:
                    pdf.write(response.content)
                found = True
                messagebox.showinfo("Success", f"PDF file '{pdf_filename}' downloaded successfully.")
                break
        
        if not found:
            messagebox.showinfo("Not Found", f"No PDF file found with the name- '{pdf_name}'.")

    except Exception as excep:
        messagebox.showerror("Error", f"An error occurred: {excep}")
        return None

root = tktr.Tk()
root.title("Provide PDF file name in the BOX Below")

input_text = Text(root, width=50, height=20, wrap=tktr.WORD)
input_text.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

generate_button = tktr.Button(root, text="Download PDF", command=download_pdf)
generate_button.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

root.columnconfigure(0, weight=5)
root.rowconfigure(0, weight=5)

root.mainloop()
