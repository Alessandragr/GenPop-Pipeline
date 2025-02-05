import os
import gzip

def add_sample_tag_to_vcf(vcf_file, output_file, base_input_dir):
    # Obtém o caminho relativo em relação ao diretório base
    relative_path = os.path.relpath(vcf_file, base_input_dir)
    sample_name = relative_path.replace(os.sep, "/")  # Substitui separadores de diretório por "/"

    # Verifica se o arquivo é .vcf ou .vcf.gz
    open_func = gzip.open if vcf_file.endswith(".gz") else open
    mode = "rt" if vcf_file.endswith(".gz") else "r"

    with open_func(vcf_file, mode) as infile, open(output_file, "w") as outfile:
        for line in infile:
            if line.startswith("#CHROM"):
                # Adiciona o caminho completo como nome da amostra na linha de cabeçalho
                line = line.strip() + f"\t{sample_name}\n"
            outfile.write(line)

    print(f"Amostra '{sample_name}' processada e salva em '{output_file}'.")

def process_vcf_files(input_dir):
    output_base_dir = os.path.join(input_dir, "renomeados")

    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".vcf") or file.endswith(".vcf.gz"):
                vcf_file = os.path.join(root, file)
                
                # Cria a estrutura de saída equivalente dentro da pasta 'renomeados'
                relative_path = os.path.relpath(root, input_dir)
                output_dir = os.path.join(output_base_dir, relative_path)
                
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                
                output_file = os.path.join(output_dir, file)
                add_sample_tag_to_vcf(vcf_file, output_file, input_dir)

    print(f"Todos os arquivos foram processados e salvos em '{output_base_dir}'.")

# Configuração: diretório de entrada
input_directory = "caminho/para/sua/pasta/analise"  # Altere para o caminho correto

# Executa o script
process_vcf_files(input_directory)
