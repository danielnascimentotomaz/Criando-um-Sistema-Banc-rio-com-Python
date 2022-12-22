saldo = 0
limite = 500
LIMITE_SAQUE = 3
numero_saque = 0
extrato = ""
while True:
   print("=================== MENU =======================")
   print("=================================")
   print("DEPÓSITAR------------------- [1]")
   print("SAQUE------------------------[2]")
   print("EXTRATO----------------------[3]")
   print("SAIR-------------------------[4]" )
   print("=================================")


   x = int(input("DIGITE A OPÇÃO: "))
   print("")

   if x == 1:

       valor = float(input("INFORME O VALOR DO DEPÓSITO: "))
       if valor > 0:
           saldo = saldo + valor
           extrato += f'DEPÓSITO: {valor:.2f}\n'
       else:
           print("OPRERAÇÃO FALHOU! VALOR INFORMADO INVÁLIDO.")


   elif x == 2:

           saque = float(input("DIGITE O VALOR PRA SACAR: "))
           excedeu_saldo = saque > saldo
           excedeu_limite = saque > limite
           excedeu_limite_saque = numero_saque >= LIMITE_SAQUE

           if excedeu_saldo:
               print("OPRERAÇÃO FALHOU! VOÇÊ NÃO TEM SALDO SUFICIENTE.")
           elif excedeu_limite:
               print("OPERAÇÃO FALHOU! O VALOR DO SALDO EXCEDE O LIMITE.")

           elif excedeu_limite_saque:
               print("OPERAÇÃO FALHOU! NÚMERO MÁXIMO DE SAQUE DIARIO EXCEDIDO.")

           elif saque > 0:
               saldo = saldo - saque
               numero_saque = numero_saque + 1
               extrato += f"SAQUE: {saque:.2f}\n"

           else:
               print("OPERAÇÃO FALHOU! O VALOR INFORMADO INVALIDO.")



   elif x == 3:

       print("============ EXTRATO ===============")
       if extrato == "":
           print("NAO FOREM REALIZADO MOVIMENTAÇÕES.\n")

       else:
           print(extrato)
       print(f"SEU SALDO É R$ {saldo:.2f} REAIS")
       print("=====================================")


   elif x == 4:
       print("\n===================")
       print("FIM DA OPERAÇÃO")
       print("=====================")
       break


   else:
       print("OPERAÇÃO INVÁLIDA, POR FAVOR SELECIONE NOVAMENTE A OPERAÇÃO DESEJADA.")
