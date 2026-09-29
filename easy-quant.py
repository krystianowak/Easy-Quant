import os
import time

print("   ================================================")
print("")
print("       Easy Quant, a user friendly wrapper for")
print("             llama.cpp's llama-quantize.")
print("")
print("                Bare AVX support")
print("")
print("   ================================================")

time.sleep(1)

print("")

GGUF_Path = input("Enter the absolute file path for your GGUF file: ")
print("")
Output_Dir = os.makedirs("output", exist_ok=True)

print("   ================================================")
print("")
print("       Enter the quantization technique to use.")
print("")
print("                   Popular choices:")
print("")
print("   ================================================")
print("")
print("1. Q8_0, ~50% smaller file size compared to Float16,")
print("8-8.5 BPW (bits per weight), highest quality on the list.")
print("")
print("2. Q6_K, ~60% smaller file size compared to Float16,")
print("6.6 BPW, quality almost indistinguishable from Q8.")
print("")
print("3. Q5_K_M, ~65% smaller file size compared to Float16,")
print("~5.5 BPW, minimal loss (around 0.5-1%) in tests compared to Q8.")
print("")
print("4. Q4_K_M, 70-75% smaller file size compared to Float16,")
print("~4.65 BPW, still goes strong in shorter context windows, slight degradation starts to occur in longer context windows.")
print("")
print("5. Q3_K_M, ~76% smaller file size compared to Float16,")
print("~3.6 BPW, same case as Q4_K_M when it comes to quality.")
print("")
print("The '--allow-requantize' flag is on by default and could produce unexpected results, but enables further quantization")
print("(going from Q8_0 to Q4_K_M for example instead of always having to start from FP16).")
print("")
Quant_Choice = input("Type the specific quant name. Other ones not on the list are also valid choices (Imatrix quants like IQ4_XS or IQ2_XS aren't supported): ")

print("")

Confirmation = str(input("This process may take a big toll on system resources (can use tens of gigabytes of RAM and a lot of CPU processing power). Do you want to continue? (Y/N): "))

print("")

Output_Path = f"output/model-{Quant_Choice}.gguf"

if Confirmation == "N":

    exit()

elif Confirmation == "Y" or "y":
    
    print("Those are the options you've selected: ")
    print("")
    print(f"Your GGUF file's path: {GGUF_Path}")
    print("")
    print(f"Your quant choice: {Quant_Choice}")
    print("")
    print("The quantized file will be ready in the folder named output at the root of this directory.")
    print("")
    print("Starting llama-quantize... ")
    print("")

    args = str("--allow-requantize"), str(GGUF_Path), str(Output_Path), str(Quant_Choice)

    quanttool_dir = os.path.dirname(os.path.abspath(__file__))
    llama_path = os.path.join(quanttool_dir, "llama-quantize", "llama-quantize.exe")
    
    os.startfile(llama_path, arguments=" ".join(args)) 

    print("Quantizing...")

    time.sleep(5)