import time
input("Olá campeão, como é o seu nome?? ")
print(".\n.")
time.sleep(1)
print("\nVamos aprender um pouco mais sobre os relevos?\n")

escolha=input("Você sabe oq é um relevo? (s = sim/n = não)\n")

time.sleep(1)
if escolha == 's':
  print("\nNossa que ótimo..")
elif escolha == 'n':
  print("\nNão? Então vamos ver agora.\nO relevo é o conjunto de formas físicas que compõem a superfície da Terra.")
  print("É onde as transformações geológicas se expressam mais nitidamente, sendo também o local de habitação do ser humano e da maior parte dos animais terrestres.")

print("\n------------------------------------------- ")

time.sleep(2)
print("\nExistem tipos de relevos:\n")

time.sleep(1)

L = ['1. Montanhas','2. Planaltos','3. Planícies','4. Depressão','5. Sair']
for i in range(5):
    print(L [i])
print("\n------------------------------------------- \n")
k = input("Ecolha um e veja sobre ele:\n")

time.sleep(3)

if k == '1':
    print("\n\nEntão você quer saber mais sobre o relevo de Montanhas.\n")
    print(".")
    time.sleep(2)
    print("\n  Montanhas são formas de relevo que apresentam elevações de altitudes superiores em comparação com regiões imediatamente vizinhas.")      
    time.sleep(2)
    print("Alguns autores afirmam que uma elevação no relevo só pode ser considerada como formação montanhosa se possuir mais de 300 metros de altitude \nem relação ao relevo que se encontra ao redor.")
    time.sleep(2)
    print("  Esse tipo de relevo geralmente é caracterizado por ser geologicamente recente, possuindo essa forma mais acidentada \npor ter sofrido por menos tempo a ação dos agentes modeladores da superfície terrestre.\n")
    time.sleep(2)
    print("\nCURIOSIDADES SOBRE MONTANHAS:\n")
    time.sleep(1)
    print("**A parte mais alta de uma montanha é chamada de cume. Já a parte mais baixa, próxima a base da montanha, é conhecida como sopé")
    time.sleep(1)
    print("**2002 foi o Ano Internacional das Montanhas. Foi uma homenagem e campanha, definida pela ONU, de valorização dessa importante forma de relevo.")

elif k == '2':
    print("\n\nEntão você quer saber mais sobre o relevo de Planaltos.\n")
    print(".")
    time.sleep(2)
    print("\n  Algumas vezes chamados de platôs, os planaltos são elevações de relevo que possuem uma extensão um pouco ampla e a partmais alta relativamente plana. \nApresentam, em geral, altitudes medianas, sendo menores que as montanhas e maiores que as planícies.")
    time.sleep(2)
    print("\nEles são classificados conforme a composição predominante de suas rochas, dividindo-se em:")
    time.sleep(2)
    print("\n *Planaltos cristalinos (formados por rochas ígneas intrusivas e metamórficas);\n *Planaltos sedimentares (formados por rochas sedimentares); \n *Planaltos basálticos (formado por rochas ígneas extrusivas).\n")
    time.sleep(2)
    print("\nCURIOSIDADES SOBRE PLANALTOS:\n")
    time.sleep(1)
    print("**Planaltos são formas de relevo que apresentam superfícies mais ou menos planas e geralmente acidentadas e irregulares.")
    time.sleep(1)
    print("**Em suas bordas comumente aparecem elevações de topo plano, como serras.")
    time.sleep(1)
    print("**Esse tipo de relevo encontra-se acima de 300 metros do nível do mar, podendo chegar a mais de 2000 metros de altitude.")

elif k == '3':
    print("\n\nEntão você quer saber mais sobre o relevo de Planícies.\n")
    print(".")
    time.sleep(2)
    print("\n  Planícies são áreas mais ou menos planas e que possuem uma altitude menor em relação às montanhas e aos planaltos.")
    time.sleep(2)
    print("Caracterizam-se pela grande quantidade de sedimentos acumulados em sua superfície, geralmente trazidos pela água das chuvas, \ndos rios ou, no caso das planícies litorâneas, pela água dos oceanos e dos mares.")
    time.sleep(2)
    print("\n  Planície é uma unidade de relevo caracterizada por possuir paisagens geralmente planas, \npouco acidentadas e localizadas em regiões com baixas altitudes, estando geralmente próximas ao nível do mar.\n")
    time.sleep(2)
    print("\nCURIOSIDADE SOBRE PLANÍCIES:\n")
    time.sleep(1)
    print("**As planícies são consideradas formas de relevo em construção, diferentemente dos planaltos, que são considerados relevos em destruição.")
       
elif k == '4':
    print("\n\nEntão você quer saber mais sobreo relevo de Depressão.\n")
    print(".")
    time.sleep(2)
    print("\n  Depressões são unidades de relevo normalmente rebaixadas. \nPossuem altitudes que variam entre 100 m e 500 m e costumam ser classificadas em relativas e absolutas.")
    time.sleep(2)
    print("\n *Depressão relativa (que apresenta altitude mais baixa que as áreas ao redor, mas estão acima do nível do mar);\n *Depressão absoluta (se apresenta abaixo do nível do mar).\n")
    print("  Esse tipo de paisagem é modelado por meio de processos de desgaste provocados por agentes erosivos que modelam o relevo.")
    time.sleep(2)
    print("  Em geral, costuma abranger regiões geologicamente antigas e que, portanto, sofrem bastante com ações de erosão e sedimentação das rochas e dos solos, \no que se revela em sua superfície ligeiramente ondulada.\n")
    time.sleep(2)
    print("\nCURIOSIDADES SOBRE DEPRESSÕES:\n")
    time.sleep(1)
    print("**As depressões no Brasil são originárias de processos erosivos nas bordas das bacias sedimentares.")
    time.sleep(1)
    print("**Durante um certo tempo, essa forma de relevo no Brasil não aparecia nos estudos propostos por pesquisadores.")

           
elif k == '5':
    time.sleep(1)
    print("\n\nEstudos finalizados")

print("\n\n------------------------------------------- \n\n")
