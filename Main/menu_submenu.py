
def pausar():
    input("\nPressione ENTER para continuar...")

def menu_principal():
    opcao = 0
    while opcao !=3:
    

        print("\n╔══════════════════════════════╗")
        print("║          CLINICA PLUS         ║")
        print("╠═══════════════════════════════╣")
        print("║ 1 -        Médico             ║")
        print("║ 2 -       Paciente            ║")
        print("║ 3 -    Finalizar Sistema      ║")
        print("╚═══════════════════════════════╝")
        try:
          opcao = int(input("Opção: "))

        except ValueError:
           print("\nDigite apenas numeros!")
           input("\nPressione ENTER para continuar...")
           continue

        match opcao:
           case 1:
              menu_medico()
              
            
           case 2:
              menu_paciente()
              

           case 3:
              
              print("\n╔═══════════════════════════════╗")
              print("║  Sistema encerrado. Até logo! ║")
              print("╚═══════════════════════════════╝\n")
              
           case _:
              print("Digite alguma das opçoes validas...")
              pausar()


def menu_medico():
   opcao = 0
   while opcao !=5:
      
        print("\n╔══════════════════════════════╗")
        print("║          MENU MEDICO          ║")
        print("╠═══════════════════════════════╣")
        print("║ 1 -   Consultas do dia        ║")
        print("║ 2 -  Pacientes cadastrados    ║")
        print("║ 3 -  Historico de pacientes   ║")
        print("║ 4 -   Remover pacientes       ║")
        print("║ 5 -        Retornar           ║")
        print("╚═══════════════════════════════╝")

        try:
         opcao = int(input("Opção: "))

        except ValueError:
           print("Digite apenas numeros")
           input("Digite ENTER para continuar")
        
        match opcao:
           
           case 1:
              print("Vai ser direcionado para as consultas do dia")

           case 2: 
              print("Vai listar os pacientes cadastrados")

           case 3:
              print("Vai listar o historico dos pacientes")

           case 4:
              print("Vai ir para opção de remover pacientes")

           case 5:
              print("Voltando...")

           case _:
              print("Digite alguma das opçoes validas...")
              pausar()

def menu_paciente():
   opcao = 0
   while opcao !=4:
       
        print("\n╔══════════════════════════════╗")
        print("║         MENU PACIENTE         ║")
        print("╠═══════════════════════════════╣")
        print("║ 1 -    Agendar consulta       ║")
        print("║ 2 -   Medicos disponiveis     ║")
        print("║ 3 -  Historico de consulta    ║")
        print("║ 4 -        Retornar           ║")
        print("╚═══════════════════════════════╝")

        try:
           opcao = int(input("Opção: "))

        except ValueError:
            print("Digite alguma das opçoes validas...")
            input("Digite ENTER para continuar")

        
        match opcao:
           case 1:  
              print("Vai ser direcionado para a area de agendamento")

           case 2:
              print("Vai listar os medicos disponiveis")

           case 3: 
              print("Vai mostrar o historico de consultas do paciente")

           case 4:
              print("Voltando...")
           case _:
              print("Digite alguma das opçoes validas...")
              pausar()
    
menu_principal()

   

            
            


               
            

        

    
