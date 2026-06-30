import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Entradas
atendimento = ctrl.Antecedent(np.arange(0, 11, 1), 'atendimento')
comida = ctrl.Antecedent(np.arange(0, 11, 1), 'comida')
espera = ctrl.Antecedent(np.arange(0, 61, 1), 'espera')

# Saída
gorjeta = ctrl.Consequent(np.arange(0, 26, 1), 'gorjeta')

# Atendimento
atendimento['ruim'] = fuzz.trimf(atendimento.universe, [0,0,5])
atendimento['medio'] = fuzz.trimf(atendimento.universe,[2,5,8])
atendimento['bom'] = fuzz.trimf(atendimento.universe,[5,10,10])

# Comida
comida['ruim'] = fuzz.trimf(comida.universe,[0,0,5])
comida['media'] = fuzz.trimf(comida.universe,[2,5,8])
comida['boa'] = fuzz.trimf(comida.universe,[5,10,10])

# Espera
espera['curta'] = fuzz.trimf(espera.universe,[0,0,20])
espera['media'] = fuzz.trimf(espera.universe,[10,30,50])
espera['longa'] = fuzz.trimf(espera.universe,[40,60,60])

# Gorjeta
gorjeta['baixa'] = fuzz.trimf(gorjeta.universe,[0,0,10])
gorjeta['media'] = fuzz.trimf(gorjeta.universe,[5,12,18])
gorjeta['alta'] = fuzz.trimf(gorjeta.universe,[15,25,25])

rules = [

    ctrl.Rule(atendimento['ruim'], gorjeta['baixa']),

    ctrl.Rule(comida['ruim'], gorjeta['baixa']),

    ctrl.Rule(atendimento['ruim'] & espera['longa'], gorjeta['baixa']),

    ctrl.Rule(atendimento['medio'] & comida['media'], gorjeta['media']),

    ctrl.Rule(atendimento['bom'] & comida['boa'], gorjeta['alta']),

    ctrl.Rule(atendimento['bom'] & comida['media'], gorjeta['media']),

    ctrl.Rule(atendimento['medio'] & comida['boa'], gorjeta['media']),

    ctrl.Rule(atendimento['bom'] & espera['curta'], gorjeta['alta']),

    ctrl.Rule(atendimento['bom'] & comida['boa'] & espera['longa'],gorjeta['media']),

    ctrl.Rule(comida['boa'] & espera['curta'], gorjeta['alta']),

    ctrl.Rule(comida['boa'] & espera['longa'], gorjeta['media']),

    ctrl.Rule(atendimento['bom'] & comida['boa'] & espera['curta'], gorjeta['alta']),

    ctrl.Rule(atendimento['ruim'] & comida['ruim'] & espera['longa'], gorjeta['baixa']),

    ctrl.Rule(atendimento['medio'] & espera['media'], gorjeta['media']),

    ctrl.Rule(comida['ruim'] & espera['longa'], gorjeta['baixa'])

]

# Cria o sistema fuzzy
sistema = ctrl.ControlSystem(rules)