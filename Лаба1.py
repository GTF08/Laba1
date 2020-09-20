import math

def GetQuality(value):
    if value ==0:
        return 'Информационный {0}'.format(value)
    elif 0.1<=value<=3.9:
        return 'Низкий {0}'.format(value)
    elif 4.0<=value<=6.9:
        return 'Средний {0}'.format(value)
    elif 7.0<=value<=8.9:
        return 'Высокий {0}'.format(value)
    elif 9.0 <= value <= 10:
        return 'Критический {0}'.format(value)

def BaseScore(C,I,A,S,AV,AC,PR,UI):
    ImpBase = 1-((1-C)*(1-I)*(1-A))
    Exp = 8.22*AV*AC*PR*UI
    
    if S==0:
        Impact = 6.42*ImpBase
        returnValue = math.ceil(min((Impact + Exp),10)*10)/10
    else:
        Impact = 7.52 * (ImpBase-0.029)-3.25*pow((ImpBase-0.02),15)
        returnValue = math.ceil(min(1.08*(Impact + Exp),10)*10)/10
    if Impact <=0:
        return 0
    else: return returnValue

def TempScore(BaseScore, E, RL, RC):
    return math.ceil(BaseScore * E * RL * RC * 10)/10

def EnvScore(MC,MI,MA,MS,MAV,MAC,MPR,MUI,E,RL,RC,CR,IR,AR):
    MImpBase = min(1-((1-MC*CR)*(1-MI*IR)*(1-MA*AR)),0.915)
    MExp = 8.22*MAV*MAC*MPR*MUI
    
    if MS==0:
        MImpact = 6.42*MImpBase
        returnValue = math.ceil(math.ceil(min((MImpact + MExp),10)*10)/10 * E * RL * RC * 10)/10
    else:
        MImpact = 7.52 * (MImpBase-0.029)-3.25*pow((MImpBase-0.02),15)
        returnValue = math.ceil(math.ceil(min(1.08*(MImpact + MExp),10)*10)/10 * E * RL * RC * 10)/10
    if MImpact <=0:
        return 0
    else: return returnValue


def GetValueFromDictByChar(Dict, Char):
    while(Dict.get(Char)== None):
        Char = input('''Неверное значение, введите снова
''')
    return Dict.get(Char)
    
    

def Dialogue():
    SDict = dict(U = 0, C = 1)
  
    S = GetValueFromDictByChar(SDict,input('''Введите уровень влияния на другие компоненты системы S
                        U - Не оказывает
                        C - Оказывает
'''))
    
        
    valuesDict = dict(AV = dict(N = 0.85, A = 0.62, L = 0.55, P = 0.2),
                      AC = dict(L = 0.77, H = 0.44),
                      PR = dict(N = 0.85, L = 0.62 if S == 0 else 0.68, H = 0.27 if S ==0 else 0.5),
                      UI = dict(N = 0.85, R = 0.62),
                      CIA = dict(N = 0.0, L = 0.22, H = 0.56),

                      E = dict(X = 1.0, U = 0.91, P = 0.94, F = 0.97, H = 1.0),
                      RL = dict(X = 1.0, O = 0.95, T = 0.96, W = 0.97, U = 1.0),
                      RC = dict(X = 1.0, U = 0.92, R = 0.96, C = 1.0),
                      
                      CRCICA = dict(X = 1.0, H = 1.5, M = 1.0, L = 0.5))

#################BASE SCORE ##############################      
    AV = GetValueFromDictByChar(valuesDict.get('AV'),input('''Введите уровень вектора атаки AV
                        P - Физический
                        L - Локальный
                        A - Смежная сеть
                        N - Сетевой
'''))
    
    AC = GetValueFromDictByChar(valuesDict.get('AC'),input('''Введите уровень сложности атаки AC
                        L - Низкий
                        H - Высокий
'''))


    PR = GetValueFromDictByChar(valuesDict.get('PR'),input('''Введите уровень привелегий PR
                        N - Не требуется
                        L - Низкий
                        H - Высокий
'''))


    UI = GetValueFromDictByChar(valuesDict.get('UI'),input('''Введите уровень взаимодейтсвия с пользователем UI
                        N - Не требуется
                        R - Требуется
''')) 

    C = GetValueFromDictByChar(valuesDict.get('CIA'),input('''Введите уровень влияния на конфиденциальность C
                        N - Не оказывает
                        L - Низкий
                        H - Высокий
'''))

    I = GetValueFromDictByChar(valuesDict.get('CIA'),input('''Введите уровень влияния на целостность I
                        N - Не оказывает
                        L - Низкий
                        H - Высокий
'''))


    A = GetValueFromDictByChar(valuesDict.get('CIA'),input('''Введите уровень влияния на доступность A
                        N - Не оказывает
                        L - Низкий
                        H - Высокий
'''))
##################### TEMP SCORE #################
    E = GetValueFromDictByChar(valuesDict.get('E'),input('''Введите уровень доступности средств эксплуатации E
                        X - Не определен
                        U - Недостоверен
                        P - Доказательство концепции
                        F - Конструктивный
                        H - Высокий
'''))

    RL = GetValueFromDictByChar(valuesDict.get('RL'),input('''Введите уровень исправления RL
                        X - Не определен
                        O - Официальное исправление
                        T - Временное исправление
                        W - Обходным путем
                        U - Недоступный
'''))

    RC = GetValueFromDictByChar(valuesDict.get('RC'),input('''Введите степень достоверности источника RC
                        X - Не определен
                        U - Неизвестен
                        R - Умеренный
                        C - Подтвержденный
'''))

###################### ENV SCORE ########################
    MSDict = dict(X = S, U = 0, C = 1)
    MS = GetValueFromDictByChar(MSDict,input('''Введите cкорректированный уровень влияния на другие компоненты системы MS
                        X - Не определен
                        U - Не оказывает
                        C - Оказывает
'''))
    
    envDicts = dict(MAV = dict(X = AV, N = 0.85, A = 0.62, L = 0.55, P = 0.2),
                    MAC = dict(X = AC, L = 0.77, H = 0.44),
                    MPR = dict(X = PR, N = 0.85, L = 0.62 if MS == 0 else 0.68, H = 0.27 if MS ==0 else 0.5),
                    MUI = dict(X = UI, N = 0.85, R = 0.62),
                    MC = dict(X = C, N = 0.0, L = 0.22, H = 0.56),
                    MI = dict(X = I, N = 0.0, L = 0.22, H = 0.56),
                    MA = dict(X = A, N = 0.0, L = 0.22, H = 0.56),
                    CRIRAR = dict(X = 1.0, H = 1.5, M = 1.0, L = 0.5))

    MAV = GetValueFromDictByChar(envDicts.get('MAV'),input('''Введите cкорректированный уровень вектора атаки MAV
                        X - Неопределен
                        P - Физический
                        L - Локальный
                        A - Смежная сеть
                        N - Сетевой
'''))
    
    MAC = GetValueFromDictByChar(envDicts.get('MAC'),input('''Введите cкорректированный уровень сложности атаки MAC
                        X - Неопределен
                        L - Низкий
                        H - Высокий
'''))


    MPR = GetValueFromDictByChar(envDicts.get('MPR'),input('''Введите cкорректированный уровень привелегий MPR
                        X - Неопределен
                        N - Не требуется
                        L - Низкий
                        H - Высокий
'''))


    MUI = GetValueFromDictByChar(envDicts.get('MUI'),input('''Введите cкорректированный уровень взаимодейтсвия MUI с пользователем
                        X - Неопределен
                        N - Не требуется
                        R - Требуется
''')) 

    MC = GetValueFromDictByChar(envDicts.get('MC'),input('''Введите cкорректированный уровень влияния на конфиденциальность MC
                        X - Неопределен
                        N - Не оказывает
                        L - Низкий
                        H - Высокий
'''))

    MI = GetValueFromDictByChar(envDicts.get('MI'),input('''Введите cкорректированный уровень влияния на целостность MI
                        X - Неопределен
                        N - Не оказывает
                        L - Низкий
                        H - Высокий
'''))


    MA = GetValueFromDictByChar(envDicts.get('MA'),input('''Введите cкорректированный уровень влияния на доступность MA
                        X - Неопределен
                        N - Не оказывает
                        L - Низкий
                        H - Высокий
'''))

    CR = GetValueFromDictByChar(envDicts.get('CRIRAR'),input('''Введите cкорректированный уровень требований к конфиденциальности CR
                        X - Неопределен
                        L - Низкий
                        M - Средний
                        H - Высокий
'''))

    IR = GetValueFromDictByChar(envDicts.get('CRIRAR'),input('''Введите cкорректированный уровень требований к целостности IR
                        X - Неопределен
                        L - Низкий
                        M - Средний
                        H - Высокий
'''))

    AR = GetValueFromDictByChar(envDicts.get('CRIRAR'),input('''Введите cкорректированный уровень требований к доступности AR
                        X - Неопределен
                        L - Низкий
                        M - Средний
                        H - Высокий
'''))
    
    
    print(GetQuality(BaseScore(C,I,A,S,AV,AC,PR,UI)))
    print(GetQuality(TempScore(BaseScore(C,I,A,S,AV,AC,PR,UI),E,RL,RC)))
    print(GetQuality(EnvScore(MC,MI,MA,MS,MAV,MAC,MPR,MUI,E,RL,RC,CR,IR,AR)))

Dialogue()



