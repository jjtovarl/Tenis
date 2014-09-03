def score():
  """
  Inicio del partido, cuando los marcadores son 0
  Por ejemplo:
  >>> score()
  (0, 0)
  """
  j1 = 0
  j2 = 0
  
  return j1,j2

def score1(j):
  """
  El jugador 1 inicia con el saque y no es interceptado por el jugador 2, entonces anota
  Por ejemplo:
  >>> score1(1)
  (15, 0)
  """
  j1 = 15
  j2 = 0

  return j1,j2

def score2(j):
  """
  El jugador 1 lanza por segunda ocación y no es interceptado por el jugador 2, entonces anota
  Por ejemplo:
  >>> score2(1)
  (30, 0)
  """
  j1 = 30
  j2 = 0

  return j1,j2

def score3(j):
  """
  El jugador 1 lanza por tercera ocación y no es interceptado por el jugador 2, entonces anota
  Por ejemplo:
  >>> score3(1)
  (40, 0)
  """
  j1 = 40
  j2 = 0

  return j1,j2

def score4(j):
  """
  El jugador 1 lanza por cuarta ocación y no es interceptado por el jugador 2, entonces anota
  Por ejemplo:
  >>> score4(1)
  ('wins!', 'loses')
  """
  j1 = 'wins!'
  j2 = 'loses'

  return j1,j2

def score5(j):
  """
  El jugador 1 lanza por primera ocación y es interceptado por el jugador 2, entonces anota jugador 2
  Por ejemplo:
  >>> score5(2)
  (0, 15)
  """
  j1 = 0
  j2 = 15

  return j1,j2

def score6(j):
  """
  El jugador 1 lanza por segunda ocación y no es interceptado por el jugador 2, entonces anota jugador 1
  Por ejemplo:
  >>> score6(1)
  (15, 15)
  """
  j1 = 15
  j2 = 15

  return j1,j2

def score7(j):
  """
  El jugador 1 lanza por tercera ocación y no es interceptado por el jugador 2, entonces anota jugador 1
  Por ejemplo:
  >>> score7(1)
  (30, 15)
  """
  j1 = 30
  j2 = 15

  return j1,j2

def score8(j):
  """
  El jugador 1 lanza por cuarta ocación y es interceptado por el jugador 2, entonces anota jugador 2
  Por ejemplo:
  >>> score8(2)
  (30, 30)
  """
  j1 = 30
  j2 = 30

  return j1,j2

def score9(j):
  """
  El jugador 1 lanza por quinta ocación y es interceptado por el jugador 2, entonces anota jugador 2
  Por ejemplo:
  >>> score9(2)
  (30, 40)
  """
  j1 = 30
  j2 = 40

  return j1,j2

def score10(j):
  """
  El jugador 1 lanza por sexta ocación y no es interceptado por el jugador 2, entonces anota jugador 1
  Por ejemplo:
  >>> score10(1)
  ('deuce', 'deuce')
  """
  j1 = 'deuce'
  j2 = 'deuce'

  return j1,j2

def score11(j):
  """
  El jugador 1 lanza por septima ocación y es interceptado por el jugador 2, entonces anota jugador 2
  Por ejemplo:
  >>> score11(2)
  ('deuce', 'ads')
  """
  j1 = 'deuce'
  j2 = 'ads'

  return j1,j2

def score12(j):
  """
  El jugador 1 lanza por septima ocación y no es interceptado por el jugador 2, entonces anota jugador 1
  Por ejemplo:
  >>> score12(1)
  ('ads', 'ads')
  """
  j1 = 'ads'
  j2 = 'ads'

  return j1,j2

def score13(j):
  """
  El jugador 1 lanza por septima ocación y no es interceptado por el jugador 2, entonces anota jugador 1
  Por ejemplo:
  >>> score13(1)
  ('wins!', 'ads')
  """
  j1 = 'wins!'
  j2 = 'ads'

  return j1,j2

def score14(j):
  """
  El jugador 1 lanza por septima ocación y es interceptado por el jugador 2, entonces anota jugador 2
  Por ejemplo:
  >>> score14(2)
  ('ads', 'wins!')
  """
  j1 = 'ads'
  j2 = 'wins!'

  return j1,j2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
