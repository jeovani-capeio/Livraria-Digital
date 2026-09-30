class Trimestre:#O trimestre vai ser criado logo que for instânciado o aluno, mas sem valor algum, apenas o numero do trimestre. Nele vai ser possivel atribuir notas as disciplinas do Aluno de acordo o trimmestre
    #lista_disciplinas=list()
    #PROBLEMA: esta lista estava definida ao nível da CLASSE (fora do __init__), por isso é
    #PARTILHADA por todos os trimestres de todos os alunos - confirmei com um teste: o trimestre
    #de um aluno ficava com as disciplinas de outro aluno, só porque ambos são "Trimestre".
    #Passa a ser criada dentro do __init__, uma lista nova e independente por cada trimestre.
    def __init__(self,numero="1"):
        self.numero=numero
        self.notas=list()
        self.lista_disciplinas=list()#Agora é um atributo de instância, próprio de cada trimestre/aluno.
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self,num):
        if num.strip().isdigit():
            self._numero=int(num)
            return
        raise ValueError("Trimestre deve ter apenas valores númericos")
        
    def add_disciplina_aluno(self,disciplina):#Depois de já ter atribuido o curso ao aluno, vai ser retirado as disciplinas(nome) que o mesmo dispõe, e sera guardado numa lista.
        self.lista_disciplinas.append(disciplina)
        
    def adicionar_notas_disciplina(self,nome_disciplina,nota_mac,nota_professor,nota_trimestral):
        #Vai permitir adicionar notas a cada disciplina.
        #Vai criar um dicionario que vai conter o nome da disciplina e as notas atribuidas, tudo isso apenas no trimestre em questão. 
        #O dicionario séra posto numa lista(self.notas) que vai armazenar todas as notas de todas as disciplinas
        #if nome_disciplina not in self.lista_disciplinas:
        #    raise Exception("Disciplina não encontrada")
        #PROBLEMA: 'nome_disciplina' é uma string, mas 'self.lista_disciplinas' guarda os objectos
        #Disciplina inteiros (é o que add_disciplina_aluno() recebe e guarda). Uma string nunca é
        #igual a um objecto Disciplina, por isso o 'in' dava sempre False - a função rebentava
        #sempre com "Disciplina não encontrada", mesmo quando a disciplina existia de facto.
        #Comparo agora o nome de cada disciplina guardada (disci.nome) com o nome recebido.
        if not any(disci.nome==nome_disciplina for disci in self.lista_disciplinas):
            raise Exception("Disciplina não encontrada")
        for a in self.notas:
            if nome_disciplina == a["Disciplina"]:
                return False
        media=(nota_mac+nota_professor+nota_trimestral)/3
        dicionario={"Disciplina":nome_disciplina,"MAC":nota_mac,"Professor":nota_professor,"Trimestral":nota_trimestral,"Media":media}
        self.notas.append(dicionario)
        return True
        
    def retornar_notas(self):#Vai retornar a lista de notas
        return self.notas
