import os
import time

print("================================================")
print("")
print("  Easy Quant, a more user friendly wrapper for")
print("          llama.cpp's llama-quantize")
print("")
print("")
print("    CPU-only compiled with AVX support for")
print("       max compatibility across systems")
print("================================================")

time.sleep(0.4)

print("")

GGUF_Path = input("Enter the absolute file path for your Float16 GGUF file: ")
print("")
Output_Dir = os.mkdir("output")

print("Enter the quantization technique to use")
print("")
print("         Popular choices:")
print("")
print("1. Q8_0, ~50% smaller file size compared to Float16, 8-8.5 BPW (bits per weight), highest quality on the list)")
print("")
print("2. Q6_K, ~60% smaller file size compared to Float16, 6.6 BPW, quality almost indistinguishable from Q8)")
print("")
print("3. Q5_K_M, ~65% smaller file size compared to Float16, ~5.5 BPW, minimal loss (around 0.5-1%) in tests compared to Q8")
print("")
print("4. Q4_K_M, 70-75% smaller file size compared to Float16, ~4.65 BPW, still goes strong in shorter context windows, slight degradation starts to occur in longer context windows")
print("")
print("5. Q3_K_M, ~76% smaller file size compared to Float16, ~3.6 BPW, same case as Q4_K_M")
print("")

Quant_Choice = input("Type the specific quant name. Other ones not on the list are also valid choices (Imatrix quants like IQ4_XS or IQ2_XS aren't supported): ")

print("")

Confirmation = str(input("This process takes a big toll on system resources (can use tens of gigabytes of RAM and a lot of CPU processing power). Do you want to continue? (Y/N): "))

print("")

Output_Path = f"output/model-{Quant_Choice}.gguf"

if Confirmation == "N":

    exit()

elif Confirmation == "Y" or "y":
    
    print("Those are the options you've selected: ")
    print("")
    print(f"Your Float16 GGUF file's path: {GGUF_Path}")
    print("")
    print(f"Your quant choice: {Quant_Choice}")
    print("")
    print("The quantized file will be ready in the folder named output at the root of this directory")
    print("")
    print("Starting the quantization process.. ")
    print("")

    args = str(GGUF_Path), str(Output_Path), str(Quant_Choice)

    quanttool_dir = os.path.dirname(os.path.abspath(__file__))
    llama_path = os.path.join(quanttool_dir, "llama-quantize", "llama-quantize.exe")
    
    os.startfile(llama_path, arguments=" ".join(args)) 