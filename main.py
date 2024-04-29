import form_main_designer as designer
import form_main as form
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def main():
    print("program start")
    form.initialize()
    designer.Main.mainloop()

if __name__ == "__main__":
    main()
