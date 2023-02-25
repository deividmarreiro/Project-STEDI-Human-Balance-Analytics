#!/bin/bash

# Especifica o diretório de entrada e o diretório de saída
input_dir="./malformed"
output_dir="./trusted"

# Loop através de cada subdiretório
for subdir in "customers" "accelerometer" "step_trainer"; do
    subdir_path="$input_dir/$subdir"
    output_subdir_path="$output_dir/$subdir"
    
    # Cria o subdiretório de saída se ele não existir
    mkdir -p "$output_subdir_path"
        
    # Loop através de cada arquivo .json no subdiretório
    for json_file in "$subdir_path"/*.json; do
        
        # Cria o arquivo de saída
        output_file="$output_subdir_path/$(basename "$json_file")"
        touch "$output_file"
        
        # Ler o arquivo .json e converter cada objeto JSON em uma linha separada
        while IFS= read -r obj || [[ -n "$obj" ]]; do
            echo "$obj" >> "$output_file"
        done < <(jq -c '.' "$json_file")
    done
done
