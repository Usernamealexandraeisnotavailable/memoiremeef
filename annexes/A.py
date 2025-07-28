def markovian_language_model (text, prompt=".", n=100) :
   from re import findall
   from numpy import unique, array, zeros, cumsum, searchsorted
   from random import random
   from warnings import filterwarnings
   pattern = r'\w+|[^\w\s]'
   states = findall(pattern, text)
   unique_states = list(unique(states))
   state_index = {state: i for i, state in enumerate(unique_states)}
   transitions = zeros((len(unique_states), len(unique_states)))
   for i in range(len(states) - 1) :
      transitions[state_index[states[i]], state_index[states[i+1]]] += 1
   filterwarnings("ignore")
   transitions /= transitions.sum(axis=1, keepdims=True)
   filterwarnings("default")
   output = [prompt]
   for _ in range(n) :
      current_index = state_index[output[-1]]
      if str(transitions[current_index][0]) == "nan" :
         return output
      if not any(transitions[current_index]) :
         break
      rand = random()
      cumm_prob = cumsum(transitions[current_index])
      next_state = unique_states[searchsorted(cumm_prob, rand)]
      output.append(next_state)
   return ' '.join(output)
