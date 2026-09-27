# Easy-Quant
Simple tool that uses llama.cpp components to simplify the process of quantization. Aims to reduce time spent configuring the environment.

# Features
- Uses an x86_64 build of llama.cpp with basic AVX (Advanced Vector Extensions) support for compatibility across systems.
- Most quantization methods are supported (ranging from Q8_0 to Q1_0).
- Easy to understand instructions in the executable

# Instructions
1. Copy the file path of the model and paste it into the command prompt window (the file must be Float16, check the "Notices" section for more info).
2. The program will create a folder called "Output" in the directory it currently resides in. This will be the destination folder where the quantized file will be saved.
3. A few common choices for quantization will appear. You don't have to specifically choose ones on the list.
4. A notice will appear about the high resource usage. Type N to exit the program, and Y to continue.
5. The process will start and may take a lot of time depending on your hardware.
6. The file will be waiting in the output folder that was mentioned in step 2.

# Notices
- The code doesn't look professional under the hood since I'm a beginner (it will improve gradually, don't worry).
- This utility still requires the same amount of computation as the standard compiled binary during the quantization process.
- It can't use the '--allow-requantize' option like in standard llama-quantize (so Float16 GGUFs are only accepted by now).
- Imatrix quants like IQ4_XS or IQ1_M aren't usable yet.

This project bundles the pre-compiled 'llama-quantize' binary from the llama.cpp project.
llama.cpp is licensed under the MIT License.
Copyright (c) 2023-2026 Georgi Gerganov and the ggml authors.
