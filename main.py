import pdfplumber
import json
from tkinter import Tk, Button, Label, filedialog, messagebox


# PDF'den satır satır metin okuma fonksiyonu
def pdf_to_text_lines(pdf_path):
    text_lines = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_lines = page.extract_text().splitlines()  # Her sayfadaki metni satır satır ayır
            text_lines.extend(page_lines)  # Satırları birleştir
    return text_lines


# JSON dosyasına satır satır yazma fonksiyonu
def save_to_json_lines(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


# PDF dosyası seçme ve işleme
def select_pdf_file():
    pdf_file = filedialog.askopenfilename(
        title="PDF Dosyasını Seçin",
        filetypes=[("PDF Dosyaları", "*.pdf")]
    )
    if not pdf_file:
        messagebox.showwarning("Uyarı", "Lütfen bir PDF dosyası seçin!")
        return None
    return pdf_file


# JSON dosyasını kaydetme
def save_json_file(data):
    json_file = filedialog.asksaveasfilename(
        title="JSON Dosyasını Kaydet",
        defaultextension=".json",
        filetypes=[("JSON Dosyaları", "*.json")]
    )
    if not json_file:
        messagebox.showwarning("Uyarı", "Lütfen bir kayıt yeri seçin!")
        return None
    save_to_json_lines(data, json_file)
    messagebox.showinfo("Başarılı", f"JSON dosyası başarıyla kaydedildi: {json_file}")


# PDF'den JSON'a dönüştürme işlemini başlatma
def convert_pdf_to_json():
    pdf_path = select_pdf_file()
    if not pdf_path:
        return
    try:
        pdf_text_lines = pdf_to_text_lines(pdf_path)  # Satır satır metin al
        save_json_file({"pdf_content": pdf_text_lines})  # JSON'a kaydet
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")


# Tkinter arayüzü oluşturma
def create_app():
    root = Tk()
    root.title("PDF to JSON Converter")
    root.geometry("400x200")

    Label(root, text="PDF'den JSON'a Dönüştürücü", font=("Arial", 14)).pack(pady=10)

    Button(root, text="PDF Seç ve Dönüştür", font=("Arial", 12), command=convert_pdf_to_json).pack(pady=20)

    Button(root, text="Çıkış", font=("Arial", 12), command=root.quit).pack(pady=10)

    root.mainloop()


# Uygulamayı başlat
if __name__ == "__main__":
    create_app()
