import os
import gzip

def AddSampleNameVcf(vcfFile, outputFile, baseInputDir):
    # Obtém o caminho relativo em relação ao diretório base
    relativePath = os.path.relpath(vcfFile, baseInputDir)
    sampleName = relativePath.replace(os.sep, "/")  # Substitui separadores de diretório por "/"

    # Verifica se o arquivo é .vcf ou .vcf.gz
    openFunc = gzip.open if vcfFile.endswith(".gz") else open
    mode = "rt" if vcfFile.endswith(".gz") else "r"

    with openFunc(vcfFile, mode) as infile, open(outputFile, "w") as outfile:
        for line in infile:
            if line.startswith("#CHROM"):
                # Adiciona o caminho completo como nome da amostra na linha de cabeçalho
                line = line.strip() + f"\t{sampleName}\n"
            outfile.write(line)

    print(f"Amostra '{sampleName}' processada e salva em '{outputFile}'.")

def processVcfFile(inputDir):
    outputBaseDir = os.path.join(inputDir, "renomeados")

    for root, _, files in os.walk(inputDir):
        for file in files:
            if file.endswith(".vcf") or file.endswith(".vcf.gz"):
                vcfFile = os.path.join(root, file)
                
                # Cria a estrutura de saída equivalente dentro da pasta 'renomeados'
                relativePath = os.path.relpath(root, inputDir)
                outputDir = os.path.join(outputBaseDir, relativePath)
                
                if not os.path.exists(outputDir):
                    os.makedirs(outputDir)
                
                outputFile = os.path.join(outputDir, file)
                AddSampleNameVcf(vcfFile, outputFile, inputDir)

    print(f"\nTodos os arquivos foram processados e salvos em '{outputBaseDir}'.")

# Configuração: diretório de entrada
inputDirectory = "C:/Users/aless/Downloads/GenPop-Pipeline/analise_bill"  

# Execução
processVcfFile(inputDirectory)




