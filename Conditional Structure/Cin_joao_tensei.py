meus_pontos_vida = int(input())
meu_ataque = int(input())
minha_defesa = int(input())
minha_fraqueza = input()
minha_resistencia = input()
nome_entidade = input()
pontos_vida_entidade = int(input())
ataque_entidade = int(input())
defesa_entidade = int(input())
fraqueza_entidade = input()
resistencia_entidade = input()
ataque_primeiro_turno = input()
ataque_segundo_turno = 0
ataque_terceiro_turno = 0
critico = 0

if ataque_primeiro_turno == 'Ataque Físico':
    dano_geral = int(meu_ataque - defesa_entidade)
    pontos_vida_entidade -= dano_geral
    if pontos_vida_entidade <= 0:
        pontos_vida_entidade = 0
        print('Turno: 1')
        print(f'São João usou {ataque_primeiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
        print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
    else:
        print('Turno: 1')
        print(f'São João usou {ataque_primeiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')

if ataque_primeiro_turno == 'Agi':
    if fraqueza_entidade == 'fogo':
        critico = 1
        dano_geral = int(meu_ataque - defesa_entidade)
        dano_geral += dano_geral * 0.7
        pontos_vida_entidade -= int(dano_geral)
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 1')
            print(f'Isso! São João usou {ataque_primeiro_turno} e acertou a fraqueza do adversário! A magia causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 1')
            print(f'Isso! São João usou {ataque_primeiro_turno} e acertou a fraqueza do adversário! A magia causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
    elif resistencia_entidade == 'fogo':
        critico = 0
        dano_geral = int(meu_ataque - defesa_entidade)
        dano_geral -= dano_geral * 0.5
        pontos_vida_entidade -= int(dano_geral)
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno}, mas acertou uma resistência, portanto causou apenas {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno}, mas acertou uma resistência, portanto causou apenas {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
    elif resistencia_entidade == 'nao tem' or fraqueza_entidade == 'nao tem':
        critico = 0
        dano_geral = int(meu_ataque - defesa_entidade)
        pontos_vida_entidade -= dano_geral
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
    elif fraqueza_entidade != 'fogo':
        dano_geral = meu_ataque - defesa_entidade
        pontos_vida_entidade -= dano_geral
        critico = 0
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
    elif resistencia_entidade != 'fogo':
        dano_geral = meu_ataque - defesa_entidade
        pontos_vida_entidade -= dano_geral
        critico = 0
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')

if ataque_primeiro_turno == 'Bufu':
    if fraqueza_entidade == 'gelo':
        critico = 1
        dano_geral = int(meu_ataque - defesa_entidade)
        dano_geral += dano_geral * 0.7
        pontos_vida_entidade -= int(dano_geral)
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 1')
            print(f'Isso! São João usou {ataque_primeiro_turno} e acertou a fraqueza do adversário! A magia causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 1')
            print(f'Isso! São João usou {ataque_primeiro_turno} e acertou a fraqueza do adversário! A magia causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
    elif resistencia_entidade == 'gelo':
        critico = 0
        dano_geral = int(meu_ataque - defesa_entidade)
        dano_geral -= dano_geral * 0.5
        pontos_vida_entidade -= int(dano_geral)
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno}, mas acertou uma resistência, portanto causou apenas {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno}, mas acertou uma resistência, portanto causou apenas {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
    elif resistencia_entidade == 'nao tem' or fraqueza_entidade == 'nao tem':
        critico = 0
        dano_geral = int(meu_ataque - defesa_entidade)
        pontos_vida_entidade -= dano_geral
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
    elif fraqueza_entidade != 'fogo':
        dano_geral = meu_ataque - defesa_entidade
        pontos_vida_entidade -= dano_geral
        critico = 0
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
    elif resistencia_entidade != 'fogo':
        dano_geral = meu_ataque - defesa_entidade
        pontos_vida_entidade -= dano_geral
        critico = 0
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')

if ataque_primeiro_turno == 'Zio':
    if fraqueza_entidade == 'eletricidade':
        critico = 1
        dano_geral = int(meu_ataque - defesa_entidade)
        dano_geral += dano_geral * 0.7
        pontos_vida_entidade -= int(dano_geral)
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 1')
            print(f'Isso! São João usou {ataque_primeiro_turno} e acertou a fraqueza do adversário! A magia causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 1')
            print(f'Isso! São João usou {ataque_primeiro_turno} e acertou a fraqueza do adversário! A magia causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
    elif resistencia_entidade == 'eletricidade':
        critico = 0
        dano_geral = int(meu_ataque - defesa_entidade)
        dano_geral -= dano_geral * 0.5
        pontos_vida_entidade -= int(dano_geral)
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno}, mas acertou uma resistência, portanto causou apenas {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno}, mas acertou uma resistência, portanto causou apenas {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
    elif resistencia_entidade == 'nao tem' or fraqueza_entidade == 'nao tem':
        critico = 0
        dano_geral = int(meu_ataque - defesa_entidade)
        pontos_vida_entidade -= int(dano_geral)
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
    elif fraqueza_entidade != 'fogo':
        dano_geral = meu_ataque - defesa_entidade
        pontos_vida_entidade -= dano_geral
        critico = 0
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
    elif resistencia_entidade != 'fogo':
        dano_geral = meu_ataque - defesa_entidade
        pontos_vida_entidade -= dano_geral
        critico = 0
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 1')
            print(f'São João usou {ataque_primeiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')

if critico == 1 and pontos_vida_entidade > 0:
    print('Turno: 2')
    print(f'{nome_entidade} teve sua fraqueza em {fraqueza_entidade} acertada, portanto não poderá agir.')
elif critico == 0 and pontos_vida_entidade > 0:
    ataque_segundo_turno = input()

critico = 0

if ataque_segundo_turno == 'Ataque Físico':
    critico = 0
    dano_geral = int(ataque_entidade - minha_defesa)
    meus_pontos_vida -= dano_geral
    if meus_pontos_vida <= 0:
        meus_pontos_vida = 0
        print('Turno: 2')
        print(f'{nome_entidade} usou {ataque_segundo_turno} e causou {dano_geral:.0f} de dano em São João que agora tem {meus_pontos_vida} de vida.')
        print(f'Morremos… Parece que {nome_entidade} tem mais chances de ascender ao trono da Midsommar…')
    else:
        print('Turno: 2')
        print(f'{nome_entidade} usou {ataque_segundo_turno} e causou {dano_geral:.0f} de dano em São João que agora tem {meus_pontos_vida} de vida.')

if ataque_segundo_turno == 'Agi':
    if minha_fraqueza == 'fogo':
        critico = 1
        dano_geral = int(ataque_entidade - minha_defesa)
        dano_geral += dano_geral * 0.7
        meus_pontos_vida -= int(dano_geral)
        if meus_pontos_vida <= 0:
            meus_pontos_vida = 0
            print('Turno: 2')
            print(f'Vixe! {nome_entidade} usou {ataque_segundo_turno} e acertou sua fraqueza! A magia causou {dano_geral:.0f} de dano em São João que agora tem {meus_pontos_vida} de vida.')
            print(f'Morremos… Parece que {nome_entidade} tem mais chances de ascender ao trono da Midsommar…')
        else:
            print('Turno: 2')
            print(f'Vixe! {nome_entidade} usou {ataque_segundo_turno} e acertou sua fraqueza! A magia causou {dano_geral:.0f} de dano em São João que agora tem {meus_pontos_vida} de vida.')
    elif minha_resistencia == 'fogo':
        critico = 0
        dano_geral = int(ataque_entidade - minha_defesa)
        dano_geral -= dano_geral * 0.5
        meus_pontos_vida -= int(dano_geral)
        if meus_pontos_vida <= 0:
            meus_pontos_vida = 0
            print('Turno: 2')
            print(f'{nome_entidade} usou {ataque_segundo_turno}, mas acertou uma resistência, portanto causou apenas {dano_geral:.0f} de dano em São João que agora tem {meus_pontos_vida} de vida.')
            print(f'Morremos… Parece que {nome_entidade} tem mais chances de ascender ao trono da Midsommar…')
        else:
            print('Turno: 2')
            print(f'{nome_entidade} usou {ataque_segundo_turno}, mas acertou uma resistência, portanto causou apenas {dano_geral:.0f} de dano em São João que agora tem {meus_pontos_vida} de vida.')
    elif minha_resistencia == 'nao tem' or minha_resistencia == 'nao tem':
        critico = 0
        dano_geral = int(ataque_entidade - minha_defesa)
        meus_pontos_vida -= int(dano_geral)
        if meus_pontos_vida <= 0:
            meus_pontos_vida = 0
            print('Turno: 2')
            print(f'{nome_entidade} usou {ataque_segundo_turno} e causou {dano_geral:.0f} de dano em São João que agora tem {meus_pontos_vida} de vida.')
            print(f'Morremos… Parece que {nome_entidade} tem mais chances de ascender ao trono da Midsommar…')
        else:
            print('Turno: 2')
            print(f'{nome_entidade} usou {ataque_segundo_turno} e causou {dano_geral:.0f} de dano em São João que agora tem {meus_pontos_vida} de vida.')

if ataque_segundo_turno == 'Bufu':
    if minha_fraqueza == 'gelo':
        critico = 1
        dano_geral = int(ataque_entidade - minha_defesa)
        dano_geral += dano_geral * 0.7
        meus_pontos_vida -= int(dano_geral)
        if meus_pontos_vida <= 0:
            meus_pontos_vida = 0
            print('Turno: 2')
            print(f'Vixe! {nome_entidade} usou {ataque_segundo_turno} e acertou sua fraqueza! A magia causou {dano_geral:.0f} de dano em São João que agora tem {meus_pontos_vida} de vida.')
            print(f'Morremos… Parece que {nome_entidade} tem mais chances de ascender ao trono da Midsommar…')
        else:
            print('Turno: 2')
            print(f'Vixe! {nome_entidade} usou {ataque_segundo_turno} e acertou sua fraqueza! A magia causou {dano_geral:.0f} de dano em São João que agora tem {meus_pontos_vida} de vida.')
    elif minha_resistencia == 'gelo':
        critico = 0
        dano_geral = int(ataque_entidade - minha_defesa)
        dano_geral -= dano_geral * 0.5
        meus_pontos_vida -= int(dano_geral)
        if meus_pontos_vida <= 0:
            meus_pontos_vida = 0
            print('Turno: 2')
            print(f'{nome_entidade} usou {ataque_segundo_turno}, mas acertou uma resistência, portanto causou apenas {dano_geral:.0f} de dano em São João que agora tem {pontos_vida_entidade} de vida.')
            print(f'Morremos… Parece que {nome_entidade} tem mais chances de ascender ao trono da Midsommar…')
        else:
            print('Turno: 2')
            print(f'{nome_entidade} usou {ataque_segundo_turno}, mas acertou uma resistência, portanto causou apenas {dano_geral:.0f} de dano em São João que agora tem {pontos_vida_entidade} de vida.')
    elif minha_resistencia == 'nao tem' or minha_resistencia == 'nao tem':
        critico = 0
        dano_geral = int(ataque_entidade - minha_defesa)
        meus_pontos_vida -= dano_geral
        if meus_pontos_vida <= 0:
            meus_pontos_vida = 0
            print('Turno: 2')
            print(f'{nome_entidade} usou {ataque_segundo_turno} e causou {dano_geral:.0f} de dano em São João que agora tem {meus_pontos_vida} de vida.')
            print(f'Morremos… Parece que {nome_entidade} tem mais chances de ascender ao trono da Midsommar…')
        else:
            print('Turno: 2')
            print(f'{nome_entidade} usou {ataque_segundo_turno} e causou {dano_geral:.0f} de dano em São João que agora tem {meus_pontos_vida} de vida.')

if ataque_segundo_turno == 'Zio':
    if minha_fraqueza == 'eletricidade':
        critico = 1
        dano_geral = int(ataque_entidade - minha_defesa)
        dano_geral += dano_geral * 0.7
        meus_pontos_vida -= int(dano_geral)
        if meus_pontos_vida <= 0:
            meus_pontos_vida = 0
            print('Turno: 2')
            print(f'Vixe! {nome_entidade} usou {ataque_segundo_turno} e acertou sua fraqueza! A magia causou {dano_geral:.0f} de dano em São João que agora tem {meus_pontos_vida} de vida.')
            print(f'Morremos… Parece que {nome_entidade} tem mais chances de ascender ao trono da Midsommar…')
        else:
            print('Turno: 2')
            print(f'Vixe! {nome_entidade} usou {ataque_segundo_turno} e acertou sua fraqueza! A magia causou {dano_geral:.0f} de dano em São João que agora tem {meus_pontos_vida} de vida.')
    elif minha_resistencia == 'eletricidade':
        critico = 0
        dano_geral = int(ataque_entidade - minha_defesa)
        dano_geral -= dano_geral * 0.5
        meus_pontos_vida -= int(dano_geral)
        if meus_pontos_vida <= 0:
            meus_pontos_vida = 0
            print('Turno: 2')
            print(f'{nome_entidade} usou {ataque_segundo_turno}, mas acertou uma resistência, portanto causou apenas {dano_geral:.0f} de dano em São João que agora tem {pontos_vida_entidade} de vida.')
            print(f'Morremos… Parece que {nome_entidade} tem mais chances de ascender ao trono da Midsommar…')
        else:
            print('Turno: 2')
            print(f'{nome_entidade} usou {ataque_segundo_turno}, mas acertou uma resistência, portanto causou apenas {dano_geral:.0f} de dano em São João que agora tem {pontos_vida_entidade} de vida.')
    elif minha_resistencia == 'nao tem' or minha_resistencia == 'nao tem':
        critico = 0
        dano_geral = int(ataque_entidade - minha_defesa)
        meus_pontos_vida -= dano_geral
        if meus_pontos_vida <= 0:
            meus_pontos_vida = 0
            print('Turno: 2')
            print(f'{nome_entidade} usou {ataque_segundo_turno} e causou {dano_geral:.0f} de dano em São João que agora tem {meus_pontos_vida} de vida.')
            print(f'Morremos… Parece que {nome_entidade} tem mais chances de ascender ao trono da Midsommar…')
        else:
            print('Turno: 2')
            print(f'{nome_entidade} usou {ataque_segundo_turno} e causou {dano_geral:.0f} de dano em São João que agora tem {meus_pontos_vida} de vida.')


if critico == 1 and meus_pontos_vida > 0:
    print('Turno: 3')
    print(f'São João teve sua fraqueza em {minha_fraqueza} acertada, portanto não poderá agir.')
elif critico == 0 and meus_pontos_vida > 0 and pontos_vida_entidade > 0:
    ataque_terceiro_turno = input()


if ataque_terceiro_turno == 'Ataque Físico':
    dano_geral = int(meu_ataque - defesa_entidade)
    pontos_vida_entidade -= dano_geral
    if pontos_vida_entidade <= 0:
        pontos_vida_entidade = 0
        print('Turno: 3')
        print(f'São João usou {ataque_terceiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
        print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
    else:
        print('Turno: 3')
        print(f'São João usou {ataque_terceiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')

if ataque_terceiro_turno == 'Agi':
    if fraqueza_entidade == 'fogo':
        critico = 1
        dano_geral = int(meu_ataque - defesa_entidade)
        dano_geral += dano_geral * 0.7
        pontos_vida_entidade -= int(dano_geral)
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 3')
            print(f'Isso! São João usou {ataque_terceiro_turno} e acertou a fraqueza do adversário! A magia causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 3')
            print(f'Isso! São João usou {ataque_terceiro_turno} e acertou a fraqueza do adversário! A magia causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
    elif resistencia_entidade == 'fogo':
        critico = 0
        dano_geral = int(meu_ataque - defesa_entidade)
        dano_geral -= dano_geral * 0.5
        pontos_vida_entidade -= int(dano_geral)
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 3')
            print(f'São João usou {ataque_terceiro_turno}, mas acertou uma resistência, portanto causou apenas {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 3')
            print(f'São João usou {ataque_terceiro_turno}, mas acertou uma resistência, portanto causou apenas {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
    elif resistencia_entidade == 'nao tem' or fraqueza_entidade == 'nao tem':
        critico = 0
        dano_geral = int(meu_ataque - defesa_entidade)
        pontos_vida_entidade -= dano_geral
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 3')
            print(f'São João usou {ataque_terceiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 3')
            print(f'São João usou {ataque_terceiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')

if ataque_terceiro_turno == 'Bufu':
    if fraqueza_entidade == 'gelo':
        critico = 1
        dano_geral = int(meu_ataque - defesa_entidade)
        dano_geral += dano_geral * 0.7
        pontos_vida_entidade -= int(dano_geral)
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 3')
            print(f'Isso! São João usou {ataque_terceiro_turno} e acertou a fraqueza do adversário! A magia causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 3')
            print(f'Isso! São João usou {ataque_terceiro_turno} e acertou a fraqueza do adversário! A magia causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
    elif resistencia_entidade == 'gelo':
        critico = 0
        dano_geral = int(meu_ataque - defesa_entidade)
        dano_geral -= dano_geral * 0.5
        pontos_vida_entidade -= int(dano_geral)
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 3')
            print(f'São João usou {ataque_terceiro_turno}, mas acertou uma resistência, portanto causou apenas {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 3')
            print(f'São João usou {ataque_terceiro_turno}, mas acertou uma resistência, portanto causou apenas {int(dano_geral)} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
    elif resistencia_entidade == 'nao tem' or fraqueza_entidade == 'nao tem':
        critico = 0
        dano_geral = int(meu_ataque - defesa_entidade)
        pontos_vida_entidade -= dano_geral
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 3')
            print(f'São João usou {ataque_terceiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 3')
            print(f'São João usou {ataque_terceiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')

if ataque_terceiro_turno == 'Zio':
    if fraqueza_entidade == 'eletricidade':
        critico = 1
        dano_geral = int(meu_ataque - defesa_entidade)
        dano_geral += dano_geral * 0.7
        pontos_vida_entidade -= int(dano_geral)
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 3')
            print(f'Isso! São João usou {ataque_terceiro_turno} e acertou a fraqueza do adversário! A magia causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 3')
            print(f'Isso! São João usou {ataque_terceiro_turno} e acertou a fraqueza do adversário! A magia causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
    elif resistencia_entidade == 'eletricidade':
        critico = 0
        dano_geral = int(meu_ataque - defesa_entidade)
        dano_geral -= dano_geral * 0.5
        pontos_vida_entidade -= int(dano_geral)
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 3')
            print(f'São João usou {ataque_terceiro_turno}, mas acertou uma resistência, portanto causou apenas {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 3')
            print(f'São João usou {ataque_terceiro_turno}, mas acertou uma resistência, portanto causou apenas {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
    elif resistencia_entidade == 'nao tem' or fraqueza_entidade == 'nao tem':
        critico = 0
        dano_geral = int(meu_ataque - defesa_entidade)
        pontos_vida_entidade -= dano_geral
        if pontos_vida_entidade <= 0:
            pontos_vida_entidade = 0
            print('Turno: 3')
            print(f'São João usou {ataque_terceiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        else:
            print('Turno: 3')
            print(f'São João usou {ataque_terceiro_turno} e causou {dano_geral:.0f} de dano em {nome_entidade} que agora tem {pontos_vida_entidade} de vida.')

if meus_pontos_vida > 0 and pontos_vida_entidade > 0:
    print('Ambos ainda sobrevivem. Melhor se retirar e derrotar entidades mais fracas para ficar mais forte…')

