# conversao_xlsx_csv_p_sql
CONVERSOR AUTOMÁTICO EXCEL PARA CSV
"""
Autor: agnaldo_bi
Data: 2026
Uso: Conversão diária de planilhas para importação no MySQL
"""

import pandas as pd
import os
import time

# ============= CONFIGURAÇÃO =============
# Caminho do arquivo original
CAMINHO_EXCEL = r"Y:\abc\- abc\abc Ano x Ano\2026.xlsx"

# Pasta de destino
CAMINHO_SAIDA = r"C:\abc\abc\abc\abc\CProjetos_BI\BI_CSV_COMERCIAL\CONVERTIDOS"

# NOME FIXO DO ARQUIVO (Altere aqui se desejar outro nome)
NOME_ARQUIVO_FIXO = "faturamento_atualizado.csv"
# ========================================

def verificar_dependencias():
    """Verifica se todas bibliotecas estão instaladas"""
    try:
        import pandas
        import openpyxl
        return True
    except ImportError:
        print("\n❌ Bibliotecas faltando! Instale com: pip install pandas openpyxl")
        return False

def criar_pasta_saida():
    """Cria pasta para os arquivos convertidos"""
    if not os.path.exists(CAMINHO_SAIDA):
        os.makedirs(CAMINHO_SAIDA)
    return CAMINHO_SAIDA

def converter_excel():
    """Função principal de conversão com nome fixo"""
    print("=" * 60)
    print("🎯 CONVERSOR EXCEL → CSV (MODO SUBSTITUIÇÃO)")
    print("=" * 60)
    
   if not verificar_dependencias():
    return
    
   pasta_saida = criar_pasta_saida()
    
   # DEFINIÇÃO DO CAMINHO FIXO (Removemos a data/hora do nome)
  caminho_csv = os.path.join(pasta_saida, NOME_ARQUIVO_FIXO)
    
  print(f"\n📂 Arquivo Excel: {CAMINHO_EXCEL}")
   print(f"💾 Saída CSV (Fixo): {caminho_csv}")
   print("-" * 60)
    
  try:
        inicio = time.time()
        
  print("🔍 Lendo arquivo Excel...")
        df = pd.read_excel(CAMINHO_EXCEL, engine='openpyxl')
        
  print(f"✅ Leitura concluída! Linhas: {len(df):,}")
        
  print(f"💾 Salvando/Substituindo: {NOME_ARQUIVO_FIXO}...")
        # Ao usar o mesmo nome, o pandas sobrescreve o arquivo existente automaticamente
        df.to_csv(caminho_csv, index=False, encoding='utf-8-sig')
        
 tempo_total = time.time() - inicio
        
 print(f"\n🎉 ATUALIZAÇÃO CONCLUÍDA!")
       print(f"⏱️  Tempo: {tempo_total:.2f} segundos")
       print(f"📍 O arquivo antigo foi substituído pela versão mais recente.")
            
 except Exception as e:
        print(f"\n❌ ERRO: {str(e)}")

 def menu_principal():
    """Menu interativo"""
    while True:
        print("\n" + "=" * 60)
        print("📊 MENU CONVERSOR (ARQUIVO ÚNICO)")
        print("=" * 60)
        print("1. 🔄 Atualizar arquivo CSV")
        print("2. ⚙️  Configurar caminhos")
        print("3. 📂 Abrir pasta de saída")
        print("4. ❌ Sair")
        
  opcao = input("\nEscolha uma opção (1-4): ").strip()
        
  if opcao == "1":
            converter_excel()
        elif opcao == "2":
            configurar_caminhos()
        elif opcao == "3":
            if os.path.exists(CAMINHO_SAIDA):
                os.startfile(CAMINHO_SAIDA)
        elif opcao == "4":
            print("\n👋 Até logo!")
            break

def configurar_caminhos():
    """Permite editar os caminhos"""
    global CAMINHO_EXCEL, CAMINHO_SAIDA
    print("\n⚙️  CONFIGURAÇÃO")
    novo_excel = input(f"Novo caminho Excel (Enter mantém):\n{CAMINHO_EXCEL}\n> ").strip()
    if novo_excel: CAMINHO_EXCEL = novo_excel
    
novo_saida = input(f"Nova pasta saída (Enter mantém):\n{CAMINHO_SAIDA}\n> ").strip()
    if novo_saida: CAMINHO_SAIDA = novo_saida

if __name__ == "__main__":
    try:
        menu_principal()
    except Exception as e:
        print(f"\n❌ ERRO CRÍTICO: {e}")
    input("\nPressione Enter para sair...")


    
