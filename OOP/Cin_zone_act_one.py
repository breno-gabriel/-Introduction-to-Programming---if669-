class Ourico:
    def __init__(self, aneis, esmeraldas, escudo, morte, super_sonic):
        self.aneis = aneis 
        self.esmeraldas = esmeraldas
        self.escudo = escudo 
        self.morte = morte
        self.super_sonic = super_sonic

    def coletar_aneis(self, aneis_coletados):
        self.aneis += aneis_coletados

    def perda_aneis(self):
        self.aneis = 0 

    def coletar_escudo(self):
        self.escudo = True 

    def quebrar_escudo(self):
        self.escudo = False 

    def coletar_esmeralda(self):
        self.esmeraldas += 1 

    def morte_sonic(self):
        self.morte = True

    def transformacao(self):
        self.super_sonic = True 

    @property
    def mostrar_status(self):
        return self.morte

    @property
    def transformar(self):
        return self.super_sonic

    @property
    def qnt_aneis(self):
        return self.aneis

    @property
    def qnt_esmeraldas(self):
        return self.esmeraldas

    @property
    def presenca_escudo(self):
        return self.escudo

sonic = Ourico(0, 0 , False, False, False)

fim_laco = False

while not fim_laco:
    comando = input()
    
    if comando == 'aneis':
        num_aneis = int(input())
        sonic.coletar_aneis(num_aneis)
        print(f'Sonic esta agora com {sonic.qnt_aneis} aneis! Gotta go fast!!!')
    elif comando == 'escudo':
        if sonic.presenca_escudo:
            print('Sonic ja esta equipado com uma protecao extra!!!')
        else:
            sonic.coletar_escudo()
            print("Sonic esta agora com uma camada a mais de protecao!!! Let's go!!!")
    elif comando == 'esmeralda':
        sonic.coletar_esmeralda()
        if sonic.qnt_esmeraldas <= 6:
            print(f'Sonic ainda precisa encontrar mais {7 - sonic.qnt_esmeraldas} esmeraldas!!!')
        elif sonic.qnt_esmeraldas == 7:
            print(f'Sonic acabou de encontrar a esmeralda que faltava!!!')
        else:
            print('Sonic ja possui todas as esmeraldas!!!')
    elif comando == 'dano':
        print('Maldito robo do Eggman!!! Este sera seu fim, bigodudo!!!')
        if sonic.presenca_escudo:
            sonic.quebrar_escudo()
        else:
            if sonic.qnt_aneis == 0:
                fim_laco = True 
                print('Infelizmente, nosso heroi nao conseguiu correr o bastante para derrotar seu nemesis...')
            else:
                sonic.perda_aneis()
    
    if sonic.qnt_aneis >= 50 and sonic.qnt_esmeraldas >= 7:
        fim_laco = True 
        print('Com o poder das esmeraldas do caos, Super Sonic conseguiu deter os planos malignos do Dr. Robotinik!!!')



    