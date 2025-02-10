# Merge dos arquivos com o BCFTools utilizando o WSL

# Instalar o WSL, caso não tenha

# sudo apt update atualizar o sistema

# sudo apt install bcftools Instalação do BCFTools


# Passo 1 => Ordenar os arquivos por ordem de cromossomos ou posição :
bcftools sort -o S6-P90-6.trimed1000.sv_sniffles.vcf P90-6.trimed1000.sv_sniffles.vcf

# Passo 2 => Mover todos os arquivos para uma nova pasta para facilitar o uso :

# Passo 3 => Zipar os arquivos :
bgzip S*.vcf

# Passo 4 => Instalar o tabix e criar a versão bix
sudo apt install tabix
tabix -p vcf S*.vcf.gz

# Passo 5 => Fazer o merge dos arquivos. Diferença entre merge e concat :
bcftools merge -m id -O b -o merged.vcf S6-P90-6.trimed1000.sv_sniffles.vcf.gz 
    S7-P90-7.trimed1000.sv_sniffles.vcf.gz 
    S8-P90-8.trimed1000.sv_sniffles.vcf.gz 
    S9-P90-9.trimed1000.sv_sniffles.vcf.gz 
    S10-P90-10.trimed1000.sv_sniffles.vcf.gz 