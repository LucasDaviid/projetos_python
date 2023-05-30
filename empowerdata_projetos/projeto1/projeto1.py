# Projeto 1 - Gerador de PDF
# Utilizamos a library  fpdf2 2.7.4

from fpdf import FPDF

# Dados
descricao_projeto = input('Digite a descrição do projeto: ')
horas = input('Digite o total de horas estimadas: ')
valor = input('Digite o valor da hora trabalhada: ')
prazo_projeto = input('Digite o prazo estimado: ')

hora_valor = float(valor) 
hora_estimada = int(horas)

total = hora_estimada * hora_valor
total_str = str(total)

# Gerador de pdf
pdf = FPDF()

pdf.add_page() # Aqui criamos uma pagina de PDF
pdf.set_font('helvetica', size=14) # Seleção da fonte e tamanho
pdf.image('rb.png', x=0, y=0) # Aqui passamos a imagem template para o PDF e as coordenadas para a imagem cobrir a pagina

# Para escrevermos no pdf totas as variaveis precisam ser str
pdf.text(115, 145, descricao_projeto)
pdf.text(115, 160, horas)
pdf.text(115, 175, valor)
pdf.text(115, 190, prazo_projeto)
pdf.text(115, 205, total_str)

pdf.output('Orçamento.pdf')
print('Orçamento gerado com sucesso!')