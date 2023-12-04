from tkinter import *
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox
#Module Used : pip install googletrans==3.1.0a0

root = Tk()
root.title("Google Translator App")
root.geometry("630x410+400+100")

def translate():
    lang_1 = text_entry1.get('1.0','end-1c')
    cl = choose_language.get()

    if lang_1 == '':
        messagebox.showerror('Language Translator',message="Enter the text to Translate!")
    else:
        text_entry2.delete(1.0,'end')
        translator = Translator()
        output = translator.translate(lang_1,dest=cl)
        text_entry2.insert('end',output.text)
def clear():
    text_entry1.delete(1.0, 'end')
    text_entry2.delete(1.0, 'end')

a= StringVar()

frame1=Frame(root, width=630, height = 410, relief="ridge", borderwidth="5", bg="#F7DC6F")
frame1.place(x=0,y=0)

lbl1=Label(root, text="Language Translator", font=('Halvetica 20 bold'),fg ="black", bg="#F7DC6F")
lbl1.pack(pady=10)

auto_select = ttk.Combobox(frame1, width=27, textvariable= a, state='randomly', font=('verdana', 10 , 'bold'))
auto_select['values']=(
                        'Auto Select',
                      )
auto_select.place(x= 25,y= 60)
auto_select.current(0)

l= StringVar()
choose_language = ttk.Combobox(frame1, width=27, textvariable= l, state='randomly', font=('verdana', 10 , 'bold'))
choose_language['values']=(
                            'Afrikaans',	
                            'Albanian',
                            'Amharic',	
                            'Arabic',	
                            'Armenian',
                            'Aymara',	
                            'Azerbaijani',
                            'Bambara',	
                            'Basque',	
                            'Belarusian',
                            'Bengali',
                            'Bhojpuri',	
                            'Bosnian',	
                            'Bulgarian',	
                            'Catalan',	
                            'Cebuano',	
                            'Chinese',
                            'Chinese',
                            'Corsican',	
                            'Croatian',	
                            'Czech',	
                            'Danish',	
                            'Dhivehi',	
                            'Dogri',	
                            'Dutch',	
                            'English',	
                            'Esperanto',	
                            'Estonian',	
                            'Ewe',
                            'Filipino (Tagalog)',	
                            'Finnish',	
                            'French',	
                            'Frisian',	
                            'Galician',	
                            'Georgian',	
                            'German',	
                            'Greek',	
                            'Guarani',	
                            'Gujarati',
                            'Haitian Creole',	
                            'Hausa',
                            'Hawaiian',
                            'Hebrew',	
                            'Hindi',	
                            'Hmong',	
                            'Hungarian',	
                            'Icelandic',	
                            'Igbo',	
                            'Ilocano',	
                            'Indonesian',
                            'Irish',
                            'Italian',	
                            'Japanese',
                            'Javanese',
                            'Kannada',	
                            'Kazakh',	
                            'Khmer',	
                            'Kinyarwanda',
                            'Konkani',	
                            'Korean',	
                            'Krio',	
                            'Kurdish',	
                            'Kurdish (Sorani)',
                            'Kyrgyz',	
                            'Lao',
                            'Latin',	
                            'Latvian',	
                            'Lingala',	
                            'Lithuanian',
                            'Luganda',	
                            'Luxembourgish',
                            'Macedonian',	
                            'Maithili',	
                            'Malagasy',	
                            'Malay',	
                            'Malayalam',
                            'Maltese',	
                            'Maori',	
                            'Marathi',	
                            'Meiteilon (Manipuri)',
                            'Mizo',	
                            'Mongolian',
                            'Myanmar (Burmese)',
                            'Nepali',	
                            'Norwegian',
                            'Nyanja (Chichewa)',
                            'Odia (Oriya)',	
                            'Oromo',	
                            'Pashto',	
                            'Persian',	
                            'Polish',	
                            'Portuguese (Portugal, Brazil)',
                            'Punjabi',	
                            'Quechua',	
                            'Romanian',	
                            'Russian',	
                            'Samoan',	
                            'Sanskrit',	
                            'Scots Gaelic',	
                            'Sepedi',	
                            'Serbian',	
                            'Sesotho',	
                            'Shona',	
                            'Sindhi',	
                            'Sinhala (Sinhalese)',	
                            'Slovak',	
                            'Slovenian',	
                            'Somali',	
                            'Spanish',	
                            'Sundanese',
                            'Swahili',	
                            'Swedish',	
                            'Tagalog (Filipino)',
                            'Tajik',	
                            'Tamil',	
                            'Tatar',	
                            'Telugu',	
                            'Thai',	
                            'Tigrinya',
                            'Tsonga',	
                            'Turkish',	
                            'Twi (Akan)',
                            'Ukrainian',
                            'Urdu',	
                            'Uyghur',	
                            'Uzbek',
                            'Vietnamese',
                            'Welsh',	
                            'Xhosa',	
                            'Yiddish',	
                            'Yoruba',	
                            'Zulu',
                          )
choose_language.place(x=320, y=60)
choose_language.current(0)
text_entry1=Text(frame1, width=20, height=7, borderwidth=5, relief="ridge", font=('verdana', 15))
text_entry1.place(x=20, y=100)

text_entry2=Text(frame1, width=20, height=7, borderwidth=5, relief="ridge", font=('verdana', 15))
text_entry2.place(x=320, y=100)

btn1=Button(frame1,command=translate, text="Translate", relief='raised', borderwidth=2, font=('verdana', 12, 'bold'), bg="#248aa2", fg="white", cursor="hand2")
btn1.place(x=193, y=300)

btn2=Button(frame1, command=clear, text="Clear", relief='raised', borderwidth=2, font=('verdana', 12, 'bold'), bg="#248aa2", fg="white", cursor="hand2")
btn2.place(x=320, y=300)

root.mainloop()
